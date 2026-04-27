---
batch_name: decision-science-and-cognitive-inference
batch_date: 2026-04-27
default_domain: cognitive-science
default_confidence: high
notes: |
  Closes 10 high-payoff ghost wiki-links in the decision-science /
  behavioural-economics / predictive-inference cluster. Each proposed
  term is referenced 6-20 times across existing v6 permanent notes and
  has obvious sibling concepts already in the graph (prospect-theory,
  loss-aversion, dual-process-theory, heuristics-and-biases, free-energy-
  principle, etc.). Selection prioritises edges that close from many
  source notes simultaneously (decision-science alone closes 20 edges).
---

# Batch: Decision Science & Cognitive Inference

## Decision Science

- domain: cognitive-science
- secondary_domains: [behavioral-economics, judgment-and-decision-making]
- aliases: [judgment and decision making, JDM]
- broader: [cognitive-science]
- narrower: [behavioral-economics, prospect-theory, expected-utility-theory]
- related: [bounded-rationality, heuristics-and-biases, dual-process-theory, satisficing, cognitive-bias]
- prerequisites: [probability-judgment, mental-model]
- confidence: high

**definition**: Decision Science is the interdisciplinary study of how individuals and groups choose between alternatives under conditions of uncertainty, risk, and limited cognitive resources, integrating models from psychology, economics, statistics, and neuroscience to describe both how decisions are actually made and how they could be made more rationally.

**key_claim**: Decision Science treats human choice as a dual-natured phenomenon — simultaneously a normative problem (what *ought* one choose given preferences and beliefs) and a descriptive problem (what do people *actually* choose given cognitive constraints) — and most progress in the field has come from quantifying the systematic gap between the two.

**warning**: Decision Science is frequently collapsed into "behavioral economics," but the field is broader: it includes naturalistic-decision-making research on expert intuition, neuroeconomic work on valuation circuitry, and prescriptive engineering of choice architectures, none of which reduce to the heuristics-and-biases program alone.

## Behavioral Economics

- domain: behavioral-economics
- secondary_domains: [cognitive-science, decision-science]
- aliases: [behavioural economics]
- broader: [decision-science]
- related: [prospect-theory, loss-aversion, hyperbolic-discounting, bounded-rationality, heuristics-and-biases, dual-process-theory, framing-effect, endowment-effect, status-quo-bias]
- prerequisites: [expected-utility-theory, cognitive-bias]
- confidence: high

**definition**: Behavioral Economics is the branch of economics that integrates psychological findings about cognition, emotion, and social context into models of economic decision-making, replacing the idealised rational agent of classical theory with empirically constrained accounts of how real people value, choose, and exchange.

**key_claim**: Behavioral Economics establishes that systematic, predictable departures from expected-utility maximisation — loss aversion, reference dependence, hyperbolic discounting, framing sensitivity — are not noise around a rational mean but stable features of human choice that any descriptive economic model must accommodate.

**warning**: Behavioral Economics is often misread as a wholesale refutation of rational-choice theory; in practice it functions as a *correction layer* on top of utility theory, identifying boundary conditions where the rational model fails rather than discarding optimisation as an analytic frame.

## Probability Judgment

- domain: cognitive-science
- secondary_domains: [decision-science, statistics]
- aliases: [subjective probability, probabilistic reasoning]
- broader: [reasoning-under-uncertainty, decision-science]
- related: [bayesian-reasoning, base-rate-neglect, conjunction-fallacy, representativeness-heuristic, availability-heuristic, gamblers-fallacy, anchoring-bias, calibration]
- prerequisites: [bayesian-reasoning, cognitive-bias]
- confidence: high

**definition**: Probability Judgment is the cognitive process by which people assign degrees of belief to uncertain events and update those beliefs in light of evidence, encompassing both the formal Bayesian benchmark and the heuristic shortcuts that humans actually deploy when statistical computation is intractable in real time.

**key_claim**: Research on Probability Judgment shows that human estimates of likelihood are systematically miscalibrated in patterned ways — over-weighting vivid or recent evidence, neglecting base rates, and committing the conjunction fallacy — and that these errors are not eliminated by domain expertise unless feedback environments are explicitly designed to surface them.

**warning**: Probability Judgment errors are often described as irrationality, but several "errors" in the laboratory turn out to be ecologically rational responses to real-world frequency distributions; treating every deviation from Bayes as a defect risks training people out of useful adaptive heuristics.

## Reference Dependence

