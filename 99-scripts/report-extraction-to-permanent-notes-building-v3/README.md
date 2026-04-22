# Pipeline v3 — Operational Reference

**Status:** Production (as of 2026-04-22)
**Last updated:** 2026-04-22

Three distinct workflows live here. Read the one you need:

| Workflow | Script | Purpose |
|----------|--------|---------|
| [Extract & Build](#1-extract--build-pipeline) | `pipeline_v3.py` | Reports → permanent notes (10-stage) |
| [Enrich Stubs](#2-stub-enrichment-pipeline) | `enrich_stubs.py` | Fill empty stubs via local LLM |
| [Merge Duplicates](#3-merge-duplicates-pipeline) | `merge_stubs.py` | Cluster + deduplicate stubs |

---

## Environment Setup

```bash
# From vault root — activate the shared venv
source .venv/Scripts/activate        # Windows Git Bash
# or
.venv\Scripts\activate               # Windows CMD/PowerShell

# Install v3 dependencies
pip install -r 99-scripts/report-extraction-to-permanent-notes-building-v3/requirements-v3.txt

# Verify Ollama is running (required for LLM steps)
curl -s http://localhost:11434/api/tags | python -m json.tool

# Verify CUDA (optional — embeddings run on CPU fine)
python -c "import torch; print('CUDA:', torch.cuda.is_available())"
```

All scripts must be run **from inside the v3 directory**:

```bash
cd "d:/10_pur3v4d3r's-vault/99-scripts/report-extraction-to-permanent-notes-building-v3"
python enrich_stubs.py --help
```

---

## Output location (external to vault)

All pipeline artefacts (run JSONs, embedding caches, LLM caches) are written **outside** the vault:

```
D:/v3-pipeline-output/
├── llm-cache/          # SHA-1 keyed JSON — never delete unless changing prompts
├── embeddings/         # .npz files for sentence-transformer vectors
└── runs/               # Per-run intermediate state files
```

> **Why external?** Pipeline JSONs grew to 90+ MB. Storing them inside the vault crashed
> Obsidian's metadata indexer. Set `V3_OUTPUT_DIR` env var to override the location.

```bash
V3_OUTPUT_DIR="D:/v3-experiments/test-run" python pipeline_v3.py --to-stage 6 --execute
```

---

## 1. Extract & Build Pipeline

**Script:** `pipeline_v3.py`
**Purpose:** Takes raw reports from `999-report-organizing/` and produces permanent notes.

### Stages

| Stage | Name | LLM? | Key Output |
|-------|------|-------|------------|
| 1 | extract | No | raw candidates JSON |
| 2 | validate | No | filtered candidates |
| 3 | consolidate | No | merged super-candidates |
| 4 | normalize | **Yes (opt-in)** | canonical names + definitions |
| 5 | match | Embeddings | matched vs. existing notes |
| 6 | render | No | permanent note files |
| 7 | stubs | No | stub .md files for unresolved concepts |
| 8 | resolve_links | No | updated wiki-links in reports |
| 9 | normalize_links | No | vault-wide link normalization |
| 10 | audit | No | resolution rate + quality gate |

### Common runs

```bash
# Dry run — stages 1–6, no files written
python pipeline_v3.py --to-stage 6

# Full pipeline, write files
python pipeline_v3.py --execute

# Up to stage 4 with LLM normalization (opt-in)
python pipeline_v3.py --to-stage 4 --llm-normalize --execute

# Single-stage re-run (e.g. re-render after editing templates)
python pipeline_v3.py --from-stage 6 --to-stage 6 --execute

# Override output dir for an experiment
V3_OUTPUT_DIR="D:/experiment-01" python pipeline_v3.py --execute
```

### Permanent notes output location

```
999-report-organizing/_permanent-notes/v3-pipeline-permanent-notes/   ← rendered notes
999-report-organizing/_permanent-notes/                                ← audit reports
```

---

## 2. Stub Enrichment Pipeline

**Script:** `enrich_stubs.py`
**Purpose:** Takes stub notes (empty or placeholder content) and calls Qwen2.5-7B to fill:
- `[!definition]` callout — **mandatory, always filled**
- Core Explanation (3–5 paragraphs)
- Practical Implications (2–3 items)
- Key Figures, Open Threads, Connections

**Stubs detected:** 991 total as of 2026-04-22
- 985 in `v3-pipeline-permanent-notes/` (kebab-case titles, `mastery-stage: seedling`)
- 6 in `03-notes/01_permanent-notes/` (older format, `maturity: seedling`, empty body)

### Quick reference

```bash
# 1. Preview — LLM runs + caches, zero files written, prints first stub output
python enrich_stubs.py --dry-run --limit 3

# 2. Safe batch — write to output dir, original stubs untouched
python enrich_stubs.py --limit 50 --output-dir D:/enrichment-preview

# 3. In-place batch — enrich 50 stubs directly (recommended after previewing)
python enrich_stubs.py --limit 50

# 4. Full run — all 991 stubs
python enrich_stubs.py

# 5. Strict mode — exit non-zero if any stub fails (good for CI)
python enrich_stubs.py --strict --limit 100
```

### All options

```
--input-dir PATH     Scan directory (repeatable). Default: both stub dirs.
--output-dir PATH    Write enriched notes here instead of in-place.
-n, --dry-run        Run LLM calls (cached) but write no files.
--limit N            Process only first N stubs (0 = no limit).
--bypass-cache       Force fresh LLM calls, ignore cache.
--model MODEL        Ollama model (default: qwen2.5:7b-instruct-q5_K_M).
--ollama-url URL     Ollama base URL (default: http://localhost:11434).
--cache-dir PATH     LLM response cache dir (default: D:/v3-pipeline-output/llm-cache).
--strict             Exit code 5 if any enrichment fails.
-v / -q              Verbose / quiet.
```

### Batch strategy (processing all 991 stubs)

The LLM processes one stub at a time (~10–30 sec each at 7B). All responses are cached,
so interrupted runs resume instantly from where they stopped.

```bash
# Recommended: batches of 100, preview first batch before committing
python enrich_stubs.py --dry-run --limit 5          # inspect quality
python enrich_stubs.py --limit 100                  # batch 1
python enrich_stubs.py --limit 200                  # batch 2 (skips already-enriched)
python enrich_stubs.py                              # finish remainder
```

Stubs already enriched (`status: enriched`, `maturity: budding`) are **skipped automatically**
on repeat runs — safe to re-run the same command.

### What changes in the note after enrichment

**Frontmatter fields updated:**

| Field | Before | After |
|-------|--------|-------|
| `status` | `stub` / `seedling` / `active` | `enriched` |
| `maturity` | `seedling` | `budding` |
| `mastery-stage` | `seedling` | `budding` |
| `domain` | `other` / `uncategorized` | corrected (if LLM confident) |
| `updated` | original date | today |
| `provenance.enrichment-method` | — | `enrich_stubs-v1` |
| `provenance.enrichment-model` | — | `qwen2.5:7b-instruct-q5_K_M` |

**Body sections added:**
- `> [!definition]` — filled with 1–2 sentence definition
- `## Core Explanation` — 3–5 `[!analytical-insight]` callouts
- `## Practical Implications` — `[!example]` callouts
- `## Key Figures` — `[!person]` callouts (if relevant)
- `## Open Threads` — `[!open-question]` callouts (if relevant)
- `## Connections` — `**Related:** [[wiki-links]]` + Dataview backlink query

### Troubleshooting enrichment

**Ollama not running:**
```bash
# Start Ollama (keep this terminal open)
ollama serve
# Verify model is available
ollama list | grep qwen2.5
```

**Model not found:**
```bash
ollama pull qwen2.5:7b-instruct-q5_K_M
```

**Low quality definitions (hallucination, wrong domain):**
```bash
# Bypass cache and try again — model responses vary slightly even at temp=0
python enrich_stubs.py --bypass-cache --limit 5
# Or try a larger model
python enrich_stubs.py --model qwen2.5:14b-instruct --limit 5
```

**Resume after interruption:**
```bash
# Just re-run the same command — enriched notes are skipped, cache is preserved
python enrich_stubs.py --limit 100
```

**Inspect cache entries:**
```bash
ls D:/v3-pipeline-output/llm-cache/ | wc -l   # count cached calls
```

**Reset enrichment for a single note** (manual): open the note, set `status: stub` and
`maturity: seedling`, delete the body below `# Title`, save. The script will re-process it.

---

## 3. Merge Duplicates Pipeline

**Script:** `merge_stubs.py`
**Purpose:** Find semantically duplicate stubs (e.g. "Cognitive Load" vs "cognitive-load")
and merge them. Run this **before** enrichment for maximum efficiency.

### Phases

| Phase | Flag | What it does |
|-------|------|-------------|
| 1 | `--scan` | Parse all stubs, detect exact-name duplicates |
| 2 | `--cluster` | Embed titles + cosine similarity clustering |
| 3 | `--verify` | LLM confirms which clusters are true duplicates |
| 4 | `--review` | Interactive TUI to accept/reject merge decisions |
| 5 | `--merge` | Execute accepted merges + rewrite vault wiki-links |

```bash
# Full pipeline (all phases in sequence)
python merge_stubs.py --all

# Dry run — plan merges without writing
python merge_stubs.py --all --dry-run

# Individual phases
python merge_stubs.py --scan
python merge_stubs.py --cluster
python merge_stubs.py --verify
python merge_stubs.py --review     # interactive TUI
python merge_stubs.py --merge
```

---

## Directory Layout

```
report-extraction-to-permanent-notes-building-v3/
│
├── README.md                   ← this file
├── pipeline_v3.py              ← master orchestrator (stages 1-10)
├── enrich_stubs.py             ← stub enrichment via Ollama (standalone)
├── merge_stubs.py              ← duplicate detection + merge (standalone)
├── config_v3.py                ← all paths, thresholds, model IDs
├── config_merge.py             ← merge pipeline config
├── phase4_gate.py              ← quality gate for stage 10
├── requirements-v3.txt         ← pinned dependencies
│
├── stages/                     ← pipeline stage modules
│   ├── s1_extract.py
│   ├── s2_validate.py
│   ├── s3_consolidate.py
│   ├── s4_normalize.py         ← LLM concept normalization (opt-in)
│   ├── s5_match.py             ← bge-small embeddings + hybrid scorer
│   ├── s6_render.py            ← Jinja2 → permanent notes
│   ├── s7_stubs.py             ← stub generation for unresolved concepts
│   ├── s8_resolve_links.py
│   ├── s9_normalize_links.py
│   └── s10_audit.py
│
├── lib/                        ← shared utilities (importable by all scripts)
│   ├── candidate.py            ← Candidate dataclass (core data model)
│   ├── embeddings.py           ← EmbeddingStore (.npz backed)
│   ├── frontmatter.py          ← YAML parse/render (ruamel.yaml)
│   ├── link_validator.py       ← garbage link detection patterns
│   ├── llm_client.py           ← OllamaClient (cache + retry + pydantic)
│   ├── markdown.py             ← callout(), join_wikilinks(), safe_filename()
│   ├── ollama_embeddings.py    ← OllamaEmbedder (nomic-embed-text)
│   ├── parallel.py             ← ProcessPoolExecutor helpers
│   ├── state.py                ← pipeline state JSON I/O
│   └── ui.py                   ← Rich console helpers
│
├── templates/
│   ├── permanent_note.md.j2    ← full note template (conditional sections)
│   └── stub.md.j2              ← minimal stub placeholder template
│
└── tests/                      ← pytest suite
    └── ...
```

---

## Key Configuration (`config_v3.py`)

```python
VAULT_ROOT       = d:\10_pur3v4d3r's-vault
REPORTS_ROOT     = VAULT_ROOT / "999-report-organizing"
PERMANENT_NOTES_DIR = REPORTS_ROOT / "_permanent-notes" / "_permanent-notes"

V3_OUTPUT_DIR    = D:/v3-pipeline-output          # override with V3_OUTPUT_DIR env var
LLM_CACHE_DIR    = V3_OUTPUT_DIR / "llm-cache"

OLLAMA_URL       = "http://localhost:11434"
LLM_MODEL_SYNTHESIZE = "qwen2.5:7b-instruct-q5_K_M"
LLM_MODEL_NORMALIZE  = "qwen2.5:7b-instruct-q5_K_M"
EMBED_MODEL_ID   = "BAAI/bge-small-en-v1.5"

AUTO_MATCH_THRESHOLD   = 0.92   # auto-merge existing note
REVIEW_QUEUE_THRESHOLD = 0.78   # flag for human review
```

---

## Models Required

| Model | Used by | Pull command |
|-------|---------|-------------|
| `qwen2.5:7b-instruct-q5_K_M` | enrich_stubs, s4_normalize, m3_verify | `ollama pull qwen2.5:7b-instruct-q5_K_M` |
| `nomic-embed-text` | merge_stubs (clustering) | `ollama pull nomic-embed-text` |
| `BAAI/bge-small-en-v1.5` | s5_match (sentence-transformers) | auto-downloaded on first use |

---

## Exit Codes

All scripts share the same exit code convention:

| Code | Meaning |
|------|---------|
| 0 | Success |
| 1 | Uncaught error |
| 2 | Bad arguments / missing directory |
| 4 | No input found (no stubs, no candidates) |
| 5 | Failures occurred (`--strict` mode only) |
| 6 | Ollama unreachable |
| 130 | Interrupted (Ctrl+C) — safe, partial writes are atomic |
