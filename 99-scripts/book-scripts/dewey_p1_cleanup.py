#!/usr/bin/env python3
"""
dewey_p1_cleanup.py -- Phase 1: OCR Cleanup + Structural Headings
Transforms raw OCR text of "How We Think" by John Dewey into
Obsidian-compatible structured markdown.

Input:  999-ebook-project/how-we-think-john-dewey.md  (raw OCR, 11789 lines)
Output: 999-ebook-project/_dewey_structural.md         (cleaned + headings)

Run: python dewey_p1_cleanup.py
"""

import re
import os

VAULT  = r"d:\10_pur3v4d3r's-vault"
EBOOK  = os.path.join(VAULT, "999-ebook-project")
INPUT  = os.path.join(EBOOK, "how-we-think-john-dewey.md")
OUTPUT = os.path.join(EBOOK, "_dewey_structural.md")

# ---------------------------------------------------------------------------
# LOOKUP TABLES
# ---------------------------------------------------------------------------

CHAPTER_TITLES = {
    1:  "What Is Thinking?",
    2:  "Why Reflective Thinking Must Be an Educational Aim",
    3:  "Native Resources in Training Thought",
    4:  "School Conditions and the Training of Thought",
    5:  "The Psychological Factor in Logical Form",
    6:  "Examples of Inference and Testing",
    7:  "Analysis of Reflective Thinking",
    8:  "The Place of Judgment in Reflective Activity",
    9:  "Understanding: Ideas and Meanings",
    10: "Understanding: Conception and Definition",
    11: "Systematic Method: Control of Data and Evidence",
    12: "Systematic Method: Control of Reasoning and Concepts",
    13: "Empirical and Scientific Thought",
    14: "Activity and the Training of Thought",
    15: "From the Concrete to the Abstract",
    16: "Language and the Training of Thought",
    17: "Observation and Information in the Training of Mind",
    18: "The Recitation and the Training of Thought",
    19: "Some General Conclusions",
}

PART_TITLES = {
    1: "The Problem of Training Thought",
    2: "Logical Considerations",
    3: "The Training of Thought",
}

WORD_TO_NUM = {
    "ONE": 1, "TWO": 2, "THREE": 3, "FOUR": 4, "FIVE": 5,
    "SIX": 6, "SEVEN": 7, "EIGHT": 8, "NINE": 9, "TEN": 10,
    "ELEVEN": 11, "TWELVE": 12, "THIRTEEN": 13, "FOURTEEN": 14,
    "FIFTEEN": 15, "SIXTEEN": 16, "SEVENTEEN": 17, "EIGHTEEN": 18,
    "NINETEEN": 19,
}

NUM_TO_WORD = {
    1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
    6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten",
    11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen",
    15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen",
    19: "Nineteen",
}

# ---------------------------------------------------------------------------
# COMPILED PATTERNS
# ---------------------------------------------------------------------------

# "CHAPTER WORD" (e.g., CHAPTER FOUR)
CHAPTER_RE = re.compile(r'^CHAPTER\s+([A-Z]+)\s*$')

# "PART WORD" (e.g., PART ONE)
PART_RE = re.compile(r'^PART\s+([A-Z]+)\s*$')

# Roman numeral section header: "I. Text here" or "I. TEXT HERE"
# Also catches OCR variants: "II]." (bracket inserted), "TI." (T misread as I)
# Patterns: I., II., III., IV., V.  and garbled versions II]., TI., I1.
SECTION_RE = re.compile(
    r'^([IVXTI]{1,5}[\]\[\.]{1,2}|[IVX]{1,5}\.)\s+(.+)$'
)

# Page header artifact: any line ending with "HOW WE THINK" or "JOHN DEWEY"
# Catches: "4 HOW WE THINK", "(Pe HOW WE THINK", "a HOW WE THINK", "284. HOW WE THINK"
PAGE_HEADER_RE = re.compile(r'^.{0,20}HOW WE THINK\s*$|^.{0,20}JOHN DEWEY\s*$', re.I)

# Running chapter headers with page numbers: "WHAT IS THINKING? 5", "REFLECTIVE THINKING AN AIM 19"
# Pattern: ALL CAPS text (possibly with ?, ', numbers) ending with a page number (or OCR'd page number)
RUNNING_HEADER_RE = re.compile(
    r'^[A-Z1][A-Z0-9\s\?\!\'\,\.\:]+\s+[\dDiJlI]{1,4}[\]\,\.]?\s*$'
)

# Footnote reference lines (e.g. "* See page 238.")
FOOTNOTE_RE = re.compile(r'^\d?\s*[\*\dagger]?\s*See page \d+', re.I)

