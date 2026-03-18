# PKM/PKB Framework — Permanent Notes Generator

> Automated pipeline for extracting, generating, auditing, and gap-filling permanent notes from a 30-report PKM/PKB Framework series.

---

## Overview

This project takes **30 structured JSON extractions** from the PKM & PKB Framework report series and transforms them into a fully connected library of **665 Obsidian-compatible permanent notes** — complete with YAML frontmatter, wiki-links, callout-based definitions, and cross-references.

The pipeline has three stages:

| Stage | Script | Output |
|-------|--------|--------|
| **1. Generate** | `generate_notes.py` | 398 permanent notes from report definitions & original syntheses |
| **2. Audit** | `audit_notes.py` | Wiki-link resolution report, orphan detection, connectivity stats |
| **3. Gap-Fill** | `generate_stubs.py` | 267 stub notes for missing wiki-link targets |

**Final metrics:**

| Metric | Before Stubs | After Stubs |
|--------|-------------|-------------|
| Total notes | 398 | 665 |
| Wiki-link resolution | 29.3% (164/559) | 86.2% (799/927) |
| Missing concepts | 299 | 32 |
| Orphan notes | 244 (61.3%) | 1 (0.2%) |

---

## Requirements

- **Python 3.10+** (stdlib only — no external packages required)
- Input: JSON files produced by `pkb_extractor.py v1.1.0` (already included in `extraction-material/json/`)

---

## Project Structure

```
_pkm-and-pkb-framework-1.0.0/
├── README.md                          ← You are here
├── _audit-report-2026-03-18.md        ← Latest audit report (markdown)
├── _permanent-notes/                  ← 665 generated .md files
│   ├── Accommodation.md               ← Full permanent note (from report)
│   ├── Activity-Theory.md             ← Stub note (gap-fill)
│   └── ...
├── extraction-material/
│   ├── json/                          ← 30 JSON extractions (input data)
│   │   ├── 01-foundations-of-knowledge-architecture-..._extracted.json
│   │   ├── 02-architecture-of-learning-..._extracted.json
│   │   └── ... (30 files)
│   └── markdown/                      ← Original markdown extractions
├── report-series/                     ← 31 source report .md files
├── scripts/
│   ├── config.py                      ← All paths, constants, mappings
│   ├── report_parser.py               ← JSON loader + note candidate extractor
│   ├── note_builder.py                ← Markdown/YAML builder for permanent notes
│   ├── generate_notes.py              ← Stage 1: main generation CLI
│   ├── audit_notes.py                 ← Stage 2: wiki-link audit CLI
│   └── generate_stubs.py              ← Stage 3: stub generator CLI
├── 00-PKM-PKB-Framework-*.md          ← Map of Content (MOC) files
└── review-of-framework-codebase/      ← Codebase review documentation
```

---

## Quick Start

All commands are run from the project root:

```bash
cd 999-report-orginizing/_pkm-and-pkb-framework-1.0.0
```

### 1. Generate Permanent Notes

```bash
# Dry run — show what would be generated (no files written)
python scripts/generate_notes.py

# Write all notes to _permanent-notes/
python scripts/generate_notes.py --execute

# Process a single report (e.g. report 01)
python scripts/generate_notes.py --report 01 --execute

# List available JSON files
python scripts/generate_notes.py --list

# Preview candidates from a specific report
python scripts/generate_notes.py --preview 01
```

### 2. Audit Wiki-Link Resolution

```bash
# Console report
python scripts/audit_notes.py

# Show top 30 missing concepts
python scripts/audit_notes.py --top 30

# Generate markdown audit report
python scripts/audit_notes.py --markdown

# Both options combined
python scripts/audit_notes.py --markdown --top 50
```

### 3. Generate Stub Notes (Gap-Fill)

```bash
# Dry run — show plan without writing
python scripts/generate_stubs.py

# Execute — write stub files to disk
python scripts/generate_stubs.py --execute

# Only generate for concepts with 15+ references
python scripts/generate_stubs.py --execute --min-refs 15

# Filter by category
python scripts/generate_stubs.py --execute --category concept
python scripts/generate_stubs.py --execute --category person

# List all missing concepts with their categories
python scripts/generate_stubs.py --list
```

