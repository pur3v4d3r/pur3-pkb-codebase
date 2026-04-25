---
tags: [moc, domain-epistemology, domain-critical-thinking, domain-logic, status-seedling]
aliases: [Critical Thinking MOC, Epistemology MOC, Logic MOC, Reasoning MOC]
created: 2026-04-25
modified: 2026-04-25
status: seedling
type: moc
moc_pattern: cluster
domain: Reasoning, Critical Thinking & Epistemology
source_notes_count: 62
target_word_count: 3200
audience: [practitioner, researcher]
maturity: established
parent_moc: null
related_mocs: ["[[moc-cognitive-architecture-learning-science]]", "[[moc-motivation-agency-self-regulation]]"]
version: 1.0.0
---

# Reasoning, Critical Thinking & Epistemology — Map of Content

> [!abstract] Domain & Scope
> **Reasoning, Critical Thinking & Epistemology** is the study of *how people should think* (normative logic), *how people actually think* (cognitive bias and heuristics), and *what intellectual character supports good thinking* (epistemic virtue). This MOC organizes ~62 permanent notes spanning formal logic, informal reasoning patterns, dual-process theory and biases, critical thinking frameworks, and epistemic virtues. It is structured as a **cluster architecture** — five co-equal sub-domains, each internally coherent but richly interconnected.
>
> **For**: Anyone developing systematic reasoning capacities; practitioners applying argumentation; researchers in epistemology or cognitive science.
> **Companion MOCs**: [[MOC - Cognitive Architecture & Learning Science]] (dual-process theory), [[MOC - Motivation, Agency & Self-Regulation]] (motivated reasoning)
> **Reading time**: ~18 min full read; clusters can be entered independently.

## 🗺️ Navigation

