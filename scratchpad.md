
# Pipeline Review: Report Extraction → Permanent Notes

I've walked the pipeline (pipeline_v2.py, pkb_extractor.py, report_parser.py, note_matcher.py, note_updater.py, note_builder.py, note_quality_scorer.py, config.py) and the latest audit (_audit-report-2026-04-20.md). Permanent notes folder is currently empty — clean slate, perfect for restructuring.

Below: what's strong, what's holding it back, what to change, and where local LLMs (RTX 4090) genuinely earn their keep vs. where they'd be over-engineering.

---

## 1. Honest Assessment of Current State

### Strengths
- **Stage isolation + dry-run-by-default** is excellent — you can re-run any stage in isolation
- **Auto-discovery of batches** in config.py removed a manual maintenance burden
- **Three-tier matching** (exact → alias → fuzzy@0.92 with a 0.78–0.92 review band) is a sensible design
- **Updater is additive-only** with paraphrase-aware dedup (`SequenceMatcher@0.80`) — safe
- **Per-note quality scorer** already exists (note_quality_scorer.py) — underused
- **20+ enriched callout types** already wired through the data model (`NoteCandidate` v2.2)

### Hard problems visible in the audit
The 2026-04-20 audit surfaces *the* core defect: **the extractor is regex-only and bleeds non-concepts into the wiki-link space.** Look at the missing-concepts table:

| # | Missing target | What it actually is |
|---|---|---|
| 18 | `memory-systems-...-foundational-report-2026-04-07` | A **report filename** (should be filtered) |
| 13 | `A dedicated investigation of the most efficient protocols...` | A **sentence** |
| 10 | `**Topic**: Attribution Retraining...\n**Report Type**:...` | A **YAML fragment** |
| 6 | `Q: How does Piaget distinguish... A: Assimilation...` | A **flashcard Q/A** that became a link target |
| 2 | `Assimilation-vs....` / `Bernard-Wei...` | **Truncated** display text from `[[X|Y...]]` parsed wrong |

Of the 638 "missing concepts," I'd estimate **~40-60% are not concepts at all** — they're parser artifacts, not link rot. This single bug inflates the unresolved count, pollutes stub generation (`generate_stubs.py` will create stubs for garbage), and makes the audit untrustworthy.

### Other latent issues
- **Note bloat**: `note_builder.build_body` emits ~20 H2 sections (Core Explanation, Practical Implications, Key Figures, Tensions, Open Questions, Reflections, Schema Activations, Active Reading, Far Transfer, Debates, Examples, AI Insights, Section Summaries, Spaced Repetition, Protocols, Diagrams, Connections, References, Methodology, Source Attribution). Most notes will populate 3–5 of those — the rest are **empty H2 headers** unless you guard every section
- **Frontmatter is enormous** (~80 lines, 12 visual section dividers). Obsidian renders this as a wall of YAML in source mode and a giant properties panel in live preview. Review-fatigue inducing
- **No cross-batch deduplication before build**: if "Self-Determination Theory" appears in 10 reports, the matcher works each time against the existing 1094 notes (O(N×M)); merging candidates *first* would be O(M)
- **No semantic matching**: `Achievement-Goal-Theory` vs `Achievement-Goal-Framework` only matches if `difflib` happens to clear 0.92 — synonyms / paraphrases / acronym/expansion pairs slip through and create duplicates
- **Sequential execution**: pipeline_v2 runs stages serially; extraction & matching are embarrassingly parallel
- **`_pipe_link()` silently degrades**: if `sanitize_filename` raises on a display name (Templater leak, sentence, etc.), it falls back to `[[raw display name]]` — **this is the source of most garbage links** in the audit. The link survives, the audit can't resolve it, and stubs propagate the garbage

---

## 2. Proposed Improvements — Prioritized

I've ranked these by **(impact / effort)**. Items P0–P2 are the high-leverage core; P3+ are quality-of-life and aesthetic.

### P0 — Fix the garbage-link leak (no LLM needed, ~1 day)

This single fix will probably move resolution from 84% → 92%+ and shrink the "missing concepts" table by half.

