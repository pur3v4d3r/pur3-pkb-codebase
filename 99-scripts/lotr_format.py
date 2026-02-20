#!/usr/bin/env python3
"""
LOTR Structural Formatter — Phase 1
Transforms raw OCR text of The Lord of the Rings into
Obsidian-compatible structured markdown.

Input:  d:/10_pur3v4d3r's-vault/The Lord of the Rings.md
Output: d:/10_pur3v4d3r's-vault/LOTR-Formatted-structural.md

Run:    python lotr_format.py
"""

import re
import os
import sys

# ─────────────────────────────────────────────────────────────────────────────
# PATHS
# ─────────────────────────────────────────────────────────────────────────────

VAULT = r"d:\10_pur3v4d3r's-vault"
INPUT_FILE  = os.path.join(VAULT, "The Lord of the Rings.md")
OUTPUT_FILE = os.path.join(VAULT, "LOTR-Formatted-structural.md")

# ─────────────────────────────────────────────────────────────────────────────
# CHAPTER / BOOK LOOKUP TABLES
# ─────────────────────────────────────────────────────────────────────────────

# (book_number, chapter_number) → canonical title (proper Unicode names)
CHAPTER_TITLES = {
    (1,  1): "A Long-Expected Party",
    (1,  2): "The Shadow of the Past",
    (1,  3): "Three Is Company",
    (1,  4): "A Short Cut to Mushrooms",
    (1,  5): "A Conspiracy Unmasked",
    (1,  6): "The Old Forest",
    (1,  7): "In the House of Tom Bombadil",
    (1,  8): "Fog on the Barrow-downs",
    (1,  9): "At the Sign of The Prancing Pony",
    (1, 10): "Strider",
    (1, 11): "A Knife in the Dark",
    (1, 12): "Flight to the Ford",
    (2,  1): "Many Meetings",
    (2,  2): "The Council of Elrond",
    (2,  3): "The Ring Goes South",
    (2,  4): "A Journey in the Dark",
    (2,  5): "The Bridge of Khazad-dûm",
    (2,  6): "Lothlórien",
    (2,  7): "The Mirror of Galadriel",
    (2,  8): "Farewell to Lórien",
    (2,  9): "The Great River",
    (2, 10): "The Breaking of the Fellowship",
    (3,  1): "The Departure of Boromir",
    (3,  2): "The Riders of Rohan",
    (3,  3): "The Uruk-hai",
    (3,  4): "Treebeard",
    (3,  5): "The White Rider",
    (3,  6): "The King of the Golden Hall",
    (3,  7): "Helm's Deep",
    (3,  8): "The Road to Isengard",
    (3,  9): "Flotsam and Jetsam",
    (3, 10): "The Voice of Saruman",
    (3, 11): "The Palantír",
    (4,  1): "The Taming of Sméagol",
    (4,  2): "The Passage of the Marshes",
    (4,  3): "The Black Gate Is Closed",
    (4,  4): "Of Herbs and Stewed Rabbit",
    (4,  5): "The Window on the West",
    (4,  6): "The Forbidden Pool",
    (4,  7): "Journey to the Cross-roads",
    (4,  8): "The Stairs of Cirith Ungol",
    (4,  9): "Shelob's Lair",
    (4, 10): "The Choices of Master Samwise",
    (5,  1): "Minas Tirith",
    (5,  2): "The Passing of the Grey Company",
    (5,  3): "The Muster of Rohan",
    (5,  4): "The Siege of Gondor",
    (5,  5): "The Ride of the Rohirrim",
    (5,  6): "The Battle of the Pelennor Fields",
    (5,  7): "The Pyre of Denethor",
    (5,  8): "The Houses of Healing",
    (5,  9): "The Last Debate",
    (5, 10): "The Black Gate Opens",
    (6,  1): "The Tower of Cirith Ungol",
    (6,  2): "The Land of Shadow",
    (6,  3): "Mount Doom",
    (6,  4): "The Field of Cormallen",
    (6,  5): "The Steward and the King",
    (6,  6): "Many Partings",
    (6,  7): "Homeward Bound",
    (6,  8): "The Scouring of the Shire",
    (6,  9): "The Grey Havens",
}

BOOK_ROMAN = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI"}

