---
title: "Markdown Extractor Suite — README"
doc_type: "documentation"
doc_created: 2026-04-21
doc_modified: 2026-04-21
tags:
  - documentation/scripts
  - tool/python
  - extractor-suite
---

# Markdown Extractor Suite

A set of focused, single-purpose Python scripts that scan a folder of Obsidian-flavoured Markdown files and emit a Markdown analytical report for one specific element each. Designed to be small, readable, dependency-light, and composable — run any combination from a tasks runner, a CI hook, or the terminal.

## Why one script per element?

Each extractor does **one thing**: extract a single category of element, aggregate its statistics, and emit a Markdown report. This keeps the code obvious, the reports focused, and the runtime fast. For an everything-at-once pipeline see [[../pkb_extractor.py]].

---

## Scripts

| Script | Extracts | Report filename |
|---|---|---|
| [`extract_yaml.py`](extract_yaml.py) | YAML frontmatter — fields, types, value distributions | `yaml-extraction-report-<date>.md` |
| [`extract_code_blocks.py`](extract_code_blocks.py) | Fenced code blocks — language, line counts, untagged audit | `code-blocks-extraction-report-<date>.md` |
| [`extract_wikilinks.py`](extract_wikilinks.py) | `[[wiki-links]]`, embeds, aliases, heading links | `wikilinks-extraction-report-<date>.md` |
| [`extract_callouts.py`](extract_callouts.py) | `> [!type]` callouts — types, titles, fold state, nesting | `callouts-extraction-report-<date>.md` |
| [`extract_tables.py`](extract_tables.py) | GFM tables — dimensions, headers, alignments | `tables-extraction-report-<date>.md` |
| [`_common.py`](_common.py) | Shared CLI parsing and Markdown table helpers (not run directly) | — |

---

## Common CLI

Every script shares the same argument surface:

```bash
python <script>.py --input <folder-or-file> [options]
```

| Flag | Default | Description |
|---|---|---|
| `--input` | *(required)* | Folder to scan, or a single `.md` file |
| `--output` | `<input>/<extractor>-report-<date>.md` | Override report destination |
| `--recursive` | off | Recurse into subfolders |
| `--exclude` | *(empty)* | Comma-separated folder names to skip (added to defaults) |
| `--top` | `25` | Top-N rows in frequency tables |
| `--quiet` | off | Suppress progress output |

Default excluded folders: `.obsidian`, `.git`, `.venv`, `node_modules`, `_attachments`, `_templates`, `__pycache__`.

### Examples

```bash
# Audit YAML schema across all permanent notes (recursively)
python extract_yaml.py --input "../../03-notes/permanent" --recursive

# Inspect code-block hygiene in your scripting docs
python extract_code_blocks.py --input "../../99-scripts" --top 40

# Find link hubs in a specific MOC folder
python extract_wikilinks.py --input "../../07-mocs"

# Survey callout taxonomy across the inbox
python extract_callouts.py --input "../../00-inbox" --recursive

# Discover table patterns across reference notes
python extract_tables.py --input "../../04-library" --recursive
```

Reports are written into the input folder by default, so they sit alongside the files they analyse.

---

## What each script extracts and reports

### 1. `extract_yaml.py`

**Extracts:** Every YAML frontmatter block (between `---` fences at the top of a file).

**Reports:**

- Coverage: how many files have / lack frontmatter, parse errors
- Field frequency table: every key, type(s), coverage %, example values
- Value distributions for low-cardinality fields (e.g. `status`, `note_type`)
- List of files missing frontmatter
- List of files with parse errors

**Optional dependency:** `pip install pyyaml` for proper YAML parsing. Without it the script falls back to a naive `key: value` parser (still useful for flat schemas).

---

### 2. `extract_code_blocks.py`

**Extracts:** Every fenced code block (```` ``` ```` or `~~~`).

**Reports:**

- Total blocks, total lines, files with code
- Language distribution: blocks, lines, file count, share %
- Top files by code volume
- Untagged-block audit: blocks lacking a language identifier (a syntax-highlighting hygiene check)

---

### 3. `extract_wikilinks.py`

**Extracts:** `[[Target]]`, `[[Target|Alias]]`, `[[Target#Heading]]`, and `![[Embed]]`. Code-fenced and inline-code regions are stripped first to avoid false positives.

**Reports:**

- Totals: links, unique targets, embeds, aliased, heading links, avg per file
- Most-linked targets (network hubs)
- Files with highest link density
- Files with zero outgoing links (isolation candidates)
- Alias patterns (target → alias usage)
- Most-embedded targets
- Most-linked headings

---

### 4. `extract_callouts.py`

**Extracts:** Obsidian callouts of the form `> [!type][+/-] Title` plus their multi-line bodies.

**Reports:**

- Totals: callouts, unique types, titled vs untitled, nested
- Type distribution (`[!note]`, `[!warning]`, `[!definition]`, …)
- Foldable state distribution (default / open `+` / collapsed `-`)
- Files with highest callout density
- Common title words (surfaces topical patterns)

---

### 5. `extract_tables.py`

**Extracts:** GFM tables (header row immediately followed by a separator row of dashes / colons).

**Reports:**

- Totals: tables, rows, files containing tables, avg rows per table
- Column-count distribution
- Row-size buckets (`0`, `1–5`, `6–20`, `21–50`, `50+`)
- Column alignment usage (`default`, `left`, `right`, `center`)
- Most common header labels (surfaces table-schema reuse)
- Files with the most / widest tables

---

## Requirements

- **Python:** 3.10+
- **Standard library only**, except `pip install pyyaml` is recommended for `extract_yaml.py`.

If you use the workspace `.venv`:

```bash
source .venv/Scripts/activate    # Git Bash on Windows
pip install pyyaml               # optional, only for extract_yaml.py
```

---

## Report structure

Every report shares the same shape:

1. **YAML frontmatter** with `title`, `extractor`, `source`, `file_count`, `tags`
2. **Executive Summary** (high-level metrics table)
3. **Distribution tables** specific to the extractor
4. **Top-N rankings** of files / values / patterns
5. **Audit sections** highlighting hygiene issues (where applicable)

Reports use Obsidian-flavoured `[[wiki-links]]` for file references so they're navigable directly inside Obsidian.

---

## Extending the suite

To add a new extractor (e.g. for footnotes, tasks, or images):

1. Copy any existing extractor as a template.
2. Replace the regex / parser in `extract()`.
3. Update the `analyse()` aggregator with the metrics you care about.
4. Add the matching tables in `render_report()`.
5. Reuse `build_arg_parser`, `gather_markdown_files`, `md_table`, and `report_frontmatter` from `_common.py`.

The shared helpers enforce a consistent CLI and report style — keep new scripts inside this folder so the imports continue to work.

---

## Related

- [[../pkb_extractor.py]] — comprehensive single-file pipeline that extracts every element type at once
- [[../folder_review_report.py]] — analytical review report focused on themes, link analytics, and integrity
- [[../vault_indexer.py]] — navigational MOC generator
