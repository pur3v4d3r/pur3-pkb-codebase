---
batch_name: logic-and-critical-reasoning
batch_date: 2026-05-01
default_domain: critical-thinking
default_confidence: high
notes: |
  Batch 5 — closes ghost links in the logic, fallacy, and critical-reasoning
  cluster: the genus terms (informal-fallacy, informal-logic), specific
  fallacies and inquiry techniques, and epistemic-injustice anchors that
  the existing critical-thinking notes already reference.
---

# Batch: Logic and Critical Reasoning

## Informal Fallacy

- secondary_domains: [logic, philosophy]
- aliases: [informal logical fallacy]
- broader: [logical-fallacies]
- narrower: [ad-hominem, straw-man-fallacy, slippery-slope-fallacy, false-dichotomy, circular-reasoning, tu-quoque]
- related: [informal-logic, logical-fallacies, formal-logic, critical-thinking, argument-analysis, principle-of-charity]
- prerequisites: [logical-fallacies]
- confidence: high

**definition**: An Informal Fallacy is an argumentative error whose defect cannot be diagnosed purely by inspection of the argument's logical form — it depends on the content of the premises, the dialectical context, the relevance of the move to the disputed claim, or the unwarranted inferential transitions involved — distinguishing it from a formal fallacy whose error is structural.

**key_claim**: Informal Fallacy taxonomies are best understood as catalogues of recurring failure modes of dialectical reasoning rather than as a closed deductive system, which is why the same surface move can be a genuine fallacy in one context and a legitimate argumentative step in another, and why a useful taxonomy must specify the dialectical conditions under which each pattern fails.

**warning**: Informal Fallacy labels are routinely deployed to dismiss arguments without engaging their substance — the so-called fallacy-fallacy — but pattern-matching to a textbook label without showing that the dialectical conditions for the fallacy actually hold often produces an unjustified rejection that itself fails the standards of careful reasoning the labels are meant to enforce.

## Informal Logic

- secondary_domains: [philosophy, critical-thinking]
- aliases: [practical reasoning, argumentation theory]
- broader: [logical-reasoning]
- narrower: [informal-fallacy, toulmin-argument-model, argument-analysis]
- related: [formal-logic, critical-thinking, argument-analysis, logical-fallacies, principle-of-charity, paul-elder-critical-thinking-framework]
- prerequisites: [logical-reasoning]
- confidence: high

**definition**: Informal Logic is the sub-discipline of logic devoted to the analysis, evaluation, and improvement of arguments as they occur in natural-language discourse — public deliberation, scientific debate, legal argumentation, everyday reasoning — using tools (argument diagrams, dialogue rules, norms of relevance and acceptability) suited to content-rich and dialectically situated reasoning rather than to formal-language proofs.

**key_claim**: Informal Logic emerged as a distinct field in the 1970s in response to the empirical observation that formal logic's expressive resources do not capture most of the reasoning errors and successes encountered in natural argumentative practice — the gap motivated the development of dialectical, pragmatic, and rhetorical tools that complement rather than reduce to formal deduction.

**warning**: Informal Logic is sometimes treated as the easier or less rigorous cousin of formal logic, but the converse is closer to the truth: informal logical analysis requires holding multiple dimensions (logical form, dialectical context, epistemic warrant, audience) in mind simultaneously, and the rigor lies in the discipline of those judgments rather than in mechanical inference.

## Tu Quoque

- secondary_domains: [logic, dialectics]
- aliases: ["you too" fallacy, appeal to hypocrisy]
- broader: [informal-fallacy]
- related: [ad-hominem, informal-fallacy, logical-fallacies, principle-of-charity, argument-analysis]
- prerequisites: [ad-hominem]
- confidence: high

**definition**: Tu Quoque is the informal fallacy in which a person rebuts a criticism by pointing out that the critic is themselves guilty of the same fault, treating the critic's hypocrisy as evidence against the criticism's content — a sub-species of ad hominem that targets consistency of practice rather than the critic's character or motives.

**key_claim**: Tu Quoque is fallacious as a refutation of a claim because the truth of a proposition is independent of the propositional consistency of the person asserting it, but the move is rhetorically powerful because it activates legitimate concerns about credibility and standing that listeners systematically allow to override their evaluation of the underlying argument.

**warning**: Tu Quoque is not always fallacious: when the dispute is genuinely about whose practical recommendations should be followed rather than about the truth of a factual claim, evidence that the recommender does not follow their own advice is relevant evidence about the recommendation's practicality; the diagnostic question is whether truth or practical authority is at stake.

