# Synthetic Permanent-Note Seeds — Workflow README

> **Purpose.** Generate `*_extracted.json` files **without writing an Academic Report first**, then feed them into the V6 Outline→Elaborate pipeline to densify the wiki-link graph in `999-report-organizing/_permanent-notes/v6-llm-elaborated/`.
>
> **Audience.** Both **the human operator** (PKB owner) and **the LLM agent** (`permanent-note-seed-agent-v1.0.0`) that drafts seed content.

---

## 1. What this workflow replaces

The standard pipeline is:

```
Academic Report (.md)
  → V4/V5/V6 extractor (mines callouts → *_extracted.json)
    → V6 pipeline (Outline → Elaborate via LLM)
      → permanent note (.md)  in  999-report-organizing/_permanent-notes/v6-llm-elaborated/
```

This workflow short-circuits the first arrow:

```
Concept brief (.yaml)
  → synth_seed_builder.py build           ← THIS WORKFLOW
    → *_extracted.json (synthetic seed)
      → V6 pipeline (Outline → Elaborate via LLM)
        → permanent note (.md)
```

Use it when you want a permanent note for a concept you **don't** want to write a full academic report for first — typically to fill in [[wiki-link]] targets that other notes already reference.

---

## 2. Directory map

```
99-scripts/synthetic-permanent-note-seeds/
├── README.md                         ← this file
├── SYNTHETIC_BUNDLE_SCHEMA.md        ← narrative contract (read before writing briefs)
├── synthetic_bundle.schema.json      ← machine-checkable JSON Schema (Draft 2020-12)
├── synth_seed_builder.py             ← CLI: `build` (brief → seed) and `validate`
├── test_synth_seed_builder.py        ← pytest companion (29 tests)
├── expand_term_list.py               ← CLI: `expand` / `build-batch` / `run` (term list → briefs → seeds)
├── test_expand_term_list.py          ← pytest companion (32 tests)
├── TERM_LIST_FORMAT.md               ← spec for the markdown term-list format (List Mode)
├── term-lists/
│   └── 2026-04-24-retrieval-practice-cluster.md   ← reference exemplar
└── briefs/
    ├── spaced-retrieval.yaml         ← single-brief reference exemplar
    ├── desirable-difficulties.yaml
    ├── interleaving.yaml
    └── <batch-name>/
        ├── manifest.json             ← written by `expand_term_list.py expand`
        └── *.yaml                    ← one brief per accepted term

.github/agents/
└── permanent-note-seed-agent-v1.0.0.md   ← LLM system prompt for drafting briefs/seeds

999-report-organizing/_extractor-output/_synthetic-seeds/
└── <YYYY-MM-DD>-<batch-name>/        ← generated *_extracted.json files land here
```

---

## 3. Quickstart (5-minute path, human operator)

```bash
# 1. Activate venv
cd "d:\10_pur3v4d3r's-vault"
source .venv/Scripts/activate         # Git Bash on Windows

# 2. Move into the workflow dir
cd 99-scripts/synthetic-permanent-note-seeds

# 3. Sanity check: tests should pass
python -m pytest test_synth_seed_builder.py -v          # expect: 29 passed

# 4. Copy an exemplar brief and edit it
cp briefs/spaced-retrieval.yaml briefs/my-new-concept.yaml
$EDITOR briefs/my-new-concept.yaml

# 5. Build the synthetic seed
python synth_seed_builder.py -v build briefs/my-new-concept.yaml \
    --out-dir "d:/10_pur3v4d3r's-vault/999-report-organizing/_extractor-output/_synthetic-seeds/2026-04-24-my-batch"

# 6. Validate the batch (always do this before running V6)
python synth_seed_builder.py validate \
    "d:/10_pur3v4d3r's-vault/999-report-organizing/_extractor-output/_synthetic-seeds/2026-04-24-my-batch"
# expect: "X file(s), 0 with errors, 0 error(s), 0 warning(s)"

# 7. Run V6 elaboration (LLM, slow — Ollama must be running)
cd ../report-extraction-to-permanent-notes-building-v6
python pipeline_v6.py \
    --input-dir "d:/10_pur3v4d3r's-vault/999-report-organizing/_extractor-output/_synthetic-seeds/2026-04-24-my-batch" \
    --report-runs "runs/2026-04-24-my-batch-log.json"

# 8. Inspect output
ls "d:/10_pur3v4d3r's-vault/999-report-organizing/_permanent-notes/v6-llm-elaborated/"
```

---

## 4. The seed builder CLI (`synth_seed_builder.py`)