---

## Scripts Reference

### `config.py` — Central Configuration

All tuneable settings live here. Edit this file to adapt the pipeline to your vault.

| Setting | Default | Purpose |
|---------|---------|---------|
| `OUTPUT_DIR` | `_permanent-notes/` | Where generated notes are written |
| `JSON_DIR` | `extraction-material/json/` | Where input JSON files live |
| `NOTE_GENERATING_CALLOUTS` | `["definition", "original-synthesis"]` | Callout types that produce notes |
| `MAX_FILENAME_LENGTH` | `80` | Max filename characters (excluding `.md`) |
| `MAX_EVIDENCE_PER_NOTE` | `3` | Evidence callouts per note |
| `MAX_INSIGHTS_PER_NOTE` | `2` | Analytical insights per note |
| `MAX_EXPANSION_TOPICS` | `4` | Expansion topic suggestions per note |
| `MAX_WIKI_LINKS_DISPLAY` | `15` | Wiki-links shown in body |
| `MAX_RELATED_LINKS` | `10` | Related links in frontmatter |
| `MAX_SEE_ALSO_LINKS` | `8` | See-also links in frontmatter |
| `DOMAIN_MAP` | *(see file)* | Maps raw domain strings → standardised slugs |
| `VALID_DOMAINS` | *(see file)* | Allowed domain values for frontmatter |
| `KNOWLEDGE_LEVEL_TO_COMPLEXITY` | *(see file)* | Maps report knowledge levels → complexity |

---

### `report_parser.py` — JSON Loading & Candidate Extraction

Reads JSON files and extracts `NoteCandidate` objects — one per definition or original-synthesis callout.

**Key components:**

- **`ReportMetadata`** — dataclass for report-level frontmatter (domain, tags, knowledge level)
- **`NoteCandidate`** — dataclass containing everything needed to build a permanent note:
  - Concept name, domain, definition text
  - Supporting callouts (evidence, insights, connections, practices, warnings)
  - Wiki-links, expansion topics, builds-on / feeds-into relationships
- **`parse_definition_title(title)`** — extracts concept name and domain from callout titles like `"Definition: Schema Theory (Cognitive Psychology)"`
- **`extract_note_candidates(data)`** — main extraction function: scans all callouts, builds candidates, resolves domains

---

### `note_builder.py` — Markdown Generation

Converts `NoteCandidate` objects into complete permanent note markdown files.

**Key components:**

- **`sanitize_filename(name)`** — converts concept names to safe filenames (strips unsafe chars, replaces spaces with hyphens, truncates)
- **`_clean_concept_name(raw)`** — strips `[[` and `]]` brackets from concept names
- **`_build_aliases(clean_name)`** — generates aliases by splitting on em-dashes (`—`), colons (`:`), and slashes (`/`); deduplicates and adds acronym variants
- **`build_frontmatter(candidate)`** — produces complete YAML frontmatter block with all fields: title, aliases, type, status, confidence, domain, complexity-level, tags, dates, relationships (builds-on, enables, wiki-links, related, see-also), expansion-topics
- **`build_body(candidate)`** — produces markdown body: H1, definition callout, explanation, evidence callouts, key insights, practical implications, connections, expansion topics, and "Referenced In" footer
- **`build_permanent_note(candidate)`** — combines frontmatter + body into a complete file

---

### `generate_notes.py` — Stage 1: Main Generator CLI

The primary pipeline script. Discovers JSON files, extracts candidates, deduplicates, and writes permanent notes.

**Features:**

- **Dry run by default** — pass `--execute` to write files
- **Deduplication** — detects duplicate concept names across reports; keeps the richer version
- **Single-report mode** — `--report 01` to process just one report
- **Preview mode** — `--preview 01` shows candidates without processing
- **Progress reporting** — shows per-report and overall statistics

**CLI flags:**

| Flag | Description |
|------|-------------|
| `--execute` | Write files to disk (default: dry run) |
| `--report N` | Process only report number N (e.g. `01`, `15`) |
| `--list` | List available JSON files and exit |
| `--preview N` | Preview note candidates from report N |

---

