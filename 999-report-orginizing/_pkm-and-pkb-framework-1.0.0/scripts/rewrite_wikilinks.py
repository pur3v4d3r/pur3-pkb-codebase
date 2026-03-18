#!/usr/bin/env python3
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
"""
rewrite_wikilinks.py
─────────────────────────────────────────────────────────────────────────────
Rewrite wiki-links from [[Display Name]] to [[Filename-Stem|Display Name]]
so Obsidian resolves them by exact filename instead of alias matching.

ROOT CAUSE:
  Wiki-links use spaces (e.g. [[Expertise Reversal Effect]]) but filenames
  use hyphens (e.g. Expertise-Reversal-Effect.md). Obsidian does NOT
  auto-resolve spaces → hyphens. Pipe syntax bypasses alias resolution
  entirely by pointing directly at the filename.

USAGE:
  python scripts/rewrite_wikilinks.py                  # Dry run (default)
  python scripts/rewrite_wikilinks.py --execute         # Apply changes
  python scripts/rewrite_wikilinks.py --scope notes     # Only permanent notes
  python scripts/rewrite_wikilinks.py --scope reports   # Only report markdown
  python scripts/rewrite_wikilinks.py --scope all       # Both (default)

SAFETY:
  - Dry-run by default — shows what WOULD change
  - Skips links that already have pipe syntax
  - Skips links that already match a filename exactly (e.g. [[Pedagogy]] → Pedagogy.md)
  - Prefers original notes over stubs for duplicate aliases
  - Reports every rewrite for auditability
"""

import re
import sys
import argparse
from pathlib import Path
from collections import defaultdict

# ── CONFIGURATION ─────────────────────────────────────────────────────────
PROJECT_ROOT = Path(__file__).resolve().parent.parent
NOTES_DIR = PROJECT_ROOT / "_permanent-notes"
REPORTS_DIR = PROJECT_ROOT / "extraction-material" / "markdown"

# Wiki-link regex: captures [[target]] and [[target|display]] and [[target#heading]]
# Group 1 = full match interior, but we use finditer on the raw text
WIKILINK_RE = re.compile(r'\[\[([^\[\]]+?)\]\]')
# ─────────────────────────────────────────────────────────────────────────


def build_resolution_index(notes_dir: Path) -> dict[str, str]:
    """
    Build a mapping: lowercase display name → filename stem.

    Resolution priority:
      1. Exact filename stem (spaces normalised)
      2. Alias from frontmatter
      3. For duplicates: prefer longer filenames (originals) over short (stubs)
    """
    # First pass: collect all stems and their aliases
    stem_data: list[tuple[str, list[str], bool]] = []  # (stem, aliases, is_stub)

    for f in sorted(notes_dir.glob("*.md")):
        stem = f.stem
        text = f.read_text(encoding="utf-8", errors="ignore")

        # Detect if this is a stub (has "stub-note" in tags or very short)
        is_stub = "stub-note" in text[:500] or len(text) < 600

        # Parse aliases from YAML frontmatter
        aliases = []
        m = re.search(r'^---\s*\n(.*?)\n---', text, re.DOTALL)
        if m:
            in_aliases = False
            for line in m.group(1).split('\n'):
                if line.startswith('aliases:'):
                    in_aliases = True
                    if '[]' in line:
                        in_aliases = False
                    continue
                if in_aliases:
                    if line.startswith('  - '):
                        val = line[4:].strip().strip('"').strip("'")
                        if val:
                            aliases.append(val)
                    elif not line.startswith('  ') and not line.startswith('#'):
                        in_aliases = False

        stem_data.append((stem, aliases, is_stub))

    # Second pass: build the index with priority handling
    index: dict[str, str] = {}         # lowercase name → stem
    conflicts: dict[str, list] = defaultdict(list)  # track duplicates

    for stem, aliases, is_stub in stem_data:
        # The "display name" version of the stem (hyphens → spaces, clean up em-dashes)
        display_from_stem = stem.replace("-", " ").strip()

        # Register the stem itself (hyphenated) — always resolves
        index[stem.lower()] = stem

        # Register space-version of stem
        space_key = display_from_stem.lower()
        if space_key not in index or (space_key in index and not is_stub):
            # Prefer originals (non-stubs) over stubs
            existing = index.get(space_key)
            if existing is None:
                index[space_key] = stem
            else:
                # Conflict: prefer longer stem (original) over shorter (stub)
                if len(stem) > len(existing):
                    index[space_key] = stem
                # If current is stub but existing is original, keep existing

        # Register all aliases
        for alias in aliases:
            alias_key = alias.lower()
            if alias_key not in index:
                index[alias_key] = stem
            else:
                existing = index[alias_key]
                if existing != stem:
                    conflicts[alias_key].append((stem, is_stub))
                    # Prefer non-stub
                    if not is_stub and len(stem) > len(existing):
                        index[alias_key] = stem

    return index


