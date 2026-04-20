---
# ═══════════════════════════════════════════════════════════════════════════
# CORE IDENTITY
# ═══════════════════════════════════════════════════════════════════════════
title: "PKM/PKB Lifelong Learning Framework: Taxonomy & Concept Registry"
aliases:
  - "PKM Framework Taxonomy"
  - "Lifelong Learning Concept Registry"
  - "PKB Design Concept Map"
type: permanent-note
status: evergreen
confidence: high

# ═══════════════════════════════════════════════════════════════════════════
# DOCUMENT IDENTIFICATION
# ═══════════════════════════════════════════════════════════════════════════
doc_id: "pkm-pkb-framework-taxonomy-v1-0"
doc_type: "taxonomy-registry"
doc_created: 2026-03-16
doc_modified: 2026-03-16
author: "claude-opus-4.6"

# ═══════════════════════════════════════════════════════════════════════════
# CLASSIFICATION & DISCOVERY
# ═══════════════════════════════════════════════════════════════════════════
primary_domain: "knowledge-management"
secondary_domains:
  - "cognitive-science"
  - "educational-psychology"
  - "taxonomy"
tags:
  - permanent-note
  - taxonomy-registry
  - concept-map
  - knowledge-management/pkm
  - cognitive-science/knowledge-architecture
  - evergreen

knowledge_level: "advanced"

# ═══════════════════════════════════════════════════════════════════════════
# PROVENANCE
# ═══════════════════════════════════════════════════════════════════════════
source-type: analytical-extraction
synthesis_technique: "PKB Codebase Review & Synthesis Agent v1.0.0"
synthesis_date: 2026-03-16
source_documents_count: 31

# ═══════════════════════════════════════════════════════════════════════════
# KNOWLEDGE GRAPH
# ═══════════════════════════════════════════════════════════════════════════
related_concepts:
  - "[[pkm-pkb-framework-synthesis]]"
  - "[[pkm-pkb-framework-working-notes]]"
  - "[[pkm-pkb-framework-expansion-topics]]"
builds_on:
  - "[[pkm-pkb-framework-working-notes]]"
---

# PKM/PKB Lifelong Learning Framework: Taxonomy & Concept Registry

> [!abstract] Purpose
> This document catalogues every significant concept extracted from the 30-report PKM/PKB Lifelong Learning Framework series plus accompanying framework overview. Concepts are organized hierarchically by domain, with precise definitions, source attributions, epistemic status ratings, and cross-connection annotations. Designed as a navigational index for both human practitioners and future AI agents.

---

## Domain Taxonomy

### 1. Cognitive Architecture & Memory Science

#### 1.1 Knowledge Representation

- **[[schema-theory]]** — Knowledge is organized in structured mental templates (schemas) that filter, organize, and reconstruct incoming information. Schemas are hierarchically nested, contextually activated, and resistant to disconfirming evidence. [Source: Report 01] [Status: <span style='color: #27FF00;'>Established</span>]
  - [[assimilation]] — Integrating new information into existing schemas without structural change [Report 03]
  - [[accommodation]] — Restructuring existing schemas to incorporate fundamentally new information [Report 03]
  - [[conceptual-change]] — Deep restructuring of domain-level schemas, requiring sustained cognitive conflict [Report 03]

- **[[Semantic-Networks]]** — Knowledge representation as interconnected nodes (concepts) and labeled edges (relationships). [[spreading-activation]] propagates access from activated nodes along associative connections. [Source: Report 01] [Status: <span style='color: #27FF00;'>Established</span>]
  - [[spreading-activation]] — Mechanism by which activating one concept makes associated concepts more accessible [Collins & Loftus 1975]
  - [[ACT-R]] — Anderson's production-system architecture implementing spreading activation in a computational cognitive model [Report 01]

- **[[Prototype-Theory]]** — Categories are organized around "best examples" (prototypes) with graded membership, not classical necessary-and-sufficient conditions. [Source: Report 15, Rosch 1975] [Status: <span style='color: #27FF00;'>Established</span>]
  - [[Basic-Level-Categories]] — Optimal categorization operates at intermediate specificity — the level maximizing within-category similarity and between-category difference [Report 15]

#### 1.2 Memory Systems

- **[[cognitive-load-theory]]** — Working memory is limited (~4 chunks); instructional design must manage intrinsic load (inherent complexity), minimize extraneous load (poor design), and optimize germane load (schema construction effort). [Source: Report 02, Sweller 1988] [Status: <span style='color: #27FF00;'>Established</span>]
  - [[Intrinsic-Load]] — Cognitive demand inherent in the material's element interactivity [Report 02]
  - [[extraneous-load]] — Cognitive demand caused by poor design, not content complexity [Report 02]
  - [[germane-load]] — Cognitive resources devoted to schema construction and automation [Report 02]

