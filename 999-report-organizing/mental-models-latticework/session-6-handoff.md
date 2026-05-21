---
title: "Session 6 Hand-off — Phase 3 Complete; Personal-Application Interlude + Session 7 Launch Spec"
type: project-handoff
project: mental-models-latticework-section
session: 6
phase-completed: 3
phase-next: personal-application-interlude-then-4
status: complete
created: "2026-05-12"
updated: "2026-05-12"
tags:
  - project-handoff
  - mental-models-latticework
  - phase-3-complete
  - session-7-launch
related:
  - "[[00-master-plan]]"
  - "[[session-5-handoff]]"
  - "[[moc-mental-models-latticework]]"
---

# Session 6 Hand-off

## 1. Deliverables

| # | Artifact | Path | Status |
|---|----------|------|--------|
| 1 | `[[mental-simulation]]` | `03-notes/01_permanent-notes/mental-simulation.md` | ✅ |
| 2 | `[[dual-process-theory]]` | `03-notes/01_permanent-notes/dual-process-theory.md` | ✅ |
| 3 | `[[predictive-coding]]` | `03-notes/01_permanent-notes/predictive-coding.md` | ✅ |
| 4 | MOC update — Phase 3 row → 🟢 complete 6/6 | `07-mocs/moc-mental-models-latticework.md` | ✅ |
| 5 | MOC update — Bridges table +12 edges (now 51 total) | `07-mocs/moc-mental-models-latticework.md` | ✅ |
| 6 | This hand-off document | `02-projects/mental-models-latticework-section/session-6-handoff.md` | ✅ |

**Phase 3 = 6/6 (COMPLETE).** Cumulative: 15/35 model notes (43%); 51 declared bridges.

## 2. Per-Note 10-Gate Verification

| Gate | mental-simulation | dual-process-theory | predictive-coding |
|------|---|---|---|
| 1. YAML + quality block | ✅ | ✅ | ✅ |
| 2. ≥3 structural-analogs | ✅ (4) | ✅ (4) | ✅ (4) |
| 3. `[!definition]` callout | ✅ | ✅ | ✅ |
| 4. `[!boundary]` callout | ✅ | ✅ | ✅ |
| 5. `[!warning]` "When NOT…" | ✅ | ✅ | ✅ |
| 6. Mermaid + ASCII | ✅ | ✅ | ✅ |
| 7. Far-transfer `[!example]` | ✅ (NTSB crash investigation) | ✅ (sterile-cockpit + surgical checklist) | ✅ (Bayesian spam filter / VAEs / world models) |
| 8. ≥2 `[!cite]` callouts | ✅ (3 + Gilbert case) | ✅ (3 + Frederick case) | ✅ (3 + Dima case) |
| 9. Three-Layer Quality Self-Assessment | ✅ | ✅ | ✅ |
| 10. Word count 1500–1900 | ✅ (~1850) | ✅ (~1900) | ✅ (~1900) |

**All 30 gates pass.**

**Cluster-internal-density rule** (Session 5 closing requirement): each Session-6 note bridges to at least one Session-5 sibling. Verified:
- `mental-simulation` ↔ `working-memory` ✅; ↔ `mental-model` ✅
- `dual-process-theory` ↔ `working-memory` ✅; ↔ `mental-model` ✅
- `predictive-coding` ↔ `schema-theory` ✅; ↔ `feedback-loop` ✅

## 3. Composite Quality Snapshot

| Note | Fidelity | Tractability | Transferability | Composite | Weakest |
|------|---------|----|----|----|----|
| mental-simulation | 5 | 4 | 5 | 4.67 | tractability |
| dual-process-theory | 4 | 4 | 5 | 4.33 | **fidelity** |
| predictive-coding | 4 | 3 | 5 | 4.00 | tractability |

