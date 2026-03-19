---
title: "The Architecture of the Examined Life: Expansion Topic Registry"
aliases:
  - "Examined Life Expansion Registry"
  - "AEL Expansion Topics"
type: expansion-registry
status: evergreen
confidence: high
doc_id: "examined-life-expansion-topics-registry-v1-0"
doc_type: "expansion-registry"
doc_created: 2026-03-19
doc_modified: 2026-03-19
author: "claude-opus-4"
primary_domain: "knowledge-management"
tags:
  - expansion-registry
  - gap-analysis
  - review-artifact
  - epistemic-cognition
  - pkb-development
source_synthesis: "[[examined-life-synthesis]]"
---

# The Architecture of the Examined Life: Expansion Topic Registry

> [!abstract] Purpose
> Prioritized registry of all expansion topics — existing, proposed by report appendices, and identified through analytical review — organized by priority tier with rationale, connections, effort estimates, and implementation guidance. Serves as the development roadmap for the PKB's next build phase.

---

## Registry Overview

| Category | Count | Status |
|----------|-------|--------|
| Existing expansion topics (in codebase) | 4 | Written but need remediation |
| R15-proposed high-priority topics | 6 | Not yet written |
| Report appendix topics (all reports) | ~60-90 | Not yet written (each report proposes 4-6) |
| Review-identified structural topics | 8 | Not yet written |
| **Total unique expansion candidates** | **~80-100** | **4 written, remainder pending** |

---

## CRITICAL Priority — Structural Remediation

> [!warning] These items address broken infrastructure before new content creation.

> [!topic-idea] **02-reference-library/ Wiki-Link Remediation**
> **Gap Identified:** All 8 notes in `02-reference-library/` contain wiki-links to phantom report filenames from an earlier planning outline. Every link is broken.
> **Where It Would Connect:** All 15 reports, all reference notes, dashboard, index
> **Estimated Effort:** Brief (1-2 hours) — mechanical find-and-replace with correct filenames
> **Value Proposition:** Restores navigability of the entire reference layer. Without this fix, 8 notes are functionally isolated from the knowledge graph.
> **Suggested Approach:** Run bulk find-replace using correction table in synthesis Section 4.2. Then validate with linkcheck script.
> **Priority Rationale:** Nothing else should be built on broken foundations.

> [!topic-idea] **Reference Note Consolidation**
> **Gap Identified:** Two reference note directories exist (`02-reference-library/` at 5.4/10 quality vs. `reference-notes/` at 8.0/10). Subject overlap exists (both cover Hadot, Epictetus, Marcus Aurelius). Content is inconsistent.
> **Where It Would Connect:** All reports, glossary, expansion topics
> **Estimated Effort:** Moderate (3-5 hours) — merge best content from both sets, establish canonical versions
> **Value Proposition:** Eliminates confusion, removes duplication, establishes single authoritative reference layer.
> **Suggested Approach:** For each overlapping source, keep the higher-quality version as base, merge any unique content from the other, deprecate the remainder. Target: single `reference-notes/` directory.

> [!topic-idea] **Dashboard & Navigation Refresh**
> **Gap Identified:** Dashboard reports "0 reference notes" vs. 14 existing. Series Index and Reading Guide are both stale.
> **Where It Would Connect:** All notes (entry point for all navigation)
> **Estimated Effort:** Brief (1-2 hours) — update counts, fix Dataview queries
> **Value Proposition:** Primary navigation entry points currently mislead users about what exists.
> **Suggested Approach:** Update dashboard queries to scan both reference directories. Update Reading Guide with current file count and organization.

---

## CRITICAL Priority — Existing Expansion Topic Remediation

> [!warning] The 4 existing expansion topics need structural fixes before new expansion topics are written. They set the template.

> [!topic-idea] **Expansion Topic YAML Frontmatter Addition**
> **Gap Identified:** All 4 existing expansion topics (`The Stoic Psychology of Emotion`, `The Embodied Mind`, `Knowledge in the Social Arena`, `Attention and Cognitive Control`) lack YAML frontmatter entirely.
> **Where It Would Connect:** Dataview queries, dashboard, metadata system
> **Estimated Effort:** Brief (30 min) — add standardized YAML to each
> **Value Proposition:** Without frontmatter these notes are invisible to Dataview queries and metadata-dependent navigation.

