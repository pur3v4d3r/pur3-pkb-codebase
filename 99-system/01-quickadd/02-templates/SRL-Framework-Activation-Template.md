<%*
// ═══════════════════════════════════════════════════════════════════════════
// SRL FRAMEWORK ACTIVATION TEMPLATE v1.0
// Specialized Forethought preparation for reading reports that introduce
// a new theoretical framework to the PKB
// ═══════════════════════════════════════════════════════════════════════════

const frameworkName = await tp.system.prompt("🧬 What framework is being introduced?");
const sourceText = await tp.system.prompt("📖 Source text/report title?");
const sessionDate = tp.date.now("YYYY-MM-DD");
_%>
---
type: srl-framework-activation
framework: "<% frameworkName %>"
source-text: "<% sourceText %>"
date: <% sessionDate %>
status: active
tags:
  - srl-session
  - framework-activation
  - forethought-phase
  - schema-building
  - new-framework
---

# 🧬 Framework Activation: <% frameworkName %>

> [!abstract] Purpose
> This is a specialized [[forethought-phase]] template for the most cognitively demanding reading task: encountering a **new theoretical framework**. New frameworks require the most deliberate preparation because they introduce new conceptual vocabulary, new structural relationships, and potentially new ways of organizing existing knowledge. See [[prior-knowledge-activation]], [[advance-organizers]], and [[schema-accommodation]].

**Source text:** <% sourceText %>
**Date:** <% sessionDate %>

---

## Step 1: Analogical Scaffolding

> [!tip] Connect the unknown to the known. See [[analogical-reasoning]] and [[structure-mapping-theory]].

**What existing framework in my PKB is most structurally similar to this one?**
> [[]]

**In what ways are they likely similar?**
> *(Look for structural parallels — shared components, similar causal logic, analogous distinctions)*

**In what ways does the new framework likely differ?**
> *(This prediction increases engagement — you'll be checking it during reading)*

**Confidence in this analogy (1–10):** ___
> *(Low confidence is fine — the point is activating relevant schema, not being correct)*

---

## Step 2: Theoretical Lineage Search

> [!tip] Situate the framework in intellectual history. See [[philosophical-lineage]].

**Is this framework's intellectual lineage already in my PKB?**
> Check: [[]] [[]] [[]]

**What prior thinkers/models does this framework build on?**
> *(Even a rough guess activates relevant schema)*

**What research tradition does this framework emerge from?**
> 

---

## Step 3: Controversy Anticipation

> [!tip] Predict potential tensions with existing knowledge. This activates deeper processing during reading by creating expectations that need to be checked. See [[Constructive-Attentiveness]].

**What claim would this framework need to make that might tension with something I already believe?**
> 

**What existing PKB concept might this framework challenge or revise?**
> [[]] — potential tension around: 

---

## Step 4: Application Priming

> [!tip] Connect to genuine intellectual need. This activates [[Intrinsic Motivation]] through [[self-determination-theory|autonomy]] and [[relatedness]].

**What problem in my existing PKB or understanding might this framework help address?**
> 

**What question have I been unable to answer that this framework might illuminate?**
> 

---

## Step 5: Vocabulary Pre-Load

> [!tip] Reduce [[Cognitive Load Theory (CLT)|cognitive load]] during reading by pre-activating technical terms. See [[lexical-automaticity]].

**Technical terms likely to appear that I should review:**

| Term | PKB Note (if exists) | Quick Definition |
|------|---------------------|-----------------|
| | [[]] | |
| | [[]] | |
| | [[]] | |

**2-minute PKB search completed?** Yes / No

---

## Step 6: Standard Forethought Goals

### Learning Outcome Goal *(mastery-framed)*
> By the end of this session, I will be able to:

### Comprehension Criterion
> I will know I've achieved this when I can:

### Process Goals
- [ ] PG1: At each major section, write one sentence explaining the framework's core mechanism
- [ ] PG2: Check each framework component against my analogical prediction from Step 1
- [ ] PG3: Flag any term I don't understand rather than glossing over it

### Self-Efficacy (1–10): ___
> *(Schema-sparse reading is expected to be harder — calibrate accordingly)*

---

## Post-Reading: Framework Integration Notes

*(Complete after reading, before the full Self-Reflection Protocol)*

**The framework's core claim/mechanism in one sentence:**
> 

**How my analogical prediction (Step 1) compared to reality:**
> *(Where was the analogy helpful? Where did it mislead?)*

**Controversies/tensions confirmed or disconfirmed (Step 3):**
> 

**New vocabulary that needs permanent notes:**
- [[]] — 
- [[]] — 

**Framework's relationship to existing PKB architecture:**
> Extends / Challenges / Complements / Replaces: [[]]

---

> [!success] Framework Activation Complete
> Proceed to the full [[SRL-Reading-Session-Template]] for the Self-Reflection Phase, or create a new session note incorporating this activation.

---

> [!connections-and-links]
> - [[advance-organizers]] — This template IS an advance organizer for framework learning
> - [[prior-knowledge-activation]] — Steps 1-2 systematically activate prior knowledge
> - [[analogical-reasoning]] — Step 1 uses structural analogy for schema activation
> - [[schema-accommodation]] — New frameworks require accommodation, not just assimilation
> - [[Cognitive Load Theory (CLT)]] — Vocabulary pre-load reduces extraneous load during reading
