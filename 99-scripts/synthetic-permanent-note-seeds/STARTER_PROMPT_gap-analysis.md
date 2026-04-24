# Starter Prompt — Gap Analysis → Term List → Pipeline

> **Purpose.** Use the existing permanent-notes folder as the input,
> identify which concepts are MISSING (broken wiki-links, sibling-shaped
> gaps in a domain), and have the agent propose a term list of new
> notes to add. The term list then feeds the standard pipeline
> (`expand_term_list.py run` → `pipeline_v6.py`).

---

## Step 1 — Run discovery commands (operator, ~10 seconds)

These three commands collect the raw signal the agent needs. Copy-paste
the OUTPUT of each into the prompt template below.

```bash
cd "d:/10_pur3v4d3r's-vault"
PERM="999-report-organizing/_permanent-notes/v6-llm-elaborated"

# A. Existing permanent notes (so the agent doesn't re-propose them)
ls "$PERM" | sed 's/\.md$//' | sort -u > /tmp/_pn_existing.txt
wc -l /tmp/_pn_existing.txt
head -50 /tmp/_pn_existing.txt    # paste this list (or all of it) into slot {EXISTING}

# B. Broken / ghost wiki-links — referenced as [[X]] but no <kebab-of-X>.md exists
grep -rho '\[\[[^]]*\]\]' "$PERM" \
  | sed 's/^\[\[//;s/\]\]$//' \
  | awk '{print tolower($0)}' \
  | sed 's/[^a-z0-9]\+/-/g;s/^-//;s/-$//' \
  | sort -u > /tmp/_pn_referenced.txt

comm -23 /tmp/_pn_referenced.txt \
         <(ls "$PERM" | sed 's/\.md$//' | sort -u) \
  > /tmp/_pn_missing.txt
wc -l /tmp/_pn_missing.txt
head -80 /tmp/_pn_missing.txt     # paste this list into slot {GHOST_LINKS}

# C. Optional: domain frequency (helps the agent see which clusters
#    are dense vs sparse — useful when guiding sibling-gap suggestions)
grep -rh '^domain:' "$PERM" \
  | awk -F: '{print $2}' | tr -d '"' | tr -d "'" \
  | awk '{$1=$1};1' | sort | uniq -c | sort -rn \
  | head -30                       # paste this table into slot {DOMAIN_HIST}
```

If you want narrower scope, substitute `$PERM` with a subdirectory or
add `| grep -i <topic>` to filter `/tmp/_pn_existing.txt`.

---

## Step 2 — The prompt

Paste into a fresh chat with the Permanent Note Seed Agent
(`.github/agents/permanent-note-seed-agent-v1.0.0.md`). Replace the
four `{...}` slots with the discovery output from Step 1 plus your
focus statement.

```text
========================================================================
ACTIVATE: List Mode  (gap-analysis variant)

I want you to analyze the gaps in my permanent-notes graph and propose
NEW notes to add. Then emit a term list per `TERM_LIST_FORMAT.md`.

──────────────────────────────────────────────────────────────────────
FOCUS
──────────────────────────────────────────────────────────────────────
{FOCUS}
  e.g. "metacognition / self-regulated-learning cluster"
  e.g. "anything missing in cognitive-science domain"
  e.g. "fill in the most-referenced ghost links"

──────────────────────────────────────────────────────────────────────
EXISTING PERMANENT NOTES (do NOT re-propose any of these)
──────────────────────────────────────────────────────────────────────
{EXISTING}
  ← paste output of /tmp/_pn_existing.txt
    (one kebab slug per line)

──────────────────────────────────────────────────────────────────────
GHOST WIKI-LINKS (referenced by existing notes but file does not exist)
──────────────────────────────────────────────────────────────────────
{GHOST_LINKS}
  ← paste output of /tmp/_pn_missing.txt
    (one kebab slug per line; ranked roughly by reference count)

──────────────────────────────────────────────────────────────────────
DOMAIN HISTOGRAM (optional context: which clusters are dense vs sparse)
──────────────────────────────────────────────────────────────────────
{DOMAIN_HIST}
  ← paste output of the domain frequency table

──────────────────────────────────────────────────────────────────────
SELECTION RULES
──────────────────────────────────────────────────────────────────────
1. Propose between 5 and 15 new terms.
2. Prioritize, in this order:
     (a) Ghost links that appear in multiple existing notes
         — high payoff: closes the most edges in the graph.
     (b) Sibling concepts of clusters in {FOCUS} that an expert would
         expect to find present (e.g. if "spaced-repetition" exists but
         "expanding-rehearsal" does not, propose it).
     (c) Foundational prerequisites that are referenced but unwritten.
3. Skip any term whose kebab slug appears in {EXISTING}.
4. For each proposed term, the `prerequisites` and `related` bullets
   SHOULD wherever possible point to slugs that ARE in {EXISTING}
   — this is how the new notes wire into the existing graph.
5. Confidence enum: low | medium | high. Default high for established
   concepts, medium for contested ones, low for speculative.

──────────────────────────────────────────────────────────────────────
OUTPUT CONTRACT
──────────────────────────────────────────────────────────────────────
Emit ONE Markdown document conforming to TERM_LIST_FORMAT.md:
  • YAML frontmatter: batch_name, batch_date (today: 2026-04-24),
    default_domain (pick the dominant domain of the proposed terms),
    default_confidence, notes (1–2 sentence rationale for the batch).
  • One `## Term Title` H2 per proposed term, in priority order.
  • Per term: link bullets (aliases, related, broader, narrower,
    prerequisites — omit if empty; never empty brackets), then
    `**definition**:` / `**key_claim**:` / `**warning**:` paragraphs.
  • Substring rule: each of those three paragraphs MUST contain the
    term name verbatim.
  • No `very-high` confidence (schema rejects it).
  • Output ONLY the markdown. No fences, no preamble, no commentary.

Before the term list, emit a single line:
    <!-- gap-analysis: N existing scanned, M ghost links found, K terms proposed -->
========================================================================
```

---

## Step 3 — Standard pipeline (unchanged)

Save the agent's output, then run:

```bash
cd "d:/10_pur3v4d3r's-vault/99-scripts/synthetic-permanent-note-seeds"

# Save agent output to:
#   term-lists/2026-04-24-<batch-name>.md

python expand_term_list.py -v run \
    term-lists/2026-04-24-<batch-name>.md
# The dedup gate will catch any slug the agent slipped through that
# already exists. Anything written is genuinely new.

python synth_seed_builder.py validate \
    "d:/10_pur3v4d3r's-vault/999-report-organizing/_extractor-output/_synthetic-seeds/2026-04-24-<batch-name>"

cd ../report-extraction-to-permanent-notes-building-v6
python pipeline_v6.py \
    --input-dir "d:/10_pur3v4d3r's-vault/999-report-organizing/_extractor-output/_synthetic-seeds/2026-04-24-<batch-name>" \
    --report-runs "runs/2026-04-24-<batch-name>-log.json"
```

---

## Mental model

```
ls _permanent-notes/                         →  {EXISTING}    (skip these)
grep [[...]] | comm -23 → kebab missing      →  {GHOST_LINKS} (close these edges)
grep ^domain: | uniq -c                      →  {DOMAIN_HIST} (calibrate sparseness)
                ▼
            agent (List Mode, gap variant)
                ▼
        term-lists/<date>-<batch>.md
                ▼
   expand_term_list.py run  →  briefs + JSON seeds
                ▼
        pipeline_v6.py      →  permanent notes
```

The `expand` step's dedup gate is your safety net — even if the agent
proposes a term that already exists, it will be skipped and logged.