- **[§1 — Formal Logic & Argument Architecture](#1-formal-logic-and-argument-architecture)** — deductive, inductive, propositional, predicate logic
- **[§2 — Informal Reasoning Patterns](#2-informal-reasoning-patterns)** — abductive, analogical, causal reasoning
- **[§3 — Dual Process Theory & the Bias Landscape](#3-dual-process-theory-and-the-bias-landscape)** — System 1/2, heuristics, biases
- **[§4 — Critical Thinking Frameworks & Practice](#4-critical-thinking-frameworks-and-practice)** — Paul-Elder, Socratic method, scientific reasoning
- **[§5 — Epistemic Virtues & Intellectual Character](#5-epistemic-virtues-and-intellectual-character)** — intellectual humility, epistemic vigilance, virtue epistemology
- **[🌉 Cross-Domain Bridges](#cross-domain-bridges)**
- **[🌅 Frontier & Open Questions](#frontier-and-open-questions)**
- **[📚 Index of Linked Notes](#index-of-linked-notes)**

---

## §1 — Formal Logic & Argument Architecture

Formal logic provides the normative skeleton for valid reasoning — the standards against which actual reasoning can be evaluated. The core formal systems represented in the vault span several levels of expressiveness.

[[propositional-logic]] is the base level: a system for evaluating the validity of arguments whose structure depends on the logical relationships between atomic propositions connected by operators (AND, OR, NOT, IF-THEN). Its expressive power is limited — it cannot reason about the internal structure of propositions — but its inference rules ([[deductive-logic]], [[deductive-reasoning]]) are the foundation for understanding what validity means: an argument is valid if and only if it is *impossible* for all premises to be true and the conclusion false, regardless of whether the premises are actually true.

[[predicate-logic]] extends propositional logic by introducing quantifiers and predicates, enabling reasoning about objects and their properties. The gain in expressive power comes at the cost of computational tractability — predicate logic is undecidable in general, which has implications for the limits of formal reasoning systems. [[modal-logic]] further extends this by adding operators for necessity and possibility, relevant for reasoning about counterfactuals and probabilistic claims.

> [!definition] Validity vs. Soundness vs. Cogency
> These three standards are routinely conflated. **Validity** (deductive) concerns logical form: does the conclusion follow necessarily from the premises? **Soundness** adds a factual requirement: is the argument valid AND are all premises true? A sound argument guarantees a true conclusion. **Cogency** is the inductive analog of soundness: the argument is inductively strong AND the premises are true. These distinctions are load-bearing for [[argument-analysis]].

[[inductive-logic]] and [[inductive-reasoning]] are formally distinct from deduction: an inductive argument supports its conclusion with varying degrees of probability but never guarantees it. The strength of an inductive argument is defeasible — new evidence can always weaken or defeat it. This is the logical backbone of [[scientific-reasoning]], where hypotheses are confirmed or disconfirmed by evidence that never entails them deductively. [[inference]] covers the general capacity for drawing conclusions from evidence.

[Synthesis-With:: [[argument-analysis]], [[scientific-reasoning]], [[abductive-reasoning]]]

---

## §2 — Informal Reasoning Patterns

Beyond formal logic, reasoning in real domains deploys several informal inference patterns that are not captured by deductive validity but are epistemically legitimate when applied correctly.

[[abductive-reasoning]] (inference to the best explanation) is the pattern by which we infer the most plausible hypothesis given a set of observations. It is neither deductively valid nor purely inductive — it introduces theoretical posits not contained in the evidence and justifies them by their explanatory power. Medical diagnosis, scientific theory formation, and everyday causal attribution ([[attribution-theory]] in [[MOC - Motivation, Agency & Self-Regulation]]) all run primarily on abductive inference. [[abductive-logic]] provides the formal treatment.

[[analogical-reasoning]] — inferring that because two things share some properties, they likely share others — is among the most powerful and dangerous of informal inference patterns. When the analogy's constraints are tight, it enables productive transfer of knowledge across domains; when they are loose, it generates superficial and misleading conclusions. [[analogical-logic]] addresses the formal conditions under which analogical inferences are well-formed.

> [!tension] Abduction and Theory Choice: The Underdetermination Problem
> A persistent problem in [[philosophy-of-science]] is that multiple competing hypotheses can often explain the same evidence equally well. Abductive reasoning picks the "best" explanation, but the criteria for "best" (simplicity, scope, fertility) are themselves contested and can be gamed. [[scientific-reasoning]] and [[fallibilism]] both grapple with this: scientific knowledge is provisional and underdetermined; the appropriate response is neither naive realism nor epistemic relativism but [[fallibilism]] — holding beliefs with confidence proportional to evidence while remaining genuinely open to revision.

[[logical-fallacies]] catalogs the common formal and informal violations: ad hominem, false dichotomy, slippery slope, appeal to authority, etc. These are not merely rhetorical tricks — they represent specific structural failures in argument that [[argument-analysis]] training should enable detection of.

[Synthesis-With:: [[critical-thinking]], [[attribution-theory]], [[epistemic-vigilance]]]

---

## §3 — Dual Process Theory & the Bias Landscape

The most important empirical contribution to understanding *actual* human reasoning is [[dual-process-theory]] — the discovery that reasoning deploys two qualitatively different processing systems with distinct properties, speeds, and failure modes (see §1 in [[MOC - Cognitive Architecture & Learning Science]] for the cognitive architecture account).

[[system-1]] ([[type-1-processing]]) is fast, automatic, associative, and largely unconscious. It enables rapid pattern recognition and effortless social cognition but is also the source of most cognitive biases. [[system-2]] ([[type-2-processing]]) is slow, deliberate, rule-governed, and conscious — it can override System 1 outputs but only when sufficiently activated and only with significant cognitive effort. [[bounded-rationality]] (Simon) frames this computationally: cognitive agents are not optimizers but satisficers, using heuristics because they are fast and frugal relative to the costs of full optimization.

[[heuristics-and-biases]] (Kahneman & Tversky) is the research program that cataloged the systematic errors that result from System 1's heuristic shortcuts. [[availability-heuristic]] — judging probability by how easily examples come to mind — produces reliable errors when ease of recall is not correlated with actual frequency. [[confirmation-bias]] — the tendency to seek, interpret, and remember information that confirms pre-existing beliefs — is among the most pervasive and consequential biases for intellectual work. [[attribute-substitution]] names the general mechanism behind many biases: when faced with a difficult question, System 1 substitutes an easier question and answers that instead, without the substitution being noticed by System 2. [[cognitive-miserliness]] describes the disposition that makes substitution the default: System 2 engagement is expensive and human cognition is generally reluctant to pay the cost.

> [!key-claim] Motivated Reasoning Is Bias in Service of Identity
> [[motivated-reasoning]] is a special case where cognitive bias is driven not by processing efficiency but by the need to reach a desired conclusion. The motivation may be emotional (self-protection, identity consistency) or social (maintaining group membership, avoiding conflict). It is the overlap point between the motivational architecture described in [[MOC - Motivation, Agency & Self-Regulation]] and the reasoning architecture described here — when the autonomy or relatedness need is threatened by an accurate conclusion, the mind can systematically distort reasoning to avoid that conclusion.

[Synthesis-With:: [[critical-thinking]], [[intellectual-humility]], [[attribution-theory]]]

---

## §4 — Critical Thinking Frameworks & Practice

If §3 describes how reasoning fails, §4 describes the frameworks and practices that help it succeed. [[critical-thinking]] and [[critical-reasoning]] describe the broad competence; several structured frameworks operationalize it.

[[paul-elder-critical-thinking-framework]] ([[paul-elder-framework]]) is among the most comprehensive practitioner frameworks. It organizes critical thinking around the *Elements of Thought* (purpose, question at issue, information, inferences, concepts, assumptions, implications, point of view) and the *Intellectual Standards* (clarity, accuracy, precision, relevance, depth, breadth, logic, significance, fairness). The framework's strength is its universality: it applies to any domain of reasoning, not just formal argumentation. [[intellectual-standards]] provides the normative criteria.

[[socratic-method]] — disciplined questioning that progressively reveals assumptions, contradictions, and unstated premises — is the oldest and most durable critical thinking practice. Its power lies in exposing the gap between what a person *thinks* they know and what they can actually defend. [[deweys-reflective-thinking]] provides the pragmatist account: genuine thinking begins when a *problem* is felt, not when information is delivered. The implication for instruction: genuine critical thinking cannot be transmitted by lecture — it must be provoked by real difficulty.

[[scientific-reasoning]] applies the critical thinking disposition to empirical claims: forming hypotheses, identifying falsifying conditions, designing controlled comparisons, and distinguishing correlation from causation. [[delphi-report]] documents the broad consensus on critical thinking competencies across domain experts.

> [!key-claim] Disposition Is as Important as Skill
> The [[delphi-report]] emphasized that critical thinking is not merely a cognitive skill but a *disposition* — an habitual inclination to deploy critical tools rather than merely possessing them. [[reflective-disposition]] and [[disposition]] capture this: someone who knows logical fallacies but doesn't apply them in actual discourse has skill without disposition. Developing critical thinking requires cultivating the *desire* to think critically, not just the capacity to do so.

[Synthesis-With:: [[epistemic-vigilance]], [[intellectual-humility]], [[dual-process-theory]]]

---

## §5 — Epistemic Virtues & Intellectual Character

Epistemic virtue theory asks: what character traits support truth-tracking, and how can they be cultivated? It bridges ethics and epistemology by treating good believing and reasoning as achievements of intellectual character, not just of cognitive process.

[[virtue-epistemology]] frames intellectual traits (open-mindedness, intellectual courage, thoroughness, rigor) as virtues that, when exercised reliably, tend to produce well-grounded beliefs. Like moral virtues, epistemic virtues are *stable dispositions* that must be cultivated through practice rather than simply adopted by decision.

[[intellectual-humility]] is the recognition of the limits and fallibility of one's own beliefs — not self-deprecation but accurate calibration of epistemic confidence. It is the motivational prerequisite for genuine learning: a person who cannot acknowledge the limits of their knowledge cannot update it. [[intellectual-humility]] connects back to both §3 (where its absence enables confirmation bias) and [[MOC - Motivation, Agency & Self-Regulation]] §7 (where metacognitive calibration performs a similar function).

[[epistemic-vigilance]] (Sperber & Mercier) is a complementary virtue: the capacity to critically evaluate incoming information rather than accepting it credulously. It is the disposition underlying healthy skepticism — neither refusing to update beliefs nor updating them on insufficient grounds. [[fallibilism]] is the epistemological stance that supports epistemic vigilance: all beliefs are held provisionally, subject to revision, but provisionally held beliefs can nonetheless guide action with appropriate confidence.

[[pragmatism]] ([[pragmatic-maxim]]) provides the underlying epistemological framework: the meaning of a belief is found in its practical consequences; beliefs that lead to successful action are warranted. This anti-foundationalist stance situates knowledge in the context of inquiry rather than in correspondence to mind-independent reality — a position that has major implications for how we understand the relationship between evidence, belief, and action.

[Synthesis-With:: [[critical-thinking]], [[metacognitive-calibration]], [[reflective-disposition]]]

---

## 🌉 Cross-Domain Bridges

> [!related] Companion MOCs
> - [[MOC - Cognitive Architecture & Learning Science]] — [[dual-process-theory]] is treated there as a mechanism of memory and learning; here it is treated as a mechanism of reasoning failure. Both accounts are necessary; neither is complete without the other. [[schema-theory]] connects: biases are often schema-driven rapid inferences that bypass deliberate evaluation.
> - [[MOC - Motivation, Agency & Self-Regulation]] — [[motivated-reasoning]] is the bridge note. The autonomy need's defense mechanisms shape how people process threatening evidence. [[intellectual-humility]] is both an epistemic virtue and a motivational orientation toward one's own fallibility.

---

## 🌅 Frontier & Open Questions

> [!frontier] Live debates
> - **Fast and frugal heuristics vs. heuristics-and-biases**: Gigerenzen and colleagues argue that many System 1 heuristics are ecologically rational (correct in the environments where they evolved) rather than straightforwardly biased. This challenges the Kahneman-Tversky program. [[heuristics-and-biases]] and [[high-validity-environment]] are the relevant notes.
> - **Can critical thinking be taught as domain-general?**: The empirical evidence for transfer of critical thinking training is thin. Domain-specific critical thinking (scientific reasoning, legal reasoning) transfers poorly to other domains. This challenges the general-skills model of critical thinking pedagogy.

> [!frontier] Gaps in this MOC's coverage
> - The vault has notes on individual reasoning but less on **social epistemology** — how groups reason, where collective intelligence emerges, and where it fails (groupthink, epistemic bubbles).
> - **Probabilistic reasoning** — Bayesian inference, base-rate neglect, calibration of subjective probabilities — is underrepresented despite strong connections to scientific reasoning and epistemic vigilance.

---

## 📚 Index of Linked Notes

| Note | Section(s) |
|------|-----------|
| [[abductive-logic]] | §2 |
| [[abductive-reasoning]] | §2 |
| [[analogical-logic]] | §2 |
| [[analogical-reasoning]] | §2 |
| [[argument-analysis]] | §1, §4 |
| [[attribute-substitution]] | §3 |
| [[availability-heuristic]] | §3 |
| [[bounded-rationality]] | §3 |
| [[cognitive-bias]] | §3 |
| [[cognitive-miserliness]] | §3 |
| [[confirmation-bias]] | §3 |
| [[critical-reasoning]] | §4 |
| [[critical-thinking]] | §4 |
| [[deductive-logic]] | §1 |
| [[deductive-reasoning]] | §1 |
| [[delphi-report]] | §4 |
| [[deweys-reflective-thinking]] | §4 |
| [[disposition]] | §4 |
| [[dual-process-theory]] | §3 |
| [[epistemic-vigilance]] | §5 |
| [[fallibilism]] | §2, §5 |
| [[heuristics-and-biases]] | §3 |
| [[high-validity-environment]] | Frontier |
| [[inductive-logic]] | §1 |
| [[inductive-reasoning]] | §1 |
| [[inference]] | §1 |
| [[intellectual-humility]] | §5 |
| [[intellectual-standards]] | §4 |
| [[logical-fallacies]] | §2 |
| [[modal-logic]] | §1 |
| [[motivated-reasoning]] | §3, Bridges |
| [[paul-elder-critical-thinking-framework]] | §4 |
| [[paul-elder-framework]] | §4 |
| [[philosophy-of-science]] | §2 |
| [[pragmatic-maxim]] | §5 |
| [[pragmatism]] | §5 |
| [[predicate-logic]] | §1 |
| [[propositional-logic]] | §1 |
| [[reflective-disposition]] | §4, §5 |
| [[reflective-thinking]] | §4 |
| [[scientific-reasoning]] | §1, §4 |
| [[socratic-method]] | §4 |
| [[system-1]] | §3 |
| [[system-2]] | §3 |
| [[type-1-processing]] | §3 |
| [[type-2-processing]] | §3 |
| [[virtue-epistemology]] | §5 |

---

> [!info] MOC Metadata
> - **Pattern**: Cluster (5 co-equal sub-domains)
> - **Source notes**: ~62
> - **Word count**: ~3,100
> - **Generated**: 2026-04-25 by MOC Specialist Agent v1.0.0
> - **Audit trail**: `MOCs/_meta/MOC - Reasoning, Critical Thinking & Epistemology.audit.md`
> - **Next review suggested**: 2026-07-25