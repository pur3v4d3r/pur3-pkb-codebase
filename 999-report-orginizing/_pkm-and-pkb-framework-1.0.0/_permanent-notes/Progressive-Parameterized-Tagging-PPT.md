---
# ═══════════════════════════════════════════════════════════════════════════
# CORE IDENTITY
# ═══════════════════════════════════════════════════════════════════════════
title: "Progressive Parameterized Tagging (PPT)"
aliases:
  - "Progressive Parameterized Tagging (PPT)"
  - "PPT"
type: permanent-note
status: evergreen
confidence: high

# ═══════════════════════════════════════════════════════════════════════════
# CLASSIFICATION
# ═══════════════════════════════════════════════════════════════════════════
tags:
  - permanent-note
  - evergreen
  - learning-science
  - pkm/organization
  - pkb/architecture
  - pkb/tagging
  - pkb/taxonomy
  - information-science/classification

domain: learning-science
subdomains:
  - information-science
  - cognitive-psychology
  - library-science
  - cognitive-science
  - educational-psychology

# ═══════════════════════════════════════════════════════════════════════════
# TEMPORAL
# ═══════════════════════════════════════════════════════════════════════════
created: 2026-03-18
updated: 2026-03-18

# ═══════════════════════════════════════════════════════════════════════════
# SOURCE TRACKING
# ═══════════════════════════════════════════════════════════════════════════
source-type: report-extraction
source-reports:
  - "15-knowledge-organization-at-scale-pkm-framework-2026-03-14"
evidence-quality: high
extraction-method: "pkb-extractor-v1 → permanent-notes-generator-v1"

# ═══════════════════════════════════════════════════════════════════════════
# CONTENT CHARACTERISTICS
# ═══════════════════════════════════════════════════════════════════════════
complexity-level: advanced-practitioner
depth-level: comprehensive

# ═══════════════════════════════════════════════════════════════════════════
# RELATIONSHIPS
# ═══════════════════════════════════════════════════════════════════════════
prerequisites:
  - "[[]]"

related:
  - "[[Taxonomy]]"
  - "[[Ontology (Knowledge)]]"
  - "[[Folksonomy]]"
  - "[[Faceted Classification]]"
  - "[[Controlled Vocabulary]]"
  - "[[Prototype Theory]]"
  - "[[Basic-Level Categories]]"
  - "[[SECI Model]]"
  - "[[Knowledge Externalization]]"
  - "[[Semantic Networks]]"

broader:
  - "[[]]"

narrower:
  - "[[]]"

see-also:
  - "[[2024]]"
  - "[[Boundary Objects and Knowledge Organization Across Contexts — When Your PKB Must Serve Multiple Roles]]"
  - "[[Cognitive Load Theory]]"
  - "[[Online Learning]]"
  - "[[Reflective Practice]]"
  - "[[Report 01: Foundations of Knowledge Architecture]]"
  - "[[Report 06: The Science of Remembering]]"
  - "[[Report 08: Reflective Practice and Experiential Learning]]"

# ═══════════════════════════════════════════════════════════════════════════
# LEARNING PATHWAYS
# ═══════════════════════════════════════════════════════════════════════════
builds-on:
  - "[[Report 01: Foundations of Knowledge Architecture]]"
  - "[[Report 03: Constructing Understanding — How Knowledge Builds on Knowledge in a PKB]]"
  - "[[Report 09: Designing the Learning PKB — Information Architecture Meets Cognitive Architecture]]"
  - "[[Report 10: Scaffolding and Fading — How PKB Structure Should Evolve with Expertise]]"

enables:
  - "[[Report 20: Retrieval-Enhanced Knowledge Networks]]"
  - "[[Report 22: Tacit Knowledge and the Limits of Capture]]"
  - "[[Report 25: The Integration Problem — How Separate Notes Become Connected Understanding]]"
  - "[[Report 27: The Complete PKM/PKB Design Framework]]"

expansion-topics:
  - topic: "[[]]"
    description: ""
    priority: medium

# ═══════════════════════════════════════════════════════════════════════════
# PERSONAL KNOWLEDGE MANAGEMENT
# ═══════════════════════════════════════════════════════════════════════════
review-frequency: quarterly
mastery-stage: seedling
importance: high
---

# Progressive Parameterized Tagging (PPT)

