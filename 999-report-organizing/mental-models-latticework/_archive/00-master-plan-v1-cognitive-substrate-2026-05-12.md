---
# ═══════════════════════════════════════════════════════════════
# CORE IDENTITY
# ═══════════════════════════════════════════════════════════════
title: "Mental Models Latticework Section — Master Build-Out Plan"
aliases:
  - "Mental Models Section Plan"
  - "Mental Models Latticework Roadmap"
  - "MM Section Build Plan"
type: project-plan
status: budding
confidence: high

# ═══════════════════════════════════════════════════════════════
# CLASSIFICATION
# ═══════════════════════════════════════════════════════════════
tags:
  - project-plan
  - mental-models
  - latticework
  - section-buildout
  - sequential-prompting
  - agent-roadmap

# ═══════════════════════════════════════════════════════════════
# TEMPORAL
# ═══════════════════════════════════════════════════════════════
created: 2026-05-12
updated: 2026-05-12
target-completion: rolling (multi-session)

# ═══════════════════════════════════════════════════════════════
# PROJECT METADATA
# ═══════════════════════════════════════════════════════════════
project-id: "mm-latticework-2026-05"
executor: "copilot-agent (Claude Opus 4.7)"
session-style: sequential-decomposed
estimated-sessions: 14
priority: high

# ═══════════════════════════════════════════════════════════════
# SOURCE MATERIAL
# ═══════════════════════════════════════════════════════════════
primary-sources:
  - "[[mental-models-foundational-report-2026-05-10]]"
  - "[[mental-models-johnson-laird-foundational-report-2026-03-11]]"
  - "[[mental-models-johnson-laird-first-principles-report-2026-03-11]]"
  - "[[mental-model]] (existing v6-elaborated draft)"
related-mocs:
  - "[[moc-cognitive-architecture-learning-science]]"
  - "[[moc-reasoning-critical-thinking-epistemology]]"
  - "[[moc-motivation-agency-self-regulation]]"
---

# 🗺️ Mental Models Latticework Section — Master Build-Out Plan

> [!abstract] Purpose
> A meticulously decomposed, multi-session execution plan for populating a comprehensive **Mental Models Latticework** section in the vault. Each session is self-contained and agent-executable by a copilot-agent (running Claude Opus 4.7). The plan integrates the user's original specification with two original frameworks from `[[mental-models-foundational-report-2026-05-10]]` — the **Three-Layer Quality Framework** (fidelity / tractability / transferability) and the **Latticework Density Heuristic** — to ensure each note is not merely informational but cultivates genuine cross-domain reasoning capacity.

---

## 0. Plan Overview

### 0.1 What This Plan Improves Upon the Original Specification

The user's seed specification listed required note sections (definition, related concepts, boundaries, visuals, examples, research, related models, personal notes, pitfalls, exercises, case studies) and two YAML schemas. This plan extends that foundation in eight specific ways:

| # | User's Original | Enhancement | Rationale |
|---|----------------|-------------|-----------|
| 1 | Two competing YAML templates | **Single unified schema** merging both | Eliminates ambiguity; one source of truth |
| 2 | "Related models" as a list | **Latticework Density Requirement**: ≥3 cross-domain structural links per note with explicit *structural correspondence* annotation | Implements the Density Heuristic from the foundational report; prevents orphan-by-domain |
| 3 | Implicit quality bar | **Three-Layer Quality Rubric** (fidelity / tractability / transferability) explicitly evaluated per note | Operationalizes the report's original contribution; gives the agent a measurable target |
| 4 | "Boundaries / contexts" callout | **Two callouts**: `[!boundary]` (scope of valid application) + `[!warning]` (over-modeling pathology / when *not* to use) | The foundational report's most actionable insight: knowing where a model fails is more valuable than knowing where it succeeds |
| 5 | "Real-world examples" | **Tiered examples**: 1 canonical + 1 personal + 1 *far-transfer* example from a non-obvious domain | Forces transferability dimension; exercises the latticework |
| 6 | Implicit epistemic status | **Per-claim epistemic tagging** (`established` / `well-motivated` / `speculative` / `personal-conjecture`) | Matches the methodology of the source reports; prevents AI hallucination from masquerading as fact |
| 7 | Single MOC envisioned | **MOC + Domain Sub-MOCs + Latticework Map** (Mermaid graph) | Mirrors actual vault MOC architecture; enables Dataview queries by discipline |
| 8 | Sequential one-at-a-time | **Phased execution with Reflexion checkpoints** between phases | Allows mid-course correction; learns from earlier sessions to improve later ones |

