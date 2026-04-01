---
title: "PKM/PKB Framework 1.0.0: Taxonomy & Concept Registry"
doc_id: "pkm-pkb-framework-taxonomy-v1-0"
doc_type: "taxonomy"
doc_created: 2026-03-16
doc_modified: 2026-03-16
author: "claude-sonnet-4-6 (via PKB Review Agent)"
primary_domain: "knowledge-management"
status: evergreen
confidence: high
source_synthesis: "[[pkm-pkb-framework-synthesis]]"
---

# PKM/PKB Framework 1.0.0: Taxonomy & Concept Registry

*Extracted from comprehensive six-pass analytical review of 31-document codebase*

---

## Domain Taxonomy

### 1. Cognitive Architecture & Memory Science

#### 1.1 Schema Theory
- **[[Schema-Theory]]** — Mental framework structuring knowledge; determines encoding and retrieval [Reports 01, 02, 03]
  - [[Schema Assimilation]] — Incorporating new information into existing schema without restructuring
  - [[Schema-Accommodation]] — Restructuring existing schema to incorporate incompatible new information
  - [[Schema Activation]] — Triggering of relevant schemas during knowledge encoding
  - [[Expert Schema Organization]] — Deep structural principle organization vs. novice surface-feature organization [Report 01]

#### 1.2 Memory Systems & Retrieval
- **[[Semantic-Memory]]** — Long-term declarative memory for concepts and their relationships [Report 01]
  - [[Spreading-Activation]] — Retrieval mechanism via network activation propagation (Collins & Loftus) [Report 01]
  - [[Associative Network]] — The underlying architecture of semantic memory
- **[[Forgetting-Curve]]** — Exponential decay of memory trace over time (Ebbinghaus) [Report 06]
- **[[Encoding-Specificity-Principle]]** — Retrieval maximized when retrieval cues match encoding cues (Tulving) [Reports 06, 11]
- **[[Memory-Consolidation]]** — Process by which memories become stable; sleep-dependent component [Report 06]
- **[[Testing-Effect]]** / **[[Retrieval-Practice-Effect]]** — Active retrieval produces dramatically better retention than passive re-study (Roediger & Karpicke) [Reports 06, 16, 20]
- **[[Generation-Effect]]** — Self-generated content is better remembered than externally provided content [Reports 17, 16]
- **[[Fluency-Illusion]]** — Overestimation of learning produced by re-reading familiar material (Bjork) [Reports 06, 12, 18]
- **[[Retrieval-Induced-Forgetting]]** — Retrieving some items from memory can impair retrieval of related items [Report 06]

#### 1.3 Working Memory & Cognitive Load
- **[[Working-Memory]]** — Limited-capacity conscious processing system (~4 novel elements) (Baddeley) [Report 02]
- **[[Cognitive-Load-Theory]]** (CLT) — Framework for managing working memory load in learning (Sweller) [Reports 02, 10]
  - [[Intrinsic-Load]] — Load inherent to the complexity of the material
  - [[Extraneous-Load]] — Load caused by poor design; reduces learning
  - [[Germane-Load]] — Load that contributes to schema formation; productive
  - [[Expertise-Reversal-Effect]] — Scaffolding that helps novices becomes load-inducing for experts [Reports 02, 10]

---

### 2. Learning Science & Instructional Design

#### 2.1 Memory Optimization
- **[[Spacing-Effect]]** — Distributed practice outperforms massed practice (Cepeda et al.) [Reports 06, 16, 20]
- **[[interleaving]]** — Mixing topics within practice sessions; improves retention and transfer (Bjork) [Reports 06, 16]
- **[[Desirable-Difficulties]]** — Conditions that impair short-term performance while enhancing long-term retention (Bjork & Bjork) [Reports 06, 16, 30]
- **[[Spaced-Repetition-Systems]]** (SRS) — Algorithmic scheduling of review based on forgetting curve (Leitner, Wozniak) [Report 06]
- **[[Transfer-Appropriate-Processing]]** — Memory is best when retrieval conditions match encoding conditions [Report 06]

