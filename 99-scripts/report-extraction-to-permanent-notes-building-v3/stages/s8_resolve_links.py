#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""s8_resolve_links.py — Stage 8: rewrite report wiki-links to resolved targets.

Thin wrapper around v2's ``rewrite_report_wikilinks.py``. Walks one or more
report directories and rewrites bare ``[[Concept Name]]`` wiki-links inside
them to pipe form ``[[concept-stem|Concept Name]]`` using the permanent-notes
index as the resolution source.

Differs from Stage 9 in scope: Stage 8 rewrites the *source* reports (so the
extractor sees consistent links next time), Stage 9 rewrites the *generated
notes* (so Obsidian resolves them cleanly in the vault).

Phase 5 deliverable.

Usage:
    python -m stages.s8_resolve_links --notes-dir _v3-output/phase-3-sandbox \
                                       --reports-dir 999-report-organizing/from-copilot
    python -m stages.s8_resolve_links --notes-dir <dir> --reports-dir <dir> --execute

Exit codes:
    0   success
    1   uncaught error
    2   notes_dir or reports_dir missing
    130 KeyboardInterrupt

Spec reference: §5 Phase 5; §4.3 (v2 reuse).

Version:
    1.0.0
"""
from __future__ import annotations

import argparse
import logging
import sys
from dataclasses import dataclass, field
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_V3_ROOT = _HERE.parent
_V2_DIR = _V3_ROOT.parent / "report-extraction-to-permanent-notes-building"
for _p in (_V3_ROOT, _V2_DIR):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import rewrite_report_wikilinks  # noqa: E402


__version__ = "1.0.0"

logger = logging.getLogger(__name__)


class ResolveLinksError(Exception):
    """Base exception for s8_resolve_links-specific errors."""


@dataclass(frozen=True)
class ResolveStats:
    """Outcome of a single Stage 8 run across one or more report directories."""
    notes_dir: str
    reports_dirs: tuple[str, ...]
    files_scanned: int
    files_changed: int
    total_rewrites: int
    unresolved: tuple[str, ...] = field(default_factory=tuple)
    executed: bool = False

    def to_dict(self) -> dict[str, object]:
        return {
            "notes_dir": self.notes_dir,
            "reports_dirs": list(self.reports_dirs),
            "files_scanned": self.files_scanned,
            "files_changed": self.files_changed,
            "total_rewrites": self.total_rewrites,
            "unresolved_count": len(self.unresolved),
            "unresolved_sample": list(self.unresolved[:50]),
            "executed": self.executed,
        }


def resolve_report_links(
    notes_dir: Path,
    reports_dirs: list[Path],
    *,
    execute: bool = False,
    recheck_piped: bool = False,
    verbose: bool = False,
) -> ResolveStats:
    """Rewrite wiki-links in every ``*.md`` under each ``reports_dirs`` entry.

    Args:
        notes_dir: Permanent-notes directory used to build the resolution index.
        reports_dirs: One or more directories of source reports to process.
        execute: If True, mutate report files in place. Otherwise dry-run.
        recheck_piped: Also re-check existing pipe links and fix wrong targets.
        verbose: Pass-through verbosity flag for v2's per-file output.

    Returns:
        Aggregated counts and unresolved-link sample.

    Raises:
        ResolveLinksError: If ``notes_dir`` or any ``reports_dirs`` entry is missing.
    """
    if not notes_dir.is_dir():
        raise ResolveLinksError(f"notes_dir does not exist: {notes_dir}")
    if not reports_dirs:
        raise ResolveLinksError("reports_dirs is empty")
    for rd in reports_dirs:
        if not rd.is_dir():
            raise ResolveLinksError(f"reports_dir does not exist: {rd}")

    logger.info("Building resolution index from %s", notes_dir)
    index = rewrite_report_wikilinks.build_resolution_index(notes_dir.resolve())
    logger.info("Index entries: %d", len(index))

    grand_changed = 0
    grand_rewrites = 0
    grand_scanned = 0
    grand_unresolved: list[str] = []

    for folder in reports_dirs:
        # Resolve to absolute so filepath.relative_to(VAULT_ROOT) works in v2 helper.
        files = sorted(folder.resolve().rglob("*.md"))
        if not files:
            logger.warning("No markdown files under %s; skipping.", folder)
            continue
        logger.info("Processing %s (%d files)", folder, len(files))
        changed, rewrites, scanned, unresolved = rewrite_report_wikilinks.process_files(
            files, index, execute=execute, verbose=verbose, recheck_piped=recheck_piped,
        )
        grand_changed += changed
        grand_rewrites += rewrites
        grand_scanned += scanned
        grand_unresolved.extend(unresolved)

    return ResolveStats(
        notes_dir=str(notes_dir),
        reports_dirs=tuple(str(p) for p in reports_dirs),
        files_scanned=grand_scanned,
        files_changed=grand_changed,
        total_rewrites=grand_rewrites,
        unresolved=tuple(grand_unresolved),
        executed=execute,
    )


def build_parser() -> argparse.ArgumentParser:
    """Construct the command-line argument parser."""
    parser = argparse.ArgumentParser(
        prog="s8_resolve_links",
        description="Stage 8: resolve & rewrite wiki-links inside source reports.",
        epilog=(
            "Examples:\n"
            "  python -m stages.s8_resolve_links --notes-dir <notes> --reports-dir <reports>\n"
            "  python -m stages.s8_resolve_links --notes-dir <n> --reports-dir <r> --execute\n"
            "  python -m stages.s8_resolve_links --notes-dir <n> "
            "--reports-dir <a> --reports-dir <b>\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--notes-dir", type=Path, required=True,
                        help="Permanent-notes directory for the resolution index (required).")
    parser.add_argument("--reports-dir", type=Path, action="append", required=True,
                        help="Reports directory to process. Repeatable.")
    parser.add_argument("--execute", action="store_true",
                        help="Apply changes (default: dry-run).")
    parser.add_argument("--recheck-piped", action="store_true",
                        help="Also re-check existing pipe links and fix wrong targets.")
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

    try:
        stats = resolve_report_links(
            args.notes_dir,
            args.reports_dir,
            execute=args.execute,
            recheck_piped=args.recheck_piped,
            verbose=args.verbose >= 1,
        )
    except ResolveLinksError as e:
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
        print(f"\n[{mode}] {stats.files_changed}/{stats.files_scanned} files changed "
              f"({stats.total_rewrites} rewrites, {len(stats.unresolved)} still unresolved)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