### 0.2 Architectural Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| **Note location (CANONICAL)** | `999-report-organizing/_permanent-notes/v6-llm-elaborated/mental-models/` (flat, kebab-case filenames) | Dedicated project subfolder under the v6 LLM-elaboration pipeline output tree; isolates Mental Models Latticework work from other v6 pipeline artifacts |
| **Legacy location (DEPRECATED)** | `03-notes/01_permanent-notes/` — older folder predating the v6 pipeline | Phase 1–3 notes (13 files) were written here in error; migration decision pending — see Session 7 hand-off §10 |
| **v6 root location (NOT this project)** | `999-report-organizing/_permanent-notes/v6-llm-elaborated/*.md` (root) | General v6 pipeline output; some entries overlap with mental-models scope (e.g. `anchoring-bias.md`, `loss-aversion.md`, `mental-model.md`) and require per-note conflict reconciliation |
| **No further nesting** in mental-models/ | Filename prefix not required; categorization via `domain` and `tags` YAML fields | Avoids breaking wiki-link conventions; Dataview can filter by tag |
| **MOC location** | `07-mocs/moc-mental-models-latticework.md` | Conforms to existing MOC naming pattern |
| **Domain sub-MOCs** | One per discipline, e.g. `07-mocs/sub/moc-mm-cognitive-science.md` | Keeps top-level MOC navigable; enables drill-down |
| **Project staging** | This plan + per-session logs at `02-projects/mental-models-latticework-section/` | Standard project structure |
| **Anti-duplication** | Every session prompt mandates `vscan` before any note creation; **also** check (a) v6-llm-elaborated root, (b) mental-models/ subfolder, (c) legacy 03-notes/01_permanent-notes/ for pre-existing entries | Vault rule; non-negotiable |

### 0.3 Phase Map

```
PHASE 1: Foundation         ── Sessions 1–2  ── Template, MOC scaffold, hub note
PHASE 2: Core Latticework   ── Sessions 3–4  ── 8 cross-domain "load-bearing" models
PHASE 3: Cognitive Science  ── Sessions 5–6  ── Memory/representation/reasoning models
PHASE 4: Decision/Behavior  ── Sessions 7–8  ── Heuristics, biases, decision frameworks
PHASE 5: Systems/Physics    ── Session  9    ── Feedback, equilibrium, scaling, second-order
PHASE 6: Economics/Bio      ── Session 10    ── Selection, opportunity cost, competition
PHASE 7: Math/Philosophy    ── Session 11    ── Inversion, first-principles, Bayes
PHASE 8: Densification      ── Session 12    ── Cross-link audit, reciprocal links
PHASE 9: Visual enrichment  ── Session 13    ── Mermaid/ASCII pass on all notes
PHASE 10: Validation        ── Session 14    ── linkcheck, orphan, metaudit, quality scoring
                                              + Reflexion → propose Phase 11+ expansion
```

---

## 1. Curated Mental Models Taxonomy

> [!principle-point] Selection Criterion
> Each model included must satisfy: **(a)** strong existing wiki-link presence in `wiki-links.md` (high latticework integration potential), **(b)** coverage in at least one of the three primary source reports, and **(c)** *cross-domain structural correspondence* with at least 2 other models in this list.

### 1.1 Phase 2 — Core Latticework (8 load-bearing models)

These 8 are first because they are *connector-models* — referenced from many other models across domains. Building them first means subsequent notes can wiki-link to live targets rather than ghost links.

| # | Note Filename | Discipline | Why First |
|---|---------------|-----------|-----------|
| 1 | `mental-model.md` | Cognitive Science (meta) | The hub concept; defines the framework |
| 2 | `latticework-of-mental-models.md` | Munger / interdisciplinary | The compositional principle |
| 3 | `first-principles-thinking.md` | Philosophy / engineering | Within-model reasoning complement |
| 4 | `second-order-thinking.md` | Decision theory | Consequences-of-consequences |
| 5 | `inversion.md` | Mathematics / Munger | "Invert, always invert" |
| 6 | `feedback-loop.md` | Systems theory / cybernetics | Causal architecture primitive |
| 7 | `opportunity-cost.md` | Economics | Trade-off primitive |
| 8 | `map-vs-territory.md` | Korzybski / epistemology | The model-reality distinction itself |

### 1.2 Phase 3 — Cognitive Science (6 models)

| Filename | Concept |
|----------|---------|
| `schema-theory.md` | Bartlett/Piaget patterned expectations |
| `chunking.md` | Miller/Chase-Simon expertise compression |
| `working-memory.md` | (likely exists; verify) capacity-bound assembly |
| `mental-simulation.md` | Running-the-model operation |
| `dual-process-theory.md` | System 1 / System 2 |
| `predictive-coding.md` | Friston / hierarchical generative models |

### 1.3 Phase 4 — Decision / Behavioral (6 models)

| Filename | Concept |
|----------|---------|
| `confirmation-bias.md` | Self-sealing model failure mode |
| `availability-heuristic.md` | Tversky-Kahneman recall-as-frequency |
| `anchoring-and-adjustment.md` | Reference-point dependence |
| `loss-aversion.md` | (exists; verify) prospect theory |
| `expected-value.md` | Probability-weighted outcomes |
| `prospect-theory.md` | Kahneman-Tversky reference-dependent utility |

