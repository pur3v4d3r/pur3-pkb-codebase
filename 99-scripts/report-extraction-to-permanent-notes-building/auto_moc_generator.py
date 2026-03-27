#!/usr/bin/env python3
"""
auto_moc_generator.py — Automatic Map of Content (MOC) Generator
═══════════════════════════════════════════════════════════════════════════════
Analyses the wiki-link graph of permanent notes and clusters related
concepts into domain-based Maps of Content. Generates ready-to-use MOC
notes with curated navigational structure.

APPROACH:
  1. Build a directed graph from wiki-links in all permanent notes
  2. Cluster notes by domain (from frontmatter)
  3. Within each domain cluster, rank notes by connectivity
  4. Generate MOC notes with grouped sections

USAGE:
  python auto_moc_generator.py                          # Preview MOCs
  python auto_moc_generator.py --execute                # Write MOC files
  python auto_moc_generator.py --domain cognitive-psychology  # Single domain
  python auto_moc_generator.py --min-notes 5            # Min notes per MOC

REQUIRES: Python 3.10+ (stdlib only)
"""

import re
import sys
import argparse
from pathlib import Path
from datetime import date
from collections import defaultdict
from dataclasses import dataclass, field

sys.path.insert(0, str(Path(__file__).parent))

from config import PERMANENT_NOTES_DIR, VALID_DOMAINS


# ══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ══════════════════════════════════════════════════════════════════════════════

_WIKILINK_RE = re.compile(r'\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]')
_FM_DOMAIN_RE = re.compile(r'^domain:\s*(.+)$', re.MULTILINE)
_FM_TITLE_RE = re.compile(r'^title:\s*"?([^"]+)"?$', re.MULTILINE)
_FM_STATUS_RE = re.compile(r'^status:\s*(.+)$', re.MULTILINE)
_FM_TAGS_RE = re.compile(r'^tags:\s*\n((?:\s+-\s+.+\n)+)', re.MULTILINE)

MIN_NOTES_FOR_MOC = 3
MOC_OUTPUT_DIR = PERMANENT_NOTES_DIR  # Place MOCs alongside permanent notes


# ══════════════════════════════════════════════════════════════════════════════
# DATA STRUCTURES
# ══════════════════════════════════════════════════════════════════════════════

@dataclass
class NoteInfo:
    """Lightweight note info for graph building."""
    stem: str
    title: str
    domain: str
    status: str
    tags: list[str]
    outgoing: set[str] = field(default_factory=set)
    incoming_count: int = 0
    filepath: Path = None


@dataclass
class MOCPlan:
    """Plan for a single MOC note."""
    domain: str
    notes: list[NoteInfo]
    total_links: int = 0
    hub_notes: list[str] = field(default_factory=list)


# ══════════════════════════════════════════════════════════════════════════════
# GRAPH BUILDING
# ══════════════════════════════════════════════════════════════════════════════

def build_note_graph(notes_dir: Path) -> dict[str, NoteInfo]:
    """Build a graph of all permanent notes with link relationships."""
    notes: dict[str, NoteInfo] = {}

    # Pass 1: Read all notes
    for filepath in sorted(notes_dir.glob("*.md")):
        content = filepath.read_text(encoding="utf-8", errors="replace")
        stem = filepath.stem.lower()

        title_match = _FM_TITLE_RE.search(content)
        domain_match = _FM_DOMAIN_RE.search(content)
        status_match = _FM_STATUS_RE.search(content)
        tags_match = _FM_TAGS_RE.search(content)

        title = title_match.group(1).strip() if title_match else filepath.stem
        domain = domain_match.group(1).strip() if domain_match else "other"
        status = status_match.group(1).strip() if status_match else "unknown"

        tags = []
        if tags_match:
            for line in tags_match.group(1).strip().split("\n"):
                tag = line.strip().lstrip("- ").strip().strip('"').strip("'")
                if tag:
                    tags.append(tag)

        outgoing = set()
        for match in _WIKILINK_RE.finditer(content):
            target = match.group(1).strip().lower()
            if target and target != stem:
                outgoing.add(target)

        notes[stem] = NoteInfo(
            stem=stem,
            title=title,
            domain=domain,
            status=status,
            tags=tags,
            outgoing=outgoing,
            filepath=filepath,
        )

    # Pass 2: Count incoming links
    for note in notes.values():
        for target in note.outgoing:
            if target in notes:
                notes[target].incoming_count += 1

    return notes


