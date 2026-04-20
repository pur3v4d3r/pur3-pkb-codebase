#!/usr/bin/env python3
"""
LOTR Summary Injection Script — Phase 3c

Reads chapter summaries from _tmp_summaries.json and replaces
[SUMMARY PLACEHOLDER: heading] markers in the three volume files.

Input:  _tmp_book_fellowship.md, _tmp_book_twotowers.md, _tmp_book_return.md
        _tmp_summaries.json
Output: Same files, updated in-place

Run: python lotr_inject_summaries.py
"""

import re
import os
import sys
import json

VAULT = r"d:\10_pur3v4d3r's-vault"

VOLUME_FILES = [
    os.path.join(VAULT, "_tmp_book_fellowship.md"),
    os.path.join(VAULT, "_tmp_book_twotowers.md"),
    os.path.join(VAULT, "_tmp_book_return.md"),
]

SUMMARIES_FILE = os.path.join(VAULT, "_tmp_summaries.json")

PLACEHOLDER_RE = re.compile(r"^\> \[SUMMARY PLACEHOLDER: (.*?)\]\s*$")


def load_summaries() -> dict[str, str]:
    with open(SUMMARIES_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    # Accept either flat dict or {"summaries": {...}}
    if isinstance(data, dict) and "summaries" in data:
        return data["summaries"]
    return data


def inject_into_file(path: str, summaries: dict[str, str]) -> tuple[int, int]:
    """Replace placeholders in file. Returns (replaced_count, missing_count)."""
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    out_lines = []
    replaced = 0
    missing = 0

    for line in lines:
        m = PLACEHOLDER_RE.match(line)
        if m:
            heading = m.group(1).strip()
            summary_text = summaries.get(heading)
            if summary_text:
                out_lines.append(f"> {summary_text.strip()}\n")
                replaced += 1
            else:
                # Leave placeholder if no summary found; warn
                out_lines.append(line)
                print(f"  [WARN] No summary for: {heading}")
                missing += 1
        else:
            out_lines.append(line)

    with open(path, "w", encoding="utf-8") as f:
        f.writelines(out_lines)

    return replaced, missing


def main():
    print("Phase 3c: Injecting Chapter Summaries")
    print("=" * 45)

    # Check inputs
    if not os.path.exists(SUMMARIES_FILE):
        print(f"ERROR: Summaries file not found: {SUMMARIES_FILE}")
        sys.exit(1)

    missing_vols = [p for p in VOLUME_FILES if not os.path.exists(p)]
    if missing_vols:
        print("ERROR: Missing volume files:")
        for m in missing_vols:
            print(f"  {m}")
        sys.exit(1)

    summaries = load_summaries()
    print(f"Loaded {len(summaries)} summaries from {os.path.basename(SUMMARIES_FILE)}")

    total_replaced = 0
    total_missing  = 0

    for path in VOLUME_FILES:
        print(f"\n  {os.path.basename(path)}")
        replaced, missing = inject_into_file(path, summaries)
        print(f"    Replaced: {replaced}  |  Missing: {missing}")
        total_replaced += replaced
        total_missing  += missing

    print(f"\nDone. Total replaced: {total_replaced} / {total_replaced + total_missing}")
    if total_missing:
        print(f"WARNING: {total_missing} placeholder(s) remain unfilled.")
    else:
        print("All placeholders filled.")
    print("\nNext: python lotr_assemble.py")


if __name__ == "__main__":
    main()
