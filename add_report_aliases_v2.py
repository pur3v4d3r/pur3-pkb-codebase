#!/usr/bin/env python3
"""
PKM Report Alias Fixer v2
=========================
Fixes v1's gap: --force rewrites ALL files regardless of unchanged status,
guaranteeing brackets are removed and all canonical aliases are present.

USAGE
-----
  # Dry run (safe preview)
  python add_report_aliases_v2.py --vault "D:\\path\\to\\vault" --dry-run

  # Normal run (only changes files that need it)
  python add_report_aliases_v2.py --vault "D:\\path\\to\\vault" --backup

  # Force rewrite ALL files (use this if normal run shows all unchanged
  # but links still don't resolve in Obsidian)
  python add_report_aliases_v2.py --vault "D:\\path\\to\\vault" --force --backup
"""

import argparse
import glob
import os
import re
import shutil
import sys
from pathlib import Path

REPORT_GLOB = "*-*pkm-framework*.md"
EM_DASH = "\u2014"
H1_RE = re.compile(r'^#\s+(Report\s+\d+\s*:.*)', re.MULTILINE)
ALIASES_BLOCK_RE = re.compile(
    r'^aliases:\s*\n((?:[ \t]+-[^\n]*\n)*)',
    re.MULTILINE
)
BRACKETS_RE = re.compile(r'^\[\[(.+)\]\]$')


def strip_brackets(text: str) -> str:
    m = BRACKETS_RE.match(text.strip())
    return m.group(1) if m else text.strip()


def has_brackets(text: str) -> bool:
    return bool(BRACKETS_RE.match(text.strip()))


def parse_aliases_raw(block_text: str) -> list[tuple[str, str]]:
    """
    Returns list of (raw_value, clean_value) tuples.
    raw_value  = exactly what's in the file (may have [[brackets]])
    clean_value = brackets stripped, quotes stripped
    """
    results = []
    for line in block_text.splitlines():
        match = re.match(r'^\s+-\s+"?(.+?)"?\s*$', line)
        if match:
            raw = match.group(1).strip('"').strip("'")
            clean = strip_brackets(raw)
            results.append((raw, clean))
    return results


def build_aliases_block(aliases: list[str]) -> str:
    lines = ["aliases:"]
    for alias in aliases:
        if ':' in alias or '"' in alias or "'" in alias or '[' in alias:
            safe = alias.replace('"', '\\"')
            lines.append(f'  - "{safe}"')
        else:
            lines.append(f"  - {alias}")
    return "\n".join(lines) + "\n"


def extract_frontmatter_bounds(content: str):
    lines = content.split('\n')
    open_idx = None
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped == '---':
            open_idx = i
            break
        elif stripped.startswith('#') or stripped == '':
            continue
        else:
            return None
    if open_idx is None:
        return None
    close_idx = None
    for i in range(open_idx + 1, len(lines)):
        if lines[i].strip() == '---':
            close_idx = i
            break
    if close_idx is None:
        return None
    char_offsets = [0]
    for line in lines:
        char_offsets.append(char_offsets[-1] + len(line) + 1)
    return (char_offsets[open_idx], char_offsets[close_idx + 1])


def derive_canonical_aliases(h1_title: str) -> list[str]:
    full = h1_title.strip()
    num_match = re.match(r'Report\s+(\d+)', full)
    bare = f"Report {num_match.group(1)}" if num_match else None
    if EM_DASH in full:
        short = full.split(EM_DASH)[0].strip()
    else:
        short = full
    aliases = []
    if bare:
        aliases.append(bare)
    if short != full:
        aliases.append(short)
    aliases.append(full)
    return aliases


