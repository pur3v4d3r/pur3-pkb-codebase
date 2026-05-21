---
# ═══════════════════════════════════════════════════════════════
# CORE IDENTITY
# ═══════════════════════════════════════════════════════════════
title: "Mental Models Toolkit — Master Plan v2"
aliases:
  - "Mental Models Plan v2"
  - "Deployable Mental Models Plan"
  - "MM Toolkit Plan"
type: project-plan
status: budding
confidence: high
version: "2.0.0"

# ═══════════════════════════════════════════════════════════════
# CLASSIFICATION
# ═══════════════════════════════════════════════════════════════
tags:
  - project-plan
  - mental-models
  - deployable-toolkit
  - pkm-praxis
  - sequential-prompting

# ═══════════════════════════════════════════════════════════════
# TEMPORAL
# ═══════════════════════════════════════════════════════════════
created: 2026-05-12
updated: 2026-05-12
supersedes: "[[_archive/00-master-plan-v1-cognitive-substrate-2026-05-12]]"

# ═══════════════════════════════════════════════════════════════
# PROJECT METADATA
# ═══════════════════════════════════════════════════════════════
project-id: "mm-toolkit-2026-05"
canonical-folder: "999-report-organizing/_permanent-notes/v6-llm-elaborated/mental-models/"
target-count: 25
priority: high
---

# 🧰 Mental Models Toolkit — Master Plan v2

> [!important] Scope Reset (2026-05-12)
> v1 of this plan drifted into the **cognitive science of mental models** (schema theory, working memory, predictive coding, dual-process theory) — i.e. *theories about how the mind builds models*. That is academically valuable but is not what this project is for.
>
> v2 redefines scope: a curated set of **25 deployable thinking tools** for daily PKM and decision work — the Mungerian latticework, not the cognitive substrate beneath it. Out-of-scope cognitive-science notes (`schema-theory`, `chunking`, `working-memory`, `mental-simulation`, `dual-process-theory`, `predictive-coding`) remain in `03-notes/01_permanent-notes/` as standalone reference material; they are not part of this toolkit.

> [!abstract] Purpose
> Build a **25-entry mental-models toolkit** in `999-report-organizing/_permanent-notes/v6-llm-elaborated/mental-models/`. Each entry is a *thinking tool you would consciously deploy* — at a desk, in a journal, when stuck on a problem — not a description of cognitive machinery.

---

## 1. The Toolkit (25 Entries, 5 Categories)

### 1.1 🧭 Decision-making (5)

| # | Filename | One-line use |
|---|----------|--------------|
| 1 | `inversion.md` | Solve forward by working backward — "what would *guarantee failure*?" |
| 2 | `second-order-thinking.md` | "And then what?" — consequences of consequences |
| 3 | `opportunity-cost.md` | Every yes is a no to everything else |
| 4 | `expected-value.md` | Payoff × probability, summed across outcomes |
| 5 | `margin-of-safety.md` | Build slack against your own wrongness |

### 1.2 🔍 Epistemics & Calibration (6)

| # | Filename | One-line use |
|---|----------|--------------|
| 6 | `first-principles-thinking.md` | Strip to axioms, rebuild from physics not analogy |
| 7 | `map-vs-territory.md` | Your model ≠ reality; mistake-class to recognize |
| 8 | `circle-of-competence.md` | Know the edge of your knowing |
| 9 | `bayesian-updating.md` | Posterior ∝ prior × likelihood; revise on evidence |
| 10 | `base-rates.md` | Prior probabilities beat narrative |
| 11 | `falsifiability.md` | "What evidence would change my mind?" — gate for beliefs |

### 1.3 🧠 Bias Awareness (PKM-Relevant) (5)

| # | Filename | One-line use |
|---|----------|--------------|
| 12 | `confirmation-bias.md` | You find what you already believe — counter via active disconfirmation |
| 13 | `survivorship-bias.md` | You only see the winners — seek the missing failures |
| 14 | `availability-heuristic.md` | Vivid ≠ frequent — recall ease ≠ probability |
| 15 | `sunk-cost-fallacy.md` | Past spend isn't future value — decisions are forward-only |
| 16 | `hindsight-bias.md` | Clarity-after-the-fact is fake — preserve forecasting record |

### 1.4 🔄 Systems & Dynamics (5)

| # | Filename | One-line use |
|---|----------|--------------|
| 17 | `feedback-loop.md` | Reinforcing vs balancing; locate the loop you're in |
| 18 | `emergence.md` | System ≠ sum of parts; behavior at the level of the whole |
| 19 | `bottleneck.md` | Theory of Constraints — slowest step caps everything |
| 20 | `compounding.md` | Exponential beats linear given time |
| 21 | `path-dependence.md` | Early choices constrain later options; lock-in dynamics |

### 1.5 📚 Knowledge-Work Heuristics (4)

