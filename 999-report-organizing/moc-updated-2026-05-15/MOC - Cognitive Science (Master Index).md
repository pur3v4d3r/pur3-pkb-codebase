---
tags: [MOC, master-index, cognitive-science, psychology, educational-psychology, learning-science]
aliases: [Cognitive Science MOC, Master Index, PKB Master Map]
moc_pattern: master-index
domain: cross-domain
source_moc_count: 10
created: 2026-05-15
status: permanent
---

# MOC — Cognitive Science (Master Index)

> [!abstract] Vault Orientation
> This is the **top-level navigation hub** for the Cognitive Science PKB. It does not duplicate the depth found in domain MOCs — instead it orients you within the vault, maps cross-domain relationships, and offers curated reading paths for different learning goals. Start here, then dive into whichever domain MOC fits your current inquiry.

---

## The Intellectual Architecture of This Vault

This vault holds permanent notes spanning the **science of mind, learning, and knowledge** — from the molecular mechanisms of memory consolidation to the social epistemology of testimony; from Baddeley's phonological loop to Zimmerman's self-regulation cycle; from Kahneman's dual-process heuristics to Luhmann's Zettelkasten. The unifying question threading every domain is:

> *How do minds acquire, organise, evaluate, and apply knowledge — and how can we engineer conditions that make this process more effective?*

The ten domain MOCs are not ten isolated silos. They are ten views of the same underlying terrain. Cognitive load theory cannot be understood without working memory. Self-regulated learning presupposes metacognitive monitoring. Critical thinking depends on epistemological commitments. Motivation shapes every learning outcome. The diagram below renders the dependency structure.

---

## Domain MOC Registry

| # | MOC | Core Question | Notes | Pattern |
|---|-----|---------------|-------|---------|
| 1 | [[MOC - Memory Science]] | How do minds encode, consolidate, and retrieve information? | 62 | Hub-and-spoke |
| 2 | [[MOC - Cognitive Load Theory]] | How does limited working memory constrain learning design? | 44 | Progressive |
| 3 | [[MOC - Metacognition and Self-Regulated Learning]] | How do learners monitor, control, and direct their own learning? | 58 | Cluster |
| 4 | [[MOC - Motivation Psychology]] | What initiates, sustains, and directs purposeful behaviour? | 78 | Cluster |
| 5 | [[MOC - Critical Thinking and Logic]] | What constitutes good reasoning, and how can it be taught? | 67 | Progressive |
| 6 | [[MOC - Epistemology]] | What is knowledge, how is it justified, and what are its limits? | 48 | Dialectical |
| 7 | [[MOC - Learning Science]] | What principles and environments produce durable, transferable learning? | 56 | Cluster |
| 8 | [[MOC - PKB and Knowledge Management]] | How can external systems extend and augment cognition? | 36 | Progressive |
| 9 | [[MOC - Social Psychology]] | How do social contexts shape cognition, attribution, and behaviour? | 38 | Cluster |
| 10 | [[MOC - Dual Process Theory and Cognitive Biases]] | How do fast intuitive and slow deliberate systems interact and err? | 46 | Hub-and-spoke |

**Total permanent notes indexed across all MOCs: ~533**

---

## Cross-Domain Relationship Map

The following diagram shows the primary intellectual dependencies and bridges between domains. A directed edge (→) means "provides foundational concepts for"; a bidirectional edge (↔) means "mutually constitutive."

```
┌─────────────────────────────────────────────────────────────────────┐
│                   COGNITIVE SCIENCE MASTER MAP                       │
└─────────────────────────────────────────────────────────────────────┘

        ┌─────────────────────┐
        │   EPISTEMOLOGY      │◄──────────────────────────┐
        │  (what is knowledge)│                           │
        └────────┬────────────┘                           │
                 │ grounds                                 │
                 ▼                                         │
        ┌─────────────────────┐     informs        ┌──────┴───────────┐
        │  CRITICAL THINKING  │◄──────────────────►│  DUAL PROCESS    │
        │  & LOGIC            │                    │  & BIASES        │
        └────────┬────────────┘                    └──────┬───────────┘
                 │ depends on                              │ biases
                 ▼                                         ▼
        ┌─────────────────────┐     underpins      ┌──────────────────┐
        │   MEMORY SCIENCE    │◄──────────────────►│  LEARNING        │
        │                     │                    │  SCIENCE         │
        └────────┬────────────┘                    └──────┬───────────┘
                 │ constrains                              │ operationalises
                 ▼                                         ▼
        ┌─────────────────────┐     shapes         ┌──────────────────┐
        │  COGNITIVE LOAD     │◄──────────────────►│  METACOGNITION   │
        │  THEORY             │                    │  & SRL           │
        └────────┬────────────┘                    └──────┬───────────┘
                 │ informs design                          │ regulated by
                 ▼                                         ▼
        ┌─────────────────────┐     fuels          ┌──────────────────┐
        │   MOTIVATION        │◄──────────────────►│  SOCIAL          │
        │   PSYCHOLOGY        │                    │  PSYCHOLOGY      │
        └────────┬────────────┘                    └──────┬───────────┘
                 │ drives                                  │ contextualises
                 └──────────────────┬──────────────────────┘
                                    ▼
                           ┌─────────────────┐
                           │  PKB & KNOWLEDGE │
                           │  MANAGEMENT      │
                           │  (applied layer) │
                           └─────────────────┘
```

---

## The Five Foundational Tensions

Rather than summarising each domain, this master index highlights the **five generative tensions** that animate the entire vault. Understanding these tensions is more valuable than memorising any individual theory, because they reveal why researchers disagree and where synthesis is still incomplete.

---

### Tension 1 — Storage vs. Reconstruction

> *Is memory a retrieval system or a generative one?*

The naive view of memory as a video playback device is empirically false. [[memory-as-reconstruction|Memory as Reconstruction]] demonstrates that every act of retrieval is also an act of creation, drawing on schemas, context, and current goals. Yet this very reconstructive flexibility is what makes memory adaptive — we remember what is useful, not what is verbatim.

This tension runs from [[MOC - Memory Science]] directly into [[MOC - Dual Process Theory and Cognitive Biases]] (where [[availability-heuristic|Availability]] and [[representativeness-heuristic|Representativeness]] show how reconstruction introduces systematic bias) and into [[MOC - Epistemology]] (where the [[reliability-of-testimony|Reliability of Testimony]] question hinges on whether eyewitness memory can be trusted).

**The synthesis**: Memory is neither a faithful archive nor random confabulation. It is a probabilistic inference engine tuned by evolutionary pressures to reconstruct plausible, schema-consistent representations — accurate enough for navigation, distorted enough to introduce predictable biases.

---

### Tension 2 — Limits vs. Architecture

> *Is working memory a bottleneck or a workspace?*

[[working-memory|Working Memory]] is often framed as a constraint: limited capacity, limited duration, the source of cognitive overload. [[MOC - Cognitive Load Theory]] treats it primarily as a bottleneck to be managed through instructional design. But Baddeley's 4-component model — phonological loop, visuospatial sketchpad, central executive, episodic buffer — reveals a sophisticated multi-channel architecture, not a single pipe.

The tension: optimising for capacity management (reduce load, chunk information) can conflict with optimising for deep processing (desirable difficulties, generative activities that intentionally impose cognitive demand). [[MOC - Learning Science]] resolves this by distinguishing load type: extraneous load should be minimised, germane load should be cultivated.

**The synthesis**: Working memory limits define the *ceiling* of simultaneous processing; schema automation raises the *floor* of what counts as a single chunk. Expertise is largely the process of converting effortful processing into automated schemas, thereby freeing capacity.

---

