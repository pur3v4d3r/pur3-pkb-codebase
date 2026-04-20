#!/usr/bin/env python3
"""
LOTR Verse Injection Script

Reads verse passage JSON files produced by the verse-identification agents,
then formats each verse block in LOTR-Formatted.md as an italicised blockquote:

  Before:   The Road goes ever on and on
            Down from the door where it began.

  After:    > *The Road goes ever on and on*
            > *Down from the door where it began.*

Input JSON format (array of objects):
  {
    "chapter":     "## Book I, Chapter 3: Three Is Company",
    "description": "Sam sings Road Goes Ever On",
    "lines":       ["The Road goes ever on and on ", ...]
  }
  Use "" (empty string) for blank lines within multi-stanza verses.

Run: python lotr_verse_inject.py
"""

import json
import os
import sys

VAULT  = r"d:\10_pur3v4d3r's-vault"
TARGET = os.path.join(VAULT, "LOTR-Formatted.md")

JSON_FILES = [
    os.path.join(VAULT, "_tmp_verse_tt1.json"),
    os.path.join(VAULT, "_tmp_verse_rt.json"),
]


# ─────────────────────────────────────────────────────────────────────────────
# CORE MATCHING & REPLACEMENT
# ─────────────────────────────────────────────────────────────────────────────

def format_verse_line(raw: str) -> str:
    """Wrap a single verse line in blockquote italic markup."""
    stripped = raw.rstrip()
    if not stripped:
        return ">\n"              # blank line within a multi-stanza verse
    # Preserve any existing **bold** or [[wiki-link]] markup inside the italic
    return f"> *{stripped}*\n"


def find_and_replace_verse(file_lines: list[str], verse_lines: list[str],
                           description: str) -> tuple[list[str], bool]:
    """
    Find the verse block in file_lines and replace it with formatted lines.

    Strategy:
    - Build a list of non-empty verse line texts (stripped) for matching.
    - Scan file_lines for the first non-empty verse line.
    - Verify the subsequent non-empty lines match the rest of the verse.
    - Replace the entire span (including embedded blank lines) with formatted text.

    Returns (updated_lines, success).
    """
    # Normalise verse: stripped content for comparison
    verse_nonempty = [l.strip() for l in verse_lines if l.strip()]
    if not verse_nonempty:
        print(f"    [SKIP] Empty verse: {description}")
        return file_lines, False

    first = verse_nonempty[0]
    n_file = len(file_lines)

    for start_i, line in enumerate(file_lines):
        line_stripped = line.strip()

        # Must match the first verse line
        if line_stripped != first:
            continue

        # Skip if already formatted as blockquote
        if line.lstrip().startswith(">"):
            continue

        # Walk forward through file to match all non-empty verse lines
        verse_idx = 0
        scan_i    = start_i
        span_end  = start_i  # exclusive end of the verse span in file

        while scan_i < n_file and verse_idx < len(verse_nonempty):
            fl = file_lines[scan_i].strip()
            if fl == verse_nonempty[verse_idx]:
                verse_idx += 1
                span_end = scan_i + 1
                scan_i   += 1
            elif fl == "":
                # blank line — allowed within verse span, keep scanning
                scan_i += 1
            else:
                break  # mismatch — this is not the right block

        if verse_idx < len(verse_nonempty):
            # Not a full match at this position; keep searching
            continue

        # ── Full match found: start_i..span_end ──────────────────────────────
        # Now rebuild that span using the *agent's* verse_lines list
        # (preserves intended stanza breaks and exact line order)
        new_block: list[str] = []

        # Determine if there are embedded blanks in the agent's verse_lines
        if any(l == "" for l in verse_lines):
            # Use the agent's lines directly (they include stanza structure)
            for vl in verse_lines:
                new_block.append(format_verse_line(vl))
        else:
            # Rebuild from file content in the span (preserves bold/wikilinks)
            for fl in file_lines[start_i:span_end]:
                new_block.append(format_verse_line(fl))

        result = file_lines[:start_i] + new_block + file_lines[span_end:]
        return result, True

    print(f"    [MISS] Not found in file: {description!r} — first line: {first!r}")
    return file_lines, False


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

def load_verses(json_path: str) -> list[dict]:
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    # Accept top-level array or {"verses": [...]}
    if isinstance(data, list):
        return data
    return data.get("verses", data.get("passages", []))


def main():
    print("Verse Injection Pass")
    print("=" * 45)

    # Verify target exists
    if not os.path.exists(TARGET):
        print(f"ERROR: Target not found: {TARGET}")
        sys.exit(1)

    # Collect all verses from available JSON files
    all_verses: list[dict] = []
    for jf in JSON_FILES:
        if os.path.exists(jf):
            verses = load_verses(jf)
            print(f"  Loaded {len(verses):>3} verses from {os.path.basename(jf)}")
            all_verses.extend(verses)
        else:
            print(f"  [SKIP] Not found: {os.path.basename(jf)}")

    if not all_verses:
        print("No verse JSON files found — nothing to do.")
        sys.exit(0)

    print(f"\n  Total verses to process: {len(all_verses)}")
    print(f"  Target file: {os.path.basename(TARGET)}")

    with open(TARGET, "r", encoding="utf-8") as f:
        lines = f.readlines()

    print(f"  File lines: {len(lines):,}\n")

    applied = 0
    missed  = 0

    for entry in all_verses:
        chapter     = entry.get("chapter", "Unknown")
        description = entry.get("description", "unnamed verse")
        verse_lines = entry.get("lines", [])

        label = f"[{chapter[-30:]}] {description}"
        lines, ok = find_and_replace_verse(lines, verse_lines, label)
        if ok:
            print(f"  OK   {label}")
            applied += 1
        else:
            missed += 1

    print(f"\nApplied: {applied}  |  Missed: {missed}")

    if applied:
        with open(TARGET, "w", encoding="utf-8") as f:
            f.writelines(lines)
        print(f"File updated: {os.path.basename(TARGET)}")

        # Quick stat check
        italic_bq = sum(1 for l in lines if l.startswith("> *"))
        print(f"Italic blockquote lines now in file: {italic_bq}")
    else:
        print("No changes written.")


if __name__ == "__main__":
    main()
