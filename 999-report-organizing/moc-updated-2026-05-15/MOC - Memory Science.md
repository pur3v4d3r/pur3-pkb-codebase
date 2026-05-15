---
tags: [moc, domain-memory, domain-cognitive-science, status-evergreen]
aliases: [Memory MOC, Memory Systems MOC]
created: 2026-05-15
modified: 2026-05-15
status: evergreen
type: moc
moc_pattern: hub-and-spoke
domain: Memory Science
source_notes_count: 62
target_word_count: 6000
audience: [practitioner, researcher]
maturity: established
parent_moc: "[[MOC - Cognitive Science (Master Index)]]"
related_mocs: ["[[MOC - Cognitive Load Theory]]", "[[MOC - Learning Science]]", "[[MOC - Metacognition and Self-Regulated Learning]]"]
version: 1.0.0
---

# Memory Science — Map of Content

> [!abstract] Domain & Scope
> **Memory science** is the empirical and theoretical study of how information is encoded, stored, consolidated, and retrieved by biological and cognitive systems. This MOC organises 62 permanent notes covering memory architecture, encoding processes, consolidation mechanisms, retrieval dynamics, forgetting, working memory, and the neuroscience underpinning all of these. It is structured as a **hub-and-spoke** model — the central hub being memory as an *active reconstructive system* rather than a passive recording device, with spokes radiating into architecture, encoding, consolidation, retrieval, forgetting, and application.
>
> **For**: Practitioners and researchers in learning science, cognitive psychology, instructional design
> **Companion MOCs**: [[MOC - Cognitive Load Theory]], [[MOC - Learning Science]], [[MOC - Metacognition and Self-Regulated Learning]]
> **Reading time**: ~30 minutes for full read; sections can be entered independently.

## 🗺️ Navigation