### 4.1 Subcommands

| Subcommand  | Purpose                                                     |
|-------------|-------------------------------------------------------------|
| `build`     | Read a YAML brief → produce one `*_extracted.json` seed     |
| `validate`  | Validate one file or every `*_extracted.json` under a dir   |

### 4.2 Global flags (must come **before** the subcommand)

```
python synth_seed_builder.py [-h] [--version] [-v] [-q] [--schema SCHEMA] COMMAND ...
```

| Flag             | Meaning                                                       |
|------------------|---------------------------------------------------------------|
| `-h`, `--help`   | Show help and exit                                            |
| `--version`      | Print version (`1.0.0`) and exit                              |
| `-v`, `--verbose`| Enable INFO-level logging (repeatable for DEBUG)              |
| `-q`, `--quiet`  | Suppress non-error output                                     |
| `--schema PATH`  | Override the JSON Schema location (defaults next to script)   |

> **CRITICAL — flag ordering.** Argparse subparsers require global flags **before** the subcommand. `python synth_seed_builder.py build foo.yaml -v` will fail with `unrecognized arguments: -v`. Use `python synth_seed_builder.py -v build foo.yaml`.

### 4.3 `build` subcommand

```bash
python synth_seed_builder.py [-v] build BRIEF [--out-dir DIR] [--filename NAME] [-n] [--overwrite]
```

| Argument          | Required | Description                                                                |
|-------------------|----------|----------------------------------------------------------------------------|
| `BRIEF`           | yes      | Path to a YAML brief file                                                  |
| `--out-dir DIR`   | no       | Output directory (default: cwd). Created if missing.                       |
| `--filename NAME` | no       | Override generated filename. Default: `<concept-kebab>-synthetic-seed-<YYYY-MM-DD>_extracted.json` |
| `-n`, `--dry-run` | no       | Build in-memory, validate, print where it *would* write — no file written  |
| `--overwrite`     | no       | Replace an existing file at the target path (default: refuse)              |

### 4.4 `validate` subcommand

```bash
python synth_seed_builder.py validate PATH [PATH ...]
```

- Each `PATH` is either a single `*_extracted.json` file or a directory (recursively scanned for `*_extracted.json`).
- Validates against: JSON Schema, V4 substring discipline, filename hygiene, kebab-case domain.
- Exit code `0` on clean batch; `4` if any file has errors.

### 4.5 Exit codes

| Code | Meaning                                |
|------|----------------------------------------|
| 0    | Success                                |
| 1    | Uncaught error                         |
| 2    | Input file/path not found              |
| 4    | Validation failure (errors present)    |
| 5    | Brief malformed (missing required key) |
| 130  | Interrupted (Ctrl+C)                   |

---

## 5. Authoring a brief (YAML format)

Briefs are the human-readable input. The schema is intentionally minimal so a human or an LLM agent can produce one in a few minutes.

### 5.1 Minimum required keys

```yaml
concept: "<Title Case Concept Name>"   # REQUIRED
domain: "kebab-case-domain"            # REQUIRED
callouts:                              # REQUIRED — at least one `definition`
  - type: "definition"
    title: "<must contain the concept name>"
    body: |
      <prose with embedded [[wiki-links]]>
```

### 5.2 Full brief structure (recommended)

```yaml
# ─── Identity ─────────────────────────────────────────────────────────
concept: "Spaced Retrieval"
domain: "cognitive-science"
secondary_domains: ["learning-science", "memory-research"]
aliases: ["Spaced Retrieval Practice"]

# ─── Graph links ──────────────────────────────────────────────────────
broader: ["retrieval-practice"]
narrower: ["expanding-retrieval"]
related: ["testing-effect", "desirable-difficulties"]
prerequisites: ["long-term-memory", "working-memory"]

# ─── Provenance ───────────────────────────────────────────────────────
confidence: "high"     # one of: low | medium | high

# ─── Callouts (the meat) ──────────────────────────────────────────────
callouts:
  - type: "definition"               # exactly 1 required (V4 mines this)
    title: "Spaced Retrieval"        # MUST contain "Spaced Retrieval"
    body: |
      <prose, may include [[wiki-links]]>

  - type: "key-claim"                # 1-2 recommended
    title: "Spaced Retrieval scales with the spacing interval"
    body: |
      ...

  - type: "key-distinction"          # 1 recommended
    title: "Spaced Retrieval vs. Distributed Re-reading"
    body: |
      ...

  - type: "example"                  # 1-2 recommended
    title: "Vocabulary acquisition with expanding intervals"
    body: |
      ...

  - type: "warning"                  # 0-1 recommended
    title: "Spacing without retrieval is not Spaced Retrieval"
    body: |
      ...

  - type: "claude-insight"           # 0-1 optional
    title: "Spaced Retrieval observation"
    body: |
      ...
```

