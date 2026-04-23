# V4 Condenser — Report-JSON → Permanent Notes (Local LLM)

> **One-line purpose:** Turn `*_extracted.json` files (produced by `pkb_extractor.py`) into atomic, kebab-case permanent notes by running each `[!definition]` callout through a local Ollama LLM that condenses the surrounding extracted context into a structured, Obsidian-ready markdown note.

**Status:** v1.0.0 — operational, 32/32 unit tests passing
**Script:** [`pipeline_v4.py`](pipeline_v4.py)
**Tests:** [`test_pipeline_v4.py`](test_pipeline_v4.py)
**Default model:** `qwen2.5:7b-instruct-q5_K_M` via Ollama
**Default output (where notes are written):** `D:\10_pur3v4d3r's-vault\999-report-organizing\_permanent-notes\v4-llm-condensed\` — override with `--output-dir PATH`
**Worthiness gate:** the LLM judges whether each concept warrants a permanent note; unworthy candidates are skipped (no file written, reason logged in the run summary). Disable with `--no-gate`.

---

## TL;DR — Run It Now

```powershell
# 1. Activate the vault venv (PowerShell)
& "d:\10_pur3v4d3r's-vault\.venv\Scripts\Activate.ps1"

# 2. Make sure Ollama is running and the model is pulled
ollama list                                       # confirm qwen2.5:7b-instruct-q5_K_M present
ollama pull qwen2.5:7b-instruct-q5_K_M            # only if missing

# 3. Dry-run preview — 2 concepts, no files written
python "d:\10_pur3v4d3r's-vault\99-scripts\report-extraction-to-permanent-notes-building-v4\pipeline_v4.py" --dry-run --limit 2 -v

# 4. Real run — process every JSON under the default extractor-output dir
python "d:\10_pur3v4d3r's-vault\99-scripts\report-extraction-to-permanent-notes-building-v4\pipeline_v4.py" -v
```

Output notes appear in `999-report-organizing/_permanent-notes/v4-llm-condensed/<kebab-title>.md`.

---

## Table of Contents

1. [What V4 Does](#what-v4-does)
2. [How V4 Differs from V3](#how-v4-differs-from-v3)
3. [Prerequisites](#prerequisites)
4. [Repository Layout](#repository-layout)
5. [Input Format](#input-format)
6. [Output Format](#output-format)
7. [CLI Reference](#cli-reference)
8. [Common Workflows](#common-workflows)
9. [Configuration](#configuration)
10. [Caching](#caching)
11. [Exit Codes](#exit-codes)
12. [Troubleshooting](#troubleshooting)
13. [Testing](#testing)
14. [Architecture Notes](#architecture-notes)
15. [Extending V4](#extending-v4)

---

## What V4 Does

For every `*_extracted.json` file under `--input-dir`, V4:

1. **Loads** the JSON and validates its shape (`extracted_items` key required).
2. **Mines concepts** — every `[!definition]` callout becomes one concept candidate. Optionally `[!key-claim]` callouts can also be mined (`--include-key-claims`). Titles are normalised (parentheticals like `(Sweller, 1988)` and ` — qualifier` suffixes stripped) and deduped case-insensitively (definition wins over key-claim).
3. **Bundles context** per concept:
   - the source `[!definition]` body
   - up to 8 same-report supporting callouts (`person`, `example`, `open-question`, `tension`, `far-transfer`, `claude-insight`, `original-synthesis`, `warning`, `principle-point`, `evidence`, `key-distinction`, `section-summary`, `key-claim`) that mention the concept by substring
   - the report's frontmatter (domain, aliases, related/see-also/broader/narrower wiki-links)
4. **Calls Ollama** with a strict structured-JSON prompt (`SYSTEM_PROMPT` + `USER_PROMPT_TEMPLATE`), validated by a pydantic `EnrichmentResponse` schema with ten required fields including a `worthy` boolean and `worthy_reason` string.
5. **Worthiness gate (anti-bloat).** The LLM judges whether the concept actually warrants its own atomic permanent note against four criteria: (a) named/teachable concept with explanatory power beyond one example, (b) re-usable across multiple contexts, (c) enough supplied substance to write a real definition + paragraph, (d) not redundant with a more canonical concept already in `related_links`/`aliases`. Unworthy candidates are **skipped — no file written** — and the rejection reason is printed in the run summary. This is the primary defense against bloating the vault with low-signal wiki-link concepts. Disable with `--no-gate`.
6. **Renders** the response as a complete Obsidian permanent note — full YAML frontmatter + `# Title` + mandatory `> [!definition]` callout + Core Explanation / Practical Implications / Key Distinctions / Key Figures / Open Threads / Connections.
7. **Writes atomically** (`.tmp → replace`) into `--output-dir` (default: `999-report-organizing/_permanent-notes/v4-llm-condensed/`) using a kebab-case filename derived from the concept title.

