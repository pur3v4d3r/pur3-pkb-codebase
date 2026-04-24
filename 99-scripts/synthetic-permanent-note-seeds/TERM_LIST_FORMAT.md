# Term-List Markdown Format — v1.0.0

A **term list** is a single Markdown file containing a batch of concepts to be turned into permanent notes. One H2 section per term. Each section has a small fixed set of fields, all human-readable.

This is the **upstream input** to `expand_term_list.py`, which in turn produces the YAML briefs that `synth_seed_builder.py build` converts to `*_extracted.json` seeds.

```
term-list.md  →  expand_term_list.py expand   →  briefs/*.yaml  +  manifest.json
              →  expand_term_list.py build-batch  →  *_extracted.json  +  validation report
              →  pipeline_v6.py            →  permanent notes
```

---

## 1. File structure

```markdown
---
batch_name: <kebab-case-batch-name>      # required — used for output dir + manifest
batch_date: 2026-04-24                   # required — ISO date; used in seed filenames
default_domain: cognitive-science        # optional — applied to terms missing a `domain`
default_confidence: high                 # optional — applied to terms missing `confidence`
notes: |                                 # optional — free-form intent for human reviewers
    Seeding the retrieval-practice cluster.
---

# Batch: <Human-Readable Batch Title>

(Optional intro prose. Ignored by the parser.)

## <Term Name in Title Case>

- **domain**: kebab-case-domain
- **secondary_domains**: [kebab-1, kebab-2]
- **aliases**: [Alt Name, Abbrev]
- **broader**: [parent-1, parent-2]
- **narrower**: [child-1]
- **related**: [sibling-1, sibling-2, sibling-3]
- **prerequisites**: [foundation-1]
- **confidence**: high

**definition**: <one-paragraph definition; may include [[wiki-links]]>

**key_claim**: <one central empirical or theoretical claim about the term>

**warning**: <one common misreading, failure mode, or boundary the seed agent must surface>

## <Next Term Name>

...
```

---

## 2. Field semantics

### 2.1 Frontmatter (file-level)

| Key                  | Required | Type   | Purpose                                                                  |
|----------------------|----------|--------|--------------------------------------------------------------------------|
| `batch_name`         | yes      | string | kebab-case; becomes the output sub-directory and manifest stem          |
| `batch_date`         | yes      | date   | ISO `YYYY-MM-DD`; used in generated seed filenames                       |
| `default_domain`     | no       | string | Fills `domain` for any term that omits it                                |
| `default_confidence` | no       | enum   | `low` / `medium` / `high`. Default: `medium`                              |
| `notes`              | no       | string | Free-form; preserved in the manifest under `batch.notes`                 |

### 2.2 Per-term H2 section

The H2 heading **is** the term name. Title Case recommended; the parser kebab-cases it for filenames.

| Bullet field        | Required | Type            | Notes                                                                         |
|---------------------|----------|-----------------|-------------------------------------------------------------------------------|
| `domain`            | yes*     | kebab-case      | *Required unless `default_domain` is set in frontmatter                       |
| `secondary_domains` | no       | list[kebab]     | Default: `[]`                                                                 |
| `aliases`           | no       | list[string]    | Free-form; default: `[]`                                                      |
| `broader`           | no       | list[kebab]     | Wiki-link slugs of parent concepts                                            |
| `narrower`          | no       | list[kebab]     | Wiki-link slugs of child concepts                                             |
| `related`           | no       | list[kebab]     | Wiki-link slugs of sibling concepts                                           |
| `prerequisites`     | no       | list[kebab]     | Wiki-link slugs of foundation concepts                                        |
| `confidence`        | no       | enum            | Overrides `default_confidence`                                                |

| Bold field    | Required | Purpose                                                                                |
|---------------|----------|----------------------------------------------------------------------------------------|
| `definition`  | yes      | Becomes the seed's `definition` callout body. **MUST contain the term name verbatim.** |
| `key_claim`   | recommended | Becomes a `key-claim` callout. MUST contain the term name (V4 substring rule).      |
| `warning`     | recommended | Becomes a `warning` callout. MUST contain the term name (V4 substring rule).        |

`expand_term_list.py` enforces the substring rule and writes warnings into the manifest if a term lacks a `key_claim` or `warning`.

### 2.3 List-syntax conventions

- Inline lists may be written as YAML-style (`[a, b, c]`) **or** comma-separated (`a, b, c`). Both parse identically.
- Empty lists may be written as `[]` or omitted entirely.
- Wiki-link bracketing is allowed but stripped: `[[foo]]` → `foo`.

---

## 3. Minimum viable term

```markdown
---
batch_name: minimal-test
batch_date: 2026-04-24
default_domain: cognitive-science
---

# Batch: Minimal Test

## Encoding Specificity

**definition**: Encoding Specificity is the principle that retrieval is most effective when the conditions at retrieval match the conditions at encoding.
```

This passes — domain inherits from `default_domain`, all link slots default to empty, `key_claim` and `warning` produce manifest warnings (non-blocking) so the seed agent can fill them later.

---

## 4. Full exemplar (3 terms)

See [term-lists/2026-04-24-retrieval-practice-cluster.md](term-lists/2026-04-24-retrieval-practice-cluster.md) for the canonical reference list bundled with this workflow.

---

## 5. What the parser does NOT support

- H1 sections as terms (use H2 only — H1 is reserved for the batch title)
- H3 sub-sections inside a term (parser ignores any heading deeper than H2)
- Inline images, code fences, tables (stripped from field bodies)
- Multi-paragraph definitions (only the first paragraph after `**definition**:` is kept)
- Term names containing forward slashes, colons, or backslashes (filename-unsafe)

If you need richer content per term, write the YAML brief directly via `synth_seed_builder.py build`.

---

## 6. Version

- **Format version**: 1.0.0 (2026-04-24)
- **Parser**: `expand_term_list.py` ≥ 1.0.0
