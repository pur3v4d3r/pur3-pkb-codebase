# 📂 Vault Indexer — README

> **Version:** 1.0.0  
> **Created:** 2026-03-13  
> **Script:** `vault_indexer.py`  
> **Requirements:** Python 3.8+ (no external dependencies)  
> **Optional:** `pip install pyyaml` for enhanced YAML parsing

---

## Overview

`vault_indexer.py` indexes an Obsidian vault folder (or any directory of Markdown files) and produces a **comprehensive Markdown index document** containing:

- **YAML frontmatter** for the index itself (Dataview-compatible)
- **Wikilinks** (`[[Note Name]]`) to every discovered document
- **Per-document metadata cards** with filesystem info, frontmatter fields, content analysis, and derived metrics
- **Aggregate statistics** — word counts, file sizes, tag distributions, status breakdowns
- **Health indicators** — missing frontmatter, empty docs, untagged notes, stale files
- **Connectivity analysis** — most/least linked documents
- **Tag taxonomy** with frequency table
- **Directory tree** visualization

The output is a production-ready Obsidian note that serves as a navigational hub (MOC-like) for the indexed folder.

---

## What It Extracts Per Document

### Filesystem Metadata
| Field | Description |
|-------|-------------|
| File size | Human-readable (e.g., "14.2 KB") |
| Created date | From filesystem (`st_birthtime` or `st_ctime`) |
| Modified date | From filesystem (`st_mtime`) |
| Days since modified | Computed staleness indicator |
| Relative path | Path from indexed root |
| Path depth | Folder nesting level |

### Frontmatter Metadata
| Field | Description |
|-------|-------------|
| title | `title`, `prompt_title`, or inferred from first heading / filename |
| tags | Normalized from YAML (inline `[]` or bullet `-` format) |
| aliases | All defined aliases |
| status | `draft`, `developing`, `evergreen`, `archived`, etc. |
| certainty | `speculative`, `provisional`, `moderate`, `established`, `verified` |
| note_type / doc_type | Note classification |
| knowledge_level | `developing`, `established`, `evergreen` |
| All custom fields | Any additional YAML keys are captured and displayed |

### Content Analysis
| Metric | Description |
|--------|-------------|
| Word count | Total words in document body |
| Estimated read time | Based on 200 WPM average |
| Heading count | Number of headings (H1–H6) |
| Wikilink count | Outgoing `[[links]]` with full list |
| Callout count | `> [!type]` blocks by type |
| Code block count | With language identifiers |
| Inline field count | `[**Field**:: Value]` patterns |
| External link count | `[text](https://...)` links |
| Embed count | `![[embeds]]` |
| Dataview presence | Whether note contains Dataview queries |
| Templater presence | Whether note contains Templater blocks |
| Body tags | `#tags` found in body text (not just frontmatter) |

### Derived Metrics
| Metric | Description |
|--------|-------------|
| Content density | Structure points (headings + callouts + links + fields) per 1000 words — a quality signal |
| Staleness | Days since last modification flagged against configurable threshold |
| Connectivity | Number of outgoing wikilinks |

---

## Index Output Sections

The generated index contains these sections:

1. **📊 Aggregate Statistics** — Total counts, averages, overall health
2. **📁 Folder Structure** — Distribution table + ASCII directory tree
3. **🏷️ Tag Taxonomy** — Frequency table with visual bars
4. **📈 Status & Type Distribution** — Pie-chart-ready breakdowns
5. **🕐 Recently Modified** — Documents changed in last 7 days
6. **⚠️ Stale Documents** — Not modified in >N days (configurable)
7. **🔗 Connectivity Overview** — Most/least connected documents
8. **📏 Largest Documents** — Top 10 by word count
9. **🚨 Health Indicators** — Missing frontmatter, empty docs, untagged notes
10. **📖 Document Directory** — Full alphabetical listing with per-doc metadata cards

---

## Installation

No installation required beyond Python 3.8+.

```bash
# Optional: install PyYAML for more robust frontmatter parsing
pip install pyyaml
```

The script works fine without PyYAML using built-in regex parsing, but PyYAML handles edge cases in complex YAML better.

---

## Usage

### Basic — Index a folder

```bash
python vault_indexer.py --input "D:/vault/04-library/philosophy"
```

Creates `04-library/philosophy/_index.md`.

### Custom output location

```bash
python vault_indexer.py --input "./03-notes" --output "./07-mocs/notes-index.md"
```

### Custom index name

```bash
python vault_indexer.py --input "./04-library" --name "library-catalog" --output "./07-mocs/notes-index.md"
```
```
python vault_indexer.py --input "D:\10_pur3v4d3r's-vault\999-report-orginizing\_pkm-and-pkb-framework-1.0.0\report-series" --name "pkb/pkm-framework-reports" --output "D:\10_pur3v4d3r's-vault\999-report-orginizing\_pkm-and-pkb-framework-1.0.0\extraction-material\pkb-pkm-framework-reports.md"
```