BOOK_NAME = {
    1: "Book One",  2: "Book Two",   3: "Book Three",
    4: "Book Four", 5: "Book Five",  6: "Book Six",
}

BOOK_WORD_MAP = {
    "ONE": 1, "TWO": 2, "THREE": 3, "FOUR": 4, "FIVE": 5, "SIX": 6,
}

APPENDIX_TITLES = {
    "A": "Annals of the Kings and Rulers",
    "B": "The Tale of Years",
    "C": "Family Trees (Hobbits)",
    "D": "Calendars",
    "E": "Writing and Spelling",
    "F": "The Languages and Peoples of the Third Age",
}

# ─────────────────────────────────────────────────────────────────────────────
# COMPILED PATTERNS
# ─────────────────────────────────────────────────────────────────────────────

# OCR page-header artifacts — lines that should be silently deleted
# Ordered from most-specific to least-specific
OCR_DELETE_PATTERNS = [
    # Page number + book title header (e.g. "22 THE LORD OF THE RINGS")
    re.compile(r'^\d+\s+THE LORD OF THE RINGS\s*$', re.I),
    re.compile(r'^\d+\s+THE FELLOWSHIP.*$', re.I),
    re.compile(r'^\d+\s+THE TWO TOWERS.*$', re.I),
    re.compile(r'^\d+\s+THE RETURN.*$', re.I),
    # Section + page number (e.g. "PROLOGUE 3", "APPENDIX A 1035")
    re.compile(r'^PROLOGUE\s+\d+\s*$', re.I),
    re.compile(r'^PROLOGUE\s+[IVXLC]+\s*$'),
    re.compile(r'^APPENDIX\s+[A-F]\s+\d+\s*$', re.I),
    re.compile(r'^APPENDIX\s+[A-F]\s+[IVXLC]+\d+\s*$', re.I),
    re.compile(r'^APPENDIX\s+[A-F]\s+I[OQG]\d+\s*$', re.I),  # OCR variants e.g. IO4I
    re.compile(r'^BOOK\s+(ONE|TWO|THREE|FOUR|FIVE|SIX)\s+\d+\s*$', re.I),
    # Foreword running header with page number
    re.compile(r'^FOREWORD TO THE SECOND EDITION\s+\w+\s*$', re.I),
    re.compile(r'^FOREWORD TO THE SECOND EDITION\s+[IVXLC]+\s*$', re.I),
    # "BEING THE N PART OF" subtitle in volume headers
    re.compile(r'^BEING THE (FIRST|SECOND|THIRD) PART OF\s*$', re.I),
    # "The Lord of the Rings" subtitle line in volume headers (short standalone)
    re.compile(r'^The Lord of the Rings\s*$'),
    # Running chapter headers with page numbers (e.g. "THE BREAKING OF THE FELLOWSHIP 407")
    re.compile(r'^[A-Z][A-Z\s\'\-]+\d{2,4}\s*$'),
    # Bare page numbers (3+ digit standalone lines)
    re.compile(r'^\d{3,4}\s*$'),
    # Roman numeral standalone page numbers (ii, iv, xxi etc.)
    re.compile(r'^[ivxlc]{2,5}\s*$'),
    re.compile(r'^[IVXLC]{2,5}\s*$'),
    # OCR map garbage lines near Book One header
    re.compile(r'^\d+\s+NORTH\s*$', re.I),
    re.compile(r'^ie\s+FARCTHING\s*$', re.I),
    re.compile(r'^SOUTH\s*FARTHING\s*$', re.I),
    # Contents page (we generate our own)
    re.compile(r'^CONTENTS\s*$'),
    # J.R.R. TOLKIEN standalone (appears as byline duplicate) — case variants
    re.compile(r'^J\.R\.R\.\s+TOLKIEN\s*$', re.I),
    re.compile(r'^J\.R\.R\.\s+Tolkien\s*$'),
    # "& HarperCollins e-books" publisher line
    re.compile(r'^&\s+HarperCollins\s+e-books\s*$', re.I),
    # "BY" byline standalone
    re.compile(r'^BY\s*$'),
    # NOTE ON THE TEXT page headers
    re.compile(r'^NOTE ON THE TEXT\s+\w+\s*$', re.I),
    re.compile(r'^NOTE ON THE\s+50TF\s+ANNIVERSARY\s+EDITION\s*$', re.I),
    re.compile(r'^NOTE ON THE\s+\d+(ST|ND|RD|TH)\s+ANNIVERSARY\s*$', re.I),
    # Title page lines
    re.compile(r'^iv THE LORD OF THE RINGS\s*$', re.I),
]

