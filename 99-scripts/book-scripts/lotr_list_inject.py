#!/usr/bin/env python3
"""
LOTR List Injection Script

Reads _tmp_lists.json produced by the Fellowship/Council list agent
and injects the formatted callout+list blocks into LOTR-Formatted.md
at the correct chapter locations.

The JSON specifies an `anchor_text` string — a few words of prose that
appear just before where the list should be inserted. The script finds
that anchor text in the correct chapter and inserts the list block
immediately after the paragraph containing it.

Run: python lotr_list_inject.py
"""

import json
import os
import re
import sys

VAULT  = r"d:\10_pur3v4d3r's-vault"
TARGET = os.path.join(VAULT, "LOTR-Formatted.md")
LISTS_FILE = os.path.join(VAULT, "_tmp_lists.json")


def find_chapter_start(lines: list[str], chapter_heading: str) -> int:
    """Return line index of the chapter heading, or -1 if not found."""
    for i, line in enumerate(lines):
        if line.strip() == chapter_heading:
            return i
    return -1


def find_next_chapter_start(lines: list[str], from_i: int) -> int:
    """Return line index of the next ## heading after from_i."""
    for i in range(from_i + 1, len(lines)):
        if lines[i].startswith("## "):
            return i
    return len(lines)


def find_anchor(lines: list[str], chapter_start: int, chapter_end: int,
                anchor_text: str) -> int:
    """
    Find the end of the paragraph containing anchor_text within the chapter.
    Returns the line index AFTER the paragraph (insertion point).
    """
    anchor_lower = anchor_text.lower().strip()

    for i in range(chapter_start, chapter_end):
        if anchor_lower in lines[i].lower():
            # Walk forward to end of paragraph (first blank line)
            j = i + 1
            while j < chapter_end and lines[j].strip() != "":
                j += 1
            return j  # insert after the blank line

    return -1


def inject_block(lines: list[str], insert_at: int, markdown: str) -> list[str]:
    """Insert markdown block at insert_at index, with surrounding blank lines."""
    block_lines = []

    # Ensure blank line before block
    if insert_at > 0 and lines[insert_at - 1].strip() != "":
        block_lines.append("\n")

    # Add the markdown content
    for ml in markdown.splitlines():
        block_lines.append(ml + "\n")

    # Ensure blank line after block
    block_lines.append("\n")

    return lines[:insert_at] + block_lines + lines[insert_at:]


def main():
    print("List Injection Pass")
    print("=" * 45)

    if not os.path.exists(LISTS_FILE):
        print(f"ERROR: {LISTS_FILE} not found")
        sys.exit(1)

    if not os.path.exists(TARGET):
        print(f"ERROR: {TARGET} not found")
        sys.exit(1)

    with open(LISTS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    with open(TARGET, "r", encoding="utf-8") as f:
        lines = f.readlines()

    print(f"  File lines: {len(lines):,}")
    injected = 0

    for key, entry in data.items():
        chapter_heading = entry.get("chapter_heading", "")
        anchor_text     = entry.get("anchor_text", "")
        markdown        = entry.get("markdown", "").strip()

        print(f"\n  [{key}]")
        print(f"    Chapter: {chapter_heading}")
        print(f"    Anchor:  {anchor_text!r}")

        if not markdown:
            print("    [SKIP] Empty markdown")
            continue

        ch_start = find_chapter_start(lines, chapter_heading)
        if ch_start == -1:
            print(f"    [MISS] Chapter heading not found")
            continue

        ch_end = find_next_chapter_start(lines, ch_start)

        # Check if block already injected (avoid duplicates)
        chapter_text = "".join(lines[ch_start:ch_end])
        first_line_of_block = markdown.splitlines()[0]
        if first_line_of_block in chapter_text:
            print(f"    [SKIP] Already injected")
            continue

        insert_at = find_anchor(lines, ch_start, ch_end, anchor_text)
        if insert_at == -1:
            # Fallback: insert right after the chapter heading + any blanks
            insert_at = ch_start + 1
            while insert_at < ch_end and lines[insert_at].strip() == "":
                insert_at += 1
            print(f"    [WARN] Anchor not found — inserting at chapter top (line {insert_at})")
        else:
            print(f"    Inserting after line {insert_at}")

        lines = inject_block(lines, insert_at, markdown)
        injected += 1
        print(f"    OK — block injected ({len(markdown.splitlines())} lines)")

    print(f"\nTotal injected: {injected}")

    if injected:
        with open(TARGET, "w", encoding="utf-8") as f:
            f.writelines(lines)
        print(f"File updated: {os.path.basename(TARGET)}")
    else:
        print("No changes written.")


if __name__ == "__main__":
    main()
