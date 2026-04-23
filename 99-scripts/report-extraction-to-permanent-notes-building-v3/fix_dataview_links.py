#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""fix_dataview_links.py — Strip stale dataview LIST blocks from migrated notes.

After ``migrate_to_vault.py`` renames files to kebab-case, the inline
dataview blocks that the v3 pipeline emitted are stale -- they reference
the old spaced filenames (e.g. ``LIST FROM [[4CID Blueprint Completeness
Checklist]]``) which no longer exist. Those queries silently return zero
results.

This script removes the entire stale dataview block from each file. The
block was a "see also" helper at the bottom of the note; deleting it does
not lose information -- the ``**Related:**`` line above already lists the
incoming/outgoing concept links.

Usage::

    python fix_dataview_links.py --dry-run
    python fix_dataview_links.py
    python fix_dataview_links.py --target-dir D:/some/other/dir

Exit codes:
    0   success
    1   uncaught error
    2   target dir missing
    4   no matches found
    130 interrupted
"""
from __future__ import annotations

import argparse
import logging
import re
import sys
from dataclasses import dataclass
from pathlib import Path

__version__ = "1.0.0"

DEFAULT_TARGET_DIR: Path = Path(
    "D:/00-inbox/v3-pipeline-permanet-note-leftovers/_triage-output/_vault-ready"
)

#: Matches a fenced ```dataview ... ``` block. Non-greedy, multiline.
_DATAVIEW_BLOCK_RE = re.compile(
    r"\n?```dataview\s*\n.*?\n```\s*\n?",
    re.DOTALL | re.IGNORECASE,
)

logger = logging.getLogger(__name__)


@dataclass
class FixRecord:
    path: Path
    blocks_removed: int
    bytes_removed: int


def fix_one(path: Path, *, dry_run: bool) -> FixRecord:
    """Remove stale dataview blocks from one file."""
    text = path.read_text(encoding="utf-8", errors="replace")
    matches = list(_DATAVIEW_BLOCK_RE.finditer(text))
    if not matches:
        return FixRecord(path=path, blocks_removed=0, bytes_removed=0)

    bytes_removed = sum(len(m.group(0)) for m in matches)
    new_text = _DATAVIEW_BLOCK_RE.sub("\n", text)
    # Collapse triple+ newlines to double
    new_text = re.sub(r"\n{3,}", "\n\n", new_text)

    if not dry_run:
        tmp = path.with_suffix(path.suffix + ".tmp")
        tmp.write_text(new_text, encoding="utf-8")
        tmp.replace(path)

    return FixRecord(
        path=path, blocks_removed=len(matches), bytes_removed=bytes_removed,
    )


def run(target_dir: Path, *, dry_run: bool) -> tuple[list[FixRecord], dict[str, int]]:
    files = sorted(target_dir.rglob("*.md"))
    logger.info("Scanning %d markdown files in %s", len(files), target_dir)
    records = [fix_one(p, dry_run=dry_run) for p in files]
    touched = [r for r in records if r.blocks_removed > 0]
    stats = {
        "total_files": len(records),
        "files_touched": len(touched),
        "blocks_removed": sum(r.blocks_removed for r in records),
        "bytes_removed": sum(r.bytes_removed for r in records),
    }
    return records, stats


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="fix_dataview_links",
        description="Strip stale ```dataview LIST FROM [[...]] ``` blocks.",
        epilog=(
            "Examples:\n"
            "  python fix_dataview_links.py --dry-run\n"
            "  python fix_dataview_links.py\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--target-dir", type=Path, default=DEFAULT_TARGET_DIR,
                   help=f"Directory to scan (default: {DEFAULT_TARGET_DIR}).")
    p.add_argument("-n", "--dry-run", action="store_true",
                   help="Preview only; write no files.")
    p.add_argument("-v", "--verbose", action="count", default=0)
    p.add_argument("-q", "--quiet", action="store_true")
    p.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    return p


def configure_logging(verbosity: int, quiet: bool) -> None:
    if quiet:
        level = logging.ERROR
    elif verbosity >= 2:
        level = logging.DEBUG
    elif verbosity == 1:
        level = logging.INFO
    else:
        level = logging.WARNING
    logging.basicConfig(level=level,
                        format="%(asctime)s [%(levelname)s] %(message)s",
                        datefmt="%H:%M:%S")


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    configure_logging(args.verbose, args.quiet)

    if not args.target_dir.is_dir():
        logger.error("Target directory not found: %s", args.target_dir)
        return 2

    try:
        _, stats = run(args.target_dir, dry_run=args.dry_run)
    except KeyboardInterrupt:
        logger.warning("Interrupted")
        return 130
    except Exception:  # noqa: BLE001
        logger.exception("Unexpected error")
        return 1

    if stats["total_files"] == 0:
        logger.warning("No markdown files found in %s", args.target_dir)
        return 4

    print()
    print("=" * 64)
    tag = "  (DRY-RUN -- nothing written)" if args.dry_run else ""
    print(f"  DATAVIEW LINK FIXER SUMMARY{tag}")
    print("=" * 64)
    print(f"  Files scanned:         {stats['total_files']:>6}")
    print(f"  Files touched:         {stats['files_touched']:>6}")
    print(f"  Dataview blocks removed: {stats['blocks_removed']:>4}")
    print(f"  Bytes removed:         {stats['bytes_removed']:>6}")
    print("=" * 64)
    return 0


if __name__ == "__main__":
    sys.exit(main())
