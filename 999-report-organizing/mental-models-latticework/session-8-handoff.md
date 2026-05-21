---
title: "Session 8 Hand-off — Mental Models Toolkit (Phase A Complete)"
type: session-handoff
session: 8
created: 2026-05-12
updated: 2026-05-12
status: phase-a-complete
supersedes: "[[session-7-handoff]]"
---

# Session 8 Hand-off — Phase A Complete · Phase B Queued

> Paste this whole file into a fresh chat to resume. Sessions 1–7 built a *cognitive-science substrate*; that scope is now retired. This session establishes the **deployable mental-models toolkit** scope and queues Phase A.

---

## 1. What Changed (read first)

- v1 of the plan drifted into cognitive-science theories (`schema-theory`, `chunking`, `working-memory`, `mental-simulation`, `dual-process-theory`, `predictive-coding`) — *theories about how minds build models*, not *models you deploy*.
- User reset the scope: build a **25-entry deployable toolkit** of Mungerian thinking tools usable in daily PKM work.
- v1 master plan archived → `_archive/00-master-plan-v1-cognitive-substrate-2026-05-12.md`
- v2 master plan written → `00-master-plan.md` *(authoritative — read next)*
- 6 cognitive-science notes are now explicitly out-of-scope; they remain in `03-notes/01_permanent-notes/` untouched.
- [[session-7-handoff]] §2–§4 (Phase 4 Decision & Behavior, the 35-note phase map, the "15 / 35" tally) are obsolete.

## 2. Project at a Glance (v2)

- **Project**: Mental Models Toolkit — 25 deployable thinking tools + 2 hub notes
- **Master plan**: [[02-projects/mental-models-latticework-section/00-master-plan.md]] *(v2 — authoritative)*
- **MOC**: [[07-mocs/moc-mental-models-latticework.md]] *(needs Phase D rewrite around 5 categories)*
- **Canonical folder**: `999-report-organizing/_permanent-notes/v6-llm-elaborated/mental-models/`
- **Legacy folder**: `03-notes/01_permanent-notes/` *(8 notes pending migration in Phase A; 6 out-of-scope notes stay)*
- **v6 root**: `999-report-organizing/_permanent-notes/v6-llm-elaborated/*.md` *(5 entries to be mined in Phase B; 4 collisions to reconcile in Phase A)*
- **Total deliverable**: **27 notes** (25 toolkit + 2 hubs)
- **Estimated sessions**: ~10 (Phase A: 1, Phase B: 5, Phase C: 3, Phase D: 1)

## 3. Status (post-Phase-A)

| Bucket | Count | Action |
|---|---|---|
| 🟢 Seeded in `mental-models/` (pending v2-anatomy rewrite) | 8 | user pipeline |
| 🟡 Mine v6-root → write fresh | 5 | **Phase B (next)** |
| 🔴 Create from scratch | 14 | Phase C |
| **Total deliverable** | **27** | — |

**Phase A outcomes (2026-05-12)**: All 4 collisions resolved as `keep-legacy`. 8 legacy notes migrated to `mental-models/`. v6-root originals (`mental-model`, `second-order-thinking`, `first-principles-thinking`, `feedback-loops`) intact as supplementary source.

**Seeded notes** (in `999-report-organizing/_permanent-notes/v6-llm-elaborated/mental-models/`):
1. `mental-model.md` (hub)
2. `latticework-of-mental-models.md` (hub)
3. `inversion.md`
4. `second-order-thinking.md`
5. `opportunity-cost.md`
6. `first-principles-thinking.md`
7. `map-vs-territory.md`
8. `feedback-loop.md`

These were authored against the **v1 cognitive-substrate scope** (heavy structural-analog YAML, ~270–312 lines). They need a rewrite pass against the **v2 deployable-toolkit anatomy** (master-plan §5: What → When to deploy → How → Worked example → Failure mode → Cross-bridges → Source). That rewrite is the user's pipeline, not the agent's.

## 4. Phase B — Resume Here

**Objective**: For each of 5 v6-root entries, read existing v6 content as raw input, supply user a **design brief + ghost-link list** for writing a fresh v2-anatomy entry in `mental-models/`. v6-root originals stay intact.

**Targets**:

| # | v6-root source | Toolkit target | Category |
|---|---|---|---|
| 12 | `confirmation-bias.md` | `confirmation-bias.md` | Bias awareness |
| 14 | `availability-heuristic.md` | `availability-heuristic.md` | Bias awareness |
| 15 | `sunk-cost-fallacy.md` | `sunk-cost-fallacy.md` | Bias awareness |
| 16 | `hindsight-bias.md` | `hindsight-bias.md` | Bias awareness |
| 18 | `emergence.md` | `emergence.md` | Systems & dynamics |

**Phase B step plan**:
1. Agent reads each v6-root source
2. Agent emits per-entry **design brief**: deployable framing, trigger conditions, 2–4 step procedure spec, 1 canonical + 1 PKM-application example sketch, failure-mode point, ≥3 cross-bridge targets within toolkit
3. User decides scope per entry: brief-only (then user writes) or brief + agent-drafted skeleton
4. At Phase B close: write `session-9-handoff.md` and trigger Personal Application Interlude (→ `session-9.5-handoff.md`)

**Standing rules** (binding for all phases):
- Agent does **NOT** draft permanent notes unilaterally — user creates via own pipeline; agent supplies design briefs + ghost-link lists only
- Every file move requires explicit user confirmation per batch
- v6-root originals **stay intact** during Phase B (mined as source, not moved)
- MOC update only at Phase D close — no incremental MOC edits

## 5. Out-of-Scope (Explicit — Do Not Touch)

These remain in `03-notes/01_permanent-notes/` as standalone cognitive-science reference material. They are valid wiki-link *targets* but not toolkit members:

- `schema-theory.md`
- `chunking.md`
- `working-memory.md`
- `mental-simulation.md`
- `dual-process-theory.md`
- `predictive-coding.md`

## 6. Working Conventions (carried forward)

- Filenames: kebab-case, flat (no subfolders inside `mental-models/`)
- YAML schema: per v1 archive §2.1 (preserved as canonical template)
- Note anatomy: per v2 master-plan §5 (1 What → 2 When to deploy → 3 How → 4 Worked example → 5 Failure mode → 6 Cross-bridges ≥3 → 7 Source attribution)
- Length: 600–1200 words per entry
- Quality gates: per v2 master-plan §6 (10 checks)
- Personal Application Interlude protocol (v1 §6.1) **carries forward** — at every Phase close, output `session-N.5-handoff.md`

## 7. New-Session Prompt (copy-paste)

```
Resume Mental Models Toolkit project at Phase B.

Read in order:
1. 02-projects/mental-models-latticework-section/session-8-handoff.md (this file)
2. 02-projects/mental-models-latticework-section/00-master-plan.md (v2 — authoritative)

Then execute Phase B step 1: read the 5 v6-root source files
(confirmation-bias, availability-heuristic, sunk-cost-fallacy,
hindsight-bias, emergence) and emit per-entry design briefs +
ghost-link lists for the v2-anatomy toolkit entries.

Standing rules: agent supplies briefs/lists only — does NOT draft
permanent notes; user creates via own pipeline. v6-root originals
stay intact.
```