#### 2.2 Constructivism & Knowledge Construction
- **[[Constructivism]]** — Learners construct knowledge rather than receive it (Piaget, Vygotsky) [Reports 01, 03, 17]
- **[[Elaboration-Theory]]** — Learning is enhanced by connecting new information to existing knowledge in elaborate ways (Reigeluth) [Reports 03, 17]
- **[[Elaborative-Interrogation]]** — Generating answers to "why?" and "how?" questions enhances encoding [Reports 17, 16]
- **[[Self-Explanation-Effect]]** — Explaining material to oneself during learning improves retention [Report 17]
- **[[Note-Making-vs.-Note-Taking]]** — Note-making (generative, constructive) vs. note-taking (passive recording) [Report 17]

#### 2.3 Transfer of Learning
- **[[Transfer-of-Learning]]** — Application of learned knowledge or skills to new contexts [Report 11]
  - [[Near-Transfer]] — Transfer to highly similar contexts
  - [[Far-Transfer]] — Transfer to substantially different contexts
  - [[Inert-Knowledge]] — Accurately stored but non-deployable knowledge (Whitehead) [Reports 11, 25]
- **[[Situated-Cognition]]** — Knowledge is tied to the context of its acquisition (Brown, Collins & Duguid) [Report 11]
- **[[Encoding-Variability]]** — Multiple encoding contexts improve transfer [Report 11]

#### 2.4 Scaffolding & Expertise Development
- **[[pedagogy]]** — Teacher-directed learning for novices [Report 10]
- **[[Andragogy]]** — Self-directed adult learning (Knowles) [Report 10]
- **[[Heutagogy]]** — Self-determined learning; learner designs the learning process itself (Hase & Kenyon) [Reports 10, 24]
- **[[Zone-of-Proximal-Development]]** (ZPD) — Distance between independent and supported performance (Vygotsky) [Reports 10, 23, 30]
- **[[Scaffolding and Fading]]** — Providing then gradually removing learning supports as competence develops [Report 10]
- **[[Dreyfus-Skill-Acquisition-Model]]** — Five-stage novice-to-expert trajectory (Dreyfus & Dreyfus) [Reports 10, 22]

---

### 3. Metacognition & Self-Regulated Learning

#### 3.1 Metacognitive Architecture
- **[[Metacognition]]** — Thinking about one's own thinking; knowledge and regulation of cognitive processes (Flavell) [Reports 04, 12]
  - [[Metacognitive-Knowledge]] — Knowledge about cognition, tasks, and strategies
  - [[Metacognitive-Monitoring]] — Ongoing assessment of one's cognitive state
  - [[Metacognitive-Control]] — Adjusting strategies in response to monitoring
- **[[Judgment-of-Learning]]** (JOL) — Prospective assessment of future memory performance; typically miscalibrated [Reports 06, 12, 18]
- **[[Feeling-of-Knowing]]** — Sense that one will be able to retrieve information; often unreliable [Report 12]
- **[[Calibration]]** — Accuracy of correspondence between confidence and actual knowledge [Reports 12, 18]
- **[[Dunning-Kruger-Effect]]** — Incompetent individuals overestimate their competence [Reports 18, 07]

#### 3.2 Self-Regulated Learning
- **[[Self-Regulated-Learning]]** (SRL) — Metacognitively guided, motivationally active, behaviorally engaged learning (Zimmerman) [Reports 04, 12]
  - [[Zimmerman-SRL-Model]] — Three-phase cycle: Forethought → Performance → Self-Reflection [Reports 04, 12]
  - [[Monitoring-Control Loop]] — Core mechanism of self-regulation [Report 04]
- **[[Implementation-Intentions]]** — If-then plans that automate intention-to-behavior conversion (Gollwitzer) [Report 12]
- **[[Structural-Metacognition-Principle]]** — Monitoring requires structural embedding, not just intention [Report 12] ***ORIGINAL SYNTHESIS***

