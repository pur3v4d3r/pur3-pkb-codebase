---
batch_name: batch-07b-logic-reasoning
batch_date: 2026-04-24
default_domain: logic
default_confidence: high
notes: |
  Batch 7b of 8. Focus: deductive/inductive/abductive reasoning and logic,
  analogical reasoning/logic, logical fallacies, propositional/predicate/modal
  logic, scientific reasoning, philosophy of science.
---

# Batch: Logic & Reasoning

## Deductive Reasoning

- domain: logic
- secondary_domains: [reasoning, philosophy]
- aliases: [deduction]
- broader: [reasoning, inference]
- related: [inductive-reasoning, abductive-reasoning, deductive-logic, [[validity], [[soundness]]]
- prerequisites: []
- confidence: high

**definition**: Deductive Reasoning is the form of inference in which the conclusion is asserted to follow *necessarily* from the premises — if the premises are true and the inferential structure is valid, the conclusion cannot be false — and is the form of reasoning formalised by classical logic and exemplified by mathematical proof.

**key_claim**: Deductive Reasoning offers certainty conditional on premises but obtains nothing the premises did not already implicitly contain; this trade-off — guaranteed conclusions in exchange for restricting outputs to what is implicit in inputs — explains why mathematics and logic can produce certain knowledge while empirical science, which requires going beyond data, cannot proceed by deduction alone.

**warning**: Deductive Reasoning is often confused in everyday speech with "good reasoning" generally, but a deductively valid argument with false premises produces a false conclusion as reliably as a good argument produces a true one; evaluating Deductive Reasoning requires checking *both* validity (the inferential structure) *and* premise truth, and casual reasoners frequently focus on one and ignore the other.

## Inductive Reasoning

- domain: logic
- secondary_domains: [reasoning, philosophy-of-science]
- aliases: [induction]
- broader: [reasoning, inference]
- related: [deductive-reasoning, abductive-reasoning, inductive-logic, [[problem-of-induction], [[hume]]]
- prerequisites: []
- confidence: high

**definition**: Inductive Reasoning is the form of inference in which conclusions are supported with *some degree of probability* rather than necessity — extending observed patterns to unobserved cases, generalising from samples to populations, projecting future from past — and is the form of reasoning fundamental to empirical science and everyday prediction.

**key_claim**: Inductive Reasoning is what makes new knowledge possible: deduction unpacks what is already implicit in premises, while induction extends knowledge beyond observed cases to unobserved ones, which is why induction is indispensable to empirical science despite being formally invalid (the conclusion can be false even when premises are true).

**warning**: Inductive Reasoning faces Hume's *problem of induction* — the inference from observed regularities to unobserved cases assumes the future will resemble the past, which itself can be justified only by an inductive argument and so is circular — and although working scientists and reasoners proceed pragmatically as though induction is licensed, the philosophical question of *why* it works has no fully satisfying answer.

## Abductive Reasoning

- domain: logic
- secondary_domains: [reasoning, philosophy-of-science]
- aliases: [abduction, inference to the best explanation]
- broader: [reasoning, inference]
- related: [deductive-reasoning, inductive-reasoning, abductive-logic, [[peirce], [[explanatory-virtues]]]
- prerequisites: []
- confidence: high

**definition**: Abductive Reasoning, named by C.S. Peirce, is the form of inference in which one accepts a hypothesis because it provides the *best available explanation* for the observed evidence — distinguished from deduction (which guarantees the conclusion) and from induction (which extends observed patterns) by its explanatory rather than enumerative character.

**key_claim**: Abductive Reasoning, formalised by Peter Lipton as "inference to the best explanation," is the dominant pattern of inference in scientific theorising, medical diagnosis, criminal investigation, and historical interpretation; it is what produces the explanatory hypotheses that subsequent deductive consequences and inductive testing then evaluate, making Abductive Reasoning the generative engine of investigative inquiry.

**warning**: Abductive Reasoning is only as good as the candidate-explanation set it considers — "the best available explanation" can still be a poor explanation if a better one was not generated — and is famously vulnerable to the *bad lot* objection: confident inference to the best of a bad lot of hypotheses is a recurring source of error in domains where investigators failed to consider hypotheses that turned out to be true.

## Deductive Logic

- domain: logic
- secondary_domains: [philosophy, mathematics]
- aliases: [formal deductive logic]
- broader: [logic]
- narrower: [propositional-logic, predicate-logic]
- related: [deductive-reasoning, [[validity], [[completeness], [[soundness]]]
- prerequisites: []
- confidence: high

**definition**: Deductive Logic is the formal study of the inferential structures that make conclusions follow necessarily from premises — comprising propositional logic (which analyses inferences in terms of sentence-level connectives), predicate logic (which adds quantifiers and predicates), and modal extensions — and provides the mathematical infrastructure for reasoning about validity.

**key_claim**: Deductive Logic, since the formalisation by Frege, Russell, and Tarski, has provided rigorous machinery for analysing reasoning that no informal vocabulary can match: arguments can be checked for validity mechanically, soundness can be proved formally, and entire theories can be axiomatised, which is why mathematical disciplines that adopt Deductive Logic gain a level of rigour that informal disciplines rarely achieve.

**warning**: Deductive Logic captures only a narrow slice of how humans actually reason: most ordinary inference is non-monotonic, defeasible, and probabilistic in ways that classical Deductive Logic cannot represent, and treating Deductive Logic as a normative model of all reasoning misjudges what it is good for — it is the logic of necessity, not the logic of practical reasoning under uncertainty.

## Inductive Logic

- domain: logic
- secondary_domains: [philosophy-of-science, statistics]
- aliases: [formal inductive logic, probabilistic logic]
- broader: [logic]
- related: [inductive-reasoning, [[bayesian-inference], [[carnap], [[confirmation-theory]]]
- prerequisites: []
- confidence: high

**definition**: Inductive Logic is the formal study of evidential support relations between premises and conclusions — analysing how strongly evidence confirms or disconfirms hypotheses — and includes Carnapian confirmation theory, contemporary Bayesian inductive logic, and statistical-inferential frameworks that extend formal techniques to non-deductive inference.

**key_claim**: Inductive Logic in its contemporary Bayesian form provides a rigorous framework for analysing evidential reasoning: prior probabilities updated by likelihood ratios produce posterior probabilities, the framework is internally coherent in ways that informal inductive judgement is not, and it predicts well-documented departures from classical statistical practice in domains where prior information matters.

**warning**: Inductive Logic in its formal Bayesian guise requires prior probability assignments that are often contested or unavailable, and the choice of priors can substantially influence conclusions — which is why critics from frequentist statistics object to "subjective" Bayesianism while critics from within Bayesianism debate principled priors; the practical implication is that Inductive Logic is a tool that requires judgement, not an algorithm that delivers conclusions automatically.

## Abductive Logic

- domain: logic
- secondary_domains: [philosophy-of-science, ai]
- aliases: [logic of abduction]
- broader: [logic]
- related: [abductive-reasoning, [[explanatory-coherence], [[inference-to-the-best-explanation], [[diagnostic-reasoning]]]
- prerequisites: []
- confidence: medium

**definition**: Abductive Logic is the formal and computational study of inference to the best explanation — including logical-AI frameworks for abductive computation, explanation-based learning, diagnostic reasoning systems, and philosophical analyses of explanatory virtues — and provides the technical machinery for the Abductive Reasoning patterns that pervade scientific and diagnostic practice.

**key_claim**: Abductive Logic faces a foundational challenge that Deductive and Inductive Logic do not: the criterion of "best" explanation is comparative across a candidate set and depends on explanatory virtues (simplicity, coherence, scope, fertility) that are themselves contested; current Abductive Logic frameworks make these virtues explicit and tractable but cannot fully resolve the underlying philosophical debates about what makes an explanation good.

**warning**: Abductive Logic is sometimes presented in AI literature as a settled formal framework, but the underlying question of what makes one explanation "better" than another remains open, and abductive systems whose explanatory metric is not justified can produce confident outputs that rest on contestable assumptions about what explanation means in the relevant domain.

## Analogical Reasoning

- domain: reasoning
- secondary_domains: [cognitive-science, problem-solving]
- aliases: [reasoning by analogy]
- broader: [reasoning]
- related: [analogical-logic, [[structure-mapping], [[gentner], [[case-based-reasoning], [[far-transfer]]]
- prerequisites: []
- confidence: high

**definition**: Analogical Reasoning is the form of inference in which structural correspondence between a familiar source domain and an unfamiliar target domain licenses the projection of relations from source to target — formalised in Dedre Gentner's structure-mapping theory and ubiquitous in scientific discovery, learning, and ordinary problem-solving.

**key_claim**: Analogical Reasoning is one of the most powerful cognitive operations available for transferring knowledge across domains, but its productive use depends on attending to *structural* (relational) similarity rather than to *surface* (object-property) similarity — a distinction novices reliably miss, which explains why analogical transfer is observed routinely in experts and rarely in novices on the same source-target pairs.

**warning**: Analogical Reasoning produces *false* projections as readily as true ones — the Bohr-atom-as-solar-system analogy, the brain-as-computer analogy, the body-as-machine analogy — because nothing in the structural correspondence by itself guarantees that the projected relations actually obtain in the target; analogies are sources of hypothesis, not of conclusion, and require independent verification.

## Analogical Logic

- domain: reasoning
- secondary_domains: [cognitive-science, ai]
- aliases: [logic of analogy]
- broader: [reasoning, [[non-classical-logic]]]
- related: [analogical-reasoning, [[structure-mapping-engine], [[case-based-reasoning], [[similarity-metrics]]]
- prerequisites: [analogical-reasoning]
- confidence: medium

**definition**: Analogical Logic is the formal and computational study of analogy as an inferential operation — including structure-mapping engines, case-based reasoning systems, similarity metrics, and philosophical analyses of analogical inference — and provides the technical machinery for evaluating when an analogical projection is warranted and how strongly.

**key_claim**: Analogical Logic, in Gentner's structure-mapping framework and its computational implementations, demonstrates that analogical inference can be made tractable and partially formalisable: systematicity (preferring deeper relational matches over isolated property matches) and one-to-one mapping constraints provide principled criteria that distinguish strong from weak analogies in ways that match human judgements of analogical quality.

**warning**: Analogical Logic remains less formally developed than deductive and inductive logic, and the formal frameworks that exist (structure-mapping, case-based reasoning) capture some but not all of what makes analogies illuminating; treating computational analogical systems as complete models of analogical reasoning misses the role of pragmatic context, conversational purpose, and aesthetic judgement in human analogical practice.

## Logical Fallacies

- domain: logic
- secondary_domains: [critical-thinking, rhetoric]
- aliases: [fallacies of reasoning, informal fallacies]
- broader: [logic, critical-thinking]
- related: [argument-analysis, [[ad-hominem], [[straw-man], [[false-dichotomy], [[appeal-to-authority]]]
- prerequisites: []
- confidence: high

**definition**: Logical Fallacies are recurring patterns of defective reasoning that resemble valid arguments but fail to support their conclusions — encompassing formal fallacies (deductively invalid moves like affirming the consequent), informal fallacies of relevance (ad hominem, appeal to emotion), and informal fallacies of presumption (false dichotomy, begging the question, hasty generalisation).

**key_claim**: Logical Fallacies are useful as a diagnostic vocabulary for naming patterns of bad reasoning, but their pedagogical leverage comes from recognising the patterns in real arguments — particularly in one's own — rather than from memorising the canonical list, since the list is long, taxonomies disagree, and many real arguments instantiate multiple fallacies or borderline cases.

**warning**: Logical Fallacies are routinely weaponised in online discourse as conversation-stoppers — "that's an ad hominem!" deployed against substantive criticisms of a claimant's relevant track record, "straw man!" deployed against any reformulation of one's view — and this rhetorical use is itself a misapplication; a charge of fallacy must be argued, not asserted, and the underlying fallacy taxonomies are subtler than the slogans suggest.

## Propositional Logic

- domain: logic
- secondary_domains: [philosophy, mathematics]
- aliases: [sentential logic, propositional calculus]
- broader: [deductive-logic]
- related: [predicate-logic, [[truth-tables], [[connectives], [[boolean-algebra]]]
- prerequisites: [deductive-logic]
- confidence: high

**definition**: Propositional Logic is the branch of formal logic that analyses inferences in terms of sentence-level connectives — and, or, not, if-then, if-and-only-if — without reference to the internal structure of the sentences, and provides the foundation on which predicate and modal logics are built.

**key_claim**: Propositional Logic is decidable — there is a mechanical procedure (truth tables, satisfiability solvers) that determines whether any propositional argument is valid — making it the first formal system in which the validity of arbitrary arguments can be checked algorithmically rather than judged intuitively, which is the foundational achievement of modern logic.

**warning**: Propositional Logic captures the inferential structure that depends purely on connectives, which is a small fraction of the inferential structure of natural-language reasoning; arguments that depend on quantification ("all," "some"), identity, or modality cannot be adequately analysed in Propositional Logic alone, which is why predicate and modal extensions were developed.

## Predicate Logic

- domain: logic
- secondary_domains: [philosophy, mathematics]
- aliases: [first-order logic, quantificational logic, FOL]
- broader: [deductive-logic]
- related: [propositional-logic, [[quantifiers], [[frege], [[completeness-theorem]]]
- prerequisites: [propositional-logic]
- confidence: high

**definition**: Predicate Logic is the branch of formal logic that extends propositional logic by analysing the internal structure of sentences in terms of predicates, terms, variables, and quantifiers (universal "for all" and existential "there exists") — formalised by Frege and standardised in the 20th century — and is the foundational logic of modern mathematics.

**key_claim**: Predicate Logic is expressive enough to formalise most mathematical reasoning and to capture the inferential structure of quantified arguments that propositional logic cannot — and Gödel's completeness theorem (1929) establishes that the standard axiom system for first-order Predicate Logic captures *all* and only the valid first-order arguments, a result of remarkable depth.

**warning**: Predicate Logic, despite its expressive power, has well-known limitations: it cannot quantify over predicates (second-order needed), cannot directly express modality (modal logic needed), and Gödel's incompleteness theorems show that for any sufficiently rich axiom system formalisable in Predicate Logic, there are true statements that the system cannot prove — limitations that constrain ambitions of fully formalising mathematics in first-order logic.

## Modal Logic

- domain: logic
- secondary_domains: [philosophy, computer-science]
- aliases: [logic of necessity and possibility]
- broader: [non-classical-logic, deductive-logic]
- related: [[possible-worlds], [[kripke-semantics], [[deontic-logic], [[epistemic-logic]]]
- prerequisites: [predicate-logic]
- confidence: high

**definition**: Modal Logic is the branch of formal logic that adds operators for *necessity* and *possibility* to classical logic — and by extension for related modalities such as obligation/permission (deontic), knowledge/belief (epistemic), and temporal relations — and is given a model-theoretic semantics through Saul Kripke's possible-worlds framework.

**key_claim**: Modal Logic provides the formal infrastructure for reasoning about contexts where classical logic is insufficient: counterfactuals in philosophy, knowledge and belief in epistemology and AI, obligation in ethics and law, computational state in computer science — and Kripke's possible-worlds semantics gives all of these a unified mathematical treatment.

**warning**: Modal Logic comes in many systems (T, S4, S5, K and many more) corresponding to different assumptions about the underlying modal accessibility relation; choosing the wrong system for a given application — using S5 for epistemic logic when knowledge is not factive across iterations, for instance — produces formally valid arguments whose conclusions don't survive scrutiny, so system selection is itself a substantive philosophical decision.

## Scientific Reasoning

- domain: philosophy-of-science
- secondary_domains: [reasoning, methodology]
- aliases: [scientific method, scientific inference]
- broader: [reasoning, philosophy-of-science]
- related: [[hypothesis-testing], [[falsificationism], [[bayesian-confirmation], inductive-reasoning, abductive-reasoning]
- prerequisites: []
- confidence: high

**definition**: Scientific Reasoning is the family of inferential and investigative practices used to generate, test, and revise empirical knowledge — including hypothesis generation, prediction, controlled observation and experimentation, statistical inference, theory comparison, and meta-analytic synthesis — and is the methodological core of the empirical sciences.

**key_claim**: Scientific Reasoning is not a single algorithm but a *cluster of practices* whose specific composition varies across disciplines: the inferential profile of high-energy physics differs from that of evolutionary biology, which differs again from that of clinical epidemiology and from the human sciences, and pedagogy that teaches a generic "scientific method" misrepresents the diversity of what working scientists actually do.

**warning**: Scientific Reasoning is widely taught as the simple Popperian falsification model, but contemporary philosophy of science (Kuhn, Lakatos, Laudan, contemporary Bayesians) has substantially complicated this picture — theories are rarely abandoned on single failed predictions, auxiliary assumptions absorb most disconfirmation, and theory choice involves comparison rather than isolated testing — so consumers of science should not expect actual practice to match the simplified textbook account.

## Philosophy of Science

- domain: philosophy-of-science
- secondary_domains: [philosophy, methodology]
- aliases: [phil sci, philosophy of the sciences]
- broader: [philosophy]
- related: [scientific-reasoning, [[scientific-realism], [[underdetermination], [[demarcation-problem], [[paradigm]]]
- prerequisites: []
- confidence: high

**definition**: The Philosophy of Science is the philosophical subfield investigating the nature, structure, and warrant of scientific knowledge — encompassing questions about scientific method, theory confirmation and falsification, scientific explanation, the demarcation of science from non-science, scientific realism vs. anti-realism, and the social structure of scientific communities.

**key_claim**: The Philosophy of Science has substantially shifted across the 20th century from logical-empiricist and Popperian models that idealised science as cumulative testing, through Kuhnian and post-Kuhnian models that emphasised paradigms and incommensurability, to contemporary integrated approaches drawing on history, sociology, and cognitive science of science — with the consequence that no single picture of "the scientific method" is endorsed by current scholarship.

**warning**: The Philosophy of Science is often invoked rhetorically by scientists and science communicators to defend or attack specific claims, but the field's own conclusions are subtler than the slogans imported from it: "science is falsifiable" (Popper), "paradigm shifts" (Kuhn), "what doesn't kill it makes it stronger" (Lakatos) are caricatures of more careful positions, and consumers of philosophy-of-science arguments should consult primary sources rather than the popular adaptations.