## Strawman Argument

- secondary_domains: [logic, dialectics]
- aliases: [straw-man fallacy, straw man]
- broader: [informal-fallacy]
- related: [straw-man-fallacy, ad-hominem, informal-fallacy, principle-of-charity, argument-analysis, critical-thinking]
- prerequisites: [informal-fallacy]
- confidence: high

**definition**: A Strawman Argument is the dialectical move in which one party misrepresents the opponent's position in a weakened or distorted form, refutes the misrepresentation, and then claims to have refuted the original position — distinguished from genuine objection by the gap between the position attacked and the position the opponent actually holds.

**key_claim**: A Strawman Argument is one of the most consequential failure modes in public discourse because the misrepresented position often becomes the version that propagates: subsequent participants engage with the strawman rather than the original, and the original becomes progressively harder to recover, which is why the principle of charity functions as the standing antidote.

**warning**: A Strawman Argument is sometimes diagnosed wherever a participant feels their position has been misunderstood, but the diagnostic standard is interpretive rather than emotional — the interpreter must show that a more charitable reading of the original was available and was not taken; without that demonstration the charge itself can become a Strawman of the critic.

## Second-Order Logic

- secondary_domains: [mathematical-logic, philosophy-of-logic]
- aliases: [SOL]
- broader: [formal-logic]
- related: [formal-logic, predicate-logic, propositional-logic, modal-logic, philosophy-of-logic]
- prerequisites: [predicate-logic]
- confidence: high

**definition**: Second-Order Logic is the formal logical system that extends first-order predicate logic by allowing quantification over predicates and relations as well as over individuals — permitting direct expression of mathematical concepts (such as the categorical characterization of the natural numbers) that first-order logic can capture only indirectly via axiom schemas.

**key_claim**: Second-Order Logic gains substantial expressive power over first-order logic but loses the metalogical properties (completeness with respect to a recursively axiomatizable proof system, compactness, Lowenheim-Skolem) that make first-order logic the standard substrate for foundations of mathematics — a trade-off Quine famously described as "set theory in sheep's clothing."

