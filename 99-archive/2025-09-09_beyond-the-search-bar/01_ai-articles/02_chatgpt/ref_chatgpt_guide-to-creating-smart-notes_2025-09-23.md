# The Smart Note: Architecture & Workflow for PKM

*Persona active: Expert Information Architect & Knowledge Management Strategist—clear, practical, principled.*

------

## Section 1: The Philosophy of a “Smart Note”

A note is not a jar for storing facts; it is a tool for thinking. Structure matters because your **future self** will not remember your **past context**. A smart note externalizes that context—what the idea means, why it matters, and where it connects—so that tomorrow’s brain can pick up the thread without friction.

**Purpose of a good note:**
 Transform raw input into *usable* knowledge. That means: (1) it can be understood in isolation, (2) it states why it’s valuable, and (3) it points to adjacent ideas so it can be recombined.

**Atomic note (one idea per note):**
 Capture **one coherent idea** per note. This lowers retrieval friction, makes linking specific, and lets you compose larger arguments by **connecting** small pieces rather than spelunking inside mega-documents. Atomic ≠ tiny; it means **conceptually singular**.

------

## Section 2: The Visual Architecture (Clarity for the Eyes)

Visual structure reduces cognitive load. You are designing a reading experience for your future self.

### Descriptive Titles

- **What it does:** Establishes identity and searchability at a glance.
- **Best practice:** Use *nouns + hook*. Prefer “Negative Space as Visual Breath (Composition)” over “Note 17.”
- **Tip:** Add a disambiguating suffix for recurring concepts (e.g., “Feedback Loops — Learning,” “Feedback Loops — Systems Dynamics”).

### The One-Sentence Summary Block

- **What it does:** Compresses the essence into a single breath. It’s your “why this matters” checksum.
- **Best practice:** Write **after** you finish the note. Phrase as: *“In short: …”* or *“This matters because …”*
- **Format:** Make it visually distinct (blockquote or callout) and place it immediately under the title.

### Headings and Subheadings

- **What they do:** Create scannable landmarks and chunk meaning.
- **Best practice:** Use a **shallow hierarchy** (H2/H3; rarely deeper). Each section should answer a single question (e.g., *What is it? Why does it matter? How do I use it?*).

### Strategic Formatting (Bold, Italics, Highlights)

- **Bold:** Final decisions, definitions, or claims.
- *Italics:* Emphasis, nuance, or terms being defined for the first time.
- ==Highlight== (if your editor supports it): Key “don’t-miss” phrases.
- **Rule:** Format to guide attention, not to decorate. If everything is emphasized, nothing is.

### Bulleted vs. Numbered Lists

- **Bulleted lists:** Unordered sets, examples, properties.
- **Numbered lists:** Sequences, procedures, arguments with steps.
- **Rule:** Keep list items parallel in grammar and length; split long items with sub-bullets.

### The Importance of White Space

- Generous line breaks around headings and major ideas.
- Short paragraphs (2–5 sentences).
- One idea cluster per visual block.
   White space is not “empty”—it is the oxygen your thinking breathes.

------

## Section 3: The Informational Architecture (Clarity for the Brain)

Make your notes **addressable** (easy to find), **contextual** (understandable later), and **interconnected** (combinable).

### Metadata / Frontmatter

**Role:** Supercharges search, surfacing, and automation.

**Common fields and why they matter:**

- `title`: The canonical name for indexing.
- `aliases`: Alternative titles for link-robustness (e.g., “negative space,” “white space in composition”).
- `tags`: Broad buckets for later filtering (`#composition`, `#learning`). Avoid tag soup—prefer 3–5 stable tags.
- `source`: Where this idea came from (URL, book, lecture).
- `created` / `updated`: Provenance; useful for reviewing and pruning.
- `summary`: Mirrors your one-sentence block for machine/readable use.
- `type`: e.g., `concept`, `technique`, `reference`, `literature-note`.
- `status`: `draft`, `evergreen`, or `needs-review` (helps with maintenance).
- `related`: Optional curated list of note IDs/titles.

Keep metadata **lightweight and consistent**. Consistency beats completeness.

### Contextual Linking

Links are **claims of relevance**. Write a **link sentence** that explains *why* the two ideas belong together. This preserves meaning even when the neighboring note changes.

**Patterns you can copy:**

- *“This note extends [[Visual Hierarchy — Design]] by specifying how **negative space** directs attention.”*
- *“For practical camera setup steps, see [[CPL Filter — Field SOP]], which operationalizes this concept.”*
- *“Counterpoint: [[Maximalist Composition]] argues for density as a style choice and when it works.”*

**Granularity tip:** Link **to the smallest viable unit** (the atomic note), not to a giant omnibus page.

### The “Related Notes” Section (Curated Discovery)

- **Function:** A mini-bibliography of nearby ideas you *recommend* visiting next.
- **Best practice:** 3–7 items, each with a **7–15 word reason** (“because…”). Manual and thoughtful beats automatic and noisy.

