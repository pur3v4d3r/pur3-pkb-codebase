---
batch_name: ct-07-formal-logic
batch_date: 2026-05-12
default_domain: logic
default_confidence: high
notes: |
  Ten formal-logic concepts covering conditional reasoning, the structural
  apparatus of validity, and famous paradoxes that constrain naive logical
  intuitions. Companion to the argument-theory and informal-fallacies sets.
---

## Necessary And Sufficient Conditions

- secondary_domains: [logic, conditional-reasoning, conceptual-analysis]
- aliases: [necessary-and-sufficient conditions]
- broader: [conditional reasoning]
- related: [conditional reasoning, contrapositive, logical consequence]

**definition**: Necessary And Sufficient Conditions describe two distinct logical relations: a necessary condition for X is one without which X cannot obtain, and a sufficient condition for X is one whose presence guarantees that X obtains; a biconditional asserts both at once.

**key_claim**: Necessary And Sufficient Conditions sharpen most ordinary "if" talk by separating out two relations that natural language regularly fuses; failure to draw the distinction is responsible for a large class of definitional disputes and policy confusions.

**warning**: Necessary And Sufficient Conditions are easy to mis-translate from English; "only if" introduces a necessary condition while "if" introduces a sufficient one, and reversing this mapping is a routine source of logical error in both casual reasoning and exam settings.

## Contrapositive

- secondary_domains: [logic, formal-logic]
- aliases: [contrapositive form]
- broader: [conditional transformations]
- related: [conditional reasoning, logical consequence, validity vs soundness]

**definition**: The Contrapositive of a conditional "if P then Q" is the conditional "if not-Q then not-P"; the original and its contrapositive are logically equivalent — they have the same truth conditions in every possible case.

**key_claim**: The Contrapositive is the only one of the three derived conditionals (converse, inverse, contrapositive) that is logically equivalent to the original; recognising this enables a wide class of valid reformulations that natural-language reasoning routinely treats as suspect or invalid.

**warning**: The Contrapositive is frequently confused with the converse ("if Q then P") or inverse ("if not-P then not-Q"), neither of which is logically equivalent to the original; affirming a converse on the strength of the original is the formal source of the affirming-the-consequent fallacy.

## Conditional Reasoning

- secondary_domains: [logic, cognitive-psychology, formal-logic]
- aliases: [reasoning with conditionals, "if-then" reasoning]
- broader: [reasoning patterns]
- narrower: [modus ponens, modus tollens]
- related: [necessary and sufficient conditions, contrapositive, suppositional reasoning]

**definition**: Conditional Reasoning is reasoning that proceeds from "if P then Q" statements together with information about P or Q to draw further conclusions; modus ponens (from P infer Q) and modus tollens (from not-Q infer not-P) are its two valid elementary patterns.

**key_claim**: Conditional Reasoning is the workhorse of both formal proof and ordinary deliberation, but psychological research consistently shows that humans handle modus ponens easily, modus tollens with difficulty, and the invalid patterns (affirming the consequent, denying the antecedent) almost as readily as the valid ones.

**warning**: Conditional Reasoning in natural language often interprets "if P then Q" as a biconditional, especially in conversational and instructional contexts; this interpretive default produces inferences that are pragmatically appropriate but formally invalid, and the formal/pragmatic gap is the source of much disagreement about what "if" means.

## Logical Consistency

- secondary_domains: [logic, formal-logic]
- aliases: [consistency, non-contradiction]
- broader: [structural properties of belief sets]
- related: [logical form, logical consequence, sound argument]

**definition**: Logical Consistency is the property of a set of statements that they could all be true together; an inconsistent set is one whose members jointly entail a contradiction, so that no possible interpretation makes them all true at once.

**key_claim**: Logical Consistency is a minimal rationality constraint on a body of belief: from a contradiction, classical logic permits the derivation of any statement whatever (ex falso quodlibet), so an inconsistent belief set provides no guidance about what else to believe.

**warning**: Logical Consistency is a structural property and need not coincide with truth or plausibility; a fully consistent set of beliefs can still be entirely false, and treating consistency as the sole epistemic standard ignores the relation between a belief set and the world it purports to describe.

## Logical Form

- secondary_domains: [logic, formal-logic, philosophy-of-language]
- aliases: [form of an argument]
- broader: [structural analysis]
- related: [argument structure, valid argument, logical consequence]

**definition**: Logical Form is the abstract structural pattern of a statement or argument that determines its logical properties — its consistency with other statements, its entailments, its validity — independently of the specific subject-matter of its terms.

**key_claim**: Logical Form is what makes formal logic possible as a general discipline; once form is isolated from content, the validity of an argument can be assessed by reference to its pattern, which generalises across every substitution that preserves the form.