**warning**: Second-Order Logic is often invoked to argue that first-order logic is expressively impoverished, but the comparison depends on whether one uses the standard semantics (which preserves expressive power but loses completeness) or Henkin semantics (which restores completeness but reduces second-order logic's distinctive strength); presenting the trade-off without naming the semantics conceals where the cost is paid.

## Temporal Logic

- secondary_domains: [mathematical-logic, computer-science]
- aliases: [tense logic]
- broader: [modal-logic]
- related: [modal-logic, formal-logic, propositional-logic, predicate-logic, non-classical-logic]
- prerequisites: [modal-logic]
- confidence: high

**definition**: Temporal Logic is the family of formal logical systems that extend classical logic with operators for temporal qualification — typically "always in the future," "sometime in the future," "until," and their past-directed duals — providing the formal resources for reasoning about how propositions' truth-values change over time, with applications spanning philosophy of time, linguistics, and program verification.

**key_claim**: Temporal Logic became central to computer science through Pnueli's 1977 application of linear temporal logic to program specification: it allowed computer scientists to express liveness and safety properties of concurrent programs formally, which made model-checking algorithms and the entire industrial verification toolchain possible — a striking case of philosophical formalism driving engineering practice.

**warning**: Temporal Logic comes in incompatible flavors (linear versus branching time, point-based versus interval-based, discrete versus dense versus continuous time) whose theorems and complexity classes differ; "Temporal Logic" without qualification names a family rather than a system, and importing results from one variant into another is a frequent source of error.

## Socratic Questioning

- secondary_domains: [pedagogy, critical-thinking]
- aliases: [Socratic dialogue, Socratic inquiry]
- broader: [socratic-method]
- related: [socratic-method, paul-elder-critical-thinking-framework, elements-of-thought, intellectual-standards, critical-thinking, reflective-thinking, deweys-reflective-thinking]
- prerequisites: [socratic-method]
- confidence: high

**definition**: Socratic Questioning is the disciplined questioning technique, generalized from the Socratic method, in which a facilitator probes the assumptions, evidence, viewpoints, implications, and conceptual clarity of a position through a structured sequence of open-ended questions — operationalized in contemporary critical-thinking pedagogy by the Paul-Elder framework's six taxonomies of questions.

**key_claim**: Socratic Questioning is most effective when it targets the structural elements of reasoning (purpose, question, information, concept, assumption, inference, point of view, implication) rather than the surface content of a position, because targeting structure forces the respondent to articulate the load-bearing components of their thinking that they did not previously have to make explicit.

**warning**: Socratic Questioning is often performed as a rhetorical technique for leading respondents to predetermined conclusions, but in that mode it functions as covert persuasion rather than inquiry; the diagnostic feature of authentic Socratic Questioning is that the questioner is also genuinely uncertain about where the inquiry will land and prepared to update on the respondent's answers.

## Source Evaluation

- secondary_domains: [information-literacy, epistemology]
- aliases: [source assessment, source criticism]
- broader: [epistemic-vigilance]
- related: [epistemic-vigilance, social-epistemology, testimony, principle-of-charity, critical-thinking, intellectual-humility]
- prerequisites: [epistemic-vigilance]
- confidence: high

**definition**: Source Evaluation is the systematic assessment of the credibility, expertise, independence, conflicts of interest, methodological quality, and corroboration status of an information source before granting its claims epistemic weight — the operational practice that implements epistemic vigilance in research, journalism, and personal knowledge work.

**key_claim**: Source Evaluation has shifted in the digital era from properties of the document to properties of the network: the trustworthiness of a claim now depends as much on the transitive credibility of the citation chain, the institutional embedding of the source, and the divergence of independent corroborations as on any feature of the document examined in isolation.

**warning**: Source Evaluation heuristics that work for traditional published sources (peer review, institutional affiliation, credentialed authorship) generalize poorly to social-media and AI-generated content, where the surface markers of credibility can be cheaply spoofed; importing the older heuristics without recalibration produces predictable failures of the form "looked authoritative, was fabricated."

## Testimonial Injustice

- secondary_domains: [epistemic-injustice, social-epistemology]
- aliases: [testimonial credibility deficit]
- broader: [epistemic-injustice]
- related: [epistemic-injustice, testimony, social-epistemology, prejudice, implicit-bias, principle-of-charity]
- prerequisites: [epistemic-injustice]
- confidence: high

**definition**: Testimonial Injustice is the epistemic-injustice form, named by Miranda Fricker, in which a hearer assigns a speaker less credibility than the speaker's testimony deserves due to identity-prejudice — racial, gendered, class-based, or other — about the social group to which the speaker is perceived to belong, with the consequence that the speaker is wronged specifically as a knower.

**key_claim**: Testimonial Injustice is wrong on two distinct registers that the analysis must keep separate: it is an ethical wrong to the speaker (treating them as less credible than they are) and an epistemic wrong to the hearer and to the wider epistemic community (excluding warranted information from the credible-testimony pool), and remedies that address only one register leave the other untouched.

**warning**: Testimonial Injustice is sometimes invoked to license the inverse error — granting credibility on identity grounds rather than evidential grounds — but the corrective virtue Fricker identifies is calibration of credibility against actual reliability, not over-correction in the opposite direction; treating any credibility deficit as Testimonial Injustice without showing prejudice as its cause inflates the construct beyond its argumentative warrant.

## Testimony

- secondary_domains: [social-epistemology, philosophy-of-language]
- aliases: [testimonial knowledge]
- broader: [social-epistemology]
- related: [social-epistemology, epistemic-vigilance, testimonial-injustice, source-evaluation, knowledge-by-acquaintance-vs-description, justified-true-belief, principle-of-charity]
- prerequisites: [social-epistemology]
- confidence: high

**definition**: Testimony in epistemology refers to the transmission of a belief from one agent to another via assertion, and to the philosophical questions about when and how such transmission yields justified belief or knowledge in the recipient — the central topic of social epistemology, since the vast majority of what any individual knows is acquired by Testimony rather than by first-person observation or inference.

**key_claim**: Testimony is the subject of a long-standing dispute between reductionist views (Testimony is justified only when the hearer has independent reason to trust the source) and non-reductionist views (Testimony is a basic source of justification analogous to perception or memory); the dispute has practical bite because the two positions license very different default attitudes toward unverified sources.

**warning**: Testimony is often discussed as if its epistemology were exhausted by the dyad of speaker and hearer, but most actual Testimony moves through chains of testifiers, with each link adding noise, bias, and selection effects; treating multi-hop Testimony with single-hop epistemic tools systematically underestimates the rate at which the original signal degrades along the chain.
