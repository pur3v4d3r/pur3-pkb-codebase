#!/usr/bin/env python3
"""
generate_toc.py
───────────────────────────────────────────────────────────────────────────────
Generate and insert a Markdown Table of Contents into any Markdown file.

FEATURES:
  - Skips YAML frontmatter blocks (--- delimiters) automatically
  - Inserts the TOC after frontmatter and any leading H1 title (configurable)
  - Produces GitHub/Obsidian-compatible anchor links
  - Wraps the TOC in sentinel comments so the script can detect and replace
    an existing TOC on re-run (idempotent)
  - Dry-run mode by default — pass --execute to apply changes
  - Backs up the original file before writing (configurable)

USAGE:
  python generate_toc.py <file.md>                 # dry-run (preview only)
  python generate_toc.py <file.md> --execute       # write TOC into file
  python generate_toc.py <file.md> --execute --no-backup  # skip backup
  python generate_toc.py <file.md> --min-depth 2   # skip H1 headings in TOC
  python generate_toc.py <file.md> --max-depth 3   # include H1-H3 only

REQUIREMENTS:
  Pure stdlib — no pip installs required.

SENTINEL COMMENTS (placed around the generated block):
  <!-- TOC START -->
  <!-- TOC END -->

ANCHOR ALGORITHM (GitHub/Obsidian compatible):
  1. Strip leading `#` and whitespace from heading text
  2. Lowercase
  3. Remove characters that are not letters, digits, spaces, or hyphens
  4. Replace spaces with hyphens
  5. Collapse runs of hyphens to a single hyphen

@version  1.0.0
"""

import re
import sys
import shutil
import argparse
import datetime
from pathlib import Path
from typing import NamedTuple


# ── CONFIGURATION — edit these defaults to suit your vault ───────────────────
CONFIG = {
    # Minimum heading depth to include in TOC (1 = H1, 2 = H2, …)
    "min_depth": 1,
    # Maximum heading depth to include in TOC (6 = include all)
    "max_depth": 6,
    # Indentation string per depth level below the minimum
    "indent": "  ",
    # Bullet character for TOC entries
    "bullet": "-",
    # Whether to skip a leading H1 title (the note title) from the TOC body
    # The TOC will still be *placed* after it; the H1 just won't appear in the list.
    "skip_first_h1": False,
    # Place the TOC *after* any leading H1 (True) or right after frontmatter (False)
    "insert_after_h1": True,
    # Create a timestamped .bak file before writing
    "backup": True,
    # Name of the heading printed above the TOC block (empty string = no heading)
    "toc_heading": "## Table of Contents",
    # Sentinel comment tags wrapping the TOC block
    "sentinel_start": "<!-- TOC START -->",
    "sentinel_end": "<!-- TOC END -->",
}
# ─────────────────────────────────────────────────────────────────────────────