| # | Filename | One-line use |
|---|----------|--------------|
| 22 | `pareto-principle.md` | 80% of value from 20% of inputs — find the 20% |
| 23 | `signal-vs-noise.md` | Most data is noise; ratio is the discipline |
| 24 | `chestertons-fence.md` | Don't remove what you don't yet understand |
| 25 | `lindy-effect.md` | The longer it's lasted, the longer it'll last |

**Plus 2 hub notes** (already exist in legacy location — to be migrated):
- `mental-model.md` — the meta-concept (what *is* a mental model, generally)
- `latticework-of-mental-models.md` — Munger's organizing concept

**Total deliverable**: **27 notes** (25 toolkit + 2 hubs) in the canonical folder.

---

## 2. Canonical Locations

```
999-report-organizing/_permanent-notes/v6-llm-elaborated/mental-models/    ← project home (canonical)
├── mental-model.md                          (hub; migrated from legacy)
├── latticework-of-mental-models.md          (hub; migrated from legacy)
├── inversion.md                             ← 25 toolkit entries
├── second-order-thinking.md
├── opportunity-cost.md
├── expected-value.md
├── margin-of-safety.md
├── first-principles-thinking.md
├── map-vs-territory.md
├── circle-of-competence.md
├── bayesian-updating.md
├── base-rates.md
├── falsifiability.md
├── confirmation-bias.md
├── survivorship-bias.md
├── availability-heuristic.md
├── sunk-cost-fallacy.md
├── hindsight-bias.md
├── feedback-loop.md
├── emergence.md
├── bottleneck.md
├── compounding.md
├── path-dependence.md
├── pareto-principle.md
├── signal-vs-noise.md
├── chestertons-fence.md
└── lindy-effect.md

03-notes/01_permanent-notes/                  ← legacy; OUT-OF-SCOPE notes stay here
├── schema-theory.md                          (cognitive science — keep, not toolkit)
├── chunking.md
├── working-memory.md
├── mental-simulation.md
├── dual-process-theory.md
└── predictive-coding.md

02-projects/mental-models-latticework-section/    ← project staging
├── 00-master-plan.md                          (this file)
├── session-N-handoff.md                       (per-session logs)
└── _archive/                                  (v1 plan + retired artifacts)
```

---

## 3. Status Matrix (27 Notes)

Legend: 🟢 done · 🟡 exists in legacy/v6-root, needs migration+rewrite · 🔴 not started · ⚠ collision in v6-root requiring reconciliation

Legend (post-Phase-A): 🟢 seeded in `mental-models/` (pending v2-anatomy rewrite) · 🟡 mine v6-root → write fresh · 🔴 create from scratch

| # | Filename | Status | Notes |
|---|----------|--------|-------|
| H1 | mental-model | 🟢 seeded | legacy version migrated; v6-root original retained as supplementary |
| H2 | latticework-of-mental-models | 🟢 seeded | migrated, no collision |
| 1 | inversion | 🟢 seeded | migrated, no collision |
| 2 | second-order-thinking | 🟢 seeded | legacy version migrated; v6-root retained |
| 3 | opportunity-cost | 🟢 seeded | migrated, no collision |
| 4 | expected-value | 🔴 create | — |
| 5 | margin-of-safety | 🔴 create | — |
| 6 | first-principles-thinking | 🟢 seeded | legacy version migrated; v6-root retained |
| 7 | map-vs-territory | 🟢 seeded | migrated, no collision |
| 8 | circle-of-competence | 🔴 create | — |
| 9 | bayesian-updating | 🔴 create | — |
| 10 | base-rates | 🔴 create | mine v6 `base-rate-neglect` as sibling source |
| 11 | falsifiability | 🔴 create | — |
| 12 | confirmation-bias | 🟡 mine v6 | — |
| 13 | survivorship-bias | 🔴 create | — |
| 14 | availability-heuristic | 🟡 mine v6 | — |
| 15 | sunk-cost-fallacy | 🟡 mine v6 | — |
| 16 | hindsight-bias | 🟡 mine v6 | — |
| 17 | feedback-loop | 🟢 seeded | legacy version migrated; mine v6 `feedback-loops` (plural) as sibling source |
| 18 | emergence | 🟡 mine v6 | — |
| 19 | bottleneck | 🔴 create | — |
| 20 | compounding | 🔴 create | — |
| 21 | path-dependence | 🔴 create | — |
| 22 | pareto-principle | 🔴 create | — |
| 23 | signal-vs-noise | 🔴 create | — |
| 24 | chestertons-fence | 🔴 create | — |
| 25 | lindy-effect | 🔴 create | — |

**Tally (post-Phase-A, 2026-05-12)**:
- 🟢 Seeded in `mental-models/` (pending v2-anatomy rewrite by user): **8**
- 🟡 Mine v6-root → write fresh: **5**
- 🔴 Create from scratch: **14**
- **Total**: **27**

---

## 4. Execution Phases (v2)