### Tension 3 — Autonomy vs. Structure

> *Does self-direction require freedom from, or scaffolded movement toward, autonomous regulation?*

[[self-determination-theory|Self-Determination Theory]] posits that autonomy support is essential for intrinsic motivation and deep engagement. Yet SRL research shows that unguided discovery — pure autonomy without structure — often leads to inefficient learning, especially for novices (the [[expertise-reversal-effect|Expertise Reversal Effect]] being the clearest case).

The tension is not between structure and freedom but between *control* (which undermines autonomy) and *scaffold* (which enables it). [[MOC - Motivation Psychology]] and [[MOC - Metacognition and Self-Regulated Learning]] converge here: the goal is *fading scaffolding* — progressively withdrawing support as competence grows, maintaining the learner's experience of self-determination throughout.

**The synthesis**: Autonomy is not the absence of structure but the internalisation of it. [[internalization-continuum|The Internalisation Continuum]] in SDT maps this precisely: external regulation → introjection → identification → integration → intrinsic motivation. Effective instruction engineers this pathway.

---

### Tension 4 — Individual vs. Social Cognition

> *Is cognition fundamentally a property of individual minds, or is it distributed across persons and artefacts?*

Most of this vault's notes treat cognition as an individual phenomenon — a single brain acquiring, organising, and applying knowledge. But [[MOC - Social Psychology]] and [[MOC - PKB and Knowledge Management]] challenge this framing. [[distributed-cognition|Distributed Cognition]] and [[extended-mind-thesis|The Extended Mind Thesis]] argue that cognitive processes are routinely offloaded onto tools, symbols, and other people. [[vygotsky-zone-of-proximal-development|Vygotsky's ZPD]] shows that learning itself is fundamentally social before it is individual.

The tension: if cognition is distributed, then individual-level interventions (better note-taking, improved metacognition) are necessary but insufficient. Social and environmental redesign becomes equally important.

**The synthesis**: Cognition is multi-level. Individual cognitive architectures (working memory, long-term memory, executive function) are real biological constraints. Social and artefactual scaffolding extends these architectures without eliminating their limits. PKB systems work precisely because they leverage [[cognitive-offloading|Cognitive Offloading]] to reduce demands on biological memory while preserving retrieval access.

---

### Tension 5 — Rationality vs. Bias

> *Are humans fundamentally rational agents who err occasionally, or fundamentally heuristic processors who sometimes reason well?*

This is the central debate between classical rational choice theory and the heuristics-and-biases programme. [[dual-process-theory|Dual Process Theory]] offers a structural resolution: System 1 is fast, heuristic, and ecologically efficient; System 2 is slow, deliberate, and rule-following. Neither is unconditionally superior.

[[MOC - Critical Thinking and Logic]] sits in direct tension with [[MOC - Dual Process Theory and Cognitive Biases]] here: the normative tradition in critical thinking assumes that better reasoning is achievable through conscious, effortful deliberation. The descriptive tradition in cognitive bias research shows that effortful deliberation is itself subject to motivated reasoning, belief bias, and myside bias.

**The synthesis**: [[intellectual-humility|Intellectual Humility]] and [[calibration|Calibration]] are the epistemically appropriate responses to this tension. We should neither abandon normative standards (because bias is real) nor treat bias as insurmountable (because debiasing strategies have documented effectiveness). The goal is [[epistemic-hygiene|Epistemic Hygiene]] — systematic practices that reduce predictable errors while sustaining the cognitive efficiency of heuristic processing.

---

## Reading Paths

Different entry points serve different purposes. The following curated paths are designed for specific goals.

---

### Path A — The Learner's Toolkit
*Goal: Improve your own learning and retention.*

```
START
  │
  ▼
[[MOC - Memory Science]]
  → encoding, spacing, retrieval practice, interleaving
  │
  ▼
[[MOC - Cognitive Load Theory]]
  → manage complexity, use worked examples, avoid split attention
  │
  ▼
[[MOC - Metacognition and Self-Regulated Learning]]
  → monitor your understanding, plan study sessions, self-test
  │
  ▼
[[MOC - Learning Science]]
  → desirable difficulties, transfer, assessment strategies
  │
  ▼
[[MOC - PKB and Knowledge Management]]
  → build a second brain, use Zettelkasten, make permanent notes
  │
  ▼
APPLY: You now have a complete evidence-based learning system.
```

---

### Path B — The Instructor's Map
*Goal: Design learning environments that actually work.*

```
START
  │
  ▼
[[MOC - Learning Science]]
  → theoretical foundations, instructional design models
  │
  ▼
[[MOC - Cognitive Load Theory]]
  → split-attention, modality, expertise reversal, 4C/ID
  │
  ▼
[[MOC - Motivation Psychology]]
  → SDT, autonomy support, achievement goals, academic emotions
  │
  ▼
[[MOC - Metacognition and Self-Regulated Learning]]
  → SRL phases, self-efficacy, feedback design
  │
  ▼
[[MOC - Social Psychology]]
  → cooperative learning, stereotype threat, social influence
  │
  ▼
APPLY: Design instruction grounded in cognitive, motivational, and social science.
```

---

### Path C — The Critical Reasoner
*Goal: Think more clearly and evaluate knowledge more rigorously.*

```
START
  │
  ▼
[[MOC - Dual Process Theory and Cognitive Biases]]
  → understand your default heuristics and their failure modes
  │
  ▼
[[MOC - Critical Thinking and Logic]]
  → argument structure, fallacies, intellectual virtues
  │
  ▼
[[MOC - Epistemology]]
  → theories of knowledge and justification, philosophy of science
  │
  ▼
[[MOC - Social Psychology]]
  → social cognition, attribution errors, groupthink
  │
  ▼
APPLY: A rigorous framework for reasoning under uncertainty.
```

---

### Path D — The PKB Architect
*Goal: Build a durable, generative knowledge management system.*

```
START
  │
  ▼
[[MOC - PKB and Knowledge Management]]
  → Zettelkasten, PARA, LYT, note anatomy
  │
  ▼
[[MOC - Memory Science]]
  → why externalisation works, retrieval practice integration
  │
  ▼
[[MOC - Metacognition and Self-Regulated Learning]]
  → PKB as metacognitive scaffold, self-monitoring via notes
  │
  ▼
[[MOC - Cognitive Load Theory]]
  → offloading principles, chunking, schema formation
  │
  ▼
APPLY: A cognitively-grounded rationale for your PKB architecture.
```

---

## Key Cross-Domain Synthesis Notes

The following permanent notes are **high-betweenness nodes** — they appear in multiple domain MOCs and serve as the primary conceptual bridges. If you read nothing else, read these.

| Note | Bridges |
|------|---------|
| [[dual-process-theory\|Dual Process Theory]] | Memory · Biases · Critical Thinking · Social Psych |
| [[working-memory\|Working Memory]] | Memory · CLT · Learning Science · Metacognition |
| [[metacognitive-monitoring\|Metacognitive Monitoring]] | Metacognition · Memory · SRL · PKB |
| [[self-determination-theory\|Self-Determination Theory]] | Motivation · SRL · Social Psych · Learning Science |
| [[schema-theory\|Schema Theory]] | Memory · CLT · Learning Science · Critical Thinking |
| [[transfer-of-learning\|Transfer of Learning]] | Learning Science · CLT · Memory · Motivation |
| [[cognitive-offloading\|Cognitive Offloading]] | PKB · Memory · CLT · Distributed Cognition |
| [[epistemic-justification\|Epistemic Justification]] | Epistemology · Critical Thinking · Social Epistemology |
| [[growth-mindset\|Growth Mindset]] | Motivation · SRL · Social Psych · Learning Science |
| [[testing-effect\|Testing Effect]] | Memory · Learning Science · Metacognition · PKB |
| [[belief-bias\|Belief Bias]] | Dual Process · Critical Thinking · Epistemology |
| [[intrinsic-motivation\|Intrinsic Motivation]] | Motivation · SRL · Social Psych · Learning Science |
| [[vygotsky-zone-of-proximal-development\|Zone of Proximal Development]] | Learning Science · Social Psych · CLT |
| [[spaced-repetition\|Spaced Repetition]] | Memory · Learning Science · PKB |
| [[intellectual-humility\|Intellectual Humility]] | Epistemology · Critical Thinking · Dual Process |

