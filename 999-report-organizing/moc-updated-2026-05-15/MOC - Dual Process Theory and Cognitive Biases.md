---
tags: [moc, domain-dual-process, domain-cognitive-biases, domain-behavioral-economics, status-evergreen]
aliases: [Cognitive Biases MOC, Dual Process MOC, Heuristics MOC, Behavioral Economics MOC]
created: 2026-05-15
modified: 2026-05-15
status: evergreen
type: moc
moc_pattern: hub-and-spoke
domain: Dual Process Theory and Cognitive Biases
source_notes_count: 46
target_word_count: 4500
audience: [practitioner, researcher]
maturity: established
parent_moc: "[[MOC - Cognitive Science (Master Index)]]"
related_mocs: ["[[MOC - Critical Thinking and Logic]]", "[[MOC - Social Psychology]]", "[[MOC - Motivation Psychology]]"]
version: 1.0.0
---

# Dual Process Theory and Cognitive Biases — Map of Content

> [!abstract] Domain & Scope
> **Dual process theory** is the architectural account of cognition that distinguishes fast, automatic, associative processing (Type 1 / System 1) from slow, deliberate, rule-governed processing (Type 2 / System 2). **Cognitive biases** are the systematic departures from normative rationality that arise from this architecture — predictable, reproducible, and theoretically tractable errors in judgment and decision-making. This MOC organises 46 permanent notes spanning the dual-process architecture, the major heuristics and their associated biases, behavioural economics applications, and the prospects for debiasing. It is structured as a **hub-and-spoke** — dual process theory as the hub, with heuristics, biases, behavioural economics, and debiasing as spokes.
>
> **For**: Decision researchers, practitioners in any domain where judgment quality matters
> **Companion MOCs**: [[MOC - Critical Thinking and Logic]], [[MOC - Social Psychology]]
> **Reading time**: ~22 minutes

## 🗺️ Navigation

