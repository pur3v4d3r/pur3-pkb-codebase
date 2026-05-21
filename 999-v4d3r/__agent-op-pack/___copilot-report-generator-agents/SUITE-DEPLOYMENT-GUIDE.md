# PKB Report Generator Suite v2.0 — Deployment & Operator Guide

> **Audience:** This document is written for **two readers simultaneously** — a human operator deploying these prompts in VS Code Copilot, and an LLM agent reading this file to understand how to execute one of the generators successfully. If you are an LLM and someone has handed you this file along with a generator prompt, read this document **before** attempting generation.

---

## What This Suite Is

The **PKB Report Generator Suite v2.0** is a set of nine specialized system prompts that produce long-form (10,000–15,000+ word) Obsidian-compatible Markdown reports. Each generator targets a different analytical structure:

| # | Generator | Best For |
|---|-----------|----------|
| 1 | **Foundational Report** | Broad encyclopedic coverage of a whole topic |
| 2 | **Annotated Critical Analysis** | Reasoning-annotated deep analysis with epistemic confidence |
| 3 | **Practitioner's Field Guide** | Problem-first practical scaffolding (PTAL cycles) |
| 4 | **Dialectical Report** | Thesis–antithesis–synthesis exploration of contested topics |
| 5 | **Comparative Architecture** | Multi-alternative evaluation across dimensions |
| 6 | **Historical-Genealogical** | Chronological/intellectual lineage tracking |
| 7 | **Socratic Exploration** | Question-chain driven inquiry |
| 8 | **First Principles Analysis** | Decompose–verify–reconstruct from foundations |
| 9 | **Deep Dive Report** | Narrow scope, exhaustive specialist depth (15K+ words) |

All nine reports are **pipeline-compatible** with `pipeline_v2.py` — they emit standardized callouts (`[!definition]`, `[!original-synthesis]`, `[!cite]`, `[!connections-and-links]`, `[!further-exploration]` + `[!topic-idea]`) that the extractor parses into permanent notes.

---

## Why Long-Form Generation Fails in Copilot

Before explaining the deployment process, you need to understand **why a single-write approach fails**. The Append-Marker Chain protocol exists because of three concrete failure modes encountered in earlier versions:

### Failure Mode 1: Response Truncation

**What happens:** Copilot attempts to write a 10,000+ word file in a single `create_file` call. The model's response gets truncated before the file content completes. Result: a partial file with no clean recovery path, and Copilot often does not realize truncation occurred.

**Why it happens:** Long-form content stresses the model's output budget. Even with extended thinking, the assistant turn has practical limits that 10,000+ words exceed.

### Failure Mode 2: `replace_string_in_file` on Nonexistent File

**What happens:** Copilot, attempting to assemble content iteratively, calls `replace_string_in_file` against a file that doesn't exist yet (or exists but is empty). The tool fails. Copilot then either retries blindly or abandons the operation.

**Why it happens:** The model conflates the conceptual "writing" workflow with the actual tool sequence required. The tool requires the file to exist and the `oldString` to be present.

### Failure Mode 3: `oldString` Matching Large Blocks

**What happens:** Copilot tries to update an existing file by passing a large `oldString` (hundreds or thousands of characters) to match before replacement. The model hallucinates the existing content, the match fails, and the operation aborts. Even worse: sometimes a partial match succeeds and corrupts the file.

**Why it happens:** LLMs cannot perfectly reproduce long strings from memory. Any whitespace difference, any character drift, any subtle reformatting causes the match to fail.

---

## The Solution: Append-Marker Chain Protocol

All nine generators use a shared file I/O pattern called the **Append-Marker Chain**. It addresses all three failure modes:

### The Pattern

```
Step 0: create_file with YAML frontmatter + a tiny unique marker
        Example final line:  <!-- MARKER_001 -->

Step 1: replace_string_in_file
        oldString:  <!-- MARKER_001 -->
        newString:  [content chunk ≤4,000 words] + <!-- MARKER_002 -->

Step 2: replace_string_in_file
        oldString:  <!-- MARKER_002 -->
        newString:  [next content chunk] + <!-- MARKER_003 -->

...and so on until the final write, which has NO trailing marker.
```

### Why This Works

| Failure Mode | How Append-Marker Chain Solves It |
|--------------|-----------------------------------|
| **Truncation** | Each write is bounded (≤4,000 words). No single write hits the output ceiling. |
| **File doesn't exist** | Step 0 always creates the file before any replacement. Tool sequence is enforced. |
| **`oldString` matching fails** | The `oldString` is ALWAYS the marker comment — a tiny, unique, ~20-character string the model can reproduce perfectly. No large-block matching ever occurs. |

### Marker Anatomy

```html
<!-- MARKER_001 -->
```

- **Comment syntax:** Markdown-safe, invisible in rendered Obsidian
- **Sequential numbering:** Easy to track which marker is current
- **Globally unique:** No risk of accidental matches elsewhere in the file
- **Tiny:** ~20 characters, trivially reproducible by the LLM
- **Removed in final write:** The last write contains no trailing marker, leaving a clean file