> [!topic-idea] **Expansion Topic Accessibility Remediation**
> **Gap Identified:** All 4 existing expansion topics are written at university-level, violating the series' "Mom Test" accessibility criterion. Reports maintain this standard; expansion topics do not.
> **Where It Would Connect:** Series tone consistency, accessibility goals
> **Estimated Effort:** Substantial (4-6 hours) — rewrite for accessibility while preserving depth
> **Value Proposition:** Aligns expansion topics with the series' core philosophy that rigorous ideas should be accessible to general audiences.
> **Suggested Approach:** Use reports' "family-friendly" voice as exemplar. Rewrite each expansion topic maintaining conceptual depth but eliminating jargon density. Add analogies and concrete examples following the report pattern.

---

## HIGH Priority — R15 Proposed Expansion Topics

> [!important] These 6 topics are explicitly proposed and prioritized by the capstone report (R15) as the most important future directions for the series.

> [!topic-idea] **[[Cross-Cultural Examined Life]]**
> **Gap Identified:** The entire series privileges Western (specifically Greco-Roman and European Enlightenment) philosophical traditions. Buddhist, Confucian, Islamic, Indigenous, and African philosophical traditions of examined living are absent.
> **Where It Would Connect:** R01 (inquiry), R05 (virtue), R08 (character), R12 (social), R15 (integration)
> **Estimated Effort:** Substantial — requires significant research beyond current source base
> **Value Proposition:** The most significant philosophical gap in the entire series. The examined life is not exclusively a Western invention.
> **Suggested Approach:** Start with Buddhist mindfulness ↔ prosoche parallel (strongest bridge), then Confucian self-cultivation ↔ askesis, then broaden.
> **R15 Priority:** Listed as highest priority

> [!topic-idea] **[[Pedagogy of the Examined Life]]**
> **Gap Identified:** The series describes what the examined life IS but provides limited guidance on how to TEACH it. Classroom, workshop, and formal education applications are unexplored.
> **Where It Would Connect:** R04 (learning), R07 (self-regulation), R12 (social), staging note, methodology
> **Estimated Effort:** Substantial
> **Value Proposition:** Translates theoretical framework into educational practice. Enables the series' ideas to spread beyond individual readers.
> **R15 Priority:** Listed as high priority

> [!topic-idea] **[[AI and Cognitive Sovereignty]]**
> **Gap Identified:** No treatment of how AI recommendation systems, language models, and algorithmic curation affect the epistemic autonomy required for examined living.
> **Where It Would Connect:** R03 (autonomy/SDT), R05 (bias), R06 (attention), R12 (social), R13 (PP)
> **Estimated Effort:** Moderate
> **Value Proposition:** Most urgent contemporary extension. Addresses whether the examined life is possible in an algorithmically mediated epistemic environment.
> **R15 Priority:** Listed as high priority

> [!topic-idea] **[[The Examined Life Under Constraint]]**
> **Gap Identified:** The series implicitly assumes conditions of relative privilege — leisure, education, safety, health. No treatment of how poverty, oppression, illness, or systemic disadvantage affect capacity for examined living.
> **Where It Would Connect:** R09 (embodiment — allostatic load), R12 (social — epistemic injustice), R15 (integration)
> **Estimated Effort:** Substantial — requires careful treatment of sensitive material
> **Value Proposition:** Without this, the series risks being an inadvertent guide for the privileged. Existential philosophy has a rich tradition of examined living under extreme constraint (Viktor Frankl, Boethius, Epictetus himself as a former slave).
> **R15 Priority:** Listed as high priority

> [!topic-idea] **[[Neural Substrates of Integrated Wisdom]]**
> **Gap Identified:** Neuroscience is cited frequently but the neural mechanisms of wisdom integration (how the brain synthesizes epistemic, emotional, practical, and social competencies) are not explored directly.
> **Where It Would Connect:** R09 (embodiment), R10 (emotion), R13 (PP), all Tier 1
> **Estimated Effort:** Substantial — requires neuroscience literature review
> **Value Proposition:** Grounds the series' philosophical claims in empirical brain science. Addresses the "so what does this look like in the brain?" question.
> **R15 Priority:** Listed as medium-high priority

