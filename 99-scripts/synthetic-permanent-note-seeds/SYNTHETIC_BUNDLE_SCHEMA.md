# Synthetic Permanent-Note Seed — Bundle Schema (v1)

> [!abstract]
> This document defines the **minimum-viable contract** that a synthetic
> `*_extracted.json` file must satisfy to be consumed by the V4 / V5 / V6
> permanent-note pipelines without modification.
>
> A "synthetic seed" is a hand- or LLM-authored JSON file that mimics the
> shape produced by `pkb_extractor.py` but originates from a concept brief
> rather than a parsed academic report. The downstream pipeline cannot
> tell the difference.

---

## 1. Why this contract exists

V4's [`build_bundles`](../report-extraction-to-permanent-notes-building-v4/pipeline_v4.py) and
[`mine_concepts`](../report-extraction-to-permanent-notes-building-v4/pipeline_v4.py) only read
~30 fields out of the ~200 the extractor emits. Synthetic seeds populate
**only those fields**. Everything else is omitted.

The contract is intentionally permissive about extra fields (the pipeline
ignores unknown keys) but **strict about the fields it does require** —
omitting `extracted_items.callouts` or the `frontmatter.title` will silently
produce zero bundles or a degenerate note.

---

## 2. Top-level shape

```jsonc
{
  "extraction_metadata": { "source_file": "<concept-kebab>-synthetic-seed-<YYYY-MM-DD>.md" },
  "document_metadata":   { "frontmatter": { /* see §3 */ } },
  "extracted_items":     { "callouts":    [ /* see §4 */ ] },
  "knowledge_graph":     { "unique_wiki_link_targets": [ /* see §5 */ ] }
}
```

| Top-level key             | Required | Read by    | Purpose                          |
|---------------------------|----------|------------|----------------------------------|
| `extraction_metadata`     | optional | provenance | filename echo only               |
| `document_metadata`       | **yes**  | V4 §3      | report-level frontmatter context |
| `extracted_items`         | **yes**  | V4 §4      | concept + support callouts       |
| `knowledge_graph`         | optional | V4 §5      | wiki-link target hints           |

---

## 3. `document_metadata.frontmatter` — required keys

These map directly into `ConceptBundle` fields.

| Key                  | Type               | Required | Pipeline use                                  |
|----------------------|--------------------|----------|-----------------------------------------------|
| `title`              | string             | **yes**  | `report_title` (LLM context)                  |
| `primary_domain`     | string (kebab)     | **yes**  | `domain` → frontmatter `primary-domain`       |
| `secondary_domains`  | list[string]       | optional | `subdomains` → frontmatter                    |
| `aliases`            | list[string]       | optional | concept aliases pool (capped at 8)            |
| `confidence`         | `high\|medium\|low` | optional (default `medium`) | rendered `confidence`     |
| `related`            | list[string]       | optional | feeds `_related_links_from_payload`           |
| `see-also`           | list[string]       | optional | "                                             |
| `broader`            | list[string]       | optional | "                                             |
| `narrower`           | list[string]       | optional | "                                             |
| `prerequisites`      | list[string]       | optional | "                                             |

**Notes:**
- Wiki-link list values may be written as raw targets (`"flow-theory"`) or
  as wiki-link syntax (`"[[flow-theory]]"`); both are stripped to bare
  targets by `_related_links_from_payload`.
- `primary_domain` is normalized via `to_kebab()`; missing → `"other"`.

---

## 4. `extracted_items.callouts` — concept + support

A list of callout objects. Each object:

```jsonc
{
  "type":  "definition",     // see allowed types below
  "title": "Concept Name",
  "body":  "Markdown body...",
  "line_number": 1,           // optional, ignored by V4/V5/V6
  "source": "...",            // optional, ignored
  "char_start": 0,            // optional, ignored
  "char_end":   0             // optional, ignored
}
```

### 4.1 Concept-seed callout (exactly **one per file**, recommended)