**Where it leaks:**
1. pkb_extractor.py — `wiki_link` regex captures `[[` → `]]` greedily and accepts anything in between, including newlines on weird inputs and YAML fragments inside callout bodies
2. `note_builder._pipe_link()` — falls back to raw display name on `InvalidConceptNameError`, perpetuating the garbage downstream
3. `note_updater._GARBAGE_LINK_PATTERNS` — has the right idea but is only applied at update-time, **not at extraction-time**

**Fix:**
- Promote `_GARBAGE_LINK_PATTERNS` (and `_REPORT_FILENAME_PATTERN`, `_MAX_CONCEPT_TOKENS` from `note_builder`) into a shared `link_validator.py`
- Run it at the **extraction boundary** in pkb_extractor.py so garbage never reaches `_extracted.json`
- Change `_pipe_link()`'s fallback from "emit broken link" to "emit plain text + warning" — broken links should fail loudly, not silently
- Add `--strict-links` flag that promotes warnings to errors for CI runs

### P1 — Pre-build candidate consolidation (no LLM, ~½ day)

Currently each `_extracted.json` produces its own `NoteCandidate`s and the matcher runs against the full notes dir for *every* candidate. With 11 batches × ~40 candidates × 1094 notes = ~480K comparisons per run.

**Fix:** Add a `consolidate_candidates.py` step between scan and match:
1. Group all candidates from all batches by normalized concept name
2. Merge their `evidence`, `insights`, `practices`, `wiki_links`, `source_reports` into a single super-candidate
3. Match once per super-candidate → either updates one note with all 10 reports' content in one pass, or creates one rich note instead of 10 successive update operations

This also kills a class of race-condition-shaped bugs where update order changes the final note content.

### P2 — Slim, conditional note template (~½ day)

Current builder emits H2 headers even for empty sections, producing skeletal notes with 15 placeholder sections. Permanent notes should be **dense, not structured-but-empty**.

**Fix:**
- Make every section conditional on its content (`if candidate.tensions: lines.append("## Tensions")`)
- Collapse the YAML frontmatter from ~80 lines to ~25 by:
  - Removing the visual `# ═══` dividers (they bloat YAML, Obsidian renders properties separately anyway)
  - Move rarely-used fields (`extraction-method`, `pipeline-version`, `extraction-batch`) into a single `provenance:` mapping
  - Drop `subdomains: [ - ""]` empty-list scaffolding
- Aim for **note-renders-well-with-3-callouts-or-30-callouts** — the same template should look right at both extremes

I can produce a redesigned template + builder rewrite as a deliverable if you greenlight a direction.

### P3 — Parallel execution (~½ day, no LLM)

Stages 1 (extract) and 2 (scan/match/build) are CPU-bound and embarrassingly parallel. Use `concurrent.futures.ProcessPoolExecutor` with `max_workers=os.cpu_count()`. On a 14900K, expect 8–12× speedup on extract and ~6× on build.

### P4 — Vector-based fuzzy matcher (LOCAL LLM, RTX 4090) — high impact

This is where the GPU starts to earn its keep. Replace `difflib.SequenceMatcher` with **sentence embeddings + cosine similarity** in note_matcher.py.

**Why it matters:**
- Catches `Achievement-Goal-Theory` ↔ `Achievement-Goal-Framework` (paraphrase)
- Catches `SDT` ↔ `Self-Determination Theory` (acronym/expansion)
- Catches `Cognitive Load Theory (Sweller)` ↔ `Sweller Cognitive Load` (reordering)
- Catches `Working Memory Capacity` ↔ `Span of Apprehension` (synonyms)

**Stack:**
- `sentence-transformers` with **`BAAI/bge-small-en-v1.5`** (~33M params, 384-dim, runs in ~50ms/batch on 4090, 90%+ recall on STS benchmarks)
- Pre-compute embeddings for all 1094 existing notes' `(stem, title, aliases)` once → cache in `_pipeline-output/notes_embeddings.npz`
- Invalidate cache by `(filepath, mtime)` per note — only re-embed changed notes
- Hybrid scoring: `0.4 * difflib + 0.6 * cosine_sim` (string sim guards against pure-semantic false positives like `Growth Mindset` ↔ `Growth Hacking`)
- Two thresholds preserved: ≥0.92 auto-match, 0.80–0.92 review queue, <0.80 = new note

**Cost:** ~150MB model, 5–10s startup, then sub-millisecond match per candidate. Strict net win on a vault this size.