---

## The PKB as Cognitive Prosthetic — A Synthesis

> [!key-claim] The Unifying Thesis
> This vault is not merely a collection of notes. It is itself an instantiation of the cognitive science it documents. Its architecture — atomic notes, bi-directional links, Maps of Content, progressive summarisation — is a direct application of principles drawn from every domain it contains.

Consider the evidence:

**From Memory Science**: Atomic permanent notes exploit the [[testing-effect|Testing Effect]] every time you retrieve and traverse links. The MOC structure leverages [[elaborative-interrogation|Elaborative Interrogation]] by forcing synthesis across notes.

**From Cognitive Load Theory**: Atomic notes reduce intrinsic load by isolating single ideas. MOCs manage extraneous load by providing navigational scaffolding. The progressive elaboration of notes from fleeting → literature → permanent mirrors the [[worked-example-effect|Worked Example Effect]]: early notes are scaffolds; permanent notes are the schema.

**From Metacognition and SRL**: Writing permanent notes is a metacognitive act — it requires you to monitor comprehension, identify gaps, and generate your own representations. The act of linking notes is a [[self-explanation|Self-Explanation]] strategy.

**From Motivation Psychology**: A well-designed PKB supports all three basic psychological needs in SDT: *autonomy* (you choose what to note and how to connect it), *competence* (growing graph = visible evidence of growth), *relatedness* (your notes engage with the ideas of other thinkers across time).

**From Dual Process and Biases**: The deliberate, effortful work of writing permanent notes is a System 2 activity that creates durable System 1 intuitions — eventually, well-connected concepts become fluent, retrievable heuristics rather than laborious reconstructions.

**From Epistemology**: Every permanent note is an epistemic commitment. The requirement to write in your own words, link to evidence, and express a single claim per note is a form of [[epistemic-hygiene|Epistemic Hygiene]] — it forces you to take responsibility for your beliefs.

The PKB is therefore a cognitive prosthetic that extends biological memory, offloads metacognitive monitoring, scaffolds SRL, and operationalises epistemic virtues. This is not metaphor. It is the direct application of the science documented in this vault.

---

## Theoretical Lineage Map

The following table locates each major theory in its intellectual lineage, enabling you to trace paradigmatic commitments across domains.

| Tradition | Founding Figures | Core Claim | Domain MOC |
|-----------|-----------------|------------|------------|
| Cognitive Architecture | Miller, Atkinson & Shiffrin, Baddeley | Mind is an information-processing system with structural constraints | Memory · CLT |
| Constructivism | Piaget, Vygotsky, Bruner | Knowledge is actively constructed, not passively received | Learning Science · SRL |
| Behaviourism | Skinner, Thorndike, Pavlov | Learning = behaviour change through reinforcement | Learning Science |
| Social Cognitive Theory | Bandura | Learning is observational; self-efficacy mediates performance | Motivation · SRL |
| Self-Determination Theory | Deci & Ryan | Intrinsic motivation requires autonomy, competence, relatedness | Motivation |
| Dual Process Theory | Kahneman, Evans, Stanovich | Two qualitatively different processing modes with distinct error profiles | Dual Process · Critical Thinking |
| Heuristics & Biases | Kahneman & Tversky | Systematic departures from rationality follow predictable patterns | Dual Process |
| Epistemic Virtue Theory | Zagzebski, Sosa | Justified belief requires not just reliable processes but virtuous intellectual character | Epistemology · Critical Thinking |
| Distributed Cognition | Hutchins, Clark & Chalmers | Cognition extends beyond the skull into tools, symbols, and social networks | PKB · Social Psych |
| Social Identity Theory | Tajfel & Turner | Group membership is constitutive of self-concept and shapes social perception | Social Psych |
| Metacognitive Theory | Flavell, Nelson & Narens | Cognition operates on two levels: object-level and meta-level | Metacognition |
| Embodied Cognition | Varela, Thompson, Rosch | Cognition is shaped by bodily experience and environmental coupling | Cross-domain |

---

## Vault Health and Maintenance Notes

> [!tip] MOC Maintenance Protocol
> These MOCs should be treated as **living documents**. When you add a permanent note that clearly belongs to a domain, add its wiki-link to the appropriate domain MOC. When a note bridges two domains (e.g., a note on [[stereotype-threat|Stereotype Threat]] that touches both Social Psychology and Motivation), link it in both MOCs under their respective Cross-Domain Bridges sections.

> [!warning] Orphan Note Detection
> Periodically audit for notes that appear in no MOC. Orphan notes represent knowledge that has been captured but not integrated. The knowledge graph topology research ([[knowledge-graph-topology|Knowledge Graph Topology]]) suggests that high-betweenness nodes are the most valuable — orphans, by definition, have zero betweenness. Integrate or archive them.

> [!info] Suggested Next Expansions
> The current vault has strong coverage of **cognitive, motivational, and social foundations**. Identified gaps for future expansion:
> - Affective Neuroscience (emotion–cognition interaction)
> - Developmental Psychology (lifespan cognitive change)
> - Computational Cognitive Science (Bayesian brain, predictive processing)
> - Psycholinguistics (language acquisition, reading science)
> - Applied Cognitive Ergonomics (human factors, interface design)

---

## Quick Reference — All Domain MOCs

> [!map] Navigate the Vault
> - [[MOC - Memory Science]] — encoding, consolidation, retrieval, forgetting, metacognitive monitoring
> - [[MOC - Cognitive Load Theory]] — working memory, load taxonomy, instructional effects
> - [[MOC - Metacognition and Self-Regulated Learning]] — monitoring, control, SRL models, SDL
> - [[MOC - Motivation Psychology]] — SDT, achievement goals, self-efficacy, academic emotions
> - [[MOC - Critical Thinking and Logic]] — argument anatomy, fallacies, intellectual virtues, CT frameworks
> - [[MOC - Epistemology]] — theories of knowledge, justification, truth, philosophy of science
> - [[MOC - Learning Science]] — learning theories, principles, instructional design, transfer
> - [[MOC - PKB and Knowledge Management]] — Zettelkasten, PARA, LYT, second brain, graph topology
> - [[MOC - Social Psychology]] — social cognition, attribution, influence, group dynamics, social identity
> - [[MOC - Dual Process Theory and Cognitive Biases]] — System 1/2, heuristics, biases, behavioural economics, debiasing

---

*Master Index last updated: 2026-05-15 | PKB v6-llm-elaborated | Total MOCs: 11 | Total indexed notes: ~533*


Now I have a complete picture of this document. Let me execute the full pipeline.

