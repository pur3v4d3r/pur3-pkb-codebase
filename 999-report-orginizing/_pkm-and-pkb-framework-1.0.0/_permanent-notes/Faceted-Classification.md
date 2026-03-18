---
# ═══════════════════════════════════════════════════════════════════════════
# CORE IDENTITY
# ═══════════════════════════════════════════════════════════════════════════
title: "Faceted Classification"
aliases:
  - "Faceted Classification"
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
  - pkm/design
  - pkb/architecture
  - information-architecture
  - cognitive-architecture
  - knowledge-management/structural-design

domain: learning-science
subdomains:
  - cognitive-science
  - information-science
  - instructional-design
  - learning-experience-design
  - cognitive-psychology

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
  - "09-designing-the-learning-pkb-pkm-framework-2026-03-14"
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
  - "[[Cognitive Architecture Isomorphism Principle]]"
  - "[[Schema Theory]]"
  - "[[Cognitive Load Theory]]"
  - "[[Working Memory]]"
  - "[[Information Architecture]]"
  - "[[Self-Regulated Learning]]"
  - "[[Spreading Activation]]"
  - "[[Semantic Networks]]"
  - "[[Progressive Disclosure]]"
  - "[[Maps of Content]]"

broader:
  - "[[]]"

narrower:
  - "[[]]"

see-also:
  - "[[2024]]"
  - "[[Accommodation]]"
  - "[[Boundary Objects and Knowledge Organization Across Contexts — When Your PKB Must Serve Multiple Roles]]"
  - "[[Cognitive Alignment Principle]]"
  - "[[Cognitive Psychology]]"
  - "[[Confirmation Bias]]"
  - "[[Constructivism]]"
  - "[[Desirable Difficulties]]"

# ═══════════════════════════════════════════════════════════════════════════
# LEARNING PATHWAYS
# ═══════════════════════════════════════════════════════════════════════════
builds-on:
  - "[[Report 01: Foundations of Knowledge Architecture]]"
  - "[[Report 02: The Architecture of Learning — Cognitive Load, Working Memory, and PKB Design]]"
  - "[[Report 04: Metacognitive Self-Regulation — The Engine of Effective PKM]]"
  - "[[Report 06: The Science of Remembering — Memory Systems, Retrieval Practice, and PKB Review Design]]"

enables:
  - "[[Report 10: Scaffolding and Fading — How PKB Structure Should Evolve with Expertise]]"
  - "[[Report 12: The Reflective PKB — Embedding Metacognitive Monitoring into Daily Practice]]"
  - "[[Report 15: Knowledge Organization at Scale — Taxonomies, Ontologies, and Emergent Structure]]"
  - "[[Report 27: The Complete PKM/PKB Design Framework]]"

expansion-topics:
  - topic: "[[Report 10: Scaffolding and Fading — How PKB Structure Should Evolve with Expertise]]"
    description: "The [[Cognitive Architecture Isomorphism Principle]] specifies the structural properties of an effec"
    priority: medium
  - topic: "[[Note Titling as Cognitive Interface Design]]"
    description: "This report identified note titling as the primary source of information scent in a PKB's navigation"
    priority: medium
  - topic: "[[The Zettelkasten as Cognitive Architecture Implementation]]"
    description: "Niklas Luhmann's Zettelkasten developed — entirely through practice and without theoretical foundati"
    priority: medium
  - topic: "[[Metadata Architecture for a Learning PKB — YAML Frontmatter Design Principles]]"
    description: "The design principles in this report apply to folders, tags, and links — the three primary structura"
    priority: medium

# ═══════════════════════════════════════════════════════════════════════════
# PERSONAL KNOWLEDGE MANAGEMENT
# ═══════════════════════════════════════════════════════════════════════════
review-frequency: quarterly
mastery-stage: seedling
importance: high
---

# Faceted Classification

