#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""strip_diagrams.py — Remove diagram sections from V6 permanent notes.

Scans permanent notes that have been processed by the diagram pipeline
(``provenance.diagram-passes >= 1``) and removes the ``## 📊 Visual Overview``
section from each one, then resets the diagram-provenance frontmatter fields so
the note is eligible for a fresh diagram run.

Typical workflow::

    # 1. Strip all diagram sections (dry-run first)
    python strip_diagrams.py --input-dir PATH --dry-run -v

    # 2. Strip for real
    python strip_diagrams.py --input-dir PATH -v

    # 3. Fix add_diagrams.py (see patch instructions), then re-run:
    python add_diagrams.py --input-dir PATH --limit 100

Usage:
    python strip_diagrams.py --dry-run --limit 5 -v
    python strip_diagrams.py --input-dir PATH
    python strip_diagrams.py --note appeal-to-emotion -v

Version:
    1.0.0

Python:
    >=3.10

Dependencies:
    stdlib:  argparse, dataclasses, datetime, logging, pathlib, re, sys
    local:   lib.frontmatter (V3 pipeline), ruamel.yaml (via V3)

Author:
    Generated alongside fix for add_diagrams.py broken-mermaid issue.
"""
from __future__ import annotations

import argparse
import datetime as dt
import logging
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

# ── V3 library injection ──────────────────────────────────────────────────────
_V3_LIB = Path(__file__).parent.parent / "report-extraction-to-permanent-notes-building-v3"
if _V3_LIB.exists() and str(_V3_LIB) not in sys.path:
    sys.path.insert(0, str(_V3_LIB))

try:
    from lib.frontmatter import parse_frontmatter, render_frontmatter  # type: ignore
except ImportError as _err:  # pragma: no cover
    sys.exit(
        f"ERROR: Cannot import lib.frontmatter from {_V3_LIB}\n"
        f"  Detail: {_err}\n"
        "  Ensure the V3 pipeline directory exists alongside V6."
    )

# ════════════════════════════════════════════════════════════════════════════
# Constants
# ════════════════════════════════════════════════════════════════════════════

__version__ = "1.0.0"

#: Default notes directory — psychology batch (primary test target).
DEFAULT_INPUT_DIR = Path(
    r"D:\10_pur3v4d3r's-vault\999-report-organizing\_permanent-notes"
    r"\_psychology-permanent-notes"
)

#: Heading that marks the start of the injected diagram section.
DIAGRAM_SECTION_HEADER = "## 📊 Visual Overview"

#: Matches the diagram section from its header through to (but not including)
#: the first level-1 heading that follows (the note's own title).
#: The section is always prepended before the title by insert_diagram_section().
_DIAGRAM_SECTION_RE = re.compile(
    r"## 📊 Visual Overview[\s\S]*?(?=\n# |\Z)"
)

# ════════════════════════════════════════════════════════════════════════════
# Logging
# ════════════════════════════════════════════════════════════════════════════

logger = logging.getLogger(__name__)

# ════════════════════════════════════════════════════════════════════════════
# Data types
# ════════════════════════════════════════════════════════════════════════════


@dataclass
class NoteRecord:
    """Parsed V6 permanent note ready for diagram stripping.

    Attributes:
        path:          Absolute path to the ``.md`` file.
        frontmatter:   Parsed YAML frontmatter dict.
        body:          Note body (everything after the closing ``---``).
        diagram_passes: Value of ``provenance.diagram-passes`` (0 if absent).
    """

    path: Path
    frontmatter: dict[str, Any]
    body: str
    diagram_passes: int


@dataclass
class StripResult:
    """Outcome of stripping a single note.

    Attributes:
        path:     Path to the processed note.
        ok:       True when the note was processed without error.
        stripped: True when a diagram section was actually found and removed.
        written:  True when the file was written to disk (not dry-run).
        error:    Non-empty when ``ok`` is False.
    """

    path: Path
    ok: bool
    stripped: bool = False
    written: bool = False
    error: str = ""


@dataclass
class RunStats:
    """Aggregate counters for a batch strip run."""

    scanned: int = 0
    stripped: int = 0      # had a diagram section removed
    already_clean: int = 0  # no diagram section found (shouldn't happen in practice)
    failed: int = 0
    written: int = 0


# ════════════════════════════════════════════════════════════════════════════
# Core stripping logic
# ════════════════════════════════════════════════════════════════════════════


def strip_diagram_section(body: str) -> tuple[str, bool]:
    """Remove the ``## 📊 Visual Overview`` section from ``body``.

    The diagram section is always prepended before the note's level-1 title
    heading (``# Title``).  After removal the body resumes with that heading.

    Args:
        body: Full note body (frontmatter already stripped).

    Returns:
        ``(new_body, was_changed)`` — the cleaned body and whether any change
        was made.  Returns the original body unchanged when no diagram section
        is present.
    """
    if DIAGRAM_SECTION_HEADER not in body:
        return body, False

    new_body = _DIAGRAM_SECTION_RE.sub("", body)

    # Normalise the leading whitespace that remains before the title.
    new_body = new_body.lstrip("\n")
    if new_body:
        new_body = "\n" + new_body  # single leading newline to match original layout

    return new_body, new_body != body


def reset_diagram_frontmatter(fm: dict[str, Any], *, today: str) -> dict[str, Any]:
    """Return an updated frontmatter dict with all diagram provenance removed.

    Removes ``diagram-passes``, ``diagram-model``, ``last-diagrammed``, and any
    repair fields so the note is treated as un-diagrammed by ``add_diagrams.py``.

    Args:
        fm:    Existing parsed frontmatter dict.
        today: ISO-8601 date string.

    Returns:
        A shallow copy of ``fm`` without diagram-related provenance fields.
    """
    out = dict(fm)
    out["updated"] = today
    provenance = dict(out.get("provenance") or {})
    for key in ("diagram-passes", "diagram-model", "last-diagrammed",
                "diagram-repair-passes", "last-repaired"):
        provenance.pop(key, None)
    if provenance:
        out["provenance"] = provenance
    else:
        out.pop("provenance", None)
    return out


# ════════════════════════════════════════════════════════════════════════════
# Note I/O
# ════════════════════════════════════════════════════════════════════════════


def load_note(path: Path) -> NoteRecord:
    """Read and parse a V6 permanent note.

    Args:
        path: Path to the ``.md`` file.

    Returns:
        Parsed :class:`NoteRecord`.

    Raises:
        ValueError: When the file cannot be read or the frontmatter is invalid.
    """
    try:
        content = path.read_text(encoding="utf-8")
    except OSError as e:
        raise ValueError(f"Cannot read {path.name}: {e}") from e

    try:
        fm, body = parse_frontmatter(content)
    except Exception as e:
        raise ValueError(f"Frontmatter parse error in {path.name}: {e}") from e

    if not isinstance(fm, dict):
        raise ValueError(f"Unexpected frontmatter type in {path.name}: {type(fm)}")

    provenance = fm.get("provenance") or {}
    diagram_passes = int(provenance.get("diagram-passes") or 0)

    return NoteRecord(path=path, frontmatter=fm, body=body, diagram_passes=diagram_passes)


def scan_notes(
    input_dir: Path,
    *,
    name_filter: str | None = None,
    limit: int | None = None,
) -> list[NoteRecord]:
    """Discover V6 notes that have been through the diagram pipeline.

    Only notes with ``provenance.diagram-passes >= 1`` are eligible.

    Args:
        input_dir:   Directory to scan (non-recursive).
        name_filter: Case-insensitive substring to filter by filename stem.
        limit:       Maximum number of notes to return.

    Returns:
        Sorted list of eligible :class:`NoteRecord` objects.

    Raises:
        FileNotFoundError: When ``input_dir`` does not exist.
    """
    if not input_dir.exists():
        raise FileNotFoundError(f"Input directory not found: {input_dir}")

    notes: list[NoteRecord] = []
    for path in sorted(input_dir.glob("*.md")):
        if name_filter and name_filter.lower() not in path.stem.lower():
            continue
        try:
            note = load_note(path)
        except ValueError as e:
            logger.warning("Skipping %s: %s", path.name, e)
            continue
        if note.diagram_passes < 1:
            logger.debug(
                "Skipping %s: not yet diagrammed (diagram-passes=%d)",
                path.name, note.diagram_passes,
            )
            continue
        notes.append(note)
        if limit is not None and len(notes) >= limit:
            break
    return notes


def write_note_atomic(path: Path, content: str) -> None:
    """Atomic write via ``.tmp → replace`` to avoid partial file states.

    Args:
        path:    Destination file path.
        content: Full UTF-8 content to write.

    Raises:
        OSError: When the write or rename fails.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(content, encoding="utf-8")
    tmp.replace(path)


def _resolve_output_path(
    src: Path,
    input_dir: Path,
    output_dir: Path | None,
) -> Path:
    if output_dir is None:
        return src
    try:
        rel = src.relative_to(input_dir)
    except ValueError:
        rel = Path(src.name)
    return output_dir / rel


# ════════════════════════════════════════════════════════════════════════════
# Orchestration
# ════════════════════════════════════════════════════════════════════════════


def strip_note(
    note: NoteRecord,
    *,
    dry_run: bool,
    output_dir: Path | None,
    input_dir: Path,
    today: str,
) -> StripResult:
    """Strip the diagram section from a single note.

    Args:
        note:       Parsed note to process.
        dry_run:    When True, compute but do not write to disk.
        output_dir: Optional mirror directory; when None, overwrites in place.
        input_dir:  Original input directory (for relative path resolution).
        today:      ISO-8601 date string for provenance stamping.

    Returns:
        :class:`StripResult` describing what happened.
    """
    try:
        new_body, changed = strip_diagram_section(note.body)
    except Exception as e:
        logger.exception("Error stripping %s", note.path.name)
        return StripResult(path=note.path, ok=False, error=f"strip error: {e}")

    if not changed:
        logger.warning("No diagram section found in %s (skipping)", note.path.name)
        return StripResult(path=note.path, ok=True, stripped=False)

    logger.info("Stripped diagram section from %s", note.path.name)

    if dry_run:
        return StripResult(path=note.path, ok=True, stripped=True)

    new_fm = reset_diagram_frontmatter(note.frontmatter, today=today)
    new_content = render_frontmatter(new_fm) + "\n" + new_body

    dest = _resolve_output_path(note.path, input_dir, output_dir)
    try:
        write_note_atomic(dest, new_content)
    except OSError as e:
        logger.error("Write failed for %s: %s", dest, e)
        return StripResult(
            path=note.path, ok=False, stripped=True, error=f"write failed: {e}",
        )

    return StripResult(path=note.path, ok=True, stripped=True, written=True)


def strip_all(
    notes: list[NoteRecord],
    *,
    dry_run: bool,
    output_dir: Path | None,
    input_dir: Path,
) -> tuple[list[StripResult], RunStats]:
    """Run diagram stripping across all ``notes``.

    Args:
        notes:      Pre-scanned note candidates (from :func:`scan_notes`).
        dry_run:    When True, compute but do not write anything to disk.
        output_dir: Optional mirror directory.
        input_dir:  Original input directory.

    Returns:
        ``(results, stats)`` — per-note outcomes and aggregate counters.
    """
    stats = RunStats(scanned=len(notes))
    results: list[StripResult] = []
    today = dt.date.today().isoformat()

    for note in notes:
        result = strip_note(
            note,
            dry_run=dry_run,
            output_dir=output_dir,
            input_dir=input_dir,
            today=today,
        )
        results.append(result)
        if not result.ok:
            stats.failed += 1
        elif result.stripped:
            stats.stripped += 1
            if result.written:
                stats.written += 1
        else:
            stats.already_clean += 1

    return results, stats


# ════════════════════════════════════════════════════════════════════════════
# CLI
# ════════════════════════════════════════════════════════════════════════════


def build_parser() -> argparse.ArgumentParser:
    """Construct the command-line argument parser."""
    parser = argparse.ArgumentParser(
        prog="strip_diagrams",
        description=(
            "Remove the '## 📊 Visual Overview' diagram section from V6 permanent "
            "notes and reset diagram-provenance frontmatter so notes are eligible "
            "for a fresh add_diagrams.py run.  No LLM required."
        ),
        epilog=(
            "Examples:\n"
            "  strip_diagrams.py --dry-run -v\n"
            "      Preview what would be stripped; nothing written.\n"
            "  strip_diagrams.py --input-dir PATH\n"
            "      Strip all diagrammed notes in PATH in place.\n"
            "  strip_diagrams.py --note appeal-to-emotion --dry-run -v\n"
            "      Preview stripping a single note.\n"
            "  strip_diagrams.py --output-dir D:/preview\n"
            "      Mirror stripped output without touching originals.\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--input-dir", type=Path, default=DEFAULT_INPUT_DIR,
        help=f"Directory of V6 notes to strip (default: {DEFAULT_INPUT_DIR})",
    )
    parser.add_argument(
        "--output-dir", type=Path, default=None,
        help="Write stripped notes to this directory instead of overwriting in place.",
    )
    parser.add_argument(
        "--note", type=str, default=None, metavar="SUBSTR",
        help="Filter notes by filename-stem substring (case-insensitive).",
    )
    parser.add_argument(
        "--limit", type=int, default=None, metavar="N",
        help="Cap on the number of notes to process.",
    )
    parser.add_argument(
        "-n", "--dry-run", action="store_true",
        help="Compute what would be stripped; make no file changes.",
    )
    parser.add_argument(
        "--strict", action="store_true",
        help="Exit non-zero when any note fails to strip.",
    )
    parser.add_argument(
        "-v", "--verbose", action="count", default=0,
        help="Increase log verbosity (-v = INFO, -vv = DEBUG).",
    )
    parser.add_argument(
        "-q", "--quiet", action="store_true",
        help="Suppress non-error output.",
    )
    parser.add_argument(
        "--version", action="version", version=f"%(prog)s {__version__}",
    )
    return parser


def configure_logging(verbosity: int, quiet: bool) -> None:
    """Configure root logger based on CLI verbosity flags."""
    if quiet:
        level = logging.ERROR
    elif verbosity >= 2:
        level = logging.DEBUG
    elif verbosity == 1:
        level = logging.INFO
    else:
        level = logging.WARNING
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def main(argv: list[str] | None = None) -> int:
    """Main entry point.

    Args:
        argv: Argument vector (defaults to ``sys.argv[1:]``).

    Returns:
        Exit code: 0 = success, 2 = input dir not found, 4 = no notes found,
        5 = strict mode with failures, 130 = interrupted.
    """
    parser = build_parser()
    args = parser.parse_args(argv)
    configure_logging(args.verbose, args.quiet)

    # ── Discover notes ────────────────────────────────────────────────────
    try:
        notes = scan_notes(
            args.input_dir,
            name_filter=args.note,
            limit=args.limit,
        )
    except FileNotFoundError as e:
        logger.error("%s", e)
        return 2

    if not notes:
        logger.warning(
            "No eligible notes found in %s (filter=%r).",
            args.input_dir, args.note,
        )
        return 4

    logger.info(
        "Found %d note(s) to strip%s.",
        len(notes),
        " (dry-run — no files will be written)" if args.dry_run else "",
    )

    # ── Run strip pipeline ────────────────────────────────────────────────
    try:
        results, stats = strip_all(
            notes,
            dry_run=args.dry_run,
            output_dir=args.output_dir,
            input_dir=args.input_dir,
        )
    except KeyboardInterrupt:
        logger.warning("Interrupted by user.")
        return 130
    except Exception:
        logger.exception("Unexpected pipeline error.")
        return 1

    # ── Summary ───────────────────────────────────────────────────────────
    action = "Would strip" if args.dry_run else "Stripped"
    logger.warning(
        "%s %d/%d notes (%d written, %d already clean, %d failed).",
        action,
        stats.stripped,
        stats.scanned,
        stats.written,
        stats.already_clean,
        stats.failed,
    )

    if args.strict and stats.failed > 0:
        return 5
    return 0


# ════════════════════════════════════════════════════════════════════════════
# Entry-point guard
# ════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    sys.exit(main())
