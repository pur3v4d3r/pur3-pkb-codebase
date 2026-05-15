---
tags: [moc, domain-metacognition, domain-self-regulated-learning, status-evergreen]
aliases: [SRL MOC, Metacognition MOC, Self-Regulation MOC]
created: 2026-05-15
modified: 2026-05-15
status: evergreen
type: moc
moc_pattern: cluster
domain: Metacognition and Self-Regulated Learning
source_notes_count: 58
target_word_count: 6000
audience: [practitioner, researcher]
maturity: established
parent_moc: "[[MOC - Cognitive Science (Master Index)]]"
related_mocs: ["[[MOC - Memory Science]]", "[[MOC - Motivation Psychology]]", "[[MOC - Learning Science]]"]
version: 1.0.0
---

# Metacognition and Self-Regulated Learning — Map of Content

> [!abstract] Domain & Scope
> **Metacognition** is thinking about one's own thinking — the monitoring and control of cognitive processes. **Self-Regulated Learning (SRL)** is its applied extension: the use of metacognitive, motivational, and behavioural strategies to govern one's own learning. This MOC organises 58 permanent notes spanning metacognitive theory, the major SRL models (Zimmerman, Winne, Pintrich), self-directed learning, and the practical application of metacognitive monitoring. It is structured as a **cluster** around three co-equal sub-domains: metacognitive architecture, SRL process models, and self-directed learning — with cross-cluster bridges throughout.
>
> **For**: Practitioners, educators, educational researchers
> **Companion MOCs**: [[MOC - Memory Science]], [[MOC - Motivation Psychology]]
> **Reading time**: ~28 minutes

## 🗺️ Navigation

