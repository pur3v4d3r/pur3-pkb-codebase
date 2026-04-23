












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








---

I have a pipeline that extracts concepts from reports and creates permanent note stubs in Obsidian.

---

# Adding to Permanent Notes with Local LLM

I have a pipeline that extracts concepts from reports and creates permanent note stubs in Obsidian. The stubs have basic metadata but lack detailed content. I want to use a local LLM (like Qwen2.5-7B-Instruct) to enrich these stubs into full-fledged permanent notes.
- First what needs to be done is a slimming down opf the amount of concept that are in this folder: `D:\00-inbox\v3-pipeline-permanet-note-leftovers\v3-pipeline-permanent-notes` -> Cuyrrentley there are 1200+ stubs, but many are duplicates or low-quality. I want to filter down to a more manageable set of ~200 high-potential stubs for enrichment.
- Then, I want to design a workflow for taking these stubs and enriching them with content generated by the local LLM. This would involve creating a structured prompt that provides the LLM with the necessary context from the stub's metadata and any available evidence, and then using the LLM's output to fill in sections of the permanent note such as the definition callout, core explanation, practical implications, key figures, etc.
- The active permanent notes can be fiound here: `D:\10_pur3v4d3r's-vault\999-report-organizing\_permanent-notes\llm-generated-permanent-notes` -> The new permanent notesneed to match the format of the original permanent notes found here.
- I have a script/python file that can be used to automate the enrichment process, which will take the stubs, generate content using the LLM, and then update the permanent notes in Obsidian accordingly. The script should also handle caching of LLM responses to avoid redundant calls and ensure efficient processing. Found here: `D:\10_pur3v4d3r's-vault\99-scripts\report-extraction-to-permanent-notes-building-v3\enrich_stubs.py` -> Use this script after we have consolidated or chossen which permanent notes from `D:\00-inbox\v3-pipeline-permanet-note-leftovers\v3-pipeline-permanent-notes` to enrich.
- The final output should be a set of enriched permanent notes in Obsidian, each with comprehensive content that goes beyond the initial stub information. The enriched notes should be well-structured, accurate, and provide valuable insights based on the original metadata and any available evidence.

---


# Report -> Permanent Note Workflow using Lacoal LLM

I have a workflow for extracting permanent note material from previously generated academic reports.
I want to take aspects from that pipeline and develop V4 of the pipeline that can extract material for permanent notes and then have the Local LLM review the information and format it into a more condensed and well developed permanent note format. Which I have already constructed.
 - The pipeline creates JSON files that contain all the extracted information, I theorizing that the local LLM can take that JSON file as input and then generate a markdown file that is formatted according to the permanent note format I have been using in Obsidian. This would involve creating a prompt for the LLM that instructs it on how to structure the markdown file, what sections to include, and how to summarize the information from the JSON file effectively.
- The LLM would need to be guided by a clear prompt template that includes the necessary context for each note, such as the title, domain, existing links, and any relevant metadata. The prompt should also specify the required sections for the permanent note, such as the definition callout, core explanation, practical implications, key figures, related concepts, and any open questions or tensions.
- The workflow should be efficient, allowing for batch processing of multiple stubs and updating them in Obsidian without manual copy-pasting. This could involve writing a script that iterates through the JSON files, calls the LLM to generate the markdown content, and then writes the output directly to the appropriate location in the Obsidian vault. The script should also handle any necessary frontmatter updates to reflect the enriched status of the notes and ensure that the metadata is accurate and up-to-date.





























# Permanent Note Enrichment Workflow


I have a pipeline that extracts concepts from reports and creates permanent note stubs in Obsidian. The stubs have basic metadata but lack detailed content. I want to use a local LLM (like Qwen2.5-7B-Instruct) to enrich these stubs into full-fledged permanent notes.

Each permanent note has a definition callout at the top, which MUST be filled, this is the main point.
- The LLM should generate content for sections like "Core Explanation," "Practical Implications," "Key Figures," etc., based on the metadata and any available evidence or insights.
- The workflow should be efficient, allowing me to process batches of stubs and update them in Obsidian without manual copy-pasting.
- I also want to ensure that the generated content is accurate and well-structured, so the LLM should be guided by a clear prompt template that includes the necessary context for each note.
- The final output should be a set of enriched permanent notes in Obsidian, each with comprehensive content that goes beyond the initial stub information.



