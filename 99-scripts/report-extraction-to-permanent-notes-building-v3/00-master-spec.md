# Pipeline v3 — Master Specification & Sequenced Rollout

**Status:** Draft v0.2 — §8 decisions locked, Phase 0 unblocked
**Author:** GPT-5 (PKB Scripting collaborator)
**Owner:** pur3v4d3r
**Target start date:** Pending §1.2 / §3.2 / §3.3 sign-off
**Supersedes:** `pipeline_v2.py` (v2.1.0) and its 11 helper scripts
**Coexistence policy:** v2 remains operational and untouched until v3 has shipped Stages 0–6 and produced ≥1 successful end-to-end run on a clean rebuild

---

## 0. Goals & Non-Goals

### Goals (in priority order)

1. **Trustworthy audits.** The "missing concepts" table must contain only real concepts — not parser garbage, not report filenames, not YAML fragments, not flashcard Q/A text. Target: ≥98% of audited unresolved targets are genuine concepts a human would acknowledge.
2. **Higher resolution rate.** From the current 84% to ≥95%, achieved primarily by (a) eliminating garbage links and (b) catching paraphrase/acronym duplicates via embeddings.
3. **Denser, cleaner notes.** Notes that adapt to their content. A note with 3 callouts shouldn't have 12 empty H2 sections. A note with 30 callouts should be navigable.
4. **Faster runs.** Full vault rebuild from clean slate in ≤10 minutes on the 14900K. Incremental runs (1 new batch) in ≤30 seconds.
5. **Local-LLM augmentation where it earns its weight.** Embeddings and concept normalization, yes. Anywhere the regex pipeline is already correct, no.
6. **Safe to experiment.** Easy to nuke `_permanent-notes/` and rebuild. Easy to swap templates and re-render. Easy to A/B two builders.

### Non-goals

- **No cloud LLM dependency.** Everything runs on the 14900K + RTX 4090. No API keys, no internet during pipeline runs.
- **No replacement of `pkb_extractor.py`.** It's the upstream stage and works. v3 hardens its outputs but does not rewrite it.
- **No new callout taxonomy.** v3 consumes the existing 25+ callout types. New callouts can be added without v3 changes.
- **No multi-vault support, no plugin packaging.** Single-vault, script-driven, run-from-terminal.
- **No "AI writes the note for you" mode by default.** LLM synthesis is opt-in per run.

---

## 1. Architecture Overview

### 1.1 Data flow (v3)

```
┌─────────────────┐
│ Reports (.md)   │
└────────┬────────┘
         │ Stage 1: extract (parallel)
         ▼
┌──────────────────────────┐
│ _extracted.json          │  ← unchanged from v2
└────────┬─────────────────┘
         │ Stage 2: validate & sanitize        [NEW: link_validator.py]
         ▼
┌──────────────────────────┐
│ _validated.json          │  ← garbage stripped, links normalized
└────────┬─────────────────┘
         │ Stage 3: consolidate                [NEW: candidate_consolidator.py]
         ▼
┌──────────────────────────┐
│ super-candidates (in-mem)│  ← one per concept, evidence merged
└────────┬─────────────────┘
         │ Stage 4: LLM normalize (optional)   [NEW: llm_normalizer.py]
         ▼
┌──────────────────────────┐
│ canonical-candidates     │  ← canonical names, aliases, definitions
└────────┬─────────────────┘
         │ Stage 5: embed & match              [NEW: semantic_matcher.py]
         ▼
┌──────────────────────────┐
│ MatchReport              │  ← exact / alias / fuzzy / semantic / new
└────────┬─────────────────┘
         │ Stage 6: build / update             [REWRITE: note_renderer.py]
         ▼
┌──────────────────────────┐
│ Permanent notes (.md)    │  ← slim conditional template
└────────┬─────────────────┘
         │ Stage 7: stub generation            [REUSE: generate_stubs.py, hardened]
         │ Stage 8: link resolution            [REUSE: rewrite_report_wikilinks.py]
         │ Stage 9: normalize wiki-links       [REUSE: normalise_wikilinks.py]
         │ Stage 10: audit + score             [REUSE: audit_notes.py + scorer]
         │ Stage 11: MOC + graph build         [NEW: moc_builder.py]
         │ Stage 12: index + report + commit   [REUSE]
         ▼
        Done
```

### 1.2 Directory layout

