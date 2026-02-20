#!/usr/bin/env python3
"""
LOTR Chapter Format Script — Phase 3a

For each chapter in the three volume files, applies:
  1. **Bold** to the first mention of each major character
  2. [[Wiki-links]] to the first mention of each key location/artifact
  3. > [!summary] placeholder at chapter end (filled later by inject script)

Input:  _tmp_fellowship_raw.md, _tmp_twotowers_raw.md, _tmp_return_raw.md
Output: _tmp_book_fellowship.md, _tmp_book_twotowers.md, _tmp_book_return.md

Run: python lotr_chapter_format.py
"""

import re
import os
import sys

VAULT = r"d:\10_pur3v4d3r's-vault"

INPUTS = [
    (
        os.path.join(VAULT, "_tmp_fellowship_raw.md"),
        os.path.join(VAULT, "_tmp_book_fellowship.md"),
        "Fellowship",
    ),
    (
        os.path.join(VAULT, "_tmp_twotowers_raw.md"),
        os.path.join(VAULT, "_tmp_book_twotowers.md"),
        "Two Towers",
    ),
    (
        os.path.join(VAULT, "_tmp_return_raw.md"),
        os.path.join(VAULT, "_tmp_book_return.md"),
        "Return",
    ),
]

# ─────────────────────────────────────────────────────────────────────────────
# BOLD TARGETS — major characters (first mention per chapter)
# Order: longer/more specific names BEFORE shorter ones to prevent partial match
# ─────────────────────────────────────────────────────────────────────────────
BOLD_CHARS = [
    ("Tom Bombadil", r"\bTom Bombadil\b"),
    ("Goldberry",    r"\bGoldberry\b"),
    ("Treebeard",    r"\bTreebeard\b"),
    ("Shadowfax",    r"\bShadowfax\b"),
    ("Meriadoc",     r"\bMeriadoc\b"),
    ("Peregrin",     r"\bPeregrin\b"),
    ("Samwise",      r"\bSamwise\b"),
    ("Saruman",      r"\bSaruman\b"),
    ("Sméagol",      r"\bSméagol\b"),
    ("Gandalf",      r"\bGandalf\b"),
    ("Aragorn",      r"\bAragorn\b"),
    ("Strider",      r"\bStrider\b"),
    ("Legolas",      r"\bLegolas\b"),
    ("Gimli",        r"\bGimli\b"),
    ("Boromir",      r"\bBoromir\b"),
    ("Faramir",      r"\bFaramir\b"),
    ("Théoden",      r"\bThéoden\b"),
    ("Denethor",     r"\bDenethor\b"),
    ("Celeborn",     r"\bCeleborn\b"),
    ("Glorfindel",   r"\bGlorfindel\b"),
    ("Galadriel",    r"\bGaladriel\b"),
    ("Elrond",       r"\bElrond\b"),
    ("Bilbo",        r"\bBilbo\b"),
    ("Éowyn",        r"\bÉowyn\b"),
    ("Éomer",        r"\bÉomer\b"),
    ("Beregond",     r"\bBeregond\b"),
    ("Gollum",       r"\bGollum\b"),
    ("Sauron",       r"\bSauron\b"),
    ("Frodo",        r"\bFrodo\b"),
    ("Merry",        r"\bMerry\b"),
    ("Pippin",       r"\bPippin\b"),
    ("Sam",          r"\bSam\b"),   # \b prevents matching inside "Samwise" / "Saruman"
]