- domain: behavioral-economics
- secondary_domains: [cognitive-science, decision-science]
- aliases: [reference-point dependence]
- broader: [prospect-theory, behavioral-economics]
- related: [loss-aversion, framing-effect, endowment-effect, anchoring-bias, status-quo-bias, mental-accounting, prospect-theory]
- prerequisites: [prospect-theory, expected-utility-theory]
- confidence: high

**definition**: Reference Dependence is the principle, central to prospect theory, that people evaluate outcomes not in terms of absolute final wealth or states but in terms of gains and losses relative to a salient reference point, which may be the status quo, an aspiration level, a recent experience, or a socially supplied benchmark.

**key_claim**: Reference Dependence explains why the same objective outcome can be experienced as a gain or a loss depending purely on framing and recent history — because the brain encodes value as change from a reference rather than as level — and this re-coding is upstream of loss aversion, the endowment effect, and a wide range of framing effects.

**warning**: Reference Dependence is often discussed as if the reference point were fixed and obvious, but choosing the operative reference is itself a contested empirical question; the literature contains genuine ambiguity about whether the reference point is the status quo, a forecast, an aspiration, or a constructed mental representation, and conclusions about loss aversion can shift accordingly.

## Predictive Coding

- domain: neuroscience
- secondary_domains: [cognitive-science, computational-neuroscience]
- aliases: [predictive coding theory]
- broader: [predictive-processing, free-energy-principle]
- narrower: [active-inference]
- related: [bayesian-brain, free-energy-principle, predictive-processing, active-inference, perceptual-load-theory, attention-and-cognitive-control]
- prerequisites: [bayesian-reasoning, neuroplasticity]
- confidence: high

**definition**: Predictive Coding is a neurocomputational framework proposing that the brain continuously generates top-down predictions about its incoming sensory input and propagates only the prediction-error — the unexplained residual — up the cortical hierarchy, so that perception and learning are organised around the minimisation of surprise rather than the passive registration of stimuli.

**key_claim**: Predictive Coding inverts the classical bottom-up view of perception: rather than building percepts from sensory primitives, the cortex is held to issue prior expectations and update them only when prediction-error signals demand revision, which parsimoniously explains illusions, attentional gain control, and the energetic efficiency of cortical processing.

**warning**: Predictive Coding is sometimes treated as a settled neural mechanism, but the strongest evidence is computational and behavioural; the canonical cortical microcircuitry that implements prediction-error signalling — putatively superficial vs deep pyramidal cells — is still under active empirical investigation and should not be cited as established neuroanatomy.

## Bayesian Brain

- domain: neuroscience
- secondary_domains: [cognitive-science, computational-neuroscience]
- aliases: [Bayesian brain hypothesis]
- broader: [predictive-processing, free-energy-principle]
- related: [predictive-coding, active-inference, free-energy-principle, bayesian-reasoning, perceptual-load-theory, predictive-processing]
- prerequisites: [bayesian-reasoning, probability-judgment]
- confidence: high

**definition**: The Bayesian Brain hypothesis holds that the nervous system represents environmental causes probabilistically and updates those representations in approximate accordance with Bayes' rule, treating perception, motor control, and cognition as varieties of probabilistic inference performed over generative models of the world.

**key_claim**: The Bayesian Brain framework unifies disparate phenomena — multisensory integration weighted by reliability, cue combination in depth perception, sensorimotor adaptation, and even certain delusional symptoms — under a single computational principle: optimal combination of prior beliefs with likelihoods derived from sensory evidence.

**warning**: The Bayesian Brain hypothesis is sometimes interpreted as the claim that the brain literally computes posterior distributions; the more defensible reading is that neural dynamics *approximate* Bayesian inference under specific energetic and architectural constraints, and confusing the as-if formalism with a literal mechanism inflates explanatory claims beyond the evidence.

## Mental Simulation

- domain: cognitive-science
- secondary_domains: [decision-science, social-cognition]
- aliases: [simulation-based reasoning, mental scenario construction]
- broader: [mental-model, episodic-memory]
- related: [counterfactual-reasoning, prospective-memory, episodic-memory, theory-of-mind, mental-contrasting, woop-method, embodied-cognition, predictive-processing]
- prerequisites: [working-memory, mental-model]
- confidence: high

**definition**: Mental Simulation is the cognitive capacity to internally enact a course of events — perceptual, motor, social, or strategic — without overt action, allowing an agent to evaluate likely outcomes, rehearse procedures, take another's perspective, or compare alternatives before committing to a choice.