### Phase A — Migration & Reconciliation ✅ COMPLETE (2026-05-12)
Moved 8 legacy notes from `03-notes/01_permanent-notes/` into `mental-models/`. All 4 collisions resolved as `keep-legacy`: v6-root originals (`mental-model`, `second-order-thinking`, `first-principles-thinking`, `feedback-loops`) retained intact as supplementary source material. Rewrite to v2 anatomy (§5) deferred to user's pipeline.

### Phase B — Mine + Write (5 sessions, ~5 notes/session)
For the 5 v6-root entries (`confirmation-bias`, `availability-heuristic`, `sunk-cost-fallacy`, `hindsight-bias`, `emergence`): read existing v6 content as raw input, write fresh deployable-tool versions in `mental-models/`. Leave v6-root originals untouched.

### Phase C — Create (3 sessions)
Author the 13 new entries from scratch. Mining sources:
- Primary: [Farnam Street mental-models taxonomy](https://fs.blog/mental-models/), Munger's "Psychology of Human Misjudgement", Shane Parrish "The Great Mental Models" series
- Personal experience integration per master-plan §6.1 protocol

### Phase D — Densification & MOC (1 session)
- Cross-link audit: each note bridges to ≥3 sibling toolkit entries
- Update [moc-mental-models-latticework.md](07-mocs/moc-mental-models-latticework.md) — replace 35-note structure with the 25 + 2 hubs
- Per-category Mermaid map

**Total: ~10 sessions**, much smaller than v1's 14.

---

## 5. Note Anatomy (per-entry minimum)

Each toolkit note answers these in order:

1. **What it is** — one-paragraph operational definition (no jargon)
2. **When to deploy** — concrete trigger conditions ("use when…")
3. **How to use** — 2–4 step procedure, plain language
4. **Worked example** — one canonical, one personal-PKM application
5. **Failure mode / boundary** — when this model misleads
6. **Cross-bridges** — ≥3 wiki-links to sibling toolkit entries with explicit *structural correspondence* annotation
7. **Source attribution** — where the model originates

Aim: ~600–1200 words per entry. Long enough to be operational; short enough to revisit weekly.

YAML schema: inherits from [v1 archive](_archive/00-master-plan-v1-cognitive-substrate-2026-05-12.md) §2.1 — that template is preserved and remains the canonical YAML.

---

## 6. Quality Gates (carried forward from v1, condensed)

A note is done when:

1. ✅ YAML frontmatter complete (title, aliases ≥2, type, status, tags ≥3, related ≥3)
2. ✅ "When to deploy" section with concrete trigger conditions
3. ✅ Worked example: 1 canonical + 1 personal-PKM
4. ✅ `[!boundary]` callout: when this model misleads
5. ✅ ≥3 cross-bridges to sibling toolkit entries with structural annotation
6. ✅ Source attribution (no fabricated citations; mark unverified `[unverified — needs source]`)
7. ✅ Wiki-links resolve (no orphan ghost-links to undefined targets)
8. ✅ `hallucination_check: true` in YAML
9. ✅ Personal Application block filled (no placeholders)
10. ✅ Word count 600–1200

---

## 7. Out-of-Scope Notes (Explicit)

These cognitive-science notes are **NOT** part of this toolkit. They remain in `03-notes/01_permanent-notes/` as standalone reference material. They may be wiki-link *targets* from toolkit entries (e.g. `confirmation-bias` may reference `[[dual-process-theory]]` for mechanism) but they are not toolkit members.

- `schema-theory.md`
- `chunking.md`
- `working-memory.md`
- `mental-simulation.md`
- `dual-process-theory.md`
- `predictive-coding.md`

---

## 8. What Was Done in v1 (Preserved)

The v1 build produced 14 cognitive-science notes in `03-notes/01_permanent-notes/`. Of those:
- **8 are toolkit-relevant** and will be migrated (Phase A): `mental-model`, `latticework-of-mental-models`, `inversion`, `second-order-thinking`, `opportunity-cost`, `first-principles-thinking`, `map-vs-territory`, `feedback-loop`
- **6 are out-of-scope** and stay where they are (per §7)

The 51 ghost-link tokens drafted in Session 7 (then deleted) are **deferred** — toolkit entries may surface a fresh, smaller stub list during Phases B/C as needed.

The Personal Application Interlude protocol (v1 §6.1) **carries forward** to v2: every Phase close triggers a personal-application pass, output `session-N.5-handoff.md`.

---

## 9. Resume Instructions

Next session resumes at **Phase A (Migration & Reconciliation)**:

1. List the 4 collision pairs with side-by-side summaries (legacy vs v6-root)
2. Get user decision per collision
3. Execute migrations
4. Write `session-8-handoff.md` documenting the new state

After Phase A: proceed to Phase B (mine + write the 5 v6-mineable entries).

> [!warning] Standing Rules (binding)
> - Agent does NOT draft permanent notes unilaterally — user creates via own pipeline; agent supplies design briefs + ghost-link lists
> - All file moves require explicit user confirmation per move-batch
> - No deletions of v6-root originals during Phase B (they remain as source material)
> - MOC update only at Phase D close