```
99-scripts/report-extraction-to-permanent-notes-building-v3/
├── pipeline_v3.py                  # Master orchestrator (replaces pipeline_v2.py)
├── config_v3.py                    # All paths, thresholds, model configs
├── stages/                         # One module per stage
│   ├── __init__.py
│   ├── s1_extract.py               # Wraps pkb_extractor.py, parallel
│   ├── s2_validate.py              # link_validator + json sanitizer
│   ├── s3_consolidate.py           # Cross-batch candidate merger
│   ├── s4_normalize.py             # LLM concept normalization (optional)
│   ├── s5_match.py                 # Embedding-based matcher
│   ├── s6_render.py                # Slim template renderer
│   ├── s7_stubs.py                 # Stub generator (hardened)
│   ├── s8_resolve_links.py         # Report wiki-link rewriter
│   ├── s9_normalize_links.py       # Vault-wide link normalizer
│   ├── s10_audit.py                # Audit + quality scoring + gating
│   ├── s11_moc.py                  # MOC + concept graph builder
│   └── s12_commit.py               # Index, report, git commit
├── lib/                            # Shared utilities
│   ├── __init__.py
│   ├── link_validator.py           # Garbage-link detection (extracted from v2)
│   ├── candidate.py                # Canonical Candidate dataclass + JSON I/O
│   ├── frontmatter.py              # YAML read/write that preserves structure
│   ├── embeddings.py               # bge-small wrapper + cache
│   ├── llm_client.py               # Ollama HTTP client + retry + structured output
│   ├── markdown.py                 # Callout, link, heading helpers
│   ├── parallel.py                 # ProcessPoolExecutor wrapper with progress
│   ├── state.py                    # Pipeline state, hashes, diff-aware skipping
│   └── ui.py                       # rich console helpers
├── templates/                      # Note rendering templates (Jinja2)
│   ├── permanent_note.md.j2        # Main slim template
│   ├── moc.md.j2                   # MOC template
│   └── stub.md.j2                  # Stub template
├── tests/
│   ├── conftest.py
│   ├── test_link_validator.py
│   ├── test_candidate.py
│   ├── test_consolidator.py
│   ├── test_matcher.py
│   ├── test_renderer.py
│   └── fixtures/                   # Sample _extracted.json files
├── _v3-output/                     # Run logs, audits, embeddings cache
│   ├── embeddings/                 # .npz files keyed by note path hash
│   ├── llm-cache/                  # JSON responses keyed by content hash
│   ├── runs/                       # Per-run logs and reports
│   └── _pipeline-state.json
└── README.md
```

### 1.3 Coexistence with v2

- v3 lives in **a sibling directory** (`...-v3/`) — zero edits to v2 files
- v3 reads from the same `_extractor-output/` and writes to the same `_permanent-notes/` (after a `--rebuild` confirmation)
- A `--target-dir <path>` flag lets v3 write to a sandbox directory for A/B comparison
- The decision to retire v2 happens *after* v3 has produced ≥3 clean runs and passed validation gates (§7)

---

## 2. Local LLM / Embedding Stack

### 2.1 Embeddings (Stage 5, mandatory)

| Component | Choice | Rationale |
|---|---|---|
| Library | `sentence-transformers` | Python-native, no separate server, runs on `torch` w/ CUDA |
| Model | `BAAI/bge-small-en-v1.5` (384-dim) | 33M params, ~5 MB on disk, fits comfortably alongside any LLM |
| Storage | `.npz` per cache slice | Lazy-loadable, append-only |
| Cache key | SHA-1 of `(filepath, mtime, title, aliases joined)` | Invalidates on any change |
| Match scoring | `0.4 * difflib + 0.6 * cosine` | String sim guards against pure-semantic false positives |
| Auto-match threshold | ≥ 0.92 | Same as v2 |
| Review-queue band | 0.78 – 0.92 | Same as v2 |

### 2.2 LLM (Stage 4, opt-in)

| Component | Primary | Upgrade path |
|---|---|---|
| Runner | **Ollama** (Windows native, simple) | vLLM if/when WSL2 setup is in place |
| Model | `qwen2.5:7b-instruct-q5_K_M` | `qwen2.5:14b-instruct-q4_K_M` for synthesis |
| Client | `requests` → `http://localhost:11434/api/chat` | `openai`-compatible endpoint also exposed |
| Structured output | JSON schema in prompt + `outlines` validation post-hoc | `instructor` if migrating to OpenAI-compatible |
| Cache | Content-hash keyed JSON files in `_v3-output/llm-cache/` | Deterministic re-runs are free |
| Concurrency | Sequential (Ollama is single-tenant) | Batch via vLLM later |