# ══════════════════════════════════════════════════════════════════════════════
# CLUSTERING
# ══════════════════════════════════════════════════════════════════════════════

def cluster_by_domain(notes: dict[str, NoteInfo]) -> dict[str, list[NoteInfo]]:
    """Group notes by domain."""
    clusters: dict[str, list[NoteInfo]] = defaultdict(list)
    for note in notes.values():
        # Skip stub notes and MOC notes
        if any(t.endswith("-stub") for t in note.tags):
            continue
        if "moc" in note.tags or note.stem.startswith("moc-"):
            continue
        clusters[note.domain].append(note)
    return clusters


def build_moc_plans(notes: dict[str, NoteInfo],
                    min_notes: int = MIN_NOTES_FOR_MOC,
                    domain_filter: str | None = None) -> list[MOCPlan]:
    """Build MOC generation plans for each domain cluster."""
    clusters = cluster_by_domain(notes)
    plans = []

    for domain, domain_notes in sorted(clusters.items()):
        if domain_filter and domain != domain_filter:
            continue
        if len(domain_notes) < min_notes:
            continue

        # Sort by connectivity (incoming + outgoing)
        domain_notes.sort(
            key=lambda n: n.incoming_count + len(n.outgoing),
            reverse=True,
        )

        # Identify hub notes (top 20% by connectivity)
        hub_count = max(1, len(domain_notes) // 5)
        hub_notes = [n.stem for n in domain_notes[:hub_count]]

        total_links = sum(
            len(n.outgoing) + n.incoming_count for n in domain_notes
        )

        plans.append(MOCPlan(
            domain=domain,
            notes=domain_notes,
            total_links=total_links,
            hub_notes=hub_notes,
        ))

    plans.sort(key=lambda p: len(p.notes), reverse=True)
    return plans


# ══════════════════════════════════════════════════════════════════════════════
# MOC GENERATION
# ══════════════════════════════════════════════════════════════════════════════

def generate_moc_content(plan: MOCPlan) -> str:
    """Generate the markdown content for a MOC note."""
    today = date.today().isoformat()
    domain_title = plan.domain.replace("-", " ").title()

    lines = [
        "---",
        f'title: "Map of Content — {domain_title}"',
        "type: moc",
        "status: evergreen",
        f"domain: {plan.domain}",
        "tags:",
        "  - moc",
        f"  - {plan.domain}",
        "  - auto-generated",
        f"created: {today}",
        f"updated: {today}",
        "---",
        "",
        f"# Map of Content — {domain_title}",
        "",
        f"> [!abstract] Overview",
        f"> This MOC provides navigational structure for **{len(plan.notes)}** "
        f"permanent notes in the **{domain_title}** domain. "
        f"Auto-generated based on wiki-link graph analysis.",
        "",
    ]

    # Hub notes section
    if plan.hub_notes:
        lines.append("## 🌟 Hub Notes (Most Connected)")
        lines.append("")
        for stem in plan.hub_notes:
            note = next((n for n in plan.notes if n.stem == stem), None)
            if note:
                conn = note.incoming_count + len(note.outgoing)
                lines.append(f"- [[{note.title}]] — *{conn} connections*")
        lines.append("")

    # Group remaining by status
    by_status: dict[str, list[NoteInfo]] = defaultdict(list)
    hub_set = set(plan.hub_notes)
    for note in plan.notes:
        if note.stem not in hub_set:
            by_status[note.status].append(note)

    status_order = ["evergreen", "budding", "developing", "seedling", "draft", "unknown"]
    status_emoji = {
        "evergreen": "🌲",
        "budding": "🌱",
        "developing": "📝",
        "seedling": "🌰",
        "draft": "📋",
        "unknown": "❓",
    }

    for status in status_order:
        group = by_status.get(status, [])
        if not group:
            continue
        emoji = status_emoji.get(status, "📄")
        lines.append(f"## {emoji} {status.title()} ({len(group)})")
        lines.append("")
        for note in sorted(group, key=lambda n: n.title.lower()):
            lines.append(f"- [[{note.title}]]")
        lines.append("")

    # Stats footer
    lines.extend([
        "---",
        "",
        f"> [!info] Statistics",
        f"> - **Total notes**: {len(plan.notes)}",
        f"> - **Hub notes**: {len(plan.hub_notes)}",
        f"> - **Total connections**: {plan.total_links}",
        f"> - **Generated**: {today}",
        "",
    ])

    return "\n".join(lines)


# ══════════════════════════════════════════════════════════════════════════════
# REPORTING & EXECUTION
# ══════════════════════════════════════════════════════════════════════════════

def print_preview(plans: list[MOCPlan]) -> None:
    """Print a preview of MOCs that would be generated."""
    print("=" * 72)
    print("  AUTO-MOC GENERATION PLAN")
    print("=" * 72)
    print(f"\n  MOCs to generate: {len(plans)}")

    for plan in plans:
        domain_title = plan.domain.replace("-", " ").title()
        print(f"\n  📁 {domain_title}")
        print(f"     Notes: {len(plan.notes)}  |  Connections: {plan.total_links}")
        print(f"     Hub notes: {', '.join(plan.hub_notes[:5])}")

    print(f"\n{'=' * 72}\n")


def execute_moc_generation(plans: list[MOCPlan], output_dir: Path,
                           execute: bool = False) -> int:
    """Generate MOC files."""
    written = 0
    for plan in plans:
        content = generate_moc_content(plan)
        filename = f"moc-{plan.domain}.md"
        filepath = output_dir / filename

        if execute:
            filepath.write_text(content, encoding="utf-8")
            print(f"  ✅ Created {filename} ({len(plan.notes)} notes)")
            written += 1
        else:
            print(f"  🔲 Would create {filename} ({len(plan.notes)} notes)")

    return written


# ══════════════════════════════════════════════════════════════════════════════
# CLI
# ══════════════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description="Auto-generate Maps of Content from wiki-link graph"
    )
    parser.add_argument("--execute", action="store_true", default=False,
                        help="Write MOC files (default: dry run)")
    parser.add_argument("--domain", type=str, default=None,
                        help="Generate MOC for a single domain only")
    parser.add_argument("--min-notes", type=int, default=MIN_NOTES_FOR_MOC,
                        help=f"Minimum notes per domain for MOC (default: {MIN_NOTES_FOR_MOC})")
    parser.add_argument("--notes-dir", type=str, default=None,
                        help="Override notes directory")
    parser.add_argument("--output-dir", type=str, default=None,
                        help="Override MOC output directory")
    args = parser.parse_args()

    notes_dir = Path(args.notes_dir) if args.notes_dir else PERMANENT_NOTES_DIR
    output_dir = Path(args.output_dir) if args.output_dir else MOC_OUTPUT_DIR

    print(f"\nBuilding wiki-link graph from {notes_dir}...")
    notes = build_note_graph(notes_dir)
    print(f"  {len(notes)} notes indexed.")

    plans = build_moc_plans(notes, min_notes=args.min_notes, domain_filter=args.domain)

    if not plans:
        print("No domains meet the minimum note threshold for MOC generation.")
        return

    print_preview(plans)
    written = execute_moc_generation(plans, output_dir, execute=args.execute)

    if args.execute:
        print(f"\n  Created {written} MOC files.")
    else:
        print(f"\n  Dry run — {len(plans)} MOCs would be created. Use --execute to apply.")


if __name__ == "__main__":
    main()
