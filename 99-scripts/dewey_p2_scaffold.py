#!/usr/bin/env python3
"""
dewey_p2_scaffold.py -- Phase 2: Chapter Scaffolding + Bold + Wiki-Links
Adds Obsidian callout template headers, bolds key Dewey terms (first mention
per chapter), and adds wiki-links for core concepts (first mention per chapter).

Input:  999-ebook-project/_dewey_structural.md
Output: 999-ebook-project/_dewey_scaffolded.md

Run: python dewey_p2_scaffold.py
"""

import re
import os

VAULT  = r"d:\10_pur3v4d3r's-vault"
EBOOK  = os.path.join(VAULT, "999-ebook-project")
INPUT  = os.path.join(EBOOK, "_dewey_structural.md")
OUTPUT = os.path.join(EBOOK, "_dewey_scaffolded.md")

# ---------------------------------------------------------------------------
# TERMS TO BOLD (first mention per chapter)
# Key philosophical / educational terms central to Dewey's argument
# Stored as lowercase for case-insensitive matching; displayed as-found in text
# ---------------------------------------------------------------------------
BOLD_TERMS = [
    "reflective thinking",
    "reflective thought",
    "inquiry",
    "doubt",
    "suggestion",
    "inference",
    "empirical",
    "inductive",
    "deductive",
    "analysis",
    "synthesis",
    "judgment",
    "observation",
    "imagination",
    "hypothesis",
    "data",
    "evidence",
    "problem",
    "perplexity",
    "testing",
    "verification",
    "logical",
    "reasoning",
    "conception",
    "meaning",
    "abstraction",
    "experience",
    "knowledge",
    "belief",
    "habit",
    "impulse",
    "curiosity",
    "open-mindedness",
    "whole-heartedness",
    "responsibility",
    "stream of consciousness",
    "critical thinking",
    "subject matter",
    "discipline",
]

# ---------------------------------------------------------------------------
# WIKI-LINKS (first mention per chapter)
# Core concepts that should become nodes in the knowledge graph
# Stored as (display_form, set_of_match_variants_lowercase)
# ---------------------------------------------------------------------------
WIKILINKS = [
    # (wiki_display, [match_strings_in_text_lowercase])
    ("Reflective Thinking",    ["reflective thinking"]),
    ("Empirical Inquiry",      ["empirical inquiry"]),
    ("Doubt",                  ["doubt"]),
    ("Hypothesis",             ["hypothesis"]),
    ("Inference",              ["inference"]),
    ("Induction",              ["induction", "inductive reasoning"]),
    ("Deduction",              ["deduction", "deductive reasoning"]),
    ("Judgment",               ["judgment"]),
    ("Pragmatism",             ["pragmatism", "pragmatic"]),
    ("Epistemology",           ["epistemology"]),
    ("William James",          ["william james"]),
    ("Aristotle",              ["aristotle"]),
    ("John Dewey",             ["john dewey", "dewey"]),
    ("Stream of Consciousness", ["stream of consciousness"]),
    ("Scientific Method",      ["scientific method"]),
    ("Problem-Solving",        ["problem-solving", "problem solving"]),
    ("Critical Thinking",      ["critical thinking"]),
    ("Metacognition",          ["metacognition"]),
    ("Cognitive Load",         ["cognitive load"]),
    ("Active Learning",        ["active learning"]),
    ("Experiential Learning",  ["experiential learning"]),
    ("Subject Matter",         ["subject matter"]),
    ("Open-Mindedness",        ["open-mindedness", "open mindedness"]),
    ("Curiosity",              ["curiosity"]),
    ("Observation",            ["observation"]),
]

# ---------------------------------------------------------------------------
# BUILD FAST-LOOKUP STRUCTURES
# ---------------------------------------------------------------------------

def build_bold_patterns():
    """Build compiled regex patterns for bold terms, longest first."""
    patterns = []
    for term in sorted(BOLD_TERMS, key=len, reverse=True):
        # Word-boundary match, case-insensitive
        pat = re.compile(r'\b(' + re.escape(term) + r')\b', re.IGNORECASE)
        patterns.append((term.lower(), pat))
    return patterns


def build_wiki_patterns():
    """Build compiled regex patterns for wiki-link terms."""
    patterns = []
    for display, matches in WIKILINKS:
        for m in sorted(matches, key=len, reverse=True):
            pat = re.compile(r'\b(' + re.escape(m) + r')\b', re.IGNORECASE)
            patterns.append((m.lower(), display, pat))
    return patterns


BOLD_PATTERNS = build_bold_patterns()
WIKI_PATTERNS = build_wiki_patterns()

# ---------------------------------------------------------------------------
# LINE TRANSFORMERS
# ---------------------------------------------------------------------------

def apply_bold(line, seen_bold):
    """Bold first occurrence of key terms. Updates seen_bold set."""
    result = line
    for term_key, pat in BOLD_PATTERNS:
        if term_key in seen_bold:
            continue
        m = pat.search(result)
        if m:
            # Replace first occurrence only with bold
            result = pat.sub(r'**\1**', result, count=1)
            seen_bold.add(term_key)
    return result