# ─────────────────────────────────────────────────────────────────────────────
# WIKI-LINK TARGETS — key locations and artifacts (first mention per chapter)
# More specific multi-word phrases first to prevent false partial matches
# ─────────────────────────────────────────────────────────────────────────────
WIKI_TARGETS = [
    # Locations — multi-word first
    ("Minas Tirith",        r"\bMinas Tirith\b"),
    ("Minas Morgul",        r"\bMinas Morgul\b"),
    ("Helm's Deep",         r"\bHelm's Deep\b"),
    ("Caras Galadhon",      r"\bCaras Galadhon\b"),
    ("Lothlórien",          r"\bLothló?rien\b"),
    ("Emyn Muil",           r"\bEmyn Muil\b"),
    ("Amon Hen",            r"\bAmon Hen\b"),
    ("Bag End",             r"\bBag End\b"),
    ("Grey Havens",         r"\bGrey Havens\b"),
    ("The Prancing Pony",   r"\b[Tt]he Prancing Pony\b|\bPrancing Pony\b"),
    ("Old Forest",          r"\bOld Forest\b"),
    ("Dead Marshes",        r"\bDead Marshes\b"),
    ("the Black Gate",      r"\b[Tt]he Black Gate\b|\bBlack Gate\b"),
    ("Pelennor Fields",     r"\bPelennor\b"),
    ("Cirith Ungol",        r"\bCirith Ungol\b"),
    ("Mount Doom",          r"\bMount Doom\b"),
    ("Khazad-dûm",          r"\bKhazad-dûm\b"),
    ("Shelob's Lair",       r"\bShelob(?:'s Lair)?\b"),
    ("Weathertop",          r"\bWeathertop\b"),
    ("Rivendell",           r"\bRivendell\b"),
    ("Isengard",            r"\bIsengard\b"),
    ("Fangorn",             r"\bFangorn\b"),
    ("Osgiliath",           r"\bOsgiliath\b"),
    ("Hobbiton",            r"\bHobbiton\b"),
    ("Edoras",              r"\bEdoras\b"),
    ("Mordor",              r"\bMordor\b"),
    ("Rohan",               r"\bRohan\b"),
    ("Gondor",              r"\bGondor\b"),
    ("Ithilien",            r"\bIthilien\b"),
    ("Orthanc",             r"\bOrthanc\b"),
    ("Meduseld",            r"\bMeduseld\b"),
    ("Bree",                r"\bBree\b"),
    ("Moria",               r"\bMoria\b"),
    ("the Shire",           r"\b[Tt]he Shire\b"),
    ("the Anduin",          r"\b[Tt]he Anduin\b|\bAnduin\b"),
    # Artifacts
    ("the One Ring",        r"\bthe One Ring\b|\bOne Ring\b"),
    ("Sting",               r"\bSting\b"),
    ("Glamdring",           r"\bGlamdring\b"),
    ("Andúril",             r"\bAndú?ril\b"),
    ("Narsil",              r"\bNarsil\b"),
    ("palantír",            r"\bpalantí?r\b"),
    ("Phial of Galadriel",  r"\bPhial of Galadriel\b|\bPhial\b"),
    ("mithril",             r"\bmithril\b"),
    ("Lembas",              r"\b[Ll]embas\b"),
]

# Matches "## Book I, Chapter 1: Title" — NOT "### Book One" or H1s
CHAPTER_HEADING_RE = re.compile(r"^## Book [IVX]+, Chapter \d+")
SECTION_HEADING_RE = re.compile(r"^#{1,6} ")


# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────

def is_inside_formatting(line: str, start: int) -> bool:
    """Return True if position `start` is inside ** bold or [[ wiki-link."""
    before = line[:start]
    # Inside **bold**
    if before.count("**") % 2 == 1:
        return True
    # Inside [[wiki-link]]
    last_open = before.rfind("[[")
    if last_open != -1 and before.rfind("]]") < last_open:
        return True
    return False


def apply_bold(line: str, pattern: str) -> tuple[str, bool]:
    """Bold the first occurrence of pattern in line (if not already formatted)."""
    m = re.search(pattern, line)
    if not m:
        return line, False
    if is_inside_formatting(line, m.start()):
        return line, False
    matched = m.group(0)
    return line[:m.start()] + f"**{matched}**" + line[m.end():], True


def apply_wiki_link(line: str, display: str, pattern: str) -> tuple[str, bool]:
    """Wiki-link the first occurrence of pattern in line (if not already formatted)."""
    m = re.search(pattern, line, re.IGNORECASE)
    if not m:
        return line, False
    if is_inside_formatting(line, m.start()):
        return line, False
    matched = m.group(0)
    return line[:m.start()] + f"[[{matched}]]" + line[m.end():], True


