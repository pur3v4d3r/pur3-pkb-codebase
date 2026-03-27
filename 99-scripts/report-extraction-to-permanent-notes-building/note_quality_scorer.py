#!/usr/bin/env python3
"""
note_quality_scorer.py — Per-Note Quality Scoring for Permanent Notes
═══════════════════════════════════════════════════════════════════════════════
Assigns a quality score (0-100) to each permanent note based on completeness,
connectivity, metadata compliance, and content richness. Surfaces the weakest
notes for review and identifies patterns in quality distribution.

SCORING DIMENSIONS (weighted):
  Metadata completeness:   20 pts  (frontmatter fields present)
  Content richness:        25 pts  (callouts, word count, sections)
  Connectivity:            25 pts  (incoming + outgoing wiki-links)
  Source attribution:      15 pts  (source-reports, see-also)
  Maintenance signals:     15 pts  (status progression, timestamps, tags)

USAGE:
  python note_quality_scorer.py                       # Score all, show summary
  python note_quality_scorer.py --bottom 30           # Show 30 worst notes
  python note_quality_scorer.py --export scores.csv   # Export all scores to CSV
  python note_quality_scorer.py --threshold 40        # Flag notes below 40

REQUIRES: Python 3.10+ (stdlib only)
"""

import re
import csv
import sys
import argparse
from pathlib import Path
from datetime import date
from dataclasses import dataclass, field
from collections import defaultdict

sys.path.insert(0, str(Path(__file__).parent))

from config import PERMANENT_NOTES_DIR, VALID_DOMAINS
from audit_notes import build_resolution_index


# ══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ══════════════════════════════════════════════════════════════════════════════

_WIKILINK_RE = re.compile(r'\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]')
_CALLOUT_RE = re.compile(r'^> \[!(\S+)\]', re.MULTILINE)
_SECTION_RE = re.compile(r'^## (.+)$', re.MULTILINE)

# Required frontmatter fields for a complete permanent note
REQUIRED_FM_FIELDS = [
    "title", "type", "status", "domain", "tags", "created", "updated",
]

# Optional but desirable fields
OPTIONAL_FM_FIELDS = [
    "aliases", "source-reports", "see-also", "confidence",
    "complexity-level", "review-frequency", "mastery-stage",
]

# Expected body sections
EXPECTED_SECTIONS = [
    "Core Explanation",
    "Practical Implications",
    "Connections & Context",
    "Reflection Prompts",
    "Spaced Repetition Seeds",
]

# Status progression (higher = more mature)
STATUS_SCORES = {
    "seedling": 1,
    "budding": 2,
    "developing": 3,
    "evergreen": 4,
    "archived": 2,
}


# ══════════════════════════════════════════════════════════════════════════════
# DATA STRUCTURES
# ══════════════════════════════════════════════════════════════════════════════

@dataclass
class NoteScore:
    """Quality score for a single permanent note."""
    filepath: Path
    stem: str
    title: str = ""
    total_score: int = 0
    metadata_score: int = 0         # /20
    content_score: int = 0          # /25
    connectivity_score: int = 0     # /25
    attribution_score: int = 0      # /15
    maintenance_score: int = 0      # /15
    # Detail metrics
    fm_fields_present: int = 0
    fm_fields_total: int = len(REQUIRED_FM_FIELDS)
    word_count: int = 0
    callout_count: int = 0
    section_count: int = 0
    incoming_links: int = 0
    outgoing_links: int = 0
    source_reports: int = 0
    see_also_count: int = 0
    status: str = ""
    has_aliases: bool = False
    has_valid_domain: bool = False
    issues: list[str] = field(default_factory=list)


# ══════════════════════════════════════════════════════════════════════════════
# FRONTMATTER PARSER
# ══════════════════════════════════════════════════════════════════════════════