### 1.4 Phase 5 — Systems / Physics (5 models)

| Filename | Concept |
|----------|---------|
| `homeostasis-and-equilibrium.md` | Self-regulating dynamics |
| `compounding.md` | Exponential growth / interest |
| `critical-mass.md` | Phase transition / threshold dynamics |
| `entropy.md` | Disorder / information loss |
| `leverage-and-fulcrum.md` | Mechanical advantage as decision metaphor |

### 1.5 Phase 6 — Economics / Biology (5 models)

| Filename | Concept |
|----------|---------|
| `natural-selection.md` | Variation-selection-retention algorithm |
| `comparative-advantage.md` | Ricardian specialization |
| `supply-and-demand.md` | Equilibrium price discovery |
| `red-queen-dynamics.md` | Co-evolutionary running-to-stand-still |
| `niche-construction.md` | Organism-environment co-modification |

### 1.6 Phase 7 — Mathematics / Philosophy (5 models)

| Filename | Concept |
|----------|---------|
| `bayesian-updating.md` | Posterior = likelihood × prior |
| `base-rate-neglect.md` | Failure mode of Bayesian intuition |
| `regression-to-the-mean.md` | Statistical reversion |
| `falsifiability.md` | Popperian scientific demarcation |
| `occams-razor.md` | Parsimony principle |

**Total Phase 2–7 notes: 35 models** (expandable in subsequent phases per Reflexion outputs)

---

## 2. The Standardized Note Template

> [!important]
> This template is the **single source of truth** for every Mental Model note. Sessions 2+ MUST follow it exactly. Saved (Session 1) at `99-system/03-templater/02-templater-master-skeleton-templates/_master-mental-model-note-template-v1.0.0.md`.

### 2.1 YAML Schema (unified)

```yaml
---
# ═══════════════════════════════════════════════════════════════
# CORE IDENTITY
# ═══════════════════════════════════════════════════════════════
title: "{Human-Readable Name}"
aliases:
  - "{Alias 1}"
  - "{Abbreviation if any}"
  - "{Common alternative phrasing}"
type: permanent-note
note-subtype: mental-model
status: budding              # seedling | budding | evergreen | wilting
confidence: high             # low | medium | high

# ═══════════════════════════════════════════════════════════════
# CLASSIFICATION
# ═══════════════════════════════════════════════════════════════
tags:
  - permanent-note
  - mental-model
  - latticework
  - "domain/{primary-discipline}"     # e.g. domain/cognitive-science
  - "subdomain/{subdomain}"           # e.g. subdomain/reasoning
  - "model-type/{type}"               # process | structural | dynamic | normative | descriptive

# ═══════════════════════════════════════════════════════════════
# TEMPORAL
# ═══════════════════════════════════════════════════════════════
created: "{YYYY-MM-DD}"
updated: "{YYYY-MM-DD}"

# ═══════════════════════════════════════════════════════════════
# CLASSIFICATION & DISCOVERY (Pipeline-Compatible)
# ═══════════════════════════════════════════════════════════════
domain: "{primary-discipline}"
subdomains: ["{sub-1}", "{sub-2}"]
primary_domain: "{Capitalized Discipline Name}"
secondary_domains: ["{Related-1}", "{Related-2}"]
knowledge_level: "intermediate"     # introductory | intermediate | advanced

# ═══════════════════════════════════════════════════════════════
# THREE-LAYER QUALITY FRAMEWORK (per foundational report)
# ═══════════════════════════════════════════════════════════════
quality:
  fidelity: "{1-5}"           # structural correspondence to modeled domain
  tractability: "{1-5}"       # cost to assemble + run vs. urgency
  transferability: "{1-5}"    # cross-domain structural reach
  composite: "{average}"
  weakest-dimension: "{which of the three}"
  cultivation-target: "{which dimension to invest in next}"

# ═══════════════════════════════════════════════════════════════
# LATTICEWORK INTEGRATION (per foundational report's density heuristic)
# ═══════════════════════════════════════════════════════════════
latticework:
  cross-domain-links: "{integer; MUST be ≥3}"
  structural-analogs:
    - model: "[[other-model-1]]"
      structural-correspondence: "{what structure is shared}"
      cross-domain-problem-illuminated: "{example}"
    - model: "[[other-model-2]]"
      structural-correspondence: "{...}"
      cross-domain-problem-illuminated: "{...}"
    - model: "[[other-model-3]]"
      structural-correspondence: "{...}"
      cross-domain-problem-illuminated: "{...}"

# ═══════════════════════════════════════════════════════════════
# RELATIONSHIPS (vault graph integration)
# ═══════════════════════════════════════════════════════════════
related: ["[[...]]", "[[...]]"]
prerequisites: ["[[...]]"]
specializes: ["[[...]]"]              # this is a more specific case of...
broader: ["[[...]]"]                  # this is a special case within...
contrasts-with: ["[[...]]"]
complements: ["[[...]]"]
enables: ["[[...]]"]
builds-on: ["[[...]]"]

# ═══════════════════════════════════════════════════════════════
# EPISTEMIC & VALIDATION
# ═══════════════════════════════════════════════════════════════
key-researchers: ["{Person-1}", "{Person-2}"]
foundational-citation: "{Author, Year, Work}"
epistemic_status: "well-established" # well-established | well-motivated | speculative | contested
hallucination_check: true             # set true after manual verification

# ═══════════════════════════════════════════════════════════════
# PERSONAL KNOWLEDGE MANAGEMENT
# ═══════════════════════════════════════════════════════════════
review-frequency: monthly             # weekly | monthly | quarterly
mastery-stage: budding                # seedling | budding | evergreen | wilting
importance: high                      # low | medium | high | critical
foundational-for-future-learning: true
source-reports:
  - "[[mental-models-foundational-report-2026-05-10]]"
---
```

