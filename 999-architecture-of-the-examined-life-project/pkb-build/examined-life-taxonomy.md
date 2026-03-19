---
title: "The Architecture of the Examined Life: Taxonomy & Concept Registry"
aliases:
  - "Examined Life Taxonomy"
  - "AEL Concept Registry"
type: taxonomy
status: evergreen
confidence: high
doc_id: "examined-life-taxonomy-v1-0"
doc_type: "taxonomy"
doc_created: 2026-03-19
doc_modified: 2026-03-19
author: "claude-opus-4"
primary_domain: "epistemic-cognition"
tags:
  - taxonomy
  - concept-registry
  - knowledge-graph
  - review-artifact
  - epistemic-cognition
source_synthesis: "[[examined-life-synthesis]]"
---

# The Architecture of the Examined Life: Taxonomy & Concept Registry

> [!abstract] Purpose
> Hierarchical classification of all significant concepts extracted from the 41-file Examined Life PKB codebase, organized by domain with definitions, source attributions, epistemic status, and relationship mappings. Designed for navigation, gap identification, and knowledge graph construction.

---

## Domain Taxonomy

### 1. Epistemology & Inquiry

#### 1.1 Foundations of Inquiry
- **[[Aporic-Receptivity]]** — Cultivated willingness to dwell productively in confusion rather than rushing to premature closure. [Source: R01] [Status: Novel synthesis]
  - **[[Aporia]]** — State of genuine puzzlement where existing schemas fail to accommodate new evidence. [Source: R01] [Status: Established]
  - **[[Socratic Method]]** — Inquiry through systematically questioning assumptions to expose hidden contradictions. [Source: R01] [Status: Established]
  - **[[Constructivism]]** — Knowledge is actively constructed through engagement with experience, not passively received. [Source: R01, R04] [Status: Established]
  - **[[Constructivist Disequilibrium]]** — The productive disruption when existing schemas cannot assimilate new information. Structurally parallels Socratic aporia. [Source: R01] [Status: Established]

#### 1.2 Epistemological Stance
- **[[Fallibilism]]** — The epistemological position that all knowledge claims are provisional and potentially revisable. [Source: R02] [Status: Established]
  - **[[Epistemic-Humility]]** — Recognition of the limits and revisability of one's own knowledge. [Source: R02, R05] [Status: Established]
  - **[[Popperian Falsificationism]]** — Scientific knowledge advances through attempts to falsify rather than verify. [Source: R02] [Status: Established]

#### 1.3 Epistemic Virtue
- **[[Bias-Virtue Correspondence]]** — Systematic mapping of 5 intellectual virtues onto 5 cognitive bias categories. [Source: R05] [Status: Novel synthesis]
  - **[[Intellectual-Humility]]** ↔ [[Overconfidence Bias]] [Source: R05]
  - **[[Open-mindedness]]** ↔ [[Confirmation Bias]] [Source: R05]
  - **[[Intellectual-Courage]]** ↔ [[Conformity Bias]] [Source: R05]
  - **[[Intellectual Thoroughness]]** ↔ [[Availability Bias]]/[[Anchoring Bias]] [Source: R05]
  - **[[Intellectual Patience]]** ↔ [[Premature Closure]] [Source: R05]
- **[[Social Epistemic Virtue]]** — Community-level virtues extending individual intellectual virtue into communal epistemic practices. [Source: R12] [Status: Novel synthesis]
  - **[[Epistemic Injustice]]** — Injustice done to someone specifically in their capacity as a knower. Fricker's concept. [Source: R12] [Status: Established]
  - **[[Testimonial-Injustice]]** — Deflated credibility given to a speaker due to identity-based prejudice. [Source: R12] [Status: Established]

### 2. Cognitive Science & Metacognition

#### 2.1 Dual Process Theory
- **[[System 1]]** — Fast, automatic, intuitive cognitive processing. [Source: R06] [Status: Established]
- **[[System 2]]** — Slow, effortful, deliberate cognitive processing. [Source: R06] [Status: Established]
- **[[Governed Attentional Gap]]** — Space between System 1 automatic response and System 2 deliberate intervention, where metacognitive attention (prosoche) intervenes. [Source: R06] [Status: Novel synthesis]
- **[[Stanovich Tripartite Model]]** — Autonomous mind, algorithmic mind, reflective mind — more differentiated than Kahneman's dual model. [Source: R06, ref-stanovich] [Status: Established]
  - **[[Dysrationalia]]** — Systematic irrationality despite adequate intelligence. [Source: ref-stanovich] [Status: Established]
  - **[[Mindware]]** — Cognitive rules, procedures, and strategies available for deployment in thinking. [Source: ref-stanovich] [Status: Established]

