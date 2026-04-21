#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""s6_render.py — Stage 6: render Candidate → slim permanent note (Markdown).

Reads consolidated candidates (Phase 2 output:
``_consolidated-candidates.json``), renders each via the slim Jinja2 template
(``templates/permanent_note.md.j2``), and writes a ``.md`` file to the
target directory.

If a target file already exists, the existing frontmatter is parsed, merged
with the freshly-built frontmatter (preserving user-editable fields and
union-merging tags/aliases/source-reports/relationships), and the body is
re-rendered. The previous body is **discarded** — body content is regenerated
from the canonical Candidate. Manual frontmatter edits are preserved per the
merge rules in :mod:`lib.frontmatter`.

Usage:
    python -m stages.s6_render <consolidated.json> -t <target_dir>
    python -m stages.s6_render _v3-output/phase-2-gate -t _v3-output/phase-3-sandbox
    python -m stages.s6_render <input> -t <dir> --dry-run

Version:
    3.0.0-phase3
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import logging
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any

# Ensure sibling ``lib/`` resolves when invoked via ``python -m stages.s6_render``.
_HERE = Path(__file__).resolve().parent
_PROJECT_ROOT = _HERE.parent
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from jinja2 import Environment, FileSystemLoader, StrictUndefined  # noqa: E402

from lib.candidate import Candidate, EvidenceItem  # noqa: E402
from lib.frontmatter import (  # noqa: E402
    build_frontmatter,
    merge_frontmatter,
    parse_frontmatter,
    render_frontmatter,
)
from lib.markdown import (  # noqa: E402
    callout,
    indent_block,
    join_wikilinks,
    safe_filename,
    to_kebab,
)

__version__ = "3.0.0-phase3"

logger = logging.getLogger(__name__)

#: Default name of the consolidated input file when input is a directory.
DEFAULT_CONSOLIDATED_FILENAME = "_consolidated-candidates.json"
TEMPLATE_NAME = "permanent_note.md.j2"
TEMPLATES_DIR = _PROJECT_ROOT / "templates"


class RenderError(Exception):
    """Base exception for stage-6 render failures."""


# ════════════════════════════════════════════════════════════════════════════
# Jinja environment
# ════════════════════════════════════════════════════════════════════════════

def _build_env() -> Environment:
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=False,
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
        undefined=StrictUndefined,
    )

    def _indent_callout(text: str) -> str:
        return indent_block((text or "").strip(), "> ")

    def _join_wikilinks(items: list[str]) -> str:
        return join_wikilinks(items)

    def _render_callout(callout_type: str, title: str, body: str, source: str | None) -> str:
        return callout(callout_type, title, body, source=source)

    env.filters["indent_callout"] = _indent_callout
    env.filters["join_wikilinks"] = _join_wikilinks
    env.globals["render_callout"] = _render_callout
    return env


# ════════════════════════════════════════════════════════════════════════════
# Item shaping for templates
# ════════════════════════════════════════════════════════════════════════════

@dataclass(frozen=True)
class TemplateItem:
    """Flat dict-friendly view of an :class:`EvidenceItem`."""
    title: str
    body: str
    source_stem: str

    @classmethod
    def from_item(cls, item: EvidenceItem) -> "TemplateItem":
        stem = item.source.file.removesuffix(".json").removesuffix("_validated")
        return cls(title=item.title or "", body=item.body or "", source_stem=stem)


def _shape_bucket(items: tuple[EvidenceItem, ...]) -> list[TemplateItem]:
    return [TemplateItem.from_item(it) for it in items]


# ════════════════════════════════════════════════════════════════════════════
# Render a single candidate
# ════════════════════════════════════════════════════════════════════════════

def render_candidate(
    cand: Candidate,
    *,
    env: Environment,
    today: dt.date,
    existing_frontmatter: dict[str, Any] | None = None,
) -> str:
    """Render ``cand`` to a complete markdown document.

    Args:
        cand: Consolidated candidate.
        env: Jinja2 environment.
        today: Date stamped into ``created`` / ``updated``.
        existing_frontmatter: When updating, the parsed existing frontmatter.
            Triggers the merge path so manual edits survive.

    Returns:
        The fully-rendered markdown document (frontmatter + body).
    """
    fresh_fm = build_frontmatter(cand, today=today)
    if existing_frontmatter:
        fresh_fm = merge_frontmatter(existing_frontmatter, fresh_fm)
    fm_block = render_frontmatter(fresh_fm).rstrip("\n")

    template = env.get_template(TEMPLATE_NAME)
    source_stems = sorted({s.file.removesuffix(".json").removesuffix("_validated")
                           for s in cand.source_reports})

    context: dict[str, Any] = {
        "frontmatter_block": fm_block,
        "title": cand.primary_name,
        "stem": safe_filename(cand.primary_name),
        "definition_body": cand.definition_body or "",
        "synthesis": "",
        "evidence":          _shape_bucket(cand.evidence),
        "insights":          _shape_bucket(cand.insights),
        "practices":         _shape_bucket(cand.practices),
        "warnings":          _shape_bucket(cand.warnings),
        "reflections":       _shape_bucket(cand.reflections),
        "claude_insights":   _shape_bucket(cand.claude_insights),
        "persons":           _shape_bucket(cand.persons),
        "tensions":          _shape_bucket(cand.tensions),
        "open_questions":    _shape_bucket(cand.open_questions),
        "flashcards":        _shape_bucket(cand.flashcards),
        "protocols":         _shape_bucket(cand.protocols),
        "diagrams":          _shape_bucket(cand.diagrams),
        "citations":         _shape_bucket(cand.citations),
        "methodology":       _shape_bucket(cand.methodology),
        "schema_activations":_shape_bucket(cand.schema_activations),
        "active_readings":   _shape_bucket(cand.active_readings),
        "far_transfers":     _shape_bucket(cand.far_transfers),
        "debates":           _shape_bucket(cand.debates),
        "examples":          _shape_bucket(cand.examples),
        "section_summaries": _shape_bucket(cand.section_summaries),
        "related_concepts":  list(cand.wiki_links_seen),
        "source_reports":    source_stems,
    }

    return template.render(**context)