# Chapter header: "Chapter 1", "Chapter 12", "Chapter II" (OCR for 11)
CHAPTER_RE = re.compile(r'^Chapter\s+(II|\d{1,2})\s*$')

# Book marker: "BOOK ONE" through "BOOK SIX" (+ "BOOK SIx" typo)
BOOK_RE = re.compile(r'^BOOK\s+(ONE|TWO|THREE|FOUR|FIVE|SIX)\s*$', re.I)

# Volume title components
RE_FELLOWSHIP    = re.compile(r'^THE FELLOWSHIP\s*$')
RE_OF_THE_RING   = re.compile(r'^OF THE RING\s*$')
RE_THE_TWO       = re.compile(r'^THE TWO\s*$')          # split across 2 lines in OCR
RE_TOWERS        = re.compile(r'^TOWERS\s*$')
RE_TWO_TOWERS    = re.compile(r'^THE TWO TOWERS\s*$')   # in case it's on one line
RE_THE_RETURN    = re.compile(r'^THE RETURN\s*$')
RE_OF_THE_KING   = re.compile(r'^OF THE KING\s*$')

# Appendix: "APPENDIX A" through "APPENDIX F"
APPENDIX_RE = re.compile(r'^APPENDIX\s+([A-F])\s*$')

# Foreword
RE_FOREWORD      = re.compile(r'^FOREWORD\s*$')
RE_TO_2ND_ED     = re.compile(r'^TO THE SECOND EDITION\s*$')

# Prologue
RE_PROLOGUE      = re.compile(r'^PROLOGUE\s*$')

# Epigraph ring-verse detection
# The ring-verse has 8 lines; "In the Land of Mordor" appears at lines 5 AND 8.
# We stop at the SECOND occurrence (count = 2).
RE_EPIGRAPH_START      = re.compile(r'^Three Rings for the Elven-kings', re.I)
RE_EPIGRAPH_MORDOR_LINE = re.compile(r'^In the Land of Mordor where the Shadows lie', re.I)

# All-caps OCR chapter title line (used to consume/skip the title after emitting H2)
RE_ALL_CAPS = re.compile(r'^[A-Z][A-ZÉÛÎÔÀÈÙÂÊÎ\s\'\-–—\.]+$')

# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────

def is_ocr_artifact(s: str) -> bool:
    """True if stripped line should be deleted (OCR artifact)."""
    for pat in OCR_DELETE_PATTERNS:
        if pat.match(s):
            return True
    return False


def parse_chapter_num(raw: str) -> int:
    """Convert OCR chapter string to int. 'II' → 11."""
    return 11 if raw.strip() == "II" else int(raw.strip())


# ─────────────────────────────────────────────────────────────────────────────
# MAIN PROCESSING
# ─────────────────────────────────────────────────────────────────────────────

