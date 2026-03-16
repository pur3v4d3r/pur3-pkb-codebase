#!/usr/bin/env python3
"""
PKM Report Link → Filename Replacer
=====================================
Replaces every [[Report XX: ...]] variation in report bodies with the
actual filename of that report (without .md), which Obsidian resolves
perfectly without needing any aliases at all.

Example:
  [[Report 01: Foundations of Knowledge Architecture — How the Mind...]]
  [[Report 01: Schema Theory, Semantic Networks]]
  [[Report 01 — Foundations of Knowledge Architecture]]
  [[Report 01: Foundations of Knowledge Architecture|Report 01]]
  [[Report 01]]

All become:
  [[01-foundations-of-knowledge-architecture-pkm-framework-2026-03-13]]

Only the body text is changed. Frontmatter is left completely untouched.

USAGE
-----
  # Safe preview — writes nothing
  python link_to_filename.py --vault "D:\\path\\to\\report-series" --dry-run

  # Apply
  python link_to_filename.py --vault "D:\\path\\to\\report-series"
"""

import argparse
import re
import sys
from pathlib import Path

REPORT_GLOB = "*-*pkm-framework*.md"

# Maps report number (as int) → filename stem (no .md)
REPORT_FILENAMES = {
    1:  "01-foundations-of-knowledge-architecture-pkm-framework-2026-03-13",
    2:  "02-architecture-of-learning-pkm-framework-2026-03-13",
    3:  "03-constructing-understanding-pkm-framework-2026-03-13",
    4:  "04-metacognitive-self-regulation-pkm-framework-2026-03-13",
    5:  "05-motivation-architecture-pkm-framework-2026-03-13",
    6:  "06-science-of-remembering-pkm-framework-2026-03-13",
    7:  "07-critical-thinking-pkm-practice-pkm-framework-2026-03-14",
    8:  "08-reflective-practice-experiential-learning-pkm-framework-2026-03-14",
    9:  "09-designing-the-learning-pkb-pkm-framework-2026-03-14",
    10: "10-scaffolding-and-fading-pkm-framework-2026-03-14",
    11: "11-transfer-problem-pkm-framework-2026-03-14",
    12: "12-reflective-pkb-metacognitive-monitoring-pkm-framework-2026-03-14",
    13: "13-emotional-regulation-resilient-learning-pkm-framework-2026-03-14",
    14: "14-inquiry-based-knowledge-building-pkm-framework-2026-03-14",
    15: "15-knowledge-organization-at-scale-pkm-framework-2026-03-14",
    16: "16-desirable-difficulties-by-design-pkm-framework-2026-03-14",
    17: "17-note-making-knowledge-construction-pkm-framework-2026-03-14",
    18: "18-calibration-epistemic-humility-pkm-framework-2026-03-15",
    19: "19-sustaining-lifelong-learning-pkm-framework-2026-03-15",
    20: "20-retrieval-enhanced-knowledge-networks-pkm-framework-2026-03-15",
    21: "21-dialectical-knowledge-building-pkm-framework-2026-03-15",
    22: "22-tacit-knowledge-limits-of-capture-pkm-framework-2026-03-15",
    23: "23-learning-environments-design-pkm-framework-2026-03-15",
    24: "24-self-determined-learning-pkm-framework-2026-03-15",
    25: "25-integration-problem-pkm-framework-2026-03-15",
    26: "26-feedback-loops-pkm-framework-2026-03-15",
    27: "27-complete-pkm-pkb-design-framework-pkm-framework-2026-03-15",
    28: "28-philosophy-of-personal-knowledge-pkm-framework-2026-03-15",
    29: "29-ethical-pkm-pkm-framework-2026-03-15",
    30: "30-future-pkm-ai-enhanced-knowledge-building-pkm-framework-2026-03-15",
}

# Matches any [[Report XX ...]] pattern — with anything after the number
LINK_RE = re.compile(r'\[\[Report\s+(\d+)(?:[^\]]+)?\]\]')


def extract_frontmatter_end(content):
    """Return char offset where frontmatter ends. Body starts here."""
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
            return 0
    if open_idx is None:
        return 0
    for i in range(open_idx + 1, len(lines)):
        if lines[i].strip() == '---':
            return sum(len(l) + 1 for l in lines[:i + 1])
    return 0


def replace_links(text):
    """Replace all [[Report XX...]] with [[filename-stem]]."""
    replacements = []

    def replacer(match):
        num = int(match.group(1))
        filename = REPORT_FILENAMES.get(num)
        if not filename:
            return match.group(0)  # unknown number — leave alone
        original = match.group(0)
        new_link = f"[[{filename}]]"
        if original != new_link:
            replacements.append((original, new_link))
        return new_link

    new_text = LINK_RE.sub(replacer, text)
    return new_text, replacements


def process_file(filepath, dry_run):
    content = filepath.read_text(encoding='utf-8')

    body_start = extract_frontmatter_end(content)
    frontmatter = content[:body_start]
    body = content[body_start:]

    new_body, replacements = replace_links(body)

    if not replacements:
        return {'file': filepath.name, 'status': 'unchanged', 'replacements': []}

    if not dry_run:
        filepath.write_text(frontmatter + new_body, encoding='utf-8')

    return {
        'file': filepath.name,
        'status': 'would_change' if dry_run else 'changed',
        'replacements': replacements,
    }


def main():
    parser = argparse.ArgumentParser(
        description='Replace [[Report XX: ...]] links with [[actual-filename]] links.'
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
    print(f"\nReport Link → Filename Replacer — {mode}")
    print(f"Vault  : {vault}")
    print(f"Files  : {len(files)}\n")
    print("─" * 65)

    total = 0
    changed = unchanged = 0

    for filepath in files:
        r = process_file(filepath, args.dry_run)

        if r['status'] in ('changed', 'would_change'):
            verb = "WOULD UPDATE" if args.dry_run else "UPDATED"
            print(f"\n{verb}: {r['file']}")
            print(f"  Links replaced: {len(r['replacements'])}")
            for old, new in r['replacements'][:4]:  # show up to 4 examples
                print(f"    {old}")
                print(f"    → {new}")
            if len(r['replacements']) > 4:
                print(f"    ... and {len(r['replacements']) - 4} more")
            total += len(r['replacements'])
            changed += 1
        else:
            print(f"  OK (unchanged): {r['file']}")
            unchanged += 1

    print("\n" + "─" * 65)
    print(f"Files updated  : {changed}")
    print(f"Files unchanged: {unchanged}")
    print(f"Total links replaced: {total}")

    if args.dry_run and changed > 0:
        print("\nRemove --dry-run to apply.")


if __name__ == '__main__':
    main()
