# V6 — Two-Pass Elaborated Permanent-Note Pipeline

> [!abstract]
> V6 layers on top of V4's bundle-mining and V3's LLM client to produce
> **materially richer permanent notes** through a two-pass LLM design:
>
>   1. **Pass A — Outline.** The model plans the note: canonical title,
>      seeded definition, definition boundary, parent concept, section
>      outline with intent + source-hooks, related concepts (typed),
>      key figures, open-questions seed, distinctions seed.
>   2. **Pass B — Elaborate.** Given the outline, the model writes the
>      long-form content: an elaborated definition that integrates the
>      parent reference, 4–6 narrative paragraphs of core explanation,
>      mechanism prose, 3–5 practical implications, key distinctions,
>      figure contributions, open questions, synthesis, and an evidence
>      narrative — all as **prose, never bullet lists**.

## Why V6?

V3/V4 produce single-pass condensations that tend to be terse and
bullet-y. V5 added merge-routing on top of V4's generator. V6 keeps
that infrastructure but **replaces the generator** with a two-pass
elaborator that dedicates one LLM round-trip to *planning* and a second
to *writing*. The result is notes that:

- Have a **definition callout** with elaborated body + boundary +
  `Falls under [[Parent-Concept]]` link.
- Have a **Core Explanation** of 4–6 narrative paragraphs (80–180 words
  each) instead of bulleted insights.
- Have **Practical Implications** as `[!example]` callouts with
  scenario-anchored 80–150 word bodies.
- Have **Key Distinctions** as `[!key-distinction]` callouts with
  concrete contrast bodies.
- Have **Key Figures**, **Open Questions** (with resolution hints),
  **Synthesis**, **Evidence narrative**, and a **Connections & Context**
  block grouped by typed relation.

## Output location

V6 writes to a **dedicated subdirectory** so it never collides with V4/V5:

    999-report-organizing/_permanent-notes/v6-llm-elaborated/

Override with `--output-dir /any/other/path`.

## Usage

### Discover what would be processed

    python pipeline_v6.py --report self-determination-theory --limit 2 --dry-run -v

### Real run on a single report

    python pipeline_v6.py --report cognitive-load-theory

### Force live LLM calls + skip worthiness gate

    python pipeline_v6.py --bypass-cache --no-gate --report sdt

### Audit log of every per-bundle outcome

    python pipeline_v6.py --report-runs runs/2026-04-23-v6-log.json

## CLI flags

| Flag                   | Purpose                                                  |
|------------------------|----------------------------------------------------------|
| `--input-dir PATH`     | Directory of `*_extracted.json` files                    |
| `--output-dir PATH`    | Override default v6 output dir                           |
| `--report STR`         | Substring filter on JSON filename stem                   |
| `--limit N`            | Cap total concepts processed                             |
| `--include-key-claims` | Include `[!key-claim]` callouts as concept candidates    |
| `--mode skip|overwrite`| Collision policy in v6 output dir (default: `skip`)      |
| `-n`, `--dry-run`      | Run LLM (cache) but write nothing                        |
| `--bypass-cache`       | Force live LLM; ignore cache                             |
| `--model NAME`         | Override Ollama model                                    |
| `--no-gate`            | Run Pass B even when Pass A returns `worthy=false`       |
| `--report-runs PATH`   | Write per-bundle JSON audit log                          |
| `--strict`             | Exit non-zero on any failure                             |
| `-v`, `-q`             | Verbosity / quiet                                        |

## Exit codes

| Code | Meaning                                |
|------|----------------------------------------|
| 0    | Success                                |
| 1    | Uncaught error                         |
| 2    | Input dir not found                    |
| 4    | No JSONs / no concepts mined           |
| 5    | `--strict` + at least one failure      |
| 6    | Ollama unreachable                     |
| 130  | Interrupted (Ctrl+C)                   |

## Architecture

```
pipeline_v6.py          # CLI orchestrator (NEW route only — fresh writes)
├── v6lib/prompts.py    # System + user templates, Pydantic schemas:
│                       #   OutlineResponse, ElaborateResponse,
│                       #   MergeResponseV6, plus contract version stamps.
├── v6lib/elaborator.py # Two-pass LLM orchestration:
│                       #   run_outline() → run_elaborate() → ElaborateResult
└── v6lib/renderer.py   # Frontmatter + body assembly into final markdown.
```

V6 imports from the V3/V4 source trees via `sys.path` injection and
reuses:

- `pipeline_v4.discover_jsons` / `load_payload` / `build_bundles` /
  `ConceptBundle` / `write_atomic`
- `lib.llm_client.OllamaClient` (V3)
- `lib.markdown.callout` / `wikilink` / `join_wikilinks` (V3)
- `config_v3.VAULT_ROOT` / `LLM_CACHE_DIR` / `OLLAMA_URL` /
  `LLM_MODEL_SYNTHESIZE` / etc.

## Cache isolation

Each LLM contract has its own cache key. V6 uses two distinct contract
versions:

- `v6-outline-v1`   — Pass A
- `v6-elaborate-v1` — Pass B (cache key also includes the outline's
                              section signature, so re-planning busts
                              elaboration).

V3/V4/V5 cache entries are not affected.

## Status

| Component        | State             |
|------------------|-------------------|
| `prompts.py`     | ✅ Complete + tested |
| `elaborator.py`  | ✅ Complete       |
| `renderer.py`    | ✅ Complete + tested |
| `pipeline_v6.py` | ✅ Complete (NEW route) |
| `merger_v6.py`   | ⏳ Deferred — only relevant on second-run-against-existing-v6-notes |
| Tests            | ✅ 21/21 passing  |

The `merger_v6.py` module is deferred because the V6 first run starts
clean against fresh JSON output. Once V6 notes exist and re-runs are
needed, the merger can mirror V5's `Merger` class but use
`MergeResponseV6` and `build_merge_user_prompt` (already defined in
`prompts.py`).

## Tests

    python -m pytest tests/ -v

Tests cover:

- `OutlineResponse` / `ElaborateResponse` schema validation
- Relation-type synonym normalization (`broader` → `generalizes`,
  `contrast` → `contrasts-with`, `narrower` → `specializes`, etc.)
- Definition-callout assembly (parent reference is appended only when
  not already present in the LLM body)
- Section ordering in the rendered note
- Empty-section omission
- Connections block ordering by canonical relation order
- Wiki-link harvesting from existing note bodies

## Smoke test

    python pipeline_v6.py --report self-determination-theory \
      --limit 2 --dry-run -v

Expected: discovers JSON, mines bundles, runs both LLM passes, prints
"V6 Summary" with `Written/dry-ran: 2` (assuming the worthiness gate
admits both).
