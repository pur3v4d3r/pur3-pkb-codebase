#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""s2_validate.py — Stage 2: garbage-link elimination + JSON sanitization.

Reads ``_extracted.json`` files emitted by ``pkb_extractor.py`` and produces:

- ``<stem>_validated.json``        — clean copy with garbage wiki-link targets
                                      stripped from frontmatter and body
- ``<stem>_validation-report.json`` — what was removed and why, plus
                                      flagged-only items (callout titles that
                                      would not pass concept validation)

Validation rules live in :mod:`lib.link_validator`. Stage 2 is a pure
walker / writer — it does not contain any rejection logic itself.

Strict mode (``--strict-links``) raises ``GarbageLinkError`` on the first
invalid target instead of stripping silently. Useful in CI / pre-commit.

Spec reference: ``_v3-spec/00-master-spec.md`` §1.1 (data flow), §5 Phase 1.

Usage:
    # Validate every _extracted.json under a batch directory
    python -m stages.s2_validate path/to/batch_dir/

    # Single file, custom output dir, dry-run
    python -m stages.s2_validate report_extracted.json -o out/ --dry-run

    # Strict mode for CI: fail on first garbage link
    python -m stages.s2_validate path/to/batch_dir/ --strict-links

Exit codes:
    0   success (or dry-run completed)
    1   uncaught error
    2   input path does not exist
    3   permission denied
    4   bad CLI arguments
    5   strict-mode garbage detected
    130 interrupted (SIGINT)
