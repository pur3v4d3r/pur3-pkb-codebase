#!/usr/bin/env python3
"""
audit_notes.py — Permanent Notes vs Wiki-Links Comprehensive Audit
═══════════════════════════════════════════════════════════════════════════════
Audits generated permanent notes to identify:
  - Resolved vs unresolved wiki-link targets
  - Missing concepts (linked but no note exists)
  - Report references vs actual knowledge concepts
  - Orphan notes (no other permanent note links to them)
  - Connectivity statistics

USAGE:
  python scripts/audit_notes.py                    # Console report
  python scripts/audit_notes.py --markdown         # Markdown file output
  python scripts/audit_notes.py --markdown --top N # Show top N missing concepts

REQUIRES: Python 3.10+ (stdlib only)
"""

import re
import sys
import argparse
from pathlib import Path
from collections import defaultdict
from datetime import date


# ══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ══════════════════════════════════════════════════════════════════════════════

NOTES_DIR = Path(__file__).parent.parent / "_permanent-notes"
WIKILINK_PATTERN = re.compile(r'\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]')
REPORT_PATTERN = re.compile(r'^(\d{2}-|Report\s)')
PLACEHOLDER_NAMES = {"Note Title", "Note Title A", "Note Title B", ""}

# Patterns that indicate a garbage / non-concept wiki-link target
_GARBAGE_LINK_PATTERNS = [
    re.compile(r'<%'),                     # Templater syntax
    re.compile(r'%>'),                     # Templater syntax
    re.compile(r'tp\.'),                   # Templater function references
    re.compile(r'^\*\*.*\*\*$'),           # Bold-wrapped text
    re.compile(r'^__.*__$'),               # Underline-wrapped text
    re.compile(r'^\d{1,4}$'),             # Pure numbers / years
    re.compile(r'^Note-?\d+$', re.I),     # Template placeholders
    re.compile(r'^Note Title', re.I),     # Template placeholder text
    re.compile(r'priority:|aliases:|topic:', re.I),  # YAML fragment leak
    re.compile(r'^\s*$'),                 # Empty / whitespace-only
    re.compile(r'^[^a-zA-Z]*$'),          # No alphabetic characters
]


def _is_garbage_link(target: str) -> bool:
    """Return True if the wiki-link target is not a valid concept name."""
    if not target or len(target.strip()) < 2:
        return True
    return any(p.search(target) for p in _GARBAGE_LINK_PATTERNS)


# ══════════════════════════════════════════════════════════════════════════════
# CORE AUDIT ENGINE
# ══════════════════════════════════════════════════════════════════════════════

class AuditResult:
    """Container for all audit metrics."""
    def __init__(self):
        self.total_notes: int = 0
        self.index_entries: int = 0
        self.unique_targets: int = 0

        self.resolved: dict[str, set[str]] = {}      # target -> source stems
        self.unresolved: dict[str, set[str]] = {}

        self.report_refs: dict[str, set[str]] = {}
        self.placeholders: dict[str, set[str]] = {}
        self.missing_concepts: dict[str, set[str]] = {}

        self.orphans: list[tuple[str, int]] = []      # (stem, outgoing_count)
        self.well_connected: list[tuple[str, int, int]] = []  # (stem, in, out)

        self.note_incoming: dict[str, set[str]] = defaultdict(set)
        self.note_outgoing: dict[str, set[str]] = {}


def build_resolution_index(notes: list[Path]) -> dict[str, str]:
    """Build a lowercase lookup mapping aliases/stems -> filename stem."""
    resolve_map: dict[str, str] = {}

    for f in notes:
        stem = f.stem
        resolve_map[stem.lower()] = stem
        resolve_map[stem.lower().replace('-', ' ')] = stem

        content = f.read_text(encoding='utf-8', errors='ignore')
        in_aliases = False
        for line in content.split('\n'):
            stripped = line.strip()
            if stripped == 'aliases:':
                in_aliases = True
                continue
            if in_aliases:
                if line.startswith('  - '):
                    alias = line.strip().lstrip('- ').strip('"').strip("'")
                    if alias:
                        resolve_map[alias.lower()] = stem
                else:
                    in_aliases = False

    return resolve_map