### 2.2 Body Structure (mandatory sections, in order)

```markdown
# {Model Name}

> [!definition] {Model Name}
> {1-3 sentence definition that captures structure + dynamics + boundary in a single statement}
> 
> **Defining property**: {what makes this distinctively this model and not something else}
> 
> **See also**: [[link-1]], [[link-2]], [[link-3]]

## In-Depth Definition

{2–4 paragraphs that elaborate the model: its origin, its claim about how some part of the world works, and the operations it supports. Wiki-link aggressively per vault convention. Cite key researchers inline.}

> [!boundary] Scope of Valid Application
> **Applies when**: {conditions under which this model's predictions track observation}
> 
> **Does NOT apply when**: {conditions under which this model's predictions degrade or invert}
> 
> **Domain of original development**: {the discipline where this model was formalized}
> 
> **Far-transfer caveats**: {what breaks when transporting to other domains}

## Mechanism / How It Works

{Step-by-step explanation of the dynamic the model captures. Use numbered steps if the mechanism is sequential; use a Mermaid diagram if the mechanism is branching or networked.}

## Visual Representation

```mermaid
{Mermaid diagram showing the model's structural relationships OR its dynamic operation. Required: at least one diagram per note.}
```

{If Mermaid is insufficient, supplement with an ASCII art diagram in a fenced code block. Include the ASCII version even when Mermaid renders, because some PKB views render only one format.}

## Related Mental Models (Latticework Position)

> [!key-claim] Latticework Density
> This model connects to **N** other models in the vault across **M** disciplines. The most consequential structural correspondences:

- **[[other-model-1]]** — *{structural correspondence}*. Cross-domain problem illuminated: {one concrete example}.
- **[[other-model-2]]** — *{structural correspondence}*. Cross-domain problem illuminated: {one concrete example}.
- **[[other-model-3]]** — *{structural correspondence}*. Cross-domain problem illuminated: {one concrete example}.
- {additional links as warranted}

> [!warning] When NOT to Reach for This Model
> {The over-modeling pathology applied to this specific model — when does deploying this model produce worse outcomes than simply engaging directly with the situation? This callout is mandatory.}

## Real-World Examples

> [!example] Canonical Example ({domain of origin})
> {The textbook case that illustrates the model in its native domain.}

> [!example] Far-Transfer Example ({non-obvious domain})
> {An application of the model in a domain *other* than its native one. The structural correspondence with the canonical case must be explicit. This callout is mandatory and exercises the transferability dimension.}

> [!example] Personal Application
> {Optional but strongly encouraged: a user-generated example from their own life. Initially populated by the agent as a *placeholder* with prompt text inviting the user to fill in.}

## Research & Empirical Foundation

{2-3 paragraphs summarizing the empirical or theoretical basis. Cite primary sources. Distinguish what is established from what is contested.}

> [!cite] {Author, Year}
> {Brief description of the work and its specific contribution to this model's foundation.}

> [!cite] {Author, Year}
> {…}

## Pitfalls & Limitations

> [!warning] Failure Mode 1 — {name}
> {Specific way this model fails, plus the diagnostic signal that the failure is occurring.}

> [!warning] Failure Mode 2 — {name}
> {…}

> [!warning] Self-Sealing Risk
> {Does this model resist falsification? If so, how, and what counter-discipline keeps it honest?}

## Practical Exercises

1. **Identification exercise**: {Prompt the user to identify this model operating in a domain they work in.}
2. **Inversion exercise**: {Prompt the user to apply [[inversion]] — find a case where the *opposite* of this model's prediction holds, and diagnose why.}
3. **Latticework exercise**: {Prompt the user to articulate the structural correspondence between this model and one of its cross-domain analogs from the YAML `latticework.structural-analogs` field.}

## Case Studies (optional — include for high-importance models only)

> [!case-study] {Title}
> {Extended worked example showing the model deployed end-to-end in a real situation.}

## Personal Notes

> [!reflection]
> {Placeholder section. The agent leaves prompts inviting the user to record their own experience, doubts, modifications, or refinements of the model.}

## Three-Layer Quality Self-Assessment

> [!methodology-and-sources]
> - **Fidelity** ({score}/5): {one-sentence justification}
> - **Tractability** ({score}/5): {one-sentence justification}
> - **Transferability** ({score}/5): {one-sentence justification}
> - **Weakest dimension**: {which} → **Cultivation target**: {what investment would strengthen it}

## Source Material

- Primary: [[mental-models-foundational-report-2026-05-10]] (sections {X}, {Y})
- Secondary: [[other-source-1]], [[other-source-2]]

## Connections (Reciprocal Links Audit)

{Auto-populated section listing every note that links *to* this note. Used in Phase 8 (densification) to verify reciprocity. Initially empty; populated by `linkcheck` script output.}
```

### 2.3 Template Quality Gates

A note **PASSES** if and only if:

1. ✅ YAML schema complete (no empty required fields)
2. ✅ `latticework.cross-domain-links ≥ 3`
3. ✅ All 3 structural-analog entries have non-empty `structural-correspondence` and `cross-domain-problem-illuminated`
4. ✅ At least one Mermaid diagram present and syntactically valid
5. ✅ `[!boundary]`, `[!warning] When NOT to Reach for This Model`, and **Far-Transfer Example** callouts all present
6. ✅ At least one `[!cite]` callout with verifiable source
7. ✅ Quality self-assessment scores all three dimensions
8. ✅ All wiki-links are either targets-that-exist OR explicitly marked as `[[ghost-link-name]]` ghost links scheduled for future creation
9. ✅ No content claims epistemic status higher than the source supports
10. ✅ Note word count: 800–2500 words (atomic-but-rich)

---

## 3. Reusable Per-Session Agent Prompt

> [!important]
> This is the canonical session prompt. Substitute the bracketed `{{...}}` variables for each session. Save as `02-projects/mental-models-latticework-section/_session-prompt-template.md`.

```markdown
# Mental Models Section Build — Session {{SESSION_NUMBER}} of {{TOTAL_SESSIONS}}

## Your Role
You are a copilot agent (Claude Opus 4.7) executing one phase of the Mental Models Latticework section build-out for the user's Obsidian PKB at `d:\10_pur3v4d3r's-vault`. You operate under the rules of the master plan at `02-projects/mental-models-latticework-section/00-master-plan.md` — read it before doing anything else.

## Session Objective
{{ONE-SENTENCE GOAL — e.g. "Create permanent notes for `inversion.md`, `second-order-thinking.md`, and `opportunity-cost.md` following the standardized template."}}

## Mandatory Pre-Flight Steps
1. **Read the master plan** at `02-projects/mental-models-latticework-section/00-master-plan.md` (sections 2 and 3 specifically).
2. **Read the standardized template** at `99-system/03-templater/02-templater-master-skeleton-templates/_master-mental-model-note-template-v1.0.0.md`.
3. **Read the previous session's hand-off note** at `02-projects/mental-models-latticework-section/session-{{N-1}}-handoff.md` (if N > 1).
4. **Run anti-duplication check** for each proposed note name: `vscan "{{model-name}}"`. If a note exists, STOP and append/refactor instead of creating.
5. **Verify wiki-link targets** — for every wiki-link you intend to use, check whether the target note exists. If not, mark it `[[ghost-{name}]]` per master plan §2.3.

## Source Material You MUST Consult
- `999-report-organizing/__pur3v4d3r-house-voice-reports/mental-models-foundational-report-2026-05-10.md` — primary; read at minimum the Lexicon (A.1), Key Figures (A.2), and the section(s) most relevant to this session's models.
- `999-report-organizing/claude-project-reports-generated/mental-models-johnson-laird-foundational-report-2026-03-11.md` — for Johnson-Laird-derived models (mental-simulation, model-construction).
- `999-report-organizing/_permanent-notes/v6-llm-elaborated/mental-model.md` — staging draft to mine.
- `wiki-links.md` — confirm naming conventions and existing targets.

## Deliverables for This Session
{{LIST OF SPECIFIC FILES TO CREATE/MODIFY, e.g.:
1. CREATE `999-report-organizing/_permanent-notes/v6-llm-elaborated/mental-models/inversion.md`
2. CREATE `999-report-organizing/_permanent-notes/v6-llm-elaborated/mental-models/second-order-thinking.md`
3. CREATE `999-report-organizing/_permanent-notes/v6-llm-elaborated/mental-models/opportunity-cost.md`
4. UPDATE `07-mocs/moc-mental-models-latticework.md` — add the 3 new entries to the appropriate domain section
5. CREATE `02-projects/mental-models-latticework-section/session-{{N}}-handoff.md` summarizing what was done and what the next session must know
}}

## Quality Bar (per master plan §2.3)
Every note you produce MUST pass all 10 quality gates. Self-audit before considering the session complete.

## Constraints
- Use the standardized YAML schema EXACTLY. Do not improvise field names.
- Use kebab-case for all wiki-link targets.
- Cite the foundational report by its full wiki-link `[[mental-models-foundational-report-2026-05-10]]`.
- Every claim of empirical fact must be traceable to a source listed in the foundational report's reference section (A.4) or to one of the Johnson-Laird reports.
- If you encounter a claim you cannot verify, mark it explicitly: `[unverified — needs source]`. Do NOT fabricate citations.
- Each note must satisfy `latticework.cross-domain-links ≥ 3` with substantive structural correspondences (not "both involve thinking" — actual mappable structure).

## Reflexion Prompt (mandatory at end of session)
Before producing the hand-off note, reflect:
1. Which of the {{N}} notes was hardest to produce? Why?
2. Did any quality gate fail on first attempt? What was the root cause?
3. What ghost links did you create that the next session must address?
4. Is the latticework density actually being built, or are notes accumulating in isolation? Cite specific cross-domain links you authored as evidence.
5. What should the next session do differently based on what you learned?

Append answers to the hand-off note under a `## Reflexion` section.

## Hand-Off Note Template
```yaml
---
session: {{N}}
date: {{YYYY-MM-DD}}
executor: copilot-opus-4.7
notes-created: [...]
notes-modified: [...]
ghost-links-created: [...]    # to be resolved in later sessions
quality-gate-failures: [...]
next-session-prerequisites: [...]
---

## What Was Accomplished
...

## Reflexion
...

## Hand-Off to Session {{N+1}}
...
```

## Forbidden Operations
- Do NOT delete or rename any existing files outside `02-projects/mental-models-latticework-section/`.
- Do NOT modify the source reports in `999-report-organizing/`.
- Do NOT skip the `vscan` anti-duplication step.
- Do NOT mark a note as `evergreen` status — new notes are `budding` at most.
- Do NOT invent citations or fabricate empirical claims.
```

---

## 4. Session-by-Session Roadmap

### Session 1 — Foundation (Template + MOC Scaffold)
**Deliverables**:
1. CREATE `99-system/03-templater/02-templater-master-skeleton-templates/_master-mental-model-note-template-v1.0.0.md` (the canonical template from §2 above)
2. CREATE `07-mocs/moc-mental-models-latticework.md` (scaffold with empty discipline sections + Mermaid placeholder for the latticework graph)
3. CREATE `02-projects/mental-models-latticework-section/session-1-handoff.md`
4. Run `vscan "mental model"` and `vscan "latticework"`; document existing related notes in hand-off

### Session 2 — Hub Note (`mental-model.md`)
**Deliverables**:
1. CREATE/EXTEND `999-report-organizing/_permanent-notes/v6-llm-elaborated/mental-models/mental-model.md` — the meta-concept hub note. The v6 root entry already exists from the elaboration pipeline; refine into the project subfolder against foundational report Section 1 + A.1 lexicon to meet master-plan §6 quality gates. This is the most-linked node in the lattice; quality must be exemplary.
2. UPDATE the MOC to feature this as the central node
3. Hand-off

### Sessions 3 & 4 — Phase 2 (Core Latticework, 4 notes each)
- **Session 3**: `latticework-of-mental-models.md`, `first-principles-thinking.md`, `inversion.md`, `map-vs-territory.md`
- **Session 4**: `second-order-thinking.md`, `feedback-loop.md`, `opportunity-cost.md`, plus latticework cross-link audit between all 8 Phase-2 notes

### Sessions 5 & 6 — Phase 3 (Cognitive Science, 3 notes each)
- **Session 5**: `schema-theory.md`, `chunking.md`, `mental-simulation.md`
- **Session 6**: `dual-process-theory.md`, `predictive-coding.md`, `working-memory.md` (verify-then-update if exists)

### Sessions 7 & 8 — Phase 4 (Decision/Behavioral, 3 notes each)
- **Session 7**: `confirmation-bias.md`, `availability-heuristic.md`, `anchoring-and-adjustment.md`
- **Session 8**: `prospect-theory.md`, `expected-value.md`, `loss-aversion.md` (verify-then-update if exists)

### Session 9 — Phase 5 (Systems / Physics, 5 notes)
`homeostasis-and-equilibrium.md`, `compounding.md`, `critical-mass.md`, `entropy.md`, `leverage-and-fulcrum.md`

### Session 10 — Phase 6 (Economics / Biology, 5 notes)
`natural-selection.md`, `comparative-advantage.md`, `supply-and-demand.md`, `red-queen-dynamics.md`, `niche-construction.md`

### Session 11 — Phase 7 (Math / Philosophy, 5 notes)
`bayesian-updating.md`, `base-rate-neglect.md`, `regression-to-the-mean.md`, `falsifiability.md`, `occams-razor.md`

### Session 12 — Phase 8 (Densification Audit)
**Deliverables**:
1. Run `linkcheck` to identify all ghost links across the 35 notes
2. For each ghost link: either resolve (point to existing note) or create a stub with `status: seedling`
3. For each note: verify reciprocal linking — if A links to B, B should link back to A in `related` or `complements`
4. Update `07-mocs/moc-mental-models-latticework.md` Mermaid graph showing all 35 nodes + edges
5. Compute and document **latticework density metric**: total cross-domain edges / total notes. Target: ≥ 4.0

### Session 13 — Phase 9 (Visual Enrichment Pass)
**Deliverables**:
1. Audit all 35 notes for visual aid quality
2. Add second diagram (ASCII complement to Mermaid) where missing
3. Add structural-correspondence diagrams for the strongest cross-domain pairs (e.g. `feedback-loop` ↔ `compounding`, `natural-selection` ↔ `bayesian-updating`)

### Session 14 — Phase 10 (Validation + Reflexion)
**Deliverables**:
1. Run `linkcheck`, `orphan`, `metaudit` across the section
2. For each note: score against the 10 quality gates; produce a quality report at `02-projects/mental-models-latticework-section/quality-report.md`
3. Compute aggregate **Three-Layer Framework** scores: average fidelity, tractability, transferability across all 35 notes
4. Identify the weakest 5 notes and list specific cultivation actions
5. Reflexion: propose Phase 11+ (next 35 models to add) based on which ghost links have accumulated
6. UPDATE `00-meta/project-tracker.md` to mark this project as Phase 1 complete; outline Phase 2 scope

---

## 5. Duplication Strategy

| Existing Asset | Action |
|----------------|--------|
| `999-report-organizing/_permanent-notes/v6-llm-elaborated/mental-model.md` | **Mine, do not link.** Source material for Session 2 only. The live note is rebuilt from scratch. |
| `999-report-organizing/__pur3v4d3r-house-voice-reports/mental-models-foundational-report-2026-05-10.md` | **Cite as primary source** in every note via `source-reports` YAML field. Do not duplicate its content; extract distilled atomic claims. |
| `99-scripts/synthetic-permanent-note-seeds/briefs/batch-02-cognitive-psychology/mental-model.yaml` | **Reference for additional concept seeds** when expanding beyond the initial 35. |
| Any existing `working-memory.md`, `loss-aversion.md`, etc. (per `wiki-links.md`) | **Verify and update** rather than recreate. Sessions 6 & 8 prompts include explicit "verify-then-update if exists" instructions. |

---

## 6. Quality Gates Per Phase

| Phase | Gate |
|-------|------|
| After Session 1 | Template renders correctly in Obsidian; MOC scaffold has all discipline sections |
| After Phase 2 (Sess 4) | All 8 core notes pass the 10-point quality bar; MOC graph shows 8 nodes with ≥ 16 edges |
| After Phase 3 (Sess 6) | Wiki-links from Phase 2 notes resolve to live targets (no ghost links to Phase 3 concepts) |
| After Phase 4 (Sess 8) | Decision-domain notes link to cognitive-science notes (cross-domain bridge audit) |
| After Phase 8 (Sess 12) | Latticework density ≥ 4.0 cross-domain edges per node average |
| After Phase 10 (Sess 14) | `linkcheck` returns zero broken links; `metaudit` returns zero schema violations; quality report shows ≥ 80% of notes scoring ≥ 4/5 on at least 2 of 3 quality dimensions |

### 6.1 Personal Application Interlude (recurring)

After each phase completion, run a **Personal Application Interlude** before beginning the next phase. The interlude populates Personal Application + Personal Notes blocks across all newly-created phase notes (and any prior placeholders still outstanding).

**Per-note protocol**: ~8–10 min if grep-based on `01_daily-notes/`; ~3–5 min if drafted from project context without grep.

**Quality bar**: *honesty over completeness* — `*Application emerging*` is preferable to a fabricated episode; project-context-drafted content is preferable to a placeholder. Each Personal Application block follows a four-part structure: (a) specific decision/project/conversation/episode, (b) what the model contributed, (c) where it failed or fell short, (d) the resulting update to one's *use* of the model. Each Personal Notes block surfaces 1–3 first-person observations (reading marginalia, half-formed connections, pattern-noticings).

**Closing artifact**: `session-N.5-handoff.md` documenting blocks filled, patterns surfaced across the cross-note pass, and any new note candidates or Phase-8 bridge-annotation candidates generated. **No MOC update required** (interludes do not produce new bridges, but may surface candidate annotations for Phase 8 enrichment).

**Precedent**: Session 6.5 (post-Phase-3) — see [[session-6.5-handoff]].

---

## 7. Improvements Beyond the Original Specification (Detail)

### 7.1 Three-Layer Quality Framework as Evaluation Rubric
Every note carries explicit `quality.fidelity / tractability / transferability` scores. This implements the foundational report's original contribution as an *operational quality bar*, not just descriptive metadata. The agent must justify each score in the body's "Three-Layer Quality Self-Assessment" section, which forces honest evaluation rather than reflexive 5s across the board.

### 7.2 Latticework Density as Connectivity Requirement
The `latticework.cross-domain-links ≥ 3` requirement with explicit `structural-correspondence` annotation prevents the most common failure mode of mental-model collections: accumulating models in isolation. Every note actively participates in the lattice.

### 7.3 Boundary + Over-Modeling Callouts
The mandatory `[!boundary]` and `[!warning] When NOT to Reach for This Model` callouts directly implement Section 6's over-modeling-pathology corrective. This is the single most actionable insight from the foundational report and most mental-model collections completely omit it.

### 7.4 Per-Claim Epistemic Tagging
The `epistemic_status` YAML field plus inline `[!cite]` callouts force the agent to distinguish established findings from speculative extensions. This matches the foundational report's own A.5 methodology note and is the primary defense against AI fabrication.

### 7.5 Far-Transfer Example as Mandatory Section
The mandatory non-obvious-domain example exercises transferability rather than passively asserting it. Notes that cannot produce a far-transfer example reveal that the model's transferability claim is overstated.

### 7.6 Reflexion Checkpoints Between Phases
Each session ends with a Reflexion that informs the next session. This implements the [[reflexion]] reasoning technique from the task-decomposition framework and prevents the same mistake from being made 14 times.

### 7.7 Ghost Link Discipline
Rather than silently breaking the graph or refusing to link to non-existent notes, the agent uses an explicit `[[ghost-{name}]]` convention that downstream sessions resolve. This permits forward-referencing without dishonesty.

### 7.8 MOC + Sub-MOCs + Mermaid Latticework Graph
The single MOC at `07-mocs/moc-mental-models-latticework.md` includes a Mermaid graph visualizing the actual lattice. Discipline sub-MOCs allow drill-down without overwhelming the top-level navigation.

---

## 8. Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| Agent fabricates citations | Per-session prompt explicitly forbids; only sources from foundational report's A.4 references are valid |
| Notes accumulate in isolation (no real lattice) | `latticework.cross-domain-links ≥ 3` quality gate; densification phase audit |
| Quality drift across sessions | Standardized template + 10-point quality bar enforced every session |
| Token budget exhaustion mid-session | Sessions cap at 3-5 notes each; each note is independent |
| User loses context between sessions | Mandatory hand-off notes + Reflexion summary |
| Existing notes get duplicated | Mandatory `vscan` step + verify-then-update sessions for known-existing concepts |
| Over-modeling the over-modeling pathology | Phase-10 Reflexion explicitly asks whether the section itself is an over-modeling failure; willingness to declare "good enough" |

---

## 9. Status & Next Action

> [!helpful-tip] To Begin Execution
> Open a fresh chat with the copilot agent (Claude Opus 4.7) and paste the **Session 1** version of the per-session prompt template (§3 above), with `{{SESSION_NUMBER}} = 1`, `{{TOTAL_SESSIONS}} = 14`, and the Session 1 deliverables list filled in from §4.

**Current status**: Plan complete; awaiting user approval to begin Session 1.

**Proposed first action**: User reviews this plan, approves or requests modifications. On approval, Session 1 is launched with the prompt assembled per §3.

---

## 🔗 Related Topics for PKB Expansion

1. **[[reflexion-protocol-for-multi-session-agent-work]]** — *Connection*: This plan uses Reflexion checkpoints; a generalized protocol would benefit other multi-session builds. *Depth Potential*: full reusable framework. *Knowledge Graph Role*: meta-protocol applicable across all `02-projects/`.

2. **[[latticework-density-metric-formalization]]** — *Connection*: The density heuristic from the foundational report is implemented here as `cross-domain-links ≥ 3`; a more rigorous formalization with weighted edges and disciplinary spread metrics would be valuable. *Depth Potential*: research note bridging knowledge-graph theory and PKM practice. *Knowledge Graph Role*: bridges `[[knowledge-graph-topology]]` with `[[Personal-Knowledge-Management]]`.

3. **[[ghost-link-resolution-workflow]]** — *Connection*: The `[[ghost-{name}]]` convention introduced here needs a vault-wide lifecycle policy. *Depth Potential*: scripted resolution + Dataview surfacing of unresolved ghosts. *Knowledge Graph Role*: closes a known gap in the vault's link-integrity tooling.

4. **[[three-layer-quality-framework-applied-to-non-mental-model-notes]]** — *Connection*: The fidelity/tractability/transferability rubric was developed for mental models but transfers to other note types (frameworks, methods, principles). *Depth Potential*: generalize as a vault-wide quality schema. *Knowledge Graph Role*: extends `[[note-quality-evaluation]]` infrastructure.