### 5.3 The substring rule (V4 enforcement — non-negotiable)

> **Every support callout's `title` OR `body` MUST contain the cleaned concept title (case-insensitive substring).**

V4's `_gather_support()` silently drops any callout whose title and body both fail this check. `synth_seed_builder.py validate` will catch violations with a clear error before V6 ever sees the seed.

**Cleaning rules** (mirror V4 `_clean_title`):
- `[[Spaced Retrieval]]` → `Spaced Retrieval`
- `Spaced Retrieval (Bjork, 1994)` → `Spaced Retrieval`
- `Spaced Retrieval — a memory technique` → `Spaced Retrieval`
- Whitespace trimmed; titles 3-80 chars

### 5.4 Recommended composition

| Callout type      | Count | Required? |
|-------------------|-------|-----------|
| `definition`      | 1     | **YES**   |
| `key-claim`       | 1-2   | recommended |
| `key-distinction` | 1     | recommended |
| `example`         | 1-2   | recommended |
| `warning`         | 0-1   | optional  |
| `claude-insight`  | 0-1   | optional  |
| **Total**         | 4-8   | hard cap at 8 (V4 `MAX_SUPPORT_CALLOUTS`) |

### 5.5 Wiki-link strategy

Embed **5-12** `[[wiki-link]]` targets across the callout bodies, drawn from:
- the `broader`, `narrower`, `related`, `prerequisites` lists in the brief
- pre-existing notes in the vault (check via `vscan`)
- intentional ghost links to concepts you'll seed next

The point of this workflow is graph density — under-linking defeats the purpose.

---

## 6. End-to-end example (the smoke batch)

This is the canonical reference run. Reproduce it any time to confirm the pipeline is healthy.

```bash
cd "d:\10_pur3v4d3r's-vault\99-scripts\synthetic-permanent-note-seeds"

# Build all 3 reference seeds
for brief in spaced-retrieval desirable-difficulties interleaving; do
    python synth_seed_builder.py -v build "briefs/${brief}.yaml" \
        --out-dir "d:/10_pur3v4d3r's-vault/999-report-organizing/_extractor-output/_synthetic-seeds/2026-04-24-smoke-batch" \
        --overwrite
done

# Validate
python synth_seed_builder.py validate \
    "d:/10_pur3v4d3r's-vault/999-report-organizing/_extractor-output/_synthetic-seeds/2026-04-24-smoke-batch"
# expect: 3 file(s), 0 with errors, 0 error(s), 0 warning(s)

# Confirm V4 mines exactly 3 bundles (no LLM call)
cd "d:\10_pur3v4d3r's-vault"
python -c "
import sys, json
from pathlib import Path
sys.path.insert(0, r'99-scripts/report-extraction-to-permanent-notes-building-v4')
from pipeline_v4 import build_bundles

batch = Path(r'999-report-organizing/_extractor-output/_synthetic-seeds/2026-04-24-smoke-batch')
total = 0
for f in sorted(batch.glob('*_extracted.json')):
    payload = json.loads(f.read_text(encoding='utf-8'))
    bundles = build_bundles(payload, report_stem=f.stem, include_key_claims=False)
    total += len(bundles)
    print(f'{f.name}: {len(bundles)} bundle(s), support={[len(b.support) for b in bundles]}')
print(f'TOTAL: {total} bundles')
"
# expect: 3 bundles, support=[5] each

# Run V6 (LLM elaboration — slow, requires Ollama at 127.0.0.1:11434)
cd "99-scripts/report-extraction-to-permanent-notes-building-v6"
python pipeline_v6.py \
    --input-dir "d:/10_pur3v4d3r's-vault/999-report-organizing/_extractor-output/_synthetic-seeds/2026-04-24-smoke-batch" \
    --report-runs "runs/2026-04-24-smoke-v6-log.json"
```

---

## 7. Troubleshooting