### 2.3 What the LLM is and isn't allowed to do

**Allowed:**
- Normalize concept names (`"Achievement-Goal-Theory"` and `"Achievement Goal Framework"` → both map to `Achievement-Goal-Theory`)
- Suggest 3–5 aliases per concept
- Suggest 1-line canonical definitions for stubs
- Classify ambiguous review-queue matches as duplicate / new / variant
- (Opt-in) Synthesize a 100–200 word `## Synthesis` section from N evidence callouts

**Forbidden:**
- Inventing wiki-links not present in source material
- Modifying or deleting evidence/insight bodies (it can summarize them; the originals stay)
- Choosing the canonical name without source-context evidence
- Running on more than 1 concept per request when structured output is required (batch via repeated calls)

---

## 3. Data Contracts

### 3.1 Canonical `Candidate` (Stage 3 output)

```python
@dataclass(frozen=True)
class Candidate:
    canonical_name: str                    # Set in Stage 4 if LLM is on, else == primary_name
    primary_name: str                      # The most-frequent concept name across batches
    aliases: tuple[str, ...]               # Includes all variant names seen
    domain: str                            # Validated against VALID_DOMAINS
    subdomains: tuple[str, ...]
    definition_body: str                   # First non-empty definition seen
    confidence: Literal["high", "medium", "low"]
    complexity: Literal["foundational", "intermediate", "advanced-practitioner", "expert"]
    importance: Literal["high", "medium", "low"]

    # Aggregated content
    evidence: tuple[Evidence, ...]
    insights: tuple[Insight, ...]
    practices: tuple[Practice, ...]
    warnings: tuple[Warning, ...]
    reflections: tuple[Reflection, ...]
    persons: tuple[Person, ...]
    tensions: tuple[Tension, ...]
    open_questions: tuple[OpenQuestion, ...]
    flashcards: tuple[Flashcard, ...]
    protocols: tuple[Protocol, ...]
    diagrams: tuple[Diagram, ...]
    citations: tuple[Citation, ...]
    methodology: tuple[Methodology, ...]
    schema_activations: tuple[SchemaActivation, ...]
    active_readings: tuple[ActiveReading, ...]
    far_transfers: tuple[FarTransfer, ...]
    debates: tuple[Debate, ...]
    examples: tuple[Example, ...]
    section_summaries: tuple[SectionSummary, ...]
    claude_insights: tuple[ClaudeInsight, ...]

    # Provenance
    source_reports: tuple[SourceReport, ...]   # Each with batch, file, line, callout type
    wiki_links_seen: tuple[str, ...]           # Validated, deduplicated
    extraction_hash: str                       # Hash of all source content for diff-aware runs
```

Each `Evidence`, `Insight`, etc. carries `(body, source_report, source_line, callout_type)` so attribution is preserved through aggregation. **No anonymous content.**

### 3.2 Slim frontmatter (Stage 6 output)

Target: ≤25 lines of YAML for typical notes (down from ~80).

```yaml
---
title: "Self-Determination Theory"
aliases: [SDT, Self Determination Theory, Deci & Ryan SDT]
type: permanent-note
status: evergreen
confidence: high
domain: educational-psychology
subdomains: [motivational-psychology, autonomy-theory]
tags: [permanent-note, evergreen, educational-psychology, motivation]
created: 2026-04-21
updated: 2026-04-21
complexity: advanced-practitioner
importance: high
review-frequency: quarterly
mastery-stage: seedling
provenance:
  source-type: report-extraction
  pipeline-version: "3.0.0"
  source-reports:
    - self-determination-theory-foundational-report-2026-04-12
    - sdt-across-cultures-foundational-report-2026-04-15
  extraction-method: pkb-extractor-v1 → pipeline-v3
relationships:
  related: ["[[intrinsic-motivation]]", "[[autonomy-support]]", "[[competence-need]]"]
  see-also: ["[[self-efficacy-theory]]", "[[goal-setting-theory]]"]
  builds-on: ["[[cognitive-evaluation-theory]]"]
  enables: ["[[autonomy-supportive-teaching]]"]
---
```

Rationale for the changes:
- **No section-divider comments in YAML** (`# ═══`) — visual noise, breaks YAML parsers
- **Inline arrays for short lists** — readable without blowing up line count
- **`relationships:` and `provenance:` mappings** — group related fields, easier to extend
- **Dropped fields** that were always empty or always identical: `prerequisites: []`, `broader: []`, `narrower: []`, `expansion-topics: []`, `evidence-quality` (== confidence), `extraction-batch` (one of source-reports), `depth-level: comprehensive` (always)