# Hyphenated line ending
HYPHEN_END_RE = re.compile(r'\S-$')

# ALL CAPS line (chapter title area) -- must be >= 3 chars
# Allows spaces, apostrophes, hyphens, colons, commas
ALL_CAPS_RE = re.compile(r'^[A-Z][A-Z\s\'\-\:,\.]+$')

# Title-case sub-section header (e.g., "The Best Way of Thinking")
# Heuristic: standalone line, 10-70 chars, starts with capital, ends without common body endings
SUBSECTION_RE = re.compile(r'^[A-Z\'\"\*\(][A-Za-z\s\'\-\:\?\!\(\)\"\.0-9]{9,69}$')

# Known "keep as-is" body-text starters (quoted speech etc.)
BODY_STARTERS = re.compile(r'^["\*\(]?[A-Z].*[,;:\.\?\!]$|^[a-z]')

# Garbage line: very short (<=10 chars) and no real word content
# Catches: "a", "i", "ee 7", "- ", "—_", "Peek a", "wate", etc.
GARBAGE_SHORT_RE = re.compile(r'^.{1,10}$')
REAL_WORD_RE     = re.compile(r'[A-Za-z]{3,}')  # has at least one 3-letter word

# ---------------------------------------------------------------------------
# HELPERS
# ---------------------------------------------------------------------------

def titlecase_section(text):
    """Convert OCR mixed-case section heading to Title Case."""
    minor = {'of', 'the', 'a', 'an', 'and', 'but', 'or', 'nor',
             'in', 'on', 'at', 'to', 'for', 'with', 'by', 'from', 'as', 'is'}
    words = text.strip().split()
    result = []
    for idx, w in enumerate(words):
        # Strip trailing punctuation for comparison
        core = w.rstrip(':.,!?').lower()
        tail = w[len(w.rstrip(':.,!?')):]
        if idx == 0 or core not in minor:
            result.append(core.capitalize() + tail)
        else:
            result.append(core + tail)
    return ' '.join(result)


def is_garbage(s):
    """True if line is an OCR garbage artifact to be deleted."""
    if not s:
        return False
    if GARBAGE_SHORT_RE.match(s) and not REAL_WORD_RE.search(s):
        return True
    # Lines with weird character mixtures (from illustration pages)
    # e.g. "PHS POC HS secN DP RODU GL OF", "BB er CaP Cr LV lays P Y="
    if '=' in s or '\\' in s or len([c for c in s if c.isdigit()]) > 3:
        return True
    return False


def is_title_zone_end(s):
    """True if this line indicates the title zone is over (body text started)."""
    # Section header always ends title zone
    if SECTION_RE.match(s):
        return True
    # Long enough to be body text (>45 chars)
    if len(s) > 45:
        return True
    # Starts with lowercase (continuation / quotation)
    if s and s[0].islower():
        return True
    # Starts with a quote or special char
    if s and s[0] in ('"', '*', '(', "'", '\u201c', '\u2018'):
        return True
    return False

# ---------------------------------------------------------------------------
# MAIN PROCESSING
# ---------------------------------------------------------------------------