> [!topic-idea] **[[Evening Self-Examination Practice Manual]]**
> **Gap Identified:** The series references Seneca's evening self-examination frequently but never provides a complete, practical guide for implementing it as a modern reflective practice.
> **Where It Would Connect:** R07 (self-regulation), R08 (character), R14 (narrative), methodology note, staging note
> **Estimated Effort:** Moderate
> **Value Proposition:** The single most implementable daily practice from the series. Translates 15 reports of theory into a concrete ritual.
> **Suggested Approach:** Three-question protocol from Seneca adapted with modern metacognitive scaffolding. Include journaling prompts, self-assessment rubric, developmental progression.
> **R15 Priority:** Listed as medium priority

---

## HIGH Priority — Review-Identified Topics

> [!topic-idea] **[[Connection Note Architecture]]**
> **Gap Identified:** The `04-connections/` directory is completely empty. MASTER-PLAN calls for 10-15 connection notes exploring cross-tier relationships. Zero have been written.
> **Where It Would Connect:** Every cross-tier relationship (R01↔R09, R05↔R10, R06↔R11, etc.)
> **Estimated Effort:** Substantial (10-15 connection notes × ~2,000 words each)
> **Value Proposition:** Connection notes are the knowledge graph's cross-links. Without them, the 15 reports are 15 silos. This is the second-largest structural gap after the broken wiki-links.
> **Suggested Starting Points:**
>   1. Prosoche ↔ Metacognitive Monitoring (strongest homology)
>   2. Emotional Granularity ↔ Epistemic Precision (strongest cross-tier bridge)
>   3. Precision Flexibility ↔ All Components (PP as unifying framework)

> [!topic-idea] **[[Glossary Completion]]**
> **Gap Identified:** Glossary contains ~40 terms out of ~125 needed. Only 30% complete.
> **Where It Would Connect:** All notes (glossary is a universal entry point)
> **Estimated Effort:** Moderate-substantial (~85 additional entries)
> **Value Proposition:** The glossary is one of the most practical navigation aids. At 30%, it leaves most technical terms undefined for readers.
> **Suggested Approach:** Use taxonomy concept list from this review as the input list. Prioritize hub concepts and bridge concepts first, then fill in domain-specific terms.

---

## MEDIUM Priority — Report-Proposed Expansion Topics (Selected)

> [!important] Each of the 15 reports proposes 4-6 expansion topics in Phase VI (Appendix). The full list runs to ~70+ topics. Below are the highest-value selections based on cross-domain bridge potential, gap-filling capacity, and pedagogical significance.

### From Tier 1 (Epistemic Cognition — R01-R08)

> [!topic-idea] **[[The Ethics of Ignorance]]** (from R02)
> **Gap Identified:** Fallibilism chapter discusses what we DON'T know but not the ethics of deliberately choosing not to know, or the social consequences of willful ignorance.
> **Where It Would Connect:** R02 (fallibilism), R05 (intellectual virtue), R12 (social), R15 (integration)
> **Estimated Effort:** Moderate
> **Value Proposition:** Extends epistemic humility into unexplored ethical territory.

> [!topic-idea] **[[Cognitive Bias Inoculation Protocols]]** (from R05)
> **Gap Identified:** R05 maps biases to virtues but doesn't detail inoculation — specific training protocols that build bias resistance.
> **Where It Would Connect:** R05 (bias), R06 (attention), R07 (self-regulation), methodology note
> **Estimated Effort:** Moderate
> **Value Proposition:** Translates the bias-virtue correspondence from theoretical mapping to practical training.

> [!topic-idea] **[[Attention as Foundational Capacity]]** (from R06)
> **Gap Identified:** Attention is implicated in nearly every report but never receives standalone deep treatment. R06 covers it through the System 1/2 lens but not as an independent capacity.
> **Where It Would Connect:** R06, expansion topic "Attention and Cognitive Control" (exists), all Tier 1 reports
> **Estimated Effort:** Moderate — existing expansion topic can be base
> **Value Proposition:** Attention may be the single most important capacity for the examined life. Deserves more than derivative treatment.

### From Tier 2 (Practical Wisdom — R09-R12)

> [!topic-idea] **[[Trauma and the Examined Life]]** (from R09/R10)
> **Gap Identified:** Allostatic load and emotional dysregulation from trauma directly impair the capacities needed for examined living. This is unaddressed.
> **Where It Would Connect:** R09 (embodiment), R10 (emotion), R12 (social), "Examined Life Under Constraint"
> **Estimated Effort:** Substantial — sensitive material requiring careful treatment
> **Value Proposition:** For many people, trauma is the primary obstacle to examined living. Ignoring it makes the series incomplete.