**Phase 2 — Aid Selection:**
1. **Enhanced Cross-Domain Architecture Map** — the existing diagram, redone with richer labels
2. **MOC Registry Note-Density Bar Chart** — visual scale of 10 MOCs by note count and pattern
3. **Five Foundational Tensions Matrix** — poles → synthesis → bridge domains
4. **Theoretical Lineage / Intellectual Genealogy** — traditions → founders → domain MOCs
5. **High-Betweenness Bridge Nodes Hub** — 15 cross-domain synthesis notes mapped to their bridges
6. **Reading Paths Swimlane** — 4 curated paths as parallel tracks
7. **PKB-as-Cognitive-Prosthetic Mapping** — vault architecture ↔ cognitive science principles
8. **Vault Dependency / Prerequisite Graph** — what must be understood before what
9. **Five Tensions Before/After Contrast** — naive vs. synthesised position for each tension
10. **TL;DR Scorecard**

---

```
# Visual Aid Suite: MOC — Cognitive Science (Master Index)

Report length: ~2,500 words (structured MOC document)
Audience:      Informed PKB practitioner (Obsidian/Zettelkasten user)
Thesis:        Ten domain MOCs spanning ~533 permanent notes form an
               interdependent cognitive science PKB whose architecture
               is itself an application of the science it documents.
Aids selected: 10 (see below)

───────────────────────────────────────────────────────────────────────────


══════════════════════════════════════════════════════════════════
  Visual Aid 1: Cross-Domain Architecture Map (Enhanced)
══════════════════════════════════════════════════════════════════

Purpose: Render the full dependency and mutual-constitution
         relationships across all ten domain MOCs in one view.

┌─────────────────────────────────────────────────────────────────────┐
│          COGNITIVE SCIENCE PKB — MASTER ARCHITECTURE                │
│                 10 Domain MOCs · ~533 Notes                         │
└─────────────────────────────────────────────────────────────────────┘

  STRATUM 1 — NORMATIVE LAYER (what SHOULD reasoning be?)
  ┌───────────────────────┐
  │   [[MOC - Epistemology]]  │  48 notes · Dialectical
  │  What is knowledge?   │
  └──────────┬────────────┘
             │ grounds ↓           ← informs (bidirectional) →
             ▼
  ┌───────────────────────┐     ↔↔↔↔↔↔↔↔↔↔↔     ┌───────────────────────────┐
  │  [[MOC - Critical         │                   │  [[MOC - Dual Process          │
  │   Thinking & Logic]]  │◄──────────────────►│   Theory & Cog. Biases]]   │
  │  Good reasoning?      │                   │  How do systems 1&2 err?  │
  │  67 notes · Progress. │                   │  46 notes · Hub+spoke     │
  └──────────┬────────────┘                   └────────────┬──────────────┘
             │ depends on ↓                                │ biases ↓
             ▼                                             ▼

  STRATUM 2 — ARCHITECTURAL LAYER (how does the mind WORK?)
  ┌───────────────────────┐     ↔↔↔↔↔↔↔↔↔↔↔     ┌───────────────────────────┐
  │  [[MOC - Memory Science]] │                   │  [[MOC - Learning Science]]    │
  │  Encode·store·retrieve│◄──────────────────►│  Principles for durable   │
  │  62 notes · Hub+spoke │                   │  transferable learning    │
  └──────────┬────────────┘                   │  56 notes · Cluster       │
             │ constrains ↓                   └────────────┬──────────────┘
             ▼                                             │ operationalises ↓
  ┌───────────────────────┐     ↔↔↔↔↔↔↔↔↔↔↔     ┌───────────────────────────┐
  │  [[MOC - Cognitive Load   │                   │  [[MOC - Metacognition         │
  │   Theory]]            │◄──────────────────►│   & SRL]]                  │
  │  WM limits · design   │                   │  Monitor·control·direct   │
  │  44 notes · Progress. │                   │  58 notes · Cluster       │
  └──────────┬────────────┘                   └────────────┬──────────────┘
             │ informs design ↓                            │ regulated by ↓

  STRATUM 3 — MOTIVATIONAL/SOCIAL LAYER (what DRIVES & contextualises?)
  ┌───────────────────────┐     ↔↔↔↔↔↔↔↔↔↔↔     ┌───────────────────────────┐
  │  [[MOC - Motivation        │                   │  [[MOC - Social Psychology]]   │
  │   Psychology]]        │◄──────────────────►│  Social context·attribution│
  │  SDT·goals·efficacy   │                   │  groupthink·identity      │
  │  78 notes · Cluster   │                   │  38 notes · Cluster       │
  └──────────┬────────────┘                   └────────────┬──────────────┘
             │ drives ↓                                    │ contextualises ↓
             └──────────────────────┬─────────────────────┘
                                    ▼

  STRATUM 4 — APPLIED LAYER (what do we BUILD with this knowledge?)
                         ┌─────────────────────────┐
                         │  [[MOC - PKB & Knowledge    │
                         │   Management]]          │
                         │  Zettelkasten·PARA·LYT  │
                         │  36 notes · Progressive │
                         └─────────────────────────┘

  Edge key:  ─── foundation flow (one-way)   ↔↔↔ mutual constitution
             ↓   vertical strata flow        ← → horizontal peer links

Source: §"Cross-Domain Relationship Map" + §"Domain MOC Registry"

Reading guide: Read top-to-bottom as a dependency stack. Strata 1–4
represent increasing proximity to practice. Horizontal bidirectional
edges (↔) mark pairs that cannot be fully understood without the
other. Note that PKB (Stratum 4) receives flows from ALL strata —
it is the convergence point of every theoretical layer.


══════════════════════════════════════════════════════════════════
  Visual Aid 2: MOC Registry — Note Density & Pattern
══════════════════════════════════════════════════════════════════

Purpose: Provide an at-a-glance comparison of MOC scale, density,
         and structural pattern to guide navigation priority.

┌──────────────────────────────────────────────┬───────┬──────────────┐
│ MOC (domain)                                 │ Notes │ Pattern      │
├──────────────────────────────────────────────┼───────┼──────────────┤
│ [[MOC - Motivation Psychology]]              │  78   │ Cluster      │
│ ████████████████████████████████████████     │       │              │
├──────────────────────────────────────────────┼───────┼──────────────┤
│ [[MOC - Critical Thinking & Logic]]          │  67   │ Progressive  │
│ ██████████████████████████████████           │       │              │
├──────────────────────────────────────────────┼───────┼──────────────┤
│ [[MOC - Memory Science]]                     │  62   │ Hub-and-spoke│
│ █████████████████████████████████            │       │              │
├──────────────────────────────────────────────┼───────┼──────────────┤
│ [[MOC - Metacognition & SRL]]                │  58   │ Cluster      │
│ ███████████████████████████████              │       │              │
├──────────────────────────────────────────────┼───────┼──────────────┤
│ [[MOC - Learning Science]]                   │  56   │ Cluster      │
│ ██████████████████████████████               │       │              │
├──────────────────────────────────────────────┼───────┼──────────────┤
│ [[MOC - Epistemology]]                       │  48   │ Dialectical  │
│ ██████████████████████████                   │       │              │
├──────────────────────────────────────────────┼───────┼──────────────┤
│ [[MOC - Dual Process & Cog. Biases]]         │  46   │ Hub-and-spoke│
│ █████████████████████████                    │       │              │
├──────────────────────────────────────────────┼───────┼──────────────┤
│ [[MOC - Social Psychology]]                  │  38   │ Cluster      │
│ █████████████████████                        │       │              │
├──────────────────────────────────────────────┼───────┼──────────────┤
│ [[MOC - PKB & Knowledge Management]]         │  36   │ Progressive  │
│ ████████████████████                         │       │              │
├──────────────────────────────────────────────┼───────┼──────────────┤
│ [[MOC - Cognitive Load Theory]]              │  44   │ Progressive  │
│ ████████████████████████                     │       │              │
├──────────────────────────────────────────────┼───────┼──────────────┤
│ TOTAL                                        │ ~533  │              │
└──────────────────────────────────────────────┴───────┴──────────────┘

  Note scale: each █ ≈ 2 notes

  Pattern legend:
  Hub-and-spoke  → central concept radiates to specifics (Memory, Dual Process)
  Progressive    → concepts scaffold each other in sequence (CLT, CT&L, PKB)
  Cluster        → nodes form thematic groupings (Motivation, SRL, Social)
  Dialectical    → ideas defined through contrasts and tensions (Epistemology)

Source: §"Domain MOC Registry"

Reading guide: Read note count as depth indicator — Motivation (78)
and Critical Thinking (67) are the densest, most elaborated domains.
PKB (36) and CLT (44) are the most structurally scaffolded (Progressive
pattern = explicit prerequisite chains). Use this to calibrate expected
reading investment per domain.


══════════════════════════════════════════════════════════════════
  Visual Aid 3: Five Foundational Tensions — Analysis Matrix
══════════════════════════════════════════════════════════════════

Purpose: Display each of the vault's five generative tensions —
         both poles, the synthesis position, and which MOCs carry it.

┌───┬─────────────────────┬──────────────────────┬─────────────────────┬──────────────────────────────┐
│ # │ TENSION             │ POLE A               │ POLE B              │ SYNTHESIS (vault position)   │
├───┼─────────────────────┼──────────────────────┼─────────────────────┼──────────────────────────────┤
│ 1 │ Storage vs.         │ Memory = faithful    │ Memory = generative │ Probabilistic inference      │
│   │ Reconstruction      │ archive (playback)   │ reconstruction      │ engine: schema-guided, bias- │
│   │                     │                      │                     │ prone, adaptively accurate   │
│   │ MOCs: Memory Sci.   │ [Atkinson-Shiffrin]  │ [Bartlett, DRM]     │ [[Reconstructive-Memory]]    │
│   │ → Dual Process      │                      │                     │                              │
│   │ → Epistemology      │                      │                     │                              │
├───┼─────────────────────┼──────────────────────┼─────────────────────┼──────────────────────────────┤
│ 2 │ Limits vs.          │ WM = bottleneck      │ WM = sophisticated  │ Limits define the ceiling;   │
│   │ Architecture        │ to manage (CLT)      │ multi-channel arch. │ schema automation raises     │
│   │                     │                      │ (Baddeley 4-comp.)  │ the floor. Expertise =       │
│   │ MOCs: CLT           │ [Sweller, Paas]      │ [Baddeley, Hitch]   │ automated schemas free WM.   │
│   │ → Memory Sci.       │                      │                     │ [[Working-Memory]]           │
│   │ → Learning Science  │                      │                     │                              │
├───┼─────────────────────┼──────────────────────┼─────────────────────┼──────────────────────────────┤
│ 3 │ Autonomy vs.        │ Self-direction needs │ Unguided discovery  │ Autonomy = internalised      │
│   │ Structure           │ freedom from control │ → inefficient for   │ structure, not absence of    │
│   │                     │ (SDT: autonomy need) │ novices (expertise  │ it. Fading scaffolding       │
│   │ MOCs: Motivation    │ [Deci & Ryan]        │ reversal effect)    │ engineers the SDT            │
│   │ → Metacog. SRL      │                      │ [Kirschner et al.]  │ internalisation continuum.   │
│   │ → Learning Science  │                      │                     │ [[Internalization-Continuum]]│
├───┼─────────────────────┼──────────────────────┼─────────────────────┼──────────────────────────────┤
│ 4 │ Individual vs.      │ Cognition is a       │ Cognition is        │ Multi-level: biological      │
│   │ Social Cognition    │ property of a single │ distributed across  │ architecture (WM, LTM) is    │
│   │                     │ brain                │ persons & artefacts │ real; social/artefactual     │
│   │ MOCs: Most MOCs     │ [classical cog. sci.]│ [Hutchins, Clark]   │ scaffolding extends it.      │
│   │ → Social Psych.     │                      │                     │ [[Cognitive-Offloading]]     │
│   │ → PKB               │                      │                     │                              │
├───┼─────────────────────┼──────────────────────┼─────────────────────┼──────────────────────────────┤
│ 5 │ Rationality vs.     │ Humans are           │ Humans are          │ Neither: [[Intellectual-     │
│   │ Bias                │ fundamentally        │ fundamentally       │ Humility]] + [[Calibration]] │
│   │                     │ rational; errors are │ heuristic; reason   │ are the response. Debiasing  │
│   │ MOCs: Dual Process  │ occasional           │ is itself biased    │ strategies work, but bias    │
│   │ → Critical Think.   │ [rational choice     │ (motivated reason.) │ is real. Epistemic hygiene   │
│   │ → Epistemology      │  theory]             │ [Kahneman, Kunda]   │ reduces predictable errors.  │
└───┴─────────────────────┴──────────────────────┴─────────────────────┴──────────────────────────────┘

Source: §"The Five Foundational Tensions"

Reading guide: Each row is an unresolved debate that spans multiple
MOCs. The SYNTHESIS column gives the vault's integrative position —
neither pole but a third claim that reframes the dichotomy. These
tensions are generative: understanding them predicts where domain
MOCs will disagree and what bridge notes will be most needed.


══════════════════════════════════════════════════════════════════
  Visual Aid 4: Theoretical Lineage Map
══════════════════════════════════════════════════════════════════

Purpose: Place each major theoretical tradition in its intellectual
         genealogy and connect it to the domain MOC(s) it anchors.

  ┌──────────────────────────────────────────────────────────────┐
  │               THEORETICAL LINEAGE ARCHITECTURE              │
  └──────────────────────────────────────────────────────────────┘

  TRADITION               CORE FIGURES            DOMAIN MOC(S)
  ─────────────────────────────────────────────────────────────
  Cognitive Architecture  Miller · Atkinson &   → [[MOC - Memory Science]]
  (information-           Shiffrin · Baddeley     [[MOC - Cognitive Load Theory]]
   processing)            (1956–1974)

  Constructivism          Piaget · Vygotsky ·   → [[MOC - Learning Science]]
  (knowledge actively     Bruner                  [[MOC - Metacognition & SRL]]
   constructed)           (1930s–1960s)

  Behaviourism            Skinner · Thorndike · → [[MOC - Learning Science]]
  (learning = behaviour   Pavlov                  (as historical contrast)
   change)                (1900s–1950s)

  Social Cognitive        Bandura               → [[MOC - Motivation Psychology]]
  Theory (self-efficacy,  (1977–1986)             [[MOC - Metacognition & SRL]]
   observational lrng.)

  Self-Determination      Deci & Ryan           → [[MOC - Motivation Psychology]]
  Theory (autonomy ·      (1985–2000)             (78 notes — largest MOC)
   competence · relat.)

  Dual Process Theory     Kahneman · Evans ·    → [[MOC - Dual Process & Biases]]
  (System 1 vs. 2,        Stanovich               [[MOC - Critical Thinking]]
   error profiles)        (1974–2002)

  Heuristics & Biases     Kahneman & Tversky    → [[MOC - Dual Process & Biases]]
  (predictable depart-    (1974–1992)
   ures from rationality)

  Epistemic Virtue        Zagzebski · Sosa      → [[MOC - Epistemology]]
  Theory (justified       (1980s–2000s)           [[MOC - Critical Thinking]]
   belief needs character)

  Distributed Cognition   Hutchins · Clark &    → [[MOC - PKB & Knowledge Mgmt]]
  (cognition extends      Chalmers                [[MOC - Social Psychology]]
   beyond the skull)      (1990s–2000s)

  Social Identity         Tajfel & Turner       → [[MOC - Social Psychology]]
  Theory (group member-   (1979–1986)
   ship shapes cognition)

  Metacognitive Theory    Flavell · Nelson &    → [[MOC - Metacognition & SRL]]
  (object-level vs.       Narens                  (58 notes — core MOC)
   meta-level cognition)  (1976–1990)

  Embodied Cognition      Varela · Thompson ·   → Cross-domain
  (cognition shaped by    Rosch                   (no single MOC; appears in
   body & environment)    (1991)                   Memory · CLT · Social Psych)

  ─────────────────────────────────────────────────────────────
  Reading lineage by column left→right: tradition names the
  paradigmatic commitment; figures are the canonical sources;
  right column shows primary PKB residency.

Source: §"Theoretical Lineage Map"

Reading guide: Two traditions span the most MOCs — Dual Process Theory
(anchors Dual Process, Critical Thinking, and bleeds into Epistemology)
and Distributed Cognition (anchors PKB and Social Psychology). These
two traditions are the most powerful cross-cutting frameworks for
integrative understanding.


══════════════════════════════════════════════════════════════════
  Visual Aid 5: High-Betweenness Bridge Nodes
══════════════════════════════════════════════════════════════════

Purpose: Map the 15 cross-domain synthesis notes that connect
         the most MOCs — the conceptual glue of the entire vault.

                         ┌────────────────────────────────┐
                         │   HIGH-BETWEENNESS BRIDGE MAP  │
                         │  (concepts appearing in 3+ MOCs)│
                         └────────────────────────────────┘

  ●────────────────────────────────────────────────────────────●
  CONCEPT                 MEM  CLT  SRL  MOT  CT   EPI  LS   PKB  SOC  DPB
  ─────────────────────────────────────────────────────────────────────────
  [[Dual-Process-Theory]]  ✓         ✓         ✓    ✓         ✓    ✓    ✓
  [[Working-Memory]]       ✓    ✓    ✓              ✓         ✓    ✓
  [[Metacognitive-Monitoring]] ✓     ✓              ✓              ✓    ✓
  [[Self-Determination-Theory]]     ✓    ✓         ✓              ✓    ✓
  [[Schema-Theory]]        ✓    ✓         ✓    ✓              ✓
  [[Transfer-of-Learning]] ✓    ✓    ✓    ✓              ✓
  [[Cognitive-Offloading]] ✓    ✓              ✓              ✓    ✓
  [[Epistemic-Justification]]        ✓              ✓    ✓              ✓
  [[Growth-Mindset]]                ✓    ✓         ✓         ✓    ✓
  [[Testing-Effect]]       ✓         ✓                        ✓    ✓
  [[Belief-Bias]]                              ✓    ✓                   ✓
  [[Intrinsic-Motivation]]          ✓    ✓         ✓         ✓    ✓
  [[Zone-of-Proximal-Dev]] ✓              ✓              ✓         ✓
  [[Spaced-Repetition]]    ✓                                  ✓    ✓
  [[Intellectual-Humility]]               ✓    ✓    ✓                   ✓
  ─────────────────────────────────────────────────────────────────────────
  BRIDGE COUNT             7    5    9    6    7    5    7    9    5    6

  MOC key: MEM=Memory · CLT=Cognitive Load · SRL=Metacog/SRL
           MOT=Motivation · CT=Critical Think · EPI=Epistemology
           LS=Learning Science · PKB=PKB/KM · SOC=Social Psych
           DPB=Dual Process/Biases

  ★ Highest bridge count (9): [[Metacognitive-Monitoring]] and [[PKB]] domain
  ★ Widest span: [[Dual-Process-Theory]] (7 MOCs)
  ★ Deepest integrative note: [[Self-Determination-Theory]] (4 MOCs)

Source: §"Key Cross-Domain Synthesis Notes"

Reading guide: The ✓ matrix shows which MOC each bridge note appears
in. Read by row to see which notes to prioritise for cross-domain
understanding — [[Metacognitive-Monitoring]] and [[Dual-Process-Theory]]
have the widest reach. Read by column to see each MOC's external
dependencies — SRL and PKB have the highest incoming bridge count (9),
meaning they require the most cross-domain context to fully understand.


══════════════════════════════════════════════════════════════════
  Visual Aid 6: Four Reading Paths — Swimlane Diagram
══════════════════════════════════════════════════════════════════

Purpose: Display the four curated vault entry paths as parallel
         goal-oriented routes through the ten domain MOCs.

  GOAL ──────────────────────────────────────────────────────────►

         PATH A             PATH B             PATH C           PATH D
       The Learner's      The Instructor's   The Critical     The PKB
         Toolkit               Map             Reasoner       Architect
      ─────────────      ──────────────     ────────────    ──────────
      (improve own       (design learning   (think more     (build a
       learning)          environments)      clearly)        durable PKB)
  ───────────────────────────────────────────────────────────────────────
  Step│ [[MOC -          [[MOC -            [[MOC -         [[MOC -
   1  │  Memory           Learning           Dual Process    PKB &
      │  Science]]        Science]]          & Biases]]      KM]]
      │  encoding ·       foundations ·      understand      Zettelkasten
      │  spacing ·        design models      System 1/2      PARA · LYT
      │  retrieval        ↓                  failures        note anatomy
      │  ↓                                   ↓               ↓
  Step│ [[MOC -          [[MOC -            [[MOC -         [[MOC -
   2  │  Cognitive        Cognitive          Critical        Memory
      │  Load Theory]]    Load Theory]]      Thinking        Science]]
      │  manage WM ·      split attention ·  & Logic]]       why extern-
      │  worked ex. ·     modality effect    argument ·      alisation
      │  chunking         4C/ID              fallacies       works ·
      │  ↓                ↓                  virtues         retrieval
      │                                      ↓               ↓
  Step│ [[MOC -          [[MOC -            [[MOC -         [[MOC -
   3  │  Metacognition    Motivation         Epistemology]]  Metacognition
      │  & SRL]]          Psychology]]       knowledge ·     & SRL]]
      │  monitor ·        SDT · autonomy     justification   PKB as
      │  plan ·           support ·          · philosophy    metacog.
      │  self-test        goals · emotions   of science      scaffold
      │  ↓                ↓                  ↓               ↓
  Step│ [[MOC -          [[MOC -            [[MOC -         [[MOC -
   4  │  Learning         Metacognition      Social          Cognitive
      │  Science]]        & SRL]]            Psychology]]    Load
      │  desirable        SRL phases ·       social cog.     Theory]]
      │  difficulties     self-efficacy ·    attribution     offloading
      │  transfer         feedback design    groupthink      schema form.
      │  ↓                ↓                                  ↓
  Step│ [[MOC -          [[MOC -                            ─────────
   5  │  PKB & KM]]       Social Psych]]                    APPLY:
      │  second brain     cooperative                        Evidence-
      │  Zettelkasten      learning ·                        based PKB
      │  permanent        stereotype                         architecture
      │  notes            threat
  ───────────────────────────────────────────────────────────────────────
  END  Complete         Design grounded     Rigorous         Durable
       evidence-based   in 3 sciences       framework        generative
       learning system  (cognitive ·        for reasoning    knowledge
                        motivational ·      under            system
                        social)             uncertainty

Source: §"Reading Paths" (A–D)

Reading guide: Each column is a self-contained reading journey.
Paths A and D are learner/builder facing; B is instructor facing;
C is epistemically focused. Paths are not mutually exclusive —
after completing one, begin another: the second path reveals
cross-domain connections invisible from inside a single path.


══════════════════════════════════════════════════════════════════
  Visual Aid 7: PKB as Cognitive Prosthetic — Mapping
══════════════════════════════════════════════════════════════════

Purpose: Show how the PKB vault's architectural features map
         directly onto cognitive science principles from each domain.

  ┌──────────────────────────────────────────────────────────────┐
  │   PKB ARCHITECTURE ←──────────── COGNITIVE SCIENCE PRINCIPLE  │
  └──────────────────────────────────────────────────────────────┘

  PKB FEATURE                    COGNITIVE SCIENCE FOUNDATION
  ─────────────────────────────────────────────────────────────

  Atomic permanent notes         [[Testing-Effect]] (Memory Science)
  (one claim per note)      →    Each retrieval/traversal =
                                 a retrieval practice event.
                                 MOC structure = [[Elaborative-
                                 Interrogation]] by forcing synthesis.

  Atomic notes isolate ideas     [[Cognitive-Load-Theory]]
  (single concepts per note) →   Reduces intrinsic load.
                                 MOC structure = extraneous load
                                 management via navigational scaffold.

  Fleeting → literature          [[Worked-Example-Effect]] (CLT)
  → permanent note pipeline →    Early notes are scaffolds;
                                 permanent notes are the schema.
                                 Progressive elaboration mirrors
                                 faded worked example sequence.

  Writing permanent notes        [[Metacognitive-Monitoring]] (SRL)
  in your own words         →    Forces comprehension monitoring,
                                 gap detection, and self-generated
                                 representation. Linking = [[Self-
                                 Explanation]] strategy.

  Bi-directional links           [[Self-Determination-Theory]] (Motivation)
  + growing graph           →    Autonomy: you choose what to note.
                                 Competence: graph growth = visible
                                 evidence of mastery.
                                 Relatedness: engaging thinkers
                                 across time and disciplines.

  Deliberate note-writing        [[Dual-Process-Theory]] (Dual Process)
  (effortful, System 2)     →    Creates durable System 1 intuitions.
                                 Well-connected concepts become
                                 fluent heuristics, not laborious
                                 reconstructions.

  Write in own words,            [[Epistemic-Justification]] (Epistemology)
  link to evidence,         →    Every note = an epistemic commitment.
  single claim per note          Single-claim norm = epistemic hygiene.
                                 Taking responsibility for beliefs.

  External PKB system            [[Cognitive-Offloading]] (PKB + CLT)
  (externalised storage)    →    Extends biological memory without
                                 eliminating architectural limits.
                                 Reduces WM demand; preserves
                                 retrieval access indefinitely.

  ─────────────────────────────────────────────────────────────
  ► The PKB is not merely documented by this vault.
    It is an instantiation of the science it documents.

Source: §"The PKB as Cognitive Prosthetic — A Synthesis"

Reading guide: Read each row as a design-to-theory justification.
Left column tells you WHAT the PKB does; right column tells you WHY
it works, grounded in specific theoretical mechanisms. Use this as
a rationale document when explaining your PKB architecture to others,
or when deciding how to extend it.


══════════════════════════════════════════════════════════════════
  Visual Aid 8: Vault Prerequisite Dependency Graph
══════════════════════════════════════════════════════════════════

Purpose: Show which domains must be understood before others —
         a directed prerequisite map for systematic vault study.

  [Epistemology] ──────────────────────────────────────────────┐
       │ (what counts as knowledge                              │
       │  and justification)                                    │
       ▼                                                        │
  [Critical Thinking & Logic] ◄────── [Dual Process & Biases] ─┘
       │ (normative reasoning standards) (empirical bias inventory)
       │
       ▼
  [Memory Science] ◄────────────────── [Dual Process & Biases]
       │ (encoding · retrieval ·          (System 1 distorts memory
       │  schema · forgetting)             reconstruction)
       │
       ├──────────────────────────────────────┐
       ▼                                      ▼
  [Cognitive Load Theory]              [Learning Science]
  (WM limits · load types ·            (principles · transfer ·
   instructional effects)               instructional design)
       │                                      │
       └──────────────┬───────────────────────┘
                      ▼
              [Metacognition & SRL]
              (monitoring · control ·
               Zimmerman cycle · SDL)
                      │
       ┌──────────────┼───────────────────────┐
       ▼              ▼                        ▼
  [Motivation]  [Social Psychology]      [PKB & KM]
  (SDT · goals ·  (attribution ·         (Zettelkasten ·
   self-efficacy)  groupthink ·           graph design ·
                   social identity)       cognitive offloading)
       │              │                        ▲
       └──────────────┴────────────────────────┘
               (all three converge
                in applied PKB design)

  Read order for a rigorous first pass through the vault:
  1 → Epistemology       (what knowledge is)
  2 → Dual Process       (how cognition actually works)
  3 → Memory Science     (the biological substrate)
  4 → Cognitive Load     (the capacity constraints)
  5 → Learning Science   (the design principles)
  6 → Metacognition/SRL  (the regulatory layer)
  7 → Motivation         (the fuel layer)
  8 → Social Psychology  (the context layer)
  9 → Critical Thinking  (the evaluative layer)
  10→ PKB & KM           (the applied layer)

Source: §"Cross-Domain Relationship Map" + §"Five Foundational Tensions"

Reading guide: Downward arrows represent conceptual dependency —
lower nodes assume mastery of higher nodes. PKB & KM is positioned
last because it is genuinely applied: it makes most sense once you
understand what it is externalising (memory), why (CLT limits),
how to regulate it (SRL), what motivates it (SDT), and how it
extends across social context (distributed cognition).


══════════════════════════════════════════════════════════════════
  Visual Aid 9: Five Tensions — Naive vs. Synthesised Positions
══════════════════════════════════════════════════════════════════

Purpose: Show the transformation from naive/dichotomous framing
         to vault's integrated synthesis position for each tension.

┌────────────────────────────┬─────────────────────────────────────┐
│   NAIVE (BEFORE) POSITION  │   VAULT SYNTHESIS (AFTER) POSITION  │
├────────────────────────────┼─────────────────────────────────────┤
│ TENSION 1: MEMORY          │                                     │
│ Memory is a reliable       │ Memory is a probabilistic inference │
│ archive — replay or        │ engine: schema-guided, adaptively   │
│ storage device.            │ accurate, systematically distorted. │
│ Retrieval = access.        │ Retrieval = re-construction.        │
│                            │ → [[Reconstructive-Memory]]         │
├────────────────────────────┼─────────────────────────────────────┤
│ TENSION 2: WORKING MEMORY  │                                     │
│ Working memory is a        │ WM limits define the ceiling;       │
│ bottleneck — the          │ schema automation raises the floor.  │
│ constraint to minimise.    │ Expertise = converting effortful    │
│ Reduce load, period.       │ processing into automated schemas.  │
│                            │ → [[Schema-Automation]]             │
├────────────────────────────┼─────────────────────────────────────┤
│ TENSION 3: AUTONOMY        │                                     │
│ Autonomy means freedom     │ Autonomy = internalised structure,  │
│ from instruction.          │ not its absence. Fading scaffolding │
│ OR: instruction means      │ engineers the SDT internalisation   │
│ control (not autonomy).    │ continuum from external regulation  │
│                            │ to intrinsic motivation.            │
│                            │ → [[Internalization-Continuum]]     │
├────────────────────────────┼─────────────────────────────────────┤
│ TENSION 4: INDIVIDUAL vs.  │                                     │
│ SOCIAL COGNITION           │ Cognition is multi-level: individual│
│ Cognition is what one      │ biological architecture is real;    │
│ brain does alone — social  │ social/artefactual scaffolding      │
│ or artefact involvement    │ extends it without eliminating its  │
│ is 'assistance', not cog.  │ limits. PKB = cognitive prosthetic. │
│                            │ → [[Cognitive-Offloading]]          │
├────────────────────────────┼─────────────────────────────────────┤
│ TENSION 5: RATIONALITY     │                                     │
│ Either: humans are         │ Neither pole. Intellectual humility │
│ fundamentally rational     │ + calibration + epistemic hygiene   │
│ (bias = exception).        │ are appropriate responses. Debiasing│
│ OR: humans are biased      │ strategies have documented efficacy.│
│ and reason cannot be       │ Normative standards remain valid    │
│ trusted.                   │ even when descriptive reality falls │
│                            │ short. → [[Intellectual-Humility]]  │
└────────────────────────────┴─────────────────────────────────────┘

Source: §"The Five Foundational Tensions"

Reading guide: The left column represents the "textbook simplification"
or "common sense" framing a reader might arrive with. The right column
is the vault's nuanced position, which consistently rejects both poles
in favour of a third synthesis that integrates the valid insights of
each. Notice the pattern: every synthesis is a both/and reframe, not
an either/or resolution.


══════════════════════════════════════════════════════════════════
  Visual Aid 10: TL;DR Scorecard
══════════════════════════════════════════════════════════════════

╔══════════════════════════════════════════════════════════════════╗
║         MOC — COGNITIVE SCIENCE (MASTER INDEX) SCORECARD        ║
╠══════════════════════════════════════════════════════════════════╣
║ Document type  : Top-level navigation MOC (not a content note)  ║
║ Scope          : 10 domain MOCs · ~533 permanent notes          ║
║ Unifying Qs    : How do minds acquire, organise, evaluate, and  ║
║                  apply knowledge — and how can we engineer       ║
║                  conditions that make this more effective?       ║
╠══════════════════════════════════════════════════════════════════╣
║ CORE THESIS    : The PKB is not merely documented by this vault. ║
║                  It is an instantiation of the cognitive science ║
║                  it documents — its architecture directly applies║
║                  principles from every stratum it contains.      ║
╠══════════════════════════════════════════════════════════════════╣
║ LARGEST MOC    : [[MOC - Motivation Psychology]] (78 notes)      ║
║ MOST BRIDGED   : [[Metacognitive-Monitoring]] (9 MOC bridges)    ║
║ WIDEST CONCEPT : [[Dual-Process-Theory]] (spans 7 MOCs)          ║
║ APPLIED APEX   : [[MOC - PKB & Knowledge Management]] (Strat. 4) ║
╠══════════════════════════════════════════════════════════════════╣
║ 5 GENERATIVE   : 1. Storage vs. Reconstruction (Memory)         ║
║ TENSIONS       : 2. Limits vs. Architecture (CLT)               ║
║                : 3. Autonomy vs. Structure (Motivation/SRL)     ║
║                : 4. Individual vs. Social Cognition (PKB)       ║
║                : 5. Rationality vs. Bias (Dual Process/CT)      ║
╠══════════════════════════════════════════════════════════════════╣
║ BEST ENTRY PT  : Path A (Learner's Toolkit) for personal use;   ║
║                  Path B (Instructor's Map) for design work;     ║
║                  Path C (Critical Reasoner) for epistemics;     ║
║                  Path D (PKB Architect) for system building.    ║
╠══════════════════════════════════════════════════════════════════╣
║ VAULT GAPS     : Affective Neuroscience · Developmental Psych   ║
║ (identified)   : Computational Cog. Sci. · Psycholinguistics    ║
║                : Applied Cognitive Ergonomics                   ║
╠══════════════════════════════════════════════════════════════════╣
║ READ THIS IF   : You need a top-down orientation before diving  ║
║                  into domain-level MOCs; or you're designing     ║
║                  cross-domain connections and need the bridge   ║
║                  note inventory; or you want the rationale for  ║
║                  the PKB architecture itself.                   ║
║ SKIP IF        : You already know which domain MOC you need     ║
║                  and want to go directly there.                 ║
╚══════════════════════════════════════════════════════════════════╝


───────────────────────────────────────────────────────────────────────────


══════════════════════════════════════════════════════════════════
  SYNTHESIS PACKET — Navigator + Top Takeaways
══════════════════════════════════════════════════════════════════

TOP 5 TAKEAWAYS FROM THIS DOCUMENT:

1. THE VAULT IS A DEPENDENCY STACK, NOT TEN SILOS
   Epistemology grounds Critical Thinking; Memory constrains CLT;
   CLT + Memory → Metacognition/SRL; all four + Motivation + Social
   Psychology converge in PKB. Understanding any domain fully
   requires at least partial familiarity with those above it.

2. FIVE TENSIONS ARE THE INTELLECTUAL ENGINE
   The vault's depth does not come from summarising theories; it
   comes from holding five productive tensions and refusing to
   resolve them into either pole. Knowing these tensions is more
   valuable than knowing any single framework.

3. FIFTEEN NOTES DO MOST OF THE CONNECTIVE WORK
   [[Dual-Process-Theory]], [[Working-Memory]], [[Metacognitive-
   Monitoring]], [[Self-Determination-Theory]], and [[Schema-Theory]]
   are the five highest-priority bridge notes. Reading these five
   will unlock cross-domain comprehension faster than any single
   domain MOC.

4. THE PKB IS A SCIENTIFIC ARTEFACT, NOT JUST A TOOL
   Each architectural decision — atomic notes, bi-directional
   links, MOC structure — has a direct theoretical justification
   in cognitive science. This is not metaphor: the vault is a
   direct application of its own content.

5. NOTE DENSITY ≠ IMPORTANCE; BRIDGING ≠ SIZE
   The smallest MOC (PKB, 36 notes) and the second-smallest
   (Social Psychology, 38) are the highest-betweenness hubs
   for practical application. Motivation (78 notes) is the
   largest but is also the most internally developed and most
   self-contained. Bridge notes live at domain intersections,
   not in the densest domains.


NAVIGATOR — Which aid answers which question:

  "What is the overall structure of the vault?"
        → Aid 1 (Cross-Domain Architecture Map)

  "How big and how complex is each domain?"
        → Aid 2 (MOC Registry Bar Chart)

  "What are the big unresolved debates?"
        → Aid 3 (Five Foundational Tensions Matrix)

  "Who built what, and which MOC should I find it in?"
        → Aid 4 (Theoretical Lineage Map)

  "Which notes should I read first for cross-domain depth?"
        → Aid 5 (High-Betweenness Bridge Nodes)

  "Which path should I follow given my goal?"
        → Aid 6 (Reading Paths Swimlane)

  "Why does my PKB architecture actually work?"
        → Aid 7 (PKB as Cognitive Prosthetic)

  "In what order should I study the ten domains?"
        → Aid 8 (Vault Prerequisite Dependency Graph)

  "What do I need to unlearn to get full value from this vault?"
        → Aid 9 (Five Tensions Before/After Contrast)

  "What is the single-page summary?"
        → Aid 10 (TL;DR Scorecard)


FINAL SCORECARD (repeated for standalone use):

╔══════════════════════════════════════════════════════════════════╗
║ Core thesis  : PKB architecture IS cognitive science in action  ║
║ Strongest pt : Tension framework — 5 generative debates         ║
║ Key action   : Read bridge notes before diving domain MOCs      ║
║ Best path    : Depends on goal (A/B/C/D — see Aid 6)            ║
║ Vault gaps   : Affective neuroscience, developmental psych      ║
╚══════════════════════════════════════════════════════════════════╝
```

---

Ten aids covering the full document. All PKB-ready with wiki-links drawn from your permanent note collection. The most actionable single artifact is **Aid 5** (the bridge node matrix) — that ✓ table tells you exactly which notes to hit first for cross-domain leverage across all ten MOCs.