---
tags: [moc, domain-cognitive-load-theory, domain-instructional-design, status-evergreen]
aliases: [CLT MOC, Cognitive Load MOC]
created: 2026-05-15
modified: 2026-05-15
status: evergreen
type: moc
moc_pattern: progressive
domain: Cognitive Load Theory
source_notes_count: 44
target_word_count: 4500
audience: [practitioner, researcher]
maturity: established
parent_moc: "[[MOC - Cognitive Science (Master Index)]]"
related_mocs: ["[[MOC - Memory Science]]", "[[MOC - Learning Science]]", "[[MOC - Metacognition and Self-Regulated Learning]]"]
version: 1.0.0
---

# Cognitive Load Theory — Map of Content

> [!abstract] Domain & Scope
> **Cognitive Load Theory (CLT)** is an instructional design framework grounded in cognitive architecture — specifically, the interaction between a limited working memory and an effectively unlimited long-term memory. This MOC organises 44 permanent notes covering the theory's foundations, the three-load taxonomy, instructional effects, the 4C/ID design system, and the theory's evolving frontiers. It is structured as a **progressive** sequence — from cognitive architecture → load taxonomy → instructional effects → design applications — matching the conceptual dependencies within the theory.
>
> **For**: Instructional designers, learning scientists, educators
> **Companion MOCs**: [[MOC - Memory Science]], [[MOC - Learning Science]]
> **Reading time**: ~22 minutes

## 🗺️ Navigation

