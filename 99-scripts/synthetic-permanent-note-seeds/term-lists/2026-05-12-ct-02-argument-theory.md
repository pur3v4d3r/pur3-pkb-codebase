---
batch_name: ct-02-argument-theory
batch_date: 2026-05-12
default_domain: critical-thinking
default_confidence: high
notes: |
  Fifteen concepts from argument theory and the structural analysis of reasoning.
  Covers the argument-evaluation vocabulary, syllogistic forms, defeasible
  reasoning, and dialectical practices such as steelmanning and burden of proof.
---

## Argument Structure

- secondary_domains: [logic, rhetoric]
- aliases: [structure of an argument]
- broader: [argumentation theory]
- narrower: [premise, conclusion, inference]
- related: [argument mapping, argument reconstruction, logical form]

**definition**: Argument Structure is the organisation of a piece of reasoning into premises, intermediate inferences, and a final conclusion, together with the relations of support that connect them.

**key_claim**: Argument Structure is the substrate that argument evaluation operates on; one cannot judge whether an argument is good until the structure has been recovered, because validity, soundness, and cogency are all properties of structured inferential moves.

**warning**: Argument Structure is often confused with rhetorical order; the structure is logical rather than presentational, so a conclusion stated first or premises buried in subordinate clauses still produce the same underlying structure once it is reconstructed.

## Valid Argument

- secondary_domains: [logic, formal-logic]
- aliases: [deductively valid argument]
- broader: [deductive arguments]
- related: [sound argument, validity vs soundness, logical form]
- prerequisites: [logical consequence]

**definition**: A Valid Argument is a deductive argument whose conclusion cannot be false when its premises are all true; validity is a structural property of the inference, not a function of the actual truth of the premises.

**key_claim**: A Valid Argument can have false premises and a false conclusion; what validity guarantees is the truth-preserving relation, which is why "valid" and "true" must be kept categorically separate when evaluating reasoning.

**warning**: A Valid Argument is routinely misdescribed as one that is "convincing" or "well-supported"; the technical sense concerns truth-preservation only, and persuasive force is neither necessary nor sufficient for validity.

## Sound Argument

- secondary_domains: [logic, formal-logic]
- aliases: [sound deductive argument]
- broader: [deductive arguments]
- related: [valid argument, validity vs soundness, premise acceptability]

**definition**: A Sound Argument is a valid deductive argument whose premises are also actually true; soundness combines structural validity with material truth and is therefore the gold standard for deductive reasoning.

**key_claim**: A Sound Argument guarantees the truth of its conclusion, which makes soundness the only argument property that fully transmits truth from premises to conclusion; everything weaker leaves room for the conclusion to fail.

**warning**: A Sound Argument cannot be established by inspecting the inference alone; one must independently verify the premises, and arguing from "this looks valid, therefore it is sound" is a standard route to confidently believing falsehoods.

## Cogent Argument

- secondary_domains: [logic, inductive-reasoning]
- aliases: [cogent inductive argument]
- broader: [inductive arguments]
- related: [strong argument, premise acceptability, inductive confirmation]

**definition**: A Cogent Argument is a strong inductive argument whose premises are also actually true; cogency is the inductive analogue of soundness, marking the highest grade an inductive argument can achieve.

**key_claim**: A Cogent Argument transmits high probability from true premises to its conclusion, but unlike a sound deductive argument it leaves the conclusion defeasible, so even a fully cogent argument can have its conclusion overturned by new evidence.

**warning**: A Cogent Argument is sometimes treated as proving its conclusion in the deductive sense; the cogency relation is probabilistic, and treating it as conclusive collapses the inductive/deductive distinction that the term was introduced to preserve.

## Strong Argument

- secondary_domains: [logic, inductive-reasoning]
- aliases: [strong inductive argument]
- broader: [inductive arguments]
- related: [cogent argument, inductive confirmation, premise acceptability]

**definition**: A Strong Argument is an inductive argument whose conclusion is highly probable given the truth of its premises; inductive strength is a matter of degree rather than the all-or-nothing property that validity is for deduction.

**key_claim**: A Strong Argument can have true premises and a false conclusion without losing its strength, because inductive support is probabilistic; this is why inductive evaluation requires distinguishing the quality of the inference from the accuracy of the prediction.

