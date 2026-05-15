---
tags: [moc, domain-critical-thinking, domain-logic, domain-argumentation, status-evergreen]
aliases: [Critical Thinking MOC, Logic MOC, Argumentation MOC]
created: 2026-05-15
modified: 2026-05-15
status: evergreen
type: moc
moc_pattern: progressive
domain: Critical Thinking and Logic
source_notes_count: 67
target_word_count: 5500
audience: [practitioner, researcher]
maturity: established
parent_moc: "[[MOC - Cognitive Science (Master Index)]]"
related_mocs: ["[[MOC - Epistemology]]", "[[MOC - Dual Process Theory and Cognitive Biases]]"]
version: 1.0.0
---

# Critical Thinking and Logic — Map of Content

> [!abstract] Domain & Scope
> **Critical thinking** is the disciplined, metacognitive process of analysing and evaluating reasoning — one's own and others' — to reach well-grounded judgments and decisions. It encompasses formal logic, informal reasoning, argument analysis, and the cognitive dispositions that sustain rational inquiry. This MOC organises 67 permanent notes covering the structure of arguments, formal and informal logic, fallacy taxonomy, critical thinking frameworks, and the intellectual virtues that make sustained critical inquiry possible. It is structured **progressively** — from argument structure (the atom) → logical forms (the molecule) → fallacies (errors) → CT frameworks (application systems) → intellectual virtues (dispositional foundations).
>
> **For**: Practitioners, educators, students of philosophy and reasoning
> **Companion MOCs**: [[MOC - Epistemology]], [[MOC - Dual Process Theory and Cognitive Biases]]
> **Reading time**: ~26 minutes

## 🗺️ Navigation

