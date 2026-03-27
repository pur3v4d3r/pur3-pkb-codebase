#!/usr/bin/env python3
"""
promote_stubs.py — Stub Note Promotion Pipeline
═══════════════════════════════════════════════════════════════════════════════
Identifies stub notes that have accumulated enough incoming content (evidence,
insights, connections) from the update pipeline to be promoted to full
permanent notes. Optionally auto-upgrades their status and fills in missing
sections.

WORKFLOW:
  1. Scan all permanent notes for stub markers (status: seedling + *-stub tag)
  2. Score each stub on promotion readiness (incoming links, content sections,
     source-reports, see-also density)
  3. Rank by score and present promotion candidates
  4. Optionally auto-promote: upgrade status, add missing section scaffolding

USAGE:
  python promote_stubs.py                          # Dry run, show candidates
  python promote_stubs.py --execute                # Promote qualifying stubs
  python promote_stubs.py --min-score 60           # Custom threshold (0-100)
  python promote_stubs.py --list                   # List all stubs with scores

REQUIRES: Python 3.10+ (stdlib only)
"""

import re
import sys
import argparse
from pathlib import Path
from datetime import date
from dataclasses import dataclass, field

sys.path.insert(0, str(Path(__file__).parent))

from config import PERMANENT_NOTES_DIR
from audit_notes import build_resolution_index


# ══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ══════════════════════════════════════════════════════════════════════════════

TODAY = date.today().isoformat()

# Tags that mark a note as a stub
STUB_TAGS = {"concept-stub", "person-stub", "domain-stub", "tool-stub", "expansion-topic-stub"}

# Minimum promotion score (0-100) to qualify for auto-promotion
DEFAULT_MIN_SCORE = 50

# Section headings expected in a full permanent note
EXPECTED_SECTIONS = [
    "Core Explanation",
    "Practical Implications",
    "Connections & Context",
    "Reflection Prompts",
    "Spaced Repetition Seeds",
]

# Wiki-link pattern
_WIKILINK_RE = re.compile(r'\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]')

# Callout pattern
_CALLOUT_RE = re.compile(r'^> \[!(\S+)\]', re.MULTILINE)


# ══════════════════════════════════════════════════════════════════════════════
# DATA STRUCTURES
# ══════════════════════════════════════════════════════════════════════════════

@dataclass
class StubScore:
    """Promotion readiness score for a single stub note."""
    filepath: Path
    stem: str
    title: str = ""
    score: int = 0              # 0-100
    incoming_links: int = 0
    outgoing_links: int = 0
    source_reports: int = 0
    see_also_count: int = 0
    callout_count: int = 0
    section_count: int = 0
    word_count: int = 0
    has_definition: bool = False
    stub_tags: list[str] = field(default_factory=list)
    breakdown: dict[str, int] = field(default_factory=dict)


# ══════════════════════════════════════════════════════════════════════════════
# SCORING ENGINE
# ══════════════════════════════════════════════════════════════════════════════

def _parse_frontmatter_field(content: str, field_name: str) -> list[str]:
    """Extract a YAML list field from frontmatter."""
    values = []
    in_field = False
    in_frontmatter = False
    for line in content.split("\n"):
        stripped = line.strip()
        if stripped == "---":
            if not in_frontmatter:
                in_frontmatter = True
                continue
            else:
                break
        if in_frontmatter:
            if stripped.startswith(f"{field_name}:"):
                in_field = True
                continue
            if in_field:
                if stripped.startswith("- "):
                    val = stripped[2:].strip().strip('"').strip("'")
                    values.append(val)
                elif stripped and not stripped.startswith("#"):
                    in_field = False
    return values