> [!topic-idea] **[[Digital Epistemic Environments]]** (from R12)
> **Gap Identified:** Social epistemology chapter (R12) doesn't address the dominant social epistemic environment: digital/social media. How do algorithmically curated information environments affect communal rationality?
> **Where It Would Connect:** R12 (social), R05 (bias), R06 (attention), "AI and Cognitive Sovereignty"
> **Estimated Effort:** Moderate
> **Value Proposition:** Updates the series' social epistemology from ancient agora to modern information landscape.

### From Tier 3 (Integrative — R13-R15)

> [!topic-idea] **[[Predictive Processing and Meditation]]** (from R13)
> **Gap Identified:** PP framework maps cleanly onto meditation research (precision weighting modulation, prediction error attenuation) but the connection is only hinted at.
> **Where It Would Connect:** R13 (PP), R06 (attention), R09 (embodiment), "Cross-Cultural Examined Life"
> **Estimated Effort:** Moderate
> **Value Proposition:** Strongest bridge between PP framework and contemplative practice traditions. Would strengthen the cross-cultural dimension.

> [!topic-idea] **[[Narrative Repair and Identity Reconstruction]]** (from R14)
> **Gap Identified:** R14 discusses narrative identity but doesn't address narrative disruption — what happens when life events shatter the story (divorce, disability, forced migration)?
> **Where It Would Connect:** R14 (narrative), R10 (emotion), "Examined Life Under Constraint", "Trauma"
> **Estimated Effort:** Moderate
> **Value Proposition:** Extends narrative psychology from construction to reconstruction, which is where most people encounter it.

---

## LOW Priority — Exploratory Topics

> [!topic-idea] **[[The Examined Life Across the Lifespan]]**
> **Connection:** R07 (development), R14 (narrative), staging note
> **Description:** The examined life at age 20 vs. 40 vs. 60 vs. 80. How do the 15 dimensions shift in emphasis and expression across developmental stages?
> **Estimated Effort:** Substantial

> [!topic-idea] **[[Aesthetic Dimensions of the Examined Life]]**
> **Connection:** R14 (narrative), R10 (emotion), R15 (integration)
> **Description:** Beauty, art, and aesthetic experience as components of examined living. Entirely absent from the current series.
> **Estimated Effort:** Substantial

> [!topic-idea] **[[Humor, Play, and the Examined Life]]**
> **Connection:** R03 (motivation), R10 (emotion), R15 (integration)
> **Description:** The series is relentlessly serious. Humor and play have genuine epistemic functions (incongruity resolution, perspective-shifting, creative exploration).
> **Estimated Effort:** Moderate

> [!topic-idea] **[[Group Examined Life Practices]]**
> **Connection:** R12 (social), "Pedagogy of the Examined Life", methodology
> **Description:** Structured practices for examined living in groups — philosophical discussion circles, peer accountability, communal reflection rituals.
> **Estimated Effort:** Moderate

---

## Implementation Roadmap

### Phase 1: Foundation Repair (Before Anything Else)
1. Fix 02-reference-library/ wiki-links
2. Consolidate reference note directories
3. Add YAML frontmatter to 4 existing expansion topics
4. Update dashboard and navigation

### Phase 2: Knowledge Graph Construction
5. Write first 5 connection notes (highest-value cross-tier bridges)
6. Complete glossary to 60%+ (hub and bridge concepts first)

### Phase 3: Accessibility & Quality
7. Remediate 4 existing expansion topics for accessibility
8. Write Evening Self-Examination Practice Manual (highest-value practical output)

### Phase 4: New Expansion Topics
9. Cross-Cultural Examined Life (highest R15 priority)
10. AI and Cognitive Sovereignty (most timely)
11. The Examined Life Under Constraint (most ethically important)
12. Pedagogy of the Examined Life (largest impact potential)

### Phase 5: Continued Build
13. Remaining connection notes (target 10-15 total)
14. Remaining expansion topics by priority
15. Glossary to 90%+
16. Second reference note pass (remaining reports)

---

*End of Expansion Topic Registry*
*Extracted from: examined-life-codebase-pack.md (41 files)*
*Generated: 2026-03-19*