# Regex that matches a markdown heading line
_HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)(?:\s+#+)?$")


class Heading(NamedTuple):
    depth: int        # 1–6
    text: str         # raw heading text (no leading #)
    line_index: int   # 0-based index in the file lines


# ── Anchor generation ─────────────────────────────────────────────────────────

def _to_anchor(text: str) -> str:
    """
    Convert heading text to a GitHub/Obsidian-compatible anchor slug.

    Example:
      "1.1 Memory & Information Processing"
      → "11-memory--information-processing"
      (dots stripped, & stripped, spaces → hyphens)
    """
    text = text.lower()
    # Keep only letters, digits, spaces, and hyphens
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    # Collapse whitespace to a single space, then replace with hyphen
    text = re.sub(r"\s+", "-", text.strip())
    # Collapse multiple consecutive hyphens
    text = re.sub(r"-{2,}", "-", text)
    # Strip leading/trailing hyphens
    text = text.strip("-")
    return text


# ── Frontmatter detection ─────────────────────────────────────────────────────

def _find_frontmatter_end(lines: list[str]) -> int:
    """
    Return the index of the line immediately *after* the closing `---` of a
    YAML frontmatter block, or 0 if no frontmatter is present.
    """
    if not lines or lines[0].rstrip() != "---":
        return 0
    for i in range(1, len(lines)):
        if lines[i].rstrip() in ("---", "..."):
            return i + 1
    return 0  # unclosed frontmatter — treat as no frontmatter


# ── Heading extraction ────────────────────────────────────────────────────────

def _extract_headings(lines: list[str], start: int, min_depth: int, max_depth: int) -> list[Heading]:
    """
    Parse heading lines in `lines[start:]` and return Heading entries
    within [min_depth, max_depth].
    """
    headings: list[Heading] = []
    in_code_block = False

    for idx in range(start, len(lines)):
        line = lines[idx]

        # Track fenced code blocks so we don't pick up headings inside them
        if line.startswith("```") or line.startswith("~~~"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue

        m = _HEADING_RE.match(line)
        if m:
            depth = len(m.group(1))
            text = m.group(2).strip()
            if min_depth <= depth <= max_depth:
                headings.append(Heading(depth=depth, text=text, line_index=idx))

    return headings


# ── TOC generation ────────────────────────────────────────────────────────────

def _build_toc_lines(headings: list[Heading], min_depth: int, indent: str, bullet: str) -> list[str]:
    """
    Build the TOC as a list of raw markdown lines (no trailing newline).
    Depth indentation is relative to `min_depth`.
    """
    # Track duplicate anchors and append -N suffix as GitHub does
    anchor_counts: dict[str, int] = {}
    toc_lines: list[str] = []

    for h in headings:
        anchor = _to_anchor(h.text)
        count = anchor_counts.get(anchor, 0)
        anchor_counts[anchor] = count + 1
        if count > 0:
            anchor = f"{anchor}-{count}"

        padding = indent * (h.depth - min_depth)
        toc_lines.append(f"{padding}{bullet} [{h.text}](#{anchor})")

    return toc_lines


# ── Sentinel block helpers ────────────────────────────────────────────────────

def _find_existing_toc_range(lines: list[str], sentinel_start: str, sentinel_end: str) -> tuple[int, int] | None:
    """
    Return (start_index, end_index_exclusive) of an existing TOC block,
    or None if not found.  Both sentinel lines are included in the range.
    """
    start_idx = None
    for i, line in enumerate(lines):
        if line.strip() == sentinel_start:
            start_idx = i
        elif line.strip() == sentinel_end and start_idx is not None:
            return start_idx, i + 1
    return None


# ── Insertion-point detection ─────────────────────────────────────────────────

def _find_insertion_point(lines: list[str], fm_end: int, insert_after_h1: bool) -> int:
    """
    Return the line index where the TOC block should be inserted.

    If `insert_after_h1` is True, scan for the first H1 after the frontmatter
    and insert after it (plus any immediately following blank lines).
    Otherwise, insert directly after the frontmatter.
    """
    if not insert_after_h1:
        return fm_end

    # Look for the first H1 heading after frontmatter
    for i in range(fm_end, len(lines)):
        if _HEADING_RE.match(lines[i]) and lines[i].startswith("# "):
            # Skip past the H1 and any blank lines that follow
            j = i + 1
            while j < len(lines) and lines[j].strip() == "":
                j += 1
            return j

    # No H1 found — fall back to right after frontmatter
    return fm_end


# ── Main logic ────────────────────────────────────────────────────────────────

def process_file(
    filepath: Path,
    min_depth: int,
    max_depth: int,
    indent: str,
    bullet: str,
    skip_first_h1: bool,
    insert_after_h1: bool,
    toc_heading: str,
    sentinel_start: str,
    sentinel_end: str,
    execute: bool,
    backup: bool,
) -> None:

    if not filepath.exists():
        print(f"ERROR: File not found: {filepath}", file=sys.stderr)
        sys.exit(1)

    if filepath.suffix.lower() not in (".md", ".markdown"):
        print(f"WARNING: '{filepath.name}' does not look like a Markdown file.")

    lines = filepath.read_text(encoding="utf-8").splitlines()

    # ── Detect frontmatter ────────────────────────────────────────────────────
    fm_end = _find_frontmatter_end(lines)

    # ── Extract headings (skip everything inside an existing TOC block) ───────
    existing_toc_range = _find_existing_toc_range(lines, sentinel_start, sentinel_end)

    # Build a copy of lines without the existing TOC to extract headings cleanly
    if existing_toc_range:
        toc_start, toc_end = existing_toc_range
        lines_for_headings = lines[:toc_start] + lines[toc_end:]
        heading_start = fm_end
    else:
        lines_for_headings = lines
        heading_start = fm_end

    headings = _extract_headings(lines_for_headings, heading_start, min_depth, max_depth)

    # Optionally skip the very first H1 from the TOC entries
    if skip_first_h1 and headings and headings[0].depth == 1:
        headings = headings[1:]

    if not headings:
        print("No headings found matching the specified depth range. Nothing to do.")
        return

    # Adjust min_depth to the shallowest heading actually present
    actual_min = min(h.depth for h in headings)

    # ── Build TOC block ───────────────────────────────────────────────────────
    toc_inner = _build_toc_lines(headings, actual_min, indent, bullet)

    toc_block: list[str] = []
    toc_block.append(sentinel_start)
    if toc_heading:
        toc_block.append("")
        toc_block.append(toc_heading)
        toc_block.append("")
    toc_block.extend(toc_inner)
    toc_block.append("")
    toc_block.append(sentinel_end)

    # ── Determine where to place the TOC ─────────────────────────────────────
    if existing_toc_range:
        # Replace existing block in-place
        new_lines = (
            lines[:existing_toc_range[0]]
            + toc_block
            + lines[existing_toc_range[1]:]
        )
        action = "Replaced existing TOC"
    else:
        # Fresh insertion — work on the full lines list
        insert_at = _find_insertion_point(lines, fm_end, insert_after_h1)
        new_lines = (
            lines[:insert_at]
            + [""]
            + toc_block
            + [""]
            + lines[insert_at:]
        )
        action = f"Inserted TOC at line {insert_at + 1}"

    # ── Preview / output ──────────────────────────────────────────────────────
    print(f"\n{'─'*60}")
    print(f"File   : {filepath}")
    print(f"Action : {action}")
    print(f"Entries: {len(toc_inner)} headings (H{actual_min}–H{max_depth})")
    print(f"{'─'*60}")
    print("\nGenerated TOC preview:\n")
    for line in toc_block:
        print(f"  {line}")
    print()

    if not execute:
        print("DRY RUN — no changes written.  Pass --execute to apply.\n")
        return

    # ── Write ─────────────────────────────────────────────────────────────────
    if backup:
        ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        backup_path = filepath.with_suffix(f".{ts}.bak")
        shutil.copy2(filepath, backup_path)
        print(f"Backup : {backup_path}")

    filepath.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
    print(f"Written: {filepath}\n")


# ── CLI ───────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate and insert a Table of Contents into a Markdown file.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("file", help="Path to the Markdown file")
    parser.add_argument(
        "--execute",
        action="store_true",
        default=False,
        help="Write the TOC to the file (default: dry run only)",
    )
    parser.add_argument(
        "--no-backup",
        action="store_true",
        default=False,
        help="Skip creating a .bak file before writing",
    )
    parser.add_argument(
        "--min-depth",
        type=int,
        default=CONFIG["min_depth"],
        metavar="N",
        help=f"Minimum heading depth to include (default: {CONFIG['min_depth']})",
    )
    parser.add_argument(
        "--max-depth",
        type=int,
        default=CONFIG["max_depth"],
        metavar="N",
        help=f"Maximum heading depth to include (default: {CONFIG['max_depth']})",
    )
    parser.add_argument(
        "--skip-h1",
        action="store_true",
        default=CONFIG["skip_first_h1"],
        help="Exclude the first H1 (document title) from the TOC entries",
    )
    parser.add_argument(
        "--no-h1-insert",
        action="store_true",
        default=False,
        help="Insert TOC immediately after frontmatter, not after the first H1",
    )

    args = parser.parse_args()

    process_file(
        filepath=Path(args.file),
        min_depth=args.min_depth,
        max_depth=args.max_depth,
        indent=CONFIG["indent"],
        bullet=CONFIG["bullet"],
        skip_first_h1=args.skip_h1,
        insert_after_h1=not args.no_h1_insert,
        toc_heading=CONFIG["toc_heading"],
        sentinel_start=CONFIG["sentinel_start"],
        sentinel_end=CONFIG["sentinel_end"],
        execute=args.execute,
        backup=not args.no_backup,
    )


if __name__ == "__main__":
    main()