- **[Cognitive Architecture: The Substrate](#cognitive-architecture-the-substrate)** — why architecture constrains learning
- **[The Three-Load Taxonomy](#the-three-load-taxonomy)** — intrinsic, extraneous, germane
- **[Element Interactivity: The Engine of Intrinsic Load](#element-interactivity-the-engine-of-intrinsic-load)** — what makes content hard
- **[The Instructional Effects Catalogue](#the-instructional-effects-catalogue)** — empirically validated design principles
- **[4C/ID: Complex Learning Architecture](#4cid-complex-learning-architecture)** — from CLT to curriculum design
- **[Evolutionary Foundations](#evolutionary-foundations)** — biological primacy and secondary knowledge
- **[Frontier & Open Questions](#frontier--open-questions)**
- **[Index of Linked Notes](#index-of-linked-notes)**

---

## Cognitive Architecture: The Substrate

CLT is anchored in a specific account of human [[cognitive-architecture|cognitive architecture]] that contrasts strikingly with naive intuitions about learning. The architecture has three key properties:

1. **Working memory is severely limited** — roughly 4 items without chunking, and capacity degrades further under dual-task conditions.
2. **Long-term memory is effectively unlimited** — and organised into [[schema|schemas]] that can be retrieved as single, complex units.
3. **Schemas in long-term memory effectively expand working memory** — a chess master's chunk encodes an entire board configuration as a single long-term memory schema retrieved as one working memory unit.

This asymmetry between working and long-term memory is the theoretical crux. Learning is the process of constructing and automating schemas in long-term memory, such that increasingly complex patterns can be processed with diminishing working memory demand. [[schema-construction|Schema construction]] is therefore the proximal goal of instruction, not short-term performance.

[[schema-automation|Schema automation]] — the process by which repeated use renders schema application fast, effortless, and automatic — is a further stage that frees working memory for higher-order operations. The power-law of practice governs this transition: early practice produces dramatic efficiency gains; later practice yields diminishing returns.

> [!key-claim] The Fundamental Asymmetry
> The instructional challenge is not to transmit information into working memory — it is to facilitate schema construction in long-term memory using a channel (working memory) that can barely hold four things at once. Everything else in CLT follows from this constraint.

[Prerequisite-For:: [[three-load-taxonomy]], [[instructional-effects]]]

---

## The Three-Load Taxonomy

[[the-standard-three-load-taxonomy|The standard three-load taxonomy]] distinguishes three forms of working memory demand:

| Load Type | Source | Instructional Target |
|-----------|--------|---------------------|
| [[intrinsic-cognitive-load\|Intrinsic]] | Element interactivity of the material | Manage via sequencing, scaffolding |
| [[extraneous-cognitive-load\|Extraneous]] | Unnecessary processing from poor design | Eliminate via design principles |
| [[germane-cognitive-load\|Germane]] | Schema construction and automation | Support through effortful practice |

### Intrinsic Load

[[intrinsic-cognitive-load|Intrinsic load]] is determined by the interaction between the learner's prior knowledge and the inherent complexity of the material, operationalised as [[element-interactivity|element interactivity]] — the number of information elements that must be held in working memory simultaneously because they interact with each other.

Low element interactivity content (e.g., vocabulary acquisition, where each word-meaning pair can be learned independently) is inherently low in intrinsic load. High element interactivity content (e.g., grammatical parsing, algebraic manipulation) requires multiple interdependent elements to be processed simultaneously. For a novice, all elements are interactive — for an expert, most are encapsulated in schemas and processed as single units.

### Extraneous Load

[[extraneous-cognitive-load|Extraneous load]] is working memory demand generated by instructional design rather than by the learning material itself — the load of navigating a poorly organised text, integrating spatially separated but conceptually related diagrams and explanations, or suppressing irrelevant decorative information. It serves no schema-construction function and should be minimised.

### The Evolution of Germane Load

[[the-evolution-of-germane-load|The evolution of the germane load construct]] represents the most significant theoretical refinement in CLT's history. In Sweller's original formulation (1988-1994), germane load was conceived as a distinct third type — effort specifically devoted to schema construction. In [[sweller-s-2010-reconceptualization|Sweller's 2010 reconceptualization]], germane load was reconceived not as a separate type but as *intrinsic load that is productively processed for schema formation*. This matters because it implies that the goal is not to add germane load on top of intrinsic and extraneous, but to ensure that intrinsic load is handled by schema-constructive processing, not extraneous busywork.

---

## Element Interactivity: The Engine of Intrinsic Load

[[why-element-interactivity-is-the-engine-of-intrinsic-load|Element interactivity is the engine of intrinsic load]] because it determines how many cognitive elements must be simultaneously active in working memory for successful processing. Two types of element interactivity bear distinguishing:

- **Logical interactivity** — elements that are objectively interdependent (syntactic rules, mathematical variables, logical dependencies)
- **Subjective interactivity** — perceived interactivity that decreases as expertise develops (what was once a complex procedure becomes a single automated schema)

This has direct implications for instructional sequencing: the [[isolated-elements-effect|isolated elements effect]] demonstrates that presenting interacting elements in isolation before integrating them reduces load for novices, even though the isolated presentation is logically incomplete. The pedagogical logic is that partial schemas are more useful than no schemas.

[[the-expertise-reversal-effect|The expertise reversal effect]] is CLT's most practically significant and theoretically rich finding: instructional techniques that are highly effective for novices become *less effective or even counterproductive* for experts. Worked examples are the canonical case — novices benefit enormously from detailed solution steps, while experts are impeded by them (they generate extraneous load by requiring the expert to process information they can already infer from schemas). The implication is that instruction must adapt dynamically to learner expertise.

---

## The Instructional Effects Catalogue

CLT has generated a rich empirical programme identifying how specific instructional designs affect working memory load. The major effects:

### The Worked Example Effect

[[the-worked-example-effect|The worked example effect]] is among CLT's most replicated findings. Novices who study worked examples learn more than those who solve equivalent problems, because problem-solving requires search through a problem space that generates high extraneous load without contributing to schema construction. [[worked-examples|Worked examples]] direct attention to the solution structure, supporting [[schema-formation|schema formation]] directly.

[[faded-worked-examples|Faded worked examples]] — a hybrid approach where solution steps are progressively removed as competence develops — provide an elegant instructional sequence that manages the transition from novice to expert while avoiding the expertise reversal effect. [[worked-example-variability|Worked example variability]] (using multiple structurally varied examples) promotes transferable schemas rather than surface-specific procedures.

### The Split-Attention Effect

[[split-attention-effect|The split-attention effect]] occurs when learners must mentally integrate multiple spatially or temporally separated sources of information. The integration itself consumes working memory, generating extraneous load. The design solution is *physical integration* — placing related information together — which converts extraneous to productive processing.

### The Modality Effect

[[the-modality-effect|The modality effect]] exploits the multicomponent structure of working memory: the phonological loop and visuospatial sketchpad can process information in parallel, effectively doubling available capacity for dual-modal presentations. Presenting visual information with accompanying narration (rather than on-screen text) uses both systems simultaneously and reduces overload. The [[modality-effect|modality effect]] is among CLT's strongest practical design implications.

### The Redundancy Effect

[[redundancy-effect|The redundancy effect]] is the counterintuitive finding that adding information can impair learning. When the same information is presented in two formats (e.g., a self-explanatory diagram plus a text explaining the same diagram), learners must redundantly process both, generating extraneous load. Removing the redundant source improves performance. The [[coherence-principle|coherence principle]] is the instructional application: eliminate seductive but irrelevant details.

The [[seductive-details-effect|seductive details effect]] specifically names the harm caused by interesting but irrelevant adjuncts — fascinating sidebars that capture attention and consume working memory without contributing to learning goals.

```
CLT Instructional Effects Overview
═══════════════════════════════════════════════════════════
Effect              | Problem it addresses   | Design fix
─────────────────────────────────────────────────────────
Worked Example      | Problem-solving load   | Study solutions before solving
Split-Attention     | Integration effort     | Physically integrate materials
Modality            | WM channel overload    | Narrate visuals; don't caption
Redundancy          | Redundant processing   | Remove, don't add
Expertise Reversal  | Expert over-scaffolding| Fade support as skill grows
Seductive Details   | Irrelevant material    | Cut interesting but off-topic content
Isolated Elements   | Overload from complex  | Teach elements before integration
═══════════════════════════════════════════════════════════
```

---

## 4C/ID: Complex Learning Architecture

[[four-component-instructional-design-4c-id|Four-Component Instructional Design (4C/ID)]] is the most comprehensive CLT-based design model for complex skill learning. Van Merriënboer's framework addresses a limitation of worked-example research: its findings were largely generated with single-solution tasks in laboratory settings, not the complex, ill-structured real-world performance that professional education targets.

[[the-four-components-of-4c-id|The four components]] are:

1. **Learning tasks** — whole, authentic, meaningful tasks that constitute the backbone of the curriculum
2. **Supportive information** — information supporting the development of mental models and problem-solving schemas
3. **Procedural information** — just-in-time information for rule-based procedures
4. **Part-task practice** — additional practice for constitutent skills requiring high automatisation

[[the-whole-task-approach]] within 4C/ID represents a philosophical commitment: complex skills are never decomposed to the point of losing the whole-task context, because transfer requires experience with the integrated performance. This is in productive tension with the element isolation principle — and [[the-clt-desirable-difficulties-reconciliation|the CLT-desirable difficulties reconciliation]] addresses how these can be integrated.

---

## Evolutionary Foundations

CLT's account of why some knowledge is easy to learn and other knowledge is hard traces to evolutionary history. [[biological-primary-knowledge|Biologically primary knowledge]] — social intelligence, basic language, intuitive physics — is knowledge our evolutionary lineage prepared us to acquire without explicit instruction, through normal experience. [[biological-secondary-knowledge|Biologically secondary knowledge]] — reading, mathematics, systematic scientific reasoning — is culturally constructed and must be explicitly taught, because natural selection has not prepared us for it.

[[evolutionary-educational-psychology|Evolutionary educational psychology]] uses this framework to explain why schools exist: the architecture of biological secondary knowledge acquisition requires intentional instructional environments precisely because these skills are not spontaneously acquired.

---

## 🌉 Cross-Domain Bridges

> [!related] Companion MOCs
> - [[MOC - Memory Science]] — The cognitive architecture CLT presupposes is detailed in the Memory Science MOC; working memory capacity limits are the foundational constraint.
> - [[MOC - Learning Science]] — CLT is the theoretical backbone of most evidence-based instructional design; the Learning Science MOC contextualises CLT within a broader ecology of learning principles.
> - [[MOC - Metacognition and Self-Regulated Learning]] — The expertise reversal effect has direct implications for adaptive self-regulation: expert learners who apply novice-appropriate strategies (e.g., studying worked examples) are wasting effort.

---

## 🌅 Frontier & Open Questions

> [!frontier] Live debates within CLT
> - **Measuring load**: Working memory load cannot be directly observed; the three proxy measures (subjective rating, dual-task performance, physiological indicators like pupil dilation) correlate imperfectly and tap different aspects of load. The field lacks a gold-standard measurement tool.
> - **Germane load operationalisation**: Despite the 2010 reconceptualisation, distinguishing germane from intrinsic load empirically remains difficult.
> - **Ecological validity**: Most CLT research involves relatively simple laboratory tasks; scaling findings to complex, professional learning contexts involves theoretically unresolved extrapolations.

---

## 📚 Index of Linked Notes

| Note | Type | Section |
|------|------|---------|
| [[biological-primary-knowledge]] | atomic | Evolutionary Foundations |
| [[biological-secondary-knowledge]] | atomic | Evolutionary Foundations |
| [[cognitive-architecture]] | reference | Architecture |
| [[coherence-principle]] | atomic | Effects |
| [[element-interactivity]] | reference | Element Interactivity |
| [[evolutionary-educational-psychology]] | atomic | Evolutionary Foundations |
| [[extraneous-cognitive-load]] | reference | Taxonomy |
| [[expertise-reversal-effect]] | atomic | Effects |
| [[faded-worked-examples]] | atomic | Effects |
| [[four-component-instructional-design-4c-id]] | reference | 4C/ID |
| [[germane-cognitive-load]] | atomic | Taxonomy |
| [[intrinsic-cognitive-load]] | reference | Taxonomy |
| [[isolated-elements-effect]] | atomic | Element Interactivity |
| [[modality-effect]] | atomic | Effects |
| [[redundancy-effect]] | atomic | Effects |
| [[schema]] | atomic | Architecture |
| [[schema-automation]] | atomic | Architecture |
| [[schema-construction]] | atomic | Architecture |
| [[schema-formation]] | atomic | Architecture |
| [[seductive-details-effect]] | atomic | Effects |
| [[split-attention-effect]] | atomic | Effects |
| [[sweller-s-2010-reconceptualization]] | atomic | Taxonomy |
| [[the-clt-desirable-difficulties-reconciliation]] | synthesis | 4C/ID |
| [[the-evolution-of-germane-load]] | atomic | Taxonomy |
| [[the-expertise-reversal-effect]] | reference | Effects |
| [[the-four-components-of-4c-id]] | reference | 4C/ID |
| [[the-history-and-evolution-of-cognitive-load-theory]] | reference | Architecture |
| [[the-modality-effect]] | atomic | Effects |
| [[the-standard-three-load-taxonomy]] | reference | Taxonomy |
| [[the-worked-example-effect]] | reference | Effects |
| [[why-element-interactivity-is-the-engine-of-intrinsic-load]] | synthesis | Element Interactivity |
| [[worked-example-variability]] | atomic | Effects |
| [[worked-examples]] | reference | Effects |
| [[working-memory-in-the-clt-framework]] | synthesis | Architecture |

---

> [!info] MOC Metadata
> - **Pattern**: progressive
> - **Source notes**: 44
> - **Word count**: ~4,200
> - **Generated**: 2026-05-15 by MOC Specialist Agent v1.0.0
> - **Audit trail**: [[_meta/MOC - Cognitive Load Theory.audit]]
> - **Next review suggested**: 2026-08-15

Now I have the full document. Let me execute the full pipeline.

---

# Visual Aid Suite: Cognitive Load Theory — Map of Content

**Report length:** ~4,200 words | **Source notes:** 44 linked permanents
**Audience:** Instructional designers, learning scientists, practitioners
**Thesis:** CLT is an instructional design framework built on a single fundamental asymmetry — working memory holds ~4 items while long-term memory is effectively unlimited — and every design principle follows from the imperative to facilitate schema construction through that bottleneck.

**Aids selected:**
1. **Causal Architecture Map** — the WM/LTM asymmetry is the theoretical crux; must be visualised first
2. **Three-Load Taxonomy Matrix** — core classification; highest density of linked notes
3. **Element Interactivity Spectrum** — drives intrinsic load; novice/expert axis is critical
4. **Instructional Effects Catalogue** — 7 empirically validated effects; the practical heart of CLT
5. **Expertise Reversal Process Flow** — the most consequential and counterintuitive finding
6. **4C/ID Architecture Diagram** — complex-learning extension; structurally distinct from single-task research
7. **Germane Load Evolution Timeline** — the most significant theoretical revision in CLT history
8. **Evolutionary Foundations Contrast** — biological primary vs. secondary explains why explicit instruction exists
9. **Before / After Design Panel** — practitioner-facing design transformation
10. **TL;DR Scorecard**

---

## Visual Aid 1: Causal Architecture Map

**Purpose:** Shows the fundamental WM/LTM asymmetry and the causal chain through which CLT's design prescriptions follow.

```
╔═══════════════════════════════════════════════════════════════════╗
║         COGNITIVE LOAD THEORY — CAUSAL ARCHITECTURE              ║
╚═══════════════════════════════════════════════════════════════════╝

  ┌─────────────────────────────────────────────────────────────┐
  │              COGNITIVE ARCHITECTURE                          │
  │                                                             │
  │  WORKING MEMORY           LONG-TERM MEMORY                  │
  │  ┌──────────────┐         ┌──────────────────────────┐     │
  │  │  ~4 items    │         │  Effectively unlimited   │     │
  │  │  fragile     │         │  Schema-organised        │     │
  │  │  temporary   │         │  Permanent               │     │
  │  └──────┬───────┘         └────────────┬─────────────┘     │
  │         │                              │                   │
  │         │◄─────── Schema retrieval ────┘                   │
  │         │         (1 schema = 1 WM slot)                   │
  └─────────┼─────────────────────────────────────────────────-┘
            │
            ▼
  ┌─────────────────────────────────────────────────────────────┐
  │              THE FUNDAMENTAL CONSTRAINT                      │
  │                                                             │
  │   Complex material presents MANY interacting elements       │
  │   Working memory can hold only FEW items at once            │
  │   → Bottleneck: learning must pass through a 4-slot channel │
  └─────────────────────┬───────────────────────────────────────┘
                        │
            ┌───────────┼───────────┐
            ▼           ▼           ▼
  ┌─────────────┐ ┌──────────┐ ┌──────────────────┐
  │ INTRINSIC   │ │EXTRANEOUS│ │    GERMANE        │
  │    LOAD     │ │   LOAD   │ │ (= productive     │
  │             │ │          │ │  intrinsic load)  │
  │ From the    │ │ From poor │ │ Intrinsic load    │
  │ material    │ │ design   │ │ channelled into   │
  │ itself      │ │          │ │ schema formation  │
  └──────┬──────┘ └────┬─────┘ └────────┬─────────┘
         │             │                │
         ▼             ▼                ▼
      MANAGE        ELIMINATE         SUPPORT
    (sequence,    (design              (effortful
    scaffold)      principles)         practice)
                        │
                        ▼
  ┌─────────────────────────────────────────────────────────────┐
  │                  PROXIMAL GOAL OF INSTRUCTION               │
  │                                                             │
  │   Schema construction in LTM → schema automation           │
  │   → fewer WM slots needed → expertise                       │
  └─────────────────────────────────────────────────────────────┘

Source: §Cognitive Architecture; §The Three-Load Taxonomy
```

**Reading guide:** Read top-down. The architecture panel establishes the constraint; the bottleneck panel names the problem; the three-load split shows how CLT categorises demand; the arrows show the design prescription for each type. The key move is that "germane load" is not a third type added to the others — it is intrinsic load redirected productively. The proximal goal box is the anchor: short-term performance is not the target; schema construction is.

**Source:** §Cognitive Architecture: The Substrate; §The Three-Load Taxonomy

---

## Visual Aid 2: Three-Load Taxonomy — Classification Matrix

**Purpose:** Precisely distinguishes all three load types across six diagnostic dimensions so practitioners can identify load types in their own materials.

```
╔═══════════════════════════════════════════════════════════════════════════╗
║             THE THREE-LOAD TAXONOMY — DIAGNOSTIC MATRIX                  ║
╚═══════════════════════════════════════════════════════════════════════════╝

┌──────────────────────┬───────────────────┬───────────────────┬───────────────────┐
│   DIMENSION          │  INTRINSIC LOAD   │ EXTRANEOUS LOAD   │   GERMANE LOAD    │
│                      │  [[Intrinsic-     │ [[Extraneous-     │ [[Germane-        │
│                      │  Cognitive-Load]] │ Cognitive-Load]]  │ Cognitive-Load]]  │
├──────────────────────┼───────────────────┼───────────────────┼───────────────────┤
│ SOURCE               │ Material itself:  │ Instructional     │ Intrinsic load    │
│                      │ element           │ design flaws      │ processed for     │
│                      │ interactivity     │ (layout, format,  │ schema formation  │
│                      │                  │ redundancy)       │ (not a 3rd type)  │
├──────────────────────┼───────────────────┼───────────────────┼───────────────────┤
│ INSTRUCTIONAL        │ Partially         │ Fully             │ Fully             │
│ CONTROLLABILITY      │ controllable      │ controllable      │ supportable       │
│                      │ (sequence,        │ (design           │ (practice design) │
│                      │  scaffold)        │  principles)      │                   │
├──────────────────────┼───────────────────┼───────────────────┼───────────────────┤
│ DESIGN               │ MANAGE:           │ ELIMINATE:        │ SUPPORT:          │
│ PRESCRIPTION         │ Sequence from     │ Integrate split   │ Provide effortful │
│                      │ low to high EI;   │ materials;        │ varied practice;  │
│                      │ scaffold novices  │ remove redundancy │ use worked        │
│                      │                  │                   │ examples          │
├──────────────────────┼───────────────────┼───────────────────┼───────────────────┤
│ RELATION TO          │ Constitutes the   │ Wastes WM         │ IS intrinsic load │
│ SCHEMA               │ challenge to be   │ with no schema    │ productively      │
│ CONSTRUCTION         │ overcome          │ contribution      │ directed          │
├──────────────────────┼───────────────────┼───────────────────┼───────────────────┤
│ EXPERT vs.           │ Decreases with    │ Remains unless    │ Shifts focus as   │
│ NOVICE               │ expertise (schema │ design is fixed   │ expertise grows   │
│                      │ encapsulation)    │                   │                   │
├──────────────────────┼───────────────────┼───────────────────┼───────────────────┤
│ KEY RISK             │ Overload from     │ WM wasted on      │ Being mistaken    │
│                      │ high element      │ irrelevant        │ for a separate    │
│                      │ interactivity     │ processing        │ additive type     │
├──────────────────────┼───────────────────┼───────────────────┼───────────────────┤
│ THEORETICAL          │ Stable since 1988 │ Stable since 1988 │ REVISED 2010:     │
│ STATUS               │                  │                   │ reconceived as    │
│                      │                  │                   │ productive-       │
│                      │                  │                   │ intrinsic         │
└──────────────────────┴───────────────────┴───────────────────┴───────────────────┘

⚠  CRITICAL DISTINCTION: Total WM load = Intrinsic + Extraneous
   Germane load is NOT additive — it is intrinsic load well-spent.
   The goal: minimise extraneous → maximise proportion of intrinsic
   load devoted to schema construction (= germane).

Source: §The Three-Load Taxonomy; [[the-standard-three-load-taxonomy]]
```

**Reading guide:** Read each row as a diagnostic lens. The "Theoretical Status" row is the most important for advanced practitioners — the 2010 reconceptualisation changes the design logic entirely: you cannot *add* germane load; you can only redirect intrinsic load. The warning box beneath the table captures the most common misreading of CLT. The bracketed wiki-links connect directly to the permanent notes containing the full theoretical treatments.

**Source:** §The Three-Load Taxonomy; §The Evolution of Germane Load

---

## Visual Aid 3: Element Interactivity Spectrum

**Purpose:** Maps the novice-to-expert axis against element interactivity to show why the same material presents radically different intrinsic loads to different learners.

```
╔═══════════════════════════════════════════════════════════════════════╗
║      ELEMENT INTERACTIVITY — THE EXPERTISE AXIS                      ║
╚═══════════════════════════════════════════════════════════════════════╝

CONTENT
COMPLEXITY          LOW EI                           HIGH EI
(Intrinsic)   ◄──────────────────────────────────────────────►
              │                                              │
 EXAMPLES:    │ Vocab: word-meaning pairs           Algebra: │
              │ (each learned independently)    variables,   │
              │                               rules, syntax  │
              │                              all interact    │
              ▼                                              ▼

NOVICE        ╔══════════════════════════════════════════════╗
              ║ ALL elements perceived as interactive         ║
              ║ Schemas not yet formed to chunk them         ║
              ║ → WM rapidly overwhelmed                     ║
              ║ → [[Intrinsic-Cognitive-Load]] very HIGH      ║
              ╚══════════════════════════════════════════════╝
                                   │
                    Schema construction over time
                                   │
                                   ▼
DEVELOPING    ╔══════════════════════════════════════════════╗
              ║ Partial schemas chunk some elements           ║
              ║ Interactivity perceived as moderate          ║
              ║ Scaffolding still beneficial                 ║
              ║ Faded worked examples appropriate here       ║
              ║ → [[faded-worked-examples]]                   ║
              ╚══════════════════════════════════════════════╝
                                   │
                    Automation of schemas
                                   │
                                   ▼
EXPERT        ╔══════════════════════════════════════════════╗
              ║ Most elements encapsulated in schemas         ║
              ║ Complex structure retrieved as 1 WM unit     ║
              ║ Previously high-EI content now LOW EI        ║
              ║ → [[Expertise-Reversal-Effect]] kicks in      ║
              ║ Novice-style support ADDS extraneous load    ║
              ╚══════════════════════════════════════════════╝

─────────────────────────────────────────────────────────────────
  DESIGN IMPLICATION: The SAME material has DIFFERENT intrinsic
  load for different learners. Instruction MUST adapt.
─────────────────────────────────────────────────────────────────

PEDAGOGICAL BRIDGE — Isolated Elements Effect:
  [[isolated-elements-effect]]
  Present interacting elements IN ISOLATION before integrating them.
  Partial schemas are more useful than no schemas, even if the
  isolated presentation is logically incomplete.

Source: §Element Interactivity; [[element-interactivity]]
```

**Reading guide:** Read vertically from Novice to Expert. The key insight is that element interactivity is not a fixed property of content — it is a *relational* property between content and learner. As schemas form, perceived interactivity decreases, and previously difficult material becomes processable as single units. The design implication at the bottom is the actionable summary: identical materials impose radically different loads on different learners, making adaptive instruction not merely desirable but theoretically mandated.

**Source:** §Element Interactivity: The Engine of Intrinsic Load

---

## Visual Aid 4: Instructional Effects Catalogue

**Purpose:** Provides a complete reference for all seven major CLT-derived instructional effects, their causal mechanism, and the design prescription each mandates.

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║         CLT INSTRUCTIONAL EFFECTS — COMPLETE CATALOGUE                       ║
╚═══════════════════════════════════════════════════════════════════════════════╝

┌─────────────────────┬────────────────────────┬────────────────┬──────────────┐
│  EFFECT             │  MECHANISM             │ DESIGN FIX     │  EVIDENCE    │
│                     │  (why it works)        │                │  STRENGTH    │
├─────────────────────┼────────────────────────┼────────────────┼──────────────┤
│ WORKED EXAMPLE      │ Problem-solving search │ Study worked   │  ★★★★★      │
│ [[the-worked-       │ generates extraneous   │ solutions      │  Most        │
│ example-effect]]    │ load; examples direct  │ BEFORE solving │  replicated  │
│                     │ attention to schema    │ equivalent     │  CLT finding │
│                     │ structure              │ problems       │              │
├─────────────────────┼────────────────────────┼────────────────┼──────────────┤
│ SPLIT-ATTENTION     │ Mental integration of  │ Physically     │  ★★★★★      │
│ [[split-attention-  │ spatially separated    │ integrate      │  Strong      │
│  effect]]           │ materials consumes WM  │ related        │  empirical   │
│                     │ (extraneous load)      │ materials      │  base        │
├─────────────────────┼────────────────────────┼────────────────┼──────────────┤
│ MODALITY            │ WM has two parallel    │ Narrate        │  ★★★★☆      │
│ [[the-modality-     │ subsystems (visual +   │ visuals with   │  Strong;     │
│  effect]]           │ phonological); dual-   │ audio, not     │  some        │
│ [[Modality-Effect]] │ modal uses both        │ on-screen text │  moderators  │
│                     │ simultaneously         │                │  found       │
├─────────────────────┼────────────────────────┼────────────────┼──────────────┤
│ REDUNDANCY          │ Duplicate information  │ Remove the     │  ★★★★☆      │
│ [[redundancy-       │ in two formats forces  │ redundant      │  Counter-    │
│  effect]]           │ parallel processing    │ source (even   │  intuitive;  │
│                     │ of same content        │ if it seems    │  well        │
│                     │ → extraneous load      │ helpful)       │  supported   │
├─────────────────────┼────────────────────────┼────────────────┼──────────────┤
│ EXPERTISE REVERSAL  │ Support designed for   │ Fade           │  ★★★★☆      │
│ [[the-expertise-    │ novices adds           │ scaffolding    │  Highly      │
│ reversal-effect]]   │ extraneous load for    │ dynamically    │  practical   │
│                     │ experts who can        │ as expertise   │  significance│
│                     │ infer what is shown    │ develops       │              │
├─────────────────────┼────────────────────────┼────────────────┼──────────────┤
│ SEDUCTIVE DETAILS   │ Interesting but        │ Cut it.        │  ★★★☆☆      │
│ [[seductive-        │ irrelevant adjuncts    │ Fascinating    │  Moderate;   │
│ details-effect]]    │ capture attention,     │ ≠ relevant     │  ecological  │
│                     │ consume WM, displace   │                │  validity    │
│                     │ learning-relevant      │                │  questions   │
│                     │ processing             │                │              │
├─────────────────────┼────────────────────────┼────────────────┼──────────────┤
│ ISOLATED ELEMENTS   │ High-EI content        │ Teach elements │  ★★★☆☆      │
│ [[isolated-         │ presented wholistically│ in isolation   │  Moderate;   │
│ elements-effect]]   │ overwhelms WM; partial │ before         │  in tension  │
│                     │ schemas enable later   │ integrating    │  with whole- │
│                     │ integration            │                │  task design │
└─────────────────────┴────────────────────────┴────────────────┴──────────────┘

 ★★★★★ = Highly replicated, robust across contexts
 ★★★★☆ = Well-supported, minor moderators identified
 ★★★☆☆ = Supported, ecological validity questions remain

 COHERENCE PRINCIPLE [[coherence-principle]]:
 Eliminates seductive details + redundancy effects under one design rule:
 "If it doesn't contribute to the learning goal, remove it."

Source: §The Instructional Effects Catalogue
```

**Reading guide:** Each row is self-contained. The "Mechanism" column is essential — it explains *why* the effect occurs, which allows designers to extend the principle to novel situations rather than mechanically applying rules. The evidence-strength column reflects the replication record honestly: the first three effects are among the most robust findings in educational psychology; the latter three carry more caveats. The Coherence Principle box shows how multiple effects converge into a single actionable meta-rule.

**Source:** §The Instructional Effects Catalogue

---

## Visual Aid 5: Expertise Reversal — Process Flow

**Purpose:** Traces the full expertise reversal mechanism from novice schema state through to expert counterproductivity, making the faded-worked-example solution visible as a dynamic transition.

```
╔══════════════════════════════════════════════════════════════════╗
║       EXPERTISE REVERSAL EFFECT — MECHANISM & RESOLUTION        ║
║       [[the-expertise-reversal-effect]] [[Expertise-Reversal-   ║
║        Effect]] [[faded-worked-examples]]                        ║
╚══════════════════════════════════════════════════════════════════╝

NOVICE STATE
┌─────────────────────────────────────────────────────────────┐
│  Schemas: absent or incomplete                              │
│  All problem elements perceived as interactive              │
│  Problem-solving: requires search through problem space     │
└──────────────────────────┬──────────────────────────────────┘
                           │
              Give WORKED EXAMPLES
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ WHY THIS WORKS FOR NOVICES:                                 │
│  • Problem-solving search → high extraneous load            │
│  • Worked examples eliminate search                         │
│  • Attention directed to solution structure                 │
│  • Schema formation accelerated                             │
│  → RESULT: Better learning than equivalent problem-solving  │
└──────────────────────────┬──────────────────────────────────┘
                           │
              Repeated practice → schemas form
                           │
                           ▼
DEVELOPING EXPERTISE
┌─────────────────────────────────────────────────────────────┐
│  Partial schemas in place                                   │
│  Can begin to infer some solution steps                     │
│  Full worked examples beginning to be redundant             │
└──────────────────────────┬──────────────────────────────────┘
                           │
         FADED WORKED EXAMPLES [[faded-worked-examples]]
         (progressively remove solution steps)
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ WHY FADING WORKS:                                           │
│  • Matches instructional support to current schema state    │
│  • Avoids redundancy effect (processing what can be inferred│
│  • Maintains productive challenge                           │
│  → RESULT: Smooth transition without expertise reversal     │
└──────────────────────────┬──────────────────────────────────┘
                           │
              Schemas complete → automation begins
                           │
                           ▼
EXPERT STATE
┌─────────────────────────────────────────────────────────────┐
│  Rich schemas encapsulate problem structure                 │
│  Can infer solution steps from problem statement alone      │
│  Worked examples now REDUNDANT                              │
└──────────────────────────┬──────────────────────────────────┘
                           │
    If still given full worked examples → ⚠ REVERSAL
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ WHY WORKED EXAMPLES HARM EXPERTS:                           │
│  • Expert can infer shown steps → shown steps = redundant   │
│  • Processing redundant information = extraneous load       │
│  • Extraneous load displaces productive processing          │
│  → RESULT: Worked examples IMPAIR expert performance        │
└─────────────────────────────────────────────────────────────┘

 DESIGN SOLUTION: Problem-solving practice for experts;
 dynamically faded examples for developing learners;
 full worked examples only for novices.

Source: §Element Interactivity; §The Instructional Effects Catalogue
```

**Reading guide:** Follow the flow top-to-bottom as a developmental sequence. The expertise reversal is not a quirk — it is a direct implication of the redundancy effect applied to expert learners. The faded-worked-example resolution in the middle of the diagram is the practical bridge that prevents reversal during the transition. The design solution box at the bottom is the actionable prescription: instruction is not a static artefact; it must adapt to expertise state.

**Source:** §Element Interactivity; §Instructional Effects Catalogue; [[the-expertise-reversal-effect]]

---

## Visual Aid 6: 4C/ID Architecture Diagram

**Purpose:** Shows the structural architecture of the Four-Component Instructional Design model and how its components address the limitations of single-task CLT research.

```
╔══════════════════════════════════════════════════════════════════════╗
║    4C/ID — FOUR-COMPONENT INSTRUCTIONAL DESIGN                      ║
║    [[four-component-instructional-design-4c-id]]                    ║
║    Extending CLT to complex, real-world skill learning              ║
╚══════════════════════════════════════════════════════════════════════╝

                  WHOLE AUTHENTIC TASK (backbone)
   ┌──────────────────────────────────────────────────────────────┐
   │                                                              │
   │  ┌────────────────────────────────────────────────────────┐ │
   │  │          COMPONENT 1: LEARNING TASKS                    │ │
   │  │          [[the-four-components-of-4c-id]]               │ │
   │  │                                                          │ │
   │  │  Whole, authentic, meaningful tasks                      │ │
   │  │  Always embedded in real-world context                   │ │
   │  │  NEVER decomposed to loss of whole-task context         │ │
   │  │                                                          │ │
   │  │  LOW complexity ──────────────────► HIGH complexity     │ │
   │  │  (early tasks, high support)     (later tasks, less)    │ │
   │  └────────────────────────────────────────────────────────┘ │
   │                         ▲                                    │
   │         ┌───────────────┼───────────────┐                   │
   │         │               │               │                   │
   │         ▼               ▼               ▼                   │
   │  ┌────────────┐  ┌─────────────┐  ┌──────────────┐         │
   │  │COMPONENT 2 │  │ COMPONENT 3 │  │ COMPONENT 4  │         │
   │  │SUPPORTIVE  │  │ PROCEDURAL  │  │  PART-TASK   │         │
   │  │INFORMATION │  │ INFORMATION │  │  PRACTICE    │         │
   │  │            │  │             │  │              │         │
   │  │ Mental     │  │ Just-in-    │  │ Constituent  │         │
   │  │ models &   │  │ time rules  │  │ skills       │         │
   │  │ problem-   │  │ for rule-   │  │ requiring    │         │
   │  │ solving    │  │ based       │  │ high         │         │
   │  │ schemas    │  │ procedures  │  │ automatisation│        │
   │  │            │  │             │  │              │         │
   │  │ PRIOR to   │  │ DURING      │  │ ALONGSIDE    │         │
   │  │ task       │  │ task        │  │ tasks        │         │
   │  └────────────┘  └─────────────┘  └──────────────┘         │
   └──────────────────────────────────────────────────────────────┘

  KEY PHILOSOPHICAL COMMITMENT — Whole-Task Approach:
  [[the-whole-task-approach]]
  ┌──────────────────────────────────────────────────────────────┐
  │ Complex skills require experience with integrated            │
  │ performance for transfer. Decomposition loses the context    │
  │ within which constituent skills must eventually operate.     │
  │                                                              │
  │ TENSION: [[isolated-elements-effect]] recommends isolation   │
  │ RESOLUTION: [[the-clt-desirable-difficulties-reconciliation]]│
  │ → Isolate for load management; always return to whole task   │
  └──────────────────────────────────────────────────────────────┘

  CLT single-task research → 4C/ID extends to:
  professional education, complex skill acquisition,
  curriculum-level design (not just lesson-level)

Source: §4C/ID: Complex Learning Architecture
```

**Reading guide:** Read the outer frame (Component 1) as the structural backbone — every 4C/ID curriculum is built around whole authentic tasks. Components 2, 3, and 4 are support structures, each with a distinct timing relationship to the learning task: prior (Component 2), during (Component 3), alongside (Component 4). The philosophical commitment box captures the productive tension with the isolated elements effect and points to where the reconciliation note lives in the PKB. The bottom note contextualises 4C/ID's scope: it is a curriculum-design system, not a single-lesson principle.

**Source:** §4C/ID: Complex Learning Architecture; [[four-component-instructional-design-4c-id]]

---

## Visual Aid 7: Germane Load — Theoretical Evolution Timeline

**Purpose:** Traces the single most significant theoretical revision in CLT history — the reconceptualisation of germane load — showing exactly what changed and why it matters for design.

```
╔══════════════════════════════════════════════════════════════════════╗
║     GERMANE LOAD — THEORETICAL EVOLUTION                            ║
║     [[the-evolution-of-germane-load]]                               ║
║     [[sweller-s-2010-reconceptualization]]                          ║
╚══════════════════════════════════════════════════════════════════════╝

1988 ────────────────── 1994 ──────────────── 2010 ──────────────► Now
  │                      │                     │
  │ CLT founded          │ Three-load          │ GERMANE LOAD
  │ (Sweller 1988)       │ taxonomy            │ RECONCEIVED
  │ WM/LTM asymmetry     │ formalised          │ (Sweller 2010)
  │ as core constraint   │                     │

══════════════════════ BEFORE 2010 ═══════════════════════════════════

  Original conception: THREE DISTINCT LOAD TYPES

  ┌─────────────┐   ┌──────────────┐   ┌─────────────────────────┐
  │  INTRINSIC  │ + │  EXTRANEOUS  │ + │       GERMANE           │
  │  (material) │   │  (bad design)│   │  (schema construction   │
  │             │   │              │   │   effort — SEPARATE     │
  │             │   │              │   │   type)                 │
  └─────────────┘   └──────────────┘   └─────────────────────────┘
         │                 │                        │
         └─────────────────┴────────────────────────┘
                           │
                    Total WM Load
                    (three additive components)

  DESIGN IMPLICATION (pre-2010):
  Add germane load on top of managed intrinsic + minimal extraneous

══════════════════════ AFTER 2010 ════════════════════════════════════

  Reconceived conception: TWO LOAD TYPES + ONE QUALITY DIMENSION

  ┌─────────────────────┐   ┌──────────────────────────────────────┐
  │    INTRINSIC        │ + │           EXTRANEOUS                 │
  │  (material)         │   │         (bad design)                 │
  │                     │   │                                      │
  │  ┌───────────────┐  │   │                                      │
  │  │ Productive ←──┼──┼───┼── Schema construction = GERMANE      │
  │  │ portion       │  │   │   = intrinsic load well spent        │
  │  └───────────────┘  │   │                                      │
  └─────────────────────┘   └──────────────────────────────────────┘
           │                               │
           └───────────────────────────────┘
                         │
                  Total WM Load
                  (two types; germane is quality
                   of intrinsic, not a third type)

  DESIGN IMPLICATION (post-2010):
  You CANNOT add germane load.
  You CAN redirect intrinsic load toward schema construction
  by eliminating extraneous load and supporting effortful practice.

══════════════════════ WHY THIS MATTERS ═════════════════════════════

  ┌──────────────────────────────────────────────────────────────┐
  │ PRE-2010 error risk: Instructors add "germane-load-inducing" │
  │ activities on top of existing load → overload               │
  │                                                              │
  │ POST-2010 logic: The instructional target is not additive.  │
  │ Eliminate extraneous → freed capacity available for         │
  │ schema-constructive processing of intrinsic load.           │
  └──────────────────────────────────────────────────────────────┘

Source: §The Three-Load Taxonomy; §The Evolution of Germane Load
```

**Reading guide:** Read left-to-right chronologically, then compare the two structural diagrams. The shift from 2010 is subtle but consequential: the three-box additive model is replaced by a two-box model where "germane" describes the quality of how intrinsic load is processed, not a separate load to be added. The "Why This Matters" box at the bottom makes the practical stakes explicit — the pre-2010 model actively encouraged a design error. The linked notes [[the-evolution-of-germane-load]] and [[sweller-s-2010-reconceptualization]] contain the primary theoretical source material.

**Source:** §The Three-Load Taxonomy; [[sweller-s-2010-reconceptualization]]

---

## Visual Aid 8: Evolutionary Foundations — Contrast Panel

**Purpose:** Maps the biological primary / secondary knowledge distinction and explains why formal instruction exists and what CLT predicts about spontaneous versus taught knowledge.

```
╔══════════════════════════════════════════════════════════════════════╗
║    EVOLUTIONARY FOUNDATIONS — KNOWLEDGE TYPE CONTRAST               ║
║    [[biological-primary-knowledge]] [[biological-secondary-         ║
║    knowledge]] [[evolutionary-educational-psychology]]              ║
╚══════════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────┬─────────────────────────────────┐
│  BIOLOGICALLY PRIMARY           │  BIOLOGICALLY SECONDARY         │
│  KNOWLEDGE                      │  KNOWLEDGE                      │
├─────────────────────────────────┼─────────────────────────────────┤
│ ORIGIN:                         │ ORIGIN:                         │
│ Evolutionary lineage prepared   │ Cultural construction;          │
│ us to acquire this knowledge    │ recent in evolutionary time     │
│ through normal experience       │                                 │
├─────────────────────────────────┼─────────────────────────────────┤
│ EXAMPLES:                       │ EXAMPLES:                       │
│ • Social intelligence           │ • Reading and writing           │
│ • Basic face recognition        │ • Mathematics                   │
│ • Intuitive physics             │ • Systematic science            │
│ • Basic spoken language         │ • Formal logic                  │
│ • Facial emotion reading        │ • Historical reasoning          │
├─────────────────────────────────┼─────────────────────────────────┤
│ HOW ACQUIRED:                   │ HOW ACQUIRED:                   │
│ Spontaneously through           │ ONLY through explicit           │
│ normal environmental            │ intentional instruction         │
│ exposure; no teaching           │ in dedicated settings           │
│ required                        │                                 │
├─────────────────────────────────┼─────────────────────────────────┤
│ CLT IMPLICATION:                │ CLT IMPLICATION:                │
│ Instruction not needed;         │ Instruction is NECESSARY —      │
│ natural selection wired         │ natural selection has NOT       │
│ acquisition mechanisms          │ wired acquisition mechanisms    │
│ already                         │                                 │
├─────────────────────────────────┼─────────────────────────────────┤
│ COGNITIVE LOAD:                 │ COGNITIVE LOAD:                 │
│ Low — evolved dedicated         │ High — must be acquired via     │
│ learning pathways for           │ general WM/LTM architecture     │
│ these domains                   │ without evolutionary support    │
└─────────────────────────────────┴─────────────────────────────────┘

               WHY SCHOOLS EXIST (CLT's evolutionary argument):
  ┌──────────────────────────────────────────────────────────────┐
  │ Biologically secondary knowledge is what schools primarily   │
  │ teach. Because natural selection has not prepared humans to  │
  │ spontaneously acquire reading, mathematics, or systematic    │
  │ science, intentional instructional environments with CLT-    │
  │ informed design are required to facilitate schema            │
  │ construction in the absence of evolutionary scaffolding.     │
  └──────────────────────────────────────────────────────────────┘

  NOTE: The distinction also explains differential difficulty.
  "Why is learning to talk easy but learning to read hard?"
  → Talk = primary; Read = secondary.

Source: §Evolutionary Foundations
```

**Reading guide:** The contrast panel is deliberately symmetrical so the structural difference is immediately visible. The most practically useful row is "How Acquired" — it defines the scope condition for CLT-informed instruction: CLT is primarily relevant to biologically secondary knowledge, because primary knowledge requires no instruction. The "Why Schools Exist" synthesis box provides the evolutionary rationale for formal education itself, grounding CLT in a broader intellectual framework. The final note connects the abstract distinction to a concrete intuitive puzzle.

**Source:** §Evolutionary Foundations; [[biological-primary-knowledge]]; [[biological-secondary-knowledge]]

---

## Visual Aid 9: Before / After Design Transformation Panel

**Purpose:** Shows the concrete instructional design transformation that CLT mandates, mapping "what poor design looks like" directly to "what CLT-informed design looks like" for each major principle.

```
╔══════════════════════════════════════════════════════════════════════╗
║     CLT DESIGN TRANSFORMATION — BEFORE / AFTER                      ║
╚══════════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────┬──────────────────────────────────┐
│  ✗ POOR DESIGN (High            │  ✓ CLT-INFORMED DESIGN           │
│    Extraneous Load)             │    (Extraneous Load Minimised)   │
├─────────────────────────────────┼──────────────────────────────────┤
│ WORKED EXAMPLES:                │ WORKED EXAMPLES:                 │
│ Present problem, ask student    │ Study the worked solution first; │
│ to solve from scratch; no       │ move to problem-solving only     │
│ solution exposure first         │ after schema seeds are present   │
├─────────────────────────────────┼──────────────────────────────────┤
│ SPLIT ATTENTION:                │ PHYSICAL INTEGRATION:            │
│ Diagram on one side of page;   │ Labels embedded directly in      │
│ explanatory text across the     │ the diagram; no need to cross-   │
│ room on the board               │ reference between sources        │
├─────────────────────────────────┼──────────────────────────────────┤
│ MODALITY:                       │ DUAL MODALITY:                   │
│ Complex visual with dense       │ Complex visual narrated with     │
│ on-screen caption text          │ audio; phonological loop +       │
│ explaining same content         │ visuospatial sketchpad both used │
├─────────────────────────────────┼──────────────────────────────────┤
│ REDUNDANCY:                     │ COHERENCE:                       │
│ Self-explanatory diagram PLUS   │ Remove the text. The diagram     │
│ paragraph explaining same       │ suffices. Adding text generates  │
│ diagram for "completeness"      │ redundancy load.                 │
├─────────────────────────────────┼──────────────────────────────────┤
│ EXPERTISE MISMATCH:             │ ADAPTIVE FADING:                 │
│ Same fully-worked example       │ Full examples for novices;       │
│ sheet for all students          │ progressive removal of steps     │
│ regardless of prior knowledge   │ as competence develops           │
├─────────────────────────────────┼──────────────────────────────────┤
│ SEDUCTIVE DETAILS:              │ COHERENCE PRINCIPLE:             │
│ Interesting historical          │ Every element must justify its   │
│ anecdote embedded in           │ presence by contributing to      │
│ technical explanation           │ learning goals. Fascinating ≠   │
│ "to engage learners"            │ instructionally relevant.        │
├─────────────────────────────────┼──────────────────────────────────┤
│ SEQUENCING:                     │ ISOLATION → INTEGRATION:         │
│ Present fully integrated        │ Teach interacting elements       │
│ complex task to novices         │ in isolation before combining    │
│ on first exposure               │ into whole-task context          │
└─────────────────────────────────┴──────────────────────────────────┘

 UNIFYING PRINCIPLE:
 ┌──────────────────────────────────────────────────────────────┐
 │ Every ✗ pattern generates extraneous load.                   │
 │ Every ✓ pattern eliminates extraneous load and redirects    │
 │ the freed WM capacity toward schema construction.           │
 └──────────────────────────────────────────────────────────────┘

Source: §The Instructional Effects Catalogue; all effect notes
```

**Reading guide:** Each row is a self-contained before/after transformation for one CLT principle. The left column represents how instructions are commonly designed without CLT awareness; the right column shows the CLT-mandated alternative with a brief mechanism note. The unifying principle box at the bottom confirms that all seven transformations share a single causal logic: eliminate extraneous load; free WM for schema construction. This panel is the most practitioner-facing aid in the suite and is designed for direct reference during instructional design work.

**Source:** §The Instructional Effects Catalogue

---

## Visual Aid 10: TL;DR Scorecard

**Purpose:** One-panel synthesis giving the thesis, strongest claims, open questions, and reading guidance.

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                  CLT MOC — REPORT SCORECARD                             ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  THESIS       Learning is schema construction through a 4-slot WM       ║
║               bottleneck; all CLT design principles follow from         ║
║               this single architectural constraint.                     ║
║                                                                          ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  STRONGEST    1. Worked example effect — most replicated finding;       ║
║  EVIDENCE        direct WM load mechanism confirmed                     ║
║               2. Split-attention effect — physical integration          ║
║                  benefit well established                               ║
║               3. Modality effect — dual-channel WM architecture         ║
║                  exploited in narration > caption design                ║
║                                                                          ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  THEORETICAL  2010 germane load reconceptualisation:                    ║
║  KEY MOVE     Germane ≠ a third type to add.                            ║
║               Germane = intrinsic load productively processed.          ║
║               Design target: eliminate extraneous → redirect freed      ║
║               capacity into schema construction.                        ║
║                                                                          ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  OPEN         • No gold-standard WM load measurement tool               ║
║  QUESTIONS    • Germane vs. intrinsic still hard to distinguish         ║
║               • Scaling CLT lab findings to complex real-world          ║
║                 professional learning unresolved                        ║
║               • Isolated elements vs. whole-task tension                ║
║                 (resolved in principle; hard in practice)               ║
║                                                                          ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  READ IF...   You design instruction, create learning materials,        ║
║               study educational psychology, or want to understand       ║
║               why "less is more" in instructional design.               ║
║                                                                          ║
║  SKIP IF...   You need curriculum theory without a WM constraint        ║
║               focus, or you are working purely with expert learners     ║
║               where CLT novice-phase prescriptions don't apply.         ║
║                                                                          ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  COMPANION    [[MOC - Memory Science]]    ← WM architecture detail      ║
║  MOCS         [[MOC - Learning Science]]  ← CLT in broader ecology      ║
║               [[MOC - Metacognition and Self-Regulated Learning]]       ║
║                  ← Expertise reversal × adaptive self-regulation        ║
║                                                                          ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

## Synthesis Packet

**Top 5 takeaways:**

1. The entire theory rests on one structural fact: WM holds ~4 items; LTM is unlimited and schema-organised. Every CLT design principle is a downstream implication of this asymmetry — not a collection of independent empirical rules.

2. "Germane load" changed meaning in 2010. It is not a third type of load to add to your design; it is a description of intrinsic load being used well. The design move is to eliminate extraneous load, freeing WM for schema-constructive processing of intrinsic load.

3. The expertise reversal effect is the most practically consequential finding: instruction optimised for novices actively impairs experts. Every scaffolded design must be designed to disappear as competence grows.

4. 4C/ID extends CLT from single-task laboratory findings to curriculum-level complex skill design, with the whole-task principle as its philosophical core: decompose for load management, but always return to integrated whole-task performance.

5. The evolutionary foundation explains CLT's domain scope: it is most relevant to biologically secondary knowledge (reading, mathematics, systematic reasoning) — the knowledge that requires explicit instruction precisely because evolution did not wire us for it.

**Navigator — which aid answers which question:**

- "What is the fundamental constraint?" → Aid 1 (Causal Architecture Map)
- "What are the three load types and how do I distinguish them?" → Aid 2 (Taxonomy Matrix)
- "Why does the same content feel easier for experts?" → Aid 3 (Element Interactivity Spectrum)
- "What design effects have empirical support?" → Aid 4 (Effects Catalogue)
- "Why do worked examples eventually backfire?" → Aid 5 (Expertise Reversal Flow)
- "What is 4C/ID and how does it extend CLT?" → Aid 6 (4C/ID Architecture)
- "What changed in 2010 about germane load?" → Aid 7 (Evolution Timeline)
- "Why does CLT apply to reading but not walking?" → Aid 8 (Evolutionary Contrast)
- "What does CLT-informed redesign look like in practice?" → Aid 9 (Before/After Panel)
- "What are the open questions and is this worth reading?" → Aid 10 (Scorecard)

**PKB vault links woven throughout:** [[Cognitive-Load-Theory]], [[Working-Memory]], [[Long-Term-Memory]], [[Schema]], [[Schema-Construction]], [[Schema-Automation]], [[Intrinsic-Cognitive-Load]], [[Extraneous-Cognitive-Load]], [[Germane-Cognitive-Load]], [[Element-Interactivity]], [[Expertise-Reversal-Effect]], [[Worked-Examples]], [[Split-Attention-Effect]], [[Modality-Effect]], [[Redundancy-Effect]], [[Four-Component-Instructional-Design]], [[Deliberate-Practice]], [[Desirable-Difficulties]], [[Instructional-Design]], [[Cognitive-Architecture]]