### 3.3 Slim body template

Every section is **conditional** — emitted only if the corresponding content exists.

```markdown
# {{ title }}

{# Always-present hook #}
> [!definition] {{ title }}
> {{ definition_body }}

{% if synthesis %}
## Synthesis
{{ synthesis }}
{% endif %}

{% if evidence or insights %}
## Core Explanation
  {% for e in evidence %}
> [!evidence] {{ e.title or "Supporting evidence" }}
> {{ e.body }}
> *— [[{{ e.source_report }}]]*
  {% endfor %}
  {% for i in insights %}
> [!analytical-insight] {{ i.title or "Key insight" }}
> {{ i.body }}
> *— [[{{ i.source_report }}]]*
  {% endfor %}
{% endif %}

{% if practices or warnings %}
## Practical Implications
  {% for p in practices %}
> [!example] {{ p.title or "Application" }}
> {{ p.body }}
  {% endfor %}
  {% for w in warnings %}
> [!warning] {{ w.title or "Caution" }}
> {{ w.body }}
  {% endfor %}
{% endif %}

{# ... and so on for tensions, open-questions, flashcards, etc. — all conditional #}

## Connections
{% if related_concepts %}
**Related:** {{ related_concepts | join(' · ') }}
{% endif %}

{# Single Dataview block at the bottom for self-maintaining "see also" #}
```dataview
LIST FROM [[{{ stem }}]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** {{ source_reports | map_to_wikilinks | join(' · ') }}
```

Notes:
- **Single Dataview block** at the bottom replaces the manually-maintained `## See Also` list — Obsidian renders incoming links live
- **Source attribution moves to a single footer line**, not repeated under every callout (still queryable via the `source-reports:` frontmatter field)
- **Section headers are demoted from H2 to a more visually consistent style** when there are <2 callouts in the section (heuristic — H2 only if section has weight)

---

## 4. Module Inventory

### 4.1 New modules (must build)

| Module | Responsibility | Approx. LoC | Deps |
|---|---|---|---|
| `lib/link_validator.py` | Centralized garbage-link detection | 150 | stdlib |
| `lib/candidate.py` | Canonical Candidate + JSON I/O | 250 | stdlib + pydantic? |
| `lib/embeddings.py` | bge-small wrapper + cache | 200 | sentence-transformers, torch, numpy |
| `lib/llm_client.py` | Ollama client + structured output + cache | 250 | requests, outlines |
| `lib/parallel.py` | ProcessPoolExecutor + rich progress | 100 | concurrent.futures, rich |
| `lib/state.py` | Pipeline state + per-stage hashes | 150 | stdlib |
| `lib/markdown.py` | Callout/link/heading helpers (extracted from v2) | 200 | stdlib |
| `lib/frontmatter.py` | Structured YAML read/write | 200 | PyYAML, ruamel.yaml |
| `stages/s2_validate.py` | Wraps link_validator, sanitizes JSON in place | 200 | lib/* |
| `stages/s3_consolidate.py` | Merges candidates across batches | 300 | lib/candidate, lib/parallel |
| `stages/s4_normalize.py` | LLM normalization (opt-in via flag) | 250 | lib/llm_client |
| `stages/s5_match.py` | Embedding-based matcher | 350 | lib/embeddings |
| `stages/s6_render.py` | Jinja2 renderer for slim template | 300 | jinja2 |
| `stages/s11_moc.py` | MOC + concept graph builder | 250 | lib/* |
| `templates/permanent_note.md.j2` | Slim conditional template | — | jinja2 |
| `templates/moc.md.j2` | Per-domain MOC template | — | jinja2 |
| `templates/stub.md.j2` | Stub note template | — | jinja2 |

### 4.2 Reused (with hardening)

| v2 module | Status in v3 | Notes |
|---|---|---|
| `pkb_extractor.py` | **Reused as-is** | Output passes through s2_validate before downstream |
| `audit_notes.py` | **Reused, wrapped** | `s10_audit.py` adds quality-score gating |
| `note_quality_scorer.py` | **Promoted** | Now run automatically post-build, not just on demand |
| `generate_stubs.py` | **Hardened** | Filters via link_validator before generating |
| `rewrite_report_wikilinks.py` | **Reused** | No changes |
| `normalise_wikilinks.py` | **Reused** | No changes |
| `vault_indexer.py` | **Reused** | No changes |

### 4.3 Deprecated (after v3 ships Stage 6)

| v2 module | Replaced by | Removal trigger |
|---|---|---|
| `pipeline_v2.py` | `pipeline_v3.py` | After 3 successful v3 runs |
| `pipeline.py` (Stage 2 engine) | stages/s5_match.py + s6_render.py | Same |
| `note_builder.py` | stages/s6_render.py + templates/* | Same |
| `note_updater.py` | stages/s6_render.py (handles update + create uniformly) | Same |
| `note_matcher.py` | stages/s5_match.py | Same |
| `report_parser.py` | lib/candidate.py | Same |
| `scan_extractions.py` | stages/s3_consolidate.py | Same |
| `dedicated_notes_builder.py` | stages/s11_moc.py (MOCs cover this use case) | Same |
| `generate_notes.py` | n/a (v1 leftover) | Immediate |
| `rewrite_wikilinks.py` | n/a (v1 leftover) | Immediate |
| `fix_broken_pipes.py` | n/a (the bug it fixes is gone in v3) | Immediate |
| `flashcard_exporter.py` | Untouched (orthogonal feature) | n/a |
| `conflict_detector.py` | TBD — review whether s10_audit covers it | Decide at Stage 10 |
| `auto_moc_generator.py` | stages/s11_moc.py | Same as pipeline_v2 |
| `fix_broken_pipes.py` | n/a | Immediate |
| `promote_stubs.py` | TBD — may keep as a manual ops tool | Keep |
| `pipeline_logger.py` | lib/state.py + lib/ui.py | After 3 runs |
| `batch_tracker.py` | lib/state.py | After 3 runs |

---

## 5. Sequenced Rollout

The rollout is **strictly sequential** and **gated**: each phase must pass its acceptance criteria before the next begins. No parallel work across phases. Each phase produces a working, testable artifact.

### Phase 0 — Foundation (no functional changes)

**Deliverables:**
- Create `99-scripts/report-extraction-to-permanent-notes-building-v3/` directory
- Set up `pyproject.toml` or `requirements-v3.txt` pinning all dependencies
- Install: `sentence-transformers`, `torch` (CUDA build), `jinja2`, `pydantic`, `ruamel.yaml`, `outlines`, `requests`, `pytest`, `pytest-cov`
- Install Ollama for Windows; pull `qwen2.5:7b-instruct-q5_K_M` and `bge-m3` (fallback embed model)
- Scaffold the directory structure (empty modules with docstrings)
- Write `tests/conftest.py` with shared fixtures (sample `_extracted.json` files copied from real batches)

**Gate:**
- `python -c "import sentence_transformers, torch; print(torch.cuda.is_available())"` returns True
- `curl http://localhost:11434/api/tags` returns the installed models
- `pytest tests/` runs (passes 0/0 — no real tests yet)

### Phase 1 — Garbage-link elimination (P0 from review)

**Deliverables:**
- `lib/link_validator.py`: consolidates `_GARBAGE_LINK_PATTERNS` from `note_updater.py`, `_REPORT_FILENAME_PATTERN` and concept-name validation from `note_builder.py`. Exports a single `is_valid_concept(name: str) -> tuple[bool, reason: str]`
- `stages/s2_validate.py`: reads each `_extracted.json`, walks all wiki-link targets and callout titles, emits a `_validated.json` with garbage stripped and a `_validation-report.json` listing what was removed and why
- Tests: ≥30 fixture cases covering all known garbage patterns + ≥10 valid concepts that must pass through
- Run validator over all 11 existing batches; manually review the validation report

**Gate:**
- 100% of explicit garbage fixtures rejected
- 100% of valid concept fixtures accepted
- Spot-check shows the 638-item "missing concepts" table from the 2026-04-20 audit shrinks to ≤350 when validator-stripped sources are re-audited (estimate; refine after running)

### Phase 2 — Cross-batch consolidation (P1)

**Deliverables:**
- `lib/candidate.py`: full `Candidate` dataclass (§3.1) with `from_extracted_json()` and `merge(other)` methods
- `stages/s3_consolidate.py`: reads all `_validated.json`, groups by normalized concept name, produces a single in-memory list of consolidated `Candidate` objects. Writes a `_consolidated-candidates.json` snapshot for inspection
- `lib/parallel.py`: `ProcessPoolExecutor` wrapper with rich progress bar
- Stages 1, 2, 3 wired into a `pipeline_v3.py --to-stage 3` partial entry point
- Tests for merge logic (no duplicate evidence, source_reports preserved, alias union)

**Gate:**
- Run on full corpus → `_consolidated-candidates.json` produced with ≤ N candidates where N < (batches × per-batch). Estimate: ~600 unique concepts vs. ~2000 raw candidates
- Total runtime for stages 1-3: ≤2 minutes on the full corpus
- 0 lost evidence: a checksum on (concept_name, evidence_body) pairs is identical pre- and post-consolidation

### Phase 3 — Slim renderer + dry-run rebuild (P2 + P10)

**Deliverables:**
- `templates/permanent_note.md.j2`: full slim template per §3.3
- `lib/frontmatter.py`: structured YAML write that emits §3.2 layout
- `stages/s6_render.py`: takes `Candidate` → renders markdown via Jinja2. **Update path**: if a note exists at the target path, parse its frontmatter, merge the new candidate's content additively (preserving manual edits to body), re-render
- `lib/markdown.py`: callout/link/heading helpers
- `pipeline_v3.py --to-stage 6 --target-dir _sandbox-rebuild`: full dry-run that produces ~600 notes in a sandbox dir without touching `_permanent-notes/`
- Visual review: open 20 sandbox notes in Obsidian, eyeball the rendering, iterate template

**Gate:**
- 0 broken Obsidian renders (every sandbox note opens and renders cleanly)
- Average note length: 150–600 lines (currently many are 800–1500 with empty sections)
- Average frontmatter lines: ≤25 (currently ~80)
- All callout types from §3.1 render with appropriate styling
- The single Dataview block at the bottom resolves correctly

### Phase 4 — Embedding-based matcher (P4)

**Deliverables:**
- `lib/embeddings.py`: bge-small wrapper, batch encoding, `.npz` cache with mtime invalidation
- `stages/s5_match.py`: replaces v2's `note_matcher.py` with hybrid `0.4*difflib + 0.6*cosine`
- A precompute step: on first run, embed all existing notes (currently 0 — clean slate; after first rebuild, ~600). Subsequent runs only embed changed notes
- Match report writes to `_v3-output/runs/<run_id>/match-report.json` with: matched, review-queue (0.78–0.92), new
- Tests: synthetic pairs (acronym/expansion, paraphrase, completely unrelated) — verify expected match band

**Gate:**
- Embedding precompute on a 600-note corpus: ≤30 seconds on RTX 4090
- Per-candidate match: ≤5 ms (after warmup)
- Recall test on a hand-curated set of 30 known synonym pairs: ≥27/30 land in match or review-queue band
- Precision test: 30 pairs of unrelated concepts → ≤2 false positives in the match band

### Phase 5 — Wire stages 7–10 + first full run

**Deliverables:**
- `stages/s7_stubs.py`: hardened `generate_stubs` that filters via `link_validator`
- `stages/s8_resolve_links.py`, `s9_normalize_links.py`: thin wrappers around existing v2 scripts
- `stages/s10_audit.py`: runs `audit_notes.py` + `note_quality_scorer.py`, gates pass/fail on (a) resolution rate ≥95%, (b) average quality ≥60, (c) low-quality notes (<40) ≤5% of total
- `pipeline_v3.py --to-stage 10` end-to-end run on a sandbox target dir
- Compare sandbox audit vs. last v2 audit (2026-04-20)

**Gate:**
- Resolution rate ≥95% (vs. 84% in v2)
- "Missing concepts" table contains ≤200 items (vs. 638) and ≥98% are real concepts on manual review
- Average note quality score ≥60
- Total runtime stages 1–10: ≤10 minutes on full corpus

### Phase 6 — Cutover

**Deliverables:**
- `pipeline_v3.py --rebuild --execute`: deletes `_permanent-notes/_permanent-notes/`, runs full pipeline, commits
- README updated to point to v3
- `pipeline_v2.py` and the deprecated modules listed in §4.3 moved to `99-scripts/_archive/v2/`
- `_audit-report-<date>-v3.md` committed alongside v2's last audit for historical comparison

**Gate:**
- 3 successful v3 runs over a 1-week window with no manual interventions
- User-acknowledged satisfaction with note rendering (§3.3 review)

### Phase 7 — LLM concept normalization (P5, opt-in)

This phase is **deliberately last** for the regex/embedding core. It ships only after the pure-Python pipeline is rock-solid and audit-clean.

**Deliverables:**
- `lib/llm_client.py`: Ollama HTTP client, structured output validation, content-hash cache
- `stages/s4_normalize.py`: takes consolidated candidates → calls Ollama with each (or batches via repeated calls) → returns `(canonical_name, aliases, definition, domain_suggestion)`. Inserted between Stage 3 and Stage 5
- Prompt: stored in `templates/normalize.prompt.txt`, version-controlled
- Flag: `--llm-normalize` (off by default)
- Cache: `_v3-output/llm-cache/<sha1>.json` — re-runs free for unchanged candidates
- A/B comparison report: same corpus rendered with and without `--llm-normalize`, diff summarized

**Gate:**
- LLM normalization adds <5 minutes to a full pipeline run on the corpus
- A/B diff shows: ≥10 new alias matches caught (paraphrase/acronym), 0 hallucinated wiki-links injected
- User reviews diff and approves or rejects per-candidate changes via a generated review queue

### Phase 8 — MOC + concept graph (P8)

**Deliverables:**
- `stages/s11_moc.py`: per-domain MOC builder using `templates/moc.md.j2`
- Per-MOC Mermaid graph of strongest 20 concept-to-concept links
- A vault-level `_GLOBAL-MOC.md` linking to all per-domain MOCs

**Gate:**
- 12 domain MOCs generated (one per `VALID_DOMAINS` value with ≥5 notes)
- Each MOC renders cleanly in Obsidian
- Mermaid graphs render without errors

### Phase 9 — LLM synthesis (P6, opt-in, optional)

Ship only if Phases 7 and 8 deliver clear value. Otherwise punt.

**Deliverables:**
- `--llm-synthesize` flag → runs a synthesis pass per high-density note (≥5 evidence/insight callouts)
- Synthesis injected as a `## Synthesis` section near the top, before `## Core Explanation`
- Original callouts preserved below as the receipt
- Synthesis cached by content hash

**Gate:**
- Synthesis pass adds <15 minutes to a full run on the corpus (corpus has maybe 50–100 high-density notes)
- 10-note manual review: synthesis is accurate, doesn't introduce new claims, cites all source reports

### Phase 10 — Diff-aware incremental runs (P7)

**Deliverables:**
- `lib/state.py`: per-stage content hashes, skip logic
- `pipeline_v3.py --incremental`: skips work for unchanged inputs

**Gate:**
- A no-op run (no new batches, no edits) finishes in ≤10 seconds
- Adding 1 new batch processes only that batch + affected matches

---

## 6. Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| bge-small embeddings give too many false positives in match band | Medium | High — silent merging of unrelated concepts | Hybrid score (string + semantic) + review queue band 0.78–0.92 + per-run match-report for inspection |
| Ollama instability on Windows | Medium | Medium — Stage 4 unavailable | Stage 4 is opt-in; pipeline runs without it. Cache survives so incomplete runs don't waste work |
| Slim template loses information valued by user | Low | Medium — note feels "less rich" | Phase 3 gate is visual review of 20 sandbox notes before any cutover. Template is iterable |
| Cutover breaks links in non-permanent-note content elsewhere in vault | Medium | High — broken links across the rest of the PKB | Run `link_check.py` on the entire vault before and after cutover. Compare diff |
| Consolidation loses content from one of N source reports | Low | High — silent data loss | Phase 2 gate includes a checksum: every (concept, evidence-body) pair from `_validated.json` must appear in the consolidated output |
| LLM normalization renames a concept incorrectly | Medium | Medium — wrong canonical name persisted | LLM proposes; renames require explicit user approval via review queue. Never auto-applied |
| Pipeline gets stuck mid-run with no clear way to resume | Medium | Medium — wasted run time | `lib/state.py` per-stage state checkpoints. `--from-stage N` resume is a first-class feature, not an afterthought |
| 14900K + 4090 thermal/power issues during long runs | Low | Low | Monitor first few runs; if seen, throttle parallelism |
| User wants to revert to v2 mid-rollout | High (correctly!) | Low — by design | v2 is untouched until Phase 6. `git checkout` of `_permanent-notes/` reverts notes |

---

## 7. Validation Plan

### 7.1 Per-phase tests

Each phase ships with `pytest` tests targeting its modules. Coverage target: ≥80% for new modules.

### 7.2 End-to-end gates (must all pass for cutover)

| Gate | Metric | Target |
|---|---|---|
| Resolution rate | `audit_notes.py --markdown` | ≥95% |
| Garbage in missing-concepts | Manual review of 50 random unresolved | ≥98% real concepts |
| Average note quality | `note_quality_scorer.py` mean | ≥60 |
| Low-quality notes | <40 score | ≤5% of total |
| Orphan notes | 0 incoming | ≤1% (currently 0.1%) |
| Total runtime (full rebuild) | wall clock | ≤10 minutes |
| Total runtime (incremental, 1 new batch) | wall clock | ≤30 seconds |
| Frontmatter line count | mean | ≤25 |
| Body section count | mean | ≤8 (only sections with content) |
| Callout coverage | % of source callouts that appear in notes | ≥95% |

### 7.3 Manual review checkpoints

After each phase, a 30-minute manual review. Specifically after Phase 3, the user opens 20 random rebuilt notes in Obsidian and signs off on rendering before Phase 4 begins.

### 7.4 Rollback procedure

At any point pre-cutover (Phase 0–5):
- v3 is in a sibling directory; deleting it has zero effect on v2
- v2 continues to work

At cutover (Phase 6):
- All changes are committed in a single git commit (`v3-cutover`)
- Rollback = `git revert v3-cutover` + `pipeline_v2.py --execute --auto-commit`
- v2 source files are archived (not deleted) to `99-scripts/_archive/v2/`

---

## 8. Locked Decisions (resolved 2026-04-21)

| # | Decision | Resolution | Notes |
|---|---|---|---|
| 1 | LLM runner | **Ollama** | Already installed, queryable via curl. vLLM remains future upgrade path if WSL2 is set up. |
| 2 | `Candidate` modeling | **pydantic v2** | Designed pydantic-first from the start; validation + structured-output integration earn the dependency. |
| 3 | Jinja2 templates | **Separate `.j2` files** | Lives in `templates/`. Non-programmer-editable, clean diffs, keeps `s6_render.py` lean. |
| 4 | `## Synthesis` (P6) | **Opt-in via `--llm-synthesize`** | Stays opt-in until ≥30 hand-reviewed syntheses validate prompt + output quality. |
| 5 | MOC depth | **Per-domain only (Phase 8)** | Per-subdomain MOCs deferred — add only if navigation pain emerges. |
| 6 | `_Master-*-Index.md` notes | **Retired in favor of MOCs** | v2 `_Master-*` files moved to `99-scripts/_archive/v2/notes/` at cutover, not deleted. |

All six decisions are final. No further blockers on Phase 0.

---

## 9. Glossary

- **Candidate** — Internal data type representing one extractable concept, before matching against existing notes
- **Super-candidate / Consolidated candidate** — A Candidate that has been merged with all other Candidates of the same concept across all batches
- **Canonical name** — The agreed-upon primary name for a concept (set deterministically in Stage 3, optionally refined by LLM in Stage 4)
- **Match band** — The cosine + difflib hybrid score range:
  - **Auto-match** (≥0.92): silently treated as the same concept
  - **Review queue** (0.78–0.92): surfaced for human or LLM decision
  - **New** (<0.78): treated as a brand-new concept
- **Garbage link** — A wiki-link target that is not a real concept (Templater syntax, YAML fragment, sentence, report filename, etc.) — eliminated by `link_validator`
- **Cutover** — The moment v3 replaces v2 as the production pipeline (Phase 6)
- **Slim template** — The v3 conditional Jinja2 template that emits only sections with content

---

## 10. Next action

**Phase 0 is unblocked.** All §8 decisions are locked.

Remaining sign-offs before scaffolding (low-risk, tell me to proceed if no edits):
1. Directory layout (§1.2) — sibling `-v3/` directory, `lib/` + `stages/` + `templates/` + `tests/`
2. Slim frontmatter spec (§3.2) — ~25 line YAML with `provenance:` and `relationships:` mappings
3. Slim body template (§3.3) — every section conditional, single bottom Dataview block, footer source attribution

**Phase 0 deliverables on greenlight:**
- Create `99-scripts/report-extraction-to-permanent-notes-building-v3/` with the §1.2 layout
- `requirements-v3.txt` pinning: `sentence-transformers`, `torch` (CUDA), `jinja2`, `pydantic>=2`, `ruamel.yaml`, `outlines`, `requests`, `pytest`, `pytest-cov`, `rich`, `click`
- Pull Ollama models: `qwen2.5:7b-instruct-q5_K_M`, `bge-m3` (embed fallback)
- Verify CUDA via `torch.cuda.is_available()` and Ollama via `curl http://localhost:11434/api/tags`
- Scaffold empty modules (docstrings only)
- `tests/conftest.py` with fixtures copied from real `_extracted.json` batches

Report back when Phase 0 gate passes, then proceed to Phase 1 (link_validator).


