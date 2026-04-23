# V5 — Merge-Aware Permanent-Note Pipeline

V5 sits on top of V4 and adds **merge-aware routing**. When you re-run the
pipeline on the same source material, V5 reconciles new content into the
existing permanent note instead of skipping or duplicating it.

---

## What V5 Does

For every concept bundle mined from `*_extracted.json`:

1. **Index** the output directory once (non-recursive — output dir only).
2. **Route** each bundle through a tiered matcher:
   - Tier 1 — exact slug
   - Tier 2 — alias hit
   - Tier 3 — normalized-title hit
   - Tier 4 — fuzzy match (default threshold `0.92`)
3. **Hit** → call the LLM with the **merge prompt** (preserves existing
   wisdom, surfaces tensions, only promotes status `stub/seedling → enriched`).
   Backs up the existing note as `<file>.md.bak.<YYYYMMDD-HHMMSS>` before
   atomic write.
4. **Miss** → fall through to V4's `condense_concept` + `render_note` to
   create a brand-new permanent note.

Reconciliation is **on by default**. Pass `--no-reconcile` to fall back to
pure-V4 generate-only behavior.

---

## Installation

No extra installation. V5 reuses V3's and V4's existing dependencies.

Required Python: `>= 3.10`

Optional Python packages (already used by V3/V4):

- `pydantic` — schema validation for LLM responses (graceful fallback
  when missing)
- `rich` — progress bar (silent fallback when missing)

Required runtime services:

- **Ollama** at `http://127.0.0.1:11434`
- Model: `qwen2.5:7b-instruct-q5_K_M` (override with `--model`)

---

## Basic Usage

```powershell
# Reconcile one report into existing notes (real run)
python pipeline_v5.py --report self-determination-theory

# Preview routing + merges without writing
python pipeline_v5.py --report self-determination-theory --dry-run

# Disable V5 and behave like V4 (skip on collision, no merge)
python pipeline_v5.py --no-reconcile --report metacognition

# Tighter fuzzy threshold + override status protection
python pipeline_v5.py --report sdt --match-threshold 0.95 --force-merge

# Audit every routing decision to a JSON file
python pipeline_v5.py --report-merges runs/2026-04-23-merge-log.json
```

---

## Common Modes

| Flag                       | Effect                                                                |
|----------------------------|-----------------------------------------------------------------------|
| `--reconcile` (default)    | V5 routing on. Hits → merge; misses → V4 generate.                    |
| `--no-reconcile`           | Disable routing. Pure V4 generate-only.                               |
| `--dry-run` / `-n`         | LLM runs (cached) but no file writes, no backups.                     |
| `--match-threshold 0.92`   | Fuzzy threshold. Lower = more aggressive matches (risk of false hits).|
| `--protect-statuses S,T,…` | Statuses that BLOCK merge. Default `evergreen,budding`.               |
| `--force-merge`            | Override `--protect-statuses`. Merge into anything.                   |
| `--no-backup`              | Skip the `.bak.<timestamp>` sibling. Use with care; emits a warning.  |
| `--report-merges PATH`     | Write a JSON audit log of every routing decision.                     |
| `--bypass-cache`           | Force live LLM calls; ignore the V3 LLM cache.                        |
| `--report STR`             | Substring filter on JSON filename stems.                              |
| `--limit N`                | Process at most N concept candidates total.                           |
| `--include-key-claims`     | Also mine `[!key-claim]` callouts (default: definitions only).        |
| `--strict`                 | Exit non-zero on any failure.                                         |
| `-v` / `-vv`               | Increase logging verbosity.                                           |
| `-q`                       | Quiet mode.                                                           |

---

## Status Promotion Lattice

V5 only ever promotes status; **demotion is impossible**.

```
stub  →  seedling  →  enriched  →  budding  →  evergreen
                    ↑
        Only promotion permitted by V5
```

The LLM may suggest `status_recommendation: "promote_to_enriched"`. V5
honors it only if the existing status rank is below `enriched`. Anything
already at `budding` or `evergreen` stays put. (Operator-managed graduation
to `budding` / `evergreen` happens manually.)

