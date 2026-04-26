---
batch_name: custom-01-logical-fallacies
batch_date: 2026-04-26
default_domain: critical-thinking
default_confidence: high
notes: |
  Custom seeding batch 01: classical informal logical fallacies. Targets ghost
  links from existing argument-analysis and reasoning notes.
---

# Batch: Logical Fallacies

## Ad Hominem

- domain: critical-thinking
- secondary_domains: [logic, argumentation]
- aliases: [argumentum ad hominem, attack on the person]
- broader: [informal-fallacy]
- related: [genetic-fallacy, tu-quoque, principle-of-charity, argument-analysis]
- prerequisites: [argument-analysis]
- confidence: high

**definition**: An Ad Hominem fallacy occurs when a critic responds to an argument by attacking a property or motive of the person making the argument rather than engaging with the argument's content, treating an irrelevant feature of the speaker as if it bore on the truth of the conclusion.

**key_claim**: Ad Hominem reasoning is fallacious because the credibility, character, or motives of an arguer are logically independent of whether their premises support their conclusion; identifying a flawed messenger never substitutes for identifying a flawed inference.

**warning**: Ad Hominem is often misapplied to any negative statement about a person, but pointing out that an arguer is biased, lying, or unqualified is not Ad Hominem when their reliability is itself the relevant question — for instance in eyewitness testimony or expert appeals.

## Appeal to Authority

- domain: critical-thinking
- secondary_domains: [logic, epistemology]
- aliases: [argumentum ad verecundiam, argument from authority]
- broader: [informal-fallacy]
- related: [expert-testimony, ad-hominem, epistemic-autonomy, principle-of-charity]
- prerequisites: [argument-analysis]
- confidence: high

**definition**: Appeal to Authority is the inferential pattern in which the truth of a claim is supposed to follow from the fact that an authority asserts it; the move becomes a fallacy when the cited authority is irrelevant, unreliable, or speaking outside their domain of competence.

**key_claim**: Appeal to Authority is not fallacious in itself — non-experts must defer to legitimate expertise to function — but becomes fallacious when the appeal substitutes for the reasoning the authority would themselves use, transferring epistemic weight without transferring epistemic justification.

**warning**: Treating every Appeal to Authority as illegitimate produces a corrosive scepticism that confuses personal verification with epistemic warrant; the relevant test is calibration of the authority to the question, not the bare fact that an authority was cited.

## Circular Reasoning

- domain: critical-thinking
- secondary_domains: [logic]
- aliases: [petitio principii, begging the question]
- broader: [informal-fallacy]
- related: [argument-analysis, principle-of-charity, modus-ponens]
- prerequisites: [argument-analysis]
- confidence: high

**definition**: Circular Reasoning is an argumentative pattern in which the conclusion is presupposed — explicitly or covertly — by one of the premises, so that the argument does no inferential work even though it may have the surface form of a deduction.

**key_claim**: Circular Reasoning fails not because it is invalid (it is in fact trivially valid) but because it provides no rational basis for accepting the conclusion that is independent of already accepting it, defeating the purpose of giving an argument at all.

**warning**: Circular Reasoning is easy to disguise through paraphrase, synonym substitution, or distance between premise and conclusion; spotting it reliably requires reconstructing the argument in normal form rather than judging it from its surface presentation.

## Conjunction Fallacy

- domain: cognitive-psychology
- secondary_domains: [judgment-and-decision-making, probability]
- aliases: [Linda problem]
- broader: [representativeness-heuristic, cognitive-bias]
- related: [base-rate-neglect, probability-judgment, representativeness-heuristic]
- prerequisites: [probability]
- confidence: high

**definition**: The Conjunction Fallacy is the empirically robust judgment error in which people rate a conjunctive event "A and B" as more probable than a constituent event "A" alone, violating the basic axiom of probability that the probability of a conjunction can never exceed the probability of either conjunct.

**key_claim**: The Conjunction Fallacy demonstrates that intuitive probability judgments are dominated by representativeness — how well a description fits a stereotype — rather than by extensional logic, and the bias survives explicit training in elementary probability.