def process_file(filepath: Path, dry_run: bool, backup: bool, force: bool) -> dict:
    content = filepath.read_text(encoding='utf-8')
    result = {
        'file': filepath.name,
        'status': 'unchanged',
        'h1': None,
        'aliases_added': [],
        'aliases_cleaned': [],
        'error': None,
    }

    h1_match = H1_RE.search(content)
    if not h1_match:
        result['status'] = 'skipped'
        result['error'] = 'No "# Report XX:" heading found'
        return result

    h1_title = h1_match.group(1).strip()
    result['h1'] = h1_title
    canonical = derive_canonical_aliases(h1_title)

    bounds = extract_frontmatter_bounds(content)
    if bounds is None:
        result['status'] = 'skipped'
        result['error'] = 'Could not locate YAML frontmatter'
        return result

    fm_start, fm_end = bounds
    frontmatter = content[fm_start:fm_end]

    aliases_match = ALIASES_BLOCK_RE.search(frontmatter)

    if aliases_match:
        raw_pairs = parse_aliases_raw(aliases_match.group(1))
        existing_clean = [clean for (_, clean) in raw_pairs]

        # Detect brackets that need cleaning
        for (raw, clean) in raw_pairs:
            if has_brackets(raw) or raw != clean:
                result['aliases_cleaned'].append(clean)

        # Detect missing canonical aliases
        for alias in canonical:
            if alias not in existing_clean:
                result['aliases_added'].append(alias)
    else:
        existing_clean = []
        result['aliases_added'] = canonical[:]

    needs_change = (
        bool(result['aliases_added']) or
        bool(result['aliases_cleaned']) or
        force
    )

    if not needs_change:
        result['status'] = 'unchanged'
        return result

    result['status'] = 'would_change' if dry_run else 'changed'

    if dry_run:
        return result

    # Build merged alias list — canonical first, then any extras
    merged = list(canonical)
    for clean in existing_clean:
        if clean not in merged:
            merged.append(clean)

    new_aliases_block = build_aliases_block(merged)

    if aliases_match:
        old_block_text = aliases_match.group(0)
        new_frontmatter = frontmatter.replace(old_block_text, new_aliases_block, 1)
    else:
        closing = '\n---\n'
        insert_pos = frontmatter.rfind(closing)
        if insert_pos == -1:
            result['status'] = 'skipped'
            result['error'] = 'Cannot find closing --- to insert aliases'
            return result
        new_frontmatter = (
            frontmatter[:insert_pos] + '\n' +
            new_aliases_block +
            frontmatter[insert_pos:]
        )

    new_content = content[:fm_start] + new_frontmatter + content[fm_end:]

    if backup:
        shutil.copy2(filepath, filepath.with_suffix('.md.bak'))

    filepath.write_text(new_content, encoding='utf-8')
    return result


def main():
    parser = argparse.ArgumentParser(
        description='Add standard aliases to PKM framework report files (v2).'
    )
    parser.add_argument('--vault', required=True)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--backup', action='store_true')
    parser.add_argument('--force', action='store_true',
        help='Rewrite ALL files even if they appear unchanged. Use this if '
             'links still do not resolve in Obsidian after a normal run.')
    parser.add_argument('--report', help='Process only this report number, e.g. --report 01')
    args = parser.parse_args()

    vault_path = Path(args.vault).expanduser().resolve()
    if not vault_path.is_dir():
        print(f"ERROR: Path not found: {vault_path}")
        sys.exit(1)

    all_files = sorted(vault_path.rglob(REPORT_GLOB))
    if args.report:
        target = args.report.zfill(2)
        all_files = [f for f in all_files if f.name.startswith(target + '-')]

    if not all_files:
        print("No matching report files found.")
        sys.exit(1)

    mode = 'DRY RUN' if args.dry_run else ('FORCE REWRITE' if args.force else 'LIVE RUN')
    print(f"\nPKM Report Alias Fixer v2 — {mode}")
    print(f"Vault : {vault_path}")
    print(f"Files : {len(all_files)}\n")
    print("─" * 70)

    changed = unchanged = skipped = 0

    for filepath in all_files:
        result = process_file(filepath, args.dry_run, args.backup, args.force)
        status = result['status']

        if status in ('changed', 'would_change'):
            verb = "WOULD UPDATE" if args.dry_run else "UPDATED"
            print(f"\n{verb}: {result['file']}")
            print(f"  H1    : {result['h1']}")
            if result['aliases_added']:
                print(f"  Add   : {result['aliases_added']}")
            if result['aliases_cleaned']:
                print(f"  Clean : {result['aliases_cleaned']} (removing [[brackets]])")
            if args.force and not result['aliases_added'] and not result['aliases_cleaned']:
                print(f"  (force rewrite — content already correct, re-saving cleanly)")
            changed += 1
        elif status == 'unchanged':
            print(f"  OK : {result['file']}")
            unchanged += 1
        else:
            print(f"  SKIP : {result['file']} — {result['error']}")
            skipped += 1

    print("\n" + "─" * 70)
    print(f"Summary: {changed} {'to update' if args.dry_run else 'updated'} | "
          f"{unchanged} unchanged | {skipped} skipped")

    if args.dry_run and changed > 0:
        print("\nRemove --dry-run to apply.")
    
    if not args.dry_run and not args.force:
        print("\nIf links still don't resolve in Obsidian after a full restart,")
        print("run again with --force to guarantee all files are rewritten cleanly.")


if __name__ == '__main__':
    main()