### Critical Rules (Non-Negotiable)

1. **Step 0 is always `create_file`.** Never start with `replace_string_in_file`.
2. **`oldString` is ALWAYS just the marker comment.** Never include any surrounding context. Never try to match large blocks.
3. **Each `newString` ends with the next marker** — except the final write, which has no trailing marker.
4. **One write per chunk.** Do not try to consolidate multiple chunks into one call.
5. **Follow the Write Chunk Map in the generator.** Each generator specifies how many writes are expected and what content each contains.

---

## How to Deploy a Generator

### Step 1: Choose the Right Generator

Pick the generator whose architecture matches your need. The table at the top of this document is the quick reference. When in doubt:

- **You want broad coverage of an unfamiliar topic** → Foundational
- **You want narrow depth on a specific aspect** → Deep Dive
- **You want practical guidance** → Practitioner's Field Guide
- **You want to evaluate multiple options** → Comparative Architecture
- **You want to explore a contested topic fairly** → Dialectical
- **You want to trace how an idea developed** → Historical-Genealogical
- **You want question-driven inquiry** → Socratic Exploration
- **You want to test conventional understanding** → First Principles Analysis
- **You want claim-by-claim epistemic annotation** → Annotated Critical Analysis

### Step 2: Provide the Generator as a System Prompt

In VS Code Copilot, paste the entire generator prompt as the system prompt or initial instruction. Each generator is self-contained — it includes its architecture, phase protocol, write chunk map, validation checklist, and reference materials.

### Step 3: Provide Input in the Required Format

Every generator expects this exact input format:

```
Generate a report on: [TOPIC]
Generate Report Here: [FULL_DIRECTORY_PATH]
Wiki-links/Permanent Notes List Location: [FULL_PATH_TO_WIKI_LINKS_FILE]
```

**Example:**
```
Generate a report on: Behavioral activation in CBT for major depressive disorder
Generate Report Here: D:/10_pur3v4d3r's-vault/30_outputs/reports
Wiki-links/Permanent Notes List Location: D:/10_pur3v4d3r's-vault/00_index/permanent-notes-index.md
```

The generator will:
1. Parse these inputs
2. Build a wiki-link index from the permanent notes file
3. Run the 9-phase blueprinting and generation protocol
4. Write the final report to the output directory using the Append-Marker Chain

### Step 4: Let the Phased Protocol Run

**Do not interrupt the generator mid-phase.** The protocol is designed as a single continuous execution. Each generator includes:

- **Phase 0:** Input parsing
- **Phase 1:** Wiki-link index construction
- **Phase 2:** Blueprint (architecture selection, scope, density planning)
- **Phase 3:** File creation with YAML frontmatter
- **Phase 4:** Main body generation (multiple writes via Append-Marker Chain)
- **Phase 5:** Integration pass
- **Phase 6:** Far Transfer section
- **Phase 7:** Synthesis
- **Phase 8:** Enhanced Appendix (12 subsections)
- **Phase 9:** Final validation

Checkpoint gates between phases verify the running tallies (word count, callout count, wiki-link count) and decide whether to proceed or remediate.

---

## What to Expect During Generation

### Running Tallies

The generator tracks its progress against density targets throughout. You will see updates like:

```
RUNNING TALLIES:
- Wiki-links placed: 23 / ≥40
- Callouts placed: 18 / ≥30
- Word count: 6,400 / ≥10,000
- File writes completed: 4
- Current marker: MARKER_005
```

These are normal. They are how the generator self-monitors.

### Multiple Tool Calls

Expect **10–13 total file operations** depending on the generator:
- 1 × `create_file` (Phase 3)
- 9–12 × `replace_string_in_file` (one per content chunk)

Each operation is small and fast. Do not be alarmed by the number — this is the architecture working as intended.

### Mid-Generation Checkpoints

The generator will pause at midpoint gates to verify density. If targets are missed, it will remediate before continuing. This is by design.

---

## Troubleshooting

### "The file already exists" error on Step 0

**Cause:** A previous generation attempt left the file in place.

**Fix:** Delete or rename the existing file. Re-run the generator. The generator does not overwrite existing files by default — this is a safety feature.

### `replace_string_in_file` fails with "no match found"

**Cause:** The marker was already consumed by a previous write, or the file was modified out of band, or the LLM tried to match something other than the marker.

**Fix:**
1. Open the file and check which marker is currently present
2. Tell the generator: "The current marker in the file is `MARKER_00X`. Continue from there."
3. If no marker is present, the file is in an undefined state — start over

### The generator tries to write a large `oldString`

**Cause:** The LLM has drifted from the Append-Marker Chain protocol.

**Fix:** Stop the generation. Remind the model: *"You must use the Append-Marker Chain protocol. The `oldString` is ALWAYS just the marker comment, never surrounding content. Reread the Append-Marker Chain section of the generator prompt."*

### Word count falls short of the floor