Filename collisions are handled by `--mode`:

| Mode        | Behaviour                                                           |
|-------------|---------------------------------------------------------------------|
| `skip`      | (default) Skip if file exists — safe re-runs.                       |
| `overwrite` | Replace any existing file unconditionally.                          |
| `merge`     | Skip only when the existing note's `status:` is one of `enriched`, `evergreen`, `budding`. Otherwise overwrite. |

---

## How V4 Differs from V3

| Aspect            | V3 `enrich_stubs.py`                                  | V4 `pipeline_v4.py`                                                |
|-------------------|-------------------------------------------------------|--------------------------------------------------------------------|
| **Input**         | Existing `.md` stubs already in the vault             | `_extracted.json` files from the extractor                         |
| **Concept source**| One concept per existing stub file                    | One concept per `[!definition]` callout in the report              |
| **Generates**     | Enriches an existing note in-place                    | Generates a brand-new permanent note from scratch                  |
| **Granularity**   | Whatever the stub generator produced                  | Atomic — one note per definition (Zettelkasten-aligned)            |
| **Output dir**    | Same dir as input (in-place)                          | Separate `v4-llm-condensed/` dir until quality is verified         |
| **Context sources** | Stub frontmatter + stub body + back-references     | Definition body + 8 supporting callouts + report frontmatter       |
| **Best for**      | Rescuing existing thin stubs                          | Generating new notes directly from freshly-extracted reports       |

V4 **reuses** V3's library code (`lib/llm_client.py`, `lib/markdown.py`, `config_v3.py`) via `sys.path` injection — **no V3 files are modified**.

---

## Prerequisites

### System

