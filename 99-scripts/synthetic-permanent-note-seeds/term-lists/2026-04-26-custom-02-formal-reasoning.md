---
batch_name: custom-02-formal-reasoning
batch_date: 2026-04-26
default_domain: logic
default_confidence: high
notes: |
  Custom seeding batch 02: core formal-reasoning patterns. Companion to the
  logical-fallacies batch; supplies the positive inferential primitives.
---

# Batch: Formal Reasoning

## Argument from Analogy

- domain: logic
- secondary_domains: [critical-thinking, reasoning]
- aliases: [analogical argument]
- broader: [inductive-reasoning, analogical-reasoning]
- related: [analogical-mapping, abductive-reasoning, modus-ponens]
- prerequisites: [argument-analysis]
- confidence: high

**definition**: An Argument from Analogy is an inductive inference in which similarities between two cases on a set of relevant features are used as grounds for concluding that they share an additional feature, with the strength of the argument depending on the number, relevance, and asymmetry of the shared properties.

**key_claim**: An Argument from Analogy is evaluated by the relevance of the mapped features rather than their count, so adding many superficial similarities does not strengthen an analogy whose core mapping fails on the property doing the explanatory work.

**warning**: An Argument from Analogy can degenerate into a "false analogy" when the source and target differ in a feature that is causally responsible for the property in dispute; spotting this disanalogy is the standard rebuttal move and is more diagnostic than counting matched features.

## Modus Ponens

- domain: logic
- secondary_domains: [propositional-logic, deductive-reasoning]
- aliases: [affirming the antecedent]
- broader: [deductive-inference]
- related: [modus-tollens, circular-reasoning, argument-analysis]
- prerequisites: [propositional-logic]
- confidence: high

**definition**: Modus Ponens is the deductively valid inference rule licensing the conclusion "Q" from the premises "If P then Q" and "P", and is one of the two foundational rules — together with Modus Tollens — for classical propositional reasoning.

**key_claim**: Modus Ponens is so central that classical logic is sometimes characterized as the discipline of preserving truth under repeated application of Modus Ponens; rejecting Modus Ponens is tantamount to rejecting the standard interpretation of the conditional itself.

**warning**: Modus Ponens is reliable only when the conditional premise is genuinely material, so apparent counter-examples typically arise from conversational conditionals (subjunctive, indicative-with-presupposition) where the conditional's truth conditions are not the classical material conditional Modus Ponens assumes.

## Modus Tollens

- domain: logic
- secondary_domains: [propositional-logic, deductive-reasoning]
- aliases: [denying the consequent]
- broader: [deductive-inference]
- related: [modus-ponens, falsification, scientific-reasoning]
- prerequisites: [propositional-logic]
- confidence: high

**definition**: Modus Tollens is the deductively valid inference rule licensing the conclusion "not P" from the premises "If P then Q" and "not Q", capturing the formal structure of falsification: a hypothesis that entails a prediction is overturned when the prediction fails.

**key_claim**: Modus Tollens is the formal backbone of Karl Popper's falsificationist account of science; an entire methodology of empirical inquiry is built on the asymmetry between confirming and disconfirming a hypothesis that Modus Tollens encodes at the propositional level.

**warning**: Modus Tollens applied to a complex theoretical claim rarely refutes a single proposition; the Duhem-Quine thesis observes that empirical disconfirmation can always be redirected to an auxiliary assumption, so the practical force of Modus Tollens depends on the holism of what gets falsified.

## Statistical Syllogism

- domain: logic
- secondary_domains: [inductive-reasoning, probability, critical-thinking]
- aliases: [direct inference, proportional syllogism]
- broader: [inductive-inference]
- related: [base-rate-neglect, argument-from-analogy, probability-judgment]
- prerequisites: [probability, argument-analysis]
- confidence: high

**definition**: A Statistical Syllogism is an inductive inference of the form "Most F are G; this is an F; therefore probably this is G," extending categorical syllogism to cases where the major premise is a statistical regularity rather than a universal generalization.

**key_claim**: A Statistical Syllogism inherits its rational force from the reference class chosen, so the same individual can be assigned different probabilities depending on which reference class is invoked, a feature known as the "reference-class problem" that resists fully principled solution.

**warning**: A Statistical Syllogism can lead to fallacious conclusions when the chosen reference class is too broad or too narrow relative to the question; ignoring more specific information that is available constitutes the inferential vice the bias literature calls base-rate misuse.