#### 2.2 Metacognition
- **[[Metacognition]]** — Thinking about thinking; monitoring and governing one's own cognitive processes. [Source: All reports] [Status: Established]
- **[[Metacognitive Monitoring]]** — Tracking the quality and accuracy of ongoing cognitive processes. Functionally identical to Stoic prosoche. [Source: R06] [Status: Established]
- **[[Physiological-Metacognition]]** — Integration of bodily self-knowledge (somatic signals, interoception, arousal) into the metacognitive monitoring system. [Source: R09, expansion topic] [Status: Emerging]
  - **[[Interoception]]** — Perception of internal bodily states. [Source: R09, expansion topic] [Status: Established]
  - **[[Interoceptive Accuracy]]** — Objective precision in detecting internal bodily signals. Garfinkel Dimension 1. [Source: expansion topic] [Status: Established]
  - **[[Interoceptive Sensibility]]** — Subjective report of interoceptive experience quality. Garfinkel Dimension 2. [Source: expansion topic] [Status: Established]
  - **[[Interoceptive Awareness]]** — Metacognitive accuracy about interoceptive prediction. Garfinkel Dimension 3. [Source: expansion topic] [Status: Established]
- **[[Narrative Metacognition]]** — Recursive examination of one's own life story as a metacognitive practice. Highest-order metacognitive operation. [Source: R14] [Status: Novel synthesis]

#### 2.3 Cognitive Bias
- **[[Cognitive-Bias]]** — Systematic patterns of deviation from rationality in judgment. [Source: R05, R06] [Status: Established]
- **[[Overconfidence Bias]]** — Excessive confidence in one's own answers and judgments. [Source: R05] [Status: Established]
- **[[Confirmation Bias]]** — Tendency to seek, interpret, and recall information confirming existing beliefs. [Source: R05] [Status: Established]
- **[[Conformity Bias]]** — Adjusting beliefs to align with perceived group consensus. [Source: R05] [Status: Established]
- **[[Availability Bias]]** — Judging likelihood based on how easily examples come to mind. [Source: R05] [Status: Established]
- **[[Anchoring Bias]]** — Over-relying on the first piece of information encountered. [Source: R05] [Status: Established]
- **[[Premature Closure]]** — Reaching conclusions before sufficient evidence has been gathered. [Source: R05] [Status: Established]
- **[[Affective-Realism]]** — Experiencing affect-influenced perceptions as objective properties of the world. [Source: R10] [Status: Established]

### 3. Predictive Processing

- **[[Predictive-Processing]]** — The brain as a prediction machine generating top-down expectations and updating them via prediction errors. [Source: R13] [Status: Established]
- **[[Precision-Flexibility]]** — Dynamic adjustment of weighting between prior beliefs and incoming evidence — the computational mechanism of the examined life. [Source: R13] [Status: Novel synthesis]
  - **[[Precision-Weighting]]** — Assigning confidence levels to predictions and prediction errors. [Source: R13] [Status: Established]
  - **[[Prediction-Error]]** — Mismatch between top-down predictions and bottom-up sensory signals. [Source: R13] [Status: Established]
  - **[[Active-Inference]]** — Acting on the world to confirm predictions, not just passively updating from error signals. [Source: R13] [Status: Established]
  - **[[Free-Energy-Principle]]** — Friston's formalization: organisms minimize variational free energy (surprise). [Source: R13] [Status: Established]
- **[[Interoceptive Predictive Processing]]** — Seth's extension: bodily sensations as "controlled hallucinations" generated by interoceptive prediction. [Source: R09, expansion topic] [Status: Emerging]

### 4. Emotion Science

- **[[Theory-of-Constructed-Emotion]]** — Barrett's framework: emotions are not triggered reactions but active constructions from affect, concepts, and context. [Source: R10, ref-barrett] [Status: Established]
- **[[Emotional-Granularity]]** — The capacity to make fine-grained distinctions between emotional states. Reframed as epistemic precision. [Source: R10] [Status: Established]
- **[[Emotional-Granularity-as-Epistemic-Precision]]** — The more precisely you differentiate emotions, the more epistemic information they carry about belief adequacy. [Source: R10] [Status: Novel synthesis]
- **[[Somatic-Marker-Hypothesis]]** — Damasio's theory that bodily feeling-states guide decision-making and reasoning. [Source: R09, ref-damasio] [Status: Established]
  - **[[Somatic Markers]]** — Bodily feeling-states associated with outcomes that guide decision-making. [Source: R09] [Status: Established]

### 5. Stoic Philosophy