**key_claim**: Mental Simulation is the common substrate uniting episodic future-thinking, counterfactual reasoning, theory of mind, and motor imagery; converging neuroimaging evidence implicates a shared default-mode/hippocampal network, suggesting that "imagining," "remembering," and "modelling another mind" are surface variants of one underlying simulation engine.

**warning**: Mental Simulation can systematically distort decisions by oversampling vivid, available, or self-flattering scenarios; this is the mechanism behind the planning fallacy, optimism bias in forecasting, and the empathy gap, so the very capacity that enables foresight also seeds predictable forecasting errors.

## Self-Control

- domain: cognitive-science
- secondary_domains: [motivation-science, self-regulated-learning]
- aliases: [behavioral self-control]
- broader: [self-regulation, executive-function]
- narrower: [willpower, inhibitory-control]
- related: [willpower, self-regulation, executive-function, inhibitory-control, intention-behavior-gap, hyperbolic-discounting, implementation-intentions, temptation-bundling, habit-formation, ego-involvement]
- prerequisites: [executive-function, inhibitory-control]
- confidence: high

**definition**: Self-Control is the capacity to override an immediate impulse, prepotent response, or short-term reward in service of a more valued long-term goal, integrating attentional, inhibitory, and motivational mechanisms that together regulate behaviour across temporal distance.

**key_claim**: Contemporary research re-conceives Self-Control less as a single "willpower muscle" and more as a portfolio of strategies — situation selection, attentional deployment, cognitive reappraisal, and pre-commitment — with the most successful self-controllers being those who *avoid* needing in-the-moment effort by structuring their environment in advance.

**warning**: Self-Control is often equated with effortful inhibition in the moment, but this framing predicts exhaustion and failure; the strategic-portfolio view warns that over-relying on suppression at the point of temptation is the *least* effective form of Self-Control and a leading cause of repeated lapses.

## Willpower

- domain: cognitive-science
- secondary_domains: [motivation-science, self-regulated-learning]
- aliases: [volitional effort]
- broader: [self-control, self-regulation, volitional-control]
- related: [self-control, ego-involvement, intention-behavior-gap, implementation-intentions, hyperbolic-discounting, executive-function, inhibitory-control, action-control-theory, habit-formation]
- prerequisites: [self-regulation, executive-function]
- confidence: medium

**definition**: Willpower is the colloquial term for the effortful, conscious, in-the-moment deployment of self-control to resist a temptation, persist at an aversive task, or initiate a difficult action, classically modelled as a limited cognitive resource that is depleted by use and replenished by rest, glucose, or motivation.

**key_claim**: The strong form of the Willpower-as-depletable-resource hypothesis — ego depletion — has been substantially weakened by failed pre-registered replications, and the field has migrated toward motivational and belief-based accounts in which Willpower's apparent fatigue depends on the actor's theory of self-control rather than on a literal resource drain.

**warning**: Willpower is the wrong unit of analysis for most behaviour change because it locates the work at the point of temptation, where intervention is least effective; treating Willpower as the lever to pull predicts repeated failure and cultivates self-blame, whereas habit design, environment structuring, and implementation intentions move the leverage upstream.

## Diffusion of Responsibility

- domain: social-psychology
- secondary_domains: [cognitive-science, decision-science]
- aliases: [responsibility diffusion]
- broader: [social-cognition, social-influence]
- related: [bystander-effect, social-loafing, conformity, deindividuation, groupthink, obedience-to-authority, social-comparison-theory]
- prerequisites: [social-cognition]
- confidence: high

**definition**: Diffusion of Responsibility is the social-psychological phenomenon in which the felt obligation to act decreases as the number of co-present others increases, because each individual implicitly assumes that someone else will or should take responsibility, leading to weaker individual response than would obtain if any one person were alone.

**key_claim**: Diffusion of Responsibility is the most parsimonious mechanism behind the bystander effect and a major contributor to social loafing in collaborative tasks; experimentally, manipulations that re-individuate responsibility — naming a specific helper, reducing perceived group size, or assigning explicit roles — restore intervention rates almost to those observed in solo conditions.

**warning**: Diffusion of Responsibility is sometimes invoked as a complete explanation for bystander non-intervention, but pluralistic ignorance, evaluation apprehension, and ambiguity of the situation co-determine the outcome; treating diffusion as the sole mechanism oversimplifies both the empirical record and the design space for interventions.