> [!definition] **Progressive Parameterized Tagging (PPT)**
> A PKB tag system that combines a small set of mandatory facet parameters with emergent content tags, organized to evolve through explicit "schema crystallization events" as the user's knowledge matures.
> 
> **Structure**: Every note is required to specify values for 3-5 mandatory facets (forming the "parameterized" backbone), plus any number of emergent content tags (forming the "folksonomy" layer). The mandatory facets are chosen for permanence — they should be stable even as domain knowledge evolves. The emergent content tags are expected to drift, be consolidated, and be reorganized at regular intervals.
> 
> **Mandatory Facets (the Parameterized Layer)**: Following Ranganathan's insight, these should be orthogonal dimensions that describe notes along stable axes. For a knowledge PKB, appropriate mandatory facets typically include: **Type** (what kind of note this is: concept, evidence, argument, question, synthesis, reference), **Domain** (the primary knowledge area: should be at basic-level category grain), **Status** (epistemic state: seedling, developing, mature, evergreen), **Relation** (primary relationship to existing knowledge: extends, challenges, exemplifies, synthesizes, questions). These four facets provide reliable, multi-path retrieval without requiring domain-specific knowledge to assign.
> 
> **Emergent Content Tags (the Folksonomy Layer)**: These are free-form, context-specific tags that reflect your current conceptual vocabulary for the note's content. They are expected to be inconsistent across time and to require periodic consolidation. They should not be used as the primary retrieval mechanism — that is the parameterized layer's job. Their function is discovery: browsing notes tagged with an emergent content tag often surfaces unexpected connections that the parameterized facets alone would not reveal.
> 
> **Schema Crystallization Events**: Scheduled intervals (quarterly for active knowledge areas, annually for stable ones) in which you review the emergent content tag layer for vocabulary drift, synonymy, and granularity inconsistency, consolidating where needed and splitting where a single tag has come to cover genuinely distinct concepts. This is the solo substitute for the social correction mechanism that folksonomies otherwise lack.

*Source: Novel synthesis — this report series*

## Core Explanation

> [!evidence] Supporting Evidence
> **The Effectiveness of Faceted Classification**: The most compelling evidence for a specific formal approach comes from faceted classification studies. Experimental comparisons by Ranganathan's successors (particularly Vickery, 1960; Spiteri, 1998) consistently find that faceted systems outperform strict hierarchical taxonomies on two critical metrics: (1) retrieval flexibility — users can reach the same item via multiple facet combinations — and (2) scalability — faceted systems degrade…

> [!evidence] Supporting Evidence
> **Formal Systems Work Better for Retrieval, Worse for Discovery**: A consistent but underappreciated pattern across information retrieval research is that formal classification systems optimize different things than users actually want at different stages of their knowledge work. Formal systems excel at precision retrieval: when you know roughly what you're looking for and need to find it. They are systematically worse at serendipitous discovery: finding things you didn't know you needed.…

> [!evidence] Supporting Evidence
> **Tags Are Theories, Not Labels**: Murphy and Medin's finding on category coherence, applied to PKB tagging, suggests that every tag is implicitly a theoretical claim about the structure of your knowledge domain. A tag like `cognitive-science` is not merely a label — it implicitly claims that there is a coherent domain of inquiry called "cognitive science" with enough internal unity that grouping notes under it enables useful inferences. A tag like `interesting` makes no such theoretical claim…

> [!analytical-insight] Key Insight
> **The Central Claim: Organization Emerges from Externalization**: The SECI model contains a claim that directly challenges the assumption underlying most PKB organizational advice: *you cannot design the right organizational structure before you have externalized enough knowledge to know what categories you need.* Nonaka's insight is that meaningful categories are not imposed before knowing — they crystallize through the process of knowing. Tags and folders that are created before engaging…

> [!analytical-insight] Key Insight
> **The Vocabulary Mismatch Problem (Information Science, Furnas et al., 1987)**: A robust empirical finding from information retrieval research: when people independently name the same object, they agree on the same word less than 20% of the time. Furnas and colleagues demonstrated this across multiple domains and found the consistency rate rarely exceeded 10-20% for spontaneous naming. This "vocabulary mismatch problem" has profound implications for PKB self-organization: the tag you used to…

## Practical Implications

> [!example] **Application**
> **The 7 ± 2 Tag Rule for Domain Categories**: Working memory research (Miller, 1956) establishes that 7 ± 2 items can be held in working memory simultaneously. Applied to PKB domain tags, this suggests that if any single domain contains more than 9 top-level sub-domain tags, the browsing experience exceeds working memory capacity and the tags lose their navigational utility. When you find yourself with more than 9 tags in any single domain, this is a signal either to reorganize into a faceted…

> [!warning] **Key Distinction**
> The most common organizational error in PKB practice is spending significant time designing a comprehensive organizational system before accumulating enough knowledge to know what categories you actually need. This is the premature optimization trap: you are designing categories for a domain you don't yet understand well enough to categorize correctly. Nonaka's externalization principle and the expert-novice categorization research both predict that early organizational designs will be wrong in…

## Connections & Context

**Related concepts:**
[[2024]] · [[Boundary Objects and Knowledge Organization Across Contexts — When Your PKB Must Serve Multiple Roles]] · [[Cognitive Load Theory]] · [[Faceted Classification]] · [[Online Learning]] · [[Prototype Theory]] · [[Reflective Practice]] · [[Report 01: Foundations of Knowledge Architecture]] · [[Report 06: The Science of Remembering]] · [[Report 08: Reflective Practice and Experiential Learning]] · [[Report 09: Designing the Learning PKB]] · [[Report 10: Scaffolding and Fading]] · [[Report 20: Retrieval-Enhanced Knowledge Networks]] · [[Report 25: The Integration Problem]] · [[SECI Model]]
