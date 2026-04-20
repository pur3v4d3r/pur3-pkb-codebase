#!/usr/bin/env python3
"""
LOTR Assembly Script — Phase 4
Combines all formatted pieces into the final LOTR-Formatted.md document.

Pieces assembled (in order):
  1. Introduction   (_tmp_intro.md)
  2. TOC            (_tmp_toc.md)
  3. Fellowship     (_tmp_book_fellowship.md)
  4. Two Towers     (_tmp_book_twotowers.md)
  5. Return         (_tmp_book_return.md)
  6. Appendices     (from LOTR-Formatted-structural.md)
  7. Index sections (auto-generated from wiki-links)

Run: python lotr_assemble.py
"""

import re
import os
import sys

VAULT = r"d:\10_pur3v4d3r's-vault"

PIECES = {
    "intro":       os.path.join(VAULT, "_tmp_intro.md"),
    "toc":         os.path.join(VAULT, "_tmp_toc.md"),
    "fellowship":  os.path.join(VAULT, "_tmp_book_fellowship.md"),
    "twotowers":   os.path.join(VAULT, "_tmp_book_twotowers.md"),
    "return":      os.path.join(VAULT, "_tmp_book_return.md"),
    "structural":  os.path.join(VAULT, "LOTR-Formatted-structural.md"),
}

OUTPUT = os.path.join(VAULT, "LOTR-Formatted.md")


# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────

def read(path: str) -> list[str]:
    with open(path, "r", encoding="utf-8") as f:
        return f.readlines()


def check_pieces():
    """Verify all required pieces exist."""
    missing = []
    for name, path in PIECES.items():
        if not os.path.exists(path):
            missing.append(f"  MISSING: {name} -> {path}")
    if missing:
        print("ERROR: Missing input files:")
        for m in missing:
            print(m)
        sys.exit(1)
    print("All input files present.")


def extract_appendices(structural_lines: list[str]) -> list[str]:
    """Extract Appendix section from the structural file (Appendix A onwards)."""
    for i, line in enumerate(structural_lines):
        if line.strip() == "## Appendix A: Annals of the Kings and Rulers":
            return structural_lines[i:]
    print("  [WARN] Could not find Appendix A in structural file.")
    return []


def extract_frontmatter(structural_lines: list[str]) -> list[str]:
    """Extract front matter from structural file (before Fellowship H1)."""
    for i, line in enumerate(structural_lines):
        if line.strip() == "# The Fellowship of the Ring":
            return structural_lines[:i]
    return []


def extract_epigraph(structural_lines: list[str]) -> list[str]:
    """
    Extract the opening Ring-verse epigraph from front matter.
    Returns lines between the H1/byline section and the first ## heading.
    Skips blank lines at the start, stops at the first ## heading.
    """
    epigraph = []
    in_epigraph_zone = False
    for line in structural_lines:
        if line.startswith("## "):
            break
        if line.startswith("# ") or line.strip() in ("*J.R.R. Tolkien*", "---"):
            in_epigraph_zone = True
            continue
        if in_epigraph_zone:
            epigraph.append(line)
    # Trim leading/trailing blank lines
    while epigraph and epigraph[0].strip() == "":
        epigraph.pop(0)
    while epigraph and epigraph[-1].strip() == "":
        epigraph.pop()
    return epigraph


def extract_wiki_links(lines: list[str]) -> dict[str, list[str]]:
    """
    Extract all [[wiki-links]] from content lines.
    Returns dict: {link_text: [chapter_references]}
    """
    wiki_re = re.compile(r'\[\[([^\]]+)\]\]')
    # Also track which chapter we're in
    chapter_re = re.compile(r'^## Book (.*?)$')

    links: dict[str, list[str]] = {}
    current_chapter = "Unknown"

    for line in lines:
        cm = chapter_re.match(line.strip())
        if cm:
            current_chapter = line.strip()[3:]  # Remove "## "

        for match in wiki_re.finditer(line):
            link_text = match.group(1)
            if link_text not in links:
                links[link_text] = []
            if current_chapter not in links[link_text]:
                links[link_text].append(current_chapter)

    return links


def generate_location_index(all_content: list[str]) -> str:
    """Generate alphabetical location index from wiki-links."""
    links = extract_wiki_links(all_content)

    # Known locations (to distinguish from characters/artifacts)
    location_keywords = [
        "Shire", "Bag End", "Rivendell", "Mordor", "Rohan", "Gondor",
        "Minas", "Isengard", "Fangorn", "Helm", "Edoras", "Pelennor",
        "Ithilien", "Cirith", "Shelob", "Tower", "Gate", "Cross-roads",
        "Marshes", "Emyn", "Lothlórien", "Caras", "Anduin", "Amon",
        "Weathertop", "Prancing", "Old Forest", "Tom Bombadil", "Ford",
        "Moria", "Khazad", "Bree", "Hobbiton", "Bywater", "Grey Havens",
    ]

    location_links = {k: v for k, v in links.items()
                      if any(kw.lower() in k.lower() for kw in location_keywords)}

    if not location_links:
        return "*(No wiki-linked locations found)*\n"

    lines_out = []
    for name in sorted(location_links.keys(), key=str.lower):
        chapters = location_links[name]
        ch_str = "; ".join(chapters[:3])
        if len(chapters) > 3:
            ch_str += f" (+{len(chapters)-3} more)"
        lines_out.append(f"- [[{name}]] — {ch_str}\n")

    return "".join(lines_out)