- **[Argument Anatomy](#argument-anatomy)** — premises, conclusions, inference
- **[Deductive Logic](#deductive-logic)** — validity, soundness, formal systems
- **[Inductive and Abductive Reasoning](#inductive-and-abductive-reasoning)** — probability, inference to best explanation
- **[The Fallacy Taxonomy](#the-fallacy-taxonomy)** — formal and informal errors
- **[Critical Thinking Frameworks](#critical-thinking-frameworks)** — Paul-Elder, Facione, Delphi
- **[Intellectual Virtues and Dispositions](#intellectual-virtues-and-dispositions)** — the character of good thinking
- **[Cross-Domain Bridges](#cross-domain-bridges)**
- **[Frontier & Open Questions](#frontier--open-questions)**
- **[Index of Linked Notes](#index-of-linked-notes)**

---

## Argument Anatomy

Every act of reasoning that goes beyond mere assertion involves an **argument** — a structured claim in which premises are offered as reasons supporting a conclusion. Understanding argument structure is the prerequisite for evaluating arguments.

### The Basic Structure

[[argument-structure|Argument structure]] involves at minimum: one or more *premises* (claim offered as evidence or grounds), a *conclusion* (claim being supported), and an *inference* (the move from premises to conclusion). [[argument-analysis|Argument analysis]] is the skill of identifying these components in natural language, where they are rarely labelled explicitly.

[[argument-reconstruction|Argument reconstruction]] is the interpretive discipline of rendering natural language arguments in standard form — explicit premises, explicit conclusion, with suppressed premises ([[enthymeme|enthymemes]]) made visible. Reconstruction is always an act of interpretation that requires a principle of charity: we render the argument in its strongest plausible form before evaluating it. [[principle-of-charity|The principle of charity]] is both an ethical and epistemic norm — ethical because it treats interlocutors with respect; epistemic because defeating a strong version of an argument is more informative than defeating a straw version.

[[argument-mapping|Argument mapping]] externalises complex argument structures as tree diagrams, revealing the hierarchical relationships between claims. [[steelmanning|Steelmanning]] — constructing the strongest possible version of an opposing argument before responding — is the highest form of charitable reconstruction.

> [!definition] Inference vs Implication
> **Inference** is the act of a reasoner drawing a conclusion from premises. **Implication** is a semantic relationship between propositions (A implies B if B is true whenever A is). Conflating them is a source of significant argumentative error: not everything a statement implies is something the speaker has inferred or endorsed.

### The Toulmin Model

[[toulmin-argument-model|The Toulmin model]] is a schema for argument that extends beyond premise-conclusion structure to include *warrants* (the principles authorising the inference), *backing* (grounds for the warrant), *qualifiers* (modality of the claim), and *rebuttals* (exceptions). It is particularly useful for natural language arguments in domains where formal validity is not the appropriate standard (legal reasoning, policy debate, everyday persuasion).

---

## Deductive Logic

Deductive reasoning is reasoning in which the conclusion is *entailed* by the premises — if the premises are true, the conclusion *must* be true. Deductive validity is the guarantee of this entailment; soundness adds that the premises must also be true.

### Validity and Soundness

[[valid-argument|A valid argument]] is one in which the truth of the premises guarantees the truth of the conclusion — the logical form is correct regardless of actual content. [[sound-argument|A sound argument]] is valid *and* has true premises. [[validity-vs-soundness|The distinction]] matters practically: valid arguments can have false conclusions (via false premises); sound arguments cannot.

[[deductive-reasoning|Deductive reasoning]] operates with logical *necessity* — if the inferential form is correct, the conclusion follows necessarily. The paradigm forms:

- **[[modus-ponens|Modus Ponens]]**: If P, then Q; P; therefore Q.
- **[[modus-tollens|Modus Tollens]]**: If P, then Q; Not Q; therefore Not P.
- **[[categorical-syllogism|Categorical Syllogism]]**: All M are P; All S are M; therefore All S are P.
- **[[contrapositive|Contrapositive]]**: If P → Q, then ¬Q → ¬P (logically equivalent).

### Formal Logic Systems

[[formal-logic|Formal logic]] provides symbolic languages with explicit syntax and semantics for representing and evaluating deductive arguments.

[[propositional-logic|Propositional logic]] deals with propositions and their connectives (and, or, not, if-then). [[truth-tables|Truth tables]] systematically evaluate the truth value of complex propositions under all possible combinations of atomic truth values — the gold standard for checking propositional validity. [[logical-form|Logical form]] is what propositional and predicate logic make explicit: two arguments with identical forms have the same validity status regardless of their content.

[[predicate-logic|Predicate logic]] (first-order logic) extends propositional logic to capture the internal structure of propositions — subjects, predicates, quantifiers (all, some, no). It can represent the syllogistic forms above and much more complex inferential relationships. [[modal-logic|Modal logic]] adds operators for necessity and possibility.

[[conditional-reasoning|Conditional reasoning]] research demonstrates that ordinary humans systematically make errors with conditional arguments — particularly the fallacious forms *affirming the consequent* (if P→Q, and Q, therefore P) and *denying the antecedent* (if P→Q, and not-P, therefore not-Q). These errors are systematic and resist correction through simple instruction, suggesting they reflect [[dual-process-theory|Type 1 processing]] defaults.

---

## Inductive and Abductive Reasoning

Not all reasoning is deductive. The majority of reasoning in everyday life, science, and scholarship is inductive or abductive — probable rather than necessary.

### Inductive Reasoning

[[inductive-reasoning|Inductive reasoning]] draws general conclusions from particular instances. The standard of evaluation is not validity but *strength* — a [[strong-argument|strong argument]] is one where the premises make the conclusion probable. [[cogent-argument|A cogent argument]] is strong with true premises.

[[inductive-logic|Inductive logic]] encompasses several forms: enumerative induction (generalising from cases), statistical induction, and analogical induction. [[argument-from-analogy|Arguments from analogy]] conclude that because two things share known properties, they likely share the target property — their strength depends on the number, relevance, and diversity of the shared properties, and the absence of disanalogies.

[[bayesian-reasoning|Bayesian reasoning]] is the normatively correct framework for updating beliefs in light of evidence: the posterior probability of a hypothesis is proportional to its prior probability multiplied by the likelihood of the evidence given the hypothesis. [[base-rate-neglect|Base-rate neglect]] — ignoring prior probabilities in favour of vivid case-specific evidence — is among the most consequential cognitive errors in probabilistic reasoning (see [[MOC - Dual Process Theory and Cognitive Biases]]).

### Abductive Reasoning

[[abductive-reasoning|Abductive reasoning]] — inference to the best explanation — is the fundamental inference form in scientific discovery, diagnosis, and interpretation. [[inference-to-the-best-explanation|Inference to the best explanation]] evaluates competing hypotheses by explanatory criteria: simplicity, scope, fit with background knowledge, and avoidance of ad hoc supplementation.

[[abductive-logic|Abductive logic]] is weaker than deductive entailment and is not truth-preserving in the way deduction is — the best current explanation may be false. But it is the inference form that actually advances knowledge in conditions of genuine uncertainty.

---

## The Fallacy Taxonomy

Fallacies are arguments that appear valid or persuasive but are not. The distinction between *formal* and *informal* fallacies organises the taxonomy.

### Formal Fallacies

**Formal fallacies** violate the structural rules of valid deduction — the logical form is incorrect regardless of content. Affirming the consequent and denying the antecedent are the canonical formal fallacies. [[circular-reasoning|Circular reasoning]] (begging the question) assumes the conclusion as a premise, making the argument trivially valid but epistemically worthless — [[begging-the-question|begging the question]] generates no independent support for the conclusion.

### Informal Fallacies

[[logical-fallacies|Informal fallacies]] (covered by [[informal-fallacy|informal fallacy]] taxonomy) arise not from formal invalidity but from irrelevance, ambiguity, or unwarranted presumption.

**Relevance fallacies**: the premise offered is not genuinely relevant to the conclusion.
- [[ad-hominem|Ad hominem]]: attacking the arguer rather than the argument
- [[appeal-to-authority|Appeal to authority]]: invoking authority without relevant expertise
- [[appeal-to-emotion|Appeal to emotion]]: using emotional manipulation in place of evidence
- [[red-herring-fallacy|Red herring]]: introducing irrelevant material to distract
- [[straw-man-fallacy|Straw man]] / [[strawman-argument|Strawman]]: misrepresenting an argument to make it easier to attack

**Inductive fallacies**: arguments that fail inductive standards.
- [[hasty-generalization|Hasty generalisation]]: drawing general conclusions from insufficient evidence
- [[false-cause-fallacy|False cause]]: assuming correlation is causation
- [[slippery-slope-fallacy|Slippery slope]]: assuming one step inevitably leads to extreme consequences without sufficient reason
- [[false-dichotomy|False dichotomy]]: presenting only two options when others exist
- [[appeal-to-nature|Appeal to nature]]: assuming natural = good/true/better

**Presumption fallacies**: arguments that build on unwarranted assumptions.
- [[begging-the-question|Begging the question]]: circular reasoning
- [[equivocation-fallacy|Equivocation]]: exploiting ambiguity by shifting a word's meaning mid-argument

```
FALLACY TAXONOMY (PARTIAL)
═════════════════════════════════════════════════════
FORMAL FALLACIES (structural errors)
│  Affirming the consequent
│  Denying the antecedent
│  Begging the question (circular)
│
INFORMAL FALLACIES
├── Relevance (premise ≠ relevant to conclusion)
│   ├── Ad hominem, Red Herring, Straw Man
│   └── Appeal to Authority/Emotion/Nature
│
├── Inductive Errors (sample/generalisation problems)
│   ├── Hasty Generalisation, False Cause
│   └── Slippery Slope, False Dichotomy
│
└── Presumption (unwarranted assumptions)
    ├── Equivocation, Appeal to Ignorance
    └── Genetic Fallacy, No True Scotsman
═════════════════════════════════════════════════════
```

[[burden-of-proof|Burden of proof]] determines who is obligated to produce evidence for a claim. [[appeal-to-ignorance|Appeal to ignorance]] (arguing that a claim is true because it hasn't been disproven) is a failure to respect burden of proof — absence of evidence is not evidence of absence, *unless* evidence should have appeared if the claim were true.

---

## Critical Thinking Frameworks

Several models systematise critical thinking as a teachable, assessable competency.

### The Delphi Report and Facione's Model

[[delphi-report|The Delphi Report]] (1990) established the consensus definition of critical thinking as "purposeful, self-regulatory judgment" involving cognitive skills (interpretation, analysis, evaluation, inference, explanation) and the dispositions that motivate their use. [[facione-critical-thinking-model|Facione's model]] operationalises this framework and grounds the [[critical-thinking-dispositions-taxonomy|critical thinking dispositions taxonomy]] in empirical CT measurement.

### Paul-Elder Framework

[[paul-elder-critical-thinking-framework|The Paul-Elder framework]] organises critical thinking around *elements of thought* — eight components of reasoning (purpose, question, information, interpretation, concepts, assumptions, implications, point of view) evaluated against [[intellectual-standards|intellectual standards]] (clarity, accuracy, precision, relevance, depth, breadth, logic, significance, fairness).

[[paul-elder-framework|Paul and Elder's]] central contribution is the insistence that critical thinking is *not* separable from subject matter: you cannot think critically "in general" — you must think critically *about* something from within a discipline's standards and concepts. This connects CT to domain epistemology.

### Watson-Glaser Model

[[watson-glaser-model|The Watson-Glaser model]] operationalises critical thinking as five measurable sub-skills: inference, recognition of assumptions, deduction, interpretation, and evaluation of arguments. It is the most widely used psychometric instrument for CT assessment in professional and educational contexts.

---

## Intellectual Virtues and Dispositions

Critical thinking frameworks agree that skill alone is insufficient — a skilled reasoner who chooses not to apply their skills when inconvenient is not genuinely critical. The **dispositional** dimension comprises the intellectual character traits that motivate sustained, fair, and rigorous inquiry.

The core intellectual virtues (drawing from [[virtue-epistemology|virtue epistemology]] and CT literature):

- **[[intellectual-humility|Intellectual humility]]**: accurate awareness of one's cognitive limitations and susceptibility to error; willingness to revise beliefs under evidence
- **[[intellectual-courage|Intellectual courage]]**: willingness to follow reasoning to uncomfortable conclusions; resisting social pressure to affirm comfortable falsehoods
- **[[intellectual-empathy|Intellectual empathy]]**: genuine effort to understand positions one disagrees with from the inside — the reasoning capacity that enables [[steelmanning|steelmanning]]
- **[[intellectual-integrity|Intellectual integrity]]**: applying the same reasoning standards to one's own claims as to others'; resisting motivated reasoning
- **[[open-mindedness|Open-mindedness]]**: genuine consideration of alternatives; not captured by [[epistemic-closure|epistemic closure]]
- **[[fair-mindedness|Fair-mindedness]]**: consistent application of epistemic standards across different viewpoints
- **[[truth-seeking-disposition|Truth-seeking]]**: valuing accuracy over comfort; [[epistemic-cowardice|epistemic cowardice]] (giving deliberately vague answers to avoid controversy) is its corruption

> [!key-claim] Virtues and Skills Are Jointly Necessary
> A highly skilled reasoner who lacks intellectual courage will deploy their skills selectively — supporting conclusions they already hold (confirmation bias as motivated reasoning). A person of great intellectual character who lacks the skills of argument analysis will be unable to act on their good intentions. CT requires both, and neither alone is sufficient.

[Synthesis-With:: [[MOC - Epistemology]]]

---

## 🌉 Cross-Domain Bridges

> [!related] Companion MOCs
> - [[MOC - Epistemology]] — The intellectual virtues that ground CT are analysed as *epistemic virtues* in epistemology; the justification structures that CT evaluates are the subject of epistemological theory.
> - [[MOC - Dual Process Theory and Cognitive Biases]] — Cognitive biases are the cognitive-psychological explanation for why intelligent people reason poorly; fallacy taxonomy is the logical-normative description of the same phenomena.
> - [[MOC - Social Psychology]] — Groupthink, conformity, and social influence are the social conditions that suppress independent critical inquiry.

---

## 🌅 Frontier & Open Questions

> [!frontier] Open questions
> - **Transfer**: CT skills learned in one domain show limited transfer to others. Is CT domain-general or a collection of domain-specific skills?
> - **Measurement**: Existing CT assessments conflate general intelligence, domain knowledge, and CT skill. More precise instruments are needed.
> - **Dispositions vs skills**: The relationship between CT dispositions and CT skills is not well understood — do dispositions cause skill development, vice versa, or are they independently acquired?

---

## 📚 Index of Linked Notes

| Note | Type | Section |
|------|------|---------|
| [[abductive-reasoning]] | atomic | Inductive/Abductive |
| [[ad-hominem]] | atomic | Fallacies |
| [[appeal-to-authority]] | atomic | Fallacies |
| [[appeal-to-emotion]] | atomic | Fallacies |
| [[appeal-to-ignorance]] | atomic | Fallacies |
| [[appeal-to-nature]] | atomic | Fallacies |
| [[argument-analysis]] | reference | Anatomy |
| [[argument-from-analogy]] | atomic | Inductive |
| [[argument-mapping]] | atomic | Anatomy |
| [[argument-reconstruction]] | atomic | Anatomy |
| [[argument-structure]] | reference | Anatomy |
| [[base-rate-neglect]] | atomic | Inductive |
| [[bayesian-reasoning]] | reference | Inductive |
| [[begging-the-question]] | atomic | Fallacies |
| [[burden-of-proof]] | atomic | Fallacies |
| [[categorical-syllogism]] | atomic | Deductive |
| [[circular-reasoning]] | atomic | Fallacies |
| [[cogent-argument]] | atomic | Inductive |
| [[conditional-reasoning]] | atomic | Deductive |
| [[contrapositive]] | atomic | Deductive |
| [[critical-thinking]] | reference | Frameworks |
| [[critical-thinking-dispositions-taxonomy]] | reference | Frameworks |
| [[delphi-report]] | reference | Frameworks |
| [[deductive-reasoning]] | reference | Deductive |
| [[enthymeme]] | atomic | Anatomy |
| [[equivocation-fallacy]] | atomic | Fallacies |
| [[epistemic-cowardice]] | atomic | Virtues |
| [[epistemic-closure]] | atomic | Virtues |
| [[fair-mindedness]] | atomic | Virtues |
| [[false-cause-fallacy]] | atomic | Fallacies |
| [[false-dichotomy]] | atomic | Fallacies |
| [[formal-logic]] | reference | Deductive |
| [[hasty-generalization]] | atomic | Fallacies |
| [[inductive-reasoning]] | reference | Inductive |
| [[inference-to-the-best-explanation]] | atomic | Abductive |
| [[informal-fallacy]] | reference | Fallacies |
| [[intellectual-courage]] | atomic | Virtues |
| [[intellectual-empathy]] | atomic | Virtues |
| [[intellectual-humility]] | atomic | Virtues |
| [[intellectual-integrity]] | atomic | Virtues |
| [[intellectual-standards]] | atomic | Frameworks |
| [[logical-fallacies]] | reference | Fallacies |
| [[modus-ponens]] | atomic | Deductive |
| [[modus-tollens]] | atomic | Deductive |
| [[modal-logic]] | atomic | Deductive |
| [[open-mindedness]] | atomic | Virtues |
| [[paul-elder-critical-thinking-framework]] | reference | Frameworks |
| [[paul-elder-framework]] | reference | Frameworks |
| [[predicate-logic]] | reference | Deductive |
| [[principle-of-charity]] | atomic | Anatomy |
| [[propositional-logic]] | reference | Deductive |
| [[red-herring-fallacy]] | atomic | Fallacies |
| [[slippery-slope-fallacy]] | atomic | Fallacies |
| [[sound-argument]] | atomic | Deductive |
| [[steelmanning]] | atomic | Anatomy |
| [[straw-man-fallacy]] | atomic | Fallacies |
| [[strong-argument]] | atomic | Inductive |
| [[toulmin-argument-model]] | reference | Anatomy |
| [[truth-seeking-disposition]] | atomic | Virtues |
| [[truth-tables]] | atomic | Deductive |
| [[valid-argument]] | atomic | Deductive |
| [[validity-vs-soundness]] | atomic | Deductive |
| [[watson-glaser-model]] | reference | Frameworks |

---

> [!info] MOC Metadata
> - **Pattern**: progressive
> - **Source notes**: 67
> - **Word count**: ~5,200
> - **Generated**: 2026-05-15 by MOC Specialist Agent v1.0.0
> - **Audit trail**: [[_meta/MOC - Critical Thinking and Logic.audit]]
> - **Next review suggested**: 2026-08-15


# Visual Aid Suite: Critical Thinking and Logic MOC

**Source:** MOC — Critical Thinking and Logic | ~5,200 words | 67 source notes
**Audience:** Practitioner + Researcher
**Thesis:** Critical thinking is a discipline requiring both formal reasoning skill — argument structure, logical systems, fallacy detection — and intellectual virtue (dispositional character); the two are jointly necessary and neither alone is sufficient.
**Aids selected:**

1. **Progressive Architecture Map** — the MOC's own five-level spine, from atom to foundation
2. **Argument Anatomy Diagram** — standard form + Toulmin extension, key distinctions
3. **Deductive Logic Taxonomy Tree** — formal systems hierarchy and canonical argument forms
4. **Three Reasoning Modes Comparison Matrix** — deductive / inductive / abductive side-by-side
5. **Fallacy Taxonomy Tree** — full classification with sub-branches and examples
6. **CT Frameworks Comparison Matrix** — Delphi-Facione vs Paul-Elder vs Watson-Glaser
7. **Intellectual Virtues Hub Map** — core virtues, their corruptions, and joint structure
8. **Skills × Virtues Joint Necessity Diagram** — the central normative claim of the MOC
9. **Before / After Contrast Panel** — naive reasoner vs skilled critical thinker
10. **TL;DR Scorecard** — synthesis capsule

---

## Visual Aid 1: Progressive Architecture Map

**Purpose:** Renders the MOC's own five-level structure so readers can orient before entering any section.

```
MOC STRUCTURE — PROGRESSIVE ARCHITECTURE
══════════════════════════════════════════════════════════════════

 ┌────────────────────────────────────────────────────┐
 │   LEVEL 1 — THE ATOM: Argument Anatomy             │ ← start
 │  Premise · Conclusion · Inference · Enthymeme      │
 │  Reconstruction · Principle of Charity · Toulmin   │
 └────────────────────────┬───────────────────────────┘
                          │  provides the raw material for
                          ▼
 ┌────────────────────────────────────────────────────┐
 │   LEVEL 2 — THE MOLECULE: Logical Systems          │
 │  DEDUCTIVE → Validity, Soundness, MP/MT/Syllogism  │
 │  INDUCTIVE → Strength, Cogency, Bayesian updating  │
 │  ABDUCTIVE → Inference to the Best Explanation     │
 └────────────────────────┬───────────────────────────┘
                          │  violations of these form
                          ▼
 ┌────────────────────────────────────────────────────┐
 │   LEVEL 3 — ERRORS: Fallacy Taxonomy               │
 │  Formal  → structural violations of valid form     │
 │  Informal → Relevance / Inductive / Presumption    │
 └────────────────────────┬───────────────────────────┘
                          │  systematised into
                          ▼
 ┌────────────────────────────────────────────────────┐
 │   LEVEL 4 — APPLICATION: CT Frameworks             │
 │  Delphi / Facione · Paul-Elder · Watson-Glaser     │
 │  Elements of Thought · Intellectual Standards      │
 └────────────────────────┬───────────────────────────┘
                          │  sustained and motivated by
                          ▼
 ┌────────────────────────────────────────────────────┐
 │   LEVEL 5 — FOUNDATION: Intellectual Virtues       │
 │  Humility · Courage · Empathy · Integrity          │
 │  Open-Mindedness · Fairness · Truth-Seeking        │
 └────────────────────────────────────────────────────┘

 Arrow direction = "required for" / "makes possible"
 Each level presupposes, but does not reduce to, the one below.
```

**Reading guide:** Read top-to-bottom to follow the MOC's own learning sequence. An arrow does not mean later levels are "more important" — Level 5 (virtues) is the *foundation*, not the capstone. The structure is progressive: you cannot reliably identify fallacies (Level 3) without understanding valid argument forms (Level 2). The entire edifice rests on dispositional character (Level 5) that motivates applying the skills at all.

**Source:** § Navigation, § Abstract

---

## Visual Aid 2: Argument Anatomy Diagram

**Purpose:** Maps the structural components of any argument — standard form and Toulmin's extended schema — and marks the critical inference/implication distinction.

```
ARGUMENT ANATOMY
══════════════════════════════════════════════════════════════════

  STANDARD FORM                    TOULMIN EXTENSION
  ────────────────                 ──────────────────────────────
  ┌───────────────┐                ┌────────────────────────────┐
  │  PREMISE(S)   │                │  GROUNDS (the data)        │
  │  P1, P2...    │                └─────────────┬──────────────┘
  └──────┬────────┘                              │
         │  grounds                              ▼
  ┌──────▼────────┐   authorised   ┌────────────────────────────┐
  │   INFERENCE   │◄───────────────│  WARRANT                   │
  │  (the move)   │   by           │  (principle licensing move)│
  └──────┬────────┘                └─────────────┬──────────────┘
         │                                       │  supported by
  ┌──────▼────────┐                ┌─────────────▼──────────────┐
  │  CONCLUSION   │                │  BACKING                   │
  └───────────────┘                └────────────────────────────┘
                                          PLUS:
  RECONSTRUCTION SEQUENCE:        ┌────────────────────────────┐
  ┌───────────────────────────┐   │ QUALIFIER (modal hedge)    │
  │ Natural language argument  │  │ "probably" · "usually"     │
  │          ↓                 │  └────────────────────────────┘
  │ Standard form rendering    │  ┌────────────────────────────┐
  │  (suppressed premises      │  │ REBUTTAL (stated exceptions│
  │   made explicit)           │  │  to the warrant)          │
  │          ↓                 │  └────────────────────────────┘
  │ Strongest plausible version│
  │  [STEELMANNING]            │   ← highest form of charity
  └───────────────────────────┘

  CRITICAL DISTINCTION — OFTEN CONFUSED:
  ┌────────────────────────────────────────────────────────┐
  │ INFERENCE = act of a reasoner drawing a conclusion     │
  │ IMPLICATION = semantic relation between propositions   │
  │                                                        │
  │ Not everything A implies, the speaker has INFERRED.   │
  │ Conflating them → systematic argumentative error.      │
  └────────────────────────────────────────────────────────┘

  Vault: [[Argument-Analysis]] [[Inference]] [[Modus-Ponens]]
```

**Reading guide:** The left column shows the minimal structure of any argument; the right column shows Toulmin's richer schema, designed for natural language domains (law, policy, everyday reasoning) where formal validity is not the right standard. The reconstruction sequence at bottom-left is a *procedure*: start with charitable interpretation of natural language and render the strongest plausible version before evaluating. The inference/implication box marks one of the most practically important distinctions in informal logic.

**Source:** § Argument Anatomy

---

## Visual Aid 3: Deductive Logic Taxonomy Tree

**Purpose:** Organises formal logic systems hierarchically and displays the canonical valid argument forms alongside their two most common invalid impostors.

```
DEDUCTIVE LOGIC — SYSTEMS AND FORMS
══════════════════════════════════════════════════════════════════

FORMAL LOGIC (symbolic, explicit syntax + semantics)
│
├── PROPOSITIONAL LOGIC (sentential)
│   ├── Units: atomic propositions
│   ├── Connectives: AND · OR · NOT · IF-THEN · IFF
│   ├── Tool: Truth tables (exhaustive validity check)
│   └── Key concept: Logical form (content-independent)
│
├── PREDICATE LOGIC — First-Order Logic (FOL)
│   ├── Extends propositional with: subject + predicate
│   ├── Quantifiers: ∀ (all) · ∃ (some) · ¬∃ (none)
│   └── Captures: syllogistic forms + much more complex
│
└── MODAL LOGIC
    ├── Adds: □ (necessarily) · ◇ (possibly)
    └── Applications: metaphysics · epistemic logic

──────────────────────────────────────────────────────────────────
CANONICAL VALID ARGUMENT FORMS
──────────────────────────────────────────────────────────────────
  Modus Ponens (MP)          Modus Tollens (MT)
  ┌──────────────────┐       ┌──────────────────┐
  │ If P, then Q     │       │ If P, then Q     │
  │ P                │       │ Not-Q            │
  │ ──────────────   │       │ ──────────────   │
  │ ∴ Q              │       │ ∴ Not-P          │
  └──────────────────┘       └──────────────────┘

  Categorical Syllogism      Contrapositive
  ┌──────────────────┐       ┌──────────────────┐
  │ All M are P      │       │ If P → Q         │
  │ All S are M      │       │ Equiv: ¬Q → ¬P   │
  │ ──────────────   │       │ (same truth value │
  │ ∴ All S are P    │       │  as original)     │
  └──────────────────┘       └──────────────────┘

──────────────────────────────────────────────────────────────────
COMMON INVALID IMPOSTORS  (appear valid — are NOT)
──────────────────────────────────────────────────────────────────
  Affirming Consequent  ✗    Denying Antecedent    ✗
  ┌──────────────────┐       ┌──────────────────┐
  │ If P, then Q     │       │ If P, then Q     │
  │ Q                │       │ Not-P            │
  │ ──────────────   │       │ ──────────────   │
  │ ∴ P ???          │       │ ∴ Not-Q ???      │
  └──────────────────┘       └──────────────────┘
  Both errors are Type 1 processing defaults —
  resist correction by simple instruction alone.

  KEY: VALID = form guarantees conclusion given true premises
       SOUND = valid + premises actually true

  Vault: [[Deductive-Reasoning]] [[Validity]] [[Soundness]]
         [[Modus-Ponens]] [[Modus-Tollens]] [[Categorical-Syllogism]]
```

**Reading guide:** The hierarchy runs from simpler (propositional) to more expressive (predicate, modal) systems. The four valid forms are the workhorses of formal deductive reasoning; knowing them by structure makes formal fallacy detection automatic — you just check whether the argument matches a valid pattern. The two invalid impostors at bottom are among the most common reasoning errors documented in the cognitive psychology literature; recognising them as structural failures, not content problems, is the key insight.

**Source:** § Deductive Logic

---

## Visual Aid 4: Three Reasoning Modes Comparison Matrix

**Purpose:** Displays deductive, inductive, and abductive reasoning side-by-side across the dimensions that matter for evaluation, enabling principled selection of the right standard for any argument.

```
THREE REASONING MODES — COMPARISON MATRIX
══════════════════════════════════════════════════════════════════

┌───────────────────┬──────────────┬──────────────┬─────────────┐
│   DIMENSION       │  DEDUCTIVE   │  INDUCTIVE   │  ABDUCTIVE  │
├───────────────────┼──────────────┼──────────────┼─────────────┤
│ Logical           │ Necessary    │ Probable     │ Plausible   │
│ relationship      │ (entailment) │ (support)    │ (explains)  │
├───────────────────┼──────────────┼──────────────┼─────────────┤
│ Direction of      │ General →    │ Particular → │ Effect →    │
│ inference         │ Particular   │ General      │ Best cause  │
├───────────────────┼──────────────┼──────────────┼─────────────┤
│ Primary quality   │ Valid /      │ Strong /     │ Best / Worse│
│ standard          │ Invalid      │ Weak         │ explanation │
├───────────────────┼──────────────┼──────────────┼─────────────┤
│ Best-case name    │ Sound        │ Cogent       │ IBE         │
│                   │ (valid+true) │ (strong+true)│ (simplicity │
│                   │              │              │  + scope)   │
├───────────────────┼──────────────┼──────────────┼─────────────┤
│ Truth-            │ YES          │ NO           │ NO          │
│ preserving?       │ (guarantees) │ (probable)   │ (fallible)  │
├───────────────────┼──────────────┼──────────────┼─────────────┤
│ Representative    │ MP, MT,      │ Enumeration, │ Scientific  │
│ examples          │ Categorical  │ Analogy,     │ discovery,  │
│                   │ Syllogism    │ Bayesian     │ Diagnosis   │
├───────────────────┼──────────────┼──────────────┼─────────────┤
│ Primary           │ Formal       │ Base-rate    │ Ad hoc      │
│ failure mode      │ fallacies    │ neglect;     │ supplementa-│
│                   │ (structural) │ Hasty gen.   │ tion        │
├───────────────────┼──────────────┼──────────────┼─────────────┤
│ Advances          │ Tests        │ Builds       │ Generates   │
│ knowledge by      │ entailments  │ generalisns  │ hypotheses  │
├───────────────────┼──────────────┼──────────────┼─────────────┤
│ Normative         │ Classical    │ Bayesian     │ Explanatory │
│ framework         │ logic        │ probability  │ criteria    │
└───────────────────┴──────────────┴──────────────┴─────────────┘

  IBE criteria: simplicity · scope · fit with background
                knowledge · absence of ad hoc additions

  NOTE: Most real-world reasoning is inductive/abductive.
  Demanding deductive standards where they don't apply
  is itself a reasoning error.

  Vault: [[Deductive-Reasoning]] [[Inductive-Reasoning]]
         [[Abductive-Reasoning]] [[Bayesian-Reasoning]]
         [[Analogical-Reasoning]]
```

**Reading guide:** Work across each row to see how the same dimension plays out differently for each reasoning type. The most practically important rows are "quality standard" (what to evaluate) and "primary failure mode" (what to watch for). A common error is importing deductive standards into inductive contexts — demanding certainty where only probability is possible. The bottom row clarifies that all three are genuinely knowledge-advancing; they are complementary, not competing.

**Source:** §§ Deductive Logic, Inductive and Abductive Reasoning

---

## Visual Aid 5: Fallacy Taxonomy Tree

**Purpose:** Provides a complete, hierarchically organised classification of formal and informal fallacies, enabling systematic error identification in any argument.

```
FALLACY TAXONOMY — COMPLETE CLASSIFICATION
══════════════════════════════════════════════════════════════════

FALLACIES
(arguments that appear valid or persuasive but are not)
│
├── FORMAL FALLACIES  (errors in logical structure)
│   Error in form regardless of content — caught by
│   checking whether the argument matches a valid form.
│   │
│   ├── Affirming the Consequent   [P→Q, Q ∴ P]  ✗
│   ├── Denying the Antecedent     [P→Q, ¬P ∴ ¬Q] ✗
│   └── Circular Reasoning / Begging the Question
│       └── Conclusion smuggled back in as premise
│           → trivially "valid" but epistemically empty
│           (generates zero independent support)
│
└── INFORMAL FALLACIES  (errors in content or context)
    │
    ├── RELEVANCE FALLACIES
    │   (premise offered is not genuinely relevant
    │    to the conclusion)
    │   ├── Ad Hominem       attack arguer, not argument
    │   ├── Appeal to Auth.  authority lacks relevant expertise
    │   ├── Appeal to Emotion manipulation replaces evidence
    │   ├── Red Herring      irrelevant material to distract
    │   └── Straw Man        misrepresent to defeat weaker version
    │
    ├── INDUCTIVE / GENERALISATION ERRORS
    │   (fail inductive reasoning standards)
    │   ├── Hasty Generalisation  sample too small/unrepresentative
    │   ├── False Cause           correlation ≠ causation
    │   ├── Slippery Slope        step 1 → extreme end, no mechanism
    │   ├── False Dichotomy       only 2 options presented; more exist
    │   └── Appeal to Nature      natural = good / true / better
    │
    └── PRESUMPTION FALLACIES
        (hidden or unwarranted assumptions)
        ├── Equivocation     word shifts meaning mid-argument
        ├── Appeal to Ign.   absence of proof ≠ proof of absence*
        ├── Genetic Fallacy  origin of claim decides its truth
        └── No True Scotsman redefine category to exclude examples

    *EXCEPTION: absence of evidence IS evidence if the evidence
     SHOULD have appeared had the claim been true.

══════════════════════════════════════════════════════════════════
  BRIDGE NOTE:
  Fallacy taxonomy (logical-normative) ↔ Cognitive bias research
  (cognitive-psychological) describe the same phenomenon at
  different levels of analysis. See:
  [[MOC - Dual Process Theory and Cognitive Biases]]

  Vault: [[Informal-Fallacies]] [[Confirmation-Bias]]
         [[Straw-Man]] [[Dual-Process-Theory]]
```

**Reading guide:** Read the tree top-down: formal fallacies are caught structurally; informal fallacies require contextual judgment about relevance, inductive standards, or hidden assumptions. The three informal sub-categories map onto the three ways an argument can fail without formal invalidity: saying something irrelevant (relevance), generalising badly (inductive), or hiding an assumption (presumption). The footnote on "absence of evidence" is important: Appeal to Ignorance is not always a fallacy — it depends on whether the absent evidence would have appeared if the claim were true.

**Source:** § The Fallacy Taxonomy

---

## Visual Aid 6: CT Frameworks Comparison Matrix

**Purpose:** Places the three dominant critical thinking frameworks side-by-side so readers can select the right model for their pedagogical or assessment context.

```
CRITICAL THINKING FRAMEWORKS — COMPARISON
══════════════════════════════════════════════════════════════════

┌─────────────────┬──────────────┬──────────────┬───────────────┐
│   DIMENSION     │DELPHI/FACIONE│  PAUL-ELDER  │ WATSON-GLASER │
├─────────────────┼──────────────┼──────────────┼───────────────┤
│ Origin          │ 1990 Delphi  │ Paul (1980s) │ Watson &      │
│                 │ APA consensus│ Elder (1990s)│ Glaser 1964+  │
├─────────────────┼──────────────┼──────────────┼───────────────┤
│ Core definition │ Purposeful,  │ Disciplined, │ Composite of  │
│                 │ self-regul.  │ self-directed│ 5 measurable  │
│                 │ judgment     │ thinking     │ sub-skills    │
├─────────────────┼──────────────┼──────────────┼───────────────┤
│ Cognitive       │ Interpretn   │ Purpose ·    │ Inference ·   │
│ components      │ Analysis ·   │ Question ·   │ Assumptions · │
│                 │ Evaluation · │ Information ·│ Deduction ·   │
│                 │ Inference ·  │ Concepts ·   │ Interpretation│
│                 │ Explanation  │ Interpretn · │ Evaluation    │
│                 │              │ Assumptions ·│               │
│                 │              │ Implications ·│              │
│                 │              │ Point of view│               │
├─────────────────┼──────────────┼──────────────┼───────────────┤
│ Standards       │ Evaluative   │ Clarity ·    │ Not explicit  │
│ applied         │ criteria     │ Accuracy ·   │ (psychometric │
│                 │ framework    │ Precision ·  │  standard)    │
│                 │              │ Relevance ·  │               │
│                 │              │ Depth · Logic│               │
│                 │              │ Breadth ·    │               │
│                 │              │ Fairness     │               │
├─────────────────┼──────────────┼──────────────┼───────────────┤
│ Dispositional   │ EXPLICIT:    │ Intellectual │ LIMITED:      │
│ dimension       │ Dispositions │ virtues as   │ implied;      │
│                 │ taxonomy     │ integral     │ not taxonomised│
├─────────────────┼──────────────┼──────────────┼───────────────┤
│ Domain stance   │ Partially    │ NOT separable│ Domain-       │
│                 │ domain-gen.  │ from subject │ general test  │
│                 │              │ matter       │               │
├─────────────────┼──────────────┼──────────────┼───────────────┤
│ Primary         │ Research +   │ Education +  │ Selection +   │
│ application     │ dispositions │ pedagogy     │ assessment    │
│                 │ measurement  │              │               │
├─────────────────┼──────────────┼──────────────┼───────────────┤
│ Assessment      │ CCTDI /      │ Rubric-based │ Watson-Glaser │
│ instrument      │ CCTST        │ standards    │ Appraisal     │
└─────────────────┴──────────────┴──────────────┴───────────────┘

  KEY DIFFERENTIATOR: Paul-Elder insists CT cannot be practised
  "in general" — you must think critically WITHIN a domain,
  using that domain's standards and concepts.
  Others permit more domain-general frameworks.

  Vault: [[Delphi-Report]] [[Paul-Elder-Critical-Thinking-Framework]]
         [[Paul-Elder-Framework]] [[Watson-Glaser-Critical-Thinking-Appraisal]]
         [[Intellectual-Standards]]
```

**Reading guide:** The matrix rows progress from framework origins to practical deployment. The most decision-relevant rows are "domain stance" (determines whether the framework works across subjects or requires domain specialisation) and "primary application" (research, pedagogy, or selection). Paul-Elder's domain-dependence claim is not widely shared and is itself a point of theoretical debate. For pure assessment and selection contexts, Watson-Glaser's psychometric precision makes it the dominant choice despite its thin dispositional treatment.

**Source:** § Critical Thinking Frameworks

---

## Visual Aid 7: Intellectual Virtues Hub Map

**Purpose:** Displays the seven core intellectual virtues, their functional definitions, and — critically — their characteristic corruptions, which are the failure modes of each virtue.

```
INTELLECTUAL VIRTUES — CORE DISPOSITIONS AND CORRUPTIONS
══════════════════════════════════════════════════════════════════

                   ┌────────────────────────┐
                   │   INTELLECTUAL         │
                   │      VIRTUES           │
                   │  (character dimension  │
                   │   of critical thinking)│
                   └──────────┬─────────────┘
      ┌────────────┬──────────┼──────────┬────────────┐
      ▼            ▼          ▼          ▼            ▼
 HUMILITY      COURAGE    EMPATHY   INTEGRITY    OPENNESS
 ─────────     ───────    ───────   ─────────    ────────
 Accurate      Follow     Genuine   Apply same   Genuine
 awareness     reasoning  inside-   standards    consider-
 of own        to uncom-  view of   to own       ation of
 cognitive     fortable   opposing  claims as    alternatives
 limits        conclusions positions to others'
      │              │         │          │           │
  ✗ CORRUPT:    ✗ CORRUPT: ✗ CORRUPT: ✗ CORRUPT: ✗ CORRUPT:
  Overconfid-  Epistemic  Dismissal  Motivated  Epistemic
  ence +       Cowardice  of other   reasoning  closure
  Dunning-     (vague     side;      (double    (filter
  Kruger       answers to straw-     standards) bubble)
  blindspot    avoid      manning
               conflict)

  ┌──────────────────────────────────────────────────────┐
  │  FAIR-MINDEDNESS                                     │
  │  Apply epistemic standards consistently regardless   │
  │  of viewpoint — not just when it supports own side   │
  │  ✗ Corruption: Selective scepticism                  │
  └──────────────────────────────────────────────────────┘

  ┌──────────────────────────────────────────────────────┐
  │  TRUTH-SEEKING                                       │
  │  Valuing accuracy and evidence over personal comfort │
  │  or social approval                                  │
  │  ✗ Corruption: Epistemic cowardice — deliberately    │
  │    vague answers to avoid controversy                │
  └──────────────────────────────────────────────────────┘

  DEVELOPMENTAL NOTE:
  Virtues and skills are JOINTLY necessary (see Aid 8).
  High skill + low virtue → sophisticated rationalisation.
  High virtue + low skill → good intentions, poor execution.

  Vault: [[Intellectual-Humility]] [[Intellectual-Courage]]
         [[Intellectual-Empathy]] [[Intellectual-Integrity]]
         [[Epistemic-Cowardice]] [[Intellectual-Virtues]]
```

**Reading guide:** Each virtue should be read vertically: the virtue name at top, its functional definition in the middle, and its characteristic corruption below. The corruption is not the mere absence of the virtue — it is an active failure mode that can mimic the virtue superficially. The two boxed virtues at bottom (fair-mindedness and truth-seeking) span all the others and act as integrating dispositions. The developmental note links directly to Aid 8.

**Source:** § Intellectual Virtues and Dispositions

---

## Visual Aid 8: Skills × Virtues Joint Necessity Diagram

**Purpose:** Renders the MOC's central normative claim — that CT skills and CT virtues are jointly necessary, neither alone sufficient — as a 2×2 with populated cells.

```
SKILLS × VIRTUES — JOINT NECESSITY OF CRITICAL THINKING
══════════════════════════════════════════════════════════════════

                          CT VIRTUES
                   LOW ◄───────────────► HIGH
                   │                        │
              ┌────┴──────────┬─────────────┴──────┐
         HIGH │ ✗ DANGEROUS   │ ✓ GENUINE CT        │
              │ RATIONALISER  │   PRACTITIONER      │
              │               │                     │
 CT           │ Skills select-│ Skills applied      │
 SKILLS       │ ively deployed│ fairly + rigorously │
              │ to support    │ Self-correction     │
              │ pre-existing  │ operative           │
              │ conclusions   │ Follows evidence    │
              │               │ wherever it leads   │
              │ Confirmation  │ Steelmans opponents │
              │ bias as        │ before critiquing  │
              │ motivated      │                    │
              │ reasoning      │                    │
              ├───────────────┼────────────────────┤
         LOW  │ ✗ UNREFLECTIVE│ ✗ WELL-INTENTIONED  │
              │   OPINION-    │   BUT INEFFECTIVE   │
              │   HOLDER      │                     │
              │               │ Good intentions;    │
              │ Neither skill │ cannot identify     │
              │ nor character │ fallacies in        │
              │ operative     │ practice            │
              │               │ Cannot act on       │
              │               │ epistemic commitments│
              └───────────────┴─────────────────────┘

  ╔═════════════════════════════════════════════════════╗
  ║  KEY CLAIM: A highly skilled reasoner who lacks     ║
  ║  intellectual courage will deploy skills to support ║
  ║  conclusions they already hold.                     ║
  ║  This produces SOPHISTICATED MOTIVATED REASONING —  ║
  ║  more dangerous than ordinary bias, because it is  ║
  ║  better at defending itself.                        ║
  ╚═════════════════════════════════════════════════════╝

  Target quadrant: HIGH skills + HIGH virtues (top-right)
  Most dangerous: HIGH skills + LOW virtues (top-left)

  Vault: [[Critical-Thinking]] [[Intellectual-Virtues]]
         [[Motivated-Reasoning]] [[Confirmation-Bias]]
```

**Reading guide:** This is the MOC's most important normative diagram. Read the top-left cell carefully — the high-skill / low-virtue quadrant is the most practically dangerous outcome of CT training that neglects character. Skills provide *power* to reason; virtues determine *whether that power is used honestly*. The bottom-left quadrant is simply uninformed; the bottom-right is earnest but limited. Only the top-right represents genuine critical thinking as defined by the Delphi consensus and the Paul-Elder framework.

**Source:** § Intellectual Virtues and Dispositions — callout "Virtues and Skills Are Jointly Necessary"

---

## Visual Aid 9: Before / After Contrast Panel

**Purpose:** Shows the concrete behavioural difference between a naive reasoner and a CT-trained reasoner across all five domains of the MOC.

```
REASONING QUALITY — BEFORE AND AFTER CT DEVELOPMENT
══════════════════════════════════════════════════════════════════

┌──────────── BEFORE CT ─────────────┬─────────── AFTER CT ───────────────┐
│                                    │                                    │
│ ARGUMENT ANATOMY                   │ ARGUMENT ANATOMY                   │
│ • Takes natural language at        │ • Reconstructs in standard form    │
│   face value                       │ • Renders enthymemes explicit      │
│ • Misses suppressed premises       │ • Steelmans before evaluating      │
│ • Attacks weakest interpretation   │ • Applies principle of charity     │
│                                    │                                    │
│ LOGICAL EVALUATION                 │ LOGICAL EVALUATION                 │
│ • Accepts valid-seeming arguments  │ • Checks form → validity           │
│ • Doesn't distinguish valid        │ • Checks premises → soundness      │
│   from sound                       │ • Detects affirming consequent,    │
│ • Persuaded by content, not form   │   denying antecedent               │
│                                    │                                    │
│ INDUCTIVE / ABDUCTIVE              │ INDUCTIVE / ABDUCTIVE              │
│ • Ignores prior probabilities      │ • Bayesian updating from priors    │
│ • Mistakes correlation for cause   │ • Evaluates inductive strength     │
│ • Accepts first plausible          │ • Compares competing explanations  │
│   explanation                      │   against IBE criteria             │
│                                    │                                    │
│ FALLACY DETECTION                  │ FALLACY DETECTION                  │
│ • Susceptible to rhetoric          │ • Identifies ad hominem,           │
│ • Persuaded by vivid anecdotes     │   straw man, red herring           │
│ • Misled by authority signals      │ • Recognises hasty generalisation  │
│ • Cannot name the error            │ • Spots equivocation mid-argument  │
│                                    │                                    │
│ DISPOSITIONAL                      │ DISPOSITIONAL                      │
│ • Motivated reasoning dominant     │ • Applies identical standards to   │
│ • Avoids uncomfortable conclusions │   self and others (integrity)      │
│ • Closes off alternative views     │ • Follows reasoning to conclusions │
│ • Vagueness to avoid conflict      │   even when uncomfortable          │
│                                    │ • Genuinely entertains alternatives│
└────────────────────────────────────┴────────────────────────────────────┘

  Note: "After" describes a skilled AND virtuous reasoner.
  Skills alone produce the top-left quadrant of Aid 8.

  Vault: [[Critical-Thinking]] [[Intellectual-Standards]]
         [[Paul-Elder-Framework]] [[Deductive-Reasoning]]
         [[Informal-Fallacies]]
```

**Reading guide:** Read row by row, left-to-right, to see the specific behavioural transformation for each reasoning domain. The disposition row at the bottom is where most CT training programs underinvest — the "before" column behaviours persist even after formal logic training if dispositional work is absent. This panel can function as a self-assessment tool: honest identification of one's current column in each row reveals the most productive development target.

**Source:** All sections

---

## Visual Aid 10: TL;DR Scorecard

**Purpose:** One-page synthesis capsule capturing thesis, key takeaways, open questions, and a reader-fit guide.

```
╔══════════════════════════════════════════════════════════════╗
║     SCORECARD — CRITICAL THINKING AND LOGIC MOC             ║
╠══════════════════════════════════════════════════════════════╣
║ THESIS      CT requires BOTH formal reasoning skill         ║
║             (argument anatomy, logic, fallacy detection,    ║
║             CT frameworks) AND intellectual virtue          ║
║             (dispositional character). Neither alone        ║
║             is sufficient; their joint absence is mere      ║
║             opinion-holding, but skill without virtue is    ║
║             the most dangerous failure mode of all.         ║
╠══════════════════════════════════════════════════════════════╣
║ ARCHITECTURE  5 levels: Atom → Molecule → Error →          ║
║               Application → Foundation (progressive)        ║
╠══════════════════════════════════════════════════════════════╣
║ TOP 5       1. Steelman first: defeat the STRONGEST         ║
║ TAKEAWAYS     version of an argument, not the easiest       ║
║             2. Valid ≠ sound: check premises, not just form ║
║             3. Most real-world reasoning is inductive or    ║
║               abductive — apply the right standard         ║
║             4. High skill + low virtue = sophisticated      ║
║               rationalisation (the most dangerous quad.)   ║
║             5. Audit your virtues, not just your skills:    ║
║               epistemic cowardice is corruption of truth-   ║
║               seeking, not mere absence of courage         ║
╠══════════════════════════════════════════════════════════════╣
║ OPEN        • Transfer: domain-general or domain-specific? ║
║ QUESTIONS   • Measurement: conflation of CT + IQ + domain  ║
║               knowledge in existing instruments            ║
║             • Dispositions ↔ Skills: causal direction?     ║
╠══════════════════════════════════════════════════════════════╣
║ READ IF     Building argument analysis literacy, teaching  ║
║ YOU...      CT, building a logic / epistemology PKB layer, ║
║             or seeking dispositional audit of own reasoning ║
╠══════════════════════════════════════════════════════════════╣
║ COMPANION   [[MOC - Epistemology]] (virtues → epistemic     ║
║ MOCs        virtues); [[MOC - Dual Process Theory and       ║
║             Cognitive Biases]] (fallacies ↔ bias research) ║
╚══════════════════════════════════════════════════════════════╝
```

**Reading guide:** The scorecard is designed for rapid recall and PKB navigation. Each cell is independently usable: the thesis cell for orientation, the five takeaways for active recall practice, the open questions for research gaps, and the reader-fit cells for deciding which collaborators to route to this MOC. The companion MOC pointers close the PKB loop.

**Source:** All sections

---

## Synthesis Packet

### Top 5 Takeaways

1. **Argument anatomy is prerequisite infrastructure.** Every reasoning skill downstream — valid form detection, fallacy identification, inductive evaluation — depends on being able to identify premises, conclusions, and the inferential move between them in natural language. Charitable reconstruction and steelmanning are not politeness; they are epistemic necessities.

2. **The valid/sound distinction is the most practically underused tool in logic.** Most informal reasoning errors involve accepting valid-seeming arguments without checking whether the premises are actually true. Teaching formal validity without teaching soundness produces only half the needed skill.

3. **Fallacy categories reveal *why* an argument fails, not just *that* it fails.** The formal/informal taxonomy enables diagnostic precision: a relevance fallacy fails differently than a presumption fallacy and requires a different corrective response.

4. **The skill × virtue joint necessity is the MOC's normative core.** High reasoning skill without intellectual virtue produces motivated reasoning of the most sophisticated kind. CT development that neglects character builds dangerous rationalisers, not critical thinkers.

5. **Open questions are genuinely open.** The transfer problem (domain-general vs domain-specific CT) is unresolved and has direct instructional implications. Practitioners should treat single-domain CT training with appropriate caution about generalisation.

### Navigator — Which Aid Answers Which Question

| Question | Aid |
|---|---|
| "How is this MOC structured?" | Aid 1 — Progressive Architecture |
| "What is an argument, precisely?" | Aid 2 — Argument Anatomy |
| "What are the valid deductive forms?" | Aid 3 — Deductive Logic Taxonomy |
| "How do deductive/inductive/abductive differ?" | Aid 4 — Three Reasoning Modes Matrix |
| "What type of fallacy is this?" | Aid 5 — Fallacy Taxonomy Tree |
| "Which CT framework should I use?" | Aid 6 — Frameworks Comparison |
| "What are the core intellectual virtues?" | Aid 7 — Virtues Hub Map |
| "Why aren't skills enough?" | Aid 8 — Skills × Virtues Diagram |
| "What does CT development look like in practice?" | Aid 9 — Before/After Panel |
| "Give me the whole MOC in one view." | Aid 10 — Scorecard |