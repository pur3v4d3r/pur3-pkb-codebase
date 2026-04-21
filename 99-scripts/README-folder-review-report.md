# 📋 Folder Review Report — README

> **Script:** `folder_review_report.py`
> **Version:** 1.0.0
> **Created:** 2026-04-21
> **Python:** 3.8+
> **Dependencies:** None required (PyYAML optional for richer frontmatter parsing)

---

## What It Does

`folder_review_report.py` reviews every Markdown file in a folder and generates a single, comprehensive **Markdown review report** saved into that same folder. The report focuses on three analytical pillars:

1. **Theme & Topic Analysis** — extracts top keywords, common title bigrams, and tag clusters from your notes.
2. **Wiki-Link Analytics** — link density, connection hubs, orphan detection, top-linked targets, aliased link patterns.
3. **Link Integrity** — broken wiki-links, broken embeds, suspicious external URLs.

The report opens with **YAML frontmatter** containing the report date, files reviewed count, total wiki-links, broken-link count, and other key metrics — making it Dataview-queryable.

### How it differs from `vault_indexer.py`

| Script | Purpose |
|---|---|
| `vault_indexer.py` | Builds a navigational MOC with a card per document |
| `folder_review_report.py` | Aggregate analytical snapshot + integrity audit |

---

## Installation

No installation required beyond Python 3.8+. Optionally:

```bash
pip install pyyaml
```

PyYAML enables full YAML parsing of frontmatter (lists, nested dicts). Without it, a fallback parser handles flat `key: value` pairs.

---

## Quick Start

```bash
# Review a single folder (non-recursive)
python 99-scripts/folder_review_report.py --input "./03-notes"

# Review a folder recursively
python 99-scripts/folder_review_report.py --input "./04-library" --recursive

# Review with vault-wide broken-link validation
python 99-scripts/folder_review_report.py --input "./00-inbox" --vault "."

# Preview without writing the file
python 99-scripts/folder_review_report.py --input "./03-notes" --dry-run
```

---

## All Commands & Options

### Required
| Flag | Description |
|---|---|
| `--input PATH` | Folder to review (required) |

### Optional
| Flag | Default | Description |
|---|---|---|
| `--output NAME` | `_REVIEW-REPORT-<date>.md` | Custom report filename |
| `--recursive` | off | Recurse into subfolders |
| `--vault PATH` | same as `--input` | Vault root used for cross-folder broken-link validation |
| `--exclude DIRS` | none | Comma-separated folder names to skip when recursive |
| `--top N` | `20` | Number of rows in "top N" tables |
| `--stopwords FILE` | none | Path to newline-delimited custom stopword file |
| `--dry-run` | off | Print summary to console without writing the file |
| `--quiet` | off | Suppress per-file progress output |

---

## Common Recipes

### Review your inbox

```bash
python 99-scripts/folder_review_report.py \
    --input "./00-inbox" \
    --vault "." \
    --top 30
```

### Recursive review of a large library

```bash
python 99-scripts/folder_review_report.py \
    --input "./04-library" \
    --recursive \
    --exclude "_attachments,_archive,drafts" \
    --vault "."
```

### Validate broken links across the entire vault

```bash
python 99-scripts/folder_review_report.py \
    --input "./03-notes" \
    --recursive \
    --vault "." \
    --output "_LINK-AUDIT-2026-04-21.md"
```

### Quick preview before committing

```bash
python 99-scripts/folder_review_report.py \
    --input "./00-inbox" \
    --dry-run \
    --quiet
```

### Custom stopword file

```bash
# Create stopwords.txt with one word per line, then:
python 99-scripts/folder_review_report.py \
    --input "./03-notes" \
    --stopwords "./99-scripts/stopwords.txt"
```

---

## Report Structure

The generated report contains the following sections:

| Section | Contents |
|---|---|
| **YAML Frontmatter** | Date, file count, totals, tags — Dataview-ready |
| **Executive Summary** | Headline metrics table |
| **File Inventory** | Table of every file: words, links, tags, modified date |
| **Theme & Topic Analysis** | Top keywords, common phrases (bigrams), tag clusters |
| **Wiki Link Analytics** | Top targets, hubs, density rankings, aliased links, orphans |
| **Link Integrity Report** | Broken wiki-links, broken embeds, suspicious external URLs |
| **Frontmatter Audit** | Field coverage table, files missing frontmatter |
| **Parse Errors** | Any files that failed to read (graceful) |
| **Recommendations** | Auto-generated improvement suggestions |

---

## Performance Notes

- **Single-pass parsing** — each file is read exactly once.
- **Compiled regex** — patterns compiled at module load.
- **Streaming-friendly** — designed to handle thousands of files without memory pressure.
- **Defensive** — a single corrupt file never aborts the run; errors are logged in the report.

Typical performance: **~500–1000 files per second** on a modern SSD.

---

## Output Location

The report is **always saved to the folder being reviewed** (per requirement). Default name:

```
_REVIEW-REPORT-YYYY-MM-DD.md
```

The leading underscore keeps it sorted to the top in most file browsers and Obsidian's file explorer. Override with `--output`.

---

## Frontmatter Schema of the Report

```yaml
---
title: "Folder Review Report — <folder-name>"
doc_type: "review-report"
report_date: 2026-04-21
report_timestamp: "2026-04-21T10:30:00+00:00"
folder_reviewed: "D:/path/to/folder"
recursive: false
files_reviewed: 42
total_words: 38291
total_size_bytes: 524288
total_wikilinks: 318
broken_wikilinks: 5
script: "folder_review_report.py v1.0.0"
tags:
  - report/folder-review
  - generated/automated
status: "generated"
---
```

This schema enables Dataview queries like:

```dataview
TABLE files_reviewed, broken_wikilinks, report_date
FROM "00-inbox"
WHERE doc_type = "review-report"
SORT report_date DESC
```

---

## Troubleshooting

| Problem | Solution |
|---|---|
| `❌ Not a directory` | Verify `--input` path exists and is a folder |
| `⚠️ No markdown files found` | Folder has no `.md` files; try `--recursive` |
| Many false-positive broken links | Pass `--vault PATH` pointing to your vault root |
| YAML parse warnings | Install PyYAML: `pip install pyyaml` |
| Report file already exists | Output is overwritten by default; use `--output` for a unique name |
| Slow on huge folders | Use `--quiet` to skip progress output; ensure SSD storage |

---

## Integration

### Run from a VS Code task

Add to `.vscode/tasks.json`:

```jsonc
{
  "label": "PKB: Folder Review Report (current folder)",
  "type": "shell",
  "command": "python",
  "args": [
    "${workspaceFolder}/99-scripts/folder_review_report.py",
    "--input", "${fileDirname}",
    "--vault", "${workspaceFolder}"
  ],
  "presentation": { "reveal": "always" }
}
```

### Schedule with Windows Task Scheduler

```powershell
python "D:\10_pur3v4d3r's-vault\99-scripts\folder_review_report.py" `
    --input "D:\10_pur3v4d3r's-vault\00-inbox" `
    --vault "D:\10_pur3v4d3r's-vault" `
    --quiet
```

---

## Exit Codes

| Code | Meaning |
|---|---|
| `0` | Success |
| `1` | No markdown files found |
| `2` | `--input` is not a valid directory |
| `3` | Failed to write the output file |

---

## License & Attribution

Generated by **PKB Scripting Architect** as part of the PKB automation suite.
Free to modify and extend for personal use.