Ready for review
Select text to add comments on the plan
Plan: Stub Enrichment Pipeline (enrich_stubs.py)
Context
The v3 extraction pipeline creates permanent note stubs — either status: stub (v3 format) or maturity: seedling with an empty body (older format). These stubs have valid frontmatter but no meaningful content. The goal is a standalone script that calls Qwen2.5-7B-Instruct via Ollama to enrich each stub into a full permanent note, with the [!definition] callout as the mandatory primary output.

Target File
d:\10_pur3v4d3r's-vault\99-scripts\report-extraction-to-permanent-notes-building-v3\enrich_stubs.py
No new modules or directories are needed.

Critical Files to Read Before Implementing
File	Why
lib/llm_client.py	OllamaClient.chat_json() signature, exception types, content_hash()
lib/frontmatter.py	parse_frontmatter(text) → (dict, str), render_frontmatter(data) → str
lib/markdown.py	callout(type, title, body), join_wikilinks(targets), safe_filename(name)
config_v3.py	VAULT_ROOT, OLLAMA_URL, LLM_MODEL_SYNTHESIZE, LLM_CACHE_DIR
stages/s4_normalize.py	Canonical pattern for LLM call + pydantic schema + error handling
Stub Detection Logic
Two stub populations to scan:

v3 pipeline stubs:   VAULT_ROOT/999-report-organizing/_permanent-notes/v3-pipeline-permanent-notes/
Older seedling notes: VAULT_ROOT/03-notes/01_permanent-notes/
A note qualifies as a stub if ANY condition is true:

status == "stub" (v3 pipeline stubs)
status == "seedling" AND body length < 50 chars after stripping the placeholder callout
maturity == "seedling" AND body is effectively empty (no H2 sections, no filled callouts)
Skip notes where status in ("enriched", "budding", "evergreen") — already processed.

Pydantic Schema
class EnrichmentResponse(BaseModel):
    definition: str              # REQUIRED — 1-2 sentences. Hard-required by validator.
    core_explanation: list[str]  # 3-5 paragraphs
    practical_implications: list[str]  # 2-3 items
    key_figures: list[str] = []        # optional, names only
    related_concepts: list[str] = []   # 3-8 concept names (plain strings, not wiki-links)
    tensions_or_questions: list[str] = []  # optional open questions
    domain: str | None = None          # corrected domain, or None if current is correct

    @field_validator("definition")
    def definition_not_empty(cls, v): ...  # raise if blank
Cache key includes PROMPT_CONTRACT_VERSION = "enrich-v1" so bumping it invalidates old cache.

Prompt Design
System prompt — scholarly, JSON-only, no hallucination:

You are a knowledgeable academic knowledge base author. Enrich a stub note from a Personal
Knowledge Base (PKB). Write accurate, concise content. Neutral scholarly tone. No invented
citations or biographical claims — omit uncertain claims rather than guess. Reply with valid
JSON only — no markdown fences, no preamble.
User prompt — structured, includes all available context:

Enriching stub: {title!r}
Domain: {domain} | Type: {note_type} | Aliases: {aliases}
Existing links: {existing_links}
{context_block}   ← includes referenced_by, existing body text, source_reports

Return JSON with fields: definition (REQUIRED), core_explanation (list),
practical_implications (list), key_figures (list), related_concepts (list),
tensions_or_questions (list), domain (optional corrected label).

Rules: definition MUST NOT be empty. Arrays may be empty but must exist.
Do not include {title!r} in related_concepts. JSON only, no fences.
Context block priority: referenced_by links → existing body text (≤600 chars) → source_reports. If nothing available: "(No additional context available.)".

Body Assembly
Sections emitted in order using lib.markdown.callout():

# {title}

> [!definition] {title}
> - **Key-Term**: [[{title}]]
> - **Definition**: {r.definition}
> - **Domain**: {domain}
> - **Status**: 🌱 budding | Confidence: speculative