**Pattern observation — fidelity emerges as a limiting dimension for the first time.** Sessions 1–5 produced uniformly fidelity-5 notes because the underlying constructs were either operationally well-defined (`[[chunking]]`, `[[working-memory]]`) or mature mathematical objects (`[[opportunity-cost]]`, `[[feedback-loop]]`, `[[Bayes-rule]]`-adjacent). Session 6 introduces *theoretically contested* constructs:
- **Dual-process theory** is empirically loose — the Keren & Schul 2009 critique (multiple distinct dichotomies conflated; characteristic clusters do not always co-vary) is unresolved; Kahneman himself caveats that "System 1" and "System 2" are *fictional characters*. Honest fidelity scoring requires a 4, not a 5.
- **Predictive coding** has strong evidence for *some* claims (top-down expectation effects; predictive-coding-style implementation in early visual cortex per Rao-Ballard) but its grand-unifying form (Friston free-energy principle) genuinely strains falsifiability per Williams 2018 / Colombo & Wright 2021. Honest fidelity scoring requires a 4.

Inflating either to 5 would misrepresent the construct's epistemic status. The standard set: **fidelity 5 is not the default — it is *earned* by constructs whose foundations are solid; mature theories with open empirical problems should honestly mark 4.** This complements the chunking-5/5/5 standard from Session 5 (a 5 *survives* explicit self-scrutiny).

The cognitive-science cluster's full quality profile:

| Note | F | T | Tr | Composite | Cultivation class (Q6 stub) |
|------|---|---|----|-----------|-----------------------------|
| schema-theory | 5 | 4 | 5 | 4.67 | hybrid (operation + substrate) |
| chunking | 5 | 5 | 5 | 5.00 | operation |
| working-memory | 5 | 3 | 5 | 4.33 | substrate |
| mental-simulation | 5 | 4 | 5 | 4.67 | operation |
| dual-process-theory | 4 | 4 | 5 | 4.33 | hybrid (taxonomy of operations) |
| predictive-coding | 4 | 3 | 5 | 4.00 | substrate (architecture-level) |