**warning**: A Strong Argument with false premises can be just as inferentially well-formed as one with true premises; conflating strength with cogency leads to treating any well-structured inductive argument as evidentially decisive.

## Syllogism

- secondary_domains: [logic, formal-logic, history-of-logic]
- aliases: [syllogistic argument]
- broader: [deductive arguments]
- narrower: [categorical syllogism, hypothetical syllogism]
- related: [enthymeme, valid argument, logical form]

**definition**: A Syllogism is a deductive argument consisting of two premises and a conclusion, in which the conclusion is derived from the premises by a fixed inferential pattern; the term originates with Aristotle and dominates the pre-modern logical tradition.

**key_claim**: A Syllogism makes the structural commitments of an inference explicit by isolating exactly two premises that jointly entail the conclusion; this minimalism is what allowed ancient and medieval logicians to enumerate valid inference patterns systematically.

**warning**: A Syllogism is sometimes treated as the universal form of deductive reasoning, but contemporary logic recognises many valid inference patterns that exceed two-premise structure; treating syllogistic form as exhaustive misrepresents the scope of deductive logic.

## Categorical Syllogism

- secondary_domains: [logic, formal-logic, history-of-logic]
- aliases: [Aristotelian syllogism, term syllogism]
- broader: [syllogism]
- related: [syllogism, valid argument, logical form]
- prerequisites: [syllogism]

**definition**: A Categorical Syllogism is a syllogism whose three statements are all categorical propositions — assertions about the relations between two classes (all, some, no, some-not) — and whose validity is determined by the arrangement of those classes across the premises and conclusion.

**key_claim**: A Categorical Syllogism is fully classifiable by its mood and figure, which together pick out exactly 256 possible forms, of which only a small finite subset is valid; this exhaustive enumerability is the historical bedrock of formal validity testing.

**warning**: A Categorical Syllogism imposes a quantifier structure (all/some/none) that does not capture relational reasoning, modal claims, or multiple-quantifier inferences; relying on it for general-purpose argument analysis silently filters out most of modern formal reasoning.

## Enthymeme

- secondary_domains: [logic, rhetoric]
- aliases: [rhetorical syllogism, suppressed-premise argument]
- broader: [argument structure]
- related: [syllogism, argument reconstruction, premise acceptability]

**definition**: An Enthymeme is an argument in which one or more premises (or, less commonly, the conclusion) is left unstated because the speaker assumes the audience will supply it; most ordinary-language arguments are enthymematic.

**key_claim**: An Enthymeme is not a deficient argument but a compressed one; reconstructing the suppressed premise is the central skill of argument analysis, because evaluation cannot proceed until the implicit content has been made explicit.

**warning**: An Enthymeme can be reconstructed in multiple legitimate ways, and the choice of reconstruction can determine whether the argument appears valid, sound, or fallacious; analysts must apply the principle of charity rather than picking the reconstruction most convenient for refutation.

## Argument Mapping

- secondary_domains: [logic, critical-thinking-pedagogy, visual-reasoning]
- aliases: [argument diagramming]
- broader: [argument analysis]
- related: [argument structure, argument reconstruction, steelmanning]

**definition**: Argument Mapping is the practice of representing the structure of an argument as a diagram in which premises, sub-conclusions, and conclusions appear as nodes connected by labelled support and objection relations.

**key_claim**: Argument Mapping makes inferential structure visually inspectable, which exposes co-premises that must be evaluated jointly, distinguishes linked from convergent support, and surfaces gaps that linear prose tends to hide.

**warning**: Argument Mapping is sometimes treated as a substitute for argument evaluation; the diagram makes structure visible but does not by itself measure validity, premise truth, or relevance, and a beautifully mapped argument can still be a bad one.

## Steelmanning

- secondary_domains: [rhetoric, dialectic, virtue-epistemology]
- aliases: [steel-manning, principle of charity application]
- broader: [argument analysis]
- related: [intellectual empathy, fair mindedness, argument reconstruction]

**definition**: Steelmanning is the practice of engaging with the strongest, most defensible version of an opposing argument — strengthening it where the original presentation was weak — before offering a critique.

**key_claim**: Steelmanning increases the epistemic value of disagreement because a critique that defeats the steelmanned version defeats the position itself, whereas a critique that defeats only the original presentation defeats nothing more than that presentation.