| Symptom                                                             | Cause / Fix                                                                                          |
|---------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| `unrecognized arguments: -v`                                        | `-v` placed after subcommand. Move it: `synth_seed_builder.py -v build ...`                          |
| Validation: `support callout 'X' violates substring rule`           | The support callout's title and body both lack the concept name. Add the name to one of them.        |
| Validation: `bad filename — must match <concept-kebab>-synthetic-seed-YYYY-MM-DD_extracted.json` | Don't rename generated seeds. Re-run `build` if you need a different name.                             |
| `pyyaml` / `jsonschema` ImportError                                 | `pip install pyyaml jsonschema` (already in the venv on this machine)                                |
| V6 mines 0 bundles                                                  | Definition callout title fails the cleaned-title test. Check title length 3-80 and remove brackets.  |
| V6 dry-run hangs > 60s                                              | Expected — V6 warms model state. Run async or use a 300s+ timeout.                                   |
| V6 elaboration fails with connection error                          | Ollama not running. Start it: `ollama serve`. Confirm: `curl 127.0.0.1:11434/api/tags`               |
| V6 model not found                                                  | Pull it: `ollama pull qwen2.5:7b-instruct-q5_K_M`                                                    |

---

## 8. LLM-agent contract

This section is for the **LLM agent** drafting briefs or seeds. Human operators can skim it.

### 8.1 Identity

The drafting agent is `permanent-note-seed-agent-v1.0.0` ([.github/agents/permanent-note-seed-agent-v1.0.0.md](../../.github/agents/permanent-note-seed-agent-v1.0.0.md)).

### 8.2 Two ways the agent can produce output

**Mode A — Brief mode (preferred for human review).**
Agent produces a YAML brief. Human reviews. Human runs `python synth_seed_builder.py build`.

**Mode B — Direct seed mode.**
Agent produces the final `*_extracted.json` directly (must conform to [synthetic_bundle.schema.json](synthetic_bundle.schema.json)). Use only when bypassing the human review gate is acceptable.

### 8.3 Hard contract for any agent output

1. **Concept name** appears in:
   - the `definition` callout title (verbatim or lightly varied)
   - **every support callout's title or body** (case-insensitive substring; see §5.3)
2. **Exactly one** `definition` callout per seed.
3. **Total callouts**: 4-8 (one definition + 3-7 support).
4. **Allowed callout types**: `definition`, `key-claim`, `key-distinction`, `example`, `warning`, `claude-insight`, `important`, `evidence`, `analogy`, `methodology-and-sources`, `principle-point`, `helpful-tip`, `counter-argument`, `abstract`, `thought-experiment`. (15 types total — see [synthetic_bundle.schema.json](synthetic_bundle.schema.json).)
5. **Title constraints**: 3-80 chars, no surrounding `[[ ]]` brackets, no trailing parenthetical citations.
6. **Wiki-links**: 5-12 `[[link]]` targets across all bodies.
7. **Domain**: kebab-case (`cognitive-science`, not `Cognitive Science`).
8. **Filename** (Mode B only): `<concept-kebab>-synthetic-seed-<YYYY-MM-DD>_extracted.json`.

### 8.4 Validation gate

Before declaring a seed "done", the agent (or its orchestrator) MUST run:

```bash
python synth_seed_builder.py validate <path-to-seed-or-batch-dir>
```

Exit code `0` and zero errors → ship. Anything else → fix and retry.

### 8.5 Failure-mode awareness

The agent must not:
- Emit a definition title that omits the concept name.
- Emit a support callout whose title and body both fail the substring rule.
- Use callout types outside the 15-type whitelist.
- Use Title-Case or snake_case domains.
- Pre-render `tags:`, `aliases:`, or other Obsidian YAML — V6 generates frontmatter downstream.
- Write inline images, Dataview queries, or Templater syntax in callout bodies.

---

## 9. Schema reference

The full machine-checkable contract: [synthetic_bundle.schema.json](synthetic_bundle.schema.json).
The narrative companion: [SYNTHETIC_BUNDLE_SCHEMA.md](SYNTHETIC_BUNDLE_SCHEMA.md).

V6 reads only the subset of fields V4's `mine_concepts()` and `build_bundles()` consume:

| Field                                          | Used by V4/V6 for                                |
|------------------------------------------------|--------------------------------------------------|
| `extracted_items.callouts[*]` where `type=definition` | Concept identity (one per seed)             |
| `extracted_items.callouts[*]` (any type)       | Support callouts (substring filter applied)      |
| `document_metadata.frontmatter.primary_domain` | `domain` field on the bundle                     |
| `document_metadata.frontmatter.secondary_domains` | `subdomains`                                  |
| `document_metadata.frontmatter.aliases`        | Bundle aliases                                   |
| `document_metadata.frontmatter.title`          | Source-report title (cosmetic in V6 output)      |
| `document_metadata.frontmatter.confidence`     | Carried into the permanent note                  |
| `extracted_items.related_concepts` (or similar) | Seed graph for `related_links`                  |

