---
tags: [moc, domain-cognitive-science, domain-learning-science, status-budding]
aliases: [Cognitive Science MOC, Learning Science MOC, CLT MOC]
created: 2026-04-25
modified: 2026-04-25
status: budding
type: moc
moc_pattern: progressive
domain: Cognitive Architecture & Learning Science
source_notes_count: 182
target_word_count: 5000
audience: [practitioner, researcher]
maturity: established
parent_moc: null
related_mocs: ["[[moc-motivation-agency-self-regulation]]", "[[moc-reasoning-critical-thinking-epistemology]]"]
version: 1.0.0
---

# Cognitive Architecture & Learning Science — Map of Content

> [!abstract] Domain & Scope
> **Cognitive Architecture & Learning Science** is the empirical and theoretical study of how minds encode, store, retrieve, and transform knowledge — and what instructional conditions optimize that process. This MOC organizes ~182 permanent notes spanning memory systems, cognitive load theory, schema formation, expertise development, evidence-based learning strategies, and instructional design. It is structured as a **progressive architecture** — each section builds on the mechanisms established in the section before it, mirroring the novice-to-expert trajectory the domain describes.
>
> **For**: Practitioners designing learning environments; researchers building theoretical fluency; autodidacts optimizing their own PKB workflows.
> **Companion MOCs**: [[moc-motivation-agency-self-regulation]], [[moc-reasoning-critical-thinking-epistemology]]
> **Reading time**: ~25 min full read; sections are self-contained entry points.

## 🗺️ Navigation