def generate_character_index(all_content: list[str]) -> str:
    """Generate character index from bold first mentions."""
    bold_re = re.compile(r'\*\*([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)?)\*\*')
    chapter_re = re.compile(r'^## Book (.*?)$')

    characters: dict[str, str] = {}  # name -> first chapter
    current_chapter = "Unknown"

    major_chars = {
        "Frodo", "Gandalf", "Aragorn", "Strider", "Legolas", "Gimli",
        "Boromir", "Merry", "Meriadoc", "Pippin", "Peregrin", "Sam", "Samwise",
        "Saruman", "Sauron", "Gollum", "Smeagol", "Sméagol", "Bilbo",
        "Treebeard", "Théoden", "Eowyn", "Éowyn", "Faramir", "Denethor",
        "Elrond", "Galadriel", "Celeborn", "Glorfindel", "Tom", "Goldberry",
        "Shadowfax", "Shelob", "Eomir", "Éomer", "Beregond",
    }

    for line in all_content:
        cm = chapter_re.match(line.strip())
        if cm:
            current_chapter = line.strip()[3:]

        for match in bold_re.finditer(line):
            name = match.group(1)
            if name in major_chars and name not in characters:
                characters[name] = current_chapter

    if not characters:
        return "*(No character first-mentions found)*\n"

    lines_out = []
    for name in sorted(characters.keys()):
        ch = characters[name]
        lines_out.append(f"- **{name}** — First appearance: {ch}\n")

    return "".join(lines_out)


# ─────────────────────────────────────────────────────────────────────────────
# MAIN ASSEMBLY
# ─────────────────────────────────────────────────────────────────────────────

def assemble():
    print("Phase 4: Assembling LOTR-Formatted.md")
    print("=" * 45)

    check_pieces()

    # Read all pieces
    intro_lines       = read(PIECES["intro"])
    toc_lines         = read(PIECES["toc"])
    fellowship_lines  = read(PIECES["fellowship"])
    twotowers_lines   = read(PIECES["twotowers"])
    return_lines      = read(PIECES["return"])
    structural_lines  = read(PIECES["structural"])

    print(f"  intro:      {len(intro_lines):>6,} lines")
    print(f"  toc:        {len(toc_lines):>6,} lines")
    print(f"  fellowship: {len(fellowship_lines):>6,} lines")
    print(f"  twotowers:  {len(twotowers_lines):>6,} lines")
    print(f"  return:     {len(return_lines):>6,} lines")

    # Extract appendices from structural file
    appendix_lines = extract_appendices(structural_lines)
    print(f"  appendices: {len(appendix_lines):>6,} lines (from structural)")

    # ── Build combined narrative (for index generation) ──────────────────────
    all_narrative = fellowship_lines + twotowers_lines + return_lines

    # ── Generate indexes ──────────────────────────────────────────────────────
    print("\nGenerating indexes...")
    location_index = generate_location_index(all_narrative)
    character_index = generate_character_index(all_narrative)

    loc_count  = location_index.count("\n- ")
    char_count = character_index.count("\n- ")
    print(f"  Locations indexed: {loc_count}")
    print(f"  Characters indexed: {char_count}")

    # ── Assemble final document ───────────────────────────────────────────────
    print("\nAssembling final document...")
    out = []

    # 1. Collection H1 (already in structural intro area, but we regenerate it)
    out.append("# The Lord of the Rings\n")
    out.append("\n*J.R.R. Tolkien*\n\n")

    # 1b. Opening epigraph (Ring-verse from front matter)
    epigraph_lines = extract_epigraph(structural_lines)
    if epigraph_lines:
        out.append("\n")
        out.extend(epigraph_lines)
        out.append("\n")
        print(f"  epigraph:   {len(epigraph_lines):>6,} lines")

    # 2. Introduction
    out.append("---\n\n")
    out.extend(intro_lines)
    out.append("\n")

    # 3. Table of Contents
    out.append("---\n\n")
    out.extend(toc_lines)
    out.append("\n")

    # 4. Front matter (foreword + prologue from structural file)
    frontmatter = extract_frontmatter(structural_lines)
    # Strip the opening H1+byline lines (we already added them above)
    fm_start = 0
    for i, l in enumerate(frontmatter):
        if l.startswith("## "):
            fm_start = i
            break
    if fm_start:
        out.append("---\n\n")
        out.extend(frontmatter[fm_start:])
        out.append("\n")

    # 5. The Fellowship of the Ring
    out.append("---\n\n")
    out.extend(fellowship_lines)
    out.append("\n")

    # 6. The Two Towers
    out.append("---\n\n")
    out.extend(twotowers_lines)
    out.append("\n")

    # 7. The Return of the King
    out.append("---\n\n")
    out.extend(return_lines)
    out.append("\n")

    # 8. Appendices
    out.append("---\n\n")
    out.extend(appendix_lines)
    out.append("\n")

    # 9. Indexes
    out.append("---\n\n")
    out.append("## Index of Key Locations\n\n")
    out.append(location_index)
    out.append("\n")
    out.append("## Index of Key Characters\n\n")
    out.append(character_index)
    out.append("\n")

    # ── Write output ──────────────────────────────────────────────────────────
    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.writelines(out)

    total_lines = len(out)
    print(f"\nDone. Output: {OUTPUT}")
    print(f"Total lines: {total_lines:,}")

    # Quick QA counts
    with open(OUTPUT, "r", encoding="utf-8") as f:
        final = f.readlines()

    h2_count = sum(1 for l in final if l.startswith("## "))
    summary_count = sum(1 for l in final if "[!summary]" in l)
    wikilink_count = sum(l.count("[[") for l in final)
    bold_count = sum(l.count("**") for l in final) // 2

    print(f"\n-- Quick QA --")
    print(f"  H2 headings:      {h2_count}")
    print(f"  Chapter summaries: {summary_count}  (expected 62)")
    print(f"  Wiki-links:       {wikilink_count}")
    print(f"  Bold spans:       {bold_count}")


if __name__ == "__main__":
    assemble()
