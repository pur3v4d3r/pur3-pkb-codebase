#!/usr/bin/env python3
"""
PKM Report Body Link Normaliser
================================
Replaces every variation of [[Report XX: ...]] in report bodies with [[Report XX]].

Handles all patterns found in the series:
  [[Report 01: Foundations of Knowledge Architecture]]
  [[Report 01: Foundations of Knowledge Architecture — How the Mind...]]
  [[Report 01 — Foundations of Knowledge Architecture]]
  [[Report 01: Schema Theory, Semantic Networks, Spreading Activation]]
  [[Report 01: Foundations of Knowledge Architecture|Report 01]]
  [[Report 01]]   ← already correct, left unchanged

All become: [[Report 01]]

IMPORTANT: Only changes body text. Frontmatter (aliases, feeds-into etc.)
is left completely untouched so existing metadata is preserved.

USAGE
-----
  # Preview changes (safe, writes nothing)
  python normalise_report_links.py --vault "D:\\path\\to\\report-series" --dry-run

  # Apply
  python normalise_report_links.py --vault "D:\\path\\to\\report-series"

  # Single report only
  python normalise_report_links.py --vault "D:\\path\\to\\report-series" --report 01
"""

import argparse
import re
import sys
from pathlib import Path

REPORT_GLOB = "*-*pkm-framework*.md"

# Matches [[Report XX: anything]] or [[Report XX — anything]] or [[Report XX|anything]]
# Capture group 1 = the two-digit (or one-digit) report number
LINK_RE = re.compile(
    r'\[\[Report\s+(\d+)(?:[:\s|—–-][^\]]+)?\]\]'
)


def extract_frontmatter_end(content):
    """
    Return the character position where the frontmatter ends (after closing ---).
    Body text starts from this position.
    Returns 0 if no frontmatter found (process whole file).
    """
    lines = content.split('\n')
    open_idx = None

    for i, line in enumerate(lines):
        s = line.strip()
        if s == '---':
            open_idx = i
            break
        elif s.startswith('#') or s == '':
            continue
        else:
            return 0  # no frontmatter

    if open_idx is None:
        return 0

    for i in range(open_idx + 1, len(lines)):
        if lines[i].strip() == '---':
            # Calculate char offset of the line AFTER the closing ---
            offset = sum(len(l) + 1 for l in lines[:i + 1])
            return offset

    return 0  # no closing --- found


def normalise_links(text):
    """Replace all [[Report XX: ...]] variations with [[Report XX]]."""
    def replacer(match):
        num = match.group(1).zfill(2)  # ensure two digits: 1 → 01
        canonical = f"[[Report {num}]]"
        original = match.group(0)
        return canonical if original != canonical else original

    return LINK_RE.sub(replacer, text)


def process_file(filepath, dry_run):
    content = filepath.read_text(encoding='utf-8')

    body_start = extract_frontmatter_end(content)
    frontmatter = content[:body_start]
    body = content[body_start:]

    new_body = normalise_links(body)

    if new_body == body:
        return {'file': filepath.name, 'status': 'unchanged', 'count': 0}

    # Count how many replacements were made
    original_links = LINK_RE.findall(body)
    new_links = LINK_RE.findall(new_body)
    replacements = sum(
        1 for m in LINK_RE.finditer(body)
        if m.group(0) != f"[[Report {m.group(1).zfill(2)}]]"
    )

    if not dry_run:
        filepath.write_text(frontmatter + new_body, encoding='utf-8')

    return {
        'file': filepath.name,
        'status': 'would_change' if dry_run else 'changed',
        'count': replacements,
        'examples': [
            m.group(0) for m in LINK_RE.finditer(body)
            if m.group(0) != f"[[Report {m.group(1).zfill(2)}]]"
        ][:5]  # show up to 5 examples per file
    }


def main():
    parser = argparse.ArgumentParser(
        description='Normalise all cross-report [[Report XX: ...]] links to [[Report XX]]'
    )
    parser.add_argument('--vault', required=True, help='Path to report-series folder')
    parser.add_argument('--dry-run', action='store_true', help='Preview only, no writes')
    parser.add_argument('--report', help='Process one report only, e.g. --report 01')
    args = parser.parse_args()

    vault = Path(args.vault).expanduser().resolve()
    if not vault.is_dir():
        print(f"ERROR: Folder not found: {vault}")
        sys.exit(1)

    files = sorted(vault.rglob(REPORT_GLOB))
    if args.report:
        files = [f for f in files if f.name.startswith(args.report.zfill(2) + '-')]

    if not files:
        print("No report files found.")
        sys.exit(1)

    mode = "DRY RUN — nothing will be written" if args.dry_run else "LIVE — files will be modified"
    print(f"\nReport Body Link Normaliser — {mode}")
    print(f"Vault : {vault}")
    print(f"Files : {len(files)}\n")
    print("─" * 65)

    total_replacements = 0
    changed = unchanged = 0

    for filepath in files:
        r = process_file(filepath, args.dry_run)

        if r['status'] in ('changed', 'would_change'):
            verb = "WOULD UPDATE" if args.dry_run else "UPDATED"
            print(f"\n{verb}: {r['file']}")
            print(f"  Links normalised: {r['count']}")
            if r['examples']:
                print(f"  Examples replaced:")
                for ex in r['examples']:
                    num = LINK_RE.match(ex).group(1).zfill(2)
                    print(f"    {ex}  →  [[Report {num}]]")
            total_replacements += r['count']
            changed += 1
        else:
            print(f"  OK (unchanged): {r['file']}")
            unchanged += 1

    print("\n" + "─" * 65)
    print(f"Files updated : {changed}")
    print(f"Files unchanged: {unchanged}")
    print(f"Total links normalised: {total_replacements}")

    if args.dry_run and changed > 0:
        print("\nRemove --dry-run to apply these changes.")


if __name__ == '__main__':
    main()
