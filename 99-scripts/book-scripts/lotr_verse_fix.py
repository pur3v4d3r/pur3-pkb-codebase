#!/usr/bin/env python3
"""
LOTR Verse Fix — Targeted Line-Range Formatter

Formats all verse/song/poetry blocks by known line ranges.
Covers Fellowship (Books I-II), Two Towers, and Return of the King.
Also re-checks the 9 TT/RotK blocks from the first pass (safely skipped
if already formatted).

Each entry is (start_line_1indexed, end_line_1indexed_inclusive, description).
Blank lines within a range become >\n; non-blank lines become > *text*\n
Already-formatted blocks (first line starts with >) are skipped.

Run: python lotr_verse_fix.py
"""

import os

VAULT  = r"d:\10_pur3v4d3r's-vault"
TARGET = os.path.join(VAULT, "LOTR-Formatted.md")

# Line ranges are 1-indexed, inclusive.
# NOTE: ranges that include OCR running-headers mid-poem are split into
# two entries so the header line is excluded from verse formatting.
VERSE_BLOCKS = [
    # ── FELLOWSHIP OF THE RING — Book I ────────────────────────────────────
    (2652,  2659,  "Road Goes Ever On (Bilbo's departure version)"),
    (4732,  4739,  "Road Goes Ever On (Frodo singing on the road)"),
    (4948,  4993,  "Sam's walking song (Upon the hearth the fire is red)"),
    (5066,  5087,  "Snow-white! Elbereth hymn (High Elves in the Woody End)"),
    (5677,  5685,  "Ho! Ho! Ho! to the bottle (Pippin's drinking song)"),
    (6577,  6599,  "Farewell we call to hearth and hall (Gildor's Elves)"),
    (7300,  7302,  "Hey dol! merry dol! ring a dong dillo! (Tom intro)"),
    (7311,  7330,  "Hey! Come merry dol! (Tom's full song for Goldberry)"),
    (7577,  7578,  "Old Tom Bombadil is a merry fellow (Goldberry sings)"),
    (8451,  8464,  "Cold be hand and heart and bone (Barrow-wight)"),
    (8520,  8525,  "Old Tom Bombadil is a merry fellow (barrow-opening)"),
    (8541,  8550,  "Get out, you old Wight! (Tom's exorcism song)"),
    (9390,  9428,  "Man in the Moon part 1 (There is an inn...)"),
    (9436,  9501,  "Man in the Moon part 2 (The Man in the Moon was drinking)"),
    (10900, 10921, "Gil-galad was an Elven-king (Sam's verse)"),
    # ── FELLOWSHIP — Book II ───────────────────────────────────────────────
    (13640, 13649, "A Elbereth Gilthoniel (at Rivendell departure)"),
    (15900, 15941, "I sit beside the fire and think (Bilbo's poem)"),
    # Gimli's Song of Durin — split to skip OCR page header at line 17955
    (17946, 17953, "Song of Durin part 1 (The world was young)"),
    (17958, 18028, "Song of Durin part 2 (He named the nameless hills...)"),
    (19199, 19294, "Song of Nimrodel (Legolas sings in Lothlórien)"),
    (20309, 20347, "When evening in the Shire was grey (Gandalf's lament)"),
    (20359, 20363, "Sam's fireworks verse (The finest rockets ever seen)"),
    (21041, 21070, "Galadriel's farewell song (I sang of leaves of gold)"),
    # Lament for Boromir — split around prose bridge 'Then Aragorn sang again'
    (23238, 23262, "Lament for Boromir part 1 — Legolas (South Wind)"),
    (23268, 23288, "Lament for Boromir part 2 — Aragorn (North Wind)"),
    # ── TWO TOWERS — already fixed in first pass; included for completeness ─
    (25865, 25865, "Half-grown hobbits (single verse-line)"),
    (26577, 26637, "Ent and Entwife song (When Spring unfolds)"),
    (26951, 26966, "Orofarne lament (Quickbeam's rowan song)"),
    (27004, 27006, "Ents herald-cry (We come with roll of drum)"),
    (27031, 27041, "Isengard marching song (To Isengard! Though...)"),
    (28027, 28032, "Legolas sea-longing prophecy (Legolas Greenleaf long)"),
    # ── TWO TOWERS — Book IV ──────────────────────────────────────────────
    (35798, 35828, "Sam's Oliphaunt poem (Grey as a mouse)"),
    (40253, 40256, "A Elbereth Gilthoniel (Sam cries out vs Shelob)"),
    # ── RETURN OF THE KING — already fixed; included for completeness ──────
    (44098, 44126, "Muster of Rohan song (From dark Dunharrow)"),
    (49609, 49634, "In western lands beneath the Sun (Sam in Cirith Ungol)"),
    (52032, 52050, "Praise of the Halflings (Long live the Halflings!)"),
    (52222, 52238, "Legolas sea-longing song (To the Sea, to the Sea!)"),
    (53915, 53922, "Road Goes Ever On — Bilbo's final version (Rivendell)"),
]


def format_verse_line(raw: str) -> str:
    """Format a single file line as blockquote-italic."""
    stripped = raw.rstrip()
    if not stripped:
        return ">\n"
    return f"> *{stripped}*\n"


def main():
    print("Verse Fix Pass (targeted line-range formatter)")
    print("=" * 50)

    with open(TARGET, "r", encoding="utf-8") as f:
        lines = f.readlines()

    print(f"  File lines: {len(lines):,}")
    total_formatted = 0

    for (start, end, desc) in VERSE_BLOCKS:
        print(f"\n  [{desc}] lines {start}-{end}")
        s = start - 1  # convert to 0-indexed
        e = end        # exclusive end for slicing

        if e > len(lines):
            print(f"    [SKIP] Range out of bounds")
            continue

        # Check if already formatted (first non-blank line starts with >)
        first_content = next(
            (lines[i] for i in range(s, e) if lines[i].strip()), None
        )
        if first_content and first_content.lstrip().startswith(">"):
            print(f"    [SKIP] Already formatted")
            continue

        new_block = []
        count = 0
        for i in range(s, e):
            original = lines[i]
            formatted = format_verse_line(original)
            new_block.append(formatted)
            if original.strip():
                count += 1

        lines = lines[:s] + new_block + lines[e:]
        total_formatted += count
        print(f"    OK — formatted {count} verse lines")

    print(f"\nTotal verse lines formatted: {total_formatted}")

    if total_formatted:
        with open(TARGET, "w", encoding="utf-8") as f:
            f.writelines(lines)
        print(f"File updated: {os.path.basename(TARGET)}")

        italic_bq = sum(1 for l in lines if l.startswith("> *"))
        print(f"Italic blockquote lines now in file: {italic_bq}")
    else:
        print("No changes written.")


if __name__ == "__main__":
    main()