---

## Backup Policy

Every merge creates `<original>.md.bak.<YYYYMMDD-HHMMSS>` as a sibling
file **before** the atomic write of the merged note. The backup is a byte-
for-byte copy of the original.

`--no-backup` opts out and emits a final-summary warning.

To restore a note from a backup:

```powershell
Move-Item -Force "<note>.md.bak.20260423-103005" "<note>.md"
```

---

## Exit Codes

| Code | Meaning                                                           |
|------|-------------------------------------------------------------------|
| 0    | Success                                                           |
| 1    | Uncaught error                                                    |
| 2    | Input directory not found                                         |
| 4    | No `*_extracted.json` files found / no concept candidates mined   |
| 5    | `--strict` and at least one merge or generation failed            |
| 6    | Ollama unreachable                                                |
| 7    | Output-directory index build failed                               |
| 130  | Interrupted by user (Ctrl+C)                                      |

---

## Cache Isolation

V5's merge prompt uses its own contract version key
(`PROMPT_CONTRACT_VERSION = "v5-merge-v1"`). Merge cache entries do NOT
collide with V4's condense cache. Both share the same on-disk cache
directory (`config_v3.LLM_CACHE_DIR` → `D:\v3-pipeline-output\llm-cache\`).

---

## Architecture

```
v5/
├── pipeline_v5.py            ← CLI orchestrator
├── v5lib/
│   ├── __init__.py
│   ├── output_index.py       ← Non-recursive output-dir index
│   ├── matcher.py            ← Tiered slug/alias/title/fuzzy matching
│   ├── merge_prompt.py       ← LLM contract + Pydantic schema
│   └── merger.py             ← One-merge orchestrator (LLM → render → backup → write)
└── tests/
    ├── conftest.py
    ├── test_output_index.py
    ├── test_matcher.py
    ├── test_merger.py
    └── test_pipeline_v5.py
```

The package is named `v5lib` (not `lib`) to avoid colliding with V3's
top-level `lib` package, which V5 also imports for `OllamaClient`,
`config_v3`, and a few helpers.

---

## Running the Tests

```powershell
cd 99-scripts/report-extraction-to-permanent-notes-building-v5
python -m pytest tests/ -v
```

44 tests cover:

- Title normalization (parametrized)
- Frontmatter parsing (inline + block + missing + malformed)
- `OutputIndex.build` (top-level only, missing dir, unreadable files)
- All four matcher tiers + below-threshold + ambiguous-match
- `harvest_wikilinks` (dedup + order preservation)
- Status-promotion lattice (parametrized, including demotion-rejection)
- `make_backup` timestamp format
- Full merger flow with mocked LLM:
  - Protected status → skip
  - `--force-merge` → override protection
  - Backup creation + atomic write
  - `--dry-run` writes nothing
  - Status promotion seedling → enriched
  - LLM error surfaces in `MergeOutcome.error`
- `pipeline_v5` CLI parser surface + `route_bundle` hit/miss

Tests use no real LLM, no real network, and no real filesystem outside
`tmp_path`.

---

## Integration

### As a library

```python
import sys
sys.path.insert(0, "99-scripts/report-extraction-to-permanent-notes-building-v5")
from v5lib.output_index import OutputIndex
from v5lib.matcher import Matcher
# ... etc
```

### As a subprocess

```powershell
python 99-scripts/report-extraction-to-permanent-notes-building-v5/pipeline_v5.py `
    --report self-determination-theory `
    --report-merges runs/sdt-merge-log.json
```

---

## What V5 Does NOT Do

- It does **not** modify V4. V5 only imports from V4.
- It does **not** scan the entire vault. The match index is scoped to the
  output directory only — by explicit design.
- It does **not** auto-promote `budding` or `evergreen` notes — those tiers
  remain operator-managed.
- It does **not** delete duplicates. If the matcher misses (e.g. a typo
  prevents the fuzzy hit), the new note will be written alongside the
  existing one. Use `--report-merges` and `--match-threshold` tuning to
  diagnose.