| Field   | Value                                                                |
|---------|----------------------------------------------------------------------|
| `type`  | `"definition"` (preferred) or `"key-claim"` (only if `--include-key-claims`) |
| `title` | The canonical concept name. **No trailing parentheticals**, no em-dash qualifiers — `_clean_title()` will strip them and you'll lose tokens. |
| `body`  | 80–250 words. Format: definition paragraph + `**Boundary:** ...` paragraph + `**See also:** [[link-a]], [[link-b]]` line. |

> [!warning] Title cleaning
> `_clean_title()` removes `(parenthetical)` suffixes and ` — qualifier`
> tails before deduplication. `"Cognitive Load (Sweller, 1988)"` becomes
> `"Cognitive Load"`. Keep titles already-clean to make the bundle
> behavior predictable.

### 4.2 Support callouts (4–8 per file, recommended)

V4 keeps a support callout only when the **cleaned concept title appears
as a case-insensitive substring inside the support callout's title or
body**. This is enforced by `_gather_support()` and is the most common
failure mode for hand-authored seeds.

Allowed `type` values (subset of `SUPPORT_CALLOUT_TYPES`):

| Type                  | Suggested count | Purpose in LLM prompt                  |
|-----------------------|-----------------|----------------------------------------|
| `key-claim`           | 1–2             | Headline empirical/theoretical claims  |
| `key-distinction`     | 0–1             | "X is not Y" disambiguation            |
| `example`             | 1–2             | Concrete instantiation                 |
| `warning`             | 0–1             | Common misreading                      |
| `claude-insight`      | 0–1             | Synthesis / non-obvious framing        |
| `important`           | 0–1             | High-priority anchor                   |
| `principle-point`     | 0–1             | Foundational principle                 |
| `evidence`            | 0–1             | Empirical anchor                       |
| `person`              | 0–1             | Triggers `key_figures` field           |
| `open-question`       | 0–1             | Triggers `tensions_or_questions`       |
| `tension`             | 0–1             | "                                      |
| `far-transfer`        | 0–1             | Cross-domain applicability             |
| `original-synthesis`  | 0–1             | Author's own synthesis                 |
| `section-summary`     | 0–1             | Encyclopedic summary                   |

**Hard caps from V4:**
- `MAX_SUPPORT_CALLOUTS = 8` — anything past 8 is dropped.
- `MAX_SUPPORT_BODY_CHARS = 600` — bodies truncated with `…`.
- `MIN_TITLE_LEN = 3`, `MAX_TITLE_LEN = 80`.

**Each support body should mention the concept title verbatim at least
once** (case-insensitive). Phrasing it as `"…the [[concept-kebab|concept
title]] mechanism…"` satisfies the substring rule and seeds an outbound
wiki-link in one move.

---

## 5. `knowledge_graph.unique_wiki_link_targets`

Optional. A flat list of bare wiki-link targets. V4 takes the first 30 and
appends them to the related-link pool (after dedup against the
frontmatter-derived list).

A safe seed strategy: enumerate every `[[target]]` you placed in the
concept body or any support body. The agent or builder script should
extract these automatically.

---

## 6. Naming convention

```
<concept-kebab>-synthetic-seed-<YYYY-MM-DD>_extracted.json
```

The `_extracted.json` suffix is **mandatory** — it matches V4's
`discover_jsons()` glob (`*_extracted.json`).

The `synthetic-seed` infix is the provenance marker. Tooling (audit
scripts, V6 frontmatter stamping) keys off this substring to distinguish
seed-born notes from report-born notes.

**Output directory** (parallels organic batches):

```
999-report-organizing/_extractor-output/_synthetic-seeds/<YYYY-MM-DD-batch>/
```

---

## 7. Worked minimal example

