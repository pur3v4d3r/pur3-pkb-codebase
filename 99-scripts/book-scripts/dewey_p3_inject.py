#!/usr/bin/env python3
"""
dewey_p3_inject.py -- Phase 4: Inject Agent Analysis into Scaffolded Document
Reads 19 JSON analysis files (one per chapter) and injects the analytical
content into the placeholder markers in _dewey_scaffolded.md.

Input:  999-ebook-project/_dewey_scaffolded.md
        999-ebook-project/_dewey_ch01.json ... _dewey_ch19.json
Output: 999-ebook-project/_dewey_injected.md

Run: python dewey_p3_inject.py
"""

import json
import os
import re

VAULT  = r"d:\10_pur3v4d3r's-vault"
EBOOK  = os.path.join(VAULT, "999-ebook-project")
INPUT  = os.path.join(EBOOK, "_dewey_scaffolded.md")
OUTPUT = os.path.join(EBOOK, "_dewey_injected.md")

NUM_TO_WORD = {
    1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
    6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten",
    11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen",
    15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen",
    19: "Nineteen",
}

# ---------------------------------------------------------------------------
# CALLOUT FORMATTERS
# ---------------------------------------------------------------------------

def fmt_quote(c):
    quote = c.get("quote", "").strip().strip('"')
    insight = c.get("insight", "").strip()
    return (
        f"> [!quote] Dewey's Voice\n"
        f"> \"{quote}\"\n"
        f">\n"
        f"> **💡 Analyst's Insight:** {insight}\n"
    )


def fmt_concept(c):
    name    = c.get("concept_name", "Unknown").strip()
    defn    = c.get("definition", "").strip()
    why     = c.get("why_it_matters", "").strip()
    modern  = c.get("modern_echo", "").strip()
    return (
        f"> [!info] Concept — [[{name}]]\n"
        f"> **Definition:** {defn}\n"
        f">\n"
        f"> **Why It Matters:** {why}\n"
        f">\n"
        f"> **Modern Echo:** {modern}\n"
    )


def fmt_warning(c):
    misconception = c.get("misconception", "").strip()
    correction    = c.get("correction", "").strip()
    relevant      = c.get("still_relevant", "").strip()
    return (
        f"> [!warning] Common Misreading\n"
        f"> **Dewey warns against:** {misconception}\n"
        f">\n"
        f"> **The Correction:** {correction}\n"
        f">\n"
        f"> **Still Relevant Because:** {relevant}\n"
    )


def fmt_tip(c):
    principle   = c.get("principle", "").strip()
    in_practice = c.get("in_practice", "").strip()
    return (
        f"> [!tip] Practical Application\n"
        f"> **Dewey's Principle:** {principle}\n"
        f">\n"
        f"> **In Practice:** {in_practice}\n"
    )


def fmt_synthesis(c):
    central = c.get("central_argument", "").strip()
    steps   = c.get("logical_progression", [])
    bridge  = c.get("bridge_to_next", "").strip()
    steps_str = "\n".join(f"> {idx+1}. {step}" for idx, step in enumerate(steps))
    return (
        f"> [!example] Chapter Synthesis\n"
        f"> **Central Argument:** {central}\n"
        f">\n"
        f"> **Logical Progression:**\n"
        f"{steps_str}\n"
        f">\n"
        f"> **Bridge to Next Chapter:** {bridge}\n"
    )


CALLOUT_FORMATTERS = {
    "quote":     fmt_quote,
    "concept":   fmt_concept,
    "warning":   fmt_warning,
    "tip":       fmt_tip,
    "synthesis": fmt_synthesis,
}


def format_callouts_block(callouts):
    """Format all callouts for a chapter as a markdown block."""
    parts = []
    for c in callouts:
        ctype = c.get("type", "")
        fmt = CALLOUT_FORMATTERS.get(ctype)
        if fmt:
            parts.append(fmt(c))
    return "\n".join(parts)


def format_abstract(data):
    abstract = data.get("abstract", "").strip()
    return f"> [!abstract] Chapter Summary\n> *{abstract}*\n"


def format_overview(data):
    return data.get("overview", "").strip() + "\n"


def format_concepts(data):
    concepts = data.get("concepts", [])
    if not concepts:
        return "*No concepts defined.*\n"
    lines = []
    for c in concepts:
        name = c.get("name", "Unknown").strip()
        defn = c.get("definition", "").strip()
        lines.append(f"- **[[{name}]]**: {defn}")
    return "\n".join(lines) + "\n"