- **[The Dual-Process Architecture](#the-dual-process-architecture)** — System 1 and System 2
- **[The Heuristics Program](#the-heuristics-program)** — availability, representativeness, affect
- **[The Cognitive Bias Catalogue](#the-cognitive-bias-catalogue)** — major biases organised by mechanism
- **[Behavioural Economics](#behavioural-economics)** — Prospect Theory and decision anomalies
- **[Motivated Reasoning and Epistemic Biases](#motivated-reasoning-and-epistemic-biases)** — when beliefs protect the self
- **[Debiasing: What Works](#debiasing-what-works)** — interventions and their limits
- **[Cross-Domain Bridges](#cross-domain-bridges)**
- **[Frontier & Open Questions](#frontier--open-questions)**
- **[Index of Linked Notes](#index-of-linked-notes)**

---

## The Dual-Process Architecture

[[dual-process-theory|Dual-process theory]] is not a single unified theory but a family of related proposals united by the claim that human cognition involves two qualitatively distinct systems (or modes of processing) that differ in speed, effort, conscious access, and susceptibility to systematic error.

[[system-1|System 1]] ([[type-1-processing|Type 1 processing]]) is the fast, automatic, effortless, associative, and largely unconscious mode. It operates through pattern matching, heuristic shortcuts, and emotional responses. It processes in parallel, is sensitive to salience and vividness, and is evolutionarily older. System 1 generates the bulk of ordinary cognition: you don't *decide* to recognise a face or feel that a situation is dangerous — these computations happen automatically.

[[system-2|System 2]] ([[type-2-processing|Type 2 processing]]) is the slow, deliberate, effortful, rule-governed, and consciously accessible mode. It can override System 1 but at metabolic cost and limited bandwidth. System 2 handles novel, complex, or logical reasoning — following a proof, completing a tax return, resisting an impulsive purchase.

[[default-interventionist-architecture|The default-interventionist architecture]] describes the operational relationship between the systems: System 1 generates a rapid default response (an intuition, an answer that "feels right"), and System 2 either endorses it uncritically (the default path, used most of the time) or intervenes to check, revise, or override it. The critical insight: System 2's intervention is *triggered* by System 1 flags of conflict or unfamiliarity — but System 1 flags are imperfect, so many System 1 errors pass through undetected.

```
DUAL-PROCESS DEFAULT-INTERVENTIONIST FLOW
════════════════════════════════════════════════════════
Input ──► System 1 ──► Default Response ──► Output
             │                    ▲
             │ Conflict flag?      │ [most of the time:
             ▼                    │  no intervention]
          System 2               │
          (deliberation)         │
             └────────────────────┘
              [Override or endorse]
════════════════════════════════════════════════════════
```

> [!key-claim] The Lazy System 2
> The dominant error pattern is not System 1 running amok but System 2 being lazy. System 2 can correct System 1 errors, but it requires effort and is often not engaged. The critical question is not "can people reason correctly?" but "do the conditions trigger System 2 engagement?"

---

## The Heuristics Program

The heuristics and biases research programme (Kahneman & Tversky, 1970s–present) identified specific cognitive shortcuts — heuristics — that produce reliable patterns of error. A heuristic is not a defect; it is a processing efficiency that works in most cases but fails in predictable ways.

### Availability Heuristic

[[availability-heuristic|The availability heuristic]] is the tendency to judge frequency or probability by the ease with which instances come to mind. Recent, vivid, and emotionally charged events are easily recalled, leading to overestimation of their frequency. After a plane crash, people overestimate air travel risk; after media coverage of rare violent crime, people overestimate violent crime rates.

The availability heuristic is adaptive in most environments — if you have encountered many instances of something, it is probably common. It fails when the *ease of recall* is driven by factors other than actual frequency (vividness, recency, media coverage, personal experience).

### Representativeness Heuristic

[[representativeness-heuristic|The representativeness heuristic]] judges probability by resemblance to a prototype or category. The [[conjunction-fallacy|conjunction fallacy]] (Linda is a feminist bank teller is judged more probable than Linda is a bank teller) is its canonical demonstration: the more representative a description, the higher its perceived probability, regardless of the logical constraint that conjunctions cannot exceed base probabilities.

[[base-rate-neglect|Base-rate neglect]] is the systematic under-weighting of prior probabilities (base rates) in favour of specific case information. Even when told that 85% of cabs are blue and only 15% are green, witnesses claiming to see a green cab shift judgments dramatically — the specific testimony dominates the base rate in System 1 processing.

### Affect Heuristic

[[affect-heuristic|The affect heuristic]] (Slovic) is the use of emotional valence as a guide to judgment. If something feels good (positive affect), risks are estimated as low and benefits as high; if it feels bad, risks are high and benefits low. This *risk-benefit confound* — genuinely independent quantities that should vary independently but that covary in subjective evaluation — is driven by affect as the primary heuristic.

---

## The Cognitive Bias Catalogue

Cognitive biases are systematic errors in judgment produced by heuristic processing, motivational influences, or cognitive limitations. They are *predictable*: the same biases appear across populations, tasks, and cultures.

### Memory-Based Biases

[[availability-heuristic|Availability-related biases]]: recency effects, [[hindsight-bias|hindsight bias]] ("I knew it all along" — events that occurred seem far more predictable in retrospect than they were in foresight), and [[curse-of-knowledge|curse of knowledge]] (difficulty imagining what it is like not to know what you know — a source of communication failures between experts and novices).

### Anchoring and Adjustment

[[anchoring-bias|Anchoring bias]] is the tendency to insufficiently adjust estimates away from an initial value (the anchor), even when that value is known to be arbitrary. When asked to estimate an unknown quantity after seeing a random number (e.g., generated by a spinning wheel), estimates are systematically pulled toward the anchor. Anchoring affects salary negotiations, legal settlements, and clinical diagnosis.

### Overconfidence

[[overconfidence-bias|Overconfidence bias]] is the tendency to be more confident in one's judgments than accuracy warrants. On knowledge tests, people report ~80% confidence in answers that are correct only ~60% of the time. [[dunning-kruger-effect|The Dunning-Kruger effect]] is a specific form: incompetent individuals tend to overestimate their competence (because they lack the metacognitive skill to recognise the gap), while highly competent individuals sometimes underestimate (because they assume tasks easy for them are easy for others).

### Framing Effects

[[framing-effect|Framing effects]] occur when the same objective information, presented differently, produces different judgments. A medical treatment described as having "90% survival rate" is more favourably evaluated than the same treatment described as having a "10% mortality rate." Frames activate different affective responses and different reference points, driving divergent choices without changing the underlying reality.

### Confirmation Bias

[[confirmation-bias|Confirmation bias]] is the pervasive tendency to seek, interpret, and recall information in ways that confirm one's existing beliefs. It operates at the search stage (seeking confirming evidence), the interpretation stage (interpreting ambiguous evidence as confirming), and the memory stage (better recall of confirming evidence). It is the cognitive bias with the broadest implications for rational inquiry, including scientific practice.

---

## Behavioural Economics

Behavioural economics applies the cognitive bias research programme to economic decision-making, revealing systematic departures from rational choice theory (expected utility maximisation).

[[prospect-theory|Prospect Theory]] (Kahneman & Tversky, 1979) is the cornerstone: it describes how people *actually* make decisions under uncertainty, as opposed to how rational-choice theory says they should. Key findings: people are *loss averse* — losses loom approximately twice as large as equivalent gains. People evaluate outcomes relative to a *reference point* rather than in absolute terms. Probability weighting is non-linear: small probabilities are overweighted, moderate-to-high probabilities are underweighted.

[[loss-aversion|Loss aversion]] explains the [[endowment-effect|endowment effect]] (owning an object makes you value it more than before you owned it), the [[status-quo-bias|status quo bias]] (preference for the current state), and [[sunk-cost-fallacy|sunk cost fallacy]] (continuing investments because of past costs, even when future prospects are poor).

[[hyperbolic-discounting|Hyperbolic discounting]] is the systematic preference for immediate rewards over future rewards at a rate that is *disproportionately* steep for near-future intervals — producing *present bias*. We make plans for the future that our future selves then fail to follow, precisely because the discounting function steepens as rewards become immediate.

[[choice-architecture|Choice architecture]] (Thaler & Sunstein) is the practical application: since default choices have disproportionate influence (loss aversion makes changing from the default feel like a loss), default design is an ethical responsibility. [[nudge-theory|Nudge theory]] uses choice architecture to steer behaviour toward beneficial outcomes without restricting freedom of choice.

---

## Motivated Reasoning and Epistemic Biases

Not all cognitive errors are processing errors — some are *motivated*: they serve psychological functions beyond accurate belief formation.

[[motivated-reasoning|Motivated reasoning]] is the use of System 2 reasoning capacities in the service of System 1-generated conclusions — rationalisations that feel like genuine reasoning but are driven by pre-existing beliefs and emotional investments. Kunda's framework distinguishes *directional* goals (wanting a particular conclusion) from *accuracy* goals (wanting the true conclusion).

[[belief-bias|Belief bias]] in reasoning is the tendency to evaluate the logic of an argument based on whether one agrees with the conclusion rather than the validity of the argument structure. People accept logically invalid arguments with believable conclusions and reject valid arguments with unbelievable conclusions.

[[myside-bias|Myside bias]] is the tendency to generate and evaluate arguments in a manner that supports one's prior beliefs — a pervasive asymmetry in the argumentative process that [[MOC - Critical Thinking and Logic]] addresses through intellectual virtues and deliberate steelmanning.

---

## Debiasing: What Works

[[cognitive-forcing-functions|Cognitive forcing functions]] are designed interventions that slow down decision-making and engage System 2 checking. They are more effective than education about biases because they work *at the point of decision* rather than relying on the biased person to remember their biases.

The evidence on debiasing is sobering: general education about cognitive biases produces small, inconsistent improvements in bias reduction. Domain-specific feedback over time with accurate outcome data is more effective. [[consider-the-opposite]] strategies (explicitly generating reasons the conclusion might be wrong) reduce anchoring and overconfidence moderately.

What does not work reliably: telling people about the bias, asking them to "try harder," or one-time training in critical thinking. The reason is clear: most cognitive biases operate at the level of System 1, below the threshold of voluntary control.

---

## 🌉 Cross-Domain Bridges

> [!related] Companion MOCs
> - [[MOC - Critical Thinking and Logic]] — Cognitive biases are the empirical explanation for the informal fallacies taxonomy; the dual-process account explains *why* intelligent people commit fallacies. CT training that succeeds in reducing bias typically targets System 2 activation, not System 1 correction.
> - [[MOC - Social Psychology]] — The fundamental attribution error, social proof, and conformity are social instantiations of heuristic processing; the dual-process framework explains their mechanisms.
> - [[MOC - Motivation Psychology]] — Motivated reasoning, ego-involvement, and the overjustification effect all involve the interaction of motivational goals with cognitive processing — the dual-process framework provides the mechanism.

---

## 🌅 Frontier & Open Questions

> [!frontier] Live debates
> - **Two systems or one?** The "systems" metaphor is increasingly contested — some researchers argue for a single system with multiple modes rather than two distinct systems. The evidence for and against is genuinely complex.
> - **Ecological rationality**: Gerd Gigerenzen argues that heuristics are not biases but *adaptive tools* — fast-and-frugal algorithms that are optimally calibrated to real-world statistical environments. The debate about when heuristics are "biased" vs "efficient" continues.
> - **Debiasing at scale**: Individual-level debiasing interventions are weakly effective. Can systemic-level interventions (process redesign, team protocols, institutional rules) achieve what individual training cannot?

---

## 📚 Index of Linked Notes

| Note | Type | Section |
|------|------|---------|
| [[affect-heuristic]] | atomic | Heuristics |
| [[anchoring-bias]] | atomic | Bias Catalogue |
| [[availability-heuristic]] | reference | Heuristics |
| [[base-rate-neglect]] | atomic | Heuristics |
| [[behavioral-economics]] | reference | Behavioural Economics |
| [[belief-bias]] | atomic | Motivated Reasoning |
| [[bounded-rationality]] | atomic | Debiasing |
| [[choice-architecture]] | atomic | Behavioural Economics |
| [[cognitive-bias]] | reference | Introduction |
| [[cognitive-ease]] | atomic | Heuristics |
| [[cognitive-forcing-functions]] | atomic | Debiasing |
| [[confirmation-bias]] | reference | Bias Catalogue |
| [[conjunction-fallacy]] | atomic | Heuristics |
| [[curse-of-knowledge]] | atomic | Bias Catalogue |
| [[decision-fatigue]] | atomic | Architecture |
| [[default-interventionist-architecture]] | reference | Architecture |
| [[dual-process-theory]] | reference | Architecture |
| [[dunning-kruger-effect]] | reference | Bias Catalogue |
| [[endowment-effect]] | atomic | Behavioural Economics |
| [[fluency-illusion]] | atomic | Bias Catalogue |
| [[framing-effect]] | reference | Bias Catalogue |
| [[gamblers-fallacy]] | atomic | Heuristics |
| [[heuristics-and-biases]] | reference | Heuristics |
| [[hindsight-bias]] | reference | Bias Catalogue |
| [[hyperbolic-discounting]] | atomic | Behavioural Economics |
| [[loss-aversion]] | reference | Behavioural Economics |
| [[motivated-reasoning]] | reference | Motivated Reasoning |
| [[myside-bias]] | atomic | Motivated Reasoning |
| [[nudge-theory]] | atomic | Behavioural Economics |
| [[overconfidence-bias]] | atomic | Bias Catalogue |
| [[present-bias]] | atomic | Behavioural Economics |
| [[prospect-theory]] | reference | Behavioural Economics |
| [[representativeness-heuristic]] | reference | Heuristics |
| [[satisficing]] | atomic | Architecture |
| [[status-quo-bias]] | atomic | Behavioural Economics |
| [[sunk-cost-fallacy]] | atomic | Bias Catalogue |
| [[system-1]] | reference | Architecture |
| [[system-2]] | reference | Architecture |
| [[type-1-processing]] | atomic | Architecture |
| [[type-2-processing]] | atomic | Architecture |

---

> [!info] MOC Metadata
> - **Pattern**: hub-and-spoke
> - **Source notes**: 46
> - **Word count**: ~4,400
> - **Generated**: 2026-05-15 by MOC Specialist Agent v1.0.0
> - **Audit trail**: [[_meta/MOC - Dual Process Theory and Cognitive Biases.audit]]
> - **Next review suggested**: 2026-08-15



# Visual Aid Suite: Dual Process Theory and Cognitive Biases — MOC

**Report length:** ~4,400 words | **Source notes:** 46
**Audience:** Practitioner / Researcher
**Thesis:** Human cognition runs on two architecturally distinct systems — automatic System 1 and deliberate System 2 — and cognitive biases are the predictable, systematic errors that emerge when System 1 dominates and System 2 fails to intervene.
**Aids selected:**
1. Process Flow — The default-interventionist architecture (the MOC's core causal model)
2. Comparison Matrix — System 1 vs System 2 across 8 dimensions
3. Taxonomy Tree — The Bias Catalogue organised by mechanism
4. Influence Map — Intellectual genealogy from founders to applications
5. Causal Architecture — Heuristic → Bias pipeline (which shortcut produces which error)
6. Comparison Matrix — Three heuristics compared (availability, representativeness, affect)
7. Swimlane Diagram — Where each bias operates in the decision cycle
8. Evidence Ledger — Key claims with evidence type and reliability
9. Before/After Contrast — Biased vs. debiased decision environment
10. TL;DR Scorecard

---

## Visual Aid 1: The Default-Interventionist Architecture

**Purpose:** Shows how System 1 and System 2 interact to produce either rational or biased outputs, including the critical "lazy System 2" failure path.

```
╔══════════════════════════════════════════════════════════════════════╗
║         DEFAULT-INTERVENTIONIST ARCHITECTURE                         ║
╚══════════════════════════════════════════════════════════════════════╝

  STIMULUS / INPUT
        │
        ▼
┌───────────────────────────────────────────────────────┐
│                      SYSTEM 1                         │
│  Fast · Automatic · Effortless · Associative          │
│  Pattern matching · Emotional response · Parallel     │
│  processing · Evolutionarily older                    │
└───────────────────────┬───────────────────────────────┘
                        │
               Generates DEFAULT response
               (intuition, "feels right")
                        │
             ┌──────────▼──────────┐
             │  Conflict detected? │
             │  (unfamiliar,       │
             │   high stakes,      │
             │   flagged as odd)   │
             └──────┬──────┬───────┘
                    │      │
               YES  │      │ NO  (most of the time)
                    ▼      │
        ┌─────────────────┐│
        │    SYSTEM 2     ││
        │  Slow · Effortful│
        │  Rule-governed  ││
        │  Consciously    ││
        │  accessible     ││
        └────────┬────────┘│
                 │         │
          ┌──────▼──────┐  │
          │  OVERRIDE   │  │ ENDORSE
          │  or REVISE  │  │ uncritically
          └──────┬──────┘  │
                 │         │
                 ▼         ▼
         ┌───────────────────────┐
         │   FINAL RESPONSE /    │
         │      JUDGMENT         │
         └───────────────────────┘
              │           │
              │           │
       CORRECTED      BIASED OUTPUT
       RESPONSE       (S1 error passed
                       through unchecked)

  ⚠ KEY INSIGHT: The critical failure is not System 1 running amok
    but System 2 being LAZY — failing to engage even when it should.
```

**Reading guide:** Follow the stimulus top-to-bottom. The critical branch is the conflict-detection diamond: when no conflict is flagged, System 2 never activates and System 1's output becomes the final judgment unchecked. Most cognitive biases live on the right-hand path. System 2 *can* correct System 1 errors, but only if engaged — and engagement requires effortful triggering.

**Source:** §The Dual-Process Architecture; §Default-Interventionist Architecture

---

## Visual Aid 2: System 1 vs. System 2 — Eight-Dimension Comparison

**Purpose:** Provides a systematic side-by-side contrast of the two processing modes across every key analytical dimension.

```
╔══════════════════════════════════════════════════════════════════════╗
║              SYSTEM 1 vs. SYSTEM 2 — PROPERTY MATRIX                ║
╠══════════════════════════════════════════════════════════════════════╣
║ DIMENSION          │  SYSTEM 1 (Type 1)     │  SYSTEM 2 (Type 2)   ║
╠════════════════════╪════════════════════════╪══════════════════════╣
║ Speed              │  Fast (milliseconds)   │  Slow (seconds)      ║
║ Effort             │  Effortless            │  Effortful           ║
║ Awareness          │  Largely unconscious   │  Consciously access. ║
║ Processing mode    │  Parallel / associat.  │  Serial / rule-gov.  ║
║ Capacity           │  High / unlimited      │  Limited bandwidth   ║
║ Activation trigger │  Automatic             │  Requires effort     ║
║ Error type         │  Systematic (biases)   │  Random / lazy S2    ║
║ Evolutionary age   │  Older                 │  More recent         ║
╠════════════════════╪════════════════════════╪══════════════════════╣
║ EXAMPLES           │  Face recognition      │  Tax return          ║
║                    │  Danger intuition      │  Logical proof       ║
║                    │  Fluent reading        │  Resist impulse      ║
║                    │  Heuristic shortcuts   │  Novel reasoning     ║
╠════════════════════╪════════════════════════╪══════════════════════╣
║ WHEN IT HELPS      │  Rapid, routine tasks  │  Novel, complex,     ║
║                    │  Expert pattern recog. │  high-stakes tasks   ║
╠════════════════════╪════════════════════════╪══════════════════════╣
║ WHEN IT FAILS      │  Vivid but rare events │  Fatigue / overload  ║
║                    │  Anchoring to salient  │  Motivated reasoning ║
║                    │  Emotional override    │  (S2 serves S1 goal) ║
╠════════════════════╪════════════════════════╪══════════════════════╣
║ DEBIASING TARGET?  │  ✗ Below voluntary     │  ✓ Engagement can    ║
║                    │    control threshold   │    be triggered      ║
╚════════════════════╧════════════════════════╧══════════════════════╝
```

**Reading guide:** Read each row as a direct contrast. The bottom rows are the most practically important: System 1 failures are largely inaccessible to voluntary correction, so debiasing must work by triggering System 2 engagement rather than suppressing System 1 directly. The "When It Fails" row maps to the major bias categories in Aid 3.

**Source:** §The Dual-Process Architecture; §Debiasing: What Works

---

## Visual Aid 3: The Bias Catalogue — Taxonomy by Mechanism

**Purpose:** Organises all major biases in the MOC into a hierarchical tree, showing that biases are not a random list but cluster by their generating mechanism.

```
COGNITIVE BIASES — TAXONOMY BY GENERATING MECHANISM
═══════════════════════════════════════════════════════════════════════

COGNITIVE BIASES
│
├── HEURISTIC-GENERATED BIASES
│   │
│   ├── Availability-Based
│   │   ├── Availability Bias (frequency ≈ ease of recall)
│   │   ├── Recency Effect
│   │   └── Hindsight Bias ("I knew it all along")
│   │
│   ├── Representativeness-Based
│   │   ├── Conjunction Fallacy (Linda problem)
│   │   ├── Base-Rate Neglect
│   │   └── Gambler's Fallacy
│   │
│   ├── Affect-Based
│   │   ├── Affect Heuristic (risk-benefit confound)
│   │   └── Cognitive Ease / Fluency Illusion
│   │
│   └── Anchoring-Based
│       ├── Anchoring & Adjustment Bias
│       └── Framing Effect (reference-point dependence)
│
├── SELF-ASSESSMENT BIASES
│   │
│   ├── Overconfidence Bias (calibration gap)
│   ├── Dunning-Kruger Effect (metacog. deficit)
│   └── Curse of Knowledge (can't unlearn)
│
├── MOTIVATED / BELIEF-PROTECTIVE BIASES
│   │
│   ├── Confirmation Bias
│   │   ├── Search stage (seek confirming evidence)
│   │   ├── Interpretation stage (ambiguity → confirm)
│   │   └── Memory stage (better recall of confirming)
│   │
│   ├── Belief Bias (conclusion acceptability > logic)
│   └── Myside Bias (asymmetric argument generation)
│
└── DECISION / ECONOMIC BIASES
    │
    ├── Loss Aversion (losses ~2× gains)
    ├── Endowment Effect
    ├── Status Quo Bias
    ├── Sunk Cost Fallacy
    └── Hyperbolic Discounting (present bias)
```

**Reading guide:** The four top-level branches correspond to the four generating mechanisms. Heuristic-generated biases (largest branch) arise from adaptive shortcuts misfiring; self-assessment biases from poor metacognitive access; motivated biases from goals overriding accuracy; decision biases from Prospect Theory's value function. Confirmation bias spans three stages — making it uniquely pervasive. The final branch maps directly to the Behavioural Economics section.

**Source:** §The Cognitive Bias Catalogue; §Behavioural Economics; §Motivated Reasoning

---

## Visual Aid 4: Intellectual Genealogy — From Founders to Applications

**Purpose:** Maps the intellectual lineage from foundational researchers to theoretical frameworks to applied domains, showing how ideas built on each other.

```
INTELLECTUAL GENEALOGY OF DUAL-PROCESS THEORY & COGNITIVE BIASES
══════════════════════════════════════════════════════════════════════

FOUNDATIONAL FIGURES
═══════════════════
Kahneman ──┐
           ├──► HEURISTICS & BIASES PROGRAMME (1970s) ──►──┐
Tversky ───┘    (availability, representativeness,           │
                 anchoring, framing)                         │
                        │                                    │
                        ▼                                    │
               PROSPECT THEORY (1979) ───────────────────►──┤
               (loss aversion, value fn,                     │
                probability weighting)                       │
                                                             │
Slovic ────────► AFFECT HEURISTIC (1990s) ───────────────►──┤
                 (risk-benefit confound)                     │
                                                             ▼
Stanovich ─────► DUAL-PROCESS THEORY ────────────────────►  SYNTHESIS
& West            (System 1 / System 2)                     FRAMEWORK
(formal)                │                                    │
                        ▼                                    │
Evans ─────────► DEFAULT-INTERVENTIONIST ────────────────►──┘
                 ARCHITECTURE
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
BEHAVIOURAL       DEBIASING       MOTIVATED
ECONOMICS         RESEARCH        REASONING
│                 │               │
Thaler &          Cognitive       Kunda
Sunstein          Forcing         (directional
│                 Functions       vs accuracy
▼                                 goals)
NUDGE THEORY ◄── Choice ─────────────────────
                 Architecture
                 design

     CONTESTED FRONTIER
     ══════════════════
     Gigerenzen ──► Ecological Rationality
     ("heuristics are adaptive, not biased")
           ▲
           │  ONGOING DEBATE
           ▼
     K&T tradition ──► "Biases are real, not artifacts"
```

**Reading guide:** Read the genealogy top-to-bottom, left-to-right. The left column shows the researchers; arrows show intellectual inheritance. The three bottom branches show how the unified framework splits into three applied programmes. The bottom box is the live debate — Gigerenzen's ecological rationality challenges the entire biases-as-errors framing and has no resolution yet.

**Source:** §The Heuristics Program; §Behavioural Economics; §Frontier & Open Questions

---

## Visual Aid 5: Heuristic → Bias Pipeline (Causal Architecture)

**Purpose:** Shows the specific causal chain from heuristic shortcut through its triggering condition to the resulting bias and real-world domain where it causes harm.

```
╔══════════════════════════════════════════════════════════════════════╗
║              HEURISTIC → BIAS CAUSAL PIPELINE                        ║
╠══════════════════════╤═══════════════════╤═════════════════╤═════════╣
║ HEURISTIC            │ TRIGGERING        │ RESULTING BIAS  │ DOMAIN  ║
║ (the shortcut)       │ CONDITION         │                 │ FAILURE ║
╠══════════════════════╪═══════════════════╪═════════════════╪═════════╣
║                      │ Vivid / recent    │ Overestimate    │ Risk    ║
║ AVAILABILITY         │ event dominates   │ rare dramatic   │ percep- ║
║ frequency ≈          │ frequency         │ events          │ tion,   ║
║ ease of recall       ├───────────────────┼─────────────────┤ policy  ║
║                      │ Media coverage    │ Recency Effect  │ support ║
╠══════════════════════╪═══════════════════╪═════════════════╪═════════╣
║                      │ Description fits  │ Conjunction     │ Legal   ║
║ REPRESENTATIVENESS   │ prototype well    │ Fallacy         │ judg-   ║
║ probability ≈        ├───────────────────┼─────────────────┤ ment,   ║
║ resemblance          │ Case info vivid   │ Base-Rate       │ clinical║
║                      │ vs. base rate dull│ Neglect         │ diagn.  ║
║                      ├───────────────────┼─────────────────┤         ║
║                      │ Sequence "looks   │ Gambler's       │ gambling║
║                      │ non-random"       │ Fallacy         │         ║
╠══════════════════════╪═══════════════════╪═════════════════╪═════════╣
║ AFFECT               │ Technology feels  │ Risk-Benefit    │ Policy  ║
║ judgment ≈           │ threatening       │ Confound (risks │ making, ║
║ emotional valence    │                   │ ↑ benefits ↓)   │ health  ║
╠══════════════════════╪═══════════════════╪═════════════════╪═════════╣
║ ANCHORING            │ Initial number    │ Insufficient    │ salary  ║
║ estimate ≈           │ encountered first │ adjustment      │ negot., ║
║ proximity to anchor  │                   │                 │ diagn.  ║
╠══════════════════════╪═══════════════════╪═════════════════╪═════════╣
║ NOTE: All four heuristics share a common pathway:                    ║
║  System 1 substitutes an *easier question* for the *harder one*      ║
║  (attribute substitution — Kahneman & Frederick, 2002)               ║
╚══════════════════════╧═══════════════════╧═════════════════╧═════════╝
```

**Reading guide:** Each row is a complete causal chain: the heuristic (the processing default), its triggering condition (what makes it misfire), the resulting bias (the specific error pattern), and the real-world failure domain. The bottom note names the unifying mechanism — attribute substitution — that connects all four heuristics at the computational level.

**Source:** §The Heuristics Program

---

## Visual Aid 6: Three Heuristics — Comparative Analysis

**Purpose:** A structured cross-comparison of the three main heuristics on five analytical dimensions.

```
┌──────────────────────┬──────────────────┬──────────────────┬──────────────┐
│ DIMENSION            │ AVAILABILITY     │ REPRESENTAT.     │ AFFECT       │
├──────────────────────┼──────────────────┼──────────────────┼──────────────┤
│ Core substitution    │ frequency →      │ probability →    │ judgment →   │
│                      │ ease of recall   │ resemblance      │ emotion      │
├──────────────────────┼──────────────────┼──────────────────┼──────────────┤
│ Canonical study      │ Shark vs. car    │ Linda the        │ Nuclear      │
│                      │ deaths; causes   │ feminist bank    │ power risk-  │
│                      │ of death ranking │ teller problem   │ benefit study│
├──────────────────────┼──────────────────┼──────────────────┼──────────────┤
│ When adaptive        │ Environments     │ Categories are   │ Emotional    │
│                      │ where frequency  │ stable and       │ responses    │
│                      │ ≈ memorability   │ diagnostic       │ track real   │
│                      │                  │                  │ value        │
├──────────────────────┼──────────────────┼──────────────────┼──────────────┤
│ When it fails        │ Vivid/recent     │ Prototype fits   │ Affect        │
│                      │ drives recall    │ but base rates   │ decoupled    │
│                      │ not frequency    │ contradict       │ from actual  │
│                      │                  │                  │ risk         │
├──────────────────────┼──────────────────┼──────────────────┼──────────────┤
│ Signature biases     │ • Recency effect │ • Conj. fallacy  │ • Risk-      │
│                      │ • Hindsight bias │ • Base-rate neg. │   benefit    │
│                      │ • Risk misestim. │ • Gambler's fall.│   confound   │
├──────────────────────┼──────────────────┼──────────────────┼──────────────┤
│ Debiasing lever      │ Consider base    │ Explicitly state │ Slow down;   │
│                      │ rates; slow down │ prior prob.;     │ consider     │
│                      │                  │ decompose        │ attributes   │
│                      │                  │                  │ separately   │
├──────────────────────┼──────────────────┼──────────────────┼──────────────┤
│ Evidence strength    │  ★★★★★           │  ★★★★★           │  ★★★★☆       │
└──────────────────────┴──────────────────┴──────────────────┴──────────────┘
```

**Reading guide:** Read column-by-column for a deep profile of each heuristic, or row-by-row to compare them on a single dimension. The debiasing row is practically critical: each heuristic requires a different intervention because they operate through different substitution mechanisms. The "When adaptive" row reflects the Gigerenzen challenge — these are not pure defects.

**Source:** §The Heuristics Program

---

## Visual Aid 7: Where Biases Strike — Decision Cycle Swimlane

**Purpose:** Shows which biases operate at which stage of the decision cycle, revealing that biases are not monolithic but target specific cognitive operations.

```
╔══════════════════════════════════════════════════════════════════════╗
║          BIASES MAPPED TO DECISION CYCLE STAGE                       ║
╠═══════════════╦══════════════════════════════════════════════════════╣
║               ║  STAGE 1   │  STAGE 2   │  STAGE 3   │  STAGE 4    ║
║               ║  PERCEIVE  │  INTERPRET │  EVALUATE  │  CHOOSE     ║
║               ║  & ENCODE  │  & INFER   │  OPTIONS   │  & COMMIT   ║
╠═══════════════╬════════════╪════════════╪════════════╪═════════════╣
║  AVAILABILITY ║ Availability│            │ Risk       │             ║
║  HEURISTIC    ║ Bias ✓     │            │ misestim.  │             ║
╠═══════════════╬════════════╪════════════╪════════════╪═════════════╣
║  REPRESENT.   ║            │ Base-rate  │ Conjunction│             ║
║  HEURISTIC    ║            │ Neglect ✓  │ Fallacy ✓  │             ║
╠═══════════════╬════════════╪════════════╪════════════╪═════════════╣
║  CONFIRMATION ║ Selective  │ Interpret  │ Selective  │             ║
║  BIAS         ║ search ✓   │ as confirm.│ recall ✓   │             ║
╠═══════════════╬════════════╪════════════╪════════════╪═════════════╣
║  ANCHORING    ║ Anchor set │            │ Insuff.    │             ║
║               ║ ✓          │            │ adjust. ✓  │             ║
╠═══════════════╬════════════╪════════════╪════════════╪═════════════╣
║  FRAMING      ║            │ Reference  │ Value      │             ║
║  EFFECT       ║            │ point set ✓│ distorted ✓│             ║
╠═══════════════╬════════════╪════════════╪════════════╪═════════════╣
║  LOSS         ║            │            │ Loss ~2×   │ Status quo  ║
║  AVERSION     ║            │            │ gain ✓     │ bias ✓      ║
╠═══════════════╬════════════╪════════════╪════════════╪═════════════╣
║  MOTIVATED    ║            │ Goal-dir.  │ Myside     │ Commit to   ║
║  REASONING    ║            │ interpret. │ argument ✓ │ prior ✓     ║
╠═══════════════╬════════════╪════════════╪════════════╪═════════════╣
║ ✓ = primary   ║            │            │            │             ║
║   stage of    ║ EARLY ─────┼────────────┼────────────┼──────► LATE ║
║   action      ║            │            │            │             ║
╚═══════════════╩════════════╧════════════╧════════════╧═════════════╝
```

**Reading guide:** Each row is a bias; each column is a decision stage. A ✓ marks where that bias most actively operates. Confirmation bias spans three columns — uniquely pervasive because it corrupts input, processing, and memory simultaneously. Loss aversion is a late-stage bias, acting primarily at the point of choice. This map informs debiasing design: interventions must target the correct stage.

**Source:** §The Cognitive Bias Catalogue; §Motivated Reasoning; §Behavioural Economics

---

## Visual Aid 8: Evidence Ledger — Key Claims and Their Support

**Purpose:** Evaluates the epistemic status of the MOC's core claims, mapping each to its evidence base and strength.

```
┌──────────────────────────────────┬─────────────────┬──────────┬───────┐
│ CLAIM                            │ EVIDENCE TYPE   │ STRENGTH │ §     │
├──────────────────────────────────┼─────────────────┼──────────┼───────┤
│ Availability drives freq. judg.  │ Experimental,   │ ★★★★★   │ §H    │
│ (ease of recall ≠ freq.)         │ replicated      │          │       │
├──────────────────────────────────┼─────────────────┼──────────┼───────┤
│ Conjunction fallacy (Linda prob) │ Experimental,   │ ★★★★★   │ §H    │
│                                  │ cross-cultural  │          │       │
├──────────────────────────────────┼─────────────────┼──────────┼───────┤
│ Loss aversion (~2× gains)        │ Experimental +  │ ★★★★★   │ §BE  │
│                                  │ field studies   │          │       │
├──────────────────────────────────┼─────────────────┼──────────┼───────┤
│ Framing effects on medical       │ Experimental,   │ ★★★★★   │ §BC  │
│ treatment choice                 │ wide replication│          │       │
├──────────────────────────────────┼─────────────────┼──────────┼───────┤
│ Anchoring from arbitrary numbers │ Experimental    │ ★★★★☆   │ §BC  │
│                                  │ (some variance) │          │       │
├──────────────────────────────────┼─────────────────┼──────────┼───────┤
│ Dunning-Kruger: low skill →      │ Correlational + │ ★★★★☆   │ §BC  │
│ overestimated competence         │ contested replic│          │       │
├──────────────────────────────────┼─────────────────┼──────────┼───────┤
│ Affect heuristic: risk-benefit   │ Survey +        │ ★★★★☆   │ §H    │
│ confound driven by affect        │ experimental    │          │       │
├──────────────────────────────────┼─────────────────┼──────────┼───────┤
│ Debiasing: education about       │ Meta-analysis   │ ★★★☆☆   │ §D    │
│ biases → small, inconsist. effect│                 │          │       │
├──────────────────────────────────┼─────────────────┼──────────┼───────┤
│ Cognitive forcing functions      │ Clinical +      │ ★★★☆☆   │ §D    │
│ reduce diagnostic errors         │ experimental    │          │       │
├──────────────────────────────────┼─────────────────┼──────────┼───────┤
│ Heuristics are ecologically      │ Mathematical +  │ ★★★☆☆   │ §FQ  │
│ rational (Gigerenzen)            │ some field data │          │       │
│                                  │ CONTESTED       │          │       │
└──────────────────────────────────┴─────────────────┴──────────┴───────┘
§H=Heuristics §BE=Behavioural Econ §BC=Bias Catalogue §D=Debiasing §FQ=Frontier
```

**Reading guide:** Read top-to-bottom by evidence strength. The top five are among the most robustly replicated findings in cognitive psychology. The debiasing claims are notably weaker — a critical limitation for practitioners. Gigerenzen's ecological rationality claim remains contested and should not be treated as settled. ★★★★★ = multiple replications across methods and cultures; ★★★☆☆ = established but qualified.

**Source:** All sections

---

## Visual Aid 9: Before / After — Biased vs. Debiased Decision Environment

**Purpose:** Contrasts the features of a default (bias-prone) decision environment with a redesigned (bias-mitigating) one.

```
┌────────────── DEFAULT ENVIRONMENT ───────────┬──────── REDESIGNED ENVIRONMENT ──────────┐
│ (System 2 rarely triggered)                  │ (System 2 engagement by design)          │
├──────────────────────────────────────────────┼──────────────────────────────────────────┤
│ Decision point arrives without               │ Structured pause / checklist             │
│ prompting reflection                         │ embedded at decision point               │
├──────────────────────────────────────────────┼──────────────────────────────────────────┤
│ Information framed however                   │ Information presented in multiple        │
│ it naturally arrives                         │ frames (survival AND mortality rates)    │
├──────────────────────────────────────────────┼──────────────────────────────────────────┤
│ Default option = doing nothing               │ Default option = beneficial behaviour;   │
│ (inertia benefits inaction)                  │ opt-out rather than opt-in               │
├──────────────────────────────────────────────┼──────────────────────────────────────────┤
│ Single numerical anchor given                │ Range of values / base rates provided    │
│ with no context                              │ before specific estimates                │
├──────────────────────────────────────────────┼──────────────────────────────────────────┤
│ Decisions made under time pressure           │ High-stakes decisions flagged for        │
│ and cognitive load                           │ "slow down" protocol                     │
├──────────────────────────────────────────────┼──────────────────────────────────────────┤
│ No prompts to consider                       │ "Consider the opposite" prompts built    │
│ disconfirming evidence                       │ into assessment process                  │
├──────────────────────────────────────────────┼──────────────────────────────────────────┤
│ Individual judgment with no                  │ Structured argument/red-team process     │
│ devil's advocate role                        │ before commitment                        │
├──────────────────────────────────────────────┼──────────────────────────────────────────┤
│ Bias education in training                   │ Cognitive forcing functions at           │
│ (general, removed from context)              │ decision point (contextual, timely)      │
├──────────────────────────────────────────────┼──────────────────────────────────────────┤
│ RESULT: System 1 defaults dominate           │ RESULT: System 2 engaged selectively     │
│ • Framing effects unchecked                  │ • Anchor awareness raised                │
│ • Anchors drive estimates                    │ • Defaults nudge toward beneficial       │
│ • Confirmation unchallenged                  │ • Structured disconfirmation built in    │
│ • Loss aversion blocks good choices          │ • Loss aversion partly neutralised       │
└──────────────────────────────────────────────┴──────────────────────────────────────────┘
```

**Reading guide:** Read left-to-right for each row — left is the unmodified environment, right is the intervention. The crucial design insight is that effective debiasing does not tell people about biases (left-column training); it redesigns the choice environment so that System 2 is triggered structurally, without relying on individual effort or memory.

**Source:** §Debiasing: What Works; §Behavioural Economics (choice architecture / nudge theory)

---

## Visual Aid 10: TL;DR Scorecard

**Purpose:** Single-page summary integrating the MOC's thesis, strongest evidence, critical limitations, and actionable implications.

```
╔══════════════════════════════════════════════════════════════════════╗
║           TL;DR SCORECARD — DUAL PROCESS THEORY & BIASES            ║
╠══════════════════════════════════════════════════════════════════════╣
║ CORE THESIS   : Two qualitatively distinct processing modes (fast    ║
║                 automatic S1 / slow deliberate S2) generate          ║
║                 predictable, systematic biases when S1 dominates     ║
║                 and S2 fails to intervene.                           ║
╠══════════════════════════════════════════════════════════════════════╣
║ STRONGEST     : Loss aversion (~2× asymmetry) ★★★★★                ║
║ EVIDENCE      : Conjunction fallacy (cross-cultural) ★★★★★          ║
║                 Availability → frequency distortion ★★★★★           ║
║                 Framing effects on consequential choice ★★★★★       ║
╠══════════════════════════════════════════════════════════════════════╣
║ CRITICAL      : Debiasing via education is weak ★★★☆☆               ║
║ LIMITATIONS   : Two-systems metaphor may be too discrete            ║
║                 Gigerenzen challenge: heuristics may be optimal     ║
║                 Most biases operate below voluntary control          ║
╠══════════════════════════════════════════════════════════════════════╣
║ KEY ACTION 1  : Design environments (choice architecture, defaults,  ║
║                 cognitive forcing functions) rather than training     ║
║                 individuals to resist biases                         ║
╠══════════════════════════════════════════════════════════════════════╣
║ KEY ACTION 2  : Distinguish which stage a bias operates at           ║
║                 (perception → interpretation → evaluation → choice)  ║
║                 and intervene at THAT stage                          ║
╠══════════════════════════════════════════════════════════════════════╣
║ KEY ACTION 3  : For high-stakes decisions, build in structured       ║
║                 "consider the opposite" and pre-mortem protocols     ║
╠══════════════════════════════════════════════════════════════════════╣
║ READ IF YOU   : Design decision systems, teach critical thinking,    ║
║                 research judgment, or make consequential choices      ║
╠══════════════════════════════════════════════════════════════════════╣
║ OPEN QUESTION : Can systemic-level interventions (process redesign,  ║
║                 team protocols, institutional rules) achieve what     ║
║                 individual debiasing cannot?                         ║
╚══════════════════════════════════════════════════════════════════════╝
```

---

## Synthesis Packet

**Top 5 Takeaways:**
1. The dominant failure mode is not System 1 running wild — it is System 2 failing to engage. Triggering deliberation is the central design challenge.
2. Biases are not a random list; they cluster by generating mechanism (heuristic-based, self-assessment, motivated, decision-economic), each requiring different interventions.
3. The three core heuristics (availability, representativeness, affect) are adaptive shortcuts that fail in predictable, specifiable conditions — not defects.
4. Debiasing through education is weak. Cognitive forcing functions and choice architecture work because they intervene at the point of decision, not in the training room.
5. The ecological rationality debate (Gigerenzen) is live and unresolved — the claim that biases are real errors rather than adaptive tools is contested, not settled.

**Navigator — which aid answers which question:**

| Question | Aid |
|---|---|
| "How do System 1 and System 2 actually interact?" | Aid 1 (Process Flow) |
| "What exactly are the differences between the two systems?" | Aid 2 (Comparison Matrix) |
| "What biases are there and how are they related?" | Aid 3 (Taxonomy Tree) |
| "Who developed these ideas and how?" | Aid 4 (Genealogy Map) |
| "Which heuristic produces which bias?" | Aid 5 (Causal Pipeline) |
| "How are the three heuristics different from each other?" | Aid 6 (Heuristic Comparison) |
| "At what point in a decision does each bias strike?" | Aid 7 (Swimlane) |
| "How confident should I be in these claims?" | Aid 8 (Evidence Ledger) |
| "What does a well-designed decision environment look like?" | Aid 9 (Before/After) |
| "What's the one-page takeaway?" | Aid 10 (Scorecard) |

**PKB Vault Links for this Suite:**
[[Dual-Process-Theory]] · [[System-1]] · [[System-2]] · [[Availability-Heuristic]] · [[Representativeness-Heuristic]] · [[Affect-as-Information-Theory]] · [[Anchoring-Effects]] · [[Confirmation-Bias]] · [[Dunning-Kruger-Effect]] · [[Framing-Effect]] · [[Prospect-Theory]] · [[Loss-aversion]] · [[Motivated-Reasoning]] · [[Cognitive-Forcing-Functions]] · [[Debiasing-Interventions]] · [[Bounded-Rationality]] · [[choice-architecture]] · [[Ecological-Rationality]]