#### 5.1 Core Stoic Concepts
- **[[Prosoche]]** — Stoic attention/vigilance; continuous self-monitoring of impressions and judgments. Functionally identical to metacognitive monitoring. [Source: R06, ref-epictetus] [Status: Established]
- **[[Prohairesis]]** — Stoic moral purpose/faculty of choice; the sovereign capacity to assent or withhold assent. Structurally isomorphic to SDT autonomy. [Source: R03, ref-epictetus] [Status: Established]
- **[[Synkatathesis]]** — Stoic assent to impressions; the cognitive act of accepting a representation as true. Maps to precision weighting in PP. [Source: expansion topic] [Status: Established]
- **[[Hēgemonikon]]** — The governing faculty/ruling capacity of the soul in Stoic psychology. [Source: expansion topic] [Status: Established]
- **[[Prokoptōn]]** — "The one making progress" — the Stoic developmental ideal; someone genuinely advancing toward wisdom without claiming to have arrived. [Source: R15] [Status: Established]

#### 5.2 Stoic Emotion Theory
- **[[Propatheiai]]** — Pre-emotions/proto-passions: involuntary somatic-affective responses occurring before rational assent. Even the Stoic sage experiences them. [Source: expansion topic] [Status: Established]
  - Three essential features: involuntary/blameless, no assent given, occur even in the sage
- **[[Pathē]]** — Irrational passions resulting from false assent. Four categories: [[lupē]] (distress), [[hēdonē]] (pleasure), [[phobos]] (fear), [[epithumia]] (appetite). [Source: R10, expansion topic] [Status: Established]
- **[[Eupatheia]]** — "Good feelings" — rational emotional states of the sage. Three categories: [[chara]] (joy), [[boulēsis]] (wish), [[eulabeia]] (caution). No rational counterpart to distress. [Source: R10, expansion topic] [Status: Established]
- **[[Phantasia]]** — Impression/representation — the initial appearing of an event to consciousness, prior to judgment. [Source: expansion topic] [Status: Established]
- **[[Hormē]]** — Impulse to action generated when assent is given to an impression with action-relevance. [Source: expansion topic] [Status: Established]

#### 5.3 Stoic Practices
- **[[Askesis]]** — Spiritual exercises; disciplined practice aimed at philosophical transformation. Parallel to modern deliberate practice. [Source: R08, ref-hadot] [Status: Established]
- **[[View from Above]]** — Marcus Aurelius' meditation technique: viewing events from a cosmic perspective to calibrate significance. [Source: ref-marcus-aurelius] [Status: Established]
- **[[Evening Self-Examination]]** — Seneca's three-question review practice; prototype of modern reflective journaling. [Source: ref-marcus-aurelius, R08] [Status: Established]
- **[[Dichotomy of Control]]** — Epictetus' distinction between what is "up to us" (prohairesis) and what is not. [Source: ref-epictetus] [Status: Established]

### 6. Educational Psychology & Development

#### 6.1 Learning Theory
- **[[Cognitive Load Theory]]** — Sweller's framework: intrinsic, extraneous, and germane cognitive load. [Source: R04] [Status: Established]
- **[[Zone of Proximal Development]]** — Vygotsky's concept: the space between what a learner can do alone and what they can do with guidance. [Source: R04, ref-vygotsky] [Status: Established]
- **[[Scaffolding]]** — Structured support that enables learning within the ZPD. [Source: R04, ref-vygotsky] [Status: Established]
- **[[Self-Regulated Learning]]** — Zimmerman's framework: forethought → performance → self-reflection cycle. [Source: R07] [Status: Established]
- **[[Recursive-Self-Authorship]]** — The capacity to design and manage one's own epistemic development. SRL ↔ SDT internalization homology. [Source: R07] [Status: Novel synthesis]

#### 6.2 Motivation
- **[[Self-Determination Theory]]** — Deci & Ryan: three innate needs — autonomy, competence, relatedness — driving intrinsic motivation. [Source: R03, ref-deci-ryan] [Status: Established]
- **[[Cognitive-Vitality]]** — Self-sustaining motivational state fueling continued epistemic engagement. Synthesizes SDT intrinsic motivation with Stoic prohairesis. [Source: R03] [Status: Novel synthesis]
- **[[Internalization-Continuum]]** — SDT's spectrum from external regulation → introjected → identified → integrated motivation. [Source: R03, R07] [Status: Established]