**warning**: The Conjunction Fallacy is sometimes dismissed as a mere wording artefact, but it persists across between-subjects designs, monetary incentives, and statistically sophisticated samples, indicating a genuine deviation from coherent probabilistic reasoning rather than a comprehension failure.

## False Dichotomy

- domain: critical-thinking
- secondary_domains: [logic, rhetoric]
- aliases: [false dilemma, either-or fallacy, black-and-white thinking]
- broader: [informal-fallacy]
- related: [straw-man-fallacy, principle-of-charity, argument-analysis]
- prerequisites: [argument-analysis]
- confidence: high

**definition**: A False Dichotomy is presented when an argument frames a question as having exactly two mutually exclusive options, when in fact the option space is larger or contains overlap, forcing the audience to accept one undesirable side by suppressing genuine alternatives.

**key_claim**: False Dichotomy is rhetorically powerful because it converts a substantive question about the structure of the option space into a forced choice between two named alternatives, smuggling in the unstated premise that the framing itself is exhaustive.

**warning**: Not every either-or framing is a False Dichotomy — many real choices are genuinely binary — so the diagnosis requires showing the existence of a third option that the framing illegitimately excluded, not merely asserting that "things are more complicated."

## Gamblers Fallacy

- domain: cognitive-psychology
- secondary_domains: [judgment-and-decision-making, probability]
- aliases: [Monte Carlo fallacy, fallacy of the maturity of chances]
- broader: [cognitive-bias, representativeness-heuristic]
- related: [hot-hand-fallacy, conjunction-fallacy, law-of-small-numbers]
- prerequisites: [probability]
- confidence: high

**definition**: The Gamblers Fallacy is the mistaken belief that, in a sequence of independent random events, an outcome that has not occurred for a while becomes more likely on the next trial — as if the underlying process "owed" balance to the recent run.

**key_claim**: The Gamblers Fallacy arises because intuition treats short random sequences as if they should locally mirror the long-run distribution; the heuristic confuses representativeness of the sample with statistical independence of its elements.

**warning**: The Gamblers Fallacy is often confused with its inverse, the hot-hand fallacy; the two are opposite errors about the same underlying ignorance of independence, and combating one without the other can simply switch a person from one bias to the other.

## Slippery Slope Fallacy

- domain: critical-thinking
- secondary_domains: [logic, argumentation, rhetoric]
- aliases: [slippery-slope argument, camel's nose argument]
- broader: [informal-fallacy]
- related: [false-dichotomy, argument-analysis, causal-reasoning]
- prerequisites: [argument-analysis, causal-reasoning]
- confidence: high

**definition**: The Slippery Slope Fallacy is committed when an argument claims that a relatively modest first step will inevitably lead to a chain of progressively worse outcomes, without supplying the causal or probabilistic warrant that each transition in the chain actually follows from the previous one.

**key_claim**: The Slippery Slope Fallacy is fallacious not because chain arguments are inherently bad — many are sound — but because the rhetorical version multiplies low-probability transitions and presents the joint probability as if it were near-certain, obscuring the compounding of uncertainty.

**warning**: Dismissing every chain-of-consequences argument as a Slippery Slope Fallacy is itself an error; the legitimate diagnosis requires showing that at least one transition in the predicted chain lacks a defensible causal mechanism, not merely that the chain is long.

## Straw Man Fallacy

- domain: critical-thinking
- secondary_domains: [logic, argumentation, rhetoric]
- aliases: [straw man, straw-person argument]
- broader: [informal-fallacy]
- related: [principle-of-charity, false-dichotomy, ad-hominem, argument-analysis]
- prerequisites: [argument-analysis]
- confidence: high

**definition**: The Straw Man Fallacy occurs when an arguer responds not to their opponent's actual position but to a distorted, weakened, or caricatured version of it that is easier to refute, then claims victory over the original view by defeating the substitute.

**key_claim**: The Straw Man Fallacy persists because attacking a weakened version of an opponent's position is rhetorically efficient and emotionally satisfying, even though it fails the basic dialectical obligation to engage the strongest available form of the opposing view.

**warning**: Diagnosing a Straw Man Fallacy requires the diagnostician to first reconstruct the opponent's actual argument fairly; otherwise the accusation of straw-manning becomes itself a straw-manning move, used to dismiss critique without engagement.