def run_audit(notes_dir: Path = NOTES_DIR) -> AuditResult:
    """Execute the full audit and return structured results."""
    result = AuditResult()
    all_notes = sorted(notes_dir.glob('*.md'))
    result.total_notes = len(all_notes)

    if result.total_notes == 0:
        print(f"No notes found in {notes_dir}", file=sys.stderr)
        return result

    # 1. Build resolution index
    resolve_map = build_resolution_index(all_notes)
    result.index_entries = len(resolve_map)

    # 2. Scan all wiki-link targets
    target_sources: dict[str, set[str]] = defaultdict(set)

    for f in all_notes:
        content = f.read_text(encoding='utf-8', errors='ignore')
        targets_in_note: set[str] = set()

        for m in WIKILINK_PATTERN.finditer(content):
            target = m.group(1).strip()
            if not target or _is_garbage_link(target):
                continue
            targets_in_note.add(target)
            target_sources[target].add(f.stem)

            resolved_stem = resolve_map.get(target.lower())
            if resolved_stem:
                result.note_incoming[resolved_stem].add(f.stem)

        result.note_outgoing[f.stem] = targets_in_note

    result.unique_targets = len(target_sources)

    # 3. Classify targets
    for target, sources in target_sources.items():
        if target.lower() in resolve_map:
            result.resolved[target] = sources
        else:
            result.unresolved[target] = sources

    for target, sources in result.unresolved.items():
        if target in PLACEHOLDER_NAMES:
            result.placeholders[target] = sources
        elif REPORT_PATTERN.match(target):
            result.report_refs[target] = sources
        else:
            result.missing_concepts[target] = sources

    # 4. Find orphan notes
    for f in all_notes:
        incoming = result.note_incoming.get(f.stem, set())
        incoming_clean = incoming - {f.stem}  # exclude self-links
        outgoing_count = len(result.note_outgoing.get(f.stem, set()))

        if len(incoming_clean) == 0:
            result.orphans.append((f.stem, outgoing_count))
        else:
            result.well_connected.append((f.stem, len(incoming_clean), outgoing_count))

    result.orphans.sort(key=lambda x: x[0])
    result.well_connected.sort(key=lambda x: x[1], reverse=True)

    return result


# ══════════════════════════════════════════════════════════════════════════════
# CONSOLE REPORT
# ══════════════════════════════════════════════════════════════════════════════

def print_console_report(r: AuditResult, top_n: int = 50) -> None:
    """Print a structured console report."""
    pct = lambda n, total: f"{n/total*100:.1f}%" if total else "N/A"

    print('=' * 72)
    print('  PERMANENT NOTES vs WIKI-LINKS — COMPREHENSIVE AUDIT')
    print('=' * 72)
    print(f"""
OVERVIEW
  Permanent notes:            {r.total_notes}
  Resolution index entries:   {r.index_entries}
  Unique wiki-link targets:   {r.unique_targets}

RESOLUTION
  Resolved targets:           {len(r.resolved):>4}  ({pct(len(r.resolved), r.unique_targets)})
  Unresolved targets:         {len(r.unresolved):>4}  ({pct(len(r.unresolved), r.unique_targets)})

UNRESOLVED BREAKDOWN
  Report references:          {len(r.report_refs):>4}  (links to source reports — expected)
  Placeholders:               {len(r.placeholders):>4}  (template placeholders — expected)
  Missing concepts:           {len(r.missing_concepts):>4}  (no permanent note exists)

CONNECTIVITY
  Orphan notes (0 incoming):  {len(r.orphans):>4}  ({pct(len(r.orphans), r.total_notes)} of notes)
  Connected notes (1+ in):    {len(r.well_connected):>4}  ({pct(len(r.well_connected), r.total_notes)} of notes)
""")

    # Missing concepts
    sorted_missing = sorted(r.missing_concepts.items(), key=lambda x: len(x[1]), reverse=True)
    print('─' * 72)
    print(f'  TOP {min(top_n, len(sorted_missing))} MISSING CONCEPTS (of {len(sorted_missing)} total)')
    print('─' * 72)
    for target, sources in sorted_missing[:top_n]:
        print(f'  {len(sources):>3} notes →  {target}')

    # Top connected
    print()
    print('─' * 72)
    print(f'  TOP 20 MOST CONNECTED NOTES')
    print('─' * 72)
    for stem, inc, out in r.well_connected[:20]:
        print(f'  {inc:>3} in / {out:>3} out  {stem}')


# ══════════════════════════════════════════════════════════════════════════════
# MARKDOWN REPORT
# ══════════════════════════════════════════════════════════════════════════════