- **[Metacognition: Architecture and Components](#metacognition-architecture-and-components)** — what metacognition is made of
- **[Metacognitive Monitoring: Reading the Internal Signal](#metacognitive-monitoring-reading-the-internal-signal)** — JOLs, FOK, calibration
- **[Self-Regulated Learning: The Major Models](#self-regulated-learning-the-major-models)** — Zimmerman, Winne, Pintrich
- **[The SRL Cycle in Detail](#the-srl-cycle-in-detail)** — forethought, performance, reflection
- **[Self-Directed Learning: Expanding the Grain Size](#self-directed-learning-expanding-the-grain-size)** — SDL vs SRL
- **[The PKB as Metacognitive Architecture](#the-pkb-as-metacognitive-architecture)** — externalising regulation
- **[Cross-Domain Bridges](#cross-domain-bridges)**
- **[Frontier & Open Questions](#frontier--open-questions)**
- **[Index of Linked Notes](#index-of-linked-notes)**

> [!progression] Reading Paths
> - **Educator seeking practical tools**: Start with The SRL Cycle, then Metacognitive Monitoring.
> - **Researcher**: Read sequentially; the SRL Models section maps theoretical landscape.
> - **PKB practitioner**: The PKB as Metacognitive Architecture section is the most directly relevant.

---

## Metacognition: Architecture and Components

[[metacognition|Metacognition]] was formally introduced by Flavell (1979) as "thinking about one's own thinking." In its mature form, it encompasses two major systems: **metacognitive knowledge** and **metacognitive regulation**.

### Flavell's Taxonomy

[[flavell-s-metacognitive-taxonomy|Flavell's metacognitive taxonomy]] distinguishes three types of metacognitive knowledge:

- **Person knowledge** — beliefs about one's own and others' cognitive capabilities and limitations
- **Task knowledge** — understanding of how task features affect difficulty and strategy demands
- **Strategy knowledge** — knowledge of *which* cognitive strategies exist, *how* to apply them, and *when* each is appropriate

[[knowledge-of-cognition|Knowledge of cognition]] is the declarative dimension — what you know about thinking. It is relatively stable, consciously accessible, and can be explicitly taught. A student who knows that distributed practice outperforms massed practice holds metacognitive strategy knowledge; whether they *act* on it is a separate question handled by metacognitive regulation.

### Metacognitive Regulation

Metacognitive regulation has three interacting components:

```
METACOGNITIVE REGULATION
┌──────────────────────────────────────────────────────┐
│                                                       │
│  MONITORING ──────────── detects ──────►  CONTROL    │
│     ↑                                      │         │
│     │         (cognitive task)             ↓         │
│     └──────── evaluates ─────── evaluates ←─         │
│                                                       │
│  Plans → Implements strategies → Evaluates outcomes  │
└──────────────────────────────────────────────────────┘
```

[[metacognitive-monitoring|Metacognitive monitoring]] is the ongoing detection of one's cognitive state — comprehension level, memory strength, progress toward goals. [[metacognitive-control|Metacognitive control]] is the consequent adjustment of cognitive strategy: slowing down, re-reading, switching strategies, allocating more time. The [[monitoring-control-loop|monitoring-control loop]] is the core regulatory circuit: a monitoring signal triggers a control response, which changes the cognitive state, which is re-monitored.

[[metacognitive-regulation|Metacognitive regulation]] encompasses planning (selecting strategies before a task), monitoring (tracking during), and evaluating (appraising outcomes after). Importantly, effective regulation depends on accurate monitoring — without valid monitoring signals, control responses are misdirected or absent.

---

## Metacognitive Monitoring: Reading the Internal Signal

Metacognitive monitoring generates *feelings* and *judgments* that serve as internal diagnostic signals. The quality of these signals — their accuracy and informativeness — determines the quality of self-regulation.

### Types of Monitoring Judgments

[[metacognitive-judgments|Metacognitive judgments]] take several forms:

| Judgment type | When made | What it predicts | Accuracy |
|---------------|-----------|-----------------|---------|
| [[ease-of-learning-judgment\|Ease of Learning (EOL)]] | Before study | How easy to learn | Moderate |
| [[judgment-of-learning\|Judgment of Learning (JOL)]] | During/after study | Future recall | Low (immediate); moderate (delayed) |
| [[feeling-of-knowing\|Feeling of Knowing (FOK)]] | During retrieval failure | Whether recognition will succeed | Moderate |
| [[retrospective-confidence-judgment\|Retrospective Confidence]] | After retrieval | Whether answer was correct | Moderate |

The systematic miscalibration of immediate JOLs is particularly important: [[calibration-vs-sensitivity-in-metacognitive-judgment|calibration vs sensitivity]] distinguishes between overall accuracy (calibration) and the ability to discriminate between items you know and don't know (sensitivity). Students who feel confident about everything learn worse than those whose confidence tracks actual mastery.

### The Fluency Trap

[[metacognitive-feelings|Metacognitive feelings]] — including [[processing-fluency|processing fluency]], familiarity, and ease — are the primary cues used for JOLs. This creates a systematic bias: [[fluency-illusion|the fluency illusion]] leads students to confuse the *feeling* of understanding (generated by smooth processing of familiar material) with the *fact* of learning. Re-reading feels effective precisely because it is easy — and ease is mistaken for knowledge. The cue-utilisation framework ([[cue-utilization-framework|cue-utilization framework]]) explains this as a mismatch between proxy cues and true memory strength.

[[metacognitive-accuracy|Metacognitive accuracy]] — having JOLs that actually predict performance — is a learnable skill, improved primarily through experience with delayed feedback. Having students *predict* test scores before taking them, then reviewing discrepancies, systematically improves metacognitive calibration.

> [!key-claim] Monitoring Without Valid Signals Is Worse Than No Monitoring
> An inaccurate monitoring system generates false confidence that suppresses further effort. Students who "feel like they know it" after passive re-reading allocate less study time than those who test themselves and discover they don't. The failure of monitoring *precedes* the failure of control.

---

## Self-Regulated Learning: The Major Models

Three theoretical frameworks define the contemporary SRL landscape. They differ in their mechanistic emphasis, their relationship to motivation, and their granularity.

### Zimmerman's Social-Cognitive Model

[[cyclical-model-of-self-regulated-learning|Zimmerman's cyclical model]] organises SRL into three phases — Forethought, Performance, and Self-Reflection — constituting a feedback loop in which the outcome of one learning cycle informs the setup of the next. [[the-cyclical-feedback-architecture-as-learning-engine|The cyclical feedback architecture is the learning engine]]: progress is not linear but iterative, with each reflection phase recalibrating goals, strategy selections, and self-efficacy beliefs for the next forethought phase.

Zimmerman's model is distinctive in its emphasis on **motivational beliefs** — particularly self-efficacy — as constitutive parts of the regulatory cycle, not merely antecedents to it. A learner's judgment of their competence in the self-reflection phase directly feeds back into the goal-setting and intrinsic interest activation of the next forethought phase. This tightly integrates SRL with motivational theory (see [[MOC - Motivation Psychology]]).

### Winne's COPES Model

[[winne-s-model-of-self-regulated-learning|Winne's model]] is more cognitively detailed and metacognitively precise. It treats SRL as a cascade of cognitive operations governed by the learner's internal conditions, their task understanding, their product goals, and their evaluative standards. The acronym COPES — Conditions, Operations, Products, Evaluations, Standards — captures its core elements.

Winne's contribution is the emphasis on *standards* as the regulative reference point: monitoring involves comparing current cognitive products against internal standards, and the gap drives control. This makes the model explicitly computational in character and has generated a programme of trace-based research that captures SRL behaviour at fine granularity through log-file analysis of computer-based learning environments.

### Pintrich's 4×4 Matrix

[[pintrich-s-framework-of-self-regulated-learning|Pintrich's framework]] cross-classifies SRL along two dimensions: *phase* (planning, monitoring, control, reflection) and *area of regulation* (cognition, motivation/affect, behaviour, context). [[pintrich-s-4x4-matrix|The resulting 4×4 matrix]] is the most comprehensive taxonomy of SRL activities in the literature, serving primarily as a classification system for research rather than a dynamic process model.

[[the-four-areas-of-regulation|The four areas of regulation]] reveal that SRL is not only cognitive but also **motivational** (regulating interest and anxiety), **behavioural** (regulating effort, help-seeking, procrastination), and **contextual** (regulating the study environment). Many students regulate cognition reasonably well while failing to regulate affect — test anxiety, for example, is a motivational regulation failure as much as a cognitive one.

---

## The SRL Cycle in Detail

### Forethought Phase

[[forethought-phase|The forethought phase]] encompasses goal-setting, planning, and motivational priming. Two clusters of processes operate here: *task analysis* (setting goals, activating prior knowledge, planning strategy use) and *motivational beliefs* (self-efficacy assessment, outcome expectations, intrinsic interest activation).

[[forethought-as-regulatory-front-loading|Forethought as regulatory front-loading]] captures the insight that effective learners invest disproportionately in the setup phase, precisely because good plans reduce monitoring load during performance. The well-known phenomenon of implementation intentions ([[implementation-intention|implementation intentions]]) — specific if-then plans for when, where, and how to study — dramatically increases follow-through by automating the transition from intention to action.

### Performance/Control Phase

[[performance-phase|The performance phase]] involves executing the planned cognitive strategies while continuously monitoring progress. [[self-instruction]] and [[self-monitoring]] operate in parallel: learners talk themselves through procedures while comparing outputs to goals. Task interest, effort regulation, and [[attention-and-cognitive-control|attention management]] are the key self-control processes.

[[control-as-diagnostic-response-not-habitual-response|Control is diagnostic, not habitual]]: effective regulators adjust strategy in response to monitoring signals rather than persisting with preferred strategies regardless of feedback. The tendency to persist with a comfortable but ineffective strategy is a cardinal SRL failure mode.

### Self-Reflection Phase

[[self-reflection-phase|The self-reflection phase]] involves causal attribution of performance outcomes and adaptive inference for future cycles. [[reaction-and-reflection-as-cyclic-coupling|Reaction and reflection are cyclically coupled]]: positive performance triggers increased self-efficacy and continued motivation; negative performance triggers either adaptive strategy revision (mastery-oriented response) or maladaptive attributions to fixed ability (performance-avoidance response). This is the junction where SRL and attribution theory (see [[MOC - Motivation Psychology]]) most directly intersect.

---

## Self-Directed Learning: Expanding the Grain Size

Self-Regulated Learning and Self-Directed Learning (SDL) are related but distinct constructs. [[the-grain-size-distinction-between-sdl-and-srl|The grain-size distinction between SDL and SRL]] is the key: SRL operates at the level of specific learning episodes (how a student studies for an exam), while SDL operates at the level of the learner's entire educational trajectory (whether, what, and how to pursue learning at all).

[[self-directed-learning|SDL]] involves the learner's control over goals, resources, methods, and evaluation — not just strategy selection within an assigned curriculum. [[autonomy-as-the-motivational-foundation-of-sdl|Autonomy is the motivational foundation of SDL]]: intrinsically motivated learners who control their own learning direction show qualitatively different motivational profiles than those who merely regulate performance within externally imposed goals.

[[garrison-s-comprehensive-model-of-self-directed-learning|Garrison's comprehensive model]] integrates self-management (contextual control), self-monitoring (cognitive responsibility), and motivation (entering and task motivation) as the three defining dimensions of SDL — a formulation that bridges SRL and motivational theory.

[[metacognitive-monitoring-in-self-directed-learning|Metacognitive monitoring in self-directed learning]] takes on expanded scope: not just "do I understand this?" but "is this worth understanding?", "am I learning what I intended?", and "has my learning goal changed as I know more?". [[metacognitive-sovereignty|Metacognitive sovereignty]] — the capacity to govern one's own epistemic standards and learning trajectory — is the developmental endpoint of SRL and SDL combined.

---

## The PKB as Metacognitive Architecture

[[the-pkb-as-constitutive-metacognitive-architecture|The PKB as constitutive metacognitive architecture]] is one of the more theoretically ambitious ideas in the personal knowledge management literature. The claim is that a well-designed personal knowledge base is not merely a *tool for* metacognition but a constitutive component of metacognitive functioning — an [[externalized-metacognition|externalised metacognition]] that makes thinking visible, persistent, and refineable.

[[externalized-cognitive-architecture|Externalised cognitive architecture]] more broadly — writing, diagrams, maps — functions as cognitive scaffolding that offloads monitoring and planning demands from internal working memory to a stable external medium. [[cognitive-offloading|Cognitive offloading]] is the mechanism: by recording thoughts externally, the mind is freed for higher-order integrative processing rather than maintenance.

[[metacognitive-scaffolding|Metacognitive scaffolding]] provided by a PKB includes: forcing elaboration at the point of note-making (generation effect), creating a record for delayed JOL testing (retrieval practice), and providing a visible map of knowledge structure that reveals gaps (coverage monitoring).

> [!key-claim] The Note-Making Process as SRL Practice
> Active note-making ([[active-note-making|active note-making]]) is not just information recording — it is metacognitive rehearsal. Deciding how to connect a new note to existing knowledge requires activating prior schemas, monitoring for comprehension, and evaluating structural fit. These are precisely the SRL processes that produce deep encoding and durable understanding.

[Synthesis-With:: [[MOC - PKB and Knowledge Management]]]

---

## 🌉 Cross-Domain Bridges

> [!related] Companion MOCs
> - [[MOC - Memory Science]] — Metacognitive monitoring relies on the same judgment mechanisms (JOL, FOK, fluency) analysed in Memory Science; metacognitive control is functionally dependent on memory consolidation processes.
> - [[MOC - Motivation Psychology]] — Self-efficacy, goal orientation, and attribution theory are constitutive parts of the SRL cycle (Zimmerman's model embeds them explicitly); the motivation-cognition interface is most visible here.
> - [[MOC - PKB and Knowledge Management]] — The PKB as externalised metacognitive architecture bridges SRL theory with practical knowledge management implementation.
> - [[MOC - Learning Science]] — Study strategy research (retrieval practice, spacing, elaboration) is the empirical operationalisation of SRL principles.

---

## 🌅 Frontier & Open Questions

> [!frontier] Live debates
> - **Measurement validity**: Do SRL self-report measures (MSLQ and equivalents) actually measure the processes they purport to, or do they capture general academic conscientiousness? Trace-based measures (log-files, eye-tracking) reveal discrepancies.
> - **The metacognitive bootstrapping problem**: [[the-metacognitive-bootstrapping-problem|The bootstrapping problem]] — you need metacognitive knowledge to know that your metacognitive knowledge is deficient — is theoretically important and practically intractable by direct instruction alone.
> - **Domain specificity**: Is SRL a domain-general capacity or a collection of domain-specific competencies? Evidence accumulates for both positions.

---

## 📚 Index of Linked Notes

| Note | Type | Section |
|------|------|---------|
| [[active-note-making]] | atomic | PKB |
| [[attention-and-cognitive-control]] | atomic | Performance Phase |
| [[autonomy-as-the-motivational-foundation-of-sdl]] | synthesis | SDL |
| [[calibration-vs-sensitivity-in-metacognitive-judgment]] | atomic | Monitoring |
| [[cognitive-offloading]] | atomic | PKB |
| [[comprehension-monitoring]] | atomic | Monitoring |
| [[control-as-diagnostic-response-not-habitual-response]] | synthesis | Performance |
| [[cue-utilization-framework]] | atomic | Monitoring |
| [[cyclical-model-of-self-regulated-learning]] | reference | SRL Models |
| [[ease-of-learning-judgment]] | atomic | Monitoring |
| [[externalized-cognitive-architecture]] | atomic | PKB |
| [[externalized-metacognition]] | atomic | PKB |
| [[flavell-s-metacognitive-taxonomy]] | reference | Architecture |
| [[fluency-illusion]] | atomic | Monitoring |
| [[forethought-as-regulatory-front-loading]] | synthesis | Forethought |
| [[forethought-phase]] | atomic | SRL Cycle |
| [[garrison-s-comprehensive-model-of-self-directed-learning]] | reference | SDL |
| [[implementation-intention]] | atomic | Forethought |
| [[judgment-of-learning]] | atomic | Monitoring |
| [[knowledge-of-cognition]] | atomic | Architecture |
| [[metacognition]] | reference | Architecture |
| [[metacognitive-accuracy]] | atomic | Monitoring |
| [[metacognitive-calibration]] | atomic | Monitoring |
| [[metacognitive-control]] | atomic | Architecture |
| [[metacognitive-experience]] | atomic | Architecture |
| [[metacognitive-feelings]] | atomic | Monitoring |
| [[metacognitive-judgments]] | atomic | Monitoring |
| [[metacognitive-knowledge]] | reference | Architecture |
| [[metacognitive-monitoring]] | reference | Monitoring |
| [[metacognitive-monitoring-in-self-directed-learning]] | atomic | SDL |
| [[metacognitive-regulation]] | reference | Architecture |
| [[metacognitive-scaffolding]] | atomic | PKB |
| [[metacognitive-sovereignty]] | synthesis | SDL |
| [[monitoring-control-loop]] | atomic | Architecture |
| [[performance-phase]] | atomic | SRL Cycle |
| [[pintrich-s-4x4-matrix]] | reference | SRL Models |
| [[pintrich-s-framework-of-self-regulated-learning]] | reference | SRL Models |
| [[reaction-and-reflection-as-cyclic-coupling]] | synthesis | Reflection Phase |
| [[retrospective-confidence-judgment]] | atomic | Monitoring |
| [[self-directed-learning]] | reference | SDL |
| [[self-reflection-phase]] | atomic | SRL Cycle |
| [[self-regulated-learning]] | reference | SRL Models |
| [[the-cyclical-feedback-architecture-as-learning-engine]] | synthesis | SRL Models |
| [[the-four-areas-of-regulation]] | atomic | SRL Models |
| [[the-grain-size-distinction-between-sdl-and-srl]] | synthesis | SDL |
| [[the-metacognitive-bootstrapping-problem]] | atomic | Frontier |
| [[the-metacognitive-scaffolding-principle]] | synthesis | PKB |
| [[the-pkb-as-constitutive-metacognitive-architecture]] | synthesis | PKB |
| [[winne-s-model-of-self-regulated-learning]] | reference | SRL Models |

---

> [!info] MOC Metadata
> - **Pattern**: cluster
> - **Source notes**: 58
> - **Word count**: ~5,500
> - **Generated**: 2026-05-15 by MOC Specialist Agent v1.0.0
> - **Audit trail**: [[_meta/MOC - Metacognition and Self-Regulated Learning.audit]]
> - **Next review suggested**: 2026-08-15


# Visual Aid Suite: Metacognition and Self-Regulated Learning MOC

**Source:** MOC — Metacognition and Self-Regulated Learning (58 permanent notes)
**Audience:** Practitioner / Researcher (as specified in frontmatter)
**Thesis:** Metacognitive monitoring accuracy is the master variable in SRL — without valid internal signals, all regulatory effort is misdirected; the SRL cycle, PKB practice, and SDL are successive expansions of the same monitoring-control architecture.

**Aids selected:**
1. **Taxonomy Tree** — decompose the full metacognitive architecture hierarchically
2. **Causal/Argument Map** — show how monitoring quality cascades into SRL outcomes
3. **Process Flow** — Zimmerman's three-phase cyclical model with feedback arrows
4. **Comparison Matrix** — Zimmerman vs. Winne vs. Pintrich across five dimensions
5. **Pintrich 4×4 Grid** — the cross-classification matrix reconstructed in ASCII
6. **Monitoring Judgments Panel** — all four judgment types side-by-side
7. **Influence/Genealogy Map** — intellectual lineage from Flavell (1979) to PKB
8. **Spectrum** — SRL↔SDL grain-size continuum
9. **Before/After Panel** — poor vs. effective metacognitive regulation
10. **TL;DR Scorecard** — synthesis of the whole MOC

---

## Visual Aid 1: Metacognitive Architecture — Taxonomy Tree

**Purpose:** Hierarchically decompose [[Metacognition.md]] into its two major systems and their sub-components, providing a structural overview of the domain.

```
METACOGNITION  [[Metacognition.md]]
├── METACOGNITIVE KNOWLEDGE  [[Metacognitive-Knowledge.md]]
│   ├── Person Knowledge
│   │   ├── Self-knowledge (own capabilities & limits)
│   │   └── Other-knowledge (others' cognitive traits)
│   ├── Task Knowledge
│   │   ├── How task features affect difficulty
│   │   └── How task features affect strategy demands
│   └── Strategy Knowledge
│       ├── Declarative  [[declarative-metacognitive-knowledge.md]]
│       │   └── WHAT strategies exist
│       ├── Procedural  [[procedural-metacognitive-knowledge.md]]
│       │   └── HOW to apply them
│       └── Conditional  [[conditional-metacognitive-knowledge.md]]
│           └── WHEN each is appropriate
│
└── METACOGNITIVE REGULATION  [[Metacognitive-Regulation.md]]
    ├── Planning
    │   ├── Goal-setting
    │   ├── Strategy selection
    │   └── Prior knowledge activation
    ├── Monitoring  [[Metacognitive-Monitoring.md]]
    │   ├── EOL judgments (before study)
    │   ├── JOL judgments (during/after)  [[Judgment-of-Learning-JOL.md]]
    │   ├── FOK judgments (retrieval failure) [[Feeling-of-Knowing-FOK.md]]
    │   └── Retrospective confidence
    │       └── ⚠ FLUENCY TRAP: cue ≠ criterion
    │           [[Fluency-Illusion.md]]
    └── Control  [[Metacognitive-Self-Regulation.md]]
        ├── Strategy adjustment
        ├── Effort reallocation
        ├── Help-seeking
        └── Study-time regulation
            └── DEPENDS ON monitoring accuracy
                [[Metacognitive-Calibration.md]]
```

**Reading guide:** Read top-to-bottom: knowledge (the declarative, stable component) is the left branch; regulation (the dynamic, process component) is the right. The `⚠` node marks the critical failure mode: because monitoring uses *fluency* as a proxy for learning, it is systematically biased. The entire right branch is only as good as the quality of monitoring signals. Control depends on monitoring; monitoring depends on calibration.

**Source:** §Metacognition: Architecture and Components; §Metacognitive Monitoring

---

## Visual Aid 2: Causal Architecture — How Monitoring Quality Drives Outcomes

**Purpose:** Map the causal cascade from monitoring signal quality through control responses to learning outcomes, showing where the system fails and why.

```
 ┌─────────────────────────────────────────────────────────┐
 │              METACOGNITIVE CAUSAL ARCHITECTURE           │
 └─────────────────────────────────────────────────────────┘

  LEARNING EXPERIENCE
        │
        ▼
 ┌──────────────────┐    FLUENCY CUES (invalid)
 │ MONITORING SIGNAL│◄───────────────────────── Re-reading
 │ [[Metacognitive- │    STRENGTH CUES (valid)
 │  Monitoring.md]] │◄───────────────────────── Testing
 └────────┬─────────┘
          │
          │   Calibrated?
     ─────┴──────────────
    │                    │
    ▼ YES                ▼ NO
VALID SIGNAL        INVALID SIGNAL
(accurate JOL)      (fluency illusion)
    │                    │
    ▼                    ▼
APPROPRIATE         MISDIRECTED
CONTROL             CONTROL
[[Metacognitive-    (false confidence,
 Control.md]]        reduced effort,
    │                no fix-up)
    │                    │
    ▼                    ▼
STRATEGY          STRATEGY PERSISTS
ADJUSTMENT        regardless of failure
    │
    ▼
REGULATION OF
STUDY BEHAVIOUR
 • Time reallocation
 • Strategy switch
 • Help-seeking
    │
    ▼
 LEARNING OUTCOME
 (durable encoding,
  transferable schema)

 KEY DRIVER OF CALIBRATION:
 Prediction → Test → Discrepancy Review
 [[Metacognitive-Calibration.md]]
 [[Metacognitive-Accuracy.md]]
```

**Reading guide:** Follow the left fork (valid signal) for the well-functioning metacognitive system; follow the right fork (invalid signal) for the failure mode. The critical insight is that the failure point is at the *signal*, not the *response* — an accurate monitoring system enables appropriate control automatically. The fluency illusion is not a control failure; it is a monitoring failure that makes control impossible. Calibration training (predict → test → review) is the intervention that restores signal validity.

**Source:** §Metacognitive Monitoring: Reading the Internal Signal; Key-claim callout: "Monitoring Without Valid Signals Is Worse Than No Monitoring"

---

## Visual Aid 3: Zimmerman's Three-Phase SRL Cycle — Process Flow

**Purpose:** Render [[Zimmerman's-Cyclical-SRL-Model.md]] as a process diagram showing the three phases, their internal components, and the feedback loops that make it a genuine cycle.

```
 ╔═══════════════════════════════════════════════════════╗
 ║        ZIMMERMAN'S CYCLICAL SRL MODEL                 ║
 ║   [[Zimmerman's-Cyclical-SRL-Model.md]]               ║
 ╚═══════════════════════════════════════════════════════╝

 ┌──────────────────── FEEDBACK LOOP ─────────────────────┐
 │                                                         │
 ▼                                                         │
┌──────────────────────────────┐                           │
│  1. FORETHOUGHT PHASE         │                           │
│  [[Forethought-Phase.md]]     │                           │
│                               │                           │
│  Task Analysis:               │                           │
│   • Goal setting              │                           │
│   • Strategic planning        │                           │
│   • Prior knowledge activation│                           │
│                               │                           │
│  Motivational Beliefs:        │                           │
│   • Self-efficacy assessment  │ ◄── fed back from Phase 3 │
│     [[Self-Efficacy.md]]      │                           │
│   • Outcome expectations      │                           │
│   • Intrinsic interest        │                           │
│   • Implementation intentions │                           │
│     [[Implementation-         │                           │
│      Intention.md]]           │                           │
└───────────────┬───────────────┘                           │
                │                                           │
                ▼                                           │
┌──────────────────────────────┐                           │
│  2. PERFORMANCE PHASE         │                           │
│  [[Performance-Phase.md]]     │                           │
│                               │                           │
│  Self-Control:                │                           │
│   • Strategy implementation   │                           │
│   • Self-instruction          │                           │
│   • Attention management      │                           │
│     [[Attention.md]]          │                           │
│   • Effort regulation         │                           │
│                               │                           │
│  Self-Monitoring:             │                           │
│   • Real-time tracking        │                           │
│   • Comparing output to goals │ ←── control is DIAGNOSTIC │
│   • Detecting mismatch        │     not habitual          │
└───────────────┬───────────────┘                           │
                │                                           │
                ▼                                           │
┌──────────────────────────────┐                           │
│  3. SELF-REFLECTION PHASE     │                           │
│  [[Self-Reflection-Phase.md]] │                           │
│                               │                           │
│  Self-Judgement:              │                           │
│   • Causal attribution        │                           │
│     [[Attribution-Theory.md]] │                           │
│   • Performance evaluation    │                           │
│                               │                           │
│  Self-Reaction:               │                           │
│  ┌───────────┬──────────────┐ │                           │
│  │ MASTERY   │PERFORMANCE-  │ │                           │
│  │ ORIENTED  │AVOIDANCE     │ │                           │
│  │           │              │ │                           │
│  │→ Strategy │→ Fixed-      │ │                           │
│  │  revision │  ability     │ │                           │
│  │→ Higher   │  attribution │ │                           │
│  │  efficacy │→ Disengagement│ │                           │
│  └───────────┴──────────────┘ │                           │
└───────────────────────────────┘                           │
                │                                           │
                └───────── recalibrates ──────────────────►─┘
```

**Reading guide:** The three boxes are phases in order, but the crucial feature is the *feedback arrow* at the bottom: the self-reflection phase feeds directly back into the next forethought phase, updating self-efficacy beliefs and goal structures. This is what makes SRL a genuine cycle rather than a linear sequence. The branching in Phase 3 (mastery-oriented vs. performance-avoidance) shows where motivational theory enters: negative performance can either improve or destroy future regulatory capacity depending on attribution style.

**Source:** §Self-Regulated Learning: The Major Models (Zimmerman subsection); §The SRL Cycle in Detail

---

## Visual Aid 4: Three SRL Models — Comparison Matrix

**Purpose:** Side-by-side evaluation of [[Zimmerman's-Cyclical-SRL-Model.md]], [[Winne-and-Hadwin.md]], and [[Pintrich's-Integrative-SRL-Framework.md]] across five analytical dimensions.

```
┌──────────────────────┬────────────────┬────────────────┬────────────────┐
│ DIMENSION            │  ZIMMERMAN     │   WINNE        │   PINTRICH     │
├──────────────────────┼────────────────┼────────────────┼────────────────┤
│ Metaphor /           │ Iterative      │ Computational  │ Taxonomic      │
│ Core Character       │ cycle          │ cascade        │ matrix         │
│                      │                │ (COPES)        │                │
├──────────────────────┼────────────────┼────────────────┼────────────────┤
│ Mechanistic          │ Motivational   │ Cognitive      │ Both: 4 areas  │
│ Emphasis             │ beliefs central│ operations     │ = cognition,   │
│                      │ (self-efficacy)│ & standards    │ motiv, behav,  │
│                      │                │                │ context        │
├──────────────────────┼────────────────┼────────────────┼────────────────┤
│ Motivation           │ ★★★★★          │ ★★☆☆☆          │ ★★★★☆          │
│ Integration          │ Constitutive   │ Backdrop       │ Explicit row   │
│                      │ (embedded in   │ (not           │ in matrix,     │
│                      │  each phase)   │  modelled)     │ not dynamic    │
├──────────────────────┼────────────────┼────────────────┼────────────────┤
│ Granularity /        │ Coarse         │ Fine           │ Medium         │
│ Analytical Precision │ (phase level)  │ (trace-based   │ (process +     │
│                      │                │  event level)  │ area grid)     │
├──────────────────────┼────────────────┼────────────────┼────────────────┤
│ Primary Use          │ Instructional  │ Research       │ Research       │
│ Case                 │ design,        │ measurement,   │ classification,│
│                      │ coaching       │ log-file       │ survey         │
│                      │                │ analysis       │ instrument     │
├──────────────────────┼────────────────┼────────────────┼────────────────┤
│ Feedback Loop        │ Phase 3 →      │ Standards-     │ Not modelled   │
│ Architecture         │ Phase 1        │ Products gap   │ dynamically;   │
│                      │ (cyclic)       │ drives next    │ static grid    │
│                      │                │ operation      │                │
├──────────────────────┼────────────────┼────────────────┼────────────────┤
│ Weakness             │ Motivational   │ Motivation     │ Lacks dynamic  │
│                      │ constructs     │ under-         │ process model; │
│                      │ under-         │ theorised;     │ comprehensive  │
│                      │ operationalised│ complex        │ but unwieldy   │
└──────────────────────┴────────────────┴────────────────┴────────────────┘
  
  [[Barry-Zimmerman.md]]    [[Philip-Winne.md]]     [[Paul-Pintrich.md]]
```

**Reading guide:** Read across rows to compare the three models on the same dimension; read down columns for a portrait of each model's character. The "Mechanistic Emphasis" row is the most theoretically important: Zimmerman integrates motivation as a *constitutive* part of the cycle, Winne treats it as background, and Pintrich handles it as a separate regulated area. Practitioners will find Zimmerman most actionable; researchers doing trace-based work will find Winne most precise; those needing comprehensive taxonomy will find Pintrich most exhaustive.

**Source:** §Self-Regulated Learning: The Major Models

---

## Visual Aid 5: Pintrich's 4×4 Regulation Matrix

**Purpose:** Reconstruct [[Pintrich's-4×4-Matrix.md]] — the cross-classification of SRL *phases* × *areas of regulation* — as a navigable reference grid.

```
╔════════════════════════════════════════════════════════════════════════╗
║          PINTRICH'S 4×4 MATRIX  [[Pintrich's-4×4-Matrix.md]]          ║
║          Phases (rows) × Areas of Regulation (columns)                ║
╠════════════════╦══════════════╦══════════════╦══════════╦═════════════╣
║                ║  COGNITION   ║   MOTIV /    ║BEHAVIOUR ║  CONTEXT    ║
║    PHASE       ║              ║   AFFECT     ║          ║             ║
╠════════════════╬══════════════╬══════════════╬══════════╬═════════════╣
║  PLANNING      ║ Activating   ║ Goal         ║ Planning ║ Perceiving  ║
║                ║ prior        ║ orientation  ║ time &   ║ task        ║
║                ║ knowledge;   ║ activation;  ║ effort;  ║ conditions; ║
║                ║ metacogn.    ║ self-        ║ planning ║ evaluating  ║
║                ║ knowledge    ║ efficacy     ║ for help ║ context     ║
║                ║ activation   ║ judgments    ║          ║ resources   ║
╠════════════════╬══════════════╬══════════════╬══════════╬═════════════╣
║  MONITORING    ║ Metacogn.    ║ Monitoring   ║ Monitor  ║ Monitoring  ║
║                ║ monitoring   ║ motivation,  ║ effort,  ║ changing    ║
║                ║ of cognition;║ affect,      ║ time use,║ task &      ║
║                ║ comprehension║ anxiety      ║ need for ║ context     ║
║                ║ monitoring   ║              ║ help     ║ conditions  ║
╠════════════════╬══════════════╬══════════════╬══════════╬═════════════╣
║  CONTROL       ║ Cognitive    ║ Regulating   ║ Increase/║ Change or   ║
║  (Regulation)  ║ strategy     ║ motivation & ║ reduce   ║ renegotiate ║
║                ║ selection &  ║ affect;      ║ effort;  ║ task;       ║
║                ║ adaptation   ║ controlling  ║ persist/ ║ seek help;  ║
║                ║              ║ anxiety      ║ disengage║ restructure ║
║                ║              ║              ║          ║ context     ║
╠════════════════╬══════════════╬══════════════╬══════════╬═════════════╣
║  REFLECTION    ║ Cognitive    ║ Affective    ║ Behaviour║ Evaluating  ║
║                ║ judgments;   ║ reactions;   ║ reflect; ║ task &      ║
║                ║ attributions ║ causal       ║ choice   ║ context;    ║
║                ║ for cogn.    ║ attributions ║ behav.   ║ attributions║
║                ║ outcomes     ║              ║          ║ to context  ║
╚════════════════╩══════════════╩══════════════╩══════════╩═════════════╝

 ⚠ KEY DIAGNOSTIC:
   Many students regulate COGNITION adequately while failing to
   regulate AFFECT (test anxiety = motivation/affect control failure)
   — the matrix reveals hidden regulatory gaps.
```

**Reading guide:** Each cell is an SRL activity: phase tells you *when* it happens, area tells you *what domain* it operates on. The matrix is most useful as a diagnostic tool — to identify which cells a learner or instructional design has covered and which have been neglected. The Motivation/Affect column is the most commonly under-addressed in both teaching and self-study; test anxiety sits in Monitoring (row 2) and Control (row 3) of that column.

**Source:** §Self-Regulated Learning: The Major Models (Pintrich subsection); §The Four Areas of Regulation

---

## Visual Aid 6: Metacognitive Monitoring Judgments — Comparison Panel

**Purpose:** Display all four monitoring judgment types ([[Judgment-of-Learning-JOL.md]], [[Feeling-of-Knowing-FOK.md]], [[Ease-of-Learning.md]], retrospective confidence) side-by-side for rapid comparison.

```
┌─────────────────────────────────────────────────────────────────┐
│           METACOGNITIVE MONITORING JUDGMENT TYPES               │
│           [[Metacognitive-Judgments.md]]                        │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────┬────────────────┬────────────────┬─────────────┐
│   JUDGMENT      │  TIMING        │  PREDICTS      │  ACCURACY   │
├─────────────────┼────────────────┼────────────────┼─────────────┤
│ Ease of         │                │                │             │
│ Learning (EOL)  │ BEFORE study   │ How easy the   │   ★★★☆☆     │
│                 │                │ item will be   │  Moderate   │
│ [[Ease-of-      │ Pre-learning   │ to learn       │             │
│  Learning.md]]  │ judgment       │                │             │
├─────────────────┼────────────────┼────────────────┼─────────────┤
│ Judgment of     │                │                │             │
│ Learning (JOL)  │ DURING / AFTER │ Future recall  │ ★☆☆☆☆ immed.│
│                 │ study          │ success        │ ★★★☆☆ delay.│
│ [[Judgment-of-  │                │                │             │
│  Learning-      │ ⚠ Immediate    │ ⚠ Fluency      │  KEY: delay │
│  JOL.md]]       │ JOLs driven    │ confounds      │  JOLs far   │
│                 │ by FLUENCY     │ felt ease with │  more valid  │
│                 │ not strength   │ actual learning│             │
├─────────────────┼────────────────┼────────────────┼─────────────┤
│ Feeling of      │                │                │             │
│ Knowing (FOK)   │ DURING         │ Whether cued   │   ★★★☆☆     │
│                 │ retrieval      │ recall (or     │  Moderate   │
│ [[Feeling-of-   │ failure        │ recognition)   │             │
│  Knowing-       │                │ will succeed   │ Better for  │
│  FOK.md]]       │ When can't     │                │ recognition │
│                 │ recall         │                │ than cued   │
│                 │ spontaneously  │                │ recall      │
├─────────────────┼────────────────┼────────────────┼─────────────┤
│ Retrospective   │                │                │             │
│ Confidence      │ AFTER          │ Whether the    │   ★★★☆☆     │
│ Judgment (RCJ)  │ retrieval      │ retrieved      │  Moderate   │
│                 │                │ answer is      │             │
│                 │ Post-response  │ correct        │ Higher for  │
│                 │ evaluation     │                │ correct vs. │
│                 │                │                │ incorrect   │
└─────────────────┴────────────────┴────────────────┴─────────────┘

CALIBRATION TRAINING:  Predict score → Take test → Review discrepancy
                       [[Metacognitive-Calibration.md]]
→ Improves accuracy of JOLs over time through feedback loop
```

**Reading guide:** The four rows map the monitoring system across the full learning episode: EOL before, JOL during/after, FOK during retrieval, RCJ after retrieval. The ⚠ flags mark the fluency trap in JOLs — the single most practically important failure mode in the set. The accuracy column shows why immediate JOLs are unreliable (low, ★☆☆☆☆) while delayed JOLs improve substantially: time degrades fluency as a confound, leaving only true memory strength as the basis for the judgment.

**Source:** §Metacognitive Monitoring: Types of Monitoring Judgments; §The Fluency Trap

---

## Visual Aid 7: Intellectual Genealogy — From Flavell (1979) to PKB Architecture

**Purpose:** Map the intellectual lineage of key ideas in this domain, showing which theorists built on whom and how the field developed from Flavell's foundational work through SRL models to PKB applications.

```
 FLAVELL (1979)
 [[Flavell.md]]
 "thinking about
  one's own thinking"
        │
        ├──────────────────────────────────────────────┐
        │                                              │
        ▼                                              ▼
 NELSON & NARENS                               ANN BROWN
 [[Nelson-Narens-Model.md]]                    [[Ann-Brown.md]]
 Monitoring-Control                            Metacognition
 formal model                                  in classroom
 (object/meta levels)                          (reciprocal teaching)
        │                                              │
        ├──────────────────┐                           │
        │                  │                           │
        ▼                  ▼                           ▼
 WINNE                ZIMMERMAN                  BROWN &
 [[Philip-Winne.md]]  [[Barry-Zimmerman.md]]     PALINCSAR
 COPES model;         Social-cognitive           Instructional
 standards-based      SRL cycle;                 applications
 monitoring;          motivation                 of metacognition
 trace methods        integrated
        │                  │
        └──────────┬────────┘
                   │
                   ▼
            PINTRICH
            [[Paul-Pintrich.md]]
            4×4 matrix;
            MSLQ instrument;
            motivation/affect
            as regulated area
                   │
        ┌──────────┤
        │          │
        ▼          ▼
  GARRISON       SCHRAW &
  [[D.-Randy-    DENNISON
   Garrison.md]] Metacognitive
  SDL model;     Awareness
  self-manage,   Inventory
  self-monitor,  (MAI)
  motivation
        │
        ▼
  METACOGNITIVE
  SOVEREIGNTY
  [[Metacognitive-
   Calibration.md]]
  Goal: self-governing
  learner with own
  epistemic standards
        │
        └──────────────────────────────────────────────┐
                                                       │
                                                       ▼
                                              PKB AS EXTERNALISED
                                              METACOGNITION
                                              [[PKB.md]]
                                              [[Metacognitive-
                                               Scaffolding.md]]
                                              [[Cognitive-
                                               Offloading.md]]
                                              Not merely a tool FOR
                                              metacognition — a
                                              constitutive component
                                              OF it
```

**Reading guide:** Follow the central spine (Flavell → Nelson-Narens → Winne/Zimmerman → Pintrich → Garrison) for the theoretical mainstream. The right branch shows applied/educational research running in parallel. The bottom row (PKB as externalised metacognition) represents the most recent theoretical development: the claim that PKB systems don't just *support* metacognition but become part of the metacognitive architecture itself — an extension of the monitoring-control loop into external media.

**Source:** §Metacognition Architecture; §SRL Models; §PKB as Metacognitive Architecture; §Influence Map throughout MOC

---

## Visual Aid 8: SRL ↔ SDL — Grain-Size Spectrum

**Purpose:** Position [[Self-Regulated-Learning.md]] and [[Self-Directed-Learning.md]] on a continuum that shows their relationship and the grain-size distinction.

```
GRAIN SIZE ──────────────────────────────────────────────────────►
(episode)                                          (life/trajectory)

│                                                                  │
SRL                                                               SDL
│                                                                  │

●─────────────────────────●──────────────────────────────●────────●
Single        Study      Course        Curriculum     Learning   Life-
Task          Session    Level         Level          Trajectory  Long
                                                                  
WHAT IS       What       How to        What to        What/why   Whether,
REGULATED?    strategies study this    study this     to learn   what, &
              to use     exam          semester       at all     how to
              right now                                          learn

LOCUS OF      Learner    Learner +     Learner +      Learner    Fully
GOAL-SETTING  within     teacher       institution    with       self-
              task                                   guidance   authored

MOTIVATION    Intrinsic  Mixed         Mixed          Internalized Autonomous
PROFILE       interest                               identified  integrated
              task-level                                         [[Autonomous-
                                                                  Motivation.md]]

THEORETICAL   Zimmerman  Zimmerman     Pintrich       Garrison   Garrison +
HOME          Winne      Winne         (context       SDL model  Autonomy
              Pintrich                 column)                    [[Autonomy.md]]

              ◄──── ACADEMIC SRL ──────────────────── SDL ────►
                    (most research)                  (life-wide)
```

**Reading guide:** The grain-size distinction is the fundamental conceptual divide: SRL asks *how* a learner studies; SDL asks *whether, what, and why* they learn at all. As grain size increases, motivational constructs become more central and structural constraints loosen. A student who SRL-regulates very effectively within externally-set curricula may not have SDL capacity at all — they have never chosen their own learning direction. [[Metacognitive-Sovereignty.md]] is the developmental endpoint at the SDL end: the learner governs their own epistemic standards.

**Source:** §Self-Directed Learning: Expanding the Grain Size; SDL vs SRL distinction throughout

---

## Visual Aid 9: Before/After — Poor vs. Effective Metacognitive Regulation

**Purpose:** Contrast two profiles — the poorly-calibrated learner and the effectively self-regulating learner — across the full monitoring-control-reflection cycle.

```
┌──────── POORLY CALIBRATED LEARNER ─────┬───── EFFECTIVE SRL LEARNER ──────┐
│                                         │                                   │
│ MONITORING STRATEGY                     │ MONITORING STRATEGY               │
│  • Re-reads material passively          │  • Self-tests before judging      │
│  • Feels "smooth" processing            │  • Uses delayed JOLs              │
│  • Immediate JOL = high confidence      │  • Prediction → check → compare  │
│  • Fluency mistaken for mastery         │  • Discrepancy drives study plan  │
│    [[Fluency-Illusion.md]]              │    [[Metacognitive-Accuracy.md]]  │
│                                         │                                   │
│ MONITORING OUTPUT                       │ MONITORING OUTPUT                 │
│  • "I know this" (false signal)         │  • "I know A, not B" (valid signal│
│  • No discrimination between            │  • Calibrated confidence by item  │
│    known and unknown items              │  • Clear study priority list      │
│                                         │                                   │
│ CONTROL RESPONSE                        │ CONTROL RESPONSE                  │
│  • Reduces study time on basis          │  • Redirects time to gaps         │
│    of false confidence                  │  • Switches strategies when       │
│  • Persists with comfortable            │    monitoring signals mismatch    │
│    strategy (re-reading)                │  • Uses diagnostic fix-up         │
│  • Does not seek help                   │    strategies                     │
│                                         │  • Help-seeking when needed       │
│                                         │                                   │
│ FORETHOUGHT PHASE                       │ FORETHOUGHT PHASE                 │
│  • Vague goal: "study chapter 4"        │  • Specific goal: "recall X by Y" │
│  • No implementation intention          │  • Implementation intention set   │
│  • Self-efficacy uncalibrated           │    [[Implementation-Intention.md]]│
│    (over- or under-confident)           │  • Self-efficacy reflects history │
│                                         │                                   │
│ REFLECTION PHASE                        │ REFLECTION PHASE                  │
│  • "I just wasn't good at this"         │  • "Strategy X failed — switch    │
│  • Fixed-ability attribution            │    to Y next time"                │
│  • Efficacy unchanged or lower          │  • Effort/strategy attribution    │
│  • Same approach next time              │  • Efficacy maintained/increased  │
│                                         │  • Approach revised for cycle N+1 │
│                                         │                                   │
│ OUTCOME                                 │ OUTCOME                           │
│  • Surprised by test failure            │  • Performance matches prediction │
│  • Learning stagnation                  │  • Iterative improvement          │
│  • Learned helplessness risk            │  • Metacognitive sovereignty      │
│    [[Learned-Helplessness.md]]          │    develops                       │
└─────────────────────────────────────────┴───────────────────────────────────┘
```

**Reading guide:** Read row by row across the two columns to see the contrast at each stage of the regulatory cycle. The most important row is the first (Monitoring Strategy): because everything downstream depends on signal quality, the intervention point is always monitoring first. Note that the Reflection Phase contrast explains why poor metacognitive learners fail to improve between cycles — the fixed-ability attribution short-circuits the feedback loop that should drive strategy revision.

**Source:** §Metacognitive Monitoring; §The SRL Cycle in Detail; §Fluency Trap

---

## Visual Aid 10: Dependency Graph — What Must Be in Place for SRL to Work

**Purpose:** Show the prerequisite architecture for functional SRL — what foundational capacities must exist before higher-order regulation becomes possible.

```
 ┌──────────────────────────────────────────────────────────────┐
 │              SRL PREREQUISITE ARCHITECTURE                   │
 └──────────────────────────────────────────────────────────────┘

 FOUNDATIONAL LAYER (must exist first)
 ┌────────────────┐   ┌─────────────────┐   ┌────────────────┐
 │ Domain         │   │ Working Memory  │   │ Self-Efficacy  │
 │ Knowledge      │   │ Capacity        │   │ Baseline       │
 │ [[Domain-      │   │ [[Working-      │   │ [[Self-        │
 │  Knowledge.md]]│   │  Memory.md]]    │   │  Efficacy.md]] │
 └───────┬────────┘   └────────┬────────┘   └───────┬────────┘
         └────────────────┬────┘                    │
                          │◄────────────────────────┘
                          ▼
 MONITORING LAYER (validity determines everything above)
 ┌───────────────────────────────────────────────────────────┐
 │  CALIBRATED MONITORING [[Metacognitive-Calibration.md]]   │
 │                                                           │
 │  EOL → JOL → FOK → RCJ  (all four types functioning)     │
 │  Fluency trap bypassed (via self-testing, not re-reading) │
 │  Calibration accuracy: JOLs predict test performance      │
 └───────────────────────┬───────────────────────────────────┘
                         │
         ┌───────────────┴────────────────┐
         ▼                                ▼
 ┌──────────────────┐          ┌──────────────────────────┐
 │ STRATEGY         │          │ METACOGNITIVE KNOWLEDGE  │
 │ KNOWLEDGE        │          │ [[Metacognitive-         │
 │ (Conditional)    │          │  Knowledge.md]]          │
 │ When/how to      │          │ Person + Task + Strategy │
 │ apply strategies │          │ knowledge                │
 └────────┬─────────┘          └────────────┬─────────────┘
          └────────────────┬────────────────┘
                           ▼
 REGULATION LAYER
 ┌──────────────────────────────────────────────────────┐
 │  METACOGNITIVE REGULATION [[Metacognitive-           │
 │                             Regulation.md]]          │
 │   Planning → Monitoring → Control (evaluate/adjust)  │
 └────────────────────────┬─────────────────────────────┘
                          │
                          ▼
 CYCLE LAYER
 ┌──────────────────────────────────────────────────────┐
 │  SRL CYCLE: Forethought → Performance → Reflection   │
 │  [[Zimmerman's-Cyclical-SRL-Model.md]]               │
 └────────────────────────┬─────────────────────────────┘
                          │
              ┌───────────┴──────────────┐
              ▼                          ▼
 ┌─────────────────────┐     ┌───────────────────────────┐
 │ SDL CAPACITY        │     │ PKB AS METACOGNITIVE      │
 │ [[Self-Directed-    │     │ ARCHITECTURE              │
 │  Learning.md]]      │     │ [[PKB.md]]                │
 │ Autonomous goal-    │     │ [[Metacognitive-          │
 │ setting, trajectory │     │  Scaffolding.md]]         │
 │ governance          │     │ Externalised monitoring + │
 └─────────────────────┘     │ persistent regulation     │
                             └───────────────────────────┘
```

**Reading guide:** Read bottom-to-top: you cannot have functional SRL without calibrated monitoring (middle layer), and you cannot have calibrated monitoring without baseline domain knowledge and working memory resources (foundational layer). The two top-level outcomes — SDL capacity and PKB integration — are only available once the full regulatory stack is functioning. The monitoring layer is the choke point: weaknesses there propagate upward to corrupt everything built on it.

**Source:** §Architecture and Components; §Monitoring; §SRL Cycle; §SDL; §PKB

---

## Synthesis Packet

**Top 5 Takeaways:**

1. **Monitoring is the master variable.** Every downstream SRL failure traces to a monitoring failure first. Calibrated signals → appropriate control → learning; uncalibrated signals → misdirected control → stagnation. Intervention should target monitoring before control.

2. **The fluency illusion is the most dangerous self-deception in learning.** The feeling of smooth processing is systematically mistaken for knowledge. Re-reading feels effective; self-testing feels difficult. Effective regulation requires replacing fluency as a monitoring cue with actual memory-strength signals.

3. **The three SRL models are complementary, not competing.** Zimmerman is the practitioner's model (motivationally rich, actionable); Winne is the researcher's model (computationally precise, trace-measurable); Pintrich is the taxonomist's model (exhaustive grid, survey-ready). Knowing which to use when is itself a metacognitive skill.

4. **SRL and SDL differ by grain size, not by kind.** SRL governs the episode; SDL governs the trajectory. Building SRL skills is necessary but not sufficient for SDL — you also need autonomous motivation and the capacity to set your own epistemic standards (metacognitive sovereignty).

5. **A well-designed PKB is metacognitive architecture, not just storage.** The note-making process forces the SRL cycle (forethought in choosing connections, monitoring in evaluating fit, reflection in updating structure). This makes active PKB practice a form of metacognitive rehearsal with every note.

---

**Navigator — which aid answers which question:**

| Question | Aid |
|---|---|
| "What is metacognition actually made of?" | Aid 1 (Taxonomy Tree) |
| "Why does re-reading feel effective but not work?" | Aid 2 (Causal Map) + Aid 6 (Judgment Panel) |
| "What are the stages of Zimmerman's model?" | Aid 3 (SRL Cycle Flow) |
| "How do the three major SRL models differ?" | Aid 4 (Comparison Matrix) |
| "What is Pintrich's 4×4 matrix?" | Aid 5 (Pintrich Grid) |
| "What types of monitoring judgments exist?" | Aid 6 (Judgment Panel) |
| "Where did these ideas come from?" | Aid 7 (Genealogy Map) |
| "What is the difference between SRL and SDL?" | Aid 8 (Grain-Size Spectrum) |
| "What does poor vs. good metacognitive regulation look like?" | Aid 9 (Before/After) |
| "What needs to be in place for SRL to work?" | Aid 10 (Dependency Graph) |

---

```
╔══════════════════════════════════════════════════════════════╗
║              MOC SCORECARD: Metacognition & SRL              ║
╠══════════════════════════════════════════════════════════════╣
║ Core thesis   : Monitoring calibration is the master         ║
║                 variable; all SRL rides on signal validity   ║
║ Strongest node: Fluency illusion / monitoring judgment        ║
║                 research — robust, replicated, actionable    ║
║ Open question : SRL domain-specificity; measurement          ║
║                 validity of self-report instruments          ║
║ Bootstrapping : Can't know your metacognition is poor        ║
║ problem       : without metacognition — intractable directly ║
║ Key action    : Replace re-reading with self-testing;        ║
║                 use delayed JOLs; review prediction gaps     ║
║ Read if you   : Design learning, coach students, build PKB   ║
║ Skip if you   : Want motivational theory only (→ Motivation  ║
║                 MOC) or memory mechanisms only (→ Memory MOC)║
║ Companion MOCs: Memory Science | Motivation Psychology       ║
║                 PKB & Knowledge Management | Learning Science║
╚══════════════════════════════════════════════════════════════╝
```