# ─────────────────────────────────────────────────────────────────────────────
# CHAPTER PROCESSING
# ─────────────────────────────────────────────────────────────────────────────

def process_chapter(lines: list[str], heading: str) -> list[str]:
    """
    Process all lines of one chapter:
      - Apply wiki-links and bold to first mentions
      - Append summary placeholder callout
    """
    seen_chars: set[str] = set()
    seen_locs:  set[str] = set()
    result = []

    for line in lines:
        # Pass through headings and pre-formatted blockquotes unchanged
        if SECTION_HEADING_RE.match(line) or line.startswith(">"):
            result.append(line)
            continue

        # Apply wiki-links first (to avoid bolding inside a wiki-link)
        for (display, pattern) in WIKI_TARGETS:
            if display not in seen_locs:
                line, matched = apply_wiki_link(line, display, pattern)
                if matched:
                    seen_locs.add(display)

        # Apply bold character mentions
        for (name, pattern) in BOLD_CHARS:
            if name not in seen_chars:
                line, matched = apply_bold(line, pattern)
                if matched:
                    seen_chars.add(name)

        result.append(line)

    # Append summary placeholder
    if result and result[-1].strip() != "":
        result.append("\n")
    result.append("> [!summary] Chapter Summary\n")
    result.append(f"> [SUMMARY PLACEHOLDER: {heading}]\n")
    result.append("\n")

    return result


# ─────────────────────────────────────────────────────────────────────────────
# VOLUME PROCESSING
# ─────────────────────────────────────────────────────────────────────────────

def process_volume(input_path: str, output_path: str, label: str):
    print(f"\nProcessing {label}...")
    print(f"  Input:  {os.path.basename(input_path)}")
    print(f"  Output: {os.path.basename(output_path)}")

    with open(input_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    print(f"  Lines read: {len(lines):,}")

    # ── Split into pre-chapter content + chapter sections ────────────────────
    pre_chapter_lines: list[str] = []
    chapters: list[tuple[str, list[str]]] = []  # (heading, lines)
    current_heading: str | None = None
    current_lines: list[str] = []

    for line in lines:
        if CHAPTER_HEADING_RE.match(line):
            if current_heading is None:
                # Lines before the first chapter (H1, H3 book headings, etc.)
                pre_chapter_lines = current_lines
            else:
                chapters.append((current_heading, current_lines))
            current_heading = line.rstrip()
            current_lines = [line]
        else:
            current_lines.append(line)

    # Capture last chapter
    if current_heading is not None:
        chapters.append((current_heading, current_lines))
    else:
        pre_chapter_lines = current_lines

    print(f"  Chapters found: {len(chapters)}")

    # ── Process and assemble ──────────────────────────────────────────────────
    out_lines: list[str] = list(pre_chapter_lines)
    for (heading, ch_lines) in chapters:
        out_lines.extend(process_chapter(ch_lines, heading))

    # ── Write ─────────────────────────────────────────────────────────────────
    with open(output_path, "w", encoding="utf-8") as f:
        f.writelines(out_lines)

    bold_count    = sum(l.count("**") for l in out_lines) // 2
    wiki_count    = sum(l.count("[[") for l in out_lines)
    summary_count = sum(1 for l in out_lines if "[!summary]" in l)
    print(f"  Lines written:   {len(out_lines):,}")
    print(f"  Bold spans:      {bold_count}")
    print(f"  Wiki-links:      {wiki_count}")
    print(f"  Summary slots:   {summary_count}")


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

def main():
    print("Phase 3a: Chapter-Level Formatting")
    print("=" * 45)

    missing = [inp for inp, _, _ in INPUTS if not os.path.exists(inp)]
    if missing:
        print("ERROR: Missing input files:")
        for m in missing:
            print(f"  {m}")
        sys.exit(1)

    for inp, out, label in INPUTS:
        process_volume(inp, out, label)

    print("\n\nPhase 3a complete.")
    print("Summary placeholders embedded — ready for summary agent.")
    print("Next: run summary agent → save to _tmp_summaries.json")
    print("      then run: python lotr_inject_summaries.py")


if __name__ == "__main__":
    main()