#### 6.3 Developmental Framework
- **[[5-Stage Developmental Model]]** — Adapted from Dreyfus and SDT internalization for the examined life. [Source: R15, staging note] [Status: Novel framework]
  - **Stage 1: Conscious Incompetence (Awakening)** — Initial recognition of cognitive limitations
  - **Stage 2: Deliberate Practice (Building)** — Systematic effortful application of individual components
  - **Stage 3: Integrated Practice (Weaving)** — Components begin operating together; fragile under stress
  - **Stage 4: Emerging Orientation (Inhabiting)** — The framework becomes a natural orientation, not imposed discipline
  - **Stage 5: The Examined Life (Being)** — Full integration; examined living as natural expression of personhood

### 7. Practical Wisdom & Action

- **[[Phronesis]]** — Aristotelian practical wisdom: the trained perceptual-evaluative capacity to discern what situations require and respond appropriately. [Source: R11, ref-aristotle] [Status: Established]
- **[[Action-Perception Link]]** — The phronimos and Klein's RPD expert are the same kind of knower: both perceive what situations require through trained perception. [Source: R11] [Status: Novel synthesis]
- **[[Recognition-Primed Decision Making]]** — Klein's NDM model: experts make decisions by pattern-matching to previously experienced situations, not by analyzing options. [Source: R11] [Status: Established]
- **[[Knowing-How vs Knowing-That]]** — Ryle's distinction between practical competence and propositional knowledge. [Source: ref-ryle, R05, R11] [Status: Established]

### 8. Narrative Psychology

- **[[Narrative Identity]]** — McAdams' concept: the internalized, evolving story of the self that integrates reconstructed past and imagined future into a purposeful life story. [Source: R14] [Status: Established]
- **[[Narrative Coherence]]** — The degree to which a life story is internally consistent, temporally organized, and experientially meaningful. [Source: R14] [Status: Established]
- **[[Redemptive Narrative]]** — McAdams' pattern: life stories that move from suffering to positive outcome, generating resilience and generativity. [Source: R14] [Status: Established]
- **[[Contamination Narrative]]** — McAdams' counter-pattern: life stories where positive beginnings decay into negative outcomes. [Source: R14] [Status: Established]

### 9. Embodied Cognition

- **[[Embodied-Cognition]]** — The view that cognitive processes are shaped by and dependent upon the body and its interactions with the environment. [Source: R09, expansion topic] [Status: Established]
- **[[4E-Cognition]]** — Cognition as embodied, embedded, enactive, and extended. [Source: expansion topic] [Status: Established]
- **[[Allostasis]]** — Predictive regulation of the body's internal environment — maintaining stability through anticipatory change. [Source: expansion topic] [Status: Established]
  - **[[Allostatic-Load]]** — Cumulative physiological cost of chronic stress and allostatic regulation. Directly degrades cognitive tools needed for the examined life. [Source: expansion topic] [Status: Established]
- **[[Affordances]]** — Action possibilities offered by the environment to an agent with specific bodily capabilities. [Source: expansion topic] [Status: Established]

### 10. Integrative Concepts (Series-Specific)

- **[[Integrated-Cognitive-Personhood]]** — The examined life constitutes personhood in its fullest expression, not a set of skills added to a pre-existing person. [Source: R15] [Status: Speculative/theoretical]
- **[[Epistemic-Character-as-Concurrent-Expression]]** — Tier 1's seven components operating as unified mode of being, not additive checklist. [Source: R08] [Status: Novel synthesis]
- **[[Constructive-Attentiveness]]** — Synthesis of CLT and ZPD; the capacity to manage attentional resources in service of learning. [Source: R04] [Status: Novel synthesis]
- **[[Structural Homology]]** — The series' core analytical method: identifying deep structural parallels between ancient philosophy and modern cognitive science. [Source: Cross-cutting] [Status: Methodological]

---

## Concept Relationship Matrix (Top 20 Connections)