### `audit_notes.py` — Stage 2: Wiki-Link Audit

Scans all permanent notes, extracts wiki-link targets, and measures resolution against existing files.

**How resolution works:**

The audit builds a **resolution index** mapping lowercase aliases and filename stems to actual files. A wiki-link target is "resolved" if its lowercased form matches any alias or stem in the index. Unresolved targets are classified as:

- **Report references** — links like `01-foundations-of-...` (expected unresolved)
- **Placeholders** — template strings like `Note Title A`
- **Missing concepts** — genuinely absent notes that should exist

**Output:**

- Console report with summary table, top missing concepts, orphan list
- Markdown report (`_audit-report-2026-03-18.md`) with full details

**CLI flags:**

| Flag | Description |
|------|-------------|
| `--markdown` | Write markdown report to project root |
| `--top N` | Show top N missing concepts (default: 20) |
| `--notes-dir PATH` | Override notes directory path |

---

### `generate_stubs.py` — Stage 3: Stub Generator

Creates minimal permanent notes for concepts that are referenced but have no file.

**Categorisation engine:**

Each missing concept is automatically categorised:

| Category | Detection Method | Example |
|----------|-----------------|---------|
| `concept` | Default fallback for short, clean names | "Schema Theory", "Metacognition" |
| `person` | First name in common-names set + ≤5 words, or comma/ampersand patterns | "Alan Baddeley", "Anderson et al." |
| `domain` | Matches known domain/field names | "Educational Psychology", "Neuroscience" |
| `tool` | Matches known tool/platform names | "Anki", "Obsidian Dataview" |
| `expansion` | Long names (60+ chars) with colons or em-dashes | "AI-Augmented Heutagogy — Affordances and Risks" |
| `skip` | Pure year numbers, YAML fragments | "2024" |

**Domain inference:** uses keyword matching to assign domains (e.g. "cognitive", "memory" → `cognitive-psychology`; "pedagog", "Zimmerman" → `educational-psychology`).

**Stub note structure:**

Each stub includes:
- Full YAML frontmatter (seedling status, low confidence, category-specific tags, backlinks)
- Category-appropriate definition callout with expansion instructions
- "Referenced By" section listing up to 20 notes that link to this concept
- Auto-generation attribution note

**CLI flags:**

| Flag | Description |
|------|-------------|
| `--execute` | Write stub files to disk (default: dry run) |
| `--min-refs N` | Only generate stubs for concepts with N+ references (default: 5) |
| `--category CAT` | Filter to one category: `concept`, `person`, `domain`, `tool`, `expansion` |
| `--list` | List all missing concepts with categories and reference counts |
| `--notes-dir PATH` | Override notes directory path |

---

## Workflow: Full Pipeline Run

To regenerate everything from scratch:

```bash
# Step 1: Generate primary notes from JSON extractions
python scripts/generate_notes.py --execute

# Step 2: Run initial audit to see wiki-link gaps
python scripts/audit_notes.py --top 30

# Step 3: Generate stub notes for missing concepts (5+ references)
python scripts/generate_stubs.py --execute --min-refs 5

# Step 4: Re-audit to verify improvement
python scripts/audit_notes.py --markdown --top 30
```

> **Note:** Steps 1-3 are safe to re-run. The generator skips existing files by filename, and the stub generator checks for existing files before writing.

---

## Generated Note Format

### Full Permanent Notes (from reports)

```yaml
---
title: "Concept Name"
aliases:
  - "Concept Name"
  - "CN"
type: permanent-note
status: developing
confidence: established
domain: cognitive-psychology
complexity-level: intermediate
tags:
  - concept
  - cognitive-psychology
  - schema-theory
doc_created: 2026-03-18
doc_modified: 2026-03-18
source-type: report-extraction
extraction-method: pkb-extractor-v1.1.0
source-report: "01-foundations-of-knowledge-architecture"
builds-on:
  - "[[Related Concept A]]"
enables:
  - "[[Related Concept B]]"
wiki-links:
  - "[[Link 1]]"
  - "[[Link 2]]"
related:
  - "[[Related Note]]"
see-also:
  - "[[See Also Note]]"
expansion-topics:
  - topic: "[[Expansion Topic]]"
    description: "Why this is worth exploring"
    priority: medium
# ...
---

# Concept Name

> [!definition] Concept Name — Cognitive Psychology
> Full definition text from the report...

## Explanation & Context
...

> [!evidence] Evidence: Study Title
> Evidence text...

## Key Insights
...

## Practical Implications
...

## Connections & Cross-References
...

## Expansion Topics
...
```