#### 3.3 Reflective Practice
- **[[Dewey-Reflective-Inquiry]]** — Five-phase model of reflective problem-solving (Dewey) [Reports 04, 08, 12]
- **[[Kolb-Experiential-Learning-Cycle]]** — Concrete Experience → Reflective Observation → Abstract Conceptualization → Active Experimentation (Kolb) [Report 08]
- **[[Schön's Reflective Practice]]** — Reflection-in-action and reflection-on-action (Schön) [Report 08]

---

### 4. Knowledge Management & Organization

#### 4.1 Knowledge Architecture
- **[[Knowledge-Organization-Systems]]** (KOS) — Formal systems for organizing knowledge: hierarchies, taxonomies, faceted classification (Ranganathan, Hjørland) [Reports 01, 15]
  - [[Hierarchical Classification]] — Single-inheritance tree organization; cognitively limited
  - [[Faceted-Classification]] — Multi-dimensional organization capturing multiple attributes simultaneously (Ranganathan) [Reports 01, 15]
  - [[Ontology]] — Formal specification of conceptual domain structure including typed relationships [Report 15]
  - [[Emergent Structure]] — Organization arising from use rather than imposed from above [Report 15]
- **[[Cognitive-Alignment-Principle]]** — PKB architecture should mirror expert semantic memory structure [Report 01] ***ORIGINAL SYNTHESIS***

#### 4.2 Note Architecture
- **[[Three-Tier-Note-Architecture]]** — Atomic Notes, Concept Notes, Maps of Content (MOC) [Report 27, DP1]
  - [[Atomic Note]] — Single-concept, richly-linked, minimal-scope note
  - [[Concept Note]] — Integrative synthesis of multiple atomics within a conceptual cluster
  - [[Map of Content]] (MOC) — Navigational hub for an entire domain or project
- **[[Linking Philosophy]]** — Links as conceptual claims (relationship encoding), not navigational shortcuts [Report 27, DP2]

#### 4.3 Tacit Knowledge
- **[[Tacit-Knowledge]]** — Knowledge that is functionally operative but cannot be fully articulated (Polanyi) [Report 22]
  - [[Focal/Subsidiary Attention Distinction]] — Making subsidiary awareness focal disrupts skilled performance (Polanyi) [Report 22]
  - [[Explicit-Knowledge]] — Articulable, codifiable, transmissible propositional knowledge [Report 22]
- **[[SECI-Model]]** — Knowledge creation through Socialization, Externalization, Combination, Internalization (Nonaka & Takeuchi) [Reports 08, 22]
- **[[Tacit-Knowledge-Observatory]]** — The PKB's proper relationship to tacit knowledge: mapping rather than storing [Report 22] ***ORIGINAL SYNTHESIS***

---

### 5. Network Science & Integration

#### 5.1 Network Architecture
- **[[Small-World Network Topology]]** — High local clustering + short average path lengths; optimal PKB topology (Watts & Strogatz) [Reports 01, 25]
- **[[Betweenness-Centrality]]** — Proportion of shortest paths passing through a node; measure of bridge importance (Freeman) [Report 25]
- **[[Degree Centrality]]** — Number of direct connections; measure of hub importance [Report 25]
- **[[Clustering Coefficient]]** — Measure of local connectivity density [Report 25]
- **[[Weak Ties]]** — Infrequent connections between otherwise-distant network regions; valuable for bridging (Granovetter) [Reports 01, 25]

#### 5.2 Knowledge Integration
- **[[Integration Problem]]** — The failure of accumulated notes to become functionally connected understanding [Report 25] ***CENTRAL DIAGNOSIS***
- **[[Knowledge-Integration]]** — Active connecting, sorting, and organizing of multiple ideas into coherent frameworks (Linn) [Report 25]
- **[[Conceptual-Change]]** — Restructuring of fundamental categories and frameworks (enrichment vs. revision vs. framework theory change) (Vosniadou, Chi) [Report 25]
- **[[Threshold-Concepts]]** — Portal-concepts that transform how a learner perceives an entire domain (Meyer & Land) [Report 25]
- **[[Integration-Metabolism]]** — Scheduled, active maintenance of knowledge integration (weekly, monthly, annual cycles) [Report 27] ***ORIGINAL SYNTHESIS***

---

### 6. Motivational Psychology

- **[[Self-Determination-Theory]]** (SDT) — Autonomous motivation requires satisfaction of Autonomy, Competence, and Relatedness needs (Deci & Ryan) [Reports 05, 24]
- **[[Achievement-Goal-Theory]]** — Mastery-approach vs. performance-approach vs. performance-avoidance goals (Elliot, Dweck) [Reports 05, 13]
- **[[Mindset Theory]]** — Growth mindset (intelligence is developable) vs. fixed mindset (Dweck) [Reports 05, 13]
- **[[Intrinsic-Motivation]]** — Motivation arising from inherent interest or enjoyment; most durable [Reports 05, 13, 19]
- **[[Habit-Formation]]** — Neural pathway formation through cue-routine-reward repetition [Reports 12, 19, 29]

---

### 7. Philosophy & Ethics

- **[[Virtue-Epistemology]]** — Epistemic excellence as intellectual character cultivation (Zagzebski, Sosa, Greco) [Reports 07, 18, 29]
  - [[Intellectual-Virtue]] — Stable character disposition producing epistemically good outcomes [Report 29]
  - [[Intellectual-Vice]] — Stable character disposition undermining epistemic outcomes (Cassam) [Report 29]
  - [[Epistemic-Conscientiousness]] — Disposition to care sufficiently about getting things right (Baehr) [Report 29]
  - [[Epistemic-Humility]] — Calibrated modesty about the limits of one's knowledge [Reports 18, 29]
- **[[Stoic-Ethics]]** — Epictetus, Marcus Aurelius; Dichotomy of Control; Prosoche; Synkatathesis [Reports 07, 13, 29]
  - [[Stoic-Assent]] (Synkatathesis) — Act of accepting or rejecting an impression as accurately representing reality [Report 29]
  - [[Dichotomy-of-Control]] — Focus only on what is genuinely within one's control [Reports 07, 13]
- **[[Epistemic-Justice]]** — Whose testimony and experience is recognized as credible knowledge (Fricker) [Report 29]
- **[[pragmatism]]** — Dewey, Peirce; truth as what works; Fallibilism; inquiry as problem-solving [Reports 07, 08, 14]

---

### 8. AI-Enhanced PKM

- **[[Extended-Mind-Theory]]** — Cognitive tools can become genuine components of a distributed cognitive system (Clark & Chalmers) [Report 30]
- **[[Cognitive-Offloading]]** — Using external resources to reduce working memory demand [Report 30]
  - [[Storage Offloading]] — Offloading memory storage (generally beneficial) [Report 30]
  - [[Synthesis Offloading]] — Offloading reasoning and construction (generally harmful for learning) [Report 30]
  - [[Offloading Quality Distinction]] — The critical difference between beneficial and harmful AI assistance [Report 30] ***ORIGINAL SYNTHESIS***
- **[[Retrieval-Augmented-Generation]]** (RAG) — AI retrieval enhanced by knowledge base content [Report 30]
- **[[Google Effect]]** — Expecting future AI retrieval reduces present encoding depth (Sparrow et al.) [Report 30]
- **[[Epistemic Counterfeiting]]** — AI-generated synthesis producing knowledge-appearance without understanding substrate [Report 30] ***ORIGINAL SYNTHESIS***

---

## Concept Relationship Matrix (Key Relationships)

| Concept A | Relationship Type | Concept B | Strength |
|-----------|------------------|-----------|----------|
| [[Cognitive-Alignment-Principle]] | derives from | [[Schema-Theory]] + [[KOS]] | Strong |
| [[Cognitive-Alignment-Principle]] | mandates | [[Three-Tier-Note-Architecture]] | Strong |
| [[Testing-Effect]] | contradicts | [[Fluency-Illusion]] | Strong |
| [[Desirable-Difficulties]] | conflicts with | AI convenience | Strong |
| [[Dreyfus Skill Model]] | isomorphic with | [[Expertise-Reversal-Effect]] (CLT) | Strong |
| [[Knowledge-Integration]] | isomorphic with | Small-World Network topology | Strong |
| [[Structural-Metacognition-Principle]] | operationalizes | [[Zimmerman-SRL-Model]] | Moderate |
| [[Tacit-Knowledge-Observatory]] | reframes | PKB comprehensiveness aspiration | Strong |
| [[Integration-Metabolism]] | implements | [[Knowledge-Integration]] | Moderate |
| [[Virtue-Epistemology]] | bridges with | [[Habit-Formation]] | Moderate |
| [[Inert-Knowledge]] | is produced by | enrichment without restructuring | Strong |
| [[Weak Ties]] | are analogous to | variable encoding contexts | Moderate |
| [[Betweenness-Centrality]] | identifies | integration bridge notes | Strong |
| [[Threshold-Concepts]] | function as | high-betweenness-centrality nodes | Moderate |

---

## Hub Concepts (Most Connected — Appearing in 5+ Reports)

1. **[[Schema-Theory]]** — Reports 01, 02, 03, 04, 06, 09, 10, 11 (8+ reports)
2. **[[Metacognition]]** / **[[Metacognitive-Monitoring]]** — Reports 04, 06, 07, 08, 12, 17, 18, 26 (8+ reports)
3. **[[Desirable-Difficulties]]** — Reports 06, 11, 16, 20, 30 (5 reports)
4. **[[Self-Regulated-Learning]]** — Reports 04, 06, 08, 12, 18, 19, 24, 26 (8+ reports)
5. **[[Cognitive-Load-Theory]]** — Reports 02, 03, 09, 10, 11, 16 (6 reports)
6. **[[Constructivism]]** — Reports 01, 03, 08, 09, 14, 17 (6 reports)
7. **[[Fluency-Illusion]]** — Reports 06, 12, 18, 30 (4 reports, but central to the diagnosis)
8. **[[Testing-Effect]]** / **[[Retrieval-Practice]]** — Reports 06, 12, 16, 20, 27 (5+ reports)

---

## Bridge Concepts (Cross-Domain Connectors)

| Bridge Concept | Domain A | Domain B | Connection Type |
|---------------|----------|----------|----------------|
| [[Spreading-Activation]] | Cognitive Science | Network Science | Semantic memory as graph |
| [[Encoding-Specificity]] | Memory Science | Transfer of Learning | Same mechanism, different applications |
| [[Expertise-Reversal-Effect]] | CLT | Dreyfus Model | Cognitive architecture ↔ phenomenology |
| [[Weak Ties]] | Network Science | Transfer of Learning | Bridge notes ↔ variable encoding |
| [[Habit-Formation]] | Behavioral Science | Virtue Epistemology | Character as neural pathway |
| [[Implementation-Intentions]] | Behavioral Science | Metacognition | Bridging knowing to doing |

---

## Orphan Concepts (Weakly Connected — Needing Integration)

- **[[Epistemic-Justice]]** — Introduced in Report 29 with insufficient connections to the rest of the series
- **[[Extended-Mind-Theory]]** — Report 30's most philosophically interesting concept; could be connected back to Reports 01 and 09
- **[[Nonaka SECI Model]]** — Introduced in Reports 08 and 22 but its Socialization dimension is underconnected to the rest of the framework
- **[[Pragmatist-Epistemology]]** — Report 08 and 14 treat this; connections to virtue epistemology (Report 29) are underdeveloped

---

*Taxonomy Version 1.0.0 — Extracted by PKB Codebase Review & Synthesis Agent*
*Source: pkb-pkm-report-series-codebase-pack.md*
*Concepts marked ***ORIGINAL SYNTHESIS*** indicate novel contributions of the series, not pre-existing established concepts*