| Concept A | Relationship | Concept B | Strength | Source |
|-----------|-------------|-----------|----------|--------|
| [[Prosoche]] | ≡ Functional identity | [[Metacognitive Monitoring]] | Strong | R06 |
| [[Prohairesis]] | ≈ Structural isomorphism | [[SDT Autonomy]] | Strong | R03 |
| [[Propatheiai]] | ↔ Neural substrate | [[LeDoux Low Road]] | Moderate | Expansion |
| [[Eupatheia]] | ↔ Reconceptualization | [[TCE Categories]] | Moderate | R10 |
| [[Phronimos]] | ↔ Expertise model | [[RPD Expert]] | Strong | R11 |
| [[Socratic-Dialectic]] | ↔ Functional account | [[Argumentative Theory]] | Moderate | R12 |
| [[Synkatathesis]] | ↔ Computational mechanism | [[Precision-Weighting]] | Moderate | R13 |
| [[Askesis]] | ↔ Therapeutic parallel | [[Deliberate Practice]] | Strong | R08 |
| [[Prokoptōn]] | ↔ Developmental parallel | [[Dreyfus Model]] | Moderate | R15 |
| [[Aporia]] | ↔ Functional equivalence | [[Constructivist Disequilibrium]] | Strong | R01 |
| [[Metacognition]] | extends into | [[Physiological-Metacognition]] | Strong | R09 |
| [[Metacognition]] | extends into | [[Narrative Metacognition]] | Strong | R14 |
| [[Allostatic-Load]] | degrades | [[Metacognitive-Capacity]] | Moderate | Expansion |
| [[Emotional-Granularity]] | IS a form of | [[Epistemic Precision]] | Strong | R10 |
| [[Precision-Flexibility]] | mechanism of | [[Aporic-Receptivity]] | Strong | R13 |
| [[Precision-Flexibility]] | mechanism of | [[Intellectual-Humility]] | Strong | R13 |
| [[Narrative Identity]] | highest-level | [[Generative Model (PP)]] | Moderate | R14 |
| [[Bias-Virtue Correspondence]] | operationalizes | [[Intellectual-Virtue]] | Strong | R05 |
| [[Cognitive-Vitality]] | synthesizes | [[SDT]] + [[Stoic Prohairesis]] | Strong | R03 |
| [[Integrated-Cognitive-Personhood]] | integrates all | [[All 15 Dimensions]] | Theoretical | R15 |

---

## Hub Concepts (Most Connected — Ranked)

1. **[[Metacognition]]** — 15/15 reports, 3 expansion topics, 5+ reference notes. The master practice of the examined life.
2. **[[Stoic Philosophy]]** — 12/15 reports, 2 expansion topics, 3 reference notes. Primary ancient interlocutor.
3. **[[Predictive-Processing]]** — 5/15 reports directly, but provides mechanism for all. The unifying computational framework.
4. **[[Self-Determination Theory]]** — 6/15 reports, 1 reference note. Foundational for motivation and development.
5. **[[Phronesis]]** — 8/15 reports, 1 reference note. Foundational for practical dimension.
6. **[[Intellectual-Virtue]]** — 7/15 reports. Bridge between epistemology and character.
7. **[[Emotional-Granularity]]** — 4/15 reports, 1 expansion topic. Bridge between emotion and epistemology.
8. **[[Constructivism]]** — 5/15 reports, 2 reference notes. Learning theory backbone.

## Bridge Concepts (Cross-Domain Connectors — Ranked)

1. **[[Physiological-Metacognition]]** — Bridges embodied cognition ↔ metacognitive theory
2. **[[Precision-Flexibility]]** — Bridges predictive processing ↔ every other component
3. **[[Emotional-Granularity-as-Epistemic-Precision]]** — Bridges emotion science ↔ epistemology
4. **[[Propatheiai]]** — Bridges Stoic philosophy ↔ affective neuroscience
5. **[[Narrative Metacognition]]** — Bridges narrative psychology ↔ metacognition
6. **[[Action-Perception Link]]** — Bridges practical wisdom ↔ expertise research
7. **[[Cognitive-Vitality]]** — Bridges motivation theory ↔ epistemic engagement

## Orphan Concepts (Mentioned but Lacking Standalone Treatment)

These concepts are referenced across reports but lack dedicated expansion topics, connection notes, or glossary entries:

| Concept | Mentioned In | Priority for Standalone Treatment |
|---------|-------------|----------------------------------|
| [[Active-Inference]] | R13 | High — central to PP chapter |
| [[Narrative Identity]] (McAdams) | R14 | High — central to meaning chapter |
| [[Theory-of-Constructed-Emotion]] | R10 | High — Barrett's full framework |
| [[Epistemic Injustice]] (Fricker) | R12 | Medium — social chapter concept |
| [[Neuroplasticity]] | R04, R06 | Medium — underlying mechanism |
| [[Dreyfus-Skill-Acquisition-Model]] | R15, staging | Medium — developmental backbone |
| [[Cognitive Reappraisal]] | R10, expansion | Medium — CBT-Stoic bridge |
| [[Argumentative Theory]] (Mercier & Sperber) | R12 | Medium — social epistemology |
| [[Free-Energy-Principle]] (Friston) | R13 | Medium — PP theoretical foundation |
| [[Hermeneutic Injustice]] | R12 | Low — specified aspect of epistemic injustice |

---

*End of Taxonomy & Concept Registry*
*Extracted from: examined-life-codebase-pack.md (41 files)*
*Generated: 2026-03-19*
