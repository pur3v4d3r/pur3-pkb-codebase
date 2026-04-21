#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""s7_stubs.py — Stage 7: stub generation for unresolved real concepts.

Hardened wrapper around v2's ``generate_stubs.py``. The v2 generator emits
one stub per missing-concept entry; v3 adds a pre-filter through
``lib.link_validator.is_valid_concept`` so sentence-shaped, garbage, or
report-filename targets never reach disk.

Pipeline:

  1. Run v2 audit to discover ``audit.missing_concepts``.
  2. Filter that mapping by ``link_validator.is_valid_concept``.
  3. Build a synthetic ``AuditResult`` with the filtered subset.
  4. Hand it to ``generate_stubs.build_stub_plans`` + ``execute_plans``.
  5. Return per-rejection-reason counts so callers can audit the filter.

Phase 5 deliverable. Spec §5 line 481.

Usage:
    python -m stages.s7_stubs --notes-dir _v3-output/phase-3-sandbox
    python -m stages.s7_stubs --notes-dir <dir> --execute
    python -m stages.s7_stubs --notes-dir <dir> --min-refs 2 --execute

Exit codes:
    0   success
    1   uncaught error
    2   notes_dir missing
    130 KeyboardInterrupt

Version:
    1.0.0
"""
from __future__ import annotations

import argparse
import logging
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_V3_ROOT = _HERE.parent
_V2_DIR = _V3_ROOT.parent / "report-extraction-to-permanent-notes-building"
for _p in (_V3_ROOT, _V2_DIR):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import audit_notes  # noqa: E402
import generate_stubs  # noqa: E402
from lib import link_validator  # noqa: E402


__version__ = "1.0.0"

logger = logging.getLogger(__name__)


class StubError(Exception):
    """Base exception for s7_stubs-specific errors."""


@dataclass(frozen=True)
class StubStats:
    """Outcome of a single Stage 7 run."""
    notes_dir: str
    raw_missing: int
    accepted: int
    rejected: int
    rejection_reasons: dict[str, int] = field(default_factory=dict)
    plans: int = 0
    written: int = 0
    skipped: int = 0
    errors: tuple[str, ...] = field(default_factory=tuple)
    by_category: dict[str, int] = field(default_factory=dict)
    executed: bool = False

    def to_dict(self) -> dict[str, object]:
        return {
            "notes_dir": self.notes_dir,
            "raw_missing": self.raw_missing,
            "accepted": self.accepted,
            "rejected": self.rejected,
            "rejection_reasons": dict(self.rejection_reasons),
            "plans": self.plans,
            "written": self.written,
            "skipped": self.skipped,
            "errors": list(self.errors),
            "by_category": dict(self.by_category),
            "executed": self.executed,
        }


def filter_missing_concepts(
    missing: dict[str, set[str]],
) -> tuple[dict[str, set[str]], dict[str, int]]:
    """Filter ``missing`` keeping only concepts validated by ``link_validator``.

    Args:
        missing: ``audit.missing_concepts`` (target name -> set of source notes).

    Returns:
        ``(filtered_mapping, rejection_reason_counts)``.
    """
    filtered: dict[str, set[str]] = {}
    reasons: dict[str, int] = defaultdict(int)
    for target, sources in missing.items():
        ok, reason = link_validator.is_valid_concept(target)
        if ok:
            filtered[target] = sources
        else:
            reasons[reason or "unknown"] += 1
    return filtered, dict(reasons)


def _make_filtered_audit(original: audit_notes.AuditResult,
                         filtered_missing: dict[str, set[str]]
                         ) -> audit_notes.AuditResult:
    """Produce a shallow copy of ``original`` whose ``missing_concepts`` is filtered.

    ``audit_notes.AuditResult`` is a plain class, not a dataclass, so we
    construct a new instance by mutating attributes on a copy. Only
    ``missing_concepts`` is rebuilt; all other fields are pass-through
    references (the v2 stub generator only consults ``missing_concepts``).
    """
    # AuditResult.__init__ takes no args (sets defaults) per v2 source.
    new = audit_notes.AuditResult()
    # Copy all known attributes through, then override missing_concepts.
    for attr in (
        "total_notes", "unique_targets", "resolved", "unresolved",
        "placeholders", "report_refs", "missing_concepts",
        "orphans", "well_connected", "note_incoming", "note_outgoing",
    ):
        if hasattr(original, attr):
            setattr(new, attr, getattr(original, attr))
    new.missing_concepts = filtered_missing
    return new


def generate_stubs_filtered(
    notes_dir: Path,
    *,
    min_refs: int = 1,
    categories: set[str] | None = None,
    execute: bool = False,
) -> StubStats:
    """Run hardened stub generation against ``notes_dir``.

    Args:
        notes_dir: Permanent-notes directory to scan and write into.
        min_refs: Minimum referencing-source count for a stub to be planned.
        categories: If set, restrict planning to these v2 categories.
        execute: If True, write stub files. Otherwise dry-run.

    Returns:
        ``StubStats`` with raw / filtered / planned / written counts plus
        per-rejection-reason and per-category breakdowns.

    Raises:
        StubError: If ``notes_dir`` is missing.
    """
    if not notes_dir.is_dir():
        raise StubError(f"notes_dir does not exist: {notes_dir}")

    logger.info("Running v2 audit on %s", notes_dir)
    audit = audit_notes.run_audit(notes_dir=notes_dir)
    raw_missing = len(audit.missing_concepts)
    logger.info("Raw missing-concept count: %d", raw_missing)

    filtered, reasons = filter_missing_concepts(audit.missing_concepts)
    accepted = len(filtered)
    rejected = raw_missing - accepted
    logger.info("After link_validator filter: %d accepted, %d rejected",
                accepted, rejected)
    for reason, n in sorted(reasons.items(), key=lambda kv: -kv[1]):
        logger.info("  rejected[%s]: %d", reason, n)

    filtered_audit = _make_filtered_audit(audit, filtered)
    plans = generate_stubs.build_stub_plans(
        filtered_audit, notes_dir, min_refs=min_refs, categories=categories,
    )
    logger.info("Planned %d stubs (min_refs=%d, categories=%s)",
                len(plans), min_refs, categories)

    summary = generate_stubs.execute_plans(plans, dry_run=not execute)

    return StubStats(
        notes_dir=str(notes_dir),
        raw_missing=raw_missing,
        accepted=accepted,
        rejected=rejected,
        rejection_reasons=reasons,
        plans=len(plans),
        written=int(summary.get("written", 0)),
        skipped=int(summary.get("skipped", 0)),
        errors=tuple(summary.get("errors", [])),
        by_category=dict(summary.get("by_category", {})),
        executed=execute,
    )


def build_parser() -> argparse.ArgumentParser:
    """Construct the command-line argument parser."""
    parser = argparse.ArgumentParser(
        prog="s7_stubs",
        description="Stage 7: hardened stub generation filtered via link_validator.",
        epilog=(
            "Examples:\n"
            "  python -m stages.s7_stubs --notes-dir _v3-output/phase-3-sandbox\n"
            "  python -m stages.s7_stubs --notes-dir <dir> --execute\n"
            "  python -m stages.s7_stubs --notes-dir <dir> --min-refs 2 --execute\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--notes-dir", type=Path, required=True,
                        help="Permanent-notes directory (required).")
    parser.add_argument("--min-refs", type=int, default=1,
                        help="Minimum referencing-source count to generate a stub (default 1).")
    parser.add_argument("--categories", nargs="+", default=None,
                        help="Restrict to these v2 categories (default: all non-skip).")
    parser.add_argument("--execute", action="store_true",
                        help="Write stub files (default: dry-run).")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument("-v", "--verbose", action="count", default=0)
    parser.add_argument("-q", "--quiet", action="store_true")
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
    """Main entry point."""
    parser = build_parser()
    args = parser.parse_args(argv)
    configure_logging(args.verbose, args.quiet)

    cats = set(args.categories) if args.categories else None

    try:
        stats = generate_stubs_filtered(
            args.notes_dir,
            min_refs=args.min_refs,
            categories=cats,
            execute=args.execute,
        )
    except StubError as e:
        logger.error("%s", e)
        return 2
    except KeyboardInterrupt:
        logger.warning("Interrupted by user")
        return 130
    except Exception:
        logger.exception("Unexpected error")
        return 1

    if not args.quiet:
        mode = "EXECUTE" if stats.executed else "DRY-RUN"
        print(f"\n[{mode}] {stats.raw_missing} raw -> {stats.accepted} accepted "
              f"({stats.rejected} rejected) -> {stats.plans} planned -> "
              f"{stats.written} written")
        if stats.rejection_reasons:
            print("  Rejection reasons:")
            for r, n in sorted(stats.rejection_reasons.items(), key=lambda kv: -kv[1]):
                print(f"    {r:<24s} {n}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
