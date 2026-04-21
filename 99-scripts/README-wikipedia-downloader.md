---
title: "Wikipedia Article Downloader — Complete Command Reference"
aliases: [Wikipedia Downloader, wikipedia_downloader.py, Wiki Article Downloader, Wikipedia Scraper]
doc_type: reference-note
tags:
  - script
  - python
  - pkb-automation
  - wikipedia
  - reference-note
  - cli-tool
status: evergreen
certainty: established
doc_created: 2026-04-21
doc_modified: 2026-04-21
---

# 📚 Wikipedia Article Downloader — Complete Command Reference

> [!abstract] Purpose
> Fetch any Wikipedia article and convert it into a fully-structured Obsidian reference note — complete with rich YAML frontmatter, ghost-linked internal references, citation block, and license attribution.

**Script:** [wikipedia_downloader.py](wikipedia_downloader.py)
**Location:** `D:\10_pur3v4d3r's-vault\99-scripts\wikipedia_downloader.py`

---

## 📑 Table of Contents

1. [[#✨ What It Does]]
2. [[#🛠 Installation]]
3. [[#⚡ Quick Start]]
4. [[#🚀 Command Cookbook]]
5. [[#🎛 Full CLI Reference]]
6. [[#📝 Generated Note Structure]]
7. [[#⚙️ Configuration]]
8. [[#🔁 Batch Operations]]
9. [[#🩹 Troubleshooting]]
10. [[#🔗 Related PKB Tools]]

---

## ✨ What It Does

- Calls Wikipedia's official **REST API** (`/page/summary`, `/page/html`) and **Action API** (`prop=categories|contributors|revisions`) — no scraping.
- Converts the article HTML to clean Markdown via `markdownify`.
- Rewrites internal `/wiki/Foo` links to Obsidian `[[wiki-links]]` (ghost-link friendly).
- Builds YAML frontmatter with: `title`, `aliases`, `source_url`, `page_id`, `wikidata_id`, `description`, `doc_created`, `doc_modified` (article last revision), `status`, `certainty`, `authors` (top contributors), `references_count`, `tags` (auto-derived from categories), `related`.
- Strips Wikipedia chrome (edit links, infoboxes, navboxes, hatnotes, sister-site banners).
- Handles disambiguation pages, redirects, and missing articles gracefully.
- Prompts interactively for optional metadata, or runs fully non-interactively with `--no-prompt`.

---

## 🛠 Installation

### 1. Activate your virtual environment

```bash
# Windows / Git Bash (this vault)
source .venv/Scripts/activate

# macOS / Linux
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1

# Windows CMD
.venv\Scripts\activate.bat
```

### 2. Install dependencies

```bash
pip install requests beautifulsoup4 markdownify python-slugify rich
```

### 3. Verify the script

```bash
python -m py_compile 99-scripts/wikipedia_downloader.py && echo "✅ OK"
python 99-scripts/wikipedia_downloader.py --help
```

---

## ⚡ Quick Start

```bash
# Simplest possible call — interactive prompts for optional metadata
python 99-scripts/wikipedia_downloader.py "Albert Einstein"

# Non-interactive, accept all defaults
python 99-scripts/wikipedia_downloader.py "Albert Einstein" --no-prompt
```

Output → `04-library/wikipedia/albert-einstein.md`

---

## 🚀 Command Cookbook

### By Article Title

```bash
python 99-scripts/wikipedia_downloader.py "Carl Jung"
python 99-scripts/wikipedia_downloader.py "Cognitive Load Theory"
python 99-scripts/wikipedia_downloader.py "Mercury (planet)"           # disambiguated
```

### From a Full URL

```bash
python 99-scripts/wikipedia_downloader.py --url https://en.wikipedia.org/wiki/Stoicism
python 99-scripts/wikipedia_downloader.py --url https://en.wikipedia.org/wiki/Quantum_entanglement
```

### Choose Output Folder

```bash
python 99-scripts/wikipedia_downloader.py "Logic" --output 04-library/wikipedia
python 99-scripts/wikipedia_downloader.py "Plato" --output 03-notes/philosophy
python 99-scripts/wikipedia_downloader.py "React (software)" --output 999-codebase+pkb/refs
```

### Limit to Intro + Key Sections (scaffold mode)

```bash
# First 3 sections only — perfect for fleeting-note seeds
python 99-scripts/wikipedia_downloader.py "Knowledge graph" --sections 3

# First 5 sections
python 99-scripts/wikipedia_downloader.py "Bayesian inference" --sections 5
```

### Non-English Wikipedia

```bash
python 99-scripts/wikipedia_downloader.py "Filosofía"   --lang es
python 99-scripts/wikipedia_downloader.py "Philosophie" --lang de
python 99-scripts/wikipedia_downloader.py "Philosophie" --lang fr
python 99-scripts/wikipedia_downloader.py "哲学"         --lang ja
```

### Strip References / Disable Wiki-Link Conversion

```bash
# No References section in output
python 99-scripts/wikipedia_downloader.py "Spaced repetition" --no-references

# Keep external markdown links as-is (don't convert /wiki/Foo → [[Foo]])
python 99-scripts/wikipedia_downloader.py "Zettelkasten" --no-links

# Both
python 99-scripts/wikipedia_downloader.py "Memory" --no-references --no-links
```

### Fully Non-Interactive (CI / Batch)

```bash
python 99-scripts/wikipedia_downloader.py "Heuristic" --no-prompt --overwrite
```

### Combined "Power" Examples

```bash
# German article, 5 sections, custom folder, no prompts, overwrite
python 99-scripts/wikipedia_downloader.py "Erkenntnistheorie" \
  --lang de \
  --sections 5 \
  --output 04-library/wikipedia/de \
  --no-prompt \
  --overwrite

# Pull from URL, strip refs, save to specific PKB folder
python 99-scripts/wikipedia_downloader.py \
  --url https://en.wikipedia.org/wiki/Personal_knowledge_management \
  --output 03-notes/pkm \
  --no-references \
  --no-prompt \
  --overwrite
```

---

## 🎛 Full CLI Reference

```bash
python 99-scripts/wikipedia_downloader.py [TITLE] [OPTIONS]
```

| Flag | Type | Default | Description |
|---|---|---|---|
| `TITLE` (positional) | string | — | Article title to fetch (e.g. `"Carl Jung"`). Required unless `--url` is used. |
| `--url URL` | string | — | Full Wikipedia URL (overrides `TITLE` and `--lang`) |
| `--lang CODE` | string | `en` | Wikipedia language edition (`en`, `es`, `de`, `fr`, `ja`, ...) |
| `--output PATH` | path | `04-library/wikipedia` | Destination folder for the generated note |
| `--sections N` | int | `0` (all) | Truncate to first N top-level sections |
| `--no-references` | flag | off | Strip the References section from output |
| `--no-links` | flag | off | Keep internal links as plain markdown (don't convert to `[[wiki-links]]`) |
| `--no-prompt` | flag | off | Skip interactive metadata prompts (use defaults) |
| `--overwrite` | flag | off | Overwrite existing file without asking |
| `-h`, `--help` | flag | — | Show help message and exit |

### Exit Codes

| Code | Meaning |
|---|---|
| `0` | Success — note created |
| `1` | Article not found, user aborted, or HTTP error |
| `2` | Invalid CLI arguments (no title and no URL) |

---

## 📝 Generated Note Structure

```markdown
---
title: "Albert Einstein"
aliases: [Albert Einstein]
doc_type: reference-note
source: wikipedia
source_url: "https://en.wikipedia.org/wiki/Albert_Einstein"
source_lang: en
page_id: 736
wikidata_id: Q937
description: "German-born theoretical physicist (1879–1955)"
doc_created: 2026-04-21
doc_modified: 2026-04-15      # ← article's last revision date
status: seedling
certainty: moderate
knowledge_level: reference
authors:
  - ContributorName1
  - ContributorName2
references_count: 287
tags:
  - wikipedia
  - reference-note
  - external-source
  - wikipedia/physicists
  - wikipedia/nobel-laureates-in-physics
related: []
---

# Albert Einstein

> [!abstract] German-born theoretical physicist (1879–1955)
> Albert Einstein was a German-born theoretical physicist...

## Overview
...

## Article Content
...converted markdown with [[wiki-links]]...

## Source & Citation
- **Source:** [Wikipedia — Albert Einstein](https://en.wikipedia.org/wiki/Albert_Einstein)
- **Retrieved:** 2026-04-21
- **License:** CC BY-SA 4.0

## Related Notes
- *(Add wiki-links to related notes in your vault here.)*
```

---

## ⚙️ Configuration

Edit the `CONFIG` block at the top of [wikipedia_downloader.py](wikipedia_downloader.py):

```python
CONFIG = {
    "default_output_folder": "04-library/wikipedia",
    "default_lang": "en",
    "user_agent": "PKB-WikipediaDownloader/1.0 (Obsidian PKB; contact: local)",
    "max_sections": 0,            # 0 = all sections
    "include_references": True,
    "convert_internal_links": True,
    "tag_prefix": "wikipedia",    # category tags become wikipedia/<slug>
    "max_categories_as_tags": 8,
    "max_contributors": 5,
    "default_status": "seedling",
    "default_certainty": "moderate",
}
```

---

## 🔁 Batch Operations

### Bash loop — multiple titles

```bash
for topic in "Stoicism" "Epicureanism" "Cynicism (philosophy)" "Skepticism"; do
  python 99-scripts/wikipedia_downloader.py "$topic" \
    --output 04-library/wikipedia/philosophy \
    --no-prompt --overwrite
done
```

### From a text file (one title per line)

```bash
# topics.txt contains one article title per line
while IFS= read -r topic; do
  [ -z "$topic" ] && continue
  python 99-scripts/wikipedia_downloader.py "$topic" --no-prompt --overwrite
done < topics.txt
```

### PowerShell loop

```powershell
$topics = @("Plato", "Aristotle", "Socrates", "Heraclitus")
foreach ($t in $topics) {
  python 99-scripts/wikipedia_downloader.py $t --no-prompt --overwrite
}
```

### VS Code Task (add to `.vscode/tasks.json`)

```jsonc
{
  "label": "PKB: Download Wikipedia Article",
  "type": "shell",
  "command": "python",
  "args": [
    "${workspaceFolder}/99-scripts/wikipedia_downloader.py",
    "${input:wikiTitle}",
    "--no-prompt"
  ],
  "problemMatcher": []
}
// + add to inputs array:
// "inputs": [
//   { "id": "wikiTitle", "type": "promptString", "description": "Wikipedia article title" }
// ]
```

---

## 🩹 Troubleshooting

| Problem | Cause | Fix |
|---|---|---|
| `❌ Article not found` | Title typo or wrong language | Try `--url <full URL>`, check `--lang` |
| `⚠️ disambiguation page` | Title is ambiguous (e.g. `"Mercury"`) | Use the canonical disambiguated title (e.g. `"Mercury (planet)"`) or pick from the disambiguation page |
| `Missing dependencies` | Packages not installed in active env | `pip install requests beautifulsoup4 markdownify python-slugify rich` |
| `ModuleNotFoundError: No module named 'X'` | Wrong venv active | Run `source .venv/Scripts/activate` first |
| Empty body / weird formatting | Article uses unusual Wiki templates | Try with `--sections 5` to get clean intro only |
| HTTP 429 (rate limit) | Too many rapid calls | Wait a minute; add `sleep 1` in batch loops |
| Garbled non-Latin filenames | Slugify default behaviour | Filenames are slugified to ASCII; the `title` frontmatter field preserves the original |
| File exists, no overwrite | Safety guard | Add `--overwrite` flag |
| `SSL: CERTIFICATE_VERIFY_FAILED` | Corporate proxy / outdated certs | Update certs: `pip install --upgrade certifi` |

### Debug Mode

Add a quick `print` near the top of `main()` if you need to inspect the API response:

```python
import json
print(json.dumps(summary, indent=2))   # after client.summary(title)
```

### Test the API directly

```bash
# Quick sanity check — does the API respond?
curl -s "https://en.wikipedia.org/api/rest_v1/page/summary/Albert_Einstein" | head -50
```

---

## 🔗 Related PKB Tools

- [pkb_extractor.py](pkb_extractor.py) — Extract structured content from existing notes
- [scrape_universal.py](scrape_universal.py) — Download papers from arXiv / OpenReview / ACL
- [vault_indexer.py](vault_indexer.py) — Build a vault-wide content index
- [meta_audit.py](meta_audit.py) — Validate frontmatter compliance after downloading
- [link_check.py](link_check.py) — Find broken `[[wiki-links]]` (useful after Wikipedia ghost-link conversion)

---

## 📜 License & Attribution

> [!important] Wikipedia content licensing
> All content fetched from Wikipedia is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). The script automatically adds an attribution block to every generated note. **Do not strip this attribution** if redistributing notes.