def generate_markdown_report(r: AuditResult, top_n: int = 50) -> str:
    """Generate a full markdown audit report."""
    pct = lambda n, total: f"{n/total*100:.1f}%" if total else "N/A"
    today = date.today().isoformat()

    lines = [
        '---',
        f'title: "Permanent Notes Audit — {today}"',
        'type: audit-report',
        f'created: {today}',
        f'notes-audited: {r.total_notes}',
        f'resolution-rate: "{pct(len(r.resolved), r.unique_targets)}"',
        f'orphan-rate: "{pct(len(r.orphans), r.total_notes)}"',
        'tags:',
        '  - audit',
        '  - permanent-notes',
        '  - wiki-links',
        '---',
        '',
        f'# Permanent Notes Audit — {today}',
        '',
        '## Overview',
        '',
        '| Metric | Value |',
        '|---|---|',
        f'| Permanent notes | **{r.total_notes}** |',
        f'| Resolution index entries | {r.index_entries} |',
        f'| Unique wiki-link targets | {r.unique_targets} |',
        f'| Resolved targets | **{len(r.resolved)}** ({pct(len(r.resolved), r.unique_targets)}) |',
        f'| Unresolved targets | {len(r.unresolved)} ({pct(len(r.unresolved), r.unique_targets)}) |',
        f'| → Report references | {len(r.report_refs)} (expected) |',
        f'| → Placeholders | {len(r.placeholders)} (expected) |',
        f'| → Missing concepts | **{len(r.missing_concepts)}** |',
        f'| Orphan notes (0 incoming) | **{len(r.orphans)}** ({pct(len(r.orphans), r.total_notes)}) |',
        f'| Connected notes (1+ in) | {len(r.well_connected)} ({pct(len(r.well_connected), r.total_notes)}) |',
        '',
        '---',
        '',
        f'## Missing Concepts — {len(r.missing_concepts)} concepts referenced but no note exists',
        '',
        'These are wiki-link targets that appear in the body or frontmatter of permanent notes',
        'but have no corresponding permanent note file (no filename or alias match).',
        '',
        '| # Notes Linking | Missing Concept |',
        '|---|---|',
    ]

    sorted_missing = sorted(r.missing_concepts.items(), key=lambda x: len(x[1]), reverse=True)
    for target, sources in sorted_missing[:top_n]:
        lines.append(f'| {len(sources)} | {target} |')

    if len(sorted_missing) > top_n:
        lines.append(f'| ... | *{len(sorted_missing) - top_n} more concepts below threshold* |')

    lines.extend([
        '',
        '---',
        '',
        '## Report References (Expected — Not Concepts)',
        '',
        f'{len(r.report_refs)} wiki-links point to source report filenames. These are expected',
        'and do not need permanent note files.',
        '',
    ])

    # Top 15 report refs
    sorted_reports = sorted(r.report_refs.items(), key=lambda x: len(x[1]), reverse=True)
    lines.append('| # Notes | Report Reference |')
    lines.append('|---|---|')
    for target, sources in sorted_reports[:15]:
        display = target[:80] + ('…' if len(target) > 80 else '')
        lines.append(f'| {len(sources)} | {display} |')
    if len(sorted_reports) > 15:
        lines.append(f'| ... | *{len(sorted_reports) - 15} more* |')

    lines.extend([
        '',
        '---',
        '',
        f'## Orphan Notes — {len(r.orphans)} notes with 0 incoming links',
        '',
        'These permanent notes are not referenced by any other permanent note in the set.',
        'They have outgoing links but nothing links back to them.',
        '',
        '| Note | Outgoing Links |',
        '|---|---|',
    ])

    for stem, out_count in r.orphans[:60]:
        lines.append(f'| [[{stem}]] | {out_count} |')
    if len(r.orphans) > 60:
        lines.append(f'| ... | *{len(r.orphans) - 60} more* |')

    lines.extend([
        '',
        '---',
        '',
        '## Most Connected Notes (Top 20)',
        '',
        '| Note | Incoming | Outgoing |',
        '|---|---|---|',
    ])

    for stem, inc, out in r.well_connected[:20]:
        lines.append(f'| [[{stem}]] | {inc} | {out} |')

    lines.extend([
        '',
        '---',
        '',
        '*Generated by `audit_notes.py` — run `python scripts/audit_notes.py --markdown` to regenerate.*',
    ])

    return '\n'.join(lines)


# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(description="Audit permanent notes vs wiki-links")
    parser.add_argument('--markdown', action='store_true',
                        help='Generate markdown report file')
    parser.add_argument('--top', type=int, default=50,
                        help='Show top N missing concepts (default: 50)')
    parser.add_argument('--notes-dir', type=str, default=None,
                        help='Override notes directory path')
    args = parser.parse_args()

    notes_dir = Path(args.notes_dir) if args.notes_dir else NOTES_DIR

    if not notes_dir.exists():
        print(f"Notes directory not found: {notes_dir}", file=sys.stderr)
        sys.exit(1)

    result = run_audit(notes_dir)

    if args.markdown:
        report = generate_markdown_report(result, top_n=args.top)
        output_path = notes_dir.parent / f"_audit-report-{date.today().isoformat()}.md"
        output_path.write_text(report, encoding='utf-8')
        print(f"Markdown report written to: {output_path}")
        print(f"  {result.total_notes} notes audited")
        print(f"  {len(result.resolved)}/{result.unique_targets} targets resolved ({len(result.resolved)/result.unique_targets*100:.1f}%)")
        print(f"  {len(result.missing_concepts)} missing concepts")
        print(f"  {len(result.orphans)} orphan notes")
    else:
        print_console_report(result, top_n=args.top)


if __name__ == '__main__':
    main()