def _parse_fm(content: str) -> dict[str, str | list[str]]:
    """Quick frontmatter parser — returns field name -> raw value."""
    fm: dict[str, str | list[str]] = {}
    in_fm = False
    current_key = ""
    current_list: list[str] = []

    for line in content.split("\n"):
        stripped = line.strip()
        if stripped == "---":
            if not in_fm:
                in_fm = True
                continue
            else:
                if current_key and current_list:
                    fm[current_key] = current_list
                break
        if not in_fm:
            continue

        if stripped.startswith("- ") and current_key:
            val = stripped[2:].strip().strip('"').strip("'")
            current_list.append(val)
            continue

        if ":" in stripped:
            # Save previous list field
            if current_key and current_list:
                fm[current_key] = current_list
                current_list = []

            key, _, val = stripped.partition(":")
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            current_key = key
            if val:
                fm[key] = val
            else:
                current_list = []

    return fm


# ══════════════════════════════════════════════════════════════════════════════
# SCORING ENGINE
# ══════════════════════════════════════════════════════════════════════════════

def score_note(filepath: Path, incoming_count: int) -> NoteScore:
    """Score a permanent note on quality (0-100)."""
    result = NoteScore(filepath=filepath, stem=filepath.stem)
    content = filepath.read_text(encoding="utf-8", errors="replace")
    fm = _parse_fm(content)

    result.title = str(fm.get("title", filepath.stem))

    # ── 1. Metadata completeness (20 pts) ─────────────────────────────
    present = 0
    for field_name in REQUIRED_FM_FIELDS:
        if field_name in fm:
            present += 1
        else:
            result.issues.append(f"Missing required field: {field_name}")
    result.fm_fields_present = present

    # Required fields: up to 14 pts (2 per field)
    pts_required = min(present * 2, 14)

    # Optional fields: up to 6 pts (1 per field)
    optional_present = sum(1 for f in OPTIONAL_FM_FIELDS if f in fm)
    pts_optional = min(optional_present, 6)

    # Valid domain check
    domain = str(fm.get("domain", ""))
    result.has_valid_domain = domain in VALID_DOMAINS
    if not result.has_valid_domain and domain:
        result.issues.append(f"Invalid domain: {domain}")

    # Aliases check
    aliases = fm.get("aliases", [])
    result.has_aliases = bool(aliases) and aliases != [""]
    if not result.has_aliases:
        result.issues.append("No aliases defined")

    result.metadata_score = pts_required + pts_optional

    # ── 2. Content richness (25 pts) ──────────────────────────────────
    # Body extraction (skip frontmatter)
    body_start = content.find("\n---", content.find("---") + 3)
    body = content[body_start + 4:] if body_start > 0 else content

    result.word_count = len(body.split())
    result.callout_count = len(_CALLOUT_RE.findall(content))
    sections = _SECTION_RE.findall(content)
    result.section_count = len(sections)

    # Word count: up to 8 pts (1 per 100 words, capped at 800+)
    pts_words = min(result.word_count // 100, 8)

    # Callout density: up to 8 pts (2 per callout, capped at 4)
    pts_callouts = min(result.callout_count * 2, 8)

    # Expected sections: up to 9 pts
    matched_sections = sum(
        1 for s in EXPECTED_SECTIONS
        if any(s.lower() in sec.lower() for sec in sections)
    )
    pts_sections = min(matched_sections * 2, 9)

    if result.word_count < 100:
        result.issues.append("Very low word count (<100)")

    result.content_score = pts_words + pts_callouts + pts_sections

    # ── 3. Connectivity (25 pts) ──────────────────────────────────────
    result.incoming_links = incoming_count
    outgoing = set()
    for m in _WIKILINK_RE.finditer(content):
        outgoing.add(m.group(1).strip().lower())
    result.outgoing_links = len(outgoing)

    # Incoming: up to 13 pts (1 per link, capped at 13)
    pts_incoming = min(incoming_count, 13)
    # Outgoing: up to 12 pts (1 per 2 links, capped at 12)
    pts_outgoing = min(len(outgoing) // 2, 12)

    if incoming_count == 0:
        result.issues.append("Orphan note (0 incoming links)")

    result.connectivity_score = pts_incoming + pts_outgoing

    # ── 4. Source attribution (15 pts) ─────────────────────────────────
    reports = fm.get("source-reports", [])
    if isinstance(reports, str):
        reports = [reports] if reports else []
    result.source_reports = len(reports)

    see_also = fm.get("see-also", [])
    if isinstance(see_also, str):
        see_also = [see_also] if see_also else []
    result.see_also_count = len(see_also)

    # Source reports: up to 10 pts (3 per report, capped)
    pts_sources = min(len(reports) * 3, 10)
    # See-also: up to 5 pts (1 per link, capped)
    pts_see_also = min(len(see_also), 5)

    result.attribution_score = pts_sources + pts_see_also

    # ── 5. Maintenance signals (15 pts) ────────────────────────────────
    result.status = str(fm.get("status", ""))
    status_val = STATUS_SCORES.get(result.status, 0)

    # Status maturity: up to 8 pts (2 per level)
    pts_status = min(status_val * 2, 8)

    # Has timestamps: 3 pts
    pts_timestamps = 0
    if "created" in fm:
        pts_timestamps += 1
    if "updated" in fm:
        pts_timestamps += 2

    # Has tags: 4 pts (up to)
    tags = fm.get("tags", [])
    if isinstance(tags, str):
        tags = [tags]
    pts_tags = min(len(tags), 4)

    result.maintenance_score = pts_status + pts_timestamps + pts_tags

    # ── Total ─────────────────────────────────────────────────────────
    result.total_score = (
        result.metadata_score
        + result.content_score
        + result.connectivity_score
        + result.attribution_score
        + result.maintenance_score
    )

    return result


# ══════════════════════════════════════════════════════════════════════════════
# BATCH SCORING
# ══════════════════════════════════════════════════════════════════════════════

def score_all_notes(notes_dir: Path) -> list[NoteScore]:
    """Score every permanent note in the directory."""
    all_notes = sorted(notes_dir.glob("*.md"))
    if not all_notes:
        return []

    # Build incoming link counts
    resolve_map = build_resolution_index(all_notes)
    incoming: dict[str, int] = defaultdict(int)

    for f in all_notes:
        content = f.read_text(encoding="utf-8", errors="replace")
        for m in _WIKILINK_RE.finditer(content):
            target = m.group(1).strip().lower()
            resolved = resolve_map.get(target, target)
            if resolved != f.stem.lower():
                incoming[resolved] += 1

    scores = []
    for f in all_notes:
        inc = incoming.get(f.stem, 0) + incoming.get(f.stem.lower(), 0)
        scores.append(score_note(f, inc))

    return scores


# ══════════════════════════════════════════════════════════════════════════════
# REPORTING
# ══════════════════════════════════════════════════════════════════════════════

def print_summary(scores: list[NoteScore], bottom_n: int = 20, threshold: int = 0) -> None:
    """Print a quality summary report."""
    if not scores:
        print("No notes to score.")
        return

    total = len(scores)
    avg = sum(s.total_score for s in scores) / total
    scores_sorted = sorted(scores, key=lambda s: s.total_score)

    # Distribution buckets
    buckets = {"0-19": 0, "20-39": 0, "40-59": 0, "60-79": 0, "80-100": 0}
    for s in scores:
        if s.total_score < 20:
            buckets["0-19"] += 1
        elif s.total_score < 40:
            buckets["20-39"] += 1
        elif s.total_score < 60:
            buckets["40-59"] += 1
        elif s.total_score < 80:
            buckets["60-79"] += 1
        else:
            buckets["80-100"] += 1

    print("=" * 72)
    print("  PERMANENT NOTES QUALITY REPORT")
    print("=" * 72)

    print(f"\n  Total notes scored: {total}")
    print(f"  Average score:      {avg:.1f}/100")
    print(f"  Median score:       {scores_sorted[total // 2].total_score}/100")
    print(f"  Lowest score:       {scores_sorted[0].total_score}/100")
    print(f"  Highest score:      {scores_sorted[-1].total_score}/100")

    print(f"\n  Score Distribution:")
    for bucket, count in buckets.items():
        pct = count / total * 100
        bar = "█" * int(pct / 2)
        print(f"    {bucket:>6}: {count:>4} ({pct:>5.1f}%) {bar}")

    # Dimension averages
    avg_meta = sum(s.metadata_score for s in scores) / total
    avg_content = sum(s.content_score for s in scores) / total
    avg_conn = sum(s.connectivity_score for s in scores) / total
    avg_attr = sum(s.attribution_score for s in scores) / total
    avg_maint = sum(s.maintenance_score for s in scores) / total

    print(f"\n  Dimension Averages:")
    print(f"    Metadata (/20):      {avg_meta:>5.1f}")
    print(f"    Content (/25):       {avg_content:>5.1f}")
    print(f"    Connectivity (/25):  {avg_conn:>5.1f}")
    print(f"    Attribution (/15):   {avg_attr:>5.1f}")
    print(f"    Maintenance (/15):   {avg_maint:>5.1f}")

    # Common issues
    issue_counts: dict[str, int] = defaultdict(int)
    for s in scores:
        for issue in s.issues:
            issue_counts[issue] += 1
    if issue_counts:
        print(f"\n  Most Common Issues:")
        for issue, count in sorted(issue_counts.items(), key=lambda x: -x[1])[:10]:
            print(f"    {count:>4}x  {issue}")

    # Bottom N
    flagged = [s for s in scores_sorted if s.total_score < threshold] if threshold else scores_sorted[:bottom_n]
    label = f"Below threshold ({threshold})" if threshold else f"Bottom {bottom_n}"

    print(f"\n{'─' * 72}")
    print(f"  {label} — {len(flagged)} notes")
    print(f"{'─' * 72}")
    print(f"  {'Score':>5}  {'Meta':>4}  {'Cont':>4}  {'Conn':>4}  {'Attr':>4}  {'Mnt':>3}  Name")
    print(f"{'─' * 72}")
    for s in flagged[:50]:
        name = s.title[:40] if s.title else s.stem[:40]
        print(f"  {s.total_score:>5}  {s.metadata_score:>4}  {s.content_score:>4}  "
              f"{s.connectivity_score:>4}  {s.attribution_score:>4}  {s.maintenance_score:>3}  {name}")
    if len(flagged) > 50:
        print(f"  ... and {len(flagged) - 50} more")

    print(f"\n{'=' * 72}\n")


def export_csv(scores: list[NoteScore], output_path: Path) -> None:
    """Export all scores to a CSV file."""
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "stem", "title", "total", "metadata", "content",
            "connectivity", "attribution", "maintenance",
            "word_count", "callouts", "sections", "incoming",
            "outgoing", "source_reports", "see_also", "status", "issues",
        ])
        for s in sorted(scores, key=lambda x: x.total_score):
            writer.writerow([
                s.stem, s.title, s.total_score,
                s.metadata_score, s.content_score,
                s.connectivity_score, s.attribution_score,
                s.maintenance_score, s.word_count, s.callout_count,
                s.section_count, s.incoming_links, s.outgoing_links,
                s.source_reports, s.see_also_count, s.status,
                "; ".join(s.issues),
            ])
    print(f"Exported {len(scores)} scores to {output_path}")


# ══════════════════════════════════════════════════════════════════════════════
# CLI
# ══════════════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description="Score permanent notes on quality (0-100)"
    )
    parser.add_argument("--bottom", type=int, default=20,
                        help="Show N lowest-scoring notes (default: 20)")
    parser.add_argument("--threshold", type=int, default=0,
                        help="Flag all notes below this score")
    parser.add_argument("--export", type=str, metavar="FILE",
                        help="Export scores to CSV file")
    parser.add_argument("--notes-dir", type=str, default=None,
                        help="Override notes directory")
    args = parser.parse_args()

    notes_dir = Path(args.notes_dir) if args.notes_dir else PERMANENT_NOTES_DIR

    print(f"\nScoring notes in {notes_dir}...")
    scores = score_all_notes(notes_dir)

    if not scores:
        print("No notes found.")
        return

    print_summary(scores, bottom_n=args.bottom, threshold=args.threshold)

    if args.export:
        export_csv(scores, Path(args.export))


if __name__ == "__main__":
    main()