## Core Explanation
> [!analytical-insight] ...  (one callout per paragraph)

## Practical Implications
> [!example] Application ...

## Key Figures                    (only if r.key_figures non-empty)
> [!person] {name} ...

## Open Threads                   (only if r.tensions_or_questions non-empty)
> [!open-question] Question ...

## Connections
**Related:** [[Concept A]] · [[Concept B]]   (via join_wikilinks)

---
**Sources:** [[report1]] · [[report2]]       (from stub frontmatter)
Frontmatter Updates
Only modify these fields — preserve everything else:

Field	Change
status	stub / seedling / active → "enriched"
maturity	seedling → "budding"
mastery-stage	seedling → "budding" (v3 format)
domain	corrected only if response provides non-null and current is "other"/"uncategorized"/""
updated	today's ISO date
provenance.enrichment-method	"enrich_stubs-v1"
provenance.enrichment-model	config_v3.LLM_MODEL_SYNTHESIZE
Use parse_frontmatter(text) → (dict, body) and render_frontmatter(updated_dict) → str.

File Write Strategy
In-place (default): atomic .tmp → replace() pattern from existing codebase:

tmp = path.with_suffix(".md.tmp")
tmp.write_text(content, encoding="utf-8")
tmp.replace(path)  # atomic on same filesystem
Output-dir mode (--output-dir PATH): mirrors input directory tree. Original files untouched. Useful for diff-before-commit workflows.

CLI Interface
python enrich_stubs.py [options]

Options:
  --input-dir PATH     Scan directory (repeatable). Default: both stub dirs.
  --output-dir PATH    Write enriched notes here instead of in-place.
  --dry-run / -n       Run LLM calls + cache, but write no files.
                       Prints a body preview for the first stub.
  --limit N            Process only first N stubs.
  --bypass-cache       Force live LLM calls, ignore cached responses.
  --model MODEL        Ollama model ID (default: from config_v3).
  --strict             Exit non-zero if any enrichment fails.
  -v / -q              Verbosity / quiet.
Processing Loop
Sequential (Ollama is single-tenant — concurrency queues up anyway):

for each stub:
    1. enrich_stub(stub, client) → EnrichmentResult   # LLM call + schema validation
    2. if ok:
         body = build_enriched_body(stub, result.response)
         fm   = update_frontmatter(stub.raw_frontmatter, result.response)
         content = render_frontmatter(fm) + "\n\n" + body
         if not dry_run: write_note_atomic(dest_path, content)
    3. else: log warning, continue
Rich progress bar (via rich.progress) with title preview + counter.

Error Handling
Failure	Behavior
OllamaUnavailableError on startup ping	Exit code 6, no files touched
StructuredOutputError (blank definition)	Log warning, skip stub, continue
LLMError (retries exhausted)	Log warning, skip stub, continue
OSError on write	Log error, count as failed, continue
KeyboardInterrupt	Flush progress, exit 130 (already-written files are safe)
--strict flag	Non-zero exit if any failures
Exit codes: 0=success, 1=uncaught, 2=bad args, 4=no stubs found, 5=failures (strict), 6=Ollama down.

Internal Structure
enrich_stubs.py
├── CONSTANTS: PROMPT_CONTRACT_VERSION, DEFAULT_SEARCH_DIRS, SYSTEM_PROMPT, USER_PROMPT_TEMPLATE
├── EnrichmentResponse (pydantic BaseModel)
├── StubNote (frozen dataclass: path, title, domain, type, status, maturity, aliases,
│                               source_reports, referenced_by, body_text, raw_frontmatter)
├── EnrichmentResult (frozen dataclass: stub, ok, cached, response, error)
├── is_stub(fm, body) → bool
├── _already_enriched(fm) → bool
├── scan_stubs(dirs, *, skip_enriched, limit) → list[StubNote]
├── _try_parse_stub(path) → StubNote | None
├── _build_context_block(stub) → str
├── _build_user_prompt(stub) → str
├── enrich_stub(stub, client, *, model, bypass_cache) → EnrichmentResult
├── build_enriched_body(stub, response) → str
├── update_frontmatter(fm, response) → dict
├── write_note_atomic(path, content) → None
├── enrich_all(stubs, client, *, ...) → (list[EnrichmentResult], stats_dict)
├── build_parser() → ArgumentParser
└── main(argv) → int
Verification
# 1. Dry run — preview 3 stubs, no writes
python enrich_stubs.py --dry-run --limit 3