Cluster-mean composite: 4.50. Cluster-mean tractability: 3.83 (lowest of the three layers — confirms the cognitive-science cluster's primary weakness is *cultivation-difficulty*, not fidelity or transferability).

## 4. Reflexion (5 Questions)

**Q1 — What worked well?** The cluster-internal-density rule (Session-6 notes must bridge to Session-5 siblings) produced a *visibly* tight memory-and-process cluster: every Session-6 note declares at least one Session-5 sibling as a structural analog, and the Bridges table now shows the cluster as a recognizable subgraph. The MOC's Phase-3 segment (rows 219–238 in the Bridges table) reads as a coherent sub-architecture rather than a pile of edges.

**Q2 — What was harder than expected?** Calibrating fidelity scores honestly. The temptation, having established a 5-fidelity baseline through Sessions 1–5, was to inflate dual-process-theory and predictive-coding to fidelity-5 to maintain visual uniformity. Resisting this required explicitly defending a 4 in each note's self-assessment block — *the construct itself is partially provisional; the note's fidelity is to the literature including its open problems, but the underlying object is not fully nailed down*. This is the same epistemic move chunking required in the opposite direction (a 5 survives self-scrutiny). **Standard set**: fidelity-5 is earned, not default.

**Q3 — Cross-cutting design pattern recognized?** Phase 3 reveals that the cognitive-science cluster splits along *two* orthogonal axes:
- **Substrate vs. operation** (Q6 from Session 5): is the model a capacity-constraint or an executable process?
- **Construct maturity** (new to Session 6): is the model operationally well-defined or theoretically contested?

The two axes are independent. `[[chunking]]` is operation+mature (composite 5.00); `[[working-memory]]` is substrate+mature (4.33); `[[predictive-coding]]` is substrate+contested (4.00); `[[dual-process-theory]]` is hybrid+contested (4.33). The 2×2 is a cleaner taxonomic frame than the substrate-vs-operation axis alone, and should be captured at Phase 8 densification — possibly as *two* YAML fields (`cultivation-class` + `construct-maturity`) rather than one.

**Q4 — Latticework gain?** With 51 bridges and 15 notes, the cognitive-science cluster is now *visibly the densest sub-architecture* in the lattice. The shape: `[[mental-model]]` and `[[feedback-loop]]` (Phase 1–2 hubs) function as the central junction; the six Phase-3 cognitive-science notes form a tight ring around them; cross-bridges within the cluster (chunking↔WM, schema-theory↔predictive-coding, mental-simulation↔second-order-thinking) make the ring internally dense rather than spoke-shaped. Phase 4 (Decision & Behavior) will branch outward from this dense core — the lattice is now ready for that expansion.

**Q5 — What does this reveal about the master plan?** The Phase-3 split across Sessions 5–6 was correctly calibrated; both sessions hit the 1500–1900 word band and the 10-gate quality bar without strain. The substrate-vs-operation observation from Session 5 has graduated into a 2×2 taxonomic frame in Session 6 — confirming the master plan's *bottom-up* strategy (build notes first, observe taxonomic patterns, formalize at Phase 8) is producing emergent structure that top-down planning would have missed.

**The Personal Application backlog is now substantial enough to interrupt Phase 4.** With 15 notes carrying placeholder Personal Application / Personal Notes blocks, the Q1 follow-up session (originally deferred until "after Session 6") should run *immediately*, before Phase 4 begins. Recommendation below.

## 5. Open Questions Status

| Q | Description | Resolution |
|---|-------------|-----------|
| Q1 | Drafting Personal Application / Personal Notes from daily-note material | **PROMOTED to next session.** 15 notes carry placeholders; the backlog will only grow. Run as a dedicated *Personal Application Interlude* session before Phase 4 begins. See §7. |
| Q4 | Bridges table refactor to per-family layout | **Still scheduled for Phase 8.** With 51 bridges the table is at the upper edge of one-screen scrolling; refactor remains the FIRST task of Phase 8. |
| Q5 | Ghost-link stub-creation (biographical batch) | **Still scheduled for start of Session 7.** Biographical-stub catalog has grown to ~40 candidates (Session 6 added: Johnson-Laird, Stanovich, West, Evans, Sloman, Epstein, Frederick, De Neys, Pronovost, Gawande, Henrich, Heine, Norenzayan, Rao, Ballard, Friston, Andy Clark, Williams, Colombo, Wright, Fletcher, Frith, Sterzer, Dima, Kingma, Welling, Schmidhuber, Ha, Paul Graham, Gilbert, Wilson, Schacter, Hegarty). Estimated 30-minute pass for ~40 one-paragraph stubs. |
| Q6 | Add `cultivation-class` YAML field | **Refined to TWO fields**: `cultivation-class: operation \| substrate \| hybrid` AND `construct-maturity: mature \| provisional \| contested`. The 2×2 classifies the lattice cleanly. Still deferred to Phase 8 — do NOT retrofit mid-build. |
| **Q7 (NEW)** | Personal Application Interlude protocol — what is the operational definition of "Personal Application" and how is the daily-note corpus mined? | **OPEN. Decision needed before the interlude session.** See §7 for proposed protocol. |

## 6. Cumulative Ghost-Link Catalog (Sessions 3–6)

> [!helpful-tip] Biographical stubs are batchable; conceptual stubs are not.

**New from Session 6 (Phase 3 process & inference):**
- *Conceptual*: `[[counterfactual-reasoning]]`, `[[heuristic]]`, `[[deliberation]]`, `[[Cognitive-Reflection-Test]]`, `[[WEIRD-populations]]`, `[[differential-diagnosis]]`, `[[NTSB]]`, `[[HFACS]]`, `[[free-energy-principle]]`, `[[active-inference]]`, `[[Bayesian-inference]]`, `[[variational-autoencoder]]`, `[[world-models]]`, `[[hollow-mask-illusion]]`, `[[motivated-reasoning]]`, `[[fluency-bias]]`, `[[affective-forecasting]]`, `[[prospection]]`
- *Biographical / source-stub*: `[[Johnson-Laird-1983]]`, `[[Kahneman-Tversky-1982]]`, `[[Hegarty-2004]]`, `[[Gilbert-Wilson-2007]]`, `[[Gilbert-1998]]`, `[[Schacter-2007]]`, `[[Stanovich-West-2000]]`, `[[Kahneman-2011]]`, `[[Keren-Schul-2009]]`, `[[Evans-Stanovich-2013]]`, `[[De-Neys-2012]]`, `[[De-Neys-2014]]`, `[[Frederick-2005]]`, `[[Sloman-1996]]`, `[[Epstein-1994]]`, `[[Pronovost-2006]]`, `[[Atul-Gawande]]`, `[[Henrich-Heine-Norenzayan-2010]]`, `[[Rao-Ballard-1999]]`, `[[Friston-2005]]`, `[[Friston-2010]]`, `[[Clark-2013]]`, `[[Williams-2018]]`, `[[Colombo-Wright-2021]]`, `[[Fletcher-Frith-2009]]`, `[[Sterzer-2018]]`, `[[Dima-2009]]`, `[[Karl-Friston]]`, `[[Andy-Clark]]`, `[[Kingma-Welling-2013]]`, `[[Ha-Schmidhuber-2018]]`, `[[Paul-Graham]]`

**Total ghost links cumulative: ~110.** Biographical sub-batch ≈ 50 (Bartlett, Piaget, Rumelhart, Brewer, Treyens, Loftus, Schank, Abelson, Cowan, Baddeley, Hitch, Sweller, Engle, Daneman, Carpenter, Melby-Lervåg, Hulme, Norman, Christopher Alexander, Johnson-Laird, Kahneman, Tversky, Hegarty, Gilbert, Wilson, Schacter, Stanovich, West, Evans, Keren, Schul, De Neys, Frederick, Sloman, Epstein, Pronovost, Gawande, Henrich, Heine, Norenzayan, Rao, Ballard, Friston, Clark, Williams, Colombo, Wright, Fletcher, Frith, Sterzer, Dima, Kingma, Welling, Ha, Schmidhuber, Graham). **Recommend 30-minute biographical-stub batch at start of Session 7** — this closes ~50 ghost links with one-paragraph stubs and substantially de-clutters the graph.

## 7. PROMOTED — Personal Application Interlude (Next Session)

**Decision required**: run the Personal Application Interlude as the **next session** (call it Session 6.5), before Session 7 / Phase 4.

### Rationale

- 15 notes carry placeholder Personal Application + Personal Notes blocks. The backlog grows by ~3 per Phase-3+ session.
- The placeholders are *intentionally* deferred (Q1 from Session 3 onward) to avoid context-switching mid-build; the deferral is now eight sessions deep.
- Phase 4 (Decision & Behavior) is the natural inflection point because (a) the cognitive-science substrate is now complete, providing the conceptual scaffolding the personal applications will draw on; (b) Phase 4 notes themselves are *most likely* to be applied to personal practice (decision frameworks, biases, behavioral heuristics).
- Doing the interlude *before* Phase 4 means Phase 4 notes can be drafted with their Personal Application blocks filled at creation rather than placeholder-deferred.

### Q7 — Personal Application Interlude Protocol (Proposed)

> [!helpful-tip] This protocol is a proposal, not yet ratified. User confirmation expected before the interlude session begins.

**Inputs**:
- The 15 notes' Personal Application + Personal Notes placeholder blocks
- The daily-note corpus at `01_daily-notes/` (~14 months, 200+ entries)
- Task / project / reading marginalia distributed across `00-inbox/`, `02-projects/`, `04-library/`

**Operational definition of "Personal Application"**:
> A *Personal Application* entry records (a) a specific decision, project, conversation, or reading episode in which the model was actively used; (b) what the model contributed (insight, prediction, framing, debiasing); (c) where it failed, fell short, or was misapplied; (d) the resulting update to one's *use* of the model going forward. Distinguished from *Personal Notes*, which are unstructured reading marginalia, half-formed connections, and quotable observations not (yet) tied to specific applications.

**Per-note interlude protocol** (target: 8–10 minutes per note):
1. Grep the daily-note corpus for the note's title + each alias (5-min pass per note)
2. Skim returned entries; flag 1–4 that contain genuine application episodes
3. Distill each flagged entry into 2–4 sentences in the Personal Application block
4. For ungrepped notes (e.g., recently-created notes whose use is still emerging): mark `> *Application emerging — this note has not yet been actively used; will populate after first three months of practice.*` rather than fabricate
5. Personal Notes block: surface 1–3 reading marginalia or half-formed connections from inbox / project files, OR mark `> *Open — reserved for first-person observations as they accumulate.*`

**Quality bar**: *honesty over completeness*. A note with `*Application emerging*` is preferable to a note with a fabricated application episode. Grep-yield governs depth; do not synthesize.

**Estimated session length**: 15 notes × 8–10 min = 2–2.5 hours. Single-session feasible.

**Closing tasks**:
1. Update each of the 15 notes' Personal Application + Personal Notes blocks
2. No MOC update required (this interlude does not produce new bridges)
3. Create `session-6.5-handoff.md` documenting which notes were grep-rich vs. emerging
4. Update master plan §6 to reflect the interlude as a recurring pattern (run after each phase completion, not deferred indefinitely)

## 8. Session 7 Launch Spec — Phase 4 (Decision & Behavior, Notes 1–3 of 6)

> [!attention] Sequencing: the **Personal Application Interlude (§7) runs first**. Session 7 begins only after the interlude is complete.

**Objective**: Author the **first 3 of 6 Phase-4 Decision & Behavior notes**: `[[bias]]`, `[[heuristic]]`, `[[anchoring]]` (perception-and-judgment cluster). The remaining 3 (`[[loss-aversion]]`, `[[social-proof]]`, `[[incentive-caused-bias]]`) run in Session 8.

| # | Note | Suggested Structural-Analogs | Differentiation |
|---|------|-----------------------------|-----------------|
| 1 | `[[bias]]` | `[[mental-model]]`, `[[map-vs-territory]]`, `[[dual-process-theory]]`, `[[heuristic]]` | The umbrella construct. Distinguish between *cognitive bias* (Kahneman-Tversky tradition; deviation from normative reasoning), *statistical bias* (sampling/measurement), and *bias-as-shortcut* (heuristics' useful side). The cross-bridge to `[[map-vs-territory]]` is critical: bias is map-territory error with a systematic vector. |
| 2 | `[[heuristic]]` | `[[dual-process-theory]]`, `[[bias]]`, `[[chunking]]`, `[[mental-model]]` | Gigerenzer's *fast-and-frugal* tradition vs. Kahneman-Tversky's *heuristics-and-biases* tradition — the same cognitive object viewed as adaptive vs. failure-prone. Be careful to fairly represent both. |
| 3 | `[[anchoring]]` | `[[bias]]`, `[[heuristic]]`, `[[predictive-coding]]`, `[[dual-process-theory]]` | The most-replicated cognitive bias; clean operational definition (initial value disproportionately influences subsequent estimate); strong cross-bridge to `[[predictive-coding]]` (anchor functions as a strong prior). |

**Universal Constraints (reaffirmed)**:
- All 10 quality gates apply
- All notes flagged `hallucination_check: true` from creation
- Personal Application blocks: filled at creation if grep-rich (post-interlude), else `*Application emerging*` placeholder
- Word count target: 1500–1900 (band held — confirmed sustainable)
- Each Session-7 note must declare at least one Phase-1 or Phase-2 hub as a structural-analog
- Each Session-7 note should bridge to at least one Phase-3 cognitive-science note (lattice continuity)
- **NEW**: Each Session-7 note must engage *both* Gigerenzer and Kahneman-Tversky traditions (the heuristics-and-biases vs. ecological-rationality split is the defining methodological tension of the Decision & Behavior phase; ignoring it produces shallow notes)
- `linkcheck` deferred to Phase 8

**Session 7 Opening Tasks** (before drafting):
1. **Biographical-stub batch** (~30 min): close ~50 biographical ghost links with one-paragraph stubs. Subjects listed in §6 above. This is its own deliverable and gets logged in the Session 7 hand-off.

**Session 7 Closing Tasks**:
1. MOC update: Phase 4 row → "🟡 in progress | 3 / 6"
2. MOC Bridges table: add 12 new edges (4 per note); total target ~63 bridges
3. Confirm cluster-internal-density rule for Session 8 (each Session-8 note must bridge to at least one Session-7 sibling)
4. Create `session-7-handoff.md` with Phase 4 second-half launch spec (Session 8: `[[loss-aversion]]`, `[[social-proof]]`, `[[incentive-caused-bias]]`)

## 9. Implicit Decisions Carried Forward

- All future notes get `hallucination_check: true` from creation
- **Personal Application blocks**: filled at creation post-interlude (grep-rich) OR `*Application emerging*` (insufficient daily-note material) — *no more indefinite placeholders*
- Composite quality scores must be HONEST — fidelity-5 is *earned*, not default; uniform 5.0 across all dimensions is permissible only if it survives explicit self-scrutiny (chunking standard); mature theories with open empirical problems honestly mark fidelity-4 (dual-process-theory and predictive-coding standard)
- The 2×2 (cultivation-class × construct-maturity) will be retrofitted in Phase 8, NOT mid-build
- Each Phase-4+ note declares at least one Phase-1 or Phase-2 hub as a structural-analog (preserves graph connectivity)
- Each cluster note bridges to at least one prior-cluster sibling (cluster-internal density + cross-cluster continuity)
- Tractability remains the limiting dimension across the lattice except where genuinely earned otherwise
- Phase 8 first task: Bridges table per-family refactor + 2×2 YAML field retrofit
- **NEW**: Personal Application Interlude is a recurring pattern, run after each phase completion (not deferred indefinitely)
- **NEW**: Decision & Behavior notes must engage both Gigerenzer and Kahneman-Tversky traditions

## 10. Status Summary

- ✅ **Phase 1 complete** (foundation: template + MOC + hub note)
- ✅ **Phase 2 complete** (8/8 core latticework connectors)
- ✅ **Phase 3 complete** (6/6 cognitive-science cluster)
- ⏸ **Personal Application Interlude (Session 6.5)** — recommended next, before Phase 4
- ⏸ Phase 4 (Decision & Behavior) — Sessions 7–8
- ⏸ Phases 5–7 pending
- ⏸ Phase 8 (densification) — Session 12; **first task**: Bridges per-family refactor + 2×2 YAML retrofit
- ⏸ Phase 9 (visual enrichment) — Session 13
- ⏸ Phase 10 (validation: linkcheck, vscan, quality report) — Session 14

**Cumulative**: 15 / 35 model notes (43%); 51 declared bridges; ~110 ghost links cataloged (~50 biographical, batchable at Session 7 open); 6 session hand-offs (incl. this).

---

**Next Action**: When user authorizes, **run the Personal Application Interlude (Session 6.5)** per the §7 protocol, mining the `01_daily-notes/` corpus for application episodes across all 15 existing notes. Confirmation requested on the Q7 protocol before the interlude begins. After the interlude, Session 7 opens with the biographical-stub batch, then drafts `[[bias]]`, `[[heuristic]]`, `[[anchoring]]`.
