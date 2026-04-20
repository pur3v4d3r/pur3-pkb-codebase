#!/usr/bin/env python3
"""
dewey_p4_finalize.py -- Phase 5: YAML + TOC + Intro + Final Output
Adds YAML frontmatter, generates the Table of Contents, writes the
150-250 word introduction section, and produces the final document.

Input:  999-ebook-project/_dewey_injected.md
Output: 999-ebook-project/dewey-how-we-think-formatted.md

Run: python dewey_p4_finalize.py
"""

import re
import os

VAULT  = r"d:\10_pur3v4d3r's-vault"
EBOOK  = os.path.join(VAULT, "999-ebook-project")
INPUT  = os.path.join(EBOOK, "_dewey_injected.md")
OUTPUT = os.path.join(EBOOK, "dewey-how-we-think-formatted.md")

# ---------------------------------------------------------------------------
# YAML FRONTMATTER
# ---------------------------------------------------------------------------

YAML_FRONTMATTER = """\
---
title: "How We Think"
author: "John Dewey"
year: 1910
type: book-notes
status: complete
tags:
  - philosophy
  - education
  - epistemology
  - pragmatism
  - reflective-thinking
  - john-dewey
created: 2026-02-20
modified: 2026-02-20
aliases:
  - How We Think Dewey
  - Dewey How We Think
  - HWT Dewey
---

"""

# ---------------------------------------------------------------------------
# INTRODUCTION (150-250 words)
# ---------------------------------------------------------------------------

INTRODUCTION = """\
> [!tip] Reading Guide
> This document is best read in two ways: **linearly**, following Dewey's cumulative
> argument from Chapter One through Nineteen; or **thematically**, jumping between
> chapters via the [[#🔗 Connections]] sections that link related ideas. The callout
> boxes throughout are analytical annotations — not summaries of Dewey's text, but
> interpretive lenses for applying his ideas to contemporary learning and knowledge work.

## Introduction

[[John Dewey]]'s *How We Think* (1910, revised 1933) is one of the foundational texts
of [[Pragmatism]] and [[Educational Philosophy]]. Written for teachers and educated
general readers, it addresses a deceptively simple question: what does it mean to think
*well*? Dewey's answer unfolds across nineteen chapters organized in three parts —
diagnosing the problem of training thought, analyzing the logical structure of
[[Reflective Thinking]], and prescribing the conditions under which schools can genuinely
cultivate the thinking mind.

The book's central thesis is that **[[Reflective Thinking]]** — the disciplined suspension of
judgment while evidence is gathered and tested — is not a natural default but a cultivated
habit. It emerges from genuine [[Doubt]], proceeds through successive [[Inference]] and
[[Hypothesis|hypothesis-testing]], and culminates in warranted belief. This is not
passive reception but active **[[Inquiry]]**: a transaction between a person and a
problematic situation.

Dewey's work anticipates [[Metacognition]], [[Problem-Solving|problem-based learning]],
and modern [[Critical Thinking]] frameworks by nearly a century. Reading it today, one
finds both a precise philosophical anatomy of thought and a practical manual for
anyone who teaches, learns, or manages knowledge.

"""

# ---------------------------------------------------------------------------
# TOC GENERATOR
# ---------------------------------------------------------------------------

def generate_toc(lines):
    """
    Parse the document lines and generate an anchor-linked Table of Contents.
    Captures # (Parts) and ## (Chapters) level headings.
    """
    toc_lines = ["## 📚 Table of Contents\n\n"]
    part_pattern    = re.compile(r'^# (Part .+)$')
    chapter_pattern = re.compile(r'^## (Chapter .+)$')

    # Obsidian anchor: lowercase, spaces → -, remove special chars
    def make_anchor(heading_text):
        a = heading_text.lower()
        a = re.sub(r'[^\w\s-]', '', a)
        a = re.sub(r'\s+', '-', a.strip())
        return a

    for line in lines:
        s = line.rstrip()
        pm = part_pattern.match(s)
        cm = chapter_pattern.match(s)
        if pm:
            text   = pm.group(1)
            anchor = make_anchor(text)
            toc_lines.append(f"- [[#{text}]]\n")
        elif cm:
            text   = cm.group(1)
            anchor = make_anchor(text)
            toc_lines.append(f"  - [[#{text}]]\n")

    toc_lines.append("\n")
    return toc_lines

# ---------------------------------------------------------------------------
# MAIN PROCESSING
# ---------------------------------------------------------------------------

def process():
    print("Reading injected file: " + INPUT)
    with open(INPUT, "r", encoding="utf-8") as fh:
        lines = fh.readlines()

    print(f"  Input lines: {len(lines)}")

    # Generate TOC from content
    toc = generate_toc(lines)
    print(f"  TOC entries: {len(toc) - 2}")  # subtract header + trailing newline

    # Build output: replace FRONTMATTER_PLACEHOLDER and TOC_PLACEHOLDER
    out = []
    out.append(YAML_FRONTMATTER)

    skip_next_blank = False

    i = 0
    while i < len(lines):
        raw = lines[i]
        s   = raw.rstrip('\n').strip()

        if s == "<!-- FRONTMATTER_PLACEHOLDER -->":
            # Skip — we already wrote the YAML
            i += 1
            continue

        if s == "<!-- TOC_PLACEHOLDER -->":
            # Inject intro + TOC
            out.append(INTRODUCTION)
            out.extend(toc)
            i += 1
            continue

        # Pass through all other lines
        out.append(raw)
        i += 1

    print("Writing final document: " + OUTPUT)
    with open(OUTPUT, "w", encoding="utf-8") as fh:
        fh.writelines(out)

    print("Done.")

    # Verification stats
    content = "".join(out)
    lines_out      = content.count('\n')
    chapter_count  = content.count('\n## Chapter ')
    part_count     = content.count('\n# Part ')
    callout_count  = content.count('> [!')
    abstract_count = content.count('[!abstract] Chapter Summary')
    synthesis_count = content.count('[!example] Chapter Synthesis')
    wikilink_count = content.count('[[')
    bold_count     = len(re.findall(r'\*\*[^*]+\*\*', content))

    print("\n=== FINAL DOCUMENT STATS ===")
    print(f"  Output lines:   {lines_out}")
    print(f"  Parts:          {part_count} (expect 3)")
    print(f"  Chapters:       {chapter_count} (expect 19)")
    print(f"  Callouts total: {callout_count}")
    print(f"  Abstracts:      {abstract_count} (expect 19)")
    print(f"  Syntheses:      {synthesis_count} (expect 19)")
    print(f"  Wiki-links:     {wikilink_count} (expect 100+)")
    print(f"  Bold spans:     {bold_count}")


if __name__ == "__main__":
    process()