```jsonc
{
  "extraction_metadata": {
    "source_file": "spaced-retrieval-synthetic-seed-2026-04-24.md"
  },
  "document_metadata": {
    "frontmatter": {
      "title": "Spaced Retrieval — A Synthetic Seed for the V6 Pipeline",
      "primary_domain": "cognitive-science",
      "secondary_domains": ["learning-science", "memory-research"],
      "aliases": ["Spaced Retrieval Practice", "Distributed Retrieval"],
      "confidence": "high",
      "related":      ["[[testing-effect]]", "[[desirable-difficulties]]"],
      "broader":      ["[[retrieval-practice]]"],
      "narrower":     ["[[expanding-retrieval]]"],
      "prerequisites":["[[long-term-memory]]"]
    }
  },
  "extracted_items": {
    "callouts": [
      {
        "type":  "definition",
        "title": "Spaced Retrieval",
        "body":  "Spaced retrieval is a learning technique that combines retrieval practice with distributed practice: learners attempt to recall target material across increasing temporal gaps rather than in massed blocks. Each successful retrieval at a longer interval reconsolidates the memory trace and yields a steeper retention curve than equivalent restudy.\n\n**Boundary:** Spaced retrieval is distinct from pure spaced study — the retrieval attempt itself is the load-bearing operation. Re-reading on a schedule produces only the spacing benefit; spaced retrieval produces both the spacing and the testing effect simultaneously.\n\n**See also:** [[testing-effect]], [[desirable-difficulties]], [[retrieval-practice]]"
      },
      {
        "type":  "key-claim",
        "title": "Spaced retrieval outperforms massed retrieval at long retention intervals",
        "body":  "Across multiple meta-analyses, spaced retrieval produces durable retention gains over massed retrieval at delays beyond 24 hours, with effect sizes typically d = 0.4–0.7."
      },
      {
        "type":  "key-distinction",
        "title": "Spaced retrieval vs. spaced study",
        "body":  "Distributing study sessions across time captures only half the benefit. Spaced retrieval requires the learner to actively reconstruct the target — recognition is not enough."
      },
      {
        "type":  "example",
        "title": "Spaced retrieval in vocabulary acquisition",
        "body":  "A learner who attempts to recall a new word's translation after 1 minute, 10 minutes, 1 hour, and 1 day shows substantially better one-week retention than a learner who attempts recall four times in the same 30-minute block — illustrating spaced retrieval's compounding benefit."
      },
      {
        "type":  "warning",
        "title": "Spaced retrieval requires retrieval, not recognition",
        "body":  "Re-reading flashcards on a schedule is spaced re-exposure, not spaced retrieval. The learner must produce the target from memory; passively recognizing it does not engage the same reconsolidation pathway."
      }
    ]
  },
  "knowledge_graph": {
    "unique_wiki_link_targets": [
      "testing-effect",
      "desirable-difficulties",
      "retrieval-practice",
      "expanding-retrieval",
      "long-term-memory"
    ]
  }
}
```

This file, dropped at
`_extractor-output/_synthetic-seeds/2026-04-24-batch/spaced-retrieval-synthetic-seed-2026-04-24_extracted.json`,
is consumable by:

```powershell
python pipeline_v6.py `
  --input-dir "999-report-organizing/_extractor-output/_synthetic-seeds/2026-04-24-batch" `
  --report spaced-retrieval -v
```

---

## 8. Validation checklist

Before handing a synthetic seed to V6, verify:

- [ ] Filename ends in `_extracted.json` and contains `synthetic-seed`
- [ ] Top-level keys present: `document_metadata`, `extracted_items`
- [ ] `document_metadata.frontmatter.title` is a non-empty string
- [ ] `document_metadata.frontmatter.primary_domain` is a kebab-case string
- [ ] `extracted_items.callouts` contains at least one `definition` callout
- [ ] The definition callout's title is 3–80 characters
- [ ] Every support callout's body or title contains the cleaned concept
      title as a case-insensitive substring
- [ ] No more than 8 support callouts (extras are silently dropped)
- [ ] Wiki-link targets in `knowledge_graph.unique_wiki_link_targets` are
      bare slugs, not bracketed `[[...]]` syntax
- [ ] JSON is valid (no trailing commas, no comments — use `// ...` only
      in this doc, never in a real seed)

The companion `synth_seed_builder.py --validate` enforces every item on
this list.

---

## 9. Versioning

| Schema version | Date       | Change                    |
|----------------|------------|---------------------------|
| `v1`           | 2026-04-24 | Initial contract.         |

Bump only when the V4/V5/V6 bundle-mining contract itself changes. Adding
new optional support-callout types is **not** a breaking change.
