#!/usr/bin/env python3
"""
rewrite_report_wikilinks.py
─────────────────────────────────────────────────────────────────────────────
Rewrite wiki-links in report files across multiple vault folders to use
pipe syntax: [[Filename-Stem|Display Name]]

Builds a resolution index from the permanent notes directory, then scans
all specified report folders (recursively) for .md files and rewrites
unresolved wiki-links.

USAGE:
  python rewrite_report_wikilinks.py                  # Dry run (default)
  python rewrite_report_wikilinks.py --execute        # Apply changes
  python rewrite_report_wikilinks.py --verbose        # Show all link rewrites

SAFETY:
  - Dry-run by default — shows what WOULD change
  - Skips links that already have pipe syntax
  - Skips links that already match a filename exactly
  - Reports every rewrite for auditability

@author   PKB Scripting Architect
@version  1.0.0
"""

import sys
import io
import re
import argparse
from pathlib import Path
from collections import defaultdict

# Force UTF-8 output on Windows
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(
        sys.stdout.buffer, encoding='utf-8', errors='replace', line_buffering=True
    )
if sys.stderr.encoding and sys.stderr.encoding.lower() != 'utf-8':
    sys.stderr = io.TextIOWrapper(
        sys.stderr.buffer, encoding='utf-8', errors='replace', line_buffering=True
    )

# ══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ══════════════════════════════════════════════════════════════════════════════

VAULT_ROOT = Path(r"D:\10_pur3v4d3r's-vault")

# Where the authoritative permanent notes live (used to build the resolution index)
PERMANENT_NOTES_DIR = (
    VAULT_ROOT / "999-report-orginizing"
    / "_permanent-notes" / "_permanent-notes"
)

# Report folders to scan (recursive .md search in each)
REPORT_FOLDERS = [
    VAULT_ROOT / "999-report-orginizing" / "999-first-principles-reports",
    VAULT_ROOT / "999-report-orginizing" / "999-focused-analysis-report-generator",
    VAULT_ROOT / "999-report-orginizing" / "999-foundational-report-genrator",
    VAULT_ROOT / "999-report-orginizing" / "999-socratic-reports",
    VAULT_ROOT / "999-report-orginizing" / "in-pkm",
    VAULT_ROOT / "999-report-orginizing" / "llm-and-prompt-engineering",
    VAULT_ROOT / "999-report-orginizing" / "reports-to-file",
    VAULT_ROOT / "999-architecture-of-the-examined-life-project"
    / "pkb-build" / "examined-life-pkb"
    / "the-architecture-of-the-examined-life" / "01-reports",
    VAULT_ROOT / "999-report-orginizing" / "_extractor-output",
]

# Wiki-link regex: captures [[...]] contents
WIKILINK_RE = re.compile(r'\[\[([^\[\]]+?)\]\]')

# ══════════════════════════════════════════════════════════════════════════════
# RESOLUTION INDEX BUILDER
# ══════════════════════════════════════════════════════════════════════════════

def _stem_match_quality(stem: str, lookup_key: str) -> int:
    """
    How well does this stem match the lookup key? Higher = better.
    Returns:
      3 = perfect direct match (stem's space form == lookup key)
      2 = lookup key is a prefix/substring of the stem's space form
      1 = no direct name relationship (alias-only match)
    """
    space_stem = stem.replace("-", " ").lower()
    # Normalize em-dashes for comparison
    space_stem_norm = space_stem.replace("—", " ").replace("  ", " ").strip()
    lookup_norm = lookup_key.replace("—", " ").replace("  ", " ").strip()

    if space_stem_norm == lookup_norm:
        return 3  # Perfect direct match
    if space_stem_norm.startswith(lookup_norm + " "):
        return 2  # Lookup is a leading prefix of the stem
    return 1  # Alias-only or substring match


def build_resolution_index(notes_dir: Path) -> dict[str, str]:
    """
    Build a mapping: lowercase display name -> filename stem.

    Sources:
      1. Filename stem (with hyphens and with spaces)
      2. YAML aliases from frontmatter
    Priority: prefer direct stem matches over alias matches.
    When both are aliases, prefer shorter (more specific) stems.
    """
    if not notes_dir.is_dir():
        print(f"  [ERROR] Permanent notes directory not found: {notes_dir}")
        sys.exit(1)

    stem_data: list[tuple[str, list[str], bool]] = []

    for f in sorted(notes_dir.glob("*.md")):
        stem = f.stem
        text = f.read_text(encoding="utf-8", errors="ignore")

        # Detect stubs
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

    # Pass 1: Register all direct stem matches (highest priority)
    index: dict[str, str] = {}

    for stem, aliases, is_stub in stem_data:
        # Register the hyphenated stem itself (always resolves)
        index[stem.lower()] = stem

        # Register space-version of stem (direct match = priority 3)
        space_key = stem.replace("-", " ").strip().lower()
        existing = index.get(space_key)
        if existing is None:
            index[space_key] = stem
        else:
            # Compare match quality: prefer the stem that more closely matches the key
            new_quality = _stem_match_quality(stem, space_key)
            old_quality = _stem_match_quality(existing, space_key)
            if new_quality > old_quality:
                index[space_key] = stem
            elif new_quality == old_quality and not is_stub:
                # Same quality: prefer shorter stem (more specific note)
                if len(stem) < len(existing):
                    index[space_key] = stem

    # Pass 2: Register aliases (lower priority — never overwrite direct stem matches)
    for stem, aliases, is_stub in stem_data:
        for alias in aliases:
            alias_key = alias.lower()
            if alias_key not in index:
                index[alias_key] = stem
            else:
                existing = index[alias_key]
                if existing == stem:
                    continue
                # Only overwrite if the existing entry is an alias match (quality 1)
                # and our new entry is better
                old_quality = _stem_match_quality(existing, alias_key)
                new_quality = _stem_match_quality(stem, alias_key)
                if new_quality > old_quality:
                    index[alias_key] = stem
                elif new_quality == old_quality and not is_stub:
                    # Same quality: prefer shorter stem (more specific note)
                    if len(stem) < len(existing):
                        index[alias_key] = stem

    return index


