#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""s9_normalize_links.py — Stage 9: vault-wide wiki-link normalization.

Thin wrapper around v2's ``rewrite_wikilinks.py``. Rewrites bare ``[[Display
Name]]`` links inside the permanent-notes directory to pipe form
``[[filename-stem|Display Name]]`` so Obsidian resolves them by exact stem
rather than alias-matching.

Phase 5 deliverable.

Usage:
    python -m stages.s9_normalize_links --notes-dir _v3-output/phase-3-sandbox
    python -m stages.s9_normalize_links --notes-dir <dir> --execute

Exit codes:
    0   success (or dry-run completed)
    1   uncaught error
    2   notes_dir missing
    130 KeyboardInterrupt

Spec reference: §5 Phase 5; §4.3 (v2 reuse).

Version:
    1.0.0
"""
from __future__ import annotations

import argparse
import logging
import sys
from dataclasses import dataclass
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_V3_ROOT = _HERE.parent
_V2_DIR = _V3_ROOT.parent / "report-extraction-to-permanent-notes-building"
for _p in (_V3_ROOT, _V2_DIR):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import rewrite_wikilinks  # noqa: E402


__version__ = "1.0.0"

logger = logging.getLogger(__name__)


class NormalizeLinksError(Exception):
    """Base exception for s9_normalize_links-specific errors."""


@dataclass(frozen=True)
class NormalizeStats:
    """Outcome of a single Stage 9 run."""
    notes_dir: str
    files_scanned: int
    files_changed: int
    total_rewrites: int
    executed: bool

    def to_dict(self) -> dict[str, object]:
        return {
            "notes_dir": self.notes_dir,
            "files_scanned": self.files_scanned,
            "files_changed": self.files_changed,
            "total_rewrites": self.total_rewrites,
            "executed": self.executed,
        }


def normalize_notes(notes_dir: Path, *, execute: bool = False) -> NormalizeStats:
    """Run pipe-syntax normalization on every ``*.md`` in ``notes_dir``.

    Args:
        notes_dir: Permanent-notes directory.
        execute: If True, mutate files in place. Otherwise dry-run.

    Returns:
        Counts of files scanned, changed, and total rewrites applied.

    Raises:
        NormalizeLinksError: If ``notes_dir`` is missing or empty.
    """
    if not notes_dir.is_dir():
        raise NormalizeLinksError(f"notes_dir does not exist: {notes_dir}")
    files = sorted(notes_dir.glob("*.md"))
    if not files:
        raise NormalizeLinksError(f"No markdown files in {notes_dir}")

    logger.info("Building resolution index over %d notes...", len(files))
    index = rewrite_wikilinks.build_resolution_index(notes_dir)
    logger.info("Index entries: %d", len(index))

    files_changed, total_rewrites, scanned = rewrite_wikilinks.process_files(
        files, index, execute=execute,
    )
    return NormalizeStats(
        notes_dir=str(notes_dir),
        files_scanned=scanned,
        files_changed=files_changed,
        total_rewrites=total_rewrites,
        executed=execute,
    )


def build_parser() -> argparse.ArgumentParser:
    """Construct the command-line argument parser."""
    parser = argparse.ArgumentParser(
        prog="s9_normalize_links",
        description="Stage 9: vault-wide wiki-link pipe-syntax normalization.",
        epilog=(
            "Examples:\n"
            "  python -m stages.s9_normalize_links --notes-dir _v3-output/phase-3-sandbox\n"
            "  python -m stages.s9_normalize_links --notes-dir <dir> --execute\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--notes-dir", type=Path, required=True,
                        help="Directory of permanent notes to normalize (required).")
    parser.add_argument("--execute", action="store_true",
                        help="Apply changes (default: dry-run).")
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
        stats = normalize_notes(args.notes_dir, execute=args.execute)
    except NormalizeLinksError as e:
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
        print(f"\n[{mode}] {stats.files_changed}/{stats.files_scanned} files would change "
              f"({stats.total_rewrites} link rewrites)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