# ════════════════════════════════════════════════════════════════════════════
# Filesystem orchestration
# ════════════════════════════════════════════════════════════════════════════

def target_path_for(cand: Candidate, target_dir: Path) -> Path:
    """Return the file path a candidate should be written to."""
    return target_dir / f"{safe_filename(cand.primary_name)}.md"


def load_candidates(input_path: Path) -> list[Candidate]:
    """Load consolidated candidates from a file or directory."""
    if input_path.is_dir():
        input_path = input_path / DEFAULT_CONSOLIDATED_FILENAME
    if not input_path.is_file():
        raise FileNotFoundError(f"Consolidated input not found: {input_path}")
    with input_path.open("r", encoding="utf-8") as f:
        payload = json.load(f)
    raw = payload.get("candidates") or []
    return [Candidate.from_dict(c) for c in raw]


def write_note(
    cand: Candidate,
    target_dir: Path,
    env: Environment,
    *,
    today: dt.date,
    dry_run: bool,
) -> tuple[Path, str]:
    """Render and (unless ``dry_run``) write a single note."""
    path = target_path_for(cand, target_dir)
    existing_fm: dict[str, Any] | None = None
    if path.exists():
        try:
            text = path.read_text(encoding="utf-8")
            existing_fm, _body = parse_frontmatter(text)
            if not existing_fm:
                existing_fm = None
        except OSError as e:
            logger.warning("Could not read existing %s: %s", path, e)
            existing_fm = None

    rendered = render_candidate(
        cand, env=env, today=today, existing_frontmatter=existing_fm,
    )
    if not dry_run:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(rendered, encoding="utf-8")
    return path, rendered


# ════════════════════════════════════════════════════════════════════════════
# Run
# ════════════════════════════════════════════════════════════════════════════

@dataclass
class RenderStats:
    notes_total: int = 0
    notes_created: int = 0
    notes_updated: int = 0
    bytes_written: int = 0
    by_status: Counter = None  # type: ignore[assignment]

    def __post_init__(self) -> None:
        if self.by_status is None:
            self.by_status = Counter()


def run_render(
    input_path: Path,
    target_dir: Path,
    *,
    today: dt.date | None = None,
    dry_run: bool = False,
) -> RenderStats:
    """Render every candidate in ``input_path`` to ``target_dir``.

    Returns a :class:`RenderStats` summary.
    """
    today = today or dt.date.today()
    candidates = load_candidates(input_path)
    env = _build_env()
    stats = RenderStats()

    if not dry_run:
        target_dir.mkdir(parents=True, exist_ok=True)

    for cand in candidates:
        if not cand.primary_name.strip():
            stats.by_status["skipped_empty_name"] += 1
            continue
        path = target_path_for(cand, target_dir)
        existed = path.exists()
        _, rendered = write_note(cand, target_dir, env, today=today, dry_run=dry_run)
        stats.notes_total += 1
        if existed:
            stats.notes_updated += 1
        else:
            stats.notes_created += 1
        stats.bytes_written += len(rendered.encode("utf-8"))

    return stats


# ════════════════════════════════════════════════════════════════════════════
# CLI
# ════════════════════════════════════════════════════════════════════════════

def configure_logging(verbosity: int, quiet: bool) -> None:
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


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="s6_render",
        description="Render consolidated candidates to slim permanent notes.",
        epilog=(
            "Examples:\n"
            "  python -m stages.s6_render _v3-output/phase-2-gate -t _v3-output/phase-3-sandbox\n"
            "  python -m stages.s6_render path/to/_consolidated-candidates.json -t out/\n"
            "  python -m stages.s6_render <input> -t <dir> --dry-run\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("input", type=Path,
                        help="Consolidated JSON file OR directory containing it.")
    parser.add_argument("-t", "--target-dir", type=Path, required=True,
                        help="Directory to write rendered .md notes into.")
    parser.add_argument("-n", "--dry-run", action="store_true",
                        help="Render without writing any files.")
    parser.add_argument("-v", "--verbose", action="count", default=0)
    parser.add_argument("-q", "--quiet", action="store_true")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    configure_logging(args.verbose, args.quiet)

    try:
        stats = run_render(args.input, args.target_dir, dry_run=args.dry_run)
    except FileNotFoundError as e:
        logger.error("Input not found: %s", e)
        return 2
    except PermissionError as e:
        logger.error("Permission denied: %s", e)
        return 3
    except RenderError as e:
        logger.error("Render failed: %s", e)
        return 4
    except KeyboardInterrupt:
        logger.warning("Interrupted by user")
        return 130
    except Exception:
        logger.exception("Unexpected error")
        return 1

    mode = "DRY-RUN" if args.dry_run else "WROTE"
    logger.warning(
        "%s %d notes (%d created, %d updated, %.1f KB) -> %s",
        mode, stats.notes_total, stats.notes_created, stats.notes_updated,
        stats.bytes_written / 1024, args.target_dir,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