def score_stub(filepath: Path, incoming_count: int) -> StubScore:
    """
    Score a stub note on promotion readiness (0-100).

    Scoring breakdown:
    - Incoming links:    up to 25 pts (1pt per link, capped at 25)
    - Source reports:     up to 15 pts (5pt per report, capped at 15)
    - Callout count:      up to 20 pts (4pt per callout, capped at 20)
    - Section presence:   up to 15 pts (3pt per expected section found)
    - See-also density:   up to 10 pts (2pt per see-also, capped at 10)
    - Word count:         up to 10 pts (1pt per 50 words, capped at 10)
    - Has definition:     5 pts
    """
    result = StubScore(filepath=filepath, stem=filepath.stem)
    content = filepath.read_text(encoding="utf-8", errors="replace")

    # Title
    for line in content.split("\n"):
        if line.strip().startswith("title:"):
            result.title = line.split(":", 1)[1].strip().strip('"').strip("'")
            break

    # Stub tags
    tags = _parse_frontmatter_field(content, "tags")
    result.stub_tags = [t for t in tags if t in STUB_TAGS]

    # Source reports
    reports = _parse_frontmatter_field(content, "source-reports")
    result.source_reports = len(reports)

    # See-also
    see_also = _parse_frontmatter_field(content, "see-also")
    result.see_also_count = len(see_also)

    # Incoming links
    result.incoming_links = incoming_count

    # Outgoing links
    result.outgoing_links = len(_WIKILINK_RE.findall(content))

    # Callouts
    callouts = _CALLOUT_RE.findall(content)
    result.callout_count = len(callouts)
    result.has_definition = "definition" in callouts

    # Sections
    for section in EXPECTED_SECTIONS:
        if re.search(rf'^## {re.escape(section)}', content, re.MULTILINE):
            result.section_count += 1

    # Word count (body only, skip frontmatter)
    body_start = content.find("\n---", content.find("---") + 3)
    if body_start > 0:
        body = content[body_start + 4:]
    else:
        body = content
    result.word_count = len(body.split())

    # Calculate score
    pts_incoming = min(incoming_count, 25)
    pts_reports = min(result.source_reports * 5, 15)
    pts_callouts = min(result.callout_count * 4, 20)
    pts_sections = min(result.section_count * 3, 15)
    pts_see_also = min(result.see_also_count * 2, 10)
    pts_words = min(result.word_count // 50, 10)
    pts_definition = 5 if result.has_definition else 0

    result.score = (
        pts_incoming + pts_reports + pts_callouts
        + pts_sections + pts_see_also + pts_words + pts_definition
    )

    result.breakdown = {
        "incoming_links": pts_incoming,
        "source_reports": pts_reports,
        "callouts": pts_callouts,
        "sections": pts_sections,
        "see_also": pts_see_also,
        "word_count": pts_words,
        "definition": pts_definition,
    }

    return result


# ══════════════════════════════════════════════════════════════════════════════
# PROMOTION ENGINE
# ══════════════════════════════════════════════════════════════════════════════

def find_stubs(notes_dir: Path) -> list[Path]:
    """Find all stub notes in the notes directory."""
    stubs = []
    for f in notes_dir.glob("*.md"):
        content = f.read_text(encoding="utf-8", errors="replace")
        tags = _parse_frontmatter_field(content, "tags")
        if any(t in STUB_TAGS for t in tags):
            stubs.append(f)
    return sorted(stubs)


def build_incoming_counts(notes_dir: Path) -> dict[str, int]:
    """Count incoming wiki-links for each note."""
    counts: dict[str, int] = {}
    resolve_map = build_resolution_index(list(notes_dir.glob("*.md")))

    for f in notes_dir.glob("*.md"):
        content = f.read_text(encoding="utf-8", errors="replace")
        for m in _WIKILINK_RE.finditer(content):
            target = m.group(1).strip().lower()
            resolved = resolve_map.get(target, target)
            if resolved != f.stem:
                counts[resolved] = counts.get(resolved, 0) + 1

    return counts


def promote_note(filepath: Path) -> bool:
    """
    Promote a stub note to full permanent note status.

    Changes:
    - status: seedling → budding
    - Removes *-stub tags, adds promoted-from-stub
    - Adds missing section scaffolding
    - Updates timestamp
    """
    content = filepath.read_text(encoding="utf-8", errors="replace")

    # Update status
    content = re.sub(
        r'^(status:\s*)seedling\s*$',
        r'\g<1>budding',
        content,
        flags=re.MULTILINE,
    )

    # Update confidence
    content = re.sub(
        r'^(confidence:\s*)low\s*$',
        r'\g<1>moderate',
        content,
        flags=re.MULTILINE,
    )

    # Remove stub tags, add promoted tag
    for stub_tag in STUB_TAGS:
        content = re.sub(
            rf'^\s*- {re.escape(stub_tag)}\s*$',
            '',
            content,
            flags=re.MULTILINE,
        )
    # Add promoted-from-stub tag after the remaining tags
    content = re.sub(
        r'^(tags:\s*\n(?:\s*- .*\n)*)',
        r'\g<1>  - promoted-from-stub\n',
        content,
        flags=re.MULTILINE,
    )

    # Update timestamp
    content = re.sub(
        r'^(updated:\s*).*$',
        rf'\g<1>{TODAY}',
        content,
        flags=re.MULTILINE,
    )

    # Add missing sections
    for section in EXPECTED_SECTIONS:
        if not re.search(rf'^## {re.escape(section)}', content, re.MULTILINE):
            content += f"\n\n## {section}\n\n*To be expanded.*\n"

    filepath.write_text(content, encoding="utf-8")
    return True


# ══════════════════════════════════════════════════════════════════════════════
# REPORTING
# ══════════════════════════════════════════════════════════════════════════════

def print_report(scores: list[StubScore], min_score: int, dry_run: bool, promoted: int = 0) -> None:
    """Print a formatted promotion report."""
    mode = "DRY RUN" if dry_run else "EXECUTED"

    print("=" * 72)
    print(f"  STUB PROMOTION PIPELINE — {mode}")
    print("=" * 72)

    qualifying = [s for s in scores if s.score >= min_score]
    below = [s for s in scores if s.score < min_score]

    print(f"\n  Total stubs:        {len(scores)}")
    print(f"  Qualifying (≥{min_score}):  {len(qualifying)}")
    print(f"  Below threshold:    {len(below)}")
    if not dry_run:
        print(f"  Promoted:           {promoted}")

    if qualifying:
        print(f"\n{'─' * 72}")
        print(f"  {'Score':>5}  {'In':>3}  {'Src':>3}  {'Cal':>3}  {'Sec':>3}  Name")
        print(f"{'─' * 72}")
        for s in qualifying:
            name = s.title or s.stem
            print(f"  {s.score:>5}  {s.incoming_links:>3}  {s.source_reports:>3}  "
                  f"{s.callout_count:>3}  {s.section_count:>3}  {name[:50]}")

    if below:
        print(f"\n  --- Below threshold ({len(below)} stubs) ---")
        for s in below[:20]:
            name = s.title or s.stem
            print(f"  {s.score:>5}  {name[:60]}")
        if len(below) > 20:
            print(f"  ... and {len(below) - 20} more")

    print(f"\n{'=' * 72}")
    if dry_run:
        print("  Pass --execute to promote qualifying stubs.")
    print()


# ══════════════════════════════════════════════════════════════════════════════
# CLI
# ══════════════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description="Promote stub notes to full permanent notes"
    )
    parser.add_argument("--execute", action="store_true",
                        help="Apply promotions (default: dry run)")
    parser.add_argument("--min-score", type=int, default=DEFAULT_MIN_SCORE,
                        help=f"Minimum promotion score 0-100 (default: {DEFAULT_MIN_SCORE})")
    parser.add_argument("--list", action="store_true",
                        help="List all stubs with scores (no promotion)")
    parser.add_argument("--notes-dir", type=str, default=None,
                        help="Override notes directory")
    args = parser.parse_args()

    notes_dir = Path(args.notes_dir) if args.notes_dir else PERMANENT_NOTES_DIR

    print(f"\nScanning {notes_dir} for stub notes...")
    stubs = find_stubs(notes_dir)
    print(f"Found {len(stubs)} stubs.")

    if not stubs:
        print("No stub notes found.")
        return

    print("Building incoming link counts...")
    incoming = build_incoming_counts(notes_dir)

    scores = []
    for stub in stubs:
        inc = incoming.get(stub.stem, 0) + incoming.get(stub.stem.lower(), 0)
        score = score_stub(stub, inc)
        scores.append(score)

    scores.sort(key=lambda s: s.score, reverse=True)

    if args.list:
        print_report(scores, min_score=0, dry_run=True)
        return

    qualifying = [s for s in scores if s.score >= args.min_score]

    promoted = 0
    if args.execute:
        for s in qualifying:
            try:
                promote_note(s.filepath)
                promoted += 1
            except Exception as e:
                print(f"  ERROR promoting {s.stem}: {e}")

    print_report(scores, args.min_score, dry_run=not args.execute, promoted=promoted)


if __name__ == "__main__":
    main()