### P5 — LLM-assisted concept extraction & cleanup (LOCAL LLM, RTX 4090)

Two specific places where small local LLMs dramatically outperform regex:

**5a. Callout title parsing** (`report_parser.parse_definition_title`)
The regex parser handles `"Concept** (Domain — Author, Year)"` but breaks on natural variations. A 3B–8B model can extract structured fields from messy titles with near-100% accuracy.

**5b. Concept normalization & alias mining**
Run a one-shot pass that, for each candidate concept, asks: "Give me the canonical name + 3-5 aliases + 1-line definition + parent domain." Stack:
- **Qwen2.5-7B-Instruct** or **Llama-3.1-8B-Instruct** via `vllm` or `llama.cpp` w/ Q5_K_M GGUF — both fit in 24GB VRAM with ~6K context
- Batch 32 concepts per request → ~2–3s per batch on 4090
- Use **structured output** (JSON schema with `outlines` or `lm-format-enforcer`) to guarantee parseable results
- Cache responses keyed by concept-name hash → idempotent re-runs are free

This gives you **(a)** higher-quality aliases (the audit shows aliases are sparsely populated), **(b)** automatic disambiguation suggestions for the review queue, and **(c)** stub bodies that aren't empty.

### P6 — LLM-summarized "Core Explanation" (LOCAL LLM, optional)

When a concept has 5+ pieces of evidence/insight scattered across reports, the current builder concatenates them as a list of callouts. Optionally, run a synthesis pass: "Given these 8 evidence/insight callouts about [Concept], write a 150-word integrated `## Synthesis` section that preserves all distinct claims and cites the source reports."

Adds at top of note. Original callouts stay below as the receipt. **Toggle behind `--llm-synthesize` flag** so it's opt-in per run.

### P7 — Diff-aware incremental builds (~½ day, no LLM)

`pipeline_v2` already has a `_processed-batches.json` mechanism. Extend it:
- Hash each `_extracted.json` content
- Skip the whole match→update path for unchanged extractions
- Hash each permanent note → if upstream candidates didn't change AND the note didn't change since last run, skip
- Net effect: weekly runs that touch only the new batch finish in seconds instead of minutes

### P8 — Automatic MOC + concept-graph generation

`auto_moc_generator.py` is in the directory but I didn't see it wired into `pipeline_v2`. Add as Stage 7.5:
- Per top-level `domain:` field, generate a Map of Content listing all notes
- Per `subdomain:` cluster ≥ 5 notes, generate a sub-MOC
- Compute and embed a Mermaid graph of strongest 20 concept-to-concept links per MOC

### P9 — Quality scorer in feedback loop

note_quality_scorer.py produces 0–100 scores but isn't enforced anywhere. Wire it in:
- After build, score every newly-touched note
- Notes scoring < 40 → emit to `_pipeline-output/low-quality-notes-<timestamp>.md` with specific deficits
- Optionally route to LLM enrichment pass (P6)
- Track trend: average note quality across runs → store in `_pipeline-output/quality-trend.csv`

### P10 — Note aesthetics

Concrete rendering improvements before you rebuild 1000+ notes:

- **Single H1 = title** (already done) — but add an immediate `> [!abstract]` synthesis directly under, before any other section. Gives the note a "hook" when previewed
- **Replace `*Source: ...*` italics with proper `> [!cite]` callouts** — visually consistent
- **Inline source attribution** on every callout (`(from [[report]])`) is currently text — convert to a small footer block per section: `**Sources:** [[r1]] · [[r2]] · [[r3]]`. Less visual noise per callout
- **Use Dataview inline fields** for definitions: `[**Definition**:: ...]` instead of (or in addition to) the `> [!definition]` callout — makes them queryable
- **Add a `## See Also` graph block** at the bottom: a Dataview query that auto-lists notes with shared `domain` + at least 2 shared wiki-link neighbors. Self-maintaining "related" section

---

## 3. Suggested Architecture for v3

If you want to fully restructure rather than incrementally patch, here's the shape I'd recommend:

```
Stage 0: Pre-flight (existing)
Stage 1: Extract → JSON                     [parallel, regex hardened by P0]
Stage 2: Consolidate                        [P1 — merge candidates across batches]
Stage 3: LLM-normalize concepts             [P5 — local Qwen2.5-7B, structured output]
Stage 4: Embed-and-match                    [P4 — bge-small embeddings + difflib hybrid]
Stage 5: Build notes (slim template)        [P2 — conditional sections]
Stage 5b: Optional LLM synthesis            [P6 — opt-in flag]
Stage 6: Stubs (only for high-ref non-garbage targets)
Stage 7: Resolve report wiki-links (existing)
Stage 8: Normalise wiki-links (existing)
Stage 9: Audit + quality scoring            [P9 — score gates]
Stage 10: MOC + concept-graph build         [P8]
Stage 11: Index + report + commit (existing)
```

---

## 4. Recommended Next Step

Pick one of these to start (I can execute any of them):

1. **Quick win:** P0 + P3 (garbage-link fix + parallelism). 1 day. Probably gives 90%+ of the perceived improvement before any LLM work.
2. **Aesthetic rebuild:** P2 + P10 + delete & rebuild all notes with the new template. Also 1 day. Best if you want to *see* the difference fast.
3. **Full LLM augmentation:** P4 + P5. 2–3 days. Builds the embedding cache + sets up local Qwen2.5-7B inference. Sets the foundation for P6 and beyond.
4. **Full v3:** Spec + sequenced rollout of P0→P10. I'd write a phased migration plan first, then execute in order.

Which direction do you want to take? Or should I start with #1 (highest ROI, no architectural commitment) and we can layer the LLM stuff on top once the regex pipeline is clean? 


---
---















## V3 Pipeline Improvement and LLM Capacity

### Key Locations

`D:\10_pur3v4d3r's-vault\99-scripts\report-extraction-to-permanent-notes-building-v3` -> Home of all of V3 pipeline
`D:\10_pur3v4d3r's-vault\99-scripts\report-extraction-to-permanent-notes-building-v3\00-master-spec.md` -> The master spec for the V3 pipeline, including detailed breakdowns of each stage, proposed improvements, and LLM integration points.
`D:\10_pur3v4d3r's-vault\99-scripts\report-extraction-to-permanent-notes-building-v3\README.md` -> Overview and usage instructions for the V3 pipeline
`D:\10_pur3v4d3r's-vault\999-report-organizing\__pur3v4d3r-house-voice-reports` -> Reports to test the pipeline on. These are the same reports that were used in the V2 pipeline, ensuring consistency in testing and comparison.

These are things I would like to incorperate into the pipeliune, in order of priority and impact:

### P1 — Vector-based fuzzy matcher (LOCAL LLM, RTX 4090) — high impact

This is where the GPU starts to earn its keep. Replace `difflib.SequenceMatcher` with **sentence embeddings + cosine similarity** in note_matcher.py.

**Why it matters:**
- Catches `Achievement-Goal-Theory` ↔ `Achievement-Goal-Framework` (paraphrase)
- Catches `SDT` ↔ `Self-Determination Theory` (acronym/expansion)
- Catches `Cognitive Load Theory (Sweller)` ↔ `Sweller Cognitive Load` (reordering)
- Catches `Working Memory Capacity` ↔ `Span of Apprehension` (synonyms)

**Stack:**
- `sentence-transformers` with **`BAAI/bge-small-en-v1.5`** (~33M params, 384-dim, runs in ~50ms/batch on 4090, 90%+ recall on STS benchmarks)
- Pre-compute embeddings for all 1094 existing notes' `(stem, title, aliases)` once → cache in `_pipeline-output/notes_embeddings.npz`
- Invalidate cache by `(filepath, mtime)` per note — only re-embed changed notes
- Hybrid scoring: `0.4 * difflib + 0.6 * cosine_sim` (string sim guards against pure-semantic false positives like `Growth Mindset` ↔ `Growth Hacking`)
- Two thresholds preserved: ≥0.92 auto-match, 0.80–0.92 review queue, <0.80 = new note


ollama pull qwen2.5:7b-instruct-q5_K_M

### P2 — LLM-assisted concept extraction & cleanup (LOCAL LLM, RTX 4090)

Two specific places where small local LLMs dramatically outperform regex:

**2a. Callout title parsing** (`report_parser.parse_definition_title`)
The regex parser handles `"Concept** (Domain — Author, Year)"` but breaks on natural variations. A 3B–8B model can extract structured fields from messy titles with near-100% accuracy.