def rewrite_wikilinks_in_text(text: str, index: dict[str, str]) -> tuple[str, int, list[str]]:
    """
    Rewrite all wiki-links in text to pipe syntax where needed.

    Returns: (new_text, rewrite_count, log_entries)
    """
    rewrites = 0
    log = []

    def replacer(match: re.Match) -> str:
        nonlocal rewrites
        interior = match.group(1)

        # Already has pipe syntax — skip
        if '|' in interior:
            return match.group(0)

        # Split off heading anchor if present: [[Target#Heading]]
        if '#' in interior:
            target_part, heading = interior.split('#', 1)
            target_part = target_part.strip()
            has_heading = True
        else:
            target_part = interior.strip()
            has_heading = False

        if not target_part:
            return match.group(0)

        display_name = target_part
        lookup = target_part.lower()

        # Try to resolve
        resolved_stem = index.get(lookup)

        if resolved_stem is None:
            # Try hyphenated version
            hyphen_lookup = lookup.replace(' ', '-')
            resolved_stem = index.get(hyphen_lookup)

        if resolved_stem is None:
            # Unresolvable — leave as-is
            return match.group(0)

        # Check if the link already matches the filename exactly (no rewrite needed)
        if lookup == resolved_stem.lower():
            # [[Pedagogy]] → Pedagogy.md — already works, no pipe needed
            return match.group(0)

        # Also check hyphenated version
        if lookup.replace(' ', '-') == resolved_stem.lower():
            # The display uses spaces but filename uses hyphens — NEEDS pipe syntax
            pass  # Fall through to rewrite
        elif lookup.replace('-', ' ') == resolved_stem.lower().replace('-', ' '):
            # Same words, different separators — still needs pipe
            pass

        # Build the pipe-syntax link
        if has_heading:
            new_link = f"[[{resolved_stem}#{heading}|{display_name}]]"
        else:
            new_link = f"[[{resolved_stem}|{display_name}]]"

        rewrites += 1
        log.append(f"  [[{interior}]] → [[{resolved_stem}|{display_name}]]")
        return new_link

    new_text = WIKILINK_RE.sub(replacer, text)
    return new_text, rewrites, log


def process_files(files: list[Path], index: dict[str, str], execute: bool) -> tuple[int, int, int]:
    """Process a list of files. Returns (files_changed, total_rewrites, files_scanned)."""
    files_changed = 0
    total_rewrites = 0

    for filepath in sorted(files):
        text = filepath.read_text(encoding="utf-8", errors="ignore")
        new_text, count, log = rewrite_wikilinks_in_text(text, index)

        if count > 0:
            files_changed += 1
            total_rewrites += count
            print(f"\n>> {filepath.name} ({count} rewrites)")
            for entry in log[:10]:  # Show first 10 per file
                print(entry)
            if len(log) > 10:
                print(f"  ... and {len(log) - 10} more")

            if execute:
                filepath.write_text(new_text, encoding="utf-8")

    return files_changed, total_rewrites, len(files)


def main():
    parser = argparse.ArgumentParser(description="Rewrite wiki-links to pipe syntax")
    parser.add_argument("--execute", action="store_true",
                        help="Apply changes (default: dry run)")
    parser.add_argument("--scope", choices=["notes", "reports", "all"], default="all",
                        help="Which files to process (default: all)")
    args = parser.parse_args()

    print("=" * 70)
    print("WIKI-LINK PIPE SYNTAX REWRITER")
    print("=" * 70)
    print(f"Mode: {'[EXECUTE]' if args.execute else '[DRY RUN] (pass --execute to apply)'}")
    print(f"Scope: {args.scope}")
    print()

    # Build resolution index
    print("Building resolution index...")
    index = build_resolution_index(NOTES_DIR)
    print(f"  {len(index)} resolvable names indexed")
    print()

    # Gather files
    note_files = sorted(NOTES_DIR.glob("*.md")) if args.scope in ("notes", "all") else []
    report_files = sorted(REPORTS_DIR.glob("*.md")) if args.scope in ("reports", "all") else []

    # Process permanent notes
    if note_files:
        print(f"-- Processing {len(note_files)} permanent notes --")
        n_changed, n_rewrites, n_scanned = process_files(note_files, index, args.execute)
        print(f"\n  Notes: {n_changed}/{n_scanned} files changed, {n_rewrites} links rewritten")

    # Process report markdown
    if report_files:
        print(f"\n-- Processing {len(report_files)} report files --")
        r_changed, r_rewrites, r_scanned = process_files(report_files, index, args.execute)
        print(f"\n  Reports: {r_changed}/{r_scanned} files changed, {r_rewrites} links rewritten")

    # Summary
    total_changed = (n_changed if note_files else 0) + (r_changed if report_files else 0)
    total_rewrites = (n_rewrites if note_files else 0) + (r_rewrites if report_files else 0)

    print()
    print("=" * 70)
    print(f"TOTAL: {total_rewrites} wiki-links rewritten across {total_changed} files")
    if not args.execute:
        print("** This was a DRY RUN. Pass --execute to apply changes. **")
    else:
        print("** All changes applied. **")
    print("=" * 70)


if __name__ == "__main__":
    main()
