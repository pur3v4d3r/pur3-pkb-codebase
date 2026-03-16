#!/usr/bin/env python3
"""
PKM Alias Quote Fixer
=====================
Rewrites all report aliases using single quotes instead of double quotes.
Single-quoted YAML strings are the safest format for Obsidian when aliases
contain colons — the parser never misreads them as key-value separators.

USAGE
-----
  # Preview first
  python fix_alias_quotes.py --vault "D:\path\to\report-series" --dry-run

  # Apply
  python fix_alias_quotes.py --vault "D:\path\to\report-series"
"""

import argparse
import re
import sys
from pathlib import Path

REPORT_GLOB = "*-*pkm-framework*.md"
EM_DASH = "\u2014"
H1_RE = re.compile(r'^#\s+(Report\s+\d+\s*:.*)', re.MULTILINE)
ALIASES_BLOCK_RE = re.compile(r'^aliases:\s*\n((?:[ \t]+-[^\n]*\n)*)', re.MULTILINE)
BRACKETS_RE = re.compile(r'^\[\[(.+)\]\]$')


def strip_brackets(text):
    m = BRACKETS_RE.match(text.strip())
    return m.group(1) if m else text.strip()


def parse_existing_aliases(block_text):
    """Return clean alias strings (no brackets, no quotes)."""
    aliases = []
    for line in block_text.splitlines():
        m = re.match(r'''^\s+-\s+["']?(.+?)["']?\s*$''', line)
        if m:
            raw = m.group(1).strip('"').strip("'")
            aliases.append(strip_brackets(raw))
    return aliases


def derive_canonical_aliases(h1_title):
    full = h1_title.strip()
    num_match = re.match(r'Report\s+(\d+)', full)
    bare = f"Report {num_match.group(1)}" if num_match else None
    short = full.split(EM_DASH)[0].strip() if EM_DASH in full else full
    aliases = []
    if bare:
        aliases.append(bare)
    if short != full:
        aliases.append(short)
    aliases.append(full)
    return aliases


def quote_alias(alias):
    """
    Always use single quotes for aliases containing colons or special chars.
    Single-quoted YAML strings treat colons as plain text — safest for Obsidian.
    Internal single quotes are escaped by doubling them ('').
    """
    needs_quoting = ':' in alias or '"' in alias or '[' in alias
    if needs_quoting:
        escaped = alias.replace("'", "''")  # escape any internal single quotes
        return f"'{escaped}'"
    return alias  # plain string, no quotes needed


def build_aliases_block(aliases):
    lines = ["aliases:"]
    for alias in aliases:
        lines.append(f"  - {quote_alias(alias)}")
    return "\n".join(lines) + "\n"


def extract_frontmatter_bounds(content):
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
    offsets = [0]
    for line in lines:
        offsets.append(offsets[-1] + len(line) + 1)
    return (offsets[open_idx], offsets[close_idx + 1])


def process_file(filepath, dry_run):
    content = filepath.read_text(encoding='utf-8')

    h1_match = H1_RE.search(content)
    if not h1_match:
        return {'file': filepath.name, 'status': 'skipped', 'error': 'No H1 found'}

    h1_title = h1_match.group(1).strip()
    canonical = derive_canonical_aliases(h1_title)

    bounds = extract_frontmatter_bounds(content)
    if not bounds:
        return {'file': filepath.name, 'status': 'skipped', 'error': 'No frontmatter'}

    fm_start, fm_end = bounds
    frontmatter = content[fm_start:fm_end]

    aliases_match = ALIASES_BLOCK_RE.search(frontmatter)
    existing = parse_existing_aliases(aliases_match.group(1)) if aliases_match else []

    # Merge: canonical first, then any extra existing aliases
    merged = list(canonical)
    for a in existing:
        if a not in merged:
            merged.append(a)

    new_block = build_aliases_block(merged)

    if aliases_match:
        new_fm = frontmatter.replace(aliases_match.group(0), new_block, 1)
    else:
        closing = '\n---\n'
        pos = frontmatter.rfind(closing)
        if pos == -1:
            return {'file': filepath.name, 'status': 'skipped', 'error': 'No closing ---'}
        new_fm = frontmatter[:pos] + '\n' + new_block + frontmatter[pos:]

    new_content = content[:fm_start] + new_fm + content[fm_end:]

    if not dry_run:
        filepath.write_text(new_content, encoding='utf-8')

    return {
        'file': filepath.name,
        'status': 'would_change' if dry_run else 'changed',
        'h1': h1_title,
        'aliases': merged,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--vault', required=True)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--report', help='Single report number e.g. 01')
    args = parser.parse_args()

    vault = Path(args.vault).expanduser().resolve()
    if not vault.is_dir():
        print(f"ERROR: {vault} not found")
        sys.exit(1)

    files = sorted(vault.rglob(REPORT_GLOB))
    if args.report:
        files = [f for f in files if f.name.startswith(args.report.zfill(2) + '-')]

    if not files:
        print("No report files found.")
        sys.exit(1)

    mode = "DRY RUN" if args.dry_run else "LIVE"
    print(f"\nAlias Quote Fixer — {mode}")
    print(f"Vault : {vault}")
    print(f"Files : {len(files)}\n")
    print("─" * 60)

    for filepath in files:
        r = process_file(filepath, args.dry_run)
        if r['status'] in ('changed', 'would_change'):
            verb = "WOULD UPDATE" if args.dry_run else "UPDATED"
            print(f"\n{verb}: {r['file']}")
            print(f"  H1 : {r['h1']}")
            print(f"  Aliases written (single-quoted where needed):")
            for a in r['aliases']:
                print(f"    {quote_alias(a)}")
        elif r['status'] == 'skipped':
            print(f"  SKIP: {r['file']} — {r['error']}")
        else:
            print(f"  OK : {r['file']}")

    print("\n" + "─" * 60)
    if args.dry_run:
        print("Remove --dry-run to apply.")


if __name__ == '__main__':
    main()