def process():
    print("Reading: " + INPUT)
    with open(INPUT, "r", encoding="utf-8") as fh:
        raw = fh.readlines()

    total = len(raw)
    print("  Input lines: " + str(total))

    # Strip newlines
    lines = [l.rstrip('\n') for l in raw]

    out = []

    # State machine
    started          = False   # True once we've seen first PART or CHAPTER
    in_title_zone    = False   # True right after CHAPTER header
    skip_part_sub    = False   # True: next non-blank line is Part subtitle (skip)
    chapters_seen    = 0

    # Hyphen-join buffer
    pending_half_word = ""

    # Emit document scaffold header (Phase 5 will prepend YAML)
    out.append("<!-- FRONTMATTER_PLACEHOLDER -->\n\n")
    out.append("# How We Think\n\n")
    out.append("*John Dewey (1933)*\n\n")
    out.append("---\n\n")
    out.append("<!-- TOC_PLACEHOLDER -->\n\n")

    i = 0
    while i < len(lines):
        raw_line = lines[i]
        s        = raw_line.strip()

        # ── Skip front-matter before first structural marker ──────────────
        if not started:
            if PART_RE.match(s) or CHAPTER_RE.match(s):
                started = True
                # Fall through to handle this line
            else:
                i += 1
                continue

        # ── PART header ────────────────────────────────────────────────────
        m = PART_RE.match(s)
        if m:
            pword = m.group(1).strip()
            pnum  = WORD_TO_NUM.get(pword)
            if pnum:
                ptitle = PART_TITLES.get(pnum, "Unknown Part")
                out.append("\n---\n\n")
                out.append("# Part " + NUM_TO_WORD[pnum] + " \u2014 " + ptitle + "\n\n")
                skip_part_sub = True
                in_title_zone = False
                i += 1
                continue

        # ── Skip Part subtitle (line after PART header) ────────────────────
        if skip_part_sub:
            if s:  # non-blank: this is the subtitle line -- skip it
                skip_part_sub = False
            i += 1
            continue

        # ── CHAPTER header ─────────────────────────────────────────────────
        m = CHAPTER_RE.match(s)
        if m:
            chword = m.group(1).strip()
            chnum  = WORD_TO_NUM.get(chword)
            if chnum:
                chtitle = CHAPTER_TITLES.get(chnum, "Unknown Chapter")
                out.append("\n---\n\n")
                out.append("## Chapter " + NUM_TO_WORD[chnum] + " \u2014 " + chtitle + "\n\n")
                out.append("<!-- ABSTRACT_PLACEHOLDER -->\n\n")
                in_title_zone = True
                chapters_seen += 1
                i += 1
                continue

        # ── Title zone (right after CHAPTER header) ────────────────────────
        if in_title_zone:
            if not s:  # blank -- skip
                i += 1
                continue
            if is_title_zone_end(s):
                in_title_zone = False
                # Fall through to process this line normally
            elif is_garbage(s):
                i += 1
                continue
            elif ALL_CAPS_RE.match(s) and len(s) >= 3:
                i += 1  # Skip OCR chapter title
                continue
            else:
                # Might be garbled title text -- skip if short
                if len(s) < 45:
                    i += 1
                    continue
                else:
                    in_title_zone = False
                    # Fall through

        # ── Page header artifacts ──────────────────────────────────────────
        if PAGE_HEADER_RE.match(s):
            i += 1
            continue

        # ── Running chapter headers (ALL CAPS + page number) ───────────────
        if RUNNING_HEADER_RE.match(s):
            # Must be >= 65% uppercase letters to avoid catching body text
            alpha = [c for c in s if c.isalpha()]
            upper = [c for c in s if c.isupper()]
            if alpha and len(upper) / len(alpha) >= 0.65:
                i += 1
                continue

        # ── Footnote / See page references ────────────────────────────────
        if FOOTNOTE_RE.match(s):
            i += 1
            continue

        # ── Garbage lines ──────────────────────────────────────────────────
        if s and is_garbage(s):
            i += 1
            continue

        # ── Roman numeral section header ───────────────────────────────────
        m = SECTION_RE.match(s)
        if m:
            roman = m.group(1).rstrip('.][ ')  # strip trailing dots/brackets
            text  = m.group(2)
            # Look ahead: if next non-blank line looks like a continuation
            # (short, mixed/upper case, no sentence-ending punctuation),
            # append it to the title before titlecasing
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines):
                nxt = lines[j].strip()
                # Continuation: short (< 40), not a new section, all/mostly caps
                is_cont = (
                    nxt and len(nxt) < 40
                    and not SECTION_RE.match(nxt)
                    and not CHAPTER_RE.match(nxt)
                    and not PART_RE.match(nxt)
                    and not RUNNING_HEADER_RE.match(nxt)
                    and not any(c.isdigit() for c in nxt[-3:])
                )
                alpha_n = [c for c in nxt if c.isalpha()]
                upper_n = [c for c in nxt if c.isupper()]
                if is_cont and alpha_n and len(upper_n) / len(alpha_n) >= 0.5:
                    text = text + " " + nxt
                    i = j  # will be incremented at end of block
            tcase = titlecase_section(text)
            out.append("\n### " + roman + ". " + tcase + "\n\n")
            i += 1
            continue

        # ── Hyphenated line-join ────────────────────────────────────────────
        # OCR splits hyphenated words across lines: "reflec-\ntive"
        if HYPHEN_END_RE.search(s) and not s.endswith('--'):
            # Look ahead for the continuation
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines):
                next_s = lines[j].strip()
                # Only join if continuation starts with lowercase (word continuation)
                if next_s and next_s[0].islower():
                    joined = s[:-1] + next_s
                    out.append(joined + "\n")
                    i = j + 1
                    continue

        # ── Default: emit line as-is ────────────────────────────────────────
        out.append(raw_line + "\n")
        i += 1

    print("Writing: " + OUTPUT)
    with open(OUTPUT, "w", encoding="utf-8") as fh:
        fh.writelines(out)

    lines_out = len(out)
    print("Done.")
    print("  Chapters processed: " + str(chapters_seen))
    print("  Output lines: " + str(lines_out))


if __name__ == "__main__":
    process()