"""
from __future__ import annotations

# ─── Standard library ───────────────────────────────────────────────────
import argparse
import json
import logging
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable

# ─── Local ──────────────────────────────────────────────────────────────
# Allow execution as a script from any cwd by ensuring the v3 root is on
# sys.path before the lib import.
_V3_ROOT = Path(__file__).resolve().parent.parent
if str(_V3_ROOT) not in sys.path:
    sys.path.insert(0, str(_V3_ROOT))

from lib.link_validator import is_valid_concept  # noqa: E402


# ═════════════════════════════════════════════════════════════════════════
# Constants
# ═════════════════════════════════════════════════════════════════════════

__version__ = "1.0.0"

#: Glob pattern for upstream extractor output files.
EXTRACTED_GLOB: str = "*_extracted.json"

#: Frontmatter keys whose values are lists of wiki-link strings (``[[Target]]``
#: or ``[[Target|Display]]``).
FRONTMATTER_LINK_LIST_KEYS: tuple[str, ...] = (
    "prerequisites",
    "builds_on",
    "related",
    "link_related",
    "link_up",
    "link_down",
    "link_siblings",
    "see_also",
)

#: Frontmatter keys whose values are *single* wiki-link strings.
FRONTMATTER_LINK_SCALAR_KEYS: tuple[str, ...] = (
    "link_up",
    "parent",
)

#: Regex extracting the link target from a frontmatter string. Accepts both
#: ``[[Target]]`` and ``[[Target|Display]]``. Captures the target.
_FM_LINK_PATTERN = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]*)?\]\]")


# ═════════════════════════════════════════════════════════════════════════
# Logging
# ═════════════════════════════════════════════════════════════════════════

logger = logging.getLogger(__name__)


# ═════════════════════════════════════════════════════════════════════════
# Custom exceptions
# ═════════════════════════════════════════════════════════════════════════

class ValidateError(Exception):
    """Base exception for s2_validate."""


class GarbageLinkError(ValidateError):
    """Raised in ``--strict-links`` mode when a garbage target is found."""


# ═════════════════════════════════════════════════════════════════════════
# Data types
# ═════════════════════════════════════════════════════════════════════════

@dataclass
class Removal:
    """A single rejected wiki-link target.

    Attributes:
        target:  The raw target string that was rejected.
        reason:  Reason code from :data:`lib.link_validator.REASON_CODES`.
        context: Where the target was found, e.g. ``"body"``,
                 ``"frontmatter:builds_on"``, ``"frontmatter:link_up"``.
    """
    target: str
    reason: str
    context: str

    def to_dict(self) -> dict[str, str]:
        return {"target": self.target, "reason": self.reason, "context": self.context}


@dataclass
class Flag:
    """A non-link string flagged as concept-shaped garbage (advisory only).

    Used for callout titles, which are *not* stripped from the JSON but are
    surfaced in the validation report so the operator can spot extractor bugs.
    """
    text: str
    reason: str
    context: str

    def to_dict(self) -> dict[str, str]:
        return {"text": self.text, "reason": self.reason, "context": self.context}


@dataclass
class FileReport:
    """Per-file validation report.

    Attributes:
        source_file: Path of the validated ``_extracted.json``.
        removed:     Garbage links stripped from the JSON.
        flagged:     Callout titles that did not pass concept validation
                     (advisory only — *not* stripped).
        stats:       Aggregate counts.
    """
    source_file: str
    removed: list[Removal] = field(default_factory=list)
    flagged: list[Flag] = field(default_factory=list)
    stats: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "source_file": self.source_file,
            "stats": self.stats,
            "removed": [r.to_dict() for r in self.removed],
            "flagged": [f.to_dict() for f in self.flagged],
        }


# ═════════════════════════════════════════════════════════════════════════
# Core business logic
# ═════════════════════════════════════════════════════════════════════════

def extract_target(fm_value: str) -> str | None:
    """Extract the target from a frontmatter wiki-link string.

    Args:
        fm_value: A string such as ``"[[Foo]]"`` or ``"[[Foo|Bar]]"``.

    Returns:
        The target portion (``"Foo"``), or ``None`` if the string is not a
        recognizable wiki-link.

    Example:
        >>> extract_target("[[Self-Determination-Theory]]")
        'Self-Determination-Theory'
        >>> extract_target("[[Zimmerman-SRL-Model|Zimmerman's SRL Model]]")
        'Zimmerman-SRL-Model'
        >>> extract_target("not a link") is None
        True
    """
    if not isinstance(fm_value, str):
        return None
    match = _FM_LINK_PATTERN.search(fm_value)
    return match.group(1).strip() if match else None


def _validate_target(
    target: str,
    context: str,
    removed: list[Removal],
    strict: bool,
) -> bool:
    """Check a single target. Append a Removal if invalid.

    Returns True if the target is valid (caller should keep it), False if it
    was rejected (caller should drop it). Raises :class:`GarbageLinkError`
    in strict mode on rejection.
    """
    valid, reason = is_valid_concept(target)
    if valid:
        return True
    if strict:
        raise GarbageLinkError(
            f"strict-mode rejection: target={target!r} "
            f"reason={reason!r} context={context!r}"
        )
    removed.append(Removal(target=target, reason=reason, context=context))
    return False


def validate_frontmatter_links(
    frontmatter: dict[str, Any],
    report: FileReport,
    strict: bool,
) -> dict[str, Any]:
    """Strip garbage wiki-links from frontmatter, in-place on a copy.

    Walks both list-valued keys (e.g. ``builds_on: [[[Foo]], [[Bar]]]``) and
    scalar-valued keys (e.g. ``link_up: [[Foo]]``). Non-link values pass
    through unchanged.

    Args:
        frontmatter: The ``document_metadata.frontmatter`` dict.
        report: Removals are appended here.
        strict: If True, raise on the first rejection instead of stripping.

    Returns:
        A new frontmatter dict with garbage stripped.
    """
    cleaned: dict[str, Any] = {}
    for key, value in frontmatter.items():
        if key in FRONTMATTER_LINK_LIST_KEYS and isinstance(value, list):
            kept: list[Any] = []
            for item in value:
                target = extract_target(item) if isinstance(item, str) else None
                if target is None:
                    # Not a link — pass through (don't validate non-link items).
                    kept.append(item)
                    continue
                if _validate_target(target, f"frontmatter:{key}", report.removed, strict):
                    kept.append(item)
            cleaned[key] = kept
        elif key in FRONTMATTER_LINK_SCALAR_KEYS and isinstance(value, str):
            target = extract_target(value)
            if target is None:
                cleaned[key] = value
            elif _validate_target(target, f"frontmatter:{key}", report.removed, strict):
                cleaned[key] = value
            # else: drop the key entirely (scalar invalid → no replacement)
        else:
            cleaned[key] = value
    return cleaned


def validate_body_wiki_links(
    wiki_links: list[dict[str, Any]],
    report: FileReport,
    strict: bool,
) -> list[dict[str, Any]]:
    """Strip garbage entries from the body ``wiki_links`` list.

    Args:
        wiki_links: The ``extracted_content.wiki_links`` list. Each entry is
            a dict with a ``target`` field.
        report: Removals are appended here.
        strict: If True, raise on the first rejection.

    Returns:
        A new list containing only entries whose ``target`` passes validation.
    """
    kept: list[dict[str, Any]] = []
    for entry in wiki_links:
        if not isinstance(entry, dict):
            kept.append(entry)
            continue
        target = entry.get("target")
        if not isinstance(target, str):
            kept.append(entry)
            continue
        if _validate_target(target, "body", report.removed, strict):
            kept.append(entry)
    return kept


def flag_callout_titles(
    callouts: list[dict[str, Any]],
    report: FileReport,
) -> None:
    """Flag callout titles that would not pass concept validation.

    Callouts are *not* stripped — their titles are display content, not link
    targets. But titles that look like concept-extractor garbage (templater
    leakage, sentence-shaped, YAML fragments) are surfaced in the report so
    extractor bugs are visible.

    Args:
        callouts: The ``extracted_content.callouts`` list.
        report: Flags are appended to ``report.flagged``.
    """
    for callout in callouts:
        if not isinstance(callout, dict):
            continue
        title = callout.get("title")
        if not isinstance(title, str) or not title.strip():
            continue
        valid, reason = is_valid_concept(title)
        if not valid:
            # Don't flag merely-long titles (sentence-shaped is fine for a
            # callout) or too-many-tokens. Surface only structural pathologies.
            if reason in {
                "templater-syntax",
                "template-placeholder",
                "yaml-fragment-leak",
                "disallowed-chars",
                "report-filename",
            }:
                report.flagged.append(
                    Flag(text=title, reason=reason, context="callout-title")
                )


def validate_extracted(
    data: dict[str, Any],
    source_label: str,
    strict: bool = False,
) -> tuple[dict[str, Any], FileReport]:
    """Validate one parsed ``_extracted.json`` payload.

    Pure function — does not touch the filesystem. Returns the cleaned data
    and a populated report.

    Args:
        data: Parsed JSON content from an ``_extracted.json`` file.
        source_label: Identifier for the file (used in the report).
        strict: If True, raise :class:`GarbageLinkError` on the first
            rejection instead of stripping.

    Returns:
        ``(cleaned_data, report)``. ``cleaned_data`` is a deep-ish copy with
        garbage stripped from frontmatter and body wiki-links.

    Raises:
        GarbageLinkError: In strict mode, on first rejection.
    """
    report = FileReport(source_file=source_label)

    # Shallow-clone outer dict; we only mutate the branches we touch.
    cleaned: dict[str, Any] = dict(data)

    # ── Frontmatter ────────────────────────────────────────────────────
    doc_meta = cleaned.get("document_metadata")
    if isinstance(doc_meta, dict):
        fm = doc_meta.get("frontmatter")
        if isinstance(fm, dict):
            new_fm = validate_frontmatter_links(fm, report, strict)
            new_doc_meta = dict(doc_meta)
            new_doc_meta["frontmatter"] = new_fm
            cleaned["document_metadata"] = new_doc_meta

    # ── Body wiki-links + callout titles ───────────────────────────────
    # The upstream extractor (pkb_extractor.py) stores body items under
    # ``extracted_items``. Older payloads or tests may use ``extracted_content``;
    # we accept either, prefer the present one, and write back to the same key.
    body_key = "extracted_items" if "extracted_items" in cleaned else "extracted_content"
    extracted = cleaned.get(body_key)
    if isinstance(extracted, dict):
        new_extracted = dict(extracted)

        wiki_links = extracted.get("wiki_links")
        if isinstance(wiki_links, list):
            new_extracted["wiki_links"] = validate_body_wiki_links(
                wiki_links, report, strict
            )

        callouts = extracted.get("callouts")
        if isinstance(callouts, list):
            flag_callout_titles(callouts, report)

        cleaned[body_key] = new_extracted

    # ── Stats ─────────────────────────────────────────────────────────
    by_reason = Counter(r.reason for r in report.removed)
    flagged_by_reason = Counter(f.reason for f in report.flagged)
    total_links_seen = (
        len(report.removed)
        + _count_kept_links(cleaned)
    )
    report.stats = {
        "total_links_seen": total_links_seen,
        "removed_count": len(report.removed),
        "removed_by_reason": dict(by_reason),
        "flagged_count": len(report.flagged),
        "flagged_by_reason": dict(flagged_by_reason),
        "strict_mode": strict,
    }
    return cleaned, report


def _count_kept_links(cleaned: dict[str, Any]) -> int:
    """Best-effort count of wiki-links surviving in the cleaned payload."""
    count = 0
    extracted = cleaned.get("extracted_items") or cleaned.get("extracted_content")
    if isinstance(extracted, dict):
        wiki = extracted.get("wiki_links")
        if isinstance(wiki, list):
            count += len(wiki)
    doc_meta = cleaned.get("document_metadata")
    if isinstance(doc_meta, dict):
        fm = doc_meta.get("frontmatter")
        if isinstance(fm, dict):
            for key, value in fm.items():
                if key in FRONTMATTER_LINK_LIST_KEYS and isinstance(value, list):
                    count += sum(1 for v in value if isinstance(v, str) and extract_target(v))
                elif key in FRONTMATTER_LINK_SCALAR_KEYS and isinstance(value, str):
                    if extract_target(value):
                        count += 1
    return count


# ═════════════════════════════════════════════════════════════════════════
# I/O layer
# ═════════════════════════════════════════════════════════════════════════

def discover_inputs(input_path: Path) -> list[Path]:
    """Resolve a CLI input path to the list of ``_extracted.json`` files.

    Args:
        input_path: Either a single ``.json`` file or a directory.

    Returns:
        Sorted list of ``_extracted.json`` paths.

    Raises:
        FileNotFoundError: If ``input_path`` does not exist.
    """
    if not input_path.exists():
        raise FileNotFoundError(input_path)
    if input_path.is_file():
        return [input_path]
    files = sorted(input_path.rglob(EXTRACTED_GLOB))
    return files


def derive_output_paths(
    extracted_path: Path,
    output_dir: Path | None,
) -> tuple[Path, Path]:
    """Compute the validated.json and validation-report.json paths.

    Args:
        extracted_path: Source ``..._extracted.json`` path.
        output_dir: Override directory; ``None`` means siblings of the input.

    Returns:
        ``(validated_path, report_path)``.
    """
    name = extracted_path.name
    # Strip trailing ``_extracted.json`` (or ``.json``) to get the stem.
    if name.endswith("_extracted.json"):
        stem = name[: -len("_extracted.json")]
    else:
        stem = extracted_path.stem
    parent = output_dir if output_dir is not None else extracted_path.parent
    return (
        parent / f"{stem}_validated.json",
        parent / f"{stem}_validation-report.json",
    )


def write_outputs(
    cleaned: dict[str, Any],
    report: FileReport,
    validated_path: Path,
    report_path: Path,
) -> None:
    """Write the cleaned JSON and report JSON to disk."""
    validated_path.parent.mkdir(parents=True, exist_ok=True)
    with validated_path.open("w", encoding="utf-8") as fh:
        json.dump(cleaned, fh, ensure_ascii=False, indent=2)
    with report_path.open("w", encoding="utf-8") as fh:
        json.dump(report.to_dict(), fh, ensure_ascii=False, indent=2)


def process_file(
    extracted_path: Path,
    output_dir: Path | None,
    strict: bool,
    dry_run: bool,
) -> FileReport:
    """End-to-end processing for one ``_extracted.json``.

    Returns the FileReport regardless of dry-run state.
    """
    logger.info("Validating %s", extracted_path)
    with extracted_path.open("r", encoding="utf-8") as fh:
        data = json.load(fh)
    cleaned, report = validate_extracted(
        data, source_label=str(extracted_path), strict=strict
    )
    if not dry_run:
        validated_path, report_path = derive_output_paths(extracted_path, output_dir)
        write_outputs(cleaned, report, validated_path, report_path)
        logger.info(
            "  wrote %s  (removed=%d, flagged=%d)",
            validated_path.name,
            report.stats["removed_count"],
            report.stats["flagged_count"],
        )
    else:
        logger.info(
            "  dry-run: would remove %d, flag %d",
            report.stats["removed_count"],
            report.stats["flagged_count"],
        )
    return report


def aggregate_reports(reports: Iterable[FileReport]) -> dict[str, Any]:
    """Aggregate per-file stats into a corpus-level summary."""
    reports = list(reports)
    total_removed = sum(r.stats.get("removed_count", 0) for r in reports)
    total_flagged = sum(r.stats.get("flagged_count", 0) for r in reports)
    total_seen = sum(r.stats.get("total_links_seen", 0) for r in reports)
    by_reason: Counter[str] = Counter()
    for r in reports:
        by_reason.update(r.stats.get("removed_by_reason", {}))
    return {
        "files_processed": len(reports),
        "total_links_seen": total_seen,
        "total_removed": total_removed,
        "total_flagged": total_flagged,
        "removal_rate": (total_removed / total_seen) if total_seen else 0.0,
        "removed_by_reason": dict(by_reason.most_common()),
    }


# ═════════════════════════════════════════════════════════════════════════
# CLI
# ═════════════════════════════════════════════════════════════════════════

def build_parser() -> argparse.ArgumentParser:
    """Construct the command-line argument parser."""
    parser = argparse.ArgumentParser(
        prog="s2_validate",
        description=(
            "Stage 2 — strip garbage wiki-link targets from _extracted.json "
            "files using lib.link_validator."
        ),
        epilog=(
            "Examples:\n"
            "  s2_validate path/to/batch_dir/                    # validate all in dir\n"
            "  s2_validate report_extracted.json                 # single file\n"
            "  s2_validate path/to/batch_dir/ -o out/            # custom output dir\n"
            "  s2_validate path/to/batch_dir/ --dry-run -v       # preview\n"
            "  s2_validate path/to/batch_dir/ --strict-links     # CI gate\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("input", type=Path,
                        help="Path to an _extracted.json file or a directory containing them.")
    parser.add_argument("-o", "--output-dir", type=Path, default=None,
                        help="Directory for outputs (default: alongside each input file).")
    parser.add_argument("--strict-links", action="store_true",
                        help="Raise on first garbage link instead of stripping silently.")
    parser.add_argument("-n", "--dry-run", action="store_true",
                        help="Validate and report but do not write any files.")
    parser.add_argument("-v", "--verbose", action="count", default=0,
                        help="Increase logging verbosity (-v INFO, -vv DEBUG).")
    parser.add_argument("-q", "--quiet", action="store_true",
                        help="Suppress non-error output.")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def configure_logging(verbosity: int, quiet: bool) -> None:
    """Configure the root logger from CLI verbosity flags."""
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
    """CLI entry point. Returns process exit code."""
    parser = build_parser()
    args = parser.parse_args(argv)
    configure_logging(args.verbose, args.quiet)

    try:
        files = discover_inputs(args.input)
    except FileNotFoundError as e:
        logger.error("Input path not found: %s", e)
        return 2
    except PermissionError as e:
        logger.error("Permission denied: %s", e)
        return 3

    if not files:
        logger.warning("No %s files found under %s", EXTRACTED_GLOB, args.input)
        return 0

    logger.info("Found %d file(s) to validate", len(files))

    reports: list[FileReport] = []
    try:
        for f in files:
            try:
                reports.append(process_file(
                    f,
                    output_dir=args.output_dir,
                    strict=args.strict_links,
                    dry_run=args.dry_run,
                ))
            except GarbageLinkError as e:
                logger.error("STRICT: %s", e)
                return 5
            except json.JSONDecodeError as e:
                logger.error("Failed to parse %s: %s", f, e)
                return 1
    except KeyboardInterrupt:
        logger.warning("Interrupted by user")
        return 130

    summary = aggregate_reports(reports)
    logger.warning(  # promote summary to default visibility
        "Done. files=%d  total_links=%d  removed=%d (%.1f%%)  flagged=%d",
        summary["files_processed"],
        summary["total_links_seen"],
        summary["total_removed"],
        summary["removal_rate"] * 100,
        summary["total_flagged"],
    )
    if summary["removed_by_reason"]:
        logger.warning("Removals by reason:")
        for reason, count in summary["removed_by_reason"].items():
            logger.warning("  %-22s %d", reason, count)
    return 0


# ═════════════════════════════════════════════════════════════════════════
# Entry-point guard
# ═════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    sys.exit(main())