- **[[Testing-Effect]]** — Retrieving information from memory strengthens that memory more than restudying the same information. Meta-analytic effect size d = 0.50 (Rowland 2014). [Source: Report 06, 20] [Status: <span style='color: #27FF00;'>Established</span>]

- **[[spacing-effect]]** — Distributing practice over time produces substantially better retention than massing practice. Rated "high utility" alongside practice testing (Dunlosky et al. 2013). [Source: Report 06, 16] [Status: <span style='color: #27FF00;'>Established</span>]

- **[[desirable-difficulties]]** — Learning conditions that impede short-term performance but enhance long-term retention and transfer. Core instances: testing, spacing, interleaving, generation. [Source: Report 16, Bjork 1994] [Status: <span style='color: #27FF00;'>Established</span>]
  - [[generation-effect]] — Self-generating information produces stronger memory traces than reading [Report 16, 17]
  - [[interleaving]] — Alternating between problem types during practice enhances discriminative contrast and transfer [Report 16]
  - [[retrieval-practice]] — Systematic practice of pulling information from memory rather than re-exposing to it [Report 20]

- **[[fluency-illusion]]** — Metacognitive error where ease of processing is mistaken for genuine understanding. Universal PKM failure mode amplified by AI-generated content. [Source: Report 18, 30] [Status: <span style='color: #27FF00;'>Established</span>]
  - [[Epistemic Counterfeiting]] — AI-generated text triggers fluency illusion in both creator and reader, producing the appearance of knowledge without substance [Report 30] [Status: <span style='color: #FFC700;'>Emerging synthesis</span>]

#### 1.3 Expert Knowledge Organization

- **[[Expert-Knowledge-Organization]]** — Expert knowledge differs from novice knowledge qualitatively, not just quantitatively: hierarchically deeper, more cross-connected, organized around structural principles rather than surface features. [Source: Report 01, 15] [Status: <span style='color: #27FF00;'>Established</span>]
  - [[chunking]] — Experts compress complex patterns into single retrievable units through extensive practice [Report 01]
  - [[Pattern-Recognition]] — Experts perceive domain-relevant patterns invisible to novices [Report 01]

---

### 2. Learning Theory & Instructional Design

#### 2.1 Constructivist Foundations

- **[[constructivism]]** — Knowledge is actively constructed by the learner through interaction with the environment, not passively received or transmitted. [Source: Report 03] [Status: <span style='color: #27FF00;'>Established</span>]
  - [[cognitive-constructivism]] — Individual construction through schema development (Piaget) [Report 03]
  - [[social-constructivism]] — Knowledge co-constructed through social interaction (Vygotsky) [Report 03]
  - [[zone-of-proximal-development]] — The gap between independent capability and guided capability; learning optimally targets this zone [Vygotsky, Report 10]

- **[[Scaffolding and Fading]]** — Providing structured support that is systematically withdrawn as competence develops. [Source: Report 10] [Status: <span style='color: #27FF00;'>Established</span>]
  - [[expertise-reversal-effect]] — Instructional support beneficial for novices becomes counterproductive for experts [Report 10]

#### 2.2 Self-Regulation & Metacognition

- **[[self-regulated-learning]]** — Three-phase cyclical process: forethought → performance → self-reflection, operating across cognitive, metacognitive, motivational, and behavioral dimensions. [Source: Report 04, Zimmerman 2002] [Status: <span style='color: #27FF00;'>Established</span>]
  - [[metacognitive-monitoring]] — Ongoing assessment of one's own comprehension, learning progress, and cognitive processes [Report 12]
  - [[calibration]] — Alignment between confidence in one's knowledge and actual knowledge accuracy [Report 18]
  - [[dunning-kruger-effect]] — Systematic miscalibration where low competence produces overconfidence and high competence produces underconfidence [Report 18]