**Cause:** Specialist density was insufficient, or sections were truncated, or scope was too narrow for the generator type.

**Fix:**
1. Check the validation phase output to identify the shortfall location
2. For Deep Dive generators: verify scope discipline was applied (broad scope → dilute depth)
3. For other generators: instruct the model to expand the deficient sections via additional `replace_string_in_file` operations targeting short unique strings within those sections

### Pipeline extraction fails on the generated file

**Cause:** A pipeline-critical callout was malformed, or the YAML frontmatter is missing the `doc_type` field.

**Fix:**
1. Verify the YAML frontmatter contains `doc_type: "[Report Type Name]"`
2. Verify `[!definition]`, `[!original-synthesis]`, `[!cite]`, `[!connections-and-links]`, and `[!further-exploration]` callouts use exact lowercase syntax
3. Verify the `[!connections-and-links]` callout contains all four required categories: Upstream, Downstream, Lateral, Strengthened

### Copilot stops before all writes complete

**Cause:** Context window pressure or response budget exhaustion.

**Fix:** Instruct Copilot to resume from the current marker. The Append-Marker Chain is **resumable** — as long as the file exists and contains a marker, generation can continue from that point. Tell the model: *"Resume generation from the current marker in the file. Continue with the next chunk per the Write Chunk Map."*

---

## The Multi-Pass Philosophy

These generators are not designed as single-shot tools. They are designed as **multi-pass orchestration** where each pass has a bounded purpose:

| Pass | Purpose | Tool Operations |
|------|---------|-----------------|
| **Pass 0** | Create file with YAML | 1 × `create_file` |
| **Passes 1–N** | Generate body content | N × `replace_string_in_file` (one per chunk) |
| **Integration pass** | Densify, cross-link | 0–3 × targeted `replace_string_in_file` |
| **Appendix passes** | Build the 12-section appendix | 3 × `replace_string_in_file` |
| **Validation pass** | Check density, fix gaps | 0–N × targeted `replace_string_in_file` |

**Why multi-pass works where single-shot fails:**

1. **Context locality:** Each pass focuses on a bounded section. The model doesn't need to hold the entire 10,000-word document in working memory.
2. **Resumability:** If any pass fails, the file is in a known state with a known marker. Resume from there.
3. **Auditable progress:** Running tallies after each pass make density targets visible and remediable.
4. **Bounded failure:** A failed pass affects only its chunk. Other content is not corrupted.

**The trade-off:** Multi-pass takes more total tool calls than a hypothetical single-shot would. This is the correct trade — the alternative is silent truncation, undetected gaps, and corrupted files.

---

## A Note for LLM Operators

If you are an LLM reading this document because you have been asked to execute one of the generators, here is what you need to internalize:

1. **You will be tempted to write the entire report in one tool call.** Do not do this. It will fail.
2. **You will be tempted to use large `oldString` values to update existing content.** Do not do this. It will fail.
3. **You will be tempted to skip the blueprint phase and start writing immediately.** Do not do this. The blueprint is what makes the body coherent.
4. **You will be tempted to truncate later sections (synthesis, appendix) to "save tokens."** Do not do this. The constitutional depth mandate exists because earlier versions of these prompts produced exactly that failure.
5. **Trust the protocol.** The Append-Marker Chain looks tedious. It is the only thing standing between you and a corrupted file. Follow it exactly.
6. **Read the entire generator prompt before starting Phase 0.** The Write Chunk Map tells you in advance how many writes to plan for. The validation checklist tells you what "done" looks like.

When in doubt, the rule is: **smaller writes, simpler `oldString` targets, more tool calls.** Never the opposite.

---

## Files in the Suite

```
foundational-report-generator-v2.0.md
annotated-critical-analysis-generator-v2.0.md
practitioners-field-guide-generator-v2.0.md
dialectical-report-generator-v2.0.md
comparative-architecture-generator-v2.0.md
historical-genealogical-generator-v2.0.md
socratic-exploration-generator-v2.0.md
first-principles-analysis-generator-v2.0.md
deep-dive-report-generator-v2.0.md
```

Each is a self-contained system prompt. Deploy the one matching your need.

---

## Quick Reference: Deployment Checklist

Before invoking a generator, verify:

- [ ] Output directory exists and is writable
- [ ] Wiki-links/permanent notes index file exists at the specified path
- [ ] No file with the expected output filename already exists in the output directory
- [ ] The generator prompt is provided as system prompt (not user message)
- [ ] Input format follows the three-line specification exactly
- [ ] You have not added conflicting instructions that override the generator's protocol
- [ ] You are prepared to let the protocol run uninterrupted through all 9 phases

If all boxes are checked, the generator should execute cleanly. If something fails, consult the Troubleshooting section above and resume from the current marker.

---

## Version

**Suite v2.0** — All nine generators, shared Append-Marker Chain protocol, shared Enhanced 12-section Appendix, full pipeline_v2.py compatibility.

This guide describes the deployment and operational characteristics common to all nine generators. Generator-specific architecture details are in each generator's own prompt file.