> [!definition] **Faceted Classification**
> A system of knowledge organization that classifies items using multiple independent dimensions (facets) rather than a single hierarchical scheme. A book, for instance, might be classified simultaneously along dimensions of topic, time period, geographic region, and audience — and any combination of these facets generates a valid organizational view. Faceted classification is particularly relevant to PKB design because most notes are inherently multi-dimensional: a note about the cognitive neuroscience of memory might belong simultaneously to the "cognitive psychology," "neuroscience," "learning science," and "PKM design" facets. A purely hierarchical folder system forces the note into one category; a faceted system — implemented through tags — allows it to live appropriately in all relevant categories simultaneously.

*Source: Ranganathan, 1933; Vickery, 1960 (defined across 3 reports)*

## Core Explanation

> [!evidence] Supporting Evidence
> **Expert Knowledge Organization is Hierarchical-Associative, Not Purely Hierarchical**: Research by Chase & Simon (1973) on chess expertise, Chi et al. (1981) on physics, and Bedard & Chi (1992) on medical diagnosis converges on a structural description of expert knowledge: it is organized in large, richly interconnected chunks at multiple levels of abstraction, with strong associative connections both within and between levels. Expert knowledge is not stored in a flat list, nor in a simple…

> [!evidence] Supporting Evidence
> **Organization as Retrieval Engineering**: The combined evidence from encoding specificity research (Tulving & Thomson, 1973), context-dependent memory studies (Smith & Vela, 2001), and retrieval practice research (Roediger & Karpicke, 2006) suggests something that popular PKM discourse rarely states explicitly: organizing a note is not an administrative act; it is a retrieval engineering act. Every structural decision — how a note is titled, what tags it carries, what other notes it links to,…

> [!evidence] Supporting Evidence
> **Folder Depth Imposes Real Cognitive Costs**: Card, Moran, and Newell's foundational work on human-computer interaction (1983), combined with more recent studies on information foraging (Pirolli & Card, 1999) and navigation in file systems (Bergman et al., 2010), documents that hierarchical navigation is cognitively expensive. Users lose context, make navigation errors, and experience working memory overload at folder depths beyond three to four levels. The optimal depth for working memory…

> [!analytical-insight] Key Insight
> **The Multi-Dimensional Nature of PKB Knowledge**: Every significant piece of knowledge in a PKB exists simultaneously in multiple conceptual neighborhoods. A note about the testing effect belongs to cognitive psychology, to study science, to PKM design, and to instructional design. Any PKB architecture that forces such notes into a single neighborhood — a single folder, a single hierarchical location — distorts their nature and degrades their retrievability. The evidence from information…

> [!analytical-insight] Key Insight
> **The Expertise Evidence Specifies the Target Architecture**: Most PKM advice treats the desired structure of a mature PKB as an open design question — one of many valid organizational choices. But the expertise research closes that question considerably. If the goal is a PKB that supports the development of expert knowledge organization, and if expert knowledge is consistently organized in hierarchical-associative three-level structures across domains, then the target architecture for a mature…

## Practical Implications

> [!example] **Application**
> *Describe how this concept applies in practice.*

> [!warning] **Key Distinction**
> - **"More organization is better organization"**: The evidence shows that excessive organizational complexity imposes cognitive costs that outweigh retrieval benefits. Optimal organization is the *minimum* structure needed to support retrieval and learning — not the maximum.
> - **"Tags and folders serve the same function"**: They do not. Folders impose exclusive hierarchy (one location); tags implement faceted classification (multiple simultaneous contexts). Treating tags as a refinement of…

## Connections & Context

**Related concepts:**
[[2024]] · [[Accommodation]] · [[Boundary Objects and Knowledge Organization Across Contexts — When Your PKB Must Serve Multiple Roles]] · [[Cognitive Alignment Principle]] · [[Cognitive Architecture Isomorphism Principle]] · [[Cognitive Load Theory]] · [[Cognitive Psychology]] · [[Confirmation Bias]] · [[Constructivism]] · [[Desirable Difficulties]] · [[Educational Philosophy]] · [[Elaboration Theory]] · [[Embodied and Situated Cognition — What Text-Based PKBs Cannot Capture]] · [[Encoding Specificity]] · [[Expert Knowledge Organization]]