def process():
    print(f"Reading: {INPUT_FILE}")
    with open(INPUT_FILE, "r", encoding="utf-8") as fh:
        lines = fh.readlines()

    total_input = len(lines)
    print(f"  Total input lines: {total_input:,}")

    out = []           # output buffer (list of strings)
    i   = 0            # current line index

    # State
    current_book       = 0      # 0=none/front, 1-6 for Books I-VI
    chapter_pending    = False  # saw "Chapter N", awaiting title line
    chapter_num_buf    = None
    story_started      = False  # True after first volume H1 emitted

    # Multi-line pattern flags
    fellowship_flag = False   # saw "THE FELLOWSHIP", waiting for "OF THE RING"
    two_towers_flag = False   # saw "THE TWO", waiting for "TOWERS"
    return_flag     = False   # saw "THE RETURN", waiting for "OF THE KING"
    foreword_flag   = False   # saw "FOREWORD", waiting for "TO THE SECOND EDITION"
    prologue_done   = False   # Prologue heading already emitted

    # Epigraph
    in_epigraph       = False
    epigraph_buf      = []
    epigraph_mordor_count = 0  # counts occurrences of "Mordor" line — stop at 2

    # Chapter title (the all-caps line after Chapter N) — we consume it
    consume_chapter_title = False  # skip the all-caps OCR title line (we used lookup)

    # ── Opening title page: Add H1 for the whole collection ──────────────────
    out.append("# The Lord of the Rings\n")
    out.append("\n*J.R.R. Tolkien*\n\n")
    out.append("---\n\n")

    # Skip the first two lines of the source (bare title + blank)
    skip_first = 2

    while i < len(lines):
        raw  = lines[i]
        s    = raw.strip()

        # Skip the first N lines (we already output the title)
        if i < skip_first:
            i += 1
            continue

        # ── OCR artifact suppression ─────────────────────────────────────────
        if s and is_ocr_artifact(s):
            i += 1
            continue

        # ── Consume the all-caps chapter title that follows "## Book..." ─────
        if consume_chapter_title:
            if s:
                # This is the all-caps OCR title — skip it (we used lookup)
                consume_chapter_title = False
            i += 1
            continue

        # ── Epigraph (ring-verse) ─────────────────────────────────────────────
        if RE_EPIGRAPH_START.match(s) and not in_epigraph:
            in_epigraph  = True
            epigraph_buf = [s]
            i += 1
            continue

        if in_epigraph:
            if s:
                epigraph_buf.append(s)
                if RE_EPIGRAPH_MORDOR_LINE.match(s):
                    epigraph_mordor_count += 1
            if epigraph_mordor_count >= 2:
                # Flush full 8-line verse as italicized blockquote
                in_epigraph = False
                epigraph_mordor_count = 0
                out.append("\n")
                for el in epigraph_buf:
                    out.append(f"> *{el}*\n")
                out.append("\n")
            i += 1
            continue

        # ── FOREWORD heading ─────────────────────────────────────────────────
        if RE_FOREWORD.match(s) and not foreword_flag and not story_started:
            foreword_flag = True
            i += 1
            continue

        if foreword_flag:
            if RE_TO_2ND_ED.match(s):
                foreword_flag = False
                out.append("\n## Foreword to the Second Edition\n\n")
                i += 1
                continue
            elif s and not is_ocr_artifact(s):
                # Unexpected content — flush foreword flag, output original
                foreword_flag = False
                # fall through to normal output

        # ── PROLOGUE heading ─────────────────────────────────────────────────
        if RE_PROLOGUE.match(s) and not prologue_done:
            prologue_done = True
            out.append("\n## Prologue: Concerning Hobbits, and Other Matters\n\n")
            i += 1
            # Skip the section marker "I" on next line
            while i < len(lines) and lines[i].strip() in ("I", "II", "III", "IV", ""):
                if lines[i].strip() in ("I",):
                    i += 1
                    break
                i += 1
            continue

        # ──── Everything below only applies once the story has started ────────
        # (prevents front-matter TOC lines from triggering book/chapter headings)

        # ── Volume title: THE FELLOWSHIP OF THE RING ─────────────────────────
        if RE_FELLOWSHIP.match(s):
            if story_started:
                pass  # shouldn't occur twice, but guard
            fellowship_flag = True
            i += 1
            continue

        if fellowship_flag:
            if RE_OF_THE_RING.match(s):
                fellowship_flag = False
                story_started   = True
                out.append("\n---\n\n")
                out.append("# The Fellowship of the Ring\n")
                out.append("\n*Being the First Part of The Lord of the Rings*\n\n")
                i += 1
                continue
            elif s and not is_ocr_artifact(s):
                fellowship_flag = False
                # fall through

        # ── Volume title: THE TWO TOWERS (may be split "THE TWO" / "TOWERS") ──
        if RE_TWO_TOWERS.match(s) and story_started:
            # Single-line variant
            out.append("\n---\n\n")
            out.append("# The Two Towers\n")
            out.append("\n*Being the Second Part of The Lord of the Rings*\n\n")
            i += 1
            continue

        if RE_THE_TWO.match(s) and story_started:
            two_towers_flag = True
            i += 1
            continue

        if two_towers_flag:
            if RE_TOWERS.match(s):
                two_towers_flag = False
                out.append("\n---\n\n")
                out.append("# The Two Towers\n")
                out.append("\n*Being the Second Part of The Lord of the Rings*\n\n")
                i += 1
                continue
            elif s and not is_ocr_artifact(s):
                two_towers_flag = False
                # fall through

        # ── Volume title: THE RETURN OF THE KING ─────────────────────────────
        if RE_THE_RETURN.match(s) and story_started:
            return_flag = True
            i += 1
            continue

        if return_flag:
            if RE_OF_THE_KING.match(s):
                return_flag   = False
                out.append("\n---\n\n")
                out.append("# The Return of the King\n")
                out.append("\n*Being the Third Part of The Lord of the Rings*\n\n")
                i += 1
                continue
            elif s and not is_ocr_artifact(s):
                return_flag = False
                # fall through

        # ── BOOK markers ─────────────────────────────────────────────────────
        bm = BOOK_RE.match(s)
        if bm and story_started:
            word = bm.group(1).upper()
            book_num = BOOK_WORD_MAP.get(word, 0)
            if book_num:
                current_book = book_num
                out.append(f"\n### {BOOK_NAME[book_num]}\n\n")
            i += 1
            continue

        # ── Chapter headers ───────────────────────────────────────────────────
        cm = CHAPTER_RE.match(s)
        if cm and story_started:
            chapter_num_buf  = parse_chapter_num(cm.group(1))
            chapter_pending  = True
            i += 1
            continue

        if chapter_pending and story_started:
            if s:
                # Emit the formatted chapter heading using lookup table
                chapter_pending       = False
                consume_chapter_title = True  # next non-empty line is OCR all-caps title
                book  = current_book if current_book else 1
                roman = BOOK_ROMAN.get(book, "?")
                title = CHAPTER_TITLES.get((book, chapter_num_buf), s.title())
                out.append(f"\n## Book {roman}, Chapter {chapter_num_buf}: {title}\n\n")
                # Don't advance i — let the consume_chapter_title flag handle it
                continue
            i += 1
            continue

        # ── APPENDIX headers ──────────────────────────────────────────────────
        am = APPENDIX_RE.match(s)
        if am:
            letter = am.group(1)
            title  = APPENDIX_TITLES.get(letter, "")
            label  = f"Appendix {letter}: {title}" if title else f"Appendix {letter}"
            out.append(f"\n## {label}\n\n")
            i += 1
            continue

        # ── "NOTE ON THE TEXT" heading ────────────────────────────────────────
        if s == "NOTE ON THE TEXT" and not story_started:
            out.append("\n## Note on the Text\n\n")
            i += 1
            continue

        # ── "NOTE ON THE 50TH ANNIVERSARY EDITION" (OCR variant) ─────────────
        if re.match(r'^NOTE ON THE 50', s, re.I) and not story_started:
            out.append("\n## Note on the 50th Anniversary Edition\n\n")
            i += 1
            continue

        # ── All other lines: pass through ────────────────────────────────────
        out.append(raw)
        i += 1

    # ─────────────────────────────────────────────────────────────────────────
    # WRITE OUTPUT
    # ─────────────────────────────────────────────────────────────────────────
    print(f"Writing: {OUTPUT_FILE}")
    with open(OUTPUT_FILE, "w", encoding="utf-8") as fh:
        fh.writelines(out)

    # Stats
    total_out = len(out)
    h1 = sum(1 for l in out if l.startswith("# "))
    h2 = sum(1 for l in out if l.startswith("## "))
    h3 = sum(1 for l in out if l.startswith("### "))

    print(f"\n-- Output stats --")
    print(f"  Lines written:   {total_out:>7,}")
    print(f"  Lines removed:   {total_input - total_out:>7,}  (OCR artifacts + consumed headers)")
    print(f"  H1 headings:     {h1:>7}")
    print(f"  H2 headings:     {h2:>7}  (expected 62 chapters + ~10 sections)")
    print(f"  H3 headings:     {h3:>7}  (expected 6 books)")
    print(f"------------------")

    # Warn if chapter count is off
    if h2 < 60:
        print(f"\n  [WARN] Only {h2} H2 headings found — expected 62+ chapters.")
        print("         Check script output for missed chapter patterns.")
    else:
        print(f"\n  [OK] Chapter heading count looks healthy.")

    print(f"\nDone. Output: {OUTPUT_FILE}")


if __name__ == "__main__":
    if not os.path.exists(INPUT_FILE):
        print(f"ERROR: Input file not found: {INPUT_FILE}", file=sys.stderr)
        sys.exit(1)
    process()