```
python vault_indexer.py --input "D:\10_pur3v4d3r's-vault\999-report-orginizing\_pkm-and-pkb-framework-1.0.0\report-series" --name "pkb/pkm-framework-reports" --output "D:\10_pur3v4d3r's-vault\999-report-orginizing\_pkm-and-pkb-framework-1.0.0\extraction-material\pkb-pkm-framework-reports.md"
```


Creates `04-library/library-catalog.md`.

### Limit recursion depth

```bash
python vault_indexer.py --input "." --depth 1
```

Only scans the top-level folder (no subfolders).

### Exclude folders

```bash
python vault_indexer.py --input "./04-library" --exclude "_templates,_archive,99-system"
```

Added to the default exclusion list (`.git`, `.obsidian`, `.trash`, `.venv`, `node_modules`, `__pycache__`).

### Custom staleness threshold

```bash
python vault_indexer.py --input "./03-notes" --stale 60
```

Documents not modified in 60+ days are flagged as stale (default: 30).

### Fast mode (skip content analysis)

```bash
python vault_indexer.py --input "./04-library" --no-content
```

Only extracts filesystem metadata and frontmatter — significantly faster for large folders.

### Dry run (preview without writing)

```bash
python vault_indexer.py --input "./04-library" --dry-run
```

Prints a summary to console without creating any files.

---

## CLI Reference

| Flag | Short | Default | Description |
|------|-------|---------|-------------|
| `--input` | `-i` | *(required)* | Folder to index |
| `--output` | `-o` | `<input>/_index.md` | Output file path |
| `--name` | `-n` | `_index` | Index filename (without `.md`) |
| `--depth` | `-d` | Unlimited | Max folder recursion depth |
| `--exclude` | `-e` | *(defaults)* | Comma-separated folders to skip |
| `--stale` | `-s` | `30` | Days threshold for staleness |
| `--no-content` | | `False` | Skip content analysis |
| `--dry-run` | | `False` | Preview without writing |

---

## Output Example

The generated index looks like this (abbreviated):

```markdown
---
title: "Index — philosophy"
doc_type: "folder-index"
doc_created: 2026-03-13
total_documents: 42
total_words: 87654
status: evergreen
tags:
  - index
  - auto-generated
  - folder-index
---

# 📂 Index — philosophy

> [!abstract] Overview
> Auto-generated index of **42** documents in `philosophy/`.
> Total content: **87,654** words · **1.2 MB** · ~**438** min read time.

## 📊 Aggregate Statistics

| Metric | Value |
|--------|-------|
| **Total Documents** | 42 |
| **Total Words** | 87,654 |
| ...

## 📖 Document Directory

### 1. [[epistemology-reference|Epistemology — A Reference Guide]]

| Property | Value |
|----------|-------|
| **File** | `epistemology-reference.md` |
| **Size** | 14.2 KB |
| **Created** | 2025-11-15 |
| **Modified** | 2026-02-28 |
| **Words** | 3,421 |
| **Status** | `evergreen` |

**Tags:** `#philosophy` `#epistemology` `#reference-note`
**Links to:** [[Knowledge]] · [[Justified True Belief]] · [[Empiricism]]
**Content Features:** 12 headings · 8 callouts · 2 code blocks (dataviewjs)
```

---

## Default Excluded Directories

These are always excluded (override with source edit if needed):

- `.git`
- `.obsidian`
- `.trash`
- `.venv`
- `node_modules`
- `__pycache__`
- `.DS_Store`
- `Thumbs.db`

Additional exclusions can be added via `--exclude`.

---

## How It Works

1. **Scan** — Recursively walks the input directory, collecting all `.md` files
2. **Parse** — For each file: reads filesystem stats, parses YAML frontmatter, analyzes markdown content structure
3. **Aggregate** — Computes vault-wide statistics: tag frequencies, status distributions, connectivity metrics, health indicators
4. **Render** — Produces a single Markdown document with all data organized into navigational sections
5. **Write** — Saves the index to the specified output path

The script is **read-only on your vault** — it only writes the single output index file.

---

## Tips

- **Re-run periodically** to keep the index current — the `doc_modified` field updates automatically
- **Use as an MOC** — the generated index functions like a Map of Content for the folder
- **Combine with Dataview** — since the index has proper frontmatter, you can query it with Dataview
- **Index multiple folders** — run the script multiple times with different `--input` paths
- **Fast iteration** — use `--dry-run` first to preview, then remove the flag to write

---

## Compatibility

- **Python:** 3.8+ (uses `pathlib`, `f-strings`, `typing`)
- **OS:** Windows, macOS, Linux
- **Obsidian:** Fully compatible output (wikilinks, callouts, YAML frontmatter)
- **Dataview:** Index frontmatter is Dataview-queryable
- **Encoding:** UTF-8 throughout