- **[[reflective-practice]]** — Deliberate examination of experience to extract learning and guide future action. [Source: Report 08, 12]
  - [[Dewey's-Reflective-Inquiry]] — Problem-initiated, systematic investigation moving from felt difficulty through hypothesis to tested conclusion [Report 08]
  - [[Kolb's Learning Cycle]] — Concrete Experience → Reflective Observation → Abstract Conceptualization → Active Experimentation [Report 08]

#### 2.3 Motivation & Self-Determination

- **[[self-determination-theory]]** — Intrinsic motivation requires satisfaction of three basic psychological needs: autonomy, competence, and relatedness. [Source: Report 05, Deci & Ryan] [Status: <span style='color: #27FF00;'>Established</span>]
  - [[autonomy]] — Need for volitional control over one's actions and choices [Report 05, 24]
  - [[competence]] — Need for efficacy and mastery [Report 05]
  - [[relatedness]] — Need for social connection and belonging [Report 05]

- **[[heutagogy]]** — Self-determined learning where the learner controls not just pace and sequence but also curriculum and methodology. The highest point on the [[Pedagogy-Andragogy-Heutagogy Continuum]]. [Source: Report 24, Hase & Kenyon] [Status: <span style='color: #FFC700;'>Emerging</span>]

- **[[Interest-Development-Theory]]** — Interest progresses through four phases: triggered situational → maintained situational → emerging individual → well-developed individual. [Source: Report 19] [Status: <span style='color: #27FF00;'>Established</span>]

---

### 3. Knowledge Management & Information Science

#### 3.1 Classification & Organization

- **[[Faceted-Classification]]** — Multi-dimensional classification where each item is described along multiple independent facets (e.g., domain, process type, abstraction level) rather than a single hierarchy. Named after [[Ranganathan]]'s colon classification system. [Source: Report 15] [Status: <span style='color: #27FF00;'>Established</span>]
  - [[Vocabulary-Mismatch-Problem]] — <20% naming agreement across individuals for the same concepts (Furnas et al.), making single-label systems unreliable [Report 15]
  - [[Folksonomy]] — Bottom-up emergent classification from individual tagging behavior; complements faceted classification for discovery [Report 15]

- **[[Information Foraging Theory]]** — Users navigate information environments like animals forage for food, following "information scent" along paths of highest expected value. [Source: Report 01, 15] [Status: <span style='color: #27FF00;'>Established</span>]

#### 3.2 Knowledge Creation & Conversion

- **[[SECI-Model]]** — Four modes of knowledge conversion: Socialization (tacit→tacit), Externalization (tacit→explicit), Combination (explicit→explicit), Internalization (explicit→tacit). [Source: Report 22, Nonaka & Takeuchi 1995] [Status: <span style='color: #27FF00;'>Established</span>]
  - [[tacit-knowledge]] — Knowledge that cannot be fully articulated — "we know more than we can tell" (Polanyi) [Report 22]
  - [[Explicit-Knowledge]] — Knowledge that can be codified, stored, and transferred through language and symbols [Report 22]

#### 3.3 Network Topology & Integration

- **[[Small-World-Networks]]** — Network topology combining high local clustering with short global path lengths. [Source: Report 25, Watts & Strogatz 1998] [Status: <span style='color: #27FF00;'>Established</span>]
  - [[Hub-Notes]] — Highly connected notes that serve as navigational anchors [Report 25]
  - [[Bridge Notes]] — Notes connecting otherwise isolated knowledge clusters [Report 25]
  - [[Archipelago Topology]] — Pathological PKB state where knowledge clusters form disconnected islands [Report 25]

- **[[Accumulation Problem]]** — The diagnosis that most mature PKBs fail because notes accumulate without structurally integrating. A design problem, not a discipline problem. [Source: Report 25, 27] [Status: <span style='color: #FFC700;'>Original synthesis</span>]

---

### 4. Framework-Original Concepts (Report 27 Capstone)

#### 4.1 Meta-Framework Architecture

- **[[Integrated-Learning-System-Model]]** — A PKB at full function has three synergistic properties: (1) [[Isomorphic External Memory]], (2) [[Constructive Processing Engine]], (3) [[Self-Regulating Adaptive System]]. Properties are synergistic — any one without the others is qualitatively deficient. [Source: Report 27] [Status: <span style='color: #FFC700;'>Original synthesis</span>]

- **[[Five-Convergence-Zones]]** — Points of highest-confidence cross-disciplinary agreement: [Source: Report 27] [Status: <span style='color: #FFC700;'>Original synthesis</span>]
  1. [[Organizational Isomorphism Imperative]] — PKB must mirror cognitive architecture
  2. [[Active-Construction-Imperative]] — Knowledge requires effortful processing
  3. [[Regulatory Loop Imperative]] — All learning requires feedback cycles
  4. [[Motivational Sustainability Imperative]] — PKM must sustain decades-long engagement
  5. [[Integration Imperative]] — Accumulation without integration equals failure

- **[[Twelve-Master-Principles]]** — Three-tier unified design framework: [Source: Report 27] [Status: <span style='color: #FFC700;'>Original synthesis</span>]
  - *Foundational (FP):*
    - [[FP1: Cognitive Isomorphism]] — PKB mirrors memory architecture
    - [[FP2: Active Construction]] — All processing is effortful and generative
    - [[FP3: Regulatory Embedding]] — Monitoring and feedback are structural features
    - [[FP4: Motivational Alignment]] — Design satisfies SDT needs (autonomy, competence, relatedness)
  - *Derived (DP):*
    - [[DP1: Note Architecture]] — Individual notes as cognitive units
    - [[DP2: Linking Philosophy]] — Wiki-links as spreading activation architecture
    - [[DP3: Review Architecture]] — Spaced, retrieval-based review system
    - [[DP4: Active Processing Workflows]] — Templates that require elaboration
    - [[DP5: Calibration Systems]] — Embedded confidence tracking and accuracy comparison
  - *Refinement (RP):*
    - [[RP1: Evolutionary Architecture]] — System fades scaffolding with growing expertise
    - [[RP2: Dialectical Deepening]] — Structured engagement with competing perspectives
    - [[RP3: Integration Metabolism]] — Regular synthesis practices (weekly/monthly/annual cadence)

#### 4.2 AI-Era Extensions

- **[[Cognitive Partnership Model]]** — AI in PKM should function as [[Socratic Interlocutor]], not oracle or scribe. Designed to generate productive uncertainty, surface tensions, and challenge positions. [Source: Report 30] [Status: <span style='color: #FFC700;'>Emerging synthesis</span>]

- **[[Offloading Quality Distinction]]** — Decision heuristic: storage/retrieval offloading to AI is beneficial; synthesis/reasoning offloading to AI is harmful. [Source: Report 30] [Status: <span style='color: #FFC700;'>Emerging synthesis</span>]

- **[[Convenience-Learning Tension]]** — The central paradox that AI features making PKBs most convenient for retrieval are precisely those preventing them from functioning as learning systems. [Source: Report 30] [Status: <span style='color: #FFC700;'>Emerging synthesis</span>]

---

### 5. Philosophical Foundations

#### 5.1 Epistemology

- **[[extended-mind-theory]]** — Cognitive processes extend beyond the brain when external structures (like a PKB) meet coupling conditions: reliability, accessibility, automatic endorsement, prior endorsement. [Source: Report 28, Clark & Chalmers 1998] [Status: <span style='color: #27FF00;'>Established (philosophical)</span>]

- **[[virtue-epistemology]]** — Knowledge production as exercise of intellectual virtues: curiosity, humility, thoroughness, fairness, courage. [Source: Report 28, 29] [Status: <span style='color: #27FF00;'>Established (philosophical)</span>]

- **[[epistemic-humility]]** — Calibrated awareness of the limits and reliability of one's knowledge. Operationalized through [[DP5: Calibration Systems]]. [Source: Report 18, 28] [Status: <span style='color: #27FF00;'>Established</span>]

#### 5.2 Educational Philosophy

- **[[socratic-method]]** — Knowledge emerges through structured questioning that surfaces contradictions and builds understanding through dialogue. [[aporia]] (productive confusion) precedes insight. [Source: Report 14, 21] [Status: <span style='color: #27FF00;'>Established</span>]

- **[[Pragmatist-Epistemology]]** — Knowledge is warranted assertion tested through consequences in practice, not correspondence to abstract truth. [Source: Report 28, Dewey/James/Peirce] [Status: <span style='color: #27FF00;'>Established (philosophical)</span>]

- **[[Stoic Discipline]]** — Emotional regulation through distinguishing what is within one's control (response, effort, attention) from what is not (outcomes, others' behavior). Applied to learning resilience in Reports 13, 19. [Source: Report 13] [Status: <span style='color: #27FF00;'>Established (philosophical)</span>]

---

## Concept Relationship Matrix (Top 25 Connections)

| Concept A | Relationship | Concept B | Strength | Source |
|-----------|-------------|-----------|----------|--------|
| [[schema-theory]] | *provides architecture for* | [[Cognitive Architecture Isomorphism]] | Strong | R01→R09 |
| [[desirable-difficulties]] | *provides mechanism for* | [[Active-Construction-Imperative]] | Strong | R16→R27 |
| [[self-regulated-learning]] | *operationalized as* | [[Regulatory Embedding]] | Strong | R04→R27 |
| [[Testing-Effect]] | *implements* | [[retrieval-practice]] | Strong | R06→R20 |
| [[fluency-illusion]] | *amplified by* | [[Epistemic Counterfeiting]] | Strong | R18→R30 |
| [[fluency-illusion]] | *countered by* | [[calibration]] | Strong | R18 |
| [[Small-World-Networks]] | *diagnoses* | [[Accumulation Problem]] | Strong | R25 |
| [[Faceted-Classification]] | *converges with* | [[Basic-Level-Categories]] | Moderate | R15 |
| [[heutagogy]] | *extends* | [[self-determination-theory]] | Moderate | R24→R05 |
| [[Scaffolding and Fading]] | *resolves* | Structure vs. Autonomy Tension | Moderate | R10 |
| [[Cognitive Partnership Model]] | *operationalizes* | [[Offloading Quality Distinction]] | Moderate | R30 |
| [[SECI-Model]] | *maps onto* | Capture-Process-Integrate pipeline | Moderate | R22→R09 |
| [[constructivism]] | *requires* | [[desirable-difficulties]] | Moderate | R03→R16 |
| [[Kolb's Learning Cycle]] | *parallels* | [[Zimmerman's SRL Cycle]] | Moderate | R08, R04 |
| [[integration-metabolism]] | *addresses* | [[Accumulation Problem]] | Strong | R27→R25 |
| [[spreading-activation]] | *maps to* | Wiki-link navigation patterns | Strong | R01→R09 |
| [[Stoic Discipline]] | *supports persistence through* | [[desirable-difficulties]] | Suggestive | R13→R16 |
| [[extended-mind-theory]] | *grounds* | PKB as cognitive extension | Moderate | R28 |
| [[Interest-Development-Theory]] | *resolves* | Motivational sustainability | Moderate | R19 |
| [[expertise-reversal-effect]] | *motivates* | [[RP1: Evolutionary Architecture]] | Strong | R10→R27 |

---

## Hub Concepts (Most Connected — ≥5 connections)

1. **[[desirable-difficulties]]** — Connects to: Testing Effect, Spacing Effect, Generation Effect, Interleaving, Fluency Illusion, Active Construction, Constructivism, Cognitive Partnership Model, Stoic Discipline, Note-Making
2. **[[fluency-illusion]]** — Connects to: Calibration, Dunning-Kruger, Epistemic Counterfeiting, Desirable Difficulties, Metacognitive Monitoring, Retrieval Practice, AI Integration
3. **[[self-regulated-learning]]** — Connects to: Metacognitive Monitoring, Calibration, Regulatory Embedding, Feedback Loops, Reflective Practice, Zimmerman's SRL Cycle
4. **[[Cognitive Architecture Isomorphism]]** — Connects to: Schema Theory, Semantic Networks, CLT, Expert Knowledge Organization, Information Foraging, SECI Model, Note Architecture, Linking Philosophy
5. **[[constructivism]]** — Connects to: Accommodation, Conceptual Change, ZPD, Active Construction, Desirable Difficulties, Note-Making, Elaborative Interrogation
6. **[[Integrated-Learning-System-Model]]** — Connects to: All Five Convergence Zones, all Twelve Master Principles, Isomorphic External Memory, Constructive Processing Engine, Self-Regulating Adaptive System

## Bridge Concepts (Cross-Domain Connectors)

1. **[[Cognitive Partnership Model]]** — Bridges: AI/Technology ↔ Learning Science ↔ Socratic Philosophy
2. **[[SECI-Model]]** — Bridges: Knowledge Management ↔ Cognitive Science ↔ PKB Design
3. **[[Stoic Discipline]]** — Bridges: Philosophy ↔ Emotional Regulation ↔ Learning Resilience
4. **[[extended-mind-theory]]** — Bridges: Philosophy of Mind ↔ PKB Design ↔ AI Integration
5. **[[Basic-Level-Categories]]** — Bridges: Cognitive Psychology (Rosch) ↔ Library Science (Ranganathan)

## Orphan Concepts (Weakly Connected — Needs Integration)

1. **[[Dialectics]]** (Report 21) — Rich philosophical tradition but weakly connected to practical PKB design
2. **[[Ethical PKM]]** (Report 29) — Important but architecturally disconnected from the Twelve Master Principles
3. **[[Learning Environments Design]]** (Report 23) — Overlaps substantially with Reports 09 and 10 without clear differentiated contribution
4. **[[relatedness]]** (SDT need) — Acknowledged but systematically unaddressed due to solo-practice focus

---

> [!connections-and-links] Related Documents
> - **Synthesis:** [[pkm-pkb-framework-synthesis]] — Comprehensive analytical review
> - **Working Notes:** [[pkm-pkb-framework-working-notes]] — Progressive analytical notes
> - **Expansion Topics:** [[pkm-pkb-framework-expansion-topics]] — Prioritized development registry