# 2. Safe preview — write to output dir, diff against originals
python enrich_stubs.py --limit 20 --output-dir D:/enrichment-preview

# 3. In-place — enrich 50 stubs for real
python enrich_stubs.py --limit 50

# 4. Full run — all stubs, strict mode
python enrich_stubs.py --strict
Inspect one output note: verify [!definition] callout is filled, status: enriched, maturity: budding, and at least one ## Core Explanation section exists.

Add Comment



- **Note Merger** — Merge two or more notes into a single file, resolving duplicate headings.
- **Note Stub Promoter** — Find all notes that only contain a title + frontmatter and flag them for development.
- **Folder README Generator** — Auto-generate a `README.md` index for each folder listing all notes within it.
- **File Content Analyzer** — Analyze the content of files in a directory for specific patterns, keywords, or sentiment.
- **Directory Watcher** — Watch a directory for changes and trigger actions when files are added, modified, or deleted.
- **Duplicate File Finder** — Find duplicate files in a directory based on file content or name.
- **Link Graph Exporter (JSON/CSV)** — Export the vault's link graph as a node-edge CSV or JSON for Gephi / D3.js.
- **Metadata Inheritance Injector** — Apply default frontmatter fields to all notes in a folder, inheriting from a folder-level config.
- **Bulk File Renamer (Regex)** — Rename files in bulk using regex patterns with dry-run preview.

- **PDF Page Extractor / Merger / Splitter** — Manipulate PDFs with `pypdf` or `pdfplumber`.
- **OCR Bulk Extractor** — Extract text from scanned PDFs and images with `pytesseract`.







python 99-scripts/wikipedia_downloader.py --url "https://en.wikipedia.org/wiki/John_Dewey" "--no-links" "--output" "D:\10_pur3v4d3r's-vault\999-report-organizing\wikipedia"

python 99-scripts/wikipedia_downloader.py "https://en.wikipedia.org/wiki/John_Dewey" --no-links --output "D:\10_pur3v4d3r's-vault\999-report-organizing\wikipedia"


python 99-scripts/wikipedia_downloader.py --url "https://en.wikipedia.org/wiki/Maslow%27s_hierarchy_of_needs" --no-links --no-prompt --output "D:\10_pur3v4d3r's-vault\999-report-organizing\wikipedia"

python 99-scripts/wikipedia_downloader.py "https://en.wikipedia.org/wiki/Pragmatism" --no-references --no-links --no-prompt --output "D:\10_pur3v4d3r's-vault\999-report-organizing\wikipedia"






# MOC Develpment Workflow

I have a series of permanent notes that have been extracted from reports but are currently unlinked and not organized into any Map of Content (MOC). I want to develop a workflow for taking these standalone notes and integrating them into a coherent MOC structure within Obsidian.
- The workflow should involve identifying thematic clusters among the notes, creating MOC files that link to these notes, and establishing a hierarchical structure that reflects the relationships between concepts.

`D:\10_pur3v4d3r's-vault\wiki-link-permanent-note-names-2026-03-19.md` -> A reference file that lists all permanent notes with their canonical names and wiki-link formats. This can be used to ensure consistency when linking notes in MOCs.
`D:\10_pur3v4d3r's-vault\999-report-organizing\_permanent-notes\llm-generated-permanent-notes` -> This directory contains all the permanent notes that have been generated from the report extraction pipeline. These are the notes that need to be organized into MOCs.

`D:\10_pur3v4d3r's-vault\999-report-organizing\_maps-of-content-for-permenent-notes` -> USE THIS DIRECTORY TO STORE ALL GENERATED MOCs. This keeps them organized and separate from individual notes.