# ══════════════════════════════════════════════════════════════════════════════
# WIKI-LINK REWRITER
# ══════════════════════════════════════════════════════════════════════════════

def rewrite_wikilinks_in_text(
    text: str,
    index: dict[str, str],
    recheck_piped: bool = False,
) -> tuple[str, int, list[str], list[str]]:
    """
    Rewrite all wiki-links in text to pipe syntax where needed.
    If recheck_piped=True, also re-check existing pipe links and fix wrong targets.

    Returns: (new_text, rewrite_count, rewrite_log, unresolved_log)
    """
    rewrites = 0
    log = []
    unresolved = []

    def replacer(match: re.Match) -> str:
        nonlocal rewrites
        interior = match.group(1)

        # Handle already-piped links
        if '|' in interior:
            if not recheck_piped:
                return match.group(0)

            # Re-check: extract target and display
            pipe_idx = interior.index('|')
            old_target = interior[:pipe_idx].strip()
            display_name = interior[pipe_idx + 1:].strip()

            if not display_name:
                return match.group(0)

            # Strip heading from target if present
            if '#' in old_target:
                old_target_base, heading = old_target.split('#', 1)
                has_heading = True
            else:
                old_target_base = old_target
                has_heading = False

            # Look up what the display name SHOULD resolve to
            lookup = display_name.lower()
            resolved_stem = index.get(lookup)
            if resolved_stem is None:
                resolved_stem = index.get(lookup.replace(' ', '-'))
            if resolved_stem is None:
                em_dash_lookup = lookup.replace('—', '-').replace(' ', '-')
                resolved_stem = index.get(em_dash_lookup)
            if resolved_stem is None:
                paren_match = re.match(r'^(.+?)\s*\(.*\)$', lookup)
                if paren_match:
                    paren_lookup = paren_match.group(1).strip()
                    resolved_stem = index.get(paren_lookup)
                    if resolved_stem is None:
                        resolved_stem = index.get(paren_lookup.replace(' ', '-'))

            if resolved_stem is None:
                return match.group(0)

            # If the current target is already correct, skip
            if old_target_base.lower() == resolved_stem.lower():
                return match.group(0)

            # Target needs fixing
            if has_heading:
                new_link = f"[[{resolved_stem}#{heading}|{display_name}]]"
            else:
                new_link = f"[[{resolved_stem}|{display_name}]]"

            rewrites += 1
            log.append(f"  [[{old_target_base}|{display_name}]] -> [[{resolved_stem}|{display_name}]]  (target fix)")
            return new_link

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
            # Try with em-dash variants (— vs -)
            em_dash_lookup = lookup.replace('—', '-').replace(' ', '-')
            resolved_stem = index.get(em_dash_lookup)

        if resolved_stem is None:
            # Try removing parenthetical suffixes: "Constructivism (Radical)" -> "Constructivism"
            paren_match = re.match(r'^(.+?)\s*\(.*\)$', lookup)
            if paren_match:
                paren_lookup = paren_match.group(1).strip()
                resolved_stem = index.get(paren_lookup)
                if resolved_stem is None:
                    resolved_stem = index.get(paren_lookup.replace(' ', '-'))

        if resolved_stem is None:
            # Unresolvable — leave as-is, track it
            unresolved.append(display_name)
            return match.group(0)

        # Check if the link already matches the filename exactly
        if lookup == resolved_stem.lower():
            return match.group(0)

        # Check hyphenated version — if identical (case-insensitive), needs pipe
        if lookup.replace(' ', '-').lower() == resolved_stem.lower():
            pass  # Fall through to rewrite
        elif lookup.replace('-', ' ').lower() == resolved_stem.lower().replace('-', ' '):
            pass  # Fall through to rewrite
        else:
            pass  # Still rewrite — the display differs from the stem

        # Build the pipe-syntax link
        if has_heading:
            new_link = f"[[{resolved_stem}#{heading}|{display_name}]]"
        else:
            new_link = f"[[{resolved_stem}|{display_name}]]"

        rewrites += 1
        log.append(f"  [[{interior}]] -> [[{resolved_stem}|{display_name}]]")
        return new_link

    new_text = WIKILINK_RE.sub(replacer, text)
    return new_text, rewrites, log, unresolved