Anything else in the JSON is ignored by V6, but valid JSON Schema compliance is enforced by `synth_seed_builder.py validate`.

---

## 10. Maintenance

- **Tests**: `python -m pytest test_synth_seed_builder.py -v` — must stay at 29 passing.
- **Schema changes**: update both `synthetic_bundle.schema.json` AND `SYNTHETIC_BUNDLE_SCHEMA.md` AND the agent prompt; bump `synth_seed_builder.py` `__version__`.
- **V4 changes**: if `_clean_title`, `_gather_support`, or `MAX_SUPPORT_CALLOUTS` change in V4, mirror them in `synth_seed_builder.py` and add a regression test.
- **New callout types**: extend `ALLOWED_CALLOUT_TYPES` in `synth_seed_builder.py`, the schema enum, and the agent prompt's whitelist.

---

## 11. Version

- **Workflow version**: 1.0.0 (2026-04-24)
- **`synth_seed_builder.py`**: 1.0.0
- **Seed Agent**: `permanent-note-seed-agent-v1.0.0`
- **Schema**: Draft 2020-12, file version embedded in `$id`
- **Pipeline targets**: V4 (mining), V6 (elaboration)

---

## 12. Term-List Workflow (batch upstream)

When you need to seed many concepts at once — for example, all the foundational terms in a topic cluster — authoring one YAML brief per concept is slow. The **term-list workflow** lets a Seed Agent (or you) emit a single Markdown document listing N concepts, then expands it into N briefs and N seeds in a single command.

```
term-lists/<batch>.md                                    (you author / agent emits)
  │  expand_term_list.py expand
  ▼
briefs/<batch>/*.yaml + manifest.json                    (one brief per accepted term)
  │  expand_term_list.py build-batch
  ▼
<seeds-dir>/<YYYY-MM-DD>-<batch>/*_extracted.json        (validated synthetic seeds)
  │  pipeline_v6.py
  ▼
permanent notes
```

### Subcommands

| Command       | Purpose                                                                            |
|---------------|------------------------------------------------------------------------------------|
| `expand`      | Parse the term list, dedup against existing permanent notes, write briefs + manifest |
| `build-batch` | Read a batch's manifest, call `synth_seed_builder.py build` per accepted brief     |
| `run`         | Convenience: `expand` + `build-batch` in one invocation                            |

### Quickstart

```bash
# Author or generate a term list at term-lists/<YYYY-MM-DD>-<batch>.md
# (see TERM_LIST_FORMAT.md for the spec)

# One-shot end-to-end:
python expand_term_list.py -v run \
  term-lists/2026-04-24-retrieval-practice-cluster.md

# Outputs:
#   briefs/2026-04-24-retrieval-practice-cluster/*.yaml + manifest.json
#   <default seeds dir>/2026-04-24-retrieval-practice-cluster/*_extracted.json
```

### Authoring a term list

See [`TERM_LIST_FORMAT.md`](./TERM_LIST_FORMAT.md) for the full spec. In short: YAML frontmatter (`batch_name`, `batch_date`, `default_domain`, `default_confidence`) + one `## Term Title` H2 per concept, with bullet fields for link slots (`aliases`, `related`, `broader`, `narrower`, `prerequisites`, `secondary_domains`, `domain`, `confidence`) and bold-key paragraphs for `**definition**:`, `**key_claim**:`, `**warning**:`. The exemplar at [`term-lists/2026-04-24-retrieval-practice-cluster.md`](./term-lists/2026-04-24-retrieval-practice-cluster.md) is the canonical reference.

### Dedup gate

Before writing each brief, `expand` checks `<permanent-notes-dir>/<kebab-of-term>.md`. If the file exists, the term is **skipped** (logged as `DEDUP-SKIP`) and excluded from the manifest. This makes the workflow safe to re-run: regenerating a batch will not overwrite already-promoted permanent notes. Override the location with `--permanent-notes-dir`.

### When to use this vs. single-brief `synth_seed_builder.py build`

| Use term-list workflow when                          | Use single-brief workflow when           |
|------------------------------------------------------|------------------------------------------|
| You have ≥ 3 concepts to seed in one sitting         | You're filling in a single missing wiki-link target |
| You want a Seed Agent to draft many briefs at once   | You're hand-authoring a careful brief    |
| The concepts share domain / confidence defaults      | The brief needs heavy custom prose       |
| You want dedup-against-existing-notes for free       | You're iterating on a single seed        |
