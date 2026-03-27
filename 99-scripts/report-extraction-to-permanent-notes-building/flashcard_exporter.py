#!/usr/bin/env python3
"""
flashcard_exporter.py — Extract Flashcards from Permanent Notes → Anki CSV
═══════════════════════════════════════════════════════════════════════════════
Scans permanent notes for flashcard callouts and Q/A inline fields,
then exports them as Anki-compatible CSV files.

FLASHCARD FORMAT in notes:
  > [!flashcard] Question text here?
  > Answer text here.

  OR inline:
  Q:: What is X?
  A:: X is Y.

OUTPUT: CSV with columns: Front, Back, Tags, Source
        Compatible with Anki's CSV import.

USAGE:
  python flashcard_exporter.py                               # Preview cards
  python flashcard_exporter.py --export flashcards.csv       # Export to CSV
  python flashcard_exporter.py --folder Notes/Permanent      # Custom folder

REQUIRES: Python 3.10+ (stdlib only)
"""

import csv
import re
import sys
import argparse
from pathlib import Path
from dataclasses import dataclass

sys.path.insert(0, str(Path(__file__).parent))

from config import PERMANENT_NOTES_DIR


# ══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ══════════════════════════════════════════════════════════════════════════════

_FLASHCARD_CALLOUT_RE = re.compile(
    r'^> \[!flashcard\]\s*(.+?)\n((?:> .+\n?)+)',
    re.MULTILINE,
)
_QA_INLINE_RE = re.compile(
    r'^Q::\s*(.+?)$\s*^A::\s*(.+?)$',
    re.MULTILINE,
)
_FM_TAGS_RE = re.compile(r'^tags:\s*\n((?:\s+-\s+.+\n)+)', re.MULTILINE)


# ══════════════════════════════════════════════════════════════════════════════
# DATA STRUCTURES
# ══════════════════════════════════════════════════════════════════════════════

@dataclass
class Flashcard:
    """A single flashcard."""
    front: str
    back: str
    source_note: str
    tags: list[str]


# ══════════════════════════════════════════════════════════════════════════════
# EXTRACTION
# ══════════════════════════════════════════════════════════════════════════════

def _extract_tags(content: str) -> list[str]:
    """Extract tags from frontmatter."""
    match = _FM_TAGS_RE.search(content)
    if not match:
        return []
    tags = []
    for line in match.group(1).strip().split("\n"):
        tag = line.strip().lstrip("- ").strip().strip('"').strip("'")
        if tag:
            tags.append(tag)
    return tags


def extract_flashcards(filepath: Path) -> list[Flashcard]:
    """Extract all flashcards from a single note."""
    content = filepath.read_text(encoding="utf-8", errors="replace")
    cards = []
    tags = _extract_tags(content)
    stem = filepath.stem

    # 1. Callout-based flashcards: > [!flashcard] Question\n> Answer
    for match in _FLASHCARD_CALLOUT_RE.finditer(content):
        question = match.group(1).strip()
        answer_lines = match.group(2).strip().split("\n")
        answer = "\n".join(
            line.lstrip("> ").strip() for line in answer_lines
        ).strip()
        if question and answer:
            cards.append(Flashcard(
                front=question,
                back=answer,
                source_note=stem,
                tags=tags,
            ))

    # 2. Inline Q:: / A:: pairs
    for match in _QA_INLINE_RE.finditer(content):
        question = match.group(1).strip()
        answer = match.group(2).strip()
        if question and answer:
            cards.append(Flashcard(
                front=question,
                back=answer,
                source_note=stem,
                tags=tags,
            ))

    return cards


def extract_all(notes_dir: Path) -> list[Flashcard]:
    """Extract flashcards from all notes in a directory."""
    all_cards = []
    for filepath in sorted(notes_dir.glob("*.md")):
        all_cards.extend(extract_flashcards(filepath))
    return all_cards


# ══════════════════════════════════════════════════════════════════════════════
# EXPORT
# ══════════════════════════════════════════════════════════════════════════════

def export_csv(cards: list[Flashcard], output_path: Path) -> None:
    """Export flashcards to Anki-compatible CSV."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter="\t")
        # Anki expects tab-separated, no header by default
        for card in cards:
            tag_str = " ".join(card.tags) if card.tags else ""
            writer.writerow([card.front, card.back, tag_str, card.source_note])
    print(f"Exported {len(cards)} flashcards to {output_path}")


def print_preview(cards: list[Flashcard], limit: int = 30) -> None:
    """Print a preview of extracted flashcards."""
    print("=" * 72)
    print("  FLASHCARD EXTRACTION REPORT")
    print("=" * 72)
    print(f"\n  Total flashcards found: {len(cards)}")

    # By source
    by_source: dict[str, int] = {}
    for card in cards:
        by_source[card.source_note] = by_source.get(card.source_note, 0) + 1
    print(f"  From {len(by_source)} unique notes\n")

    if by_source:
        print(f"  Top contributors:")
        for src, count in sorted(by_source.items(), key=lambda x: -x[1])[:10]:
            print(f"    {count:>3}  {src}")

    print(f"\n{'─' * 72}")
    print(f"  PREVIEW (first {min(limit, len(cards))} cards)")
    print(f"{'─' * 72}")
    for i, card in enumerate(cards[:limit], 1):
        front = card.front[:60] + ("..." if len(card.front) > 60 else "")
        back = card.back[:60] + ("..." if len(card.back) > 60 else "")
        print(f"  {i:>3}. Q: {front}")
        print(f"       A: {back}")
        print(f"       [{card.source_note}]")
    if len(cards) > limit:
        print(f"\n  ... and {len(cards) - limit} more")
    print(f"\n{'=' * 72}\n")


# ══════════════════════════════════════════════════════════════════════════════
# CLI
# ══════════════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description="Extract flashcards from permanent notes and export to Anki CSV"
    )
    parser.add_argument("--export", type=str, metavar="FILE",
                        help="Export flashcards to CSV file (tab-separated)")
    parser.add_argument("--notes-dir", type=str, default=None,
                        help="Override notes directory")
    parser.add_argument("--limit", type=int, default=30,
                        help="Preview limit (default: 30)")
    args = parser.parse_args()

    notes_dir = Path(args.notes_dir) if args.notes_dir else PERMANENT_NOTES_DIR

    print(f"\nScanning {notes_dir} for flashcards...")
    cards = extract_all(notes_dir)

    if not cards:
        print("No flashcards found.")
        return

    print_preview(cards, limit=args.limit)

    if args.export:
        export_csv(cards, Path(args.export))


if __name__ == "__main__":
    main()