- **[§1 — Cognitive Architecture: The System](#1-cognitive-architecture-the-system)** — memory systems, dual-process, information processing
- **[§2 — Cognitive Load Theory: The Bottleneck](#2-cognitive-load-theory-the-bottleneck)** — intrinsic, extraneous, germane load; element interactivity
- **[§3 — Schema Formation: How Knowledge Organizes Itself](#3-schema-formation-how-knowledge-organizes-itself)** — schemas, chunking, encoding depth
- **[§4 — The Expert-Novice Continuum](#4-the-expert-novice-continuum)** — expertise, deliberate practice, automaticity
- **[§5 — Evidence-Based Learning Strategies](#5-evidence-based-learning-strategies)** — retrieval, spacing, interleaving, elaboration
- **[§6 — Instructional Design: Engineering the Environment](#6-instructional-design-engineering-the-environment)** — 4C/ID, worked examples, scaffolding, transfer
- **[🌉 Cross-Domain Bridges](#cross-domain-bridges)**
- **[🌅 Frontier & Open Questions](#frontier-and-open-questions)**
- **[📚 Index of Linked Notes](#index-of-linked-notes)**

> [!progression] Reading Paths
> - **Conceptual overview**: Read §1, skim §3 and §5 headings, then read §4 conclusions.
> - **Practitioner (instructional design)**: Start at §5; backtrack into §2 and §3 only when you encounter an unfamiliar mechanism.
> - **PKB-builder**: §3 and the Cross-Domain Bridges section are your primary territory.

---

## §1 — Cognitive Architecture: The System

All learning is constrained by hardware before it is shaped by strategy. The field of [[cognitive-psychology]] converges on a systems-level account of the mind: information enters through sensory channels, passes into a severely capacity-limited working memory, and must be moved — through deliberate processing — into the much larger and more stable substrate of long-term memory. This architecture, outlined in [[information-processing-theory]] and formalized through the Atkinson–Shiffrin [[multi-store-model]], is not merely descriptive. It is *normatively prescriptive* for anyone designing learning conditions.

[[working-memory]] is the central bottleneck. Its capacity is classically estimated at 7±2 independent elements ([[magical-number-seven]]), though more rigorous contemporary work suggests the operational limit is closer to 3–4 chunks when chunking is controlled. [[working-memory-capacity]] varies substantially across individuals and is predictive of fluid reasoning and academic achievement. The internal architecture of working memory is itself modular: the [[central-executive]] coordinates processing; the [[phonological-loop]] handles verbal-acoustic material; the [[visuospatial-sketchpad]] handles spatial and imagistic content; and the [[episodic-buffer]] integrates information across modalities and with long-term memory. This modular structure is not academic detail — it is the mechanistic basis for the [[modality-effect]], [[dual-coding-theory]], and the design principle that audio narration over diagrams outperforms text-over-diagrams for complex procedural material.

> [!definition] Working Memory vs. Short-Term Memory
> [[short-term-memory]] and [[working-memory]] are often conflated but are theoretically distinct. STM is a passive storage buffer; WM is an *active processing workspace*. The distinction matters because the capacity limits that constrain learning are primarily *processing* limits, not passive storage limits. [[working-memory-in-the-clt-framework]] elaborates this distinction in the context of instructional load.

[[long-term-memory]] is where expertise lives. Unlike working memory, its functional capacity is effectively unlimited, and its contents — [[semantic-memory]] (facts and concepts), [[episodic-memory]] (autobiographical events), and [[procedural-memory]] (skills and procedures) — are organized into interconnected networks accessible through [[spreading-activation]]. The distinction between [[declarative-memory]] and [[non-declarative-memory]] tracks the rough divide between consciously accessible knowledge and proceduralized knowledge that operates below awareness. [[memory-consolidation]] — the post-encoding stabilization of memory traces, heavily dependent on sleep — is a mechanism frequently overlooked by learners who treat study as a one-session event.

The [[dual-process-theory]] of cognition (see also [[system-1]], [[system-2]], [[type-1-processing]], [[type-2-processing]]) introduces a second architectural dimension: not just *where* information is stored, but *how* processing is initiated. System 1 is fast, automatic, associative, and low-effort. System 2 is slow, deliberate, rule-governed, and effortful — and it operates directly through working memory. The [[default-interventionist-architecture]] describes how System 1 generates default responses that System 2 can override when sufficiently activated. This framework is the mechanistic bridge between cognitive architecture and both reasoning quality (see [[moc-reasoning-critical-thinking-epistemology]]) and motivation to engage in effortful processing (see [[moc-motivation-agency-self-regulation]]).

[Prerequisite-For:: [[cognitive-load-theory]], [[schema-theory]], [[dual-process-theory]]]
[Synthesis-With:: [[information-processing-theory]], [[cognitive-architecture]]]

---

## §2 — Cognitive Load Theory: The Bottleneck

If §1 establishes that working memory is limited, [[cognitive-load-theory]] (CLT) is the discipline that takes this limitation seriously as a design constraint. Developed by John Sweller from the late 1980s, CLT decomposes the load on working memory into three distinct types whose interactions determine whether learning occurs.

> [!definition] The Three Load Types
> - **[[intrinsic-cognitive-load]]**: Load determined by the inherent complexity of the material — specifically, by [[element-interactivity]], the number of elements that must be processed simultaneously to understand a concept. Intrinsic load cannot be eliminated without distorting the material, but it can be managed through sequencing.
> - **[[extraneous-cognitive-load]]**: Load generated by poor instructional design — redundant information, split-attention layouts, unnecessary complexity in presentation. This load is *parasitic*: it consumes capacity without contributing to learning. It must be minimized.
> - **[[germane-cognitive-load]]**: Load associated with schema formation and automation. This is the *productive* load that leads to long-term memory structures. CLT's prescriptive goal is to maximize germane load by reducing extraneous load, freeing capacity for schema construction.

The construct [[element-interactivity]] is the engine of intrinsic load (see [[why-element-interactivity-is-the-engine-of-intrinsic-load]]). When elements must be processed in relation to each other — rather than in isolation — interactivity is high and intrinsic load rises accordingly. [[relational-complexity]] extends this idea: tasks with many interacting variables demand that learners hold multiple conditional relationships in working memory simultaneously, quickly saturating capacity. [[the-standard-three-load-taxonomy]] provides the canonical framework, while [[sweller-s-2010-reconceptualization]] offers important corrections: Sweller later integrated evolutionary psychology into CLT, arguing that biologically primary knowledge ([[biologically-primary-knowledge]]) is acquired effortlessly because evolution prepared us for it, while [[biologically-secondary-knowledge]] (school-type learning) requires deliberate instructional scaffolding.

> [!key-claim] Extraneous Load Is an Instructional Design Failure Mode
> The [[split-attention-effect]] — the cost of requiring learners to mentally integrate physically separated but logically related materials — is among the most robust findings in CLT. It demonstrates that even slight presentation inefficiencies generate real capacity costs. Alongside the [[redundancy-effect]] (the cost of duplicating information across modalities when integration is unnecessary), these effects establish that instructional designers can *harm* learning through poor formatting choices, not merely fail to help.

CLT connects directly to expertise because intrinsic load is not fixed — it is expertise-dependent. Novices experience high intrinsic load for materials that experts process almost automatically, because experts have already built the schemas that allow complex relationships to be treated as single units. This is the mechanism behind the [[expertise-reversal-effect]]: instructional supports that help novices (by reducing element interactivity) can *impede* experts (who now carry the redundant cost of information they have already automated). [[the-expertise-reversal-effect]] provides the formal account; its design implication is that instructional complexity must scale with learner expertise rather than remaining fixed.

[Synthesis-With:: [[working-memory]], [[schema-theory]], [[instructional-design]]]
[Critique-Of:: [[cognitive-load-theory-and-pkb-design]] (applies CLT critique to PKB construction)]

---

## §3 — Schema Formation: How Knowledge Organizes Itself

The architecture of long-term memory is not a flat warehouse. It is a *structured network of schemas* — abstracted knowledge structures that organize information around common patterns, reducing the effective complexity of encountered material. [[schema-theory]] and its companion notes ([[schema]], [[schema-construction]], [[schema-automation]], [[declarative-schemas]], [[procedural-schemas]]) constitute one of the most important nodes in this entire vault because schemas are simultaneously the *product* of effective learning and the *precondition* for further learning.

[[schema-construction]] is the process by which related elements in working memory become bound into a single, retrievable unit in long-term memory. Once constructed, a schema can be activated as a single working-memory element regardless of its internal complexity — this is the mechanism that allows experts to handle far more complexity than novices within the same working-memory capacity. [[schema-automation]] is the further step: a schema becomes proceduralized to the point where its execution no longer requires working-memory resources at all. Automatic processing, once initiated, runs without conscious monitoring ([[automaticity]]).

[[chunking]] and [[cognitive-chunking]] describe the *phenomenology* of schema activation: expertise allows large amounts of information to be perceived and remembered as a single meaningful unit ([[chunk]]). The classical demonstration is chess masters who can reconstruct board positions from brief exposures because they perceive *configurations* (meaningful chunks) rather than individual pieces. [[hierarchical-chunk-structure]] elaborates how chunks nest within larger chunks, producing the multi-level organization visible in expert knowledge.

> [!key-claim] Schemas Are the Unit of Expertise
> The difference between novice and expert is not simply more knowledge. It is qualitatively different *organization* of knowledge. Experts' schemas are larger, more abstract, more interconnected, and more rapidly activated. [[pattern-recognition]] in expert domains is not intuition — it is schema-based rapid retrieval that feels non-deliberate because it has been automatized. This insight transforms expertise development from a motivational problem ("try harder") into an architectural one ("build better schemas through deliberate practice").

Encoding depth shapes which schemas form and how robust they are. [[levels-of-processing]] (Craik & Lockhart) established that deep, semantic encoding produces stronger, more durable memory traces than shallow, perceptual encoding. [[elaborative-encoding]] and [[encoding-depth]] elaborate the mechanism: memory traces are enriched by the connections drawn to pre-existing knowledge during encoding. This principle underlies the effectiveness of several learning strategies covered in §5.

The [[cognitive-theory-of-multimedia-learning]] (Mayer) extends CLT and schema theory into multimedia contexts. Its foundational claim — that humans process verbal and visual information through separate channels ([[dual-coding-theory]]) and that learning is strongest when both channels are used in a coordinated, non-redundant way — is among the best-validated findings in educational psychology. [[modality-effect]] is its most direct implication: spoken narration + visuals outperforms text + visuals because it distributes load across channels rather than overloading one.

[Prerequisite-For:: [[deliberate-practice]], [[retrieval-practice]], [[worked-examples]]]
[Synthesis-With:: [[cognitive-load-theory]], [[long-term-memory]], [[expertise-development]]]

---

## §4 — The Expert-Novice Continuum

Learning does not end at competence — it continues toward adaptive expertise, where knowledge is not only automated but flexibly deployable across novel contexts. [[expertise-development]] describes this arc; [[deliberate-practice]] (Ericsson) is its primary mechanism; and [[adaptive-expertise]] is its highest form.

The counterintuitive insight from expertise research is that practice in itself is insufficient for expert performance. What matters is *deliberate* practice: highly structured, feedback-dense, at the edge of current ability, with explicit focus on correcting weaknesses rather than performing strengths. The [[power-law-of-practice]] describes the characteristic learning curve: rapid improvement early, with gains becoming increasingly marginal — but real — at advanced levels. [[automaticity]] follows from deliberate practice: when a skill or knowledge structure has been practiced sufficiently, it no longer demands working-memory resources, freeing capacity for higher-order processing.

> [!tension] Automaticity vs. Adaptive Flexibility
> [[strategic-automaticity]] captures an important tension: automatized skills are efficient but brittle — they can fail in novel situations where the learned pattern doesn't cleanly apply. [[adaptive-expertise]] requires the capacity to disrupt and reconfigure automated routines when the situation demands it. This is why [[double-loop-learning]] (Argyris) — questioning the governing assumptions behind a strategy, not just optimizing the strategy — is structurally important for expert development beyond a certain level.

[[tacit-knowledge]] is the shadow side of expertise: the operational knowledge that experts cannot fully articulate. [[cognitive-pre-compilation]] describes how frequently executed knowledge structures become compressed and inaccessible to verbal report. The [[expert-blind-spot]] names the resulting failure mode: experts systematically underestimate the difficulty of material for novices because the novice's challenge (building schemas from scratch) is invisible from inside already-assembled expertise.

[[transfer-of-learning]] is the practical output of expertise — the capacity to apply knowledge to novel problems. [[far-transfer]] (across substantially different domains or contexts) is notoriously difficult to achieve and requires explicit attention during instruction. Achieving far transfer appears to require both deep schema formation *and* explicit practice varying the surface features of application problems, so that the underlying schema is indexed broadly rather than to a narrow context class.

[Synthesis-With:: [[schema-theory]], [[deliberate-practice]], [[self-regulated-learning]]]
[Related:: [[MOC - Motivation, Agency & Self-Regulation]] — motivation drives whether deliberate practice is sustained]

---

## §5 — Evidence-Based Learning Strategies

The cognitive science of learning has produced a small number of strategies with unusually strong empirical support. The strength of this evidence derives from multiple, independent lines of research converging on the same effects — replication across labs, populations, and material types. [[retrieval-practice-as-the-most-potent-single-strategy]] states the hierarchy explicitly: retrieving information from memory produces stronger long-term retention than re-reading, reviewing notes, or other restudy approaches by a substantial margin.

**The Retrieval Cluster.** [[retrieval-practice]] works because the act of retrieval itself modifies memory — it doesn't merely "test" what's there but restructures and strengthens the retrieved trace. The [[testing-effect]] is the empirical label for this phenomenon; [[spaced-retrieval]] is its temporal optimization. The [[forgetting-curve]] (Ebbinghaus) establishes why timing matters: memory degrades in a characteristic exponential pattern, and retrieving information just as it is about to be forgotten is more effective than retrieving it while it remains highly accessible. [[spaced-repetition]] systems (Anki, Mnemosyne) operationalize this by algorithmically scheduling retrievals at optimal intervals.

> [!key-claim] Desirable Difficulties Are Cognitively Demanding by Design
> [[desirable-difficulties]] (Bjork) is the theoretical framework that unifies spacing, interleaving, and retrieval practice. The key insight: conditions that feel easier during study (massed practice, re-reading) often produce weaker long-term retention than conditions that feel harder. Difficulty during encoding is not a sign of poor design — it is often the *signature* of deep processing that builds durable memory traces. This directly challenges naive intuitions about "good" study sessions.

**The Spacing Cluster.** [[spacing-effect]] refers to the robust finding that distributing practice across time produces better retention than massing it. [[interleaving]] — mixing different problem types or topics within a study session rather than blocking — produces an additional benefit: it forces the learner to identify which schema applies to which problem, strengthening the *access conditions* for knowledge retrieval rather than just the knowledge itself. [[interleaving-effect]] documents the evidence.

**The Elaboration Cluster.** [[elaboration]] is the practice of adding details, connections, and explanations to material beyond what the source provides. [[elaborative-interrogation]] (asking "why is this true?" and "how does this connect to what I already know?") is its most tractable implementation. [[self-explanation]] — generating explanations during learning — produces deeper encoding by forcing the learner to identify the gaps in their own understanding. All of these strategies exploit the [[levels-of-processing]] principle: deeper semantic processing during encoding produces more retrievable memory traces.

**The Generation Effect.** [[generation-effect]] establishes that information produced by the learner is retained better than identical information provided by the instructor. [[active-note-making]] and [[note-making-vs-note-taking]] in the PKB domain are direct applications: reprocessing source material in your own words leverages this effect at every entry into the vault.

[Synthesis-With:: [[schema-theory]], [[cognitive-load-theory]], [[metacognitive-monitoring]]]
[Related:: desirable-difficulties ↔ [[the-clt-desirable-difficulties-reconciliation]]]

---

## §6 — Instructional Design: Engineering the Environment

Strategies are something a learner applies; instructional design is what a designer builds. The design challenge is to translate the cognitive science of learning into *environmental affordances* — conditions that make productive processing more likely and parasitic load less likely.

[[four-component-instructional-design-4c-id]] (4C/ID, van Merriënboer) is among the most theoretically grounded and comprehensive instructional design models. Its core claim: complex skill acquisition requires the simultaneous development of whole-task performance (learning tasks), supportive information (conceptual knowledge enabling the task), procedural information (just-in-time rules and procedures), and part-task practice (for subskills requiring full automation). [[the-four-components-of-4c-id]] specifies the components; [[whole-task-approach]] makes the design philosophy explicit: learning from whole, realistic tasks from the beginning is superior to learning isolated components and hoping transfer occurs.

> [!key-claim] Worked Examples Are the Highest-Leverage Novice Intervention
> [[worked-examples]] are step-by-step solutions to sample problems. For novices, they dramatically reduce extraneous cognitive load (by removing the need for random means-ends search) and redirect freed capacity toward [[germane-cognitive-load]] — understanding the *structure* of the solution rather than just finding one. [[the-worked-example-effect]] documents the strong empirical support. The intervention's design implication is clear: novices should study worked examples more than they solve problems; this ratio should invert as expertise develops (see [[expertise-reversal-effect]]).

[[backward-design]] (Wiggins & McTighe) inverts the traditional design sequence: begin with the desired transfer outcomes, design assessment evidence for those outcomes, then build instruction backward from there. This counters the failure mode of teaching content that cannot be assessed or applied — "coverage" as a proxy for learning.

[[scaffolding]] and the [[zone-of-proximal-development]] (Vygotsky) establish the developmental logic: effective instruction operates at the frontier of what a learner cannot yet do independently but can accomplish with support. [[scaffolded-fading]] — gradually removing support as competence grows — is the operational protocol. [[scaffolding-fading-progression]] traces the full arc; [[scaffolding-sovereignty-progression]] frames this in terms of the learner's development toward autonomous self-direction, connecting instructional design to the motivational framework in [[MOC - Motivation, Agency & Self-Regulation]].

**Formative Assessment and Feedback.** [[formative-assessment]] closes the instructional loop by generating information about current learning state during the process rather than after it. [[assessment-design]] is the broader engineering challenge. [[feedback-design-for-autonomy-and-mastery]] addresses how feedback can be structured to support competence without undermining autonomy — a design tension at the intersection of CLT and SDT.

[Synthesis-With:: [[cognitive-load-theory]], [[schema-theory]], [[self-regulated-learning]]]
[Critique-Of:: bloom-s-taxonomy as taxonomy vs. [[instructional-design]] as *design* — the former classifies; the latter engineers]

---

## 🌉 Cross-Domain Bridges

> [!related] Companion MOCs
> - [[MOC - Motivation, Agency & Self-Regulation]] — Cognitive architecture explains *what* is built; motivation explains *why* a learner sustains the effort required to build it. The interface is sharp: [[cognitive-load-theory]] determines whether the task is within reach; [[self-efficacy]] determines whether the learner will attempt it; [[metacognitive-monitoring]] monitors whether progress is occurring.
> - [[MOC - Reasoning, Critical Thinking & Epistemology]] — [[dual-process-theory]] appears in both MOCs. In cognitive architecture it explains *how* processing works; in critical thinking it explains *why* biases occur. [[schema-theory]] connects to reasoning: well-formed schemas enable rapid pattern recognition, but poorly formed schemas enable heuristic errors.

The PKB cluster ([[personal-knowledge-base]], [[zettelkasten]], [[cognitive-load-theory-and-pkb-design]], [[the-pkb-as-constitutive-metacognitive-architecture]], [[externalized-cognitive-architecture]]) applies this entire MOC's content to knowledge management practice. A well-designed PKB is an *externalization* of long-term memory architecture — it offloads retrieval structure (wiki-links as spreading activation), reduces extraneous cognitive load (good note structure mirrors good schema structure), and supports elaborative encoding through active note-making.

---

## 🌅 Frontier & Open Questions

> [!frontier] Live debates within Cognitive Architecture & Learning Science
> - **Desirable difficulties and CLT are in tension**: If extraneous load should be minimized (CLT), but difficulty is desirable (Bjork), how do we distinguish productive difficulty from parasitic load? [[the-clt-desirable-difficulties-reconciliation]] addresses this but the synthesis remains contested.
> - **Long-term working memory**: [[long-term-working-memory]] (Ericsson & Kintsch) challenges the traditional view that working memory capacity is fixed. Expert performance draws on rapidly accessible long-term memory structures that effectively extend WM capacity. If true, WM limits are less fixed than CLT assumes.
> - **Transfer remains underpredicted**: The conditions under which deep learning produces far transfer are still poorly specified. Schema formation is necessary but not sufficient.

> [!frontier] Gaps in this MOC's coverage
> - **Affective dimensions of learning** — emotional regulation, academic emotions, flow — belong here but are better treated in [[MOC - Motivation, Agency & Self-Regulation]].
> - **Neuroscience foundations**: memory consolidation during sleep, retrieval-induced forgetting, and neuroimaging correlates of schema construction are not yet well-represented in the vault.
> - **Multimedia learning edge cases** — generative AI, interactive simulations, embodied learning ([[embodied-cognition]]) — are emerging domains that will require new notes.

---

## 📚 Index of Linked Notes

| Note | Section(s) |
|------|-----------|
| [[4e-cognition]] | Cross-domain |
| [[active-note-making]] | §5 |
| [[adaptive-expertise]] | §4 |
| [[attention-and-cognitive-control]] | §1 |
| [[automaticity]] | §3, §4 |
| [[backward-design]] | §6 |
| [[biologically-primary-knowledge]] | §2 |
| [[bloom-s-taxonomy]] | §6 |
| [[central-executive]] | §1 |
| [[chunk]] | §3 |
| [[chunking]] | §3 |
| [[cognitive-architecture]] | §1 |
| [[cognitive-chunking]] | §3 |
| [[cognitive-load-theory]] | §2 |
| [[cognitive-load-theory-and-pkb-design]] | §2, Bridges |
| [[cognitive-pre-compilation]] | §4 |
| [[cognitive-psychology]] | §1 |
| [[cognitive-psychology-foundations]] | §1 |
| [[cognitive-theory-of-multimedia-learning]] | §3 |
| [[complex-learning]] | §6 |
| [[declarative-memory]] | §1 |
| [[declarative-schemas]] | §3 |
| [[deep-processing]] | §5 |
| [[default-interventionist-architecture]] | §1 |
| [[deliberate-practice]] | §4 |
| [[desirable-difficulties]] | §5 |
| [[double-loop-learning]] | §4 |
| [[dual-coding-theory]] | §3 |
| [[dual-process-theory]] | §1 |
| [[elaboration]] | §5 |
| [[elaborative-encoding]] | §3 |
| [[elaborative-interrogation]] | §5 |
| [[elaborative-rehearsal]] | §5 |
| [[element-interactivity]] | §2 |
| [[encoding-depth]] | §3 |
| [[encoding-specificity-principle]] | §5 |
| [[episodic-buffer]] | §1 |
| [[episodic-memory]] | §1 |
| [[expert-blind-spot]] | §4 |
| [[expertise-development]] | §4 |
| [[expertise-reversal-effect]] | §2, §4 |
| [[externalized-cognitive-architecture]] | Bridges |
| [[far-transfer]] | §4 |
| [[forgetting-curve]] | §5 |
| [[formative-assessment]] | §6 |
| [[four-component-instructional-design-4c-id]] | §6 |
| [[generation-effect]] | §5 |
| [[germane-cognitive-load]] | §2 |
| [[hierarchical-chunk-structure]] | §3 |
| [[information-processing-theory]] | §1 |
| [[instructional-design]] | §6 |
| [[interleaving]] | §5 |
| [[interleaving-effect]] | §5 |
| [[intrinsic-cognitive-load]] | §2 |
| [[levels-of-processing]] | §3, §5 |
| [[long-term-memory]] | §1 |
| [[long-term-working-memory]] | §1, Frontier |
| [[magical-number-seven]] | §1 |
| [[memory-consolidation]] | §1 |
| [[modality-effect]] | §1, §3 |
| [[multi-store-model]] | §1 |
| [[non-declarative-memory]] | §1 |
| [[note-making-vs-note-taking]] | §5 |
| [[pattern-recognition]] | §3 |
| [[personal-knowledge-base]] | Bridges |
| [[phonological-loop]] | §1 |
| [[power-law-of-practice]] | §4 |
| [[prior-knowledge]] | §3 |
| [[procedural-memory]] | §1 |
| [[procedural-schemas]] | §3 |
| [[productive-failure]] | §6 |
| [[redundancy-effect]] | §2 |
| [[relational-complexity]] | §2 |
| [[retrieval-practice]] | §5 |
| [[retrieval-practice-as-the-most-potent-single-strategy]] | §5 |
| [[retrieval-structure]] | §1, §5 |
| [[scaffolded-fading]] | §6 |
| [[scaffolding]] | §6 |
| [[scaffolding-fading-progression]] | §6 |
| [[scaffolding-sovereignty-progression]] | §6 |
| [[schema]] | §3 |
| [[schema-automation]] | §3 |
| [[schema-construction]] | §3 |
| [[schema-theory]] | §3 |
| [[self-explanation]] | §5 |
| [[semantic-memory]] | §1 |
| [[short-term-memory]] | §1 |
| [[spaced-repetition]] | §5 |
| [[spaced-retrieval]] | §5 |
| [[spacing-effect]] | §5 |
| [[split-attention-effect]] | §2 |
| [[spreading-activation]] | §1 |
| [[strategic-automaticity]] | §4 |
| [[sweller-s-2010-reconceptualization]] | §2 |
| [[tacit-knowledge]] | §4 |
| [[testing-effect]] | §5 |
| [[the-clt-desirable-difficulties-reconciliation]] | §5, Frontier |
| [[the-expertise-reversal-effect]] | §2, §4 |
| [[the-standard-three-load-taxonomy]] | §2 |
| [[the-worked-example-effect]] | §6 |
| [[transfer-of-learning]] | §4 |
| [[type-1-processing]] | §1 |
| [[type-2-processing]] | §1 |
| [[visuospatial-sketchpad]] | §1 |
| [[whole-task-approach]] | §6 |
| [[why-element-interactivity-is-the-engine-of-intrinsic-load]] | §2 |
| [[worked-examples]] | §6 |
| [[working-memory]] | §1 |
| [[working-memory-capacity]] | §1 |
| [[working-memory-in-the-clt-framework]] | §2 |
| [[zettelkasten]] | Bridges |
| [[zone-of-proximal-development]] | §6 |

---

> [!info] MOC Metadata
> - **Pattern**: Progressive
> - **Source notes**: ~182
> - **Word count**: ~4,800
> - **Generated**: 2026-04-25 by MOC Specialist Agent v1.0.0
> - **Audit trail**: `MOCs/_meta/MOC - Cognitive Architecture & Learning Science.audit.md`
> - **Next review suggested**: 2026-07-25