**Example:**

- [[Rule of Thirds — Composition]] — because it’s the complementary framing strategy most people start with.
- [[Visual Weight — Perception]] — because negative space alters perceived weight and balance.
- [[Minimalism — Aesthetic]] — because minimalism uses emptiness as a design material.

------

## Section 4: The Universal Note Template

Copy–paste this into your PKM. It is editor-agnostic Markdown with YAML frontmatter.

```markdown
---
title: "[Descriptive Title Here]"
aliases:
  - "[Common Alternate Name 1]"
  - "[Common Alternate Name 2]"
tags:
  - "[#primary-domain]"   # e.g., #composition or #learning
  - "[#secondary]"
type: "[concept | technique | reference | literature-note]"
status: "[draft | evergreen | needs-review]"
source: "[URL, book/article citation, or 'personal synthesis']"
created: "[YYYY-MM-DD]"
updated: "[YYYY-MM-DD]"
summary: "[1–2 sentence summary in your own words.]"
related:
  - "[Related Note Title A]"
  - "[Related Note Title B]"
---

# [Descriptive Title Here]

> **In short:** [1–2 sentence summary in your own words. Why this matters.]

## What is the idea?
[Define the idea in clear terms. One paragraph that stands on its own.]

## Why does it matter?
[Explain the consequence, leverage, or problem it solves. Where is the edge?]

## How do I use it?
- [Bullet 1: actionable application or rule of thumb]
- [Bullet 2: concrete example or scenario]
- [Bullet 3: limits, caveats, or failure modes]

## Supporting Details / Evidence
- [Key point or quote] — *[source, page, timestamp]*  
- [Short paraphrase of evidence and how it supports the claim.]

## Contextual Links
- Because [reason], see [[Related Note A]].
- This contrasts with [[Related Note B]] because [reason].
- To apply operationally, use [[Procedure/SOP Note]].

## Related Notes (curated)
- [[Note A]] — because [7–15 word justification].
- [[Note B]] — because [7–15 word justification].
- [[Note C]] — because [7–15 word justification].

## Open Questions / Next Steps (optional)
- [What I’d test, explore, or watch for next.]

## Changelog
- [YYYY-MM-DD] Created as [draft/evergreen].  
- [YYYY-MM-DD] Updated: [what changed].
```

------

## Section 5: The Workflow (Standard Operating Procedure)

A reliable loop from spark → structure → synthesis → connection.

### SOP: Create a Smart Note

1. **Capture the spark (≤ 60 seconds).**
    Open a new note, paste the template, drop a working title and a quick placeholder summary like “TBD: about X from Y.”
2. **Ground the provenance (≤ 2 minutes).**
    Fill `source`, `created`. If this came from a book, add page or timestamp; if from you, write “personal synthesis.”
3. **Braindump (5–10 minutes).**
    In “What is the idea?” write freely **in your own words**. Do not format yet. Capture examples that made the idea click.
4. **Refactor into structure (5–10 minutes).**
   - Split the braindump into **What / Why / How**.
   - Convert scattered thoughts into bulleted lists (unordered) or numbered steps (ordered).
   - Add **bold** to the single sentence that carries each section’s main claim.
5. **Synthesize the one-sentence summary (2 minutes).**
    Return to the top and write a crisp, consequential statement: *“In short: … because … therefore …”*
6. **Contextual links (3–5 minutes).**
    Add 2–4 **link sentences** under “Contextual Links.” Each must include a *because* clause. Prefer atomic targets.
7. **Curate “Related Notes” (2–3 minutes).**
    Pick 3–7 neighbors and add a **short justification** for each. This is your recommendation engine for your future self.
8. **Finalize metadata (1–2 minutes).**
    Set `tags` (3–5 stable tags), `type`, and `status`. Add `aliases` if the idea has common alternate names.
9. **Micro-review (90 seconds).**
   - Can this note be understood by a stranger?
   - Does the summary truly say **why it matters**?
   - Are there at least two contextual links with explicit reasons?
10. **Maintain lightly (later).**
     When you touch the note again, update `updated` and add a line to **Changelog**. Promote `status` to `evergreen` once it feels stable.

------

### Quality Gates (use before you file it away)

- **Atomicity check:** Is there **one** idea here? If there are two, split.
- **Reusability check:** Could this be quoted in a future piece **without** extra explanation?
- **Connectivity check:** Do the links state **why** they exist?

------

### A tiny worked example of contextual linking

- *“This note **extends** [[Rule of Thirds — Composition]] by showing how **negative space** stabilizes off-center subjects.”*
- *“For a deliberate counterexample, see [[Maximalist Composition]]—it favors density, which changes how negative space reads.”*

------

## Closing Perspective

A smart note is a **thinking primitive**: small enough to hold in the mind, rich enough to be worth revisiting, and wired into a network that compounds over time. Build consistently, link intentionally, and keep your visual structure gentle on the eyes. The system will start to think with you.