def format_connections(data):
    conn = data.get("connections", {})
    lines = []

    for item in conn.get("builds_on", []):
        ch   = item.get("chapter")
        rsn  = item.get("reason", "")
        if ch:
            lines.append(f"- Builds on: [[Chapter {NUM_TO_WORD.get(ch, str(ch))}]] — *{rsn}*")
        else:
            lines.append(f"- Builds on: *(This is the opening chapter)* — *{rsn}*")

    for item in conn.get("anticipates", []):
        ch  = item.get("chapter")
        rsn = item.get("reason", "")
        if ch:
            lines.append(f"- Anticipates: [[Chapter {NUM_TO_WORD.get(ch, str(ch))}]] — *{rsn}*")

    for item in conn.get("contrasts_with", []):
        concept = item.get("concept", "")
        rsn     = item.get("reason", "")
        if concept:
            lines.append(f"- Contrasts with: [[{concept}]] — *{rsn}*")

    return ("\n".join(lines) + "\n") if lines else "*No connections defined.*\n"

# ---------------------------------------------------------------------------
# LOAD JSON FILES
# ---------------------------------------------------------------------------

def load_chapter_data():
    """Load all 19 JSON analysis files. Returns dict {chapter_num: data}."""
    result = {}
    missing = []
    for n in range(1, 20):
        fname = os.path.join(EBOOK, f"_dewey_ch{n:02d}.json")
        if os.path.exists(fname):
            with open(fname, "r", encoding="utf-8") as fh:
                try:
                    data = json.load(fh)
                    result[n] = data
                    print(f"  Loaded ch{n:02d}: {len(data.get('callouts', []))} callouts")
                except json.JSONDecodeError as e:
                    print(f"  ERROR parsing ch{n:02d}: {e}")
                    missing.append(n)
        else:
            print(f"  MISSING: _dewey_ch{n:02d}.json")
            missing.append(n)
    if missing:
        print(f"  Warning: {len(missing)} chapters have no JSON data: {missing}")
    return result

# ---------------------------------------------------------------------------
# CHAPTER DETECTOR
# ---------------------------------------------------------------------------

CHAPTER_HEADING_RE = re.compile(r'^## Chapter ([A-Z][a-z]+) — ')

WORD_TO_NUM = {
    "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5,
    "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10,
    "Eleven": 11, "Twelve": 12, "Thirteen": 13, "Fourteen": 14,
    "Fifteen": 15, "Sixteen": 16, "Seventeen": 17, "Eighteen": 18,
    "Nineteen": 19,
}

def get_chapter_num(line):
    """Extract chapter number from heading line. Returns int or None."""
    m = CHAPTER_HEADING_RE.match(line.strip())
    if m:
        word = m.group(1)
        return WORD_TO_NUM.get(word)
    return None

# ---------------------------------------------------------------------------
# MAIN PROCESSING
# ---------------------------------------------------------------------------

def process():
    print("Loading chapter JSON files...")
    chapter_data = load_chapter_data()

    print(f"  Loaded {len(chapter_data)} of 19 chapters")

    print("Reading scaffolded file: " + INPUT)
    with open(INPUT, "r", encoding="utf-8") as fh:
        lines = fh.readlines()

    print(f"  Input lines: {len(lines)}")

    out = []
    current_chapter = 0

    for line in lines:
        s = line.rstrip('\n')

        # Track current chapter
        ch_num = get_chapter_num(s)
        if ch_num is not None:
            current_chapter = ch_num
            out.append(line)
            continue

        data = chapter_data.get(current_chapter, {})

        # Replace placeholders
        stripped = s.strip()

        if stripped == "<!-- ABSTRACT_PLACEHOLDER -->":
            if data:
                out.append(format_abstract(data) + "\n")
            else:
                out.append(line)
            continue

        if stripped == "<!-- OVERVIEW_PLACEHOLDER -->":
            if data:
                out.append(format_overview(data) + "\n")
            else:
                out.append(line)
            continue

        if stripped == "<!-- CALLOUTS_PLACEHOLDER -->":
            if data and data.get("callouts"):
                block = format_callouts_block(data["callouts"])
                out.append(block + "\n")
            else:
                out.append(line)
            continue

        if stripped == "<!-- CONCEPTS_PLACEHOLDER -->":
            if data:
                out.append(format_concepts(data) + "\n")
            else:
                out.append(line)
            continue

        if stripped == "<!-- CONNECTIONS_PLACEHOLDER -->":
            if data:
                out.append(format_connections(data) + "\n")
            else:
                out.append(line)
            continue

        # Default: pass through
        out.append(line)

    print("Writing: " + OUTPUT)
    with open(OUTPUT, "w", encoding="utf-8") as fh:
        fh.writelines(out)

    print("Done.")
    print(f"  Output lines: {len(out)}")

    # Quick stats
    content = "".join(out)
    callout_count  = content.count("> [!")
    wikilink_count = content.count("[[")
    abstract_count = content.count("> [!abstract]")
    synthesis_count = content.count("[!example] Chapter Synthesis")
    print(f"  Callouts:   {callout_count}")
    print(f"  Wiki-links: {wikilink_count}")
    print(f"  Abstracts:  {abstract_count} (expect 19)")
    print(f"  Syntheses:  {synthesis_count} (expect 19)")


if __name__ == "__main__":
    process()