- **[The Central Claim](#the-central-claim)** — memory as reconstructive, not reproductive
- **[Memory Architecture](#memory-architecture)** — the systems and their relationships
- **[Working Memory: The Cognitive Bottleneck](#working-memory-the-cognitive-bottleneck)** — Baddeley's model and capacity limits
- **[Encoding: What Gets In](#encoding-what-gets-in)** — depth, elaboration, specificity
- **[Consolidation: What Sticks](#consolidation-what-sticks)** — sleep, synaptic change, reconsolidation
- **[Retrieval: The Practice That Builds Memory](#retrieval-the-practice-that-builds-memory)** — testing effect, spacing, interleaving
- **[Forgetting: Adaptive and Pathological](#forgetting-adaptive-and-pathological)** — interference, decay, retrieval failure
- **[Metacognitive Monitoring of Memory](#metacognitive-monitoring-of-memory)** — JOLs, FOK, fluency illusions
- **[Cross-Domain Bridges](#cross-domain-bridges)** — connections to other MOCs
- **[Frontier & Open Questions](#frontier--open-questions)** — what remains unresolved
- **[Index of Linked Notes](#index-of-linked-notes)** — flat alphabetical reference

> [!progression] Reading Paths
> - **First-time visitor**: Read §1–3 (The Central Claim, Architecture, Working Memory), then skip to Retrieval.
> - **Instructional designer**: Focus on Encoding, Retrieval, and Forgetting — these are the most directly actionable.
> - **Researcher**: Read sequentially; the Frontier section synthesises open problems.

---

## The Central Claim

[Concept-Class:: Hub]

The foundational insight of contemporary memory science is captured in [[source-information-is-cognitively-constructed-not-mechanically-recorded|Source Information Is Cognitively Constructed, Not Mechanically Recorded]]: memory is not a camera. When we encode an experience, we do not make a fidelity copy — we extract, infer, and integrate information with prior knowledge, emotion, and expectations. When we retrieve, we *reconstruct* rather than *reproduce*. This reconstruction is efficient and adaptive, but it also generates systematic errors.

The implications cascade through every other area of memory science. If encoding is constructive, then what we attend to, how deeply we process it, and what prior knowledge we bring to bear all shape what survives. If retrieval is reconstructive, then [[false-memory|false memories]] are not anomalies but natural byproducts of a system built for pattern-completion rather than verbatim storage. [[source-monitoring|Source monitoring]] errors — misremembering where or from whom information came — are not bugs but features of a system that prioritizes *what* over *where*.

> [!key-claim] Memory's Fundamental Design Principle
> Memory did not evolve to be a faithful archive. It evolved to support *adaptive action*. This means it prioritises gist over detail, relevance over completeness, and prediction over accuracy. Every forgetting and distortion phenomenon makes sense in this evolutionary light.

[Domain-Maturity:: Established]

---

## Memory Architecture

[[memory-systems|Memory systems]] are conventionally divided along two major axes: *duration* (short-term vs long-term) and *content type* (declarative vs non-declarative).

### The Multi-Store Architecture

The [[multi-store-model|multi-store model]] proposed by Atkinson and Shiffrin (1968) established the canonical framework: sensory registers feed into short-term memory (STM), which feeds into [[long-term-memory|long-term memory]] (LTM) via rehearsal. While subsequent research has substantially refined every component, the basic architecture remains influential as a pedagogical tool. The critical limitation of this model is its treatment of STM as a unitary, passive buffer — a limitation Baddeley and Hitch's working memory model directly addresses (see Working Memory section below).

Long-term memory itself bifurcates into two major branches:

```
Long-Term Memory
├── Declarative (Explicit) ─── Episodic (personally dated events)
│                          └── Semantic (general world knowledge)
└── Non-Declarative (Implicit) ─── Procedural (skills, habits)
                               ├── Priming
                               └── Conditioning
```

[[declarative-memory|Declarative memory]] is the domain of conscious recollection — the things you *know that* you know. [[episodic-memory|Episodic memory]] is specifically autobiographical, situating knowledge in a personal time-place context. [[semantic-memory|Semantic memory]] is decontextualised factual knowledge: that Paris is the capital of France carries no necessary memory of when or where you learned it. [[procedural-memory|Procedural memory]] and [[non-declarative-memory|non-declarative memory]] more broadly operate below the threshold of conscious access — a pianist's finger movements, the reflexive recoil from a hot surface.

> [!definition] Autobiographical Memory
> [[autobiographical-memory|Autobiographical memory]] is the superordinate system that integrates episodic and semantic memory about the self across time. It is constitutive of personal identity and is disproportionately susceptible to [[emotional-memory-enhancement|emotional enhancement]] — high-arousal events are remembered more vividly, though not necessarily more accurately.

### Memory in the Knowledge Ecosystem

The architecture distinction matters practically: [[schema-theory|schema theory]] reveals that long-term semantic memory is not a flat list but a structured network of [[schema|schemas]] — organised knowledge frameworks that guide encoding and retrieval. When new information fits a pre-existing schema, encoding is efficient and retrieval is facilitated. When information contradicts a schema, [[cognitive-disequilibrium|cognitive disequilibrium]] arises, requiring [[conceptual-change|conceptual change]] — a process that is effortful but produces deeper encoding.

[Prerequisite-For:: [[MOC - Cognitive Load Theory]]]

---

## Working Memory: The Cognitive Bottleneck

[[working-memory|Working memory]] is the cognitive workspace — the limited-capacity system that holds information in an active, manipulable state for ongoing cognitive operations. It is the system most directly relevant to learning, because everything we consciously process must pass through it.

### Baddeley's Multicomponent Model

The [[baddeley-and-hitch-working-memory-model|Baddeley and Hitch working memory model]] replaced the unitary STM with four interacting components:

```
                ┌─────────────────────────────────┐
                │       CENTRAL EXECUTIVE          │
                │  (attentional control, planning) │
                └───────┬───────────┬──────────────┘
                        │           │
              ┌─────────┴──┐   ┌────┴──────────────┐
              │ PHONOLOGICAL│   │  VISUOSPATIAL      │
              │   LOOP      │   │   SKETCHPAD        │
              │(verbal/audio)│   │(spatial/visual)   │
              └─────────────┘   └───────────────────┘
                        │           │
                ┌───────┴───────────┴──────────────┐
                │         EPISODIC BUFFER           │
                │  (integrates info; LTM interface)  │
                └──────────────────────────────────-┘
```

The [[central-executive|central executive]] is the controlling system — it allocates attention, coordinates the slave systems, and switches between tasks. The [[phonological-loop|phonological loop]] handles verbal and acoustic information; it is responsible for the inner voice. The [[visuospatial-sketchpad|visuospatial sketchpad]] processes spatial and visual information. The [[episodic-buffer|episodic buffer]] — added in 2000 — serves as a temporary integrative interface between working memory and long-term memory.

### Capacity and the Magical Number

[[working-memory-capacity|Working memory capacity]] is severely limited. Miller's original claim of [[magical-number-seven|seven ± two chunks]] has been refined downward: contemporary estimates suggest 3–4 meaningful units for most cognitive tasks. This constraint is not a flaw but a fundamental boundary of cognitive architecture — it is why [[cognitive-load-theory|Cognitive Load Theory]] exists as a field (see [[MOC - Cognitive Load Theory]]).

[[chunking|Chunking]] — the process of combining individual elements into meaningful units — is the primary mechanism by which expertise expands effective working memory capacity. A chess master perceives not 32 individual pieces but recognisable patterns; an expert programmer reads not individual tokens but meaningful code structures. [[chunk|Chunks]] are built through extensive experience and encoded in long-term memory schemas, which working memory can then reference as single units.

[[working-memory-updating|Working memory updating]] — the ability to displace old information with new, relevant information — is one of three executive functions (alongside inhibition and shifting) that predict higher-level cognitive performance across domains.

> [!key-claim] The Bottleneck Is the Teaching Problem
> Every instructional decision is ultimately a working memory management decision. When students fail to learn, the failure frequently occurs in working memory before information ever reaches long-term storage. This makes [[working-memory-in-the-clt-framework|working memory in the CLT framework]] the most practically consequential idea in instructional design.

[Synthesis-With:: [[MOC - Cognitive Load Theory]]]

---

## Encoding: What Gets In

Encoding is not mere registration — it is transformation. The question is not whether information enters the system but in *what form* and with *what durability*.

### Levels of Processing

[[levels-of-processing|Levels of processing]] (Craik & Lockhart, 1972) established that the *depth* of cognitive analysis performed during encoding predicts retention. Shallow processing — orthographic analysis ("is this word in capital letters?") — produces weak, transient traces. [[deep-processing|Deep processing]] — semantic analysis ("does this word fit in the sentence?") — produces durable, elaborated traces.

The mechanism is [[elaborative-encoding|elaborative encoding]]: connecting incoming information to existing knowledge through inference, example generation, and schema activation. [[elaboration|Elaboration]] is to memory what mortar is to masonry — it binds new material to the existing structure. This is why [[elaborative-interrogation|elaborative interrogation]] (asking "why is this true?") is among the most effective study strategies.

[[encoding-depth|Encoding depth]] is modulated by [[prior-knowledge|prior knowledge]]: learners with rich existing schemas encode new related information more efficiently, because they have more connection points. This creates a virtuous cycle — knowing more makes it easier to know more — with direct implications for curriculum sequencing.

### Encoding Specificity and Variability

[[encoding-specificity-principle|Encoding specificity]] (Tulving & Thomson, 1973) establishes that retrieval is maximised when cues at retrieval match cues at encoding. This has a counterintuitive implication: the same information, encoded in multiple different contexts, is more robustly accessible than information encoded in a single rich context. [[encoding-variability|Encoding variability]] — deliberately varying the conditions, examples, and contexts of learning — increases the probability that some retrieval cue will match the encoding context.

[[context-dependent-memory|Context-dependent memory]] and [[state-dependent-memory|state-dependent memory]] are specific instances of the encoding specificity principle: memory retrieval is facilitated when the external environment or internal physiological state at retrieval matches that at encoding. The practical implication is that studying in varied contexts, rather than always at the same desk, may improve performance in novel test environments.

---

## Consolidation: What Sticks

Encoding produces an initial trace that is initially labile — vulnerable to interference and disruption. Consolidation is the set of processes that gradually stabilise and transform this trace into a durable long-term memory.

### Synaptic and Systems Consolidation

At the cellular level, [[synaptic-plasticity|synaptic plasticity]] — specifically [[long-term-potentiation|long-term potentiation]] (LTP) — is the substrate of memory formation. When neurons fire together repeatedly, the synaptic connections between them are strengthened, following the principle broadly attributed to Hebb. This strengthening depends on protein synthesis and can be disrupted by metabolic interference in the hours following learning.

At the systems level, [[hippocampal-neocortical-transfer|hippocampal-neocortical transfer]] describes the process by which memories initially dependent on the hippocampus are gradually re-encoded in cortical networks for long-term storage. The hippocampus acts as an indexer and initial binder of disparate cortical representations; over time — particularly during sleep — memories become more cortically distributed and less hippocampally dependent.

### Sleep and Memory

[[sleep-and-memory-consolidation|Sleep]] is the primary biological mechanism for memory consolidation. [[sleep-stages-and-memory|Different sleep stages serve different memory functions]]: REM sleep preferentially consolidates procedural and emotional memories, while slow-wave (deep NREM) sleep consolidates declarative and semantic memories. Total sleep deprivation following a learning session dramatically impairs recall the following day — not through general fatigue effects but through specific failure of the consolidation process.

[[reconsolidation|Reconsolidation]] introduces a further complexity: memories are not stored once and remain stable thereafter. Each time a memory is retrieved, it becomes temporarily labile and must be reconsolidated. This means active retrieval is not just a test of memory — it is an act that modifies memory, potentially updating it with new information or strengthening the trace.

> [!key-claim] Sleep Is Not Optional for Learning
> A learning session followed by insufficient sleep does not simply delay consolidation — it may permanently impair it. The cognitive cost of sleep deprivation on learning is disproportionately severe relative to its effects on general performance.

### Neurochemical Modulation

Memory consolidation is modulated by neuromodulatory systems. [[cortisol-and-memory|Cortisol]] at moderate levels enhances encoding for emotionally relevant information (the amygdala-hippocampus interaction) but at high levels (chronic stress) impairs hippocampal function. [[dopamine-and-learning|Dopamine]] signals prediction error — unexpected reward or punishment — and gates what gets consolidated. [[acetylcholine-and-memory|Acetylcholine]] plays a critical role in attentional selection and initial encoding. [[norepinephrine-and-learning|Norepinephrine]] preferentially enhances consolidation of emotionally arousing material, explaining [[flashbulb-memory|flashbulb memories]]' subjective vividness.

---

## Retrieval: The Practice That Builds Memory

The most consequential insight from modern memory science is that retrieval is not merely a *test* of memory — it is the most powerful *builder* of memory. The [[testing-effect|testing effect]] (also called the retrieval practice effect) establishes that effortful retrieval of information strengthens the memory trace more than additional study of the same material.

### Why Retrieval Practice Works

[[retrieval-practice|Retrieval practice]] works through two complementary mechanisms. First, successful retrieval *restores* the memory trace and updates retrieval pathways, making future retrieval more probable and faster. Second — and more powerfully — the [[generation-effect|generation effect]] shows that the effort of retrieving information (even with errors, via [[hypercorrection-effect|hypercorrection]]) creates richer encoding than passive restudying.

[[retrieval-practice-as-the-most-potent-single-strategy|Retrieval practice is the most potent single study strategy]] across virtually all domains, populations, and retention intervals. [[active-recall|Active recall]] — generating answers from memory rather than recognising them — is more effective than [[recognition-memory|recognition]] precisely because of the greater retrieval effort required.

### Spacing and Interleaving

[[spacing-effect|The spacing effect]] is one of the most robust phenomena in memory science: distributing study sessions across time produces far greater long-term retention than massed practice, even with equal total study time. [[spaced-repetition|Spaced repetition]] systems — including the [[leitner-system|Leitner system]] and digital implementations — automate optimal spacing by scheduling reviews at expanding intervals calibrated to the forgetting curve.

[[interleaving-effect|Interleaving]] — alternating between different types of material or problem types — produces superior long-term learning compared to [[blocked-practice|blocked practice]], despite feeling less efficient during acquisition. The mechanism involves *discriminative contrast*: interleaving forces learners to identify which knowledge or strategy applies to which type of problem, deepening category-level encoding.

```
Spacing Effect: Retention vs. Study Distribution
─────────────────────────────────────────────────
   100% ┤
        │  ┌─ Spaced (3 sessions, distributed)
    80% ┤  │
        │  │      ┌─ Massed (3 sessions, consecutive)
    60% ┤  │      │
        │  │      │
    40% ┤  │      │
        │  │      │
    20% ┤  │      │
        │              
     0% ┤────────────────────────────────────────
        ↑ Study     1 week     2 weeks    1 month
```

### Spaced Retrieval Architecture

[[spaced-retrieval|Spaced retrieval]] specifically combines both principles: spacing the act of retrieval, rather than re-reading. [[retrieval-structure|Retrieval structure]] refers to the organisation of knowledge in a form accessible to retrieval cues — knowledge with richer retrieval structure is more flexibly accessible across varied contexts.

The practical triad of evidence-based study strategy is therefore: **space** learning sessions, **retrieve** actively rather than restudy, and **interleave** different materials.

[Synthesis-With:: [[MOC - Learning Science]]]

---

## Forgetting: Adaptive and Pathological

Forgetting is not the enemy of learning — it is its necessary context. [[forgetting-curve|Ebbinghaus' forgetting curve]] revealed the exponential decay of memory without rehearsal, but this decay is functional: it is what makes subsequent retrieval effortful, and that effort is what drives consolidation.

### Theories of Forgetting

[[interference-theory|Interference theory]] holds that forgetting is primarily caused by competition between memories, not by passive decay. [[proactive-interference|Proactive interference]] occurs when older memories interfere with new learning (why a new phone number is hard to remember when you've had many previous ones). [[retroactive-interference|Retroactive interference]] occurs when new learning disrupts existing memories.

[[trace-decay|Trace decay]] is the alternative hypothesis: memories fade over time through disuse alone. Contemporary evidence suggests both mechanisms operate, but interference is primary for most everyday forgetting.

### Source Monitoring Failures

[[source-monitoring|Source monitoring]] errors — attributing information to the wrong source — are a distinct category of memory failure with profound practical implications. [[source-amnesia|Source amnesia]] (remembering a fact but not where it was learned) is common and underlies many forms of [[false-memory|false memory]]. The phenomenon of [[imagination-inflation|imagination inflation]] — increased confidence in a false memory following repeated imaginative rehearsal — demonstrates that vividness is not a reliable indicator of accuracy.

> [!warning] Fluency ≠ Memory
> [[fluency-illusion|The fluency illusion]] — the metacognitive error of mistaking processing ease for memory strength — is one of the most damaging misconceptions students hold about learning. Re-reading feels effective because familiar material is processed fluently; but fluency is not encoding. Only effortful retrieval, not recognition, reliably predicts long-term retention. See [[MOC - Metacognition and Self-Regulated Learning]] for the full treatment of metacognitive monitoring.

---

## Metacognitive Monitoring of Memory

Memory science and metacognition intersect in the domain of *judgments about memory* — the internal monitoring signals that guide study decisions.

[[judgment-of-learning|Judgments of learning (JOLs)]] — predictions about how well an item will be remembered at a later test — are systematically miscalibrated in predictable ways. Immediate JOLs (made right after study) are far less accurate than [[ease-of-learning-judgment|ease of learning judgments]] (made before study) or delayed JOLs (made after a brief interval), because immediate JOLs are dominated by current processing fluency rather than memory strength.

[[feeling-of-knowing|Feeling of knowing (FOK)]] judgments — the sense that you will be able to recognise an answer you cannot currently recall — are diagnostically important: a strong FOK prompts continued search, while a weak FOK triggers abandonment. FOK is reasonably accurate for well-learned domains but unreliable for recently acquired knowledge.

[[calibration|Calibration]] — the correspondence between confidence and accuracy — is the normative standard for metacognitive monitoring. Overconfidence (high confidence with low accuracy) is the modal failure mode, particularly for novel material. [[cue-utilization-framework|The cue-utilization framework]] explains why: we rely on cues like fluency, familiarity, and effort that do not reliably correlate with actual memory strength.

This section connects to the [[MOC - Metacognition and Self-Regulated Learning]], where the full architecture of metacognitive control is developed.

---

## 🌉 Cross-Domain Bridges

> [!related] Companion MOCs
> - [[MOC - Cognitive Load Theory]] — Working memory capacity limits are the engine of CLT; this MOC provides the cognitive substrate for understanding why load management matters.
> - [[MOC - Metacognition and Self-Regulated Learning]] — Metacognitive judgments (JOLs, FOK, calibration) are the interface between memory science and self-regulated study behaviour.
> - [[MOC - Learning Science]] — The testing effect, spacing, and interleaving are the most robust findings from memory science, translated into instructional practice.
> - [[MOC - Dual Process Theory and Cognitive Biases]] — [[fluency-illusion|Fluency illusion]] and [[source-monitoring|source monitoring failures]] connect to the dual-process account of cognitive error.

---

## 🌅 Frontier & Open Questions

> [!frontier] Live debates within Memory Science
> - **Reconsolidation therapy**: Can targeted reconsolidation disruption (pharmacological or behavioural) selectively weaken traumatic memories without impairing adjacent memories? Early results are promising but human translation remains challenging.
> - **Memory specificity vs generalisation trade-off**: How does the hippocampus balance storing specific episodes vs. extracting statistical regularities? The relationship between [[pattern-recognition|pattern recognition]] and episodic specificity is not fully theorised.
> - **The role of schema in false memory**: When does prior knowledge protect memory vs. distort it? The conditions under which schemas facilitate vs. corrupt encoding are incompletely specified.

> [!frontier] Gaps in this MOC's coverage
> - **Prospective memory** ([[prospective-memory|prospective memory]] — remembering to do things in the future) is underrepresented relative to its real-world significance.
> - **Transactive memory systems** ([[transactive-memory-systems|group-level memory coordination]]) and their relationship to PKB design deserve fuller treatment.

---

## 📚 Index of Linked Notes

| Note | Type | Section |
|------|------|---------|
| [[acetylcholine-and-memory]] | atomic | Consolidation |
| [[active-recall]] | atomic | Retrieval |
| [[autobiographical-memory]] | atomic | Architecture |
| [[baddeley-and-hitch-working-memory-model]] | reference | Working Memory |
| [[blocked-practice]] | atomic | Retrieval |
| [[calibration]] | atomic | Metacognitive Monitoring |
| [[central-executive]] | atomic | Working Memory |
| [[chunk]] | atomic | Working Memory |
| [[chunking]] | atomic | Working Memory |
| [[cognitive-disequilibrium]] | atomic | Architecture |
| [[conceptual-change]] | atomic | Architecture |
| [[context-dependent-memory]] | atomic | Encoding |
| [[cortisol-and-memory]] | atomic | Consolidation |
| [[cue-utilization-framework]] | atomic | Metacognitive Monitoring |
| [[declarative-memory]] | atomic | Architecture |
| [[deep-processing]] | atomic | Encoding |
| [[elaboration]] | atomic | Encoding |
| [[elaborative-encoding]] | atomic | Encoding |
| [[elaborative-interrogation]] | atomic | Encoding |
| [[encoding-depth]] | atomic | Encoding |
| [[encoding-specificity-principle]] | atomic | Encoding |
| [[encoding-variability]] | atomic | Encoding |
| [[episodic-buffer]] | atomic | Working Memory |
| [[episodic-memory]] | atomic | Architecture |
| [[false-memory]] | atomic | Forgetting |
| [[feeling-of-knowing]] | atomic | Metacognitive Monitoring |
| [[flashbulb-memory]] | atomic | Consolidation |
| [[fluency-illusion]] | atomic | Metacognitive Monitoring |
| [[forgetting-curve]] | atomic | Forgetting |
| [[generation-effect]] | atomic | Retrieval |
| [[hippocampal-neocortical-transfer]] | atomic | Consolidation |
| [[hypercorrection-effect]] | atomic | Retrieval |
| [[imagination-inflation]] | atomic | Forgetting |
| [[interleaving-effect]] | atomic | Retrieval |
| [[judgment-of-learning]] | atomic | Metacognitive Monitoring |
| [[levels-of-processing]] | reference | Encoding |
| [[leitner-system]] | atomic | Retrieval |
| [[long-term-memory]] | atomic | Architecture |
| [[long-term-potentiation]] | atomic | Consolidation |
| [[magical-number-seven]] | atomic | Working Memory |
| [[memory-consolidation]] | reference | Consolidation |
| [[memory-systems]] | reference | Architecture |
| [[multi-store-model]] | atomic | Architecture |
| [[non-declarative-memory]] | atomic | Architecture |
| [[norepinephrine-and-learning]] | atomic | Consolidation |
| [[phonological-loop]] | atomic | Working Memory |
| [[prior-knowledge]] | atomic | Encoding |
| [[proactive-interference]] | atomic | Forgetting |
| [[procedural-memory]] | atomic | Architecture |
| [[reconsolidation]] | atomic | Consolidation |
| [[recognition-memory]] | atomic | Retrieval |
| [[retrieval-practice]] | reference | Retrieval |
| [[retrieval-practice-as-the-most-potent-single-strategy]] | synthesis | Retrieval |
| [[retrieval-structure]] | atomic | Retrieval |
| [[retroactive-interference]] | atomic | Forgetting |
| [[schema]] | atomic | Architecture |
| [[semantic-memory]] | atomic | Architecture |
| [[sleep-and-memory-consolidation]] | reference | Consolidation |
| [[sleep-stages-and-memory]] | atomic | Consolidation |
| [[source-amnesia]] | atomic | Forgetting |
| [[source-monitoring]] | atomic | Forgetting |
| [[source-information-is-cognitively-constructed-not-mechanically-recorded]] | synthesis | Central Claim |
| [[spaced-repetition]] | reference | Retrieval |
| [[spaced-retrieval]] | atomic | Retrieval |
| [[spacing-effect]] | atomic | Retrieval |
| [[state-dependent-memory]] | atomic | Encoding |
| [[synaptic-plasticity]] | atomic | Consolidation |
| [[testing-effect]] | reference | Retrieval |
| [[trace-decay]] | atomic | Forgetting |
| [[visuospatial-sketchpad]] | atomic | Working Memory |
| [[working-memory]] | reference | Working Memory |
| [[working-memory-capacity]] | atomic | Working Memory |
| [[working-memory-in-the-clt-framework]] | synthesis | Working Memory |
| [[working-memory-updating]] | atomic | Working Memory |

---

> [!info] MOC Metadata
> - **Pattern**: hub-and-spoke
> - **Source notes**: 62
> - **Word count**: ~5,800
> - **Generated**: 2026-05-15 by MOC Specialist Agent v1.0.0
> - **Audit trail**: [[_meta/MOC - Memory Science.audit]]
> - **Next review suggested**: 2026-08-15


# Visual Aid Suite: Memory Science — Map of Content

**Report length:** ~5,800 words · 62 source notes
**Audience:** Practitioner / Researcher (as specified in MOC frontmatter)
**Thesis:** Memory is an active reconstructive system, not a passive archive — encoding is transformation, consolidation is biological stabilisation, and retrieval is the most powerful act of building memory.
**Aids selected:**

1. **Causal Architecture** — what drives durable memory from attention to LTM
2. **Memory Systems Taxonomy** — full hierarchical classification
3. **Baddeley WM Model (Enriched)** — 4-component architecture + limits
4. **Intellectual Genealogy Timeline** — who built on whom across 140 years
5. **Encoding Strategies Comparison Matrix** — evidence-ranked side-by-side
6. **Consolidation Process Flow** — trace → LTM via sleep & neurochemistry
7. **Retrieval Superiority Evidence Ledger** — testing-effect claim map
8. **Forgetting Theories & Source Failures** — interference vs. decay + monitoring errors
9. **Metacognitive Monitoring Accuracy Spectrum** — JOL / FOK / fluency illusion
10. **Before / After Contrast Panel** — naive vs. evidence-based study practice
11. **TL;DR Scorecard** — final synthesis

---

## Visual Aid 1: Causal Architecture of Durable Memory

**Purpose:** Shows the full causal pipeline from initial attention through encoding, consolidation, and retrieval to durable long-term retention — making visible the mechanisms the MOC argues are "not passive."

```
╔══════════════════════════════════════════════════════════════╗
║         WHAT PRODUCES DURABLE LONG-TERM MEMORY?             ║
╚══════════════════════════════════════════════════════════════╝

ATTENTION ─────────┐
                   │
PRIOR KNOWLEDGE ───┼───────────────────────────────────┐
  (schemas)        │                                   │
                   ▼                                   │
          ┌─────────────────────────┐                  │
          │        ENCODING         │◄─────────────────┘
          │  (constructive, not     │
          │   verbatim)             │
          │                         │
          │  shallow (phonological) │→ weak trace
          │  structural             │→ moderate trace
          │  deep / semantic   ─────│→ strong trace ✓
          │  + elaboration     ─────│→ durable trace ✓✓
          └────────────┬────────────┘
                       │
                       ▼
              ┌─────────────────────┐
              │   LABILE TRACE      │
              │  (fragile; ~hours)  │
              └──────────┬──────────┘
                         │
         ┌───────────────┼───────────────────┐
         ▼               ▼                   ▼
  ┌────────────┐  ┌─────────────────┐  ┌──────────────┐
  │  SYNAPTIC  │  │     SLEEP       │  │NEUROCHEMICAL │
  │  CONSOL.   │  │  (NREM → decl.  │  │MODULATION    │
  │  (LTP,     │  │   REM → proc.)  │  │(dopamine,    │
  │  protein   │  │                 │  │ cortisol,    │
  │  synthesis)│  └────────┬────────┘  │ NE, ACh)     │
  └────┬───────┘           │           └──────┬───────┘
       └───────────────────┼───────────────────┘
                           │
                           ▼
              ┌────────────────────────────────┐
              │  HIPPOCAMPAL–NEOCORTICAL        │
              │  TRANSFER (weeks – months)      │
              │  hippocampus indexes → cortex   │
              │  distributes and stabilises     │
              └──────────────┬─────────────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │   STABLE LTM TRACE  │
                  └──────────┬──────────┘
                             │
              ┌──────────────┴──────────────────┐
              ▼                                 ▼
   ┌─────────────────────┐         ┌────────────────────────┐
   │  RETRIEVAL PRACTICE │         │   RECONSOLIDATION       │
   │  (retrieval builds  │         │   (each retrieval →     │
   │  memory, not just   │         │    labile again →       │
   │  tests it)     ✓✓✓ │         │    re-stabilised with   │
   └─────────────────────┘         │    possible updates)    │
                                   └────────────────────────┘
                             │
                             ▼
              ╔══════════════════════════╗
              ║  DURABLE RETENTION  ✓✓✓ ║
              ╚══════════════════════════╝
```

**Reading guide:** Follow arrows top-to-bottom. The left branch (synaptic consolidation) and the centre branch (sleep) converge into the hippocampal-neocortical transfer node — this is why sleep is not optional. Neurochemical modulation (right) acts as a gating signal on what gets prioritised for consolidation. The bottom fork distinguishes retrieval practice (which strengthens the stable trace) from reconsolidation (which temporarily destabilises and rewrites it). Note that encoding quality determines what enters the pipeline; a shallow trace never becomes durable regardless of sleep.

**Source:** §The Central Claim, §Encoding, §Consolidation, §Retrieval

---

## Visual Aid 2: Memory Systems Taxonomy Tree

**Purpose:** Provides the full hierarchical classification of memory systems referenced across the MOC, showing duration, content-type, and conscious-access axes simultaneously.

```
MEMORY SYSTEMS
│
├── SENSORY MEMORY  (< 1 sec; pre-attentive)
│   ├── Iconic   → visual register
│   └── Echoic  → auditory register
│
├── WORKING MEMORY  (seconds; ~3–4 active chunks)
│   ├── Central Executive  (attentional control / planning)
│   ├── Phonological Loop  (verbal / acoustic; inner voice)
│   ├── Visuospatial Sketchpad  (spatial / visual imagery)
│   └── Episodic Buffer  (LTM interface; integrative binding)
│
└── LONG-TERM MEMORY  (potentially permanent)
    │
    ├── DECLARATIVE / EXPLICIT  ← conscious recollection
    │   │
    │   ├── Episodic Memory
    │   │   ├── Autobiographical Memory  (self + time + place)
    │   │   └── Flashbulb Memory  (high-arousal events)
    │   │
    │   └── Semantic Memory  (decontextualised world knowledge)
    │       └── Schemas  (organised knowledge networks)
    │           └── Scripts, Frames, Prototypes
    │
    └── NON-DECLARATIVE / IMPLICIT  ← no conscious access
        │
        ├── Procedural Memory  (skills, habits, motor sequences)
        ├── Priming  (prior exposure → faster processing)
        ├── Conditioning  (classical & operant associations)
        └── Non-associative Learning  (habituation / sensitisation)

KEY DIMENSIONS:
  Duration:         Sensory < WM <<< LTM
  Conscious access: Declarative ✓    Non-Declarative ✗
  Capacity limit:   WM: 3–4 chunks   LTM: effectively unlimited
```

**Reading guide:** Read the tree left-to-right as specificity increases. The bold horizontal line separates WM (the bottleneck — everything consciously processed must pass through it) from LTM (the durable store). The declarative / non-declarative split is the most consequential for instruction: only declarative memory is accessible to deliberate rehearsal strategies. Schemas sit within semantic memory and are the structural mechanism by which LTM facilitates new encoding (see Aid 1, "prior knowledge" node).

**Source:** §Memory Architecture, §Working Memory

---

## Visual Aid 3: Baddeley's Working Memory Model — Enriched

**Purpose:** Maps all four components of Baddeley's multicomponent model with their functional roles, limitations, and connections to the broader memory system.

```
╔══════════════════════════════════════════════════════════════╗
║            BADDELEY'S WORKING MEMORY MODEL (1974/2000)       ║
╚══════════════════════════════════════════════════════════════╝

                ┌──────────────────────────────────┐
                │       CENTRAL EXECUTIVE           │
                │  • Attentional control             │
                │  • Coordinates slave systems       │
                │  • Task switching & inhibition     │
                │  • Divided attention management    │
                │  Capacity: most limited of all     │
                └───────────┬────────────┬───────────┘
                            │            │
             ┌──────────────┘            └──────────────┐
             ▼                                          ▼
  ┌────────────────────────┐            ┌───────────────────────┐
  │    PHONOLOGICAL LOOP   │            │  VISUOSPATIAL         │
  │  • Phonological store  │            │  SKETCHPAD            │
  │    (speech-based;      │            │  • Visual cache       │
  │     ~1.5–2 sec decay)  │            │    (visual features)  │
  │  • Articulatory        │            │  • Inner scribe       │
  │    rehearsal process   │            │    (spatial movement) │
  │  • Verbal & acoustic   │            │  • Spatial reasoning  │
  │    material            │            │  • Mental rotation    │
  └──────────┬─────────────┘            └──────────┬────────────┘
             │                                      │
             └──────────────┬───────────────────────┘
                            ▼
                ┌──────────────────────────────────┐
                │        EPISODIC BUFFER             │
                │  • Added in 2000 revision          │
                │  • Temporary integrative store     │
                │  • Binds info from PL + VSS + LTM  │
                │  • Interface to long-term memory   │
                │  • Supports narrative coherence    │
                └──────────────────────────────────-┘
                            │
                            ▼
                ┌──────────────────────────────────┐
                │       LONG-TERM MEMORY            │
                │  (Episodic + Semantic + Procedural)│
                └──────────────────────────────────-┘

CAPACITY SUMMARY:
┌─────────────────────────────────────────────────────────┐
│  Miller (1956): 7 ± 2 "chunks"                          │
│  Cowan (2001):  ~4 chunks  ← current consensus          │
│  Chunking expands effective capacity via LTM schemas    │
│  Expert > Novice capacity (same WM, richer schemas)     │
└─────────────────────────────────────────────────────────┘

WHY IT MATTERS FOR LEARNING:
  Everything consciously processed MUST pass through WM.
  Overload WM → encoding failure before LTM is even reached.
  → Direct substrate of [[Cognitive-Load-Theory]]
```

**Reading guide:** The central executive sits atop two slave systems — read left (verbal) and right (spatial) branches as parallel processing channels. They feed down into the episodic buffer (added in the 2000 revision), which acts as the integration zone and gateway to LTM. The capacity summary at the bottom anchors the practical significance: at 3–4 active chunks, WM is the tightest bottleneck in all of cognition. Chunking via [[Schema]] knowledge is the primary mechanism for expanding effective capacity.

**Source:** §Working Memory: The Cognitive Bottleneck

---

## Visual Aid 4: Intellectual Genealogy — 140 Years of Memory Science

**Purpose:** Maps the major theorists, their founding contributions, and the lines of intellectual inheritance that produced contemporary memory science.

```
1885        1932      1960s       1972      1973      1974/2000
  │           │         │           │         │           │
  │           │         │           │         │           │
EBBINGHAUS  BARTLETT  ATKINSON  CRAIK &   TULVING &  BADDELEY
Forgetting  Reconstruct &        LOCKHART  THOMSON    & HITCH
Curve       Memory    SHIFFRIN   Levels of Encoding  Working
Savings     Schema    Multi-    Processing Specificity Memory
in          Theory    Store                           Model
Relearning             Model
  │           │          │           │         │
  │           │          │           │         │
  ▼           ▼          │           ▼         ▼
Spacing    Bartlett's    │     Elaborative  Context-
Effect     "War of the   │     Interrogation Dependent
Research   Ghosts"       │     Research     Memory
(Jost 1897 Expt.        │     (Pressley)   Research
 onward)                │                    │
                         ▼                    │
                    Superseded by             │
                    Working Memory  ──────────┘
                    (Baddeley 1974)
  │           │                  │
  │           │                  ▼
  │           ▼           TULVING (1972–85)
  │      RUMELHART      Episodic vs. Semantic
  │      Schema         Memory distinction
  │      Theory (1980)  Encoding Specificity ─────┐
  │           │                                   │
  │           ▼                                   ▼
  │      Schema ──────────────────────►  Context/State-
  │      Activation                      Dependent Memory
  │      Research
  │
  ▼
TESTING EFFECT LINEAGE:
  Ebbinghaus → Spitzer (1939) → Roediger & Karpicke
  (2006): Retrieval practice > restudy confirmed
                │
                ▼
  Dunlosky et al. (2013): 10 strategies ranked
  → Retrieval practice: HIGH utility ✓✓
  → Elaborative interrogation: MODERATE ✓
  → Re-reading: LOW ✗

2000s–PRESENT:
  NADER → Reconsolidation (2000)
  WALKER → Sleep & memory consolidation
  Current: Open questions on reconsolidation therapy
```

**Reading guide:** Read left-to-right along the top row as a chronological backbone; vertical arrows show influence. Ebbinghaus (left) spawned the quantitative tradition (spacing, forgetting curve, testing effect). Bartlett (centre-left) spawned the schema/reconstructive tradition. The Baddeley column (far right) superseded Atkinson-Shiffrin as the working memory model of record. The testing-effect lineage at the bottom runs from Ebbinghaus through to Dunlosky's 2013 meta-analytic rankings — the single most practically impactful thread in the MOC.

**Source:** §Memory Architecture, §Encoding, §Retrieval, §Frontier

---

## Visual Aid 5: Encoding Strategies Comparison Matrix

**Purpose:** Evaluates seven encoding strategies across five dimensions so practitioners can select evidence-aligned approaches.

```
┌──────────────────────┬───────────┬──────────┬──────────┬──────────┬───────────┐
│  STRATEGY            │ Evidence  │ Effort   │ Transfer │ Metacog. │ Best Use  │
│                      │ Strength  │ Required │ to Novel │ Benefit  │ Case      │
├──────────────────────┼───────────┼──────────┼──────────┼──────────┼───────────┤
│ Re-reading           │  ★☆☆☆☆   │  Low     │  Low     │  Harms   │ Never as  │
│  (fluency illusion)  │  WEAK     │          │          │(fluency  │ primary   │
│                      │           │          │          │ illusion)│ strategy  │
├──────────────────────┼───────────┼──────────┼──────────┼──────────┼───────────┤
│ Highlighting /       │  ★☆☆☆☆   │  Low     │  Low     │  Harms   │ Only for  │
│  Underlining         │  WEAK     │          │          │          │ landmarks │
├──────────────────────┼───────────┼──────────┼──────────┼──────────┼───────────┤
│ Elaborative          │  ★★★☆☆   │  Moderate│  Moderate│ Moderate │ Individual│
│  Interrogation       │  MODERATE │          │          │ benefit  │ study     │
│  ("why is this true")│           │          │          │          │           │
├──────────────────────┼───────────┼──────────┼──────────┼──────────┼───────────┤
│ Self-Explanation     │  ★★★☆☆   │  Moderate│  High    │  High    │ Complex   │
│                      │  MODERATE │          │          │          │ concepts  │
├──────────────────────┼───────────┼──────────┼──────────┼──────────┼───────────┤
│ Interleaving         │  ★★★★☆   │  High    │  High    │  High    │ Problem-  │
│                      │  HIGH     │  (feels  │          │          │ type      │
│                      │           │  harder) │          │          │ discrim.  │
├──────────────────────┼───────────┼──────────┼──────────┼──────────┼───────────┤
│ Spaced Practice      │  ★★★★★   │  Moderate│  High    │ Moderate │ All long- │
│  (spacing effect)    │  HIGH     │          │          │          │ term ret. │
├──────────────────────┼───────────┼──────────┼──────────┼──────────┼───────────┤
│ Retrieval Practice   │  ★★★★★   │  High    │  Highest │  Highest │ All       │
│  (testing effect)    │  HIGHEST  │          │          │          │ material  │
│                      │           │          │          │          │ types     │
└──────────────────────┴───────────┴──────────┴──────────┴──────────┴───────────┘

Evidence key:  ★★★★★ = multiple meta-analyses, robust across populations
               ★★★☆☆ = consistent but more context-dependent
               ★☆☆☆☆ = weak, contradicted by evidence
```

**Reading guide:** Sort by the "Evidence Strength" column for a priority ranking. Note the inverse relationship between the strategies that *feel* effective (re-reading, highlighting — low effort, high familiarity, high fluency illusion) and those that *are* effective (retrieval practice — high effort, low fluency). The "Metacog. Benefit" column flags strategies that also improve metacognitive accuracy: retrieval practice improves both memory and the calibration of memory judgments. The MOC's central warning — fluency ≠ memory — is structurally visible here.

**Source:** §Encoding, §Retrieval, §Forgetting (fluency illusion warning)

---

## Visual Aid 6: Consolidation Process Flow

**Purpose:** Traces the biological pathway from an unstable encoding to a cortically distributed, stable LTM trace, making the role of sleep and neurochemistry mechanistically visible.

```
  LEARNING EVENT
       │
       ▼
  ┌───────────────────────────────────────────────────────┐
  │  INITIAL ENCODING                                     │
  │  Hippocampus binds dispersed cortical representations │
  │  Glutamate → NMDA receptor activation → LTP begins    │
  └──────────────────────┬────────────────────────────────┘
                         │
                         ▼
  ┌───────────────────────────────────────────────────────┐
  │  LABILE TRACE  (hours post-encoding)                  │
  │  ⚠ Vulnerable to:  electroconvulsive shock            │
  │                    protein synthesis inhibitors        │
  │                    new interfering learning            │
  │                    acute stress (high cortisol)        │
  └──────────────────────┬────────────────────────────────┘
                         │
           ┌─────────────┴──────────────┐
           ▼                            ▼
  ┌─────────────────────┐    ┌──────────────────────────┐
  │ NEUROCHEMICAL GATES │    │        SLEEP              │
  │                     │    │                           │
  │ Dopamine (reward/   │    │ NREM / slow-wave:         │
  │  novelty signal)    │    │  → declarative memory     │
  │                     │    │  → hippocampal replay     │
  │ Norepinephrine      │    │  → neocortical transfer   │
  │  (emotional arousal │    │                           │
  │  → flashbulb effect)│    │ REM sleep:                │
  │                     │    │  → procedural memory      │
  │ Acetylcholine       │    │  → emotional memory       │
  │  (attentional gate  │    │  → creative integration   │
  │  → what gets in)    │    │                           │
  │                     │    │ ⚠ Deprivation = permanent │
  │ Cortisol            │    │   impairment possible     │
  │  • Moderate → ✓     │    └────────────┬──────────────┘
  │  • Chronic  → ✗     │                 │
  └─────────────────────┘                 │
           │                              │
           └──────────────┬───────────────┘
                          ▼
  ┌───────────────────────────────────────────────────────┐
  │  HIPPOCAMPAL–NEOCORTICAL TRANSFER  (weeks – months)   │
  │  Hippocampus gradually releases memory to cortex      │
  │  Cortical representations become self-supporting      │
  │  Memory: less contextual → more semantic/schematic    │
  └──────────────────────┬────────────────────────────────┘
                         │
                         ▼
  ┌───────────────────────────────────────────────────────┐
  │  STABLE CORTICAL TRACE                                │
  │  ✓ Resistant to disruption                           │
  │  ✓ Integrated into schema networks                   │
  │  ✓ Accessible via multiple retrieval pathways        │
  │                                                       │
  │  BUT: Each retrieval → RECONSOLIDATION window        │
  │  Memory becomes labile again → new information       │
  │  can modify it → therapeutic and distortion risk     │
  └───────────────────────────────────────────────────────┘
```

**Reading guide:** The left branch (neurochemical gates) acts as a filtering and amplification system — dopamine flags what is surprising and worth consolidating; norepinephrine amplifies arousing events; chronic cortisol acts as a suppressor. The right branch (sleep) is the primary consolidation mechanism; the two branches converge at hippocampal-neocortical transfer. The red-flag at the bottom (reconsolidation) is a recent discovery (Nader 2000) that breaks the naive assumption of memory stability — retrieved memories are writable, not read-only.

**Source:** §Consolidation: What Sticks

---

## Visual Aid 7: Retrieval Practice — Evidence Ledger

**Purpose:** Maps the primary claims in the MOC's retrieval section to their evidence types and strength, allowing researchers and practitioners to calibrate confidence.

```
┌──────────────────────────────────┬───────────────┬──────────┬────────┐
│ CLAIM                            │ EVIDENCE TYPE │ STRENGTH │ §      │
├──────────────────────────────────┼───────────────┼──────────┼────────┤
│ Retrieval practice > restudy     │ RCTs,         │ ★★★★★  │ §Retr. │
│ for long-term retention          │ meta-analyses │  HIGHEST │        │
├──────────────────────────────────┼───────────────┼──────────┼────────┤
│ Active recall > recognition      │ Experimental  │ ★★★★☆  │ §Retr. │
│ due to retrieval effort          │ (Roediger et  │  HIGH    │        │
│                                  │  al. 2006+)   │          │        │
├──────────────────────────────────┼───────────────┼──────────┼────────┤
│ Spaced > massed practice         │ Meta-analytic │ ★★★★★  │ §Retr. │
│ with equal study time            │ consensus     │  HIGHEST │        │
├──────────────────────────────────┼───────────────┼──────────┼────────┤
│ Interleaving > blocked practice  │ Experimental; │ ★★★★☆  │ §Retr. │
│ for long-term transfer           │ some limits   │  HIGH    │        │
│                                  │ on near-term  │          │        │
├──────────────────────────────────┼───────────────┼──────────┼────────┤
│ Generation effect: generating >  │ Experimental  │ ★★★★☆  │ §Retr. │
│ reading even with errors         │ (well         │  HIGH    │        │
│  (hypercorrection)               │  replicated)  │          │        │
├──────────────────────────────────┼───────────────┼──────────┼────────┤
│ Retrieval also MODIFIES memory   │ Experimental  │ ★★★★☆  │ §Con-  │
│ (reconsolidation window)         │ (animal +     │  HIGH    │ solid. │
│                                  │ human data)   │          │        │
├──────────────────────────────────┼───────────────┼──────────┼────────┤
│ Encoding variability > single-   │ Correlational │ ★★★☆☆  │ §Enc.  │
│ context study for transfer       │ + experimental│ MODERATE │        │
├──────────────────────────────────┼───────────────┼──────────┼────────┤
│ Elaborative interrogation        │ Experimental; │ ★★★☆☆  │ §Enc.  │
│ improves retention               │ domain-       │ MODERATE │        │
│                                  │ dependent     │          │        │
└──────────────────────────────────┴───────────────┴──────────┴────────┘

VERDICT SUMMARY:
  ★★★★★ retrieval practice + spacing = the evidence-based core
  ★★★★☆ interleaving + generation effect = strong supplements
  ★★★☆☆ elaborative interrogation = valuable but context-dependent
```

**Reading guide:** Sort by "Strength" to get a practical priority ranking. The top two rows together constitute the testing effect — a claim with some of the most robust replication in cognitive psychology. Note the reconsolidation claim (row 6): this is a finding that complicates the simple "retrieval = test" model, because retrieval also *modifies* what it retrieves. The lower-strength findings are not weak; ★★★☆☆ reflects genuine experimental support with more conditions on applicability.

**Source:** §Retrieval: The Practice That Builds Memory, §Encoding

---

## Visual Aid 8: Forgetting — Theories and Source Monitoring Failures

**Purpose:** Displays the competing theoretical accounts of forgetting alongside the source-monitoring failure cluster, showing how "errors" are natural outputs of a reconstructive system.

```
╔══════════════════════════════════════════════════════════════╗
║     THEORIES OF FORGETTING: SPECTRUM & EVIDENCE             ║
╚══════════════════════════════════════════════════════════════╝

  TRACE DECAY                              INTERFERENCE
  (time alone causes                       (competition between
  forgetting)                              memories causes forgetting)
      │                                         │
      │ ← ─ ─ ─ EVIDENCE WEIGHT ─ ─ ─ ─ ─ ─ → │
      │                                         │
  ★★☆☆☆  WEAKER                          ★★★★☆  STRONGER
  (hard to isolate                       (proactive + retroactive
  from interference)                     interference well-evidenced)
  │                                           │
  ▼                                           ▼
Explains:                               Explains:
• Very long time spans                  • New learning harming old
• Passive disuse                        • Old learning blocking new
                                        • Why similar material
                                          is harder to separate

INTERFERENCE TYPES:
┌──────────────────────────────────────────────────────────┐
│  PROACTIVE INTERFERENCE                                  │
│  Old memory ──────────────────────► Disrupts new memory  │
│  (your old phone number interferes with your new one)    │
├──────────────────────────────────────────────────────────┤
│  RETROACTIVE INTERFERENCE                                │
│  New memory ──────────────────────► Disrupts old memory  │
│  (learning Spanish impairs previously learned Italian)   │
└──────────────────────────────────────────────────────────┘

╔══════════════════════════════════════════════════════════════╗
║     SOURCE MONITORING FAILURES (natural by-products         ║
║     of a reconstructive system)                             ║
╚══════════════════════════════════════════════════════════════╝

  SOURCE MONITORING ─ the process of identifying WHERE / FROM
  WHOM information originated

  FAILURE TYPE          MECHANISM              CONSEQUENCE
  ──────────────────────────────────────────────────────────
  Source Amnesia        Remember WHAT,         Cryptomnesia;
                        not WHERE learned      plagiarism risk

  Imagination Inflation  Repeated imagining     False confidence
                         → increased           in false events
                         confidence in
                         false memory

  False Memory          Schema completion       Gist remembered,
                        fills gaps with         details distorted
                        plausible content       or invented

  Misinformation Effect Post-event info         Eyewitness
  (Loftus)              corrupts original       testimony errors
                        memory trace

ADAPTIVE LOGIC:
  Memory prioritises WHAT (gist, relevance, prediction) over
  WHERE/WHEN (source attribution). This is efficient but
  produces systematic, predictable distortions.
  → False memory = not a bug, but a feature of
    a pattern-completion system.
```

**Reading guide:** The top half presents the theoretical debate: decay vs. interference. The weight of contemporary evidence favours interference as the primary mechanism for everyday forgetting, though decay operates over very long intervals. The bottom half clusters the source-monitoring failure family — each failure type shares the same root cause: the system stores *content* more reliably than *provenance*. Imagination inflation is especially important for metacognitive monitoring: the vividness of a mental image does not track its accuracy.

**Source:** §Forgetting: Adaptive and Pathological

---

## Visual Aid 9: Metacognitive Monitoring of Memory — Accuracy Spectrum

**Purpose:** Positions JOLs, FOK judgments, and calibration on an accuracy spectrum, showing when each monitoring signal is reliable and when it fails.

```
╔══════════════════════════════════════════════════════════════╗
║     METACOGNITIVE MONITORING ACCURACY SPECTRUM               ║
╚══════════════════════════════════════════════════════════════╝

  MONITORING SIGNAL                ACCURACY        FAILURE MODE
  ─────────────────────────────────────────────────────────────

  Ease-of-Learning (EOL)          ★★★★☆           Over-
  Judgment (before study)         MODERATE-HIGH    confidence
  Predicts difficulty             Timing:          for novel /
  before encoding                 pre-study        unfamiliar
                                  → most accurate  domains
  ─────────────────────────────────────────────────────────────

  Delayed JOL                     ★★★★☆           Less accurate
  (JOL after brief interval)      MODERATE-HIGH    for
  Predicts memory after gap       "delayed JOL     overlearned
                                  effect" well     items
                                  replicated
  ─────────────────────────────────────────────────────────────

  Feeling of Knowing (FOK)        ★★★☆☆           Poor accuracy
  "I know it but can't            MODERATE         for recently
  recall it now"                  Better for       acquired
  Guides continued search         familiar         knowledge
  or abandonment                  domains
  ─────────────────────────────────────────────────────────────

  Immediate JOL                   ★★☆☆☆           FLUENCY
  (JOL right after study)         LOW              ILLUSION
  Predicts future memory          Dominated by     Familiarity ≠
  right after encoding            CURRENT          Memory
                                  FLUENCY,         strength
                                  not memory       Overconfidence
                                  durability       most extreme
  ─────────────────────────────────────────────────────────────

CALIBRATION:
  ┌────────────────────────────────────────────────────────┐
  │  OVERCONFIDENT                WELL-CALIBRATED          │
  │  High confidence +            High confidence +        │
  │  Low accuracy                 High accuracy            │
  │                                                        │
  │       ●  Immediate JOLs                                │
  │          (most learners)         ●  Delayed JOLs       │
  │                                  ●  EOL judgments      │
  │                                  (domain-familiar)     │
  └────────────────────────────────────────────────────────┘

KEY INTERVENTION:
  Replace immediate JOLs with RETRIEVAL ATTEMPTS.
  Retrieval outcome (✓ or ✗) is far more diagnostic
  of memory strength than fluency of re-reading.

CUE-UTILIZATION FRAMEWORK:
  Learners rely on cues that feel diagnostic but aren't:
  • Fluency of processing        → ✗ not memory strength
  • Familiarity of material      → ✗ not retrievability
  • Amount studied               → ✗ not durability
  • Effort during re-reading     → ✗ not depth of encoding
```

**Reading guide:** The left column orders monitoring signals from most accurate (top) to least accurate (bottom). Immediate JOLs sit at the bottom because they are hijacked by processing fluency rather than actual memory strength — this is the mechanism behind the fluency illusion. The calibration panel shows this asymmetry visually: most learners cluster in the overconfident quadrant. The intervention line at the bottom (replace JOLs with retrieval attempts) connects this section directly back to Aid 7 — the same act (retrieval practice) that builds memory also produces better metacognitive calibration.

**Source:** §Metacognitive Monitoring of Memory

---

## Visual Aid 10: Before / After — Naive vs. Evidence-Based Study Practice

**Purpose:** Contrasts the study behaviours that students typically adopt (driven by fluency and familiarity signals) against the evidence-based alternatives the MOC recommends.

```
┌─────────────── NAIVE STUDY PRACTICE ──────────────────────┐
│                                                            │
│  Session structure: One long massed session               │
│  Primary method:    Re-read notes / textbook              │
│  Highlighting:      Extensive; feels productive           │
│  Self-testing:      Absent; "I'll wait until exam"        │
│  Schedule:          All material the night before         │
│  Mixed vs. blocked: Blocked (finish topic A before B)     │
│  Sleep:             Reduced to fit more study time        │
│  Confidence check:  Based on fluency / familiarity        │
│  Schema use:        Passive (no deliberate activation)    │
│  Metacognitive      "If it feels familiar, I know it"     │
│  belief:                                                   │
│                                                            │
│  OUTCOME:  High short-term familiarity                    │
│            Low long-term retention                        │
│            Overconfident on test day                      │
│            Poor transfer to novel contexts                │
└────────────────────────────────────────────────────────────┘
                         │
                         │  APPLY MEMORY SCIENCE
                         │  (this MOC's programme)
                         ▼
┌─────────────── EVIDENCE-BASED STUDY PRACTICE ─────────────┐
│                                                            │
│  Session structure: Multiple spaced shorter sessions      │
│  Primary method:    Active recall (close notes, retrieve) │
│  Highlighting:      Minimal; only to mark for retrieval   │
│  Self-testing:      Constant; before, during, after       │
│  Schedule:          Distributed; spaced repetition system │
│  Mixed vs. blocked: Interleaved (mix problem types)       │
│  Sleep:             Protected; prioritised post-learning  │
│  Confidence check:  Based on actual retrieval outcome     │
│  Schema use:        Explicit activation before encoding   │
│  Metacognitive      "Fluency lies. Retrieval reveals."   │
│  belief:                                                   │
│                                                            │
│  OUTCOME:  Lower short-term familiarity (feels harder)   │
│            High long-term retention                       │
│            Calibrated confidence                          │
│            Strong transfer to novel contexts              │
└────────────────────────────────────────────────────────────┘

MECHANISM BEHIND EVERY CHANGE:
  Spacing     → spacing effect; consolidation window preserved
  Retrieval   → testing effect; trace rebuilt, not just read
  Interleave  → discriminative contrast; category encoding
  Sleep       → consolidation; hippocampal-neocortical transfer
  Schema act. → encoding efficiency; prior knowledge nodes
  Self-test   → accurate JOLs replace fluency-based JOLs
```

**Reading guide:** Read each row horizontally as a direct swap. The before column is not random — it reflects behaviours that are rewarded by the metacognitive signals that feel accurate (fluency, familiarity) but are poor proxies for memory durability. The after column is counter-intuitive: effective study feels *harder* and less productive in the moment, which is why the metacognition section (Aid 9) must be understood alongside this one. The mechanism row at the bottom keys each change to the specific theoretical mechanism the MOC documents.

**Source:** All sections — synthesised practical application

---

## Synthesis Packet

**Top 5 Takeaways:**

1. **Memory is a reconstruction, not a recording.** Every error, distortion, and false memory follows logically from this. The system was built for adaptive action, not archival accuracy — gist over detail, prediction over fidelity.

2. **The cognitive bottleneck is working memory, not long-term memory.** At 3–4 active chunks, WM is where most learning failures originate. Instructional design is WM management (→ [[Cognitive-Load-Theory]]).

3. **Encoding depth is the primary determinant of trace quality.** Shallow (phonological) processing produces forgettable traces; deep (semantic) processing with elaboration produces durable ones. Prior knowledge schemas are multipliers.

4. **Retrieval practice is the most powerful known memory intervention.** It does not merely test memory — it rebuilds it, recalibrates metacognition, and outperforms all other single strategies across populations and materials.

5. **The fluency illusion is the enemy of effective learning.** Students study using strategies that maximise familiarity (re-reading, massed practice) because familiarity feels like knowing. Immediate JOLs are the worst possible guide to study planning; retrieval outcomes are the best.

---

**Navigator — which aid answers which question:**

| Question | Aid |
|---|---|
| "What is the full causal chain from attention to durable memory?" | Aid 1 |
| "What are all the memory systems and how do they relate?" | Aid 2 |
| "How does working memory work and why is it a bottleneck?" | Aid 3 |
| "Who built what, and who influenced whom?" | Aid 4 |
| "Which study strategies are actually worth my time?" | Aid 5 |
| "What happens biologically during consolidation?" | Aid 6 |
| "How strong is the evidence for retrieval practice?" | Aid 7 |
| "Why do we forget, and why do false memories form?" | Aid 8 |
| "When should I trust my feeling of knowing?" | Aid 9 |
| "What should I actually do differently when studying?" | Aid 10 |

---

**Final Scorecard:**

```
╔══════════════════════════════════════════════════════════════╗
║              MEMORY SCIENCE MOC — SCORECARD                  ║
╠══════════════════════════════════════════════════════════════╣
║  Core thesis  : Memory is reconstructive; retrieval is its   ║
║                most powerful architect, not mere test.       ║
║  Strongest evd: Testing effect (★★★★★, meta-analytic         ║
║                consensus; spacing effect equally robust)     ║
║  Weakest link : Reconsolidation therapy translation to       ║
║                humans; frontier, not established practice    ║
║  Key action   : Replace re-reading with spaced retrieval     ║
║                practice; protect sleep post-learning         ║
║  Key warning  : Fluency illusion — feeling of knowing ≠      ║
║                knowing; immediate JOLs are systematically    ║
║                deceptive                                     ║
║  Read if you  : Design instruction, study anything           ║
║                seriously, or research learning science       ║
║  Skip if you  : Need neuroanatomy depth or clinical memory   ║
║                pathology (this MOC is cognitive-functional)  ║
║  PKB connects : [[Cognitive-Load-Theory]]                    ║
║    to:          [[Metacognitive-Monitoring]]                  ║
║                 [[Spaced-Repetition]]                        ║
║                 [[Retrieval-Practice]]                       ║
║                 [[Schema-Theory]]                            ║
║                 [[Fluency-Illusion]]                         ║
╚══════════════════════════════════════════════════════════════╝
```