**warning**: Logical Form is not uniquely determined by surface grammar; the same English sentence can be assigned different logical forms depending on the formal language used, and disputes about the "correct" formalisation of natural language are themselves substantive philosophical questions.

## Validity Vs Soundness

- secondary_domains: [logic, formal-logic, critical-thinking-pedagogy]
- aliases: [validity-soundness distinction]
- broader: [deductive evaluation]
- related: [valid argument, sound argument, premise acceptability]

**definition**: Validity Vs Soundness contrasts two grades of deductive evaluation: validity is the structural property that guarantees truth-preservation from premises to conclusion, while soundness adds the further requirement that the premises actually be true.

**key_claim**: Validity Vs Soundness is the most reliably misunderstood distinction in introductory logic; the technical sense of "valid" allows arguments with false premises and false conclusions to be valid, which is unintuitive but is exactly what makes validity a purely structural notion.

**warning**: Validity Vs Soundness can be flattened by everyday usage in which "valid" means "good" and "sound" means "agreeable"; importing the colloquial senses into formal evaluation collapses the two-step structure of deductive assessment that the distinction was introduced to enforce.

## Logical Consequence

- secondary_domains: [logic, formal-logic, model-theory]
- aliases: [entailment, semantic consequence]
- broader: [deductive relations]
- related: [valid argument, logical form, epistemic closure]

**definition**: Logical Consequence is the relation that holds between a set of premises and a conclusion when the truth of the premises guarantees the truth of the conclusion, as a matter of logical form rather than empirical fact.

**key_claim**: Logical Consequence is the precise relation that validity tracks; an argument is valid exactly when its conclusion is a logical consequence of its premises, which is why every theory of logic is in part a theory of consequence.

**warning**: Logical Consequence has multiple non-equivalent definitions across logical systems (semantic vs syntactic, classical vs intuitionistic vs relevance); treating the relation as fixed across all of logic obscures the fact that what counts as following-from depends on which logical framework is in force.

## Sorites Paradox

- secondary_domains: [logic, philosophy-of-language, vagueness]
- aliases: [paradox of the heap, sorites]
- broader: [paradoxes of vagueness]
- related: [liar paradox, suppositional reasoning]

**definition**: The Sorites Paradox is the puzzle generated by chaining together intuitively true premises about vague predicates ("a heap of sand minus one grain is still a heap") to produce an unacceptable conclusion ("a single grain is a heap"); each step seems obvious but the cumulative reasoning fails.

**key_claim**: The Sorites Paradox shows that vague predicates resist treatment by classical logic; either the seemingly obvious tolerance principles must be denied, classical logic must be revised (e.g., to many-valued or fuzzy logics), or the law of excluded middle must be qualified for vague terms.

**warning**: The Sorites Paradox is sometimes dismissed as a verbal trick, but it has generated a substantial technical literature precisely because every proposed solution carries significant cost; treating it as a mere word game ignores that vagueness is a pervasive property of natural-language predicates.

## Liar Paradox

- secondary_domains: [logic, philosophy-of-language, semantic-paradoxes]
- aliases: [Epimenides paradox, liar sentence]
- broader: [semantic paradoxes]
- related: [sorites paradox, logical consistency, logical form]

**definition**: The Liar Paradox is the puzzle generated by self-referential sentences such as "this sentence is false," which appear to be true if and only if they are false; the paradox shows that naive principles of truth and self-reference are jointly inconsistent.

**key_claim**: The Liar Paradox forced the development of formal theories of truth that block self-application (Tarski's hierarchy) or revise classical logic (paracomplete and paraconsistent approaches); without one of these moves, a natural language with both a truth predicate and unrestricted self-reference is provably inconsistent.

**warning**: The Liar Paradox should not be filed away as a curiosity; structurally similar paradoxes (Curry's, Yablo's, the strengthened liar) reappear in any system rich enough to express its own semantics, so any theory of truth must take a position on them whether explicitly or by default.

## Suppositional Reasoning

- secondary_domains: [logic, conditional-reasoning, philosophy-of-mind]
- aliases: [reasoning under supposition, hypothetical reasoning]
- broader: [reasoning patterns]
- related: [conditional reasoning, contrapositive, argument structure]

**definition**: Suppositional Reasoning is reasoning in which a proposition is temporarily assumed for the sake of argument, used to derive consequences, and then discharged — the most familiar form is conditional proof, in which assuming P and deriving Q licenses the conclusion "if P then Q."

**key_claim**: Suppositional Reasoning is what allows agents to reason about possibilities they do not believe; it is the cognitive mechanism behind hypothetical thinking, indirect proof, planning, and counterfactual evaluation, all of which require entertaining content without endorsing it.

**warning**: Suppositional Reasoning can leak: assumptions made for the sake of argument sometimes get treated as established when the argument is recapped, especially in long chains of reasoning, so explicit discharge of suppositions is a discipline rather than an automatic process.