- **OS:** Windows 10/11 (paths use Windows separators in examples; works on macOS/Linux with adjusted paths)
- **Python:** 3.10 or newer
- **Ollama:** running locally on `http://127.0.0.1:11434` (V3's `config_v3.OLLAMA_URL` default)
- **GPU:** RTX 4090 recommended for the default 7B Q5 model; smaller GPUs work with smaller models via `--model`

### Python packages

All already required by V3 — V4 adds no new dependencies:

```powershell
pip install requests pydantic rich
```

> If `pydantic` is missing, V4 still runs (schema validation is gracefully disabled, with a warning).
> If `rich` is missing, V4 still runs (progress bar / coloured summary fall back to plain text).

### Model

```powershell
ollama pull qwen2.5:7b-instruct-q5_K_M
```

To use a different model:

```powershell
python pipeline_v4.py --model llama3.1:8b-instruct-q5_K_M
```

### V3 must be present

V4 imports from `../report-extraction-to-permanent-notes-building-v3/`:

- `config_v3.py` (constants: `VAULT_ROOT`, `OLLAMA_URL`, `LLM_MODEL_SYNTHESIZE`, `LLM_CACHE_DIR`, …)
- `lib/llm_client.py` (`OllamaClient`, exception classes)
- `lib/markdown.py` (`callout`, `join_wikilinks`, `safe_filename`, `to_kebab`)

If V3 has been moved or renamed, edit the `_V3_DIR` constant near the top of `pipeline_v4.py`.

---

## Repository Layout

```
99-scripts/
├── report-extraction-to-permanent-notes-building-v3/    ← READ-ONLY for V4
│   ├── config_v3.py
│   └── lib/
│       ├── llm_client.py
│       └── markdown.py
└── report-extraction-to-permanent-notes-building-v4/    ← THIS PROJECT
    ├── README.md                                        ← you are here
    ├── pipeline_v4.py                                   ← the script
    └── test_pipeline_v4.py                              ← pytest companion (32 tests)

999-report-organizing/
├── _extractor-output/                                   ← INPUT (default)
│   └── 2026-04-21-__pur3v4d3r-house-voice-reports/
│       └── *_extracted.json
└── _permanent-notes/
    └── v4-llm-condensed/                                ← OUTPUT (default)
        └── <kebab-title>.md
```

---

## Input Format

V4 expects each input file to be a JSON object produced by `pkb_extractor.py` with at minimum:

```jsonc
{
  "document_metadata": {
    "frontmatter": {
      "title": "...",
      "aliases": ["...", "..."],
      "primary_domain": "Cognitive Psychology",
      "secondary_domains": ["Educational Psychology"],
      "confidence": "high",
      "related": ["[[concept-a]]", "[[concept-b]]"],
      "see-also": ["[[concept-c]]"],
      "broader": [], "narrower": [], "prerequisites": []
    }
  },
  "extracted_items": {
    "callouts": [
      { "type": "definition",  "title": "Cognitive Load", "body": "..." },
      { "type": "key-claim",   "title": "...",            "body": "..." },
      { "type": "person",      "title": "John Sweller",   "body": "..." },
      { "type": "example",     "title": "Worked Example", "body": "..." },
      { "type": "open-question","title": "...",           "body": "..." }
    ]
  },
  "knowledge_graph": {
    "unique_wiki_link_targets": ["working-memory", "schema-theory", "..."]
  }
}
```

Filename convention: `<report-stem>_extracted.json`. The `_extracted` suffix is stripped to derive the source-report stem used in the `source-reports:` frontmatter field of every generated note.

---

## Output Format

Each generated `.md` file is a fully-formed Obsidian permanent note:

```markdown
---
title: "Cognitive Load"
aliases:
  - "Cognitive Load"
  - "CLT"
type: permanent-note
status: enriched
confidence: high

tags:
  - permanent-note
  - v4-llm-condensed
  - cognitive-psychology

domain: cognitive-psychology
subdomains:
  - educational-psychology

created: 2026-04-23
updated: 2026-04-23

source-type: report-extraction
source-reports:
  - "sample-report-2026-04-21"
evidence-quality: high
extraction-method: "pkb-extractor-v1 → pipeline-v4-condenser"

complexity-level: advanced-practitioner
depth-level: condensed

related:
  - "[[Working Memory]]"
  - "[[Schema Theory]]"
see-also:
  - "[[]]"
broader:
  - "[[]]"
narrower:
  - "[[]]"

review-frequency: quarterly
mastery-stage: budding
importance: medium

provenance:
  pipeline-version: "v4.0.0"
  prompt-contract: "v4-condense-v1"
---

# Cognitive Load

> [!definition] **Cognitive Load**
> The total amount of mental effort being deployed in working memory at a given moment…

## Core Explanation

…paragraph 1…

…paragraph 2…

## Practical Implications

> [!example] **Application 1**
> …

## Key Distinctions

> [!warning] **Distinction**
> …

## Key Figures

- John Sweller — originator of cognitive load theory

## Open Threads

> [!open-question] **Question**
> …

## Connections & Context

**Related:** [[Working Memory]] · [[Schema Theory]] · [[Chunking]]

**Source:** [[sample-report-2026-04-21]]
```

Optional sections (`Practical Implications`, `Key Distinctions`, `Key Figures`, `Open Threads`) are **omitted entirely** when the LLM returns empty arrays — no empty headings.

---

## CLI Reference

```text
usage: pipeline_v4 [-h] [--version] [--input-dir INPUT_DIR]
                   [--output-dir OUTPUT_DIR] [--report REPORT] [--limit LIMIT]
                   [--include-key-claims]
                   [--mode {skip,overwrite,merge}] [-n] [--bypass-cache]
                   [--model MODEL] [--strict] [-v] [-q]
```

| Flag                    | Type   | Default                                | Purpose                                                                                  |
|-------------------------|--------|----------------------------------------|------------------------------------------------------------------------------------------|
| `--input-dir PATH`      | path   | `999-report-organizing/_extractor-output` | Recursively scanned for `*_extracted.json`.                                              |
| `--output-dir PATH`     | path   | `999-report-organizing/_permanent-notes/v4-llm-condensed` | Destination for generated notes.                                                         |
| `--report SUBSTRING`    | str    | (none)                                 | Case-insensitive substring filter on JSON filename stems.                                |
| `--limit N`             | int    | (none)                                 | Process only the first N concept candidates total (across all matched JSONs).           |
| `--include-key-claims`  | flag   | off                                    | Also mine `[!key-claim]` callouts as concepts (in addition to `[!definition]`).         |
| `--mode {skip,overwrite,merge}` | choice | `skip`                         | Filename collision policy.                                                                |
| `-n`, `--dry-run`       | flag   | off                                    | Run LLM calls (and cache them) but write **no** files.                                   |
| `--bypass-cache`        | flag   | off                                    | Force live LLM calls; ignore cached responses.                                           |
| `--model MODEL`         | str    | `qwen2.5:7b-instruct-q5_K_M`           | Ollama model identifier.                                                                  |
| `--strict`              | flag   | off                                    | Exit code 5 if any concept fails to convert.                                             |
| `--no-gate`             | flag   | off                                    | Disable the LLM worthiness judgment — force a note for every concept.                   |
| `-v`, `--verbose`       | count  | 0                                      | `-v` = INFO, `-vv` = DEBUG.                                                              |
| `-q`, `--quiet`         | flag   | off                                    | Suppress non-error output.                                                               |
| `--version`             | action |                                        | Print `pipeline_v4 1.0.0` and exit.                                                       |
| `-h`, `--help`          | action |                                        | Show full help with examples.                                                             |

---

## Common Workflows

### A. Preview before committing (recommended first run)

```powershell
python pipeline_v4.py --dry-run --limit 5 -v
```

What this does: discovers JSONs, mines up to 5 concepts, calls the LLM (cached afterwards), prints a Rich summary table — but writes no files. Inspect the cache or repeat without `--dry-run` to materialise the same outputs from cache (instant, no GPU work).

### B. Process one specific report

```powershell
python pipeline_v4.py --report self-determination-theory -v
```

The substring matches anywhere in the filename stem — `self-determination`, `sdt`, etc. all work.

### C. Process one specific batch directory

```powershell
python pipeline_v4.py `
  --input-dir "D:\10_pur3v4d3r's-vault\999-report-organizing\_extractor-output\2026-04-21-__pur3v4d3r-house-voice-reports" `
  -v
```

### D. Re-run with key-claims included

If a report's `[!definition]` callouts are sparse, broaden the concept pool:

```powershell
python pipeline_v4.py --include-key-claims -v
```

### E. Force regeneration of existing notes

```powershell
python pipeline_v4.py --mode overwrite --bypass-cache -v
```

`--mode overwrite` ignores existing files; `--bypass-cache` ignores cached LLM responses (useful after editing the prompt or bumping `PROMPT_CONTRACT_VERSION`).

### F. Smart merge — keep already-curated notes, regenerate the rest

```powershell
python pipeline_v4.py --mode merge -v
```

Files whose `status:` is `enriched`, `evergreen`, or `budding` are skipped (you've already invested in them); everything else is regenerated.

### G. Strict CI-style run

```powershell
python pipeline_v4.py --strict -v
```

Exits non-zero on the first conversion failure — useful for nightly batch jobs that should page you on regressions.

### H. End-to-end fresh run on a brand-new batch

```powershell
# 1. Run the extractor (V3 / V2) to populate _extractor-output/<new-batch>/
# 2. Preview
python pipeline_v4.py --input-dir "...\_extractor-output\<new-batch>" --dry-run --limit 3 -v

# 3. Spot-check the cached LLM output by re-running without dry-run + --limit 3
python pipeline_v4.py --input-dir "...\_extractor-output\<new-batch>" --limit 3 -v

# 4. Inspect the 3 generated notes manually. If happy, full run:
python pipeline_v4.py --input-dir "...\_extractor-output\<new-batch>" -v
```

---

## Configuration

V4 reads constants from V3's `config_v3.py`:

| Constant                       | Used for                                                |
|--------------------------------|---------------------------------------------------------|
| `VAULT_ROOT`                   | Default input/output paths                              |
| `OLLAMA_URL`                   | Ollama API endpoint (default `http://127.0.0.1:11434`) |
| `LLM_MODEL_SYNTHESIZE`         | Default model identifier                                |
| `LLM_CACHE_DIR`                | Cache directory for LLM responses                       |
| `LLM_REQUEST_TIMEOUT_S`        | Per-request timeout (default 120s)                      |
| `LLM_MAX_RETRIES`              | Retries on transient failures (default 3)               |

V4-specific constants live at the top of `pipeline_v4.py`:

| Constant                     | Default                                              | Purpose                                                  |
|------------------------------|------------------------------------------------------|----------------------------------------------------------|
| `PROMPT_CONTRACT_VERSION`    | `"v4-condense-v1"`                                   | Bump to invalidate the LLM cache after prompt edits.     |
| `DEFAULT_OUTPUT_DIR`         | `…/_permanent-notes/v4-llm-condensed`                | Destination for generated notes.                         |
| `DEFAULT_INPUT_DIR`          | `…/_extractor-output`                                | Default scan root.                                       |
| `MAX_SUPPORT_CALLOUTS`       | `8`                                                  | Max same-report supporting callouts bundled per concept. |
| `MAX_SUPPORT_BODY_CHARS`     | `600`                                                | Max chars of each support callout's body.                |
| `MIN_TITLE_LEN` / `MAX_TITLE_LEN` | `3` / `80`                                       | Concept-title sanity gates.                              |
| `ENRICHED_STATUSES`          | `{enriched, evergreen, budding}`                     | Statuses that block `--mode merge` from overwriting.     |

---

## Caching

LLM responses are cached on disk by V3's `OllamaClient` under `config_v3.LLM_CACHE_DIR` (typically `D:/v3-pipeline-output/llm-cache/`).

Cache key includes:

- `PROMPT_CONTRACT_VERSION` — bump to invalidate everything
- model identifier
- concept title (lowercase)
- source report stem
- first 300 chars of the source definition body

Implications:

- **Re-runs are free** if nothing relevant changed.
- **Editing the prompt** in `SYSTEM_PROMPT` / `USER_PROMPT_TEMPLATE` does *not* invalidate the cache automatically — bump `PROMPT_CONTRACT_VERSION` (e.g. to `"v4-condense-v2"`) when you change prompt semantics.
- **`--bypass-cache`** forces live calls without invalidating stored entries.

---

## Exit Codes

| Code | Meaning                                                  |
|------|----------------------------------------------------------|
| `0`  | Success                                                  |
| `1`  | Uncaught exception (bug — please file)                   |
| `2`  | Bad CLI arguments / `--input-dir` does not exist          |
| `4`  | No `*_extracted.json` files matched, or no concepts mined |
| `5`  | One or more conversions failed (only when `--strict`)    |
| `6`  | Ollama unreachable (server down or wrong URL)            |
| `130`| Interrupted by user (Ctrl+C)                             |

---

## Troubleshooting

| Symptom                                         | Likely cause / fix                                                                                              |
|-------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Exit `6 — Ollama unreachable`                   | `ollama serve` not running. Start it: `ollama serve` (or restart the desktop app).                              |
| Exit `4 — No *_extracted.json files matched`    | Wrong `--input-dir` or `--report` substring. Check the path and try without `--report`.                          |
| Exit `4 — no concept candidates mined`          | The reports lack `[!definition]` callouts. Try `--include-key-claims`.                                          |
| `pydantic not installed — schema validation disabled` | Install pydantic: `pip install pydantic`. Schema validation makes failures explicit instead of silent.       |
| `StructuredOutputError` failures in summary     | The model returned non-JSON or missing `definition` field. Try a stronger model: `--model qwen2.5:14b-instruct`. |
| LLM output looks copy-pasted from the source    | Prompt is too lenient. Bump `PROMPT_CONTRACT_VERSION` and tighten the "must paraphrase" rule in `USER_PROMPT_TEMPLATE`. |
| Generated notes overwrite my manually-edited ones | Default mode is `skip` — this shouldn't happen. If you used `--mode overwrite`, switch to `--mode merge` and set the curated note's `status: enriched`. |
| Concept titles include `(Author, Year)` clutter | Already handled by `_clean_title()`. If a new title pattern slips through, add a regex to `_TITLE_PAREN_RE` / `_TITLE_DASH_RE`. |
| `from lib.llm_client import …` fails            | V3 directory has been moved or renamed. Edit `_V3_DIR` in `pipeline_v4.py` to point at the new location.        |
| Filename collisions across reports              | Two reports both define `Cognitive Load` → second run hits the existing file → behaves per `--mode`. Use `--mode merge` to add to the curated copy manually. |

---

## Testing

```powershell
# Activate venv
& "d:\10_pur3v4d3r's-vault\.venv\Scripts\Activate.ps1"

cd "d:\10_pur3v4d3r's-vault\99-scripts\report-extraction-to-permanent-notes-building-v4"

# Run all tests
python -m pytest test_pipeline_v4.py -v

# With coverage
python -m pytest test_pipeline_v4.py --cov=pipeline_v4 --cov-report=term-missing
```

The test suite covers:

- title cleaning (parentheticals, em-dashes, wiki-link brackets)
- title sanity gates (length, sentence-rejection)
- concept mining (definitions only, with key-claims, dedupe)
- bundle construction (support gathering, frontmatter integration, kebab filenames)
- rendering (definition callout present, optional sections omitted, frontmatter shape)
- I/O (atomic writes, JSON loading, dir discovery, status-field parsing)
- collision modes (skip / overwrite / merge interactions with `ENRICHED_STATUSES`)
- CLI integration (help text, missing input dir, no-JSONs, end-to-end dry-run with mocked Ollama)

Tests **do not** require Ollama or pydantic to be running — the LLM client is mocked.

---

## Architecture Notes

### Flow (per concept)

```
JSON file
   │
   ├── load_payload()                         → dict
   ├── mine_concepts()                        → [(callout_type, callout), ...]
   │      └── _clean_title() + _is_usable_title()
   │
   ├── build_bundles()                        → [ConceptBundle, ...]
   │      ├── _gather_support()               → tuple[SourceCallout, ...]
   │      └── _related_links_from_payload()   → tuple[str, ...]
   │
   ├── condense_concept(bundle, client)       → (EnrichmentResponse, cached)
   │      └── OllamaClient.chat_json(SYSTEM_PROMPT, USER_PROMPT_TEMPLATE, schema=EnrichmentResponse)
   │
   ├── render_note()                          → str
   │      ├── render_frontmatter_block()      → YAML
   │      └── render_body()                   → markdown sections
   │
   ├── resolve_destination(mode)              → (Path, skip_reason | None)
   └── write_atomic()                         → .tmp → replace
```

### Why per-definition granularity?

The extractor's `[!definition]` callouts already mark concept boundaries — V4 doesn't need to *discover* concepts, just *condense* the surrounding evidence into a structured note. This:

- Aligns with the Zettelkasten principle of one concept per atomic note
- Avoids the LLM having to decide what's a concept (which it does poorly)
- Keeps each LLM call small (~2–4K tokens) and fast (~3–5s on RTX 4090)
- Makes outputs deterministic at the concept-extraction layer (only the LLM call is non-deterministic, and it's cached)

### Alternative architecture preserved

A multi-stage pipeline (`extract → normalize → match → render`, modelled after V3's stage system) was considered and pruned as over-engineered for the current scope. Defer to V4.1 if the single-pass condenser proves insufficient.

### Why no V3 modifications?

V3 is a stable, working pipeline with 1200+ existing stub outputs. V4 must not destabilise it. By importing V3 modules read-only via `sys.path` injection, V4 can evolve independently and V3 remains a known-good fallback.

---

## Extending V4

### Add a new supporting callout type

Edit `SUPPORT_CALLOUT_TYPES` in `pipeline_v4.py`:

```python
SUPPORT_CALLOUT_TYPES: frozenset[str] = frozenset({
    "definition", "key-claim", "person", "example", "open-question",
    "tension", "far-transfer", "claude-insight", "original-synthesis",
    "warning", "principle-point", "evidence", "key-distinction",
    "section-summary",
    "your-new-callout-type",   # ← add here
})
```

### Change the prompt

Edit `SYSTEM_PROMPT` and/or `USER_PROMPT_TEMPLATE`. **Then bump `PROMPT_CONTRACT_VERSION`** (e.g. `"v4-condense-v2"`) so the cache invalidates.

### Add a new frontmatter field

Edit `render_frontmatter_block()`. Keep additions backwards-compatible with the existing template at `_permanent-notes/permanent-note-pack/permanent-note-template.md` so generated notes round-trip cleanly through any vault tooling.

### Use a different model

```powershell
python pipeline_v4.py --model llama3.1:8b-instruct-q5_K_M
```

Or change the default by editing `LLM_MODEL_SYNTHESIZE` in V3's `config_v3.py` (affects V3 too).

### Support a different output schema

Edit `EnrichmentResponse` (pydantic class). Update `USER_PROMPT_TEMPLATE` to describe the new schema. Update `render_body()` to consume the new fields. Bump `PROMPT_CONTRACT_VERSION`. Update tests.

---

## Quick Reference Card

```text
╔══════════════════════════════════════════════════════════════════════════╗
║  V4 CHEATSHEET                                                           ║
╠══════════════════════════════════════════════════════════════════════════╣
║  Preview            python pipeline_v4.py --dry-run --limit 5 -v         ║
║  One report         python pipeline_v4.py --report <substring> -v        ║
║  One batch          python pipeline_v4.py --input-dir <path> -v          ║
║  Full run           python pipeline_v4.py -v                             ║
║  Replace existing   python pipeline_v4.py --mode overwrite -v            ║
║  Smart merge        python pipeline_v4.py --mode merge -v                ║
║  Broaden concepts   python pipeline_v4.py --include-key-claims -v        ║
║  Force regen        python pipeline_v4.py --bypass-cache -v              ║
║  CI mode            python pipeline_v4.py --strict -v                    ║
║                                                                          ║
║  Tests              python -m pytest test_pipeline_v4.py -v              ║
║  Help               python pipeline_v4.py --help                         ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

**Maintainer notes**

- Generated by Python Script Designer & Generator — Expert v1.0.0
- Pipeline contract version: `v4-condense-v1`
- Last verified: 2026-04-23 (32/32 tests passing)