### Stub Notes (gap-fill)

```yaml
---
title: "Missing Concept Name"
aliases:
  - "Missing Concept Name"
type: permanent-note
status: seedling
confidence: low
domain: cognitive-psychology
tags:
  - concept-stub
  - cognitive-psychology
doc_created: 2026-03-18
doc_modified: 2026-03-18
source-type: stub-generation
extraction-method: generate-stubs-v1.0
referenced-by-count: 12
see-also:
  - "[[Linking Note 1]]"
  - "[[Linking Note 2]]"
# ...
---

# Missing Concept Name

> [!definition] Missing Concept Name
> **Status: Stub — awaiting development.**
>
> This note was auto-generated because 12 other permanent notes
> reference this concept. Expand with a proper definition,
> evidence, and connections.

---

*Auto-generated stub — 12 references across the permanent notes library.*

## Referenced By

- [[Linking Note 1]]
- [[Linking Note 2]]
- ...
```

---

## Customisation Guide

### Adding New Reports

1. Run your extractor to produce a new `*_extracted.json` in `extraction-material/json/`
2. Run `python scripts/generate_notes.py --execute` — only new notes are written (existing files are skipped)
3. Run `python scripts/generate_stubs.py --execute` — new stubs for any new missing concepts

### Changing Content Limits

Edit `scripts/config.py`:

```python
MAX_EVIDENCE_PER_NOTE = 5    # Was 3 — show more evidence per note
MAX_EXPANSION_TOPICS = 6     # Was 4 — more expansion suggestions
MAX_FILENAME_LENGTH = 100    # Was 80 — allow longer filenames
```

### Changing the Domain Taxonomy

Add entries to `DOMAIN_MAP` in `config.py` to handle new domain strings:

```python
DOMAIN_MAP = {
    # ... existing entries ...
    "behavioral science": "cognitive-psychology",
    "data science": "computer-science",
}
```

And add the slug to `VALID_DOMAINS` if it's a new category:

```python
VALID_DOMAINS = [
    # ... existing ...
    "behavioral-science",
]
```

### Changing Stub Categorisation

Edit the detection sets in `generate_stubs.py`:

```python
TOOL_NAMES = {
    "dataview", "canvas", "obsidian", "anki",
    "notion",   # ← add new tools here
}

DOMAIN_NAMES = {
    "educational psychology", "cognitive science",
    "data science",  # ← add new domains here
}
```

---

## Git History

| Commit | Description |
|--------|-------------|
| `a0db20a` | Initial permanent notes generation (398 notes) |
| `17f404e` | Fix YAML parse errors — escape double quotes in topic names |
| `855328b` | Rewrite alias generation for wiki-link resolution |
| `5d7b0c9` | Add `audit_notes.py` — wiki-link audit tool |
| `cfa5ca6` | Generate 267 stub notes — 86.2% resolution, 1 orphan |

---

## Known Limitations

1. **32 remaining missing concepts** — 18 are year references (`2024`), 1 is a YAML truncation artifact, ~13 are single-reference concepts below the `--min-refs 5` threshold. Lower the threshold with `--min-refs 1` to generate stubs for these.

2. **Expansion topic description truncation** — Some notes have expansion-topics whose descriptions were truncated mid-wiki-link (e.g. `[[Dual Coding Theory` without closing `]]`). This causes 1 corrupted audit entry covering 14 notes. The root cause is in `note_builder.py`'s description truncation logic — a fix would ensure wiki-links are never split.

3. **Re-running `generate_notes.py --execute`** will skip all existing files (including stubs). To regenerate a specific note, delete its file first, then re-run.

4. **Person detection** relies on a set of ~174 common first names. Uncommon names may be miscategorised as concepts.

---

## License

Internal PKB tooling — not distributed externally.