def apply_wikilinks(line, seen_wiki, seen_bold):
    """Wiki-link first occurrence of key concepts.
    Also marks matched terms in seen_bold to prevent double-formatting."""
    result = line
    for term_key, display, pat in WIKI_PATTERNS:
        if term_key in seen_wiki:
            continue
        m = pat.search(result)
        if m:
            matched_text = m.group(1)
            result = result[:m.start()] + "[[" + display + "|" + matched_text + "]]" + result[m.end():]
            seen_wiki.add(term_key)
            # Prevent bold from applying to this same term (avoids bold inside [[]])
            seen_bold.add(term_key)
    return result


def transform_line(line, seen_bold, seen_wiki, in_body):
    """Apply all transformations to a body-text line."""
    if not in_body:
        return line
    # Skip markdown structural lines
    s = line.strip()
    if (s.startswith('#') or s.startswith('>') or s.startswith('<!--')
            or s.startswith('---') or not s):
        return line
    # Apply wiki-links first; this also updates seen_bold for linked terms
    line = apply_wikilinks(line, seen_wiki, seen_bold)
    # Apply bold only to terms not already wiki-linked
    line = apply_bold(line, seen_bold)
    return line

# ---------------------------------------------------------------------------
# CHAPTER FOOTER TEMPLATE
# Appended at the end of each chapter's body content
# ---------------------------------------------------------------------------

CHAPTER_FOOTER = """
### Overview

<!-- OVERVIEW_PLACEHOLDER -->

---

### 📖 Key Passages & Analysis

<!-- CALLOUTS_PLACEHOLDER -->

---

### 🧠 Core Concepts Introduced

<!-- CONCEPTS_PLACEHOLDER -->

---

### 🔗 Connections

<!-- CONNECTIONS_PLACEHOLDER -->

"""

# ---------------------------------------------------------------------------
# MAIN PROCESSING
# ---------------------------------------------------------------------------

def process():
    print("Reading: " + INPUT)
    with open(INPUT, "r", encoding="utf-8") as fh:
        lines = fh.readlines()

    total = len(lines)
    print("  Input lines: " + str(total))

    out = []
    i = 0

    # State
    in_chapter      = False   # inside a chapter block
    in_body         = False   # past the ABSTRACT_PLACEHOLDER (body text)
    chapter_num     = 0
    chapters_done   = 0

    # Per-chapter term tracking
    seen_bold  = set()
    seen_wiki  = set()

    # Chapter heading pattern
    CHAPTER_HEADING_RE = re.compile(r'^## Chapter ([A-Z][a-z]+) — ')
    PART_HEADING_RE    = re.compile(r'^# Part ')
    ABSTRACT_MARKER    = "<!-- ABSTRACT_PLACEHOLDER -->"

    while i < len(lines):
        raw = lines[i]
        s   = raw.rstrip('\n').strip()

        # ── New chapter or part: close previous chapter first ─────────────
        is_new_chapter = CHAPTER_HEADING_RE.match(s)
        is_new_part    = PART_HEADING_RE.match(s)

        if (is_new_chapter or is_new_part) and in_chapter:
            # End previous chapter: insert footer before the separator
            # The separator line `---` precedes this heading — back-track to insert
            # Actually: find the last `---` in out and insert footer before it
            # Simpler: just append footer now, before we emit the divider
            out.append(CHAPTER_FOOTER)
            in_chapter = False
            in_body    = False
            seen_bold  = set()
            seen_wiki  = set()
            chapters_done += 1

        if is_new_chapter:
            in_chapter = True
            in_body    = False
            out.append(raw)
            i += 1
            continue

        # ── Abstract placeholder: marks transition point ──────────────────
        if ABSTRACT_MARKER in s:
            out.append(raw)
            in_body = True
            i += 1
            continue

        # ── Part headers reset state ───────────────────────────────────────
        if is_new_part:
            in_chapter = False
            in_body    = False
            out.append(raw)
            i += 1
            continue

        # ── Separator lines: pass through ─────────────────────────────────
        if s == "---":
            out.append(raw)
            i += 1
            continue

        # ── Body text: apply transformations ──────────────────────────────
        if in_body and in_chapter:
            transformed = transform_line(raw.rstrip('\n'), seen_bold, seen_wiki, True)
            out.append(transformed + "\n")
            i += 1
            continue

        # ── Default: pass through ─────────────────────────────────────────
        out.append(raw)
        i += 1

    # Close last chapter if still open
    if in_chapter:
        out.append(CHAPTER_FOOTER)
        chapters_done += 1

    print("Writing: " + OUTPUT)
    with open(OUTPUT, "w", encoding="utf-8") as fh:
        fh.writelines(out)

    print("Done.")
    print("  Chapters scaffolded: " + str(chapters_done))
    print("  Output lines: " + str(len(out)))


if __name__ == "__main__":
    process()