**2b. Concept normalization & alias mining**
Run a one-shot pass that, for each candidate concept, asks: "Give me the canonical name + 3-5 aliases + 1-line definition + parent domain." Stack:
- **Qwen2.5-7B-Instruct** or **Llama-3.1-8B-Instruct** via `vllm` or `llama.cpp` w/ Q5_K_M GGUF — both fit in 24GB VRAM with ~6K context
- Batch 32 concepts per request → ~2–3s per batch on 4090
- Use **structured output** (JSON schema with `outlines` or `lm-format-enforcer`) to guarantee parseable results
- Cache responses keyed by concept-name hash → idempotent re-runs are free

This gives you **(a)** higher-quality aliases (the audit shows aliases are sparsely populated), **(b)** automatic disambiguation suggestions for the review queue, and **(c)** stub bodies that aren't empty.


### P3 — LLM-summarized "Core Explanation" (LOCAL LLM, optional)

When a concept has 5+ pieces of evidence/insight scattered across reports, the current builder concatenates them as a list of callouts. Optionally, run a synthesis pass: "Given these 8 evidence/insight callouts about [Concept], write a 150-word integrated `## Synthesis` section that preserves all distinct claims and cites the source reports."

Adds at top of note. Original callouts stay below as the receipt. **Toggle behind `--llm-synthesize` flag** so it's opt-in per run.



### P4 — Automatic MOC + concept-graph generation

`auto_moc_generator.py` is in the directory but I didn't see it wired into `pipeline_v2`. Add as Stage 7.5:
- Per top-level `domain:` field, generate a Map of Content listing all notes
- Per `subdomain:` cluster ≥ 5 notes, generate a sub-MOC
- Compute and embed a Mermaid graph of strongest 20 concept-to-concept links per MOC




















Develop a workflow for turning the vast neumber of permanent notes stubs into full fledge permanent notes.
- using local llm
- adding information, like definition callouit and such.






I have a pipeline that extracts concepts from reports and creates permanent note stubs in Obsidian. The stubs have basic metadata but lack detailed content. I want to use a local LLM (like Qwen2.5-7B-Instruct) to enrich these stubs into full-fledged permanent notes.
- The LLM should generate content for sections like "Core Explanation," "Practical Implications," "Key Figures," etc., based on the metadata and any available evidence or insights.
- The workflow should be efficient, allowing me to process batches of stubs and update them in Obsidian without manual copy-pasting.
- I also want to ensure that the generated content is accurate and well-structured, so the LLM should be guided by a clear prompt template that includes the necessary context for each note.
- The final output should be a set of enriched permanent notes in Obsidian, each with comprehensive content that goes beyond the initial stub information.

---

I have a pipeline that extracts concepts from reports and creates permanent note stubs in Obsidian.

---


I have extracted and generated 2000+ permanent note stubs in Obsidian using a custom pipeline. 

I need to consolidate the number of permanent notes as much as possible, by merging stubs that refer to the same concept but were created from different reports.
- I want to use a local LLM (like Qwen2.5-7B-Instruct) to assist in identifying which stubs can be merged based on their metadata and any available evidence or insights.
- The LLM should analyze the content of the stubs, including their titles, metadata,and any associated evidence or insights, to determine if they refer to the same underlying concept.
- The workflow should allow me to review the LLM's suggestions for merging stubs, providing a clear interface for accepting or rejecting each suggestion.
- Once stubs are merged, the resulting permanent note should combine the metadata and content from the original stubs, ensuring that no valuable information is lost in the consolidation process.
- The final output should be a more concise set of permanent notes in Obsidian, with merged content where appropriate, while maintaining the integrity and richness of the information extracted from the reports.
- The goal is to reduce redundancy in the permanent notes while preserving the depth and breadth of information, ultimately creating a more organized and efficient knowledge base in Obsidian.
 Need a plan for cobining the stubs that refer to the same concept but were created from different reports, using a local LLM to assist in identifying which stubs can be merged based on their metadata and any available evidence or insights.
- The new combined notes should have wikilinks to all the source reports and should preserve all the insights and evidence from the original stubs.
I have ollama running locally with Qwen2.5-7B-Instruct, which I can use to analyze the stubs and suggest merges based on their content and metadata. I want to create a workflow that allows me to efficiently review the LLM's suggestions and merge stubs in Obsidian while preserving all relevant information.

---