# ══════════════════════════════════════════════════════════════════════════════
# FILE PROCESSOR
# ══════════════════════════════════════════════════════════════════════════════

def process_files(
    files: list[Path],
    index: dict[str, str],
    execute: bool,
    verbose: bool,
    recheck_piped: bool = False,
) -> tuple[int, int, int, list[str]]:
    """
    Process a list of files. Returns (files_changed, total_rewrites, files_scanned, all_unresolved).
    """
    files_changed = 0
    total_rewrites = 0
    all_unresolved: list[str] = []

    for filepath in sorted(files):
        text = filepath.read_text(encoding="utf-8", errors="ignore")
        new_text, count, log, unresolved = rewrite_wikilinks_in_text(text, index, recheck_piped)

        all_unresolved.extend(unresolved)

        if count > 0:
            files_changed += 1
            total_rewrites += count

            if verbose:
                print(f"\n  >> {filepath.relative_to(VAULT_ROOT)} ({count} rewrites)")
                for entry in log[:20]:
                    print(entry)
                if len(log) > 20:
                    print(f"    ... and {len(log) - 20} more")
            else:
                print(f"  {filepath.relative_to(VAULT_ROOT)}: {count} rewrites")

            if execute:
                filepath.write_text(new_text, encoding="utf-8")

    return files_changed, total_rewrites, len(files), all_unresolved


# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description="Rewrite wiki-links in report files to pipe syntax using permanent note index"
    )
    parser.add_argument("--execute", action="store_true",
                        help="Apply changes (default: dry run)")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Show individual link rewrites per file")
    parser.add_argument("--show-unresolved", action="store_true",
                        help="Show all unresolved wiki-links at the end")
    parser.add_argument("--recheck-piped", action="store_true",
                        help="Also re-check existing pipe links and fix wrong targets")
    args = parser.parse_args()

    print("=" * 72)
    print("WIKI-LINK PIPE SYNTAX REWRITER — MULTI-FOLDER REPORTS")
    print("=" * 72)
    print(f"Mode: {'[EXECUTE]' if args.execute else '[DRY RUN] (pass --execute to apply)'}")
    if args.recheck_piped:
        print(f"Recheck: [ON] — will also fix wrongly-targeted pipe links")
    print(f"Permanent notes: {PERMANENT_NOTES_DIR}")
    print()

    # Build resolution index from permanent notes
    print("Building resolution index from permanent notes...")
    index = build_resolution_index(PERMANENT_NOTES_DIR)
    print(f"  {len(index)} resolvable names indexed")
    print()

    # Process each report folder
    grand_files_changed = 0
    grand_total_rewrites = 0
    grand_files_scanned = 0
    grand_unresolved: list[str] = []

    for folder in REPORT_FOLDERS:
        if not folder.is_dir():
            print(f"[SKIP] Folder not found: {folder.relative_to(VAULT_ROOT)}")
            continue

        md_files = sorted(folder.rglob("*.md"))
        if not md_files:
            print(f"[SKIP] No .md files in: {folder.relative_to(VAULT_ROOT)}")
            continue

        rel_folder = folder.relative_to(VAULT_ROOT)
        print(f"\n{'─' * 72}")
        print(f"FOLDER: {rel_folder} ({len(md_files)} files)")
        print(f"{'─' * 72}")

        changed, rewrites, scanned, unresolved = process_files(
            md_files, index, args.execute, args.verbose, args.recheck_piped
        )

        grand_files_changed += changed
        grand_total_rewrites += rewrites
        grand_files_scanned += scanned
        grand_unresolved.extend(unresolved)

        print(f"\n  Folder summary: {changed}/{scanned} files changed, {rewrites} links rewritten")

    # Grand summary
    print()
    print("=" * 72)
    print("GRAND SUMMARY")
    print("=" * 72)
    print(f"  Files scanned:    {grand_files_scanned}")
    print(f"  Files changed:    {grand_files_changed}")
    print(f"  Links rewritten:  {grand_total_rewrites}")
    print(f"  Unresolved links: {len(grand_unresolved)}")

    if args.show_unresolved and grand_unresolved:
        unique_unresolved = sorted(set(grand_unresolved))
        print(f"\n  Unique unresolved wiki-links ({len(unique_unresolved)}):")
        for name in unique_unresolved:
            print(f"    - [[{name}]]")

    if not args.execute:
        print("\n** This was a DRY RUN. Pass --execute to apply changes. **")
    else:
        print("\n** All changes applied. **")
    print("=" * 72)


if __name__ == "__main__":
    main()