**warning**: Steelmanning can be misapplied as putting words in the opponent's mouth or as constructing a position the opponent would disavow; the practice requires reconstructing the strongest version that the opponent could plausibly endorse, not the strongest version one can imagine on their behalf.

## Burden Of Proof

- secondary_domains: [logic, rhetoric, epistemology]
- aliases: [onus probandi]
- broader: [dialectical norms]
- related: [appeal to ignorance, premise acceptability, defeater]

**definition**: Burden Of Proof is the dialectical obligation to provide reasons for a contested claim; it specifies which party in a disagreement must produce evidence or argument before the other party is required to respond.

**key_claim**: Burden Of Proof is asymmetric and context-sensitive: the party making a positive existence claim, the party seeking to overturn a default position, and the party invoking an unusual mechanism each typically bear it, which is why the question "who has the burden here?" usually does substantive work in resolving disputes.

**warning**: Burden Of Proof is frequently weaponised as a rhetorical move to relieve oneself of any need to argue; declaring that "the burden is on you" without justifying the assignment is a standard form of evasive reasoning that masquerades as procedural fairness.

## Defeater

- secondary_domains: [epistemology, defeasible-reasoning]
- aliases: [epistemic defeater]
- broader: [defeasible reasoning]
- narrower: [rebutting defeater, undercutting defeater]
- related: [premise acceptability, burden of proof]

**definition**: A Defeater is a piece of evidence or argument that, when added to one's existing reasons for a belief, removes or substantially reduces the justification that those reasons would otherwise provide.

**key_claim**: A Defeater operates on the justificatory relation rather than on the belief directly; this is why a thinker can rationally lower confidence in a conclusion even when none of the original supporting premises has been refuted.

**warning**: A Defeater is sometimes confused with mere disagreement; the existence of someone who denies the conclusion is not a defeater unless the disagreement is itself evidence — for example, by tracking information the believer lacks.

## Rebutting Defeater

- secondary_domains: [epistemology, defeasible-reasoning]
- aliases: [type-1 defeater]
- broader: [defeater]
- related: [undercutting defeater, premise acceptability]
- prerequisites: [defeater]

**definition**: A Rebutting Defeater is a defeater that gives positive reason to believe the conclusion is false, as distinct from giving reason to doubt that the original evidence supports it.

**key_claim**: A Rebutting Defeater attacks the conclusion directly, which means even an impeccable argument loses justificatory force when one acquires independent reason to believe its conclusion is in fact false.

**warning**: A Rebutting Defeater can be confused with an undercutting defeater because both reduce justification; the distinction matters because they call for different responses — the rebutting case typically requires identifying which premise is the false one, while the undercutting case does not.

## Undercutting Defeater

- secondary_domains: [epistemology, defeasible-reasoning]
- aliases: [type-2 defeater, undermining defeater]
- broader: [defeater]
- related: [rebutting defeater, premise acceptability]
- prerequisites: [defeater]

**definition**: An Undercutting Defeater is a defeater that gives reason to doubt that one's evidence actually supports the conclusion, without giving any direct reason to believe the conclusion is false.

**key_claim**: An Undercutting Defeater attacks the inferential link between evidence and conclusion rather than the conclusion itself; this is what distinguishes "your evidence is unreliable" (undercutting) from "your conclusion is wrong" (rebutting).

**warning**: An Undercutting Defeater is often dismissed as merely procedural, but a successful undercutter neutralises a previously strong argument and leaves the conclusion's truth value entirely open, which is a substantively different epistemic state from believing the conclusion is false.

## Premise Acceptability

- secondary_domains: [logic, informal-logic, rhetoric]
- aliases: [acceptability of premises]
- broader: [argument evaluation]
- related: [sound argument, cogent argument, burden of proof, defeater]

**definition**: Premise Acceptability is the criterion for evaluating whether the premises of an argument should be granted by a reasonable audience, given the available evidence, the audience's background knowledge, and the argumentative context.

**key_claim**: Premise Acceptability replaces strict truth as the working criterion in informal logic because most ordinary arguments turn on premises whose truth is contested or unverifiable; the practical question is whether the premises can be reasonably accepted, not whether they are demonstrably true.

**warning**: Premise Acceptability is audience-relative without being arbitrary; an arguer cannot simply assert that their premises are acceptable, because the acceptability standard requires that a reasonable, informed audience would grant them, which is a public criterion rather than a personal one.
