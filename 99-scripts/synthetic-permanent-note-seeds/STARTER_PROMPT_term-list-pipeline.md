# Starter Prompt — Term List → JSON Seeds → V6 Permanent Notes

> Copy everything between the `===` lines into a fresh chat with the
> Permanent Note Seed Agent (`.github/agents/permanent-note-seed-agent-v1.0.0.md`).
> Fill in the four `<<< ... >>>` slots, then send.
> The agent will emit a Markdown term list. Then run the two shell
> commands at the bottom of this file to drive the rest of the pipeline.

---

## The prompt

```text
========================================================================
ACTIVATE: List Mode

I want to seed a batch of permanent notes for the following concept
cluster. Emit ONE Markdown term list per `TERM_LIST_FORMAT.md`. No
fences, no preamble, no commentary — just the document, ready to save
to `99-scripts/synthetic-permanent-note-seeds/term-lists/`.

──────────────────────────────────────────────────────────────────────
BATCH METADATA
──────────────────────────────────────────────────────────────────────
batch_name:         <<< kebab-case batch slug, e.g. metacognition-cluster >>>
batch_date:         <<< today, ISO YYYY-MM-DD >>>
default_domain:     <<< kebab-case domain, e.g. cognitive-science >>>
default_confidence: <<< low | medium | high  (default: high) >>>

──────────────────────────────────────────────────────────────────────
TERMS TO SEED
──────────────────────────────────────────────────────────────────────
<<< Paste 3–15 concept names, one per line. Optional one-line hint
    after a colon. Example:
        Metacognition: thinking about thinking; Flavell 1979
        Judgment of Learning: prediction of future recall
        Illusion of Fluency: confusing reading-ease for understanding
>>>

──────────────────────────────────────────────────────────────────────
HARD REQUIREMENTS (do not violate)
──────────────────────────────────────────────────────────────────────
• YAML frontmatter first; one `## Term Title` H2 per concept.
• For every term, emit:
    - bullets:  aliases, related, broader, narrower, prerequisites
                (omit any that don't apply; never leave empty brackets)
    - **definition**: paragraph (MUST contain the term name verbatim)
    - **key_claim**:  paragraph (MUST contain the term name verbatim)
    - **warning**:    paragraph (MUST contain the term name verbatim)
• Confidence enum: low | medium | high  (NEVER very-high — the seed
  schema rejects it).
• No duplicate terms (case-insensitive after kebab-casing).
• Wiki-link slots: bare kebab tokens or `[[Wiki Names]]` both work.
• Output is ONLY the markdown document. Nothing else.
========================================================================
```

---

## After the agent responds

1. **Save** the agent's output to:
   ```
   99-scripts/synthetic-permanent-note-seeds/term-lists/<YYYY-MM-DD>-<batch-name>.md
   ```

2. **Expand → seeds** in one command (writes briefs, dedups against
   existing permanent notes, builds JSON seeds):
   ```bash
   cd "d:/10_pur3v4d3r's-vault/99-scripts/synthetic-permanent-note-seeds"
   python expand_term_list.py -v run \
       term-lists/<YYYY-MM-DD>-<batch-name>.md
   ```
   Expected output:
   - `briefs/<YYYY-MM-DD>-<batch-name>/*.yaml` + `manifest.json`
   - `<seeds-dir>/<YYYY-MM-DD>-<batch-name>/*_extracted.json`

3. **Validate** the seed batch (cheap, no LLM):
   ```bash
   python synth_seed_builder.py validate \
       "d:/10_pur3v4d3r's-vault/999-report-organizing/_extractor-output/_synthetic-seeds/<YYYY-MM-DD>-<batch-name>"
   # expect: "N file(s), 0 with errors, 0 error(s), 0 warning(s)"
   ```

4. **V6 elaboration** (LLM — Ollama must be running):
   ```bash
   cd ../report-extraction-to-permanent-notes-building-v6
   python pipeline_v6.py \
       --input-dir "d:/10_pur3v4d3r's-vault/999-report-organizing/_extractor-output/_synthetic-seeds/<YYYY-MM-DD>-<batch-name>" \
       --report-runs "runs/<YYYY-MM-DD>-<batch-name>-log.json"
   ```

5. **Inspect** the new permanent notes:
   ```bash
   ls "d:/10_pur3v4d3r's-vault/999-report-organizing/_permanent-notes/v6-llm-elaborated/"
   ```

---

## One-liner mental model

```
chat prompt (above)         →  Markdown term list
expand_term_list.py run     →  YAML briefs  +  manifest  +  JSON seeds
synth_seed_builder validate →  schema gate  (fail fast, no LLM cost)
pipeline_v6.py              →  permanent notes (V6 elaborated, full callouts)
```
