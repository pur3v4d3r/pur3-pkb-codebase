---
batch_name: 2026-04-25-batch-12-decision-science-and-habit
batch_date: 2026-04-25
default_domain: decision-science
default_confidence: high
notes: |
  Behavioral economics core (prospect theory, biases, choice architecture)
  + naturalistic decision-making + behavior-change/habit cluster. Seeds a
  substrate the metacognition / motivation / pedagogy notes already
  reference as ghost links.
---

# Batch: Decision Science, Behavioral Economics & Habit/Behavior Change

## Prospect Theory

- secondary_domains: [behavioral-economics, cognitive-psychology]
- aliases: [Kahneman-Tversky prospect theory]
- broader: [decision-under-uncertainty]
- related: [loss-aversion, expected-utility-theory, framing-effect, reference-dependence, kahneman-daniel, tversky-amos]
- prerequisites: [expected-utility-theory]

**definition**: Prospect Theory is the descriptive theory of decision under risk, developed by Kahneman and Tversky in 1979, in which people evaluate outcomes as *gains and losses relative to a reference point* rather than as final wealth states, weight probabilities non-linearly (overweighting small probabilities, underweighting moderate-to-large ones), and exhibit asymmetric sensitivity in which losses loom roughly twice as large as equivalent gains.

**key_claim**: Prospect Theory replaced expected-utility theory as the standard descriptive account of risky choice because it predicts a wide menu of robust anomalies — the certainty effect, the reflection effect, the isolation effect, framing reversals — with a single value-function-plus-weighting-function structure, where expected-utility theory required *post-hoc* exceptions for each.

**warning**: Prospect Theory is descriptive, not normative; using it to argue that loss-averse choices are "rational" or that expected-utility is "wrong" conflates two questions — Prospect Theory describes how people *do* choose, expected-utility describes how a coherent agent *should* choose, and the gap between them is the entire point.

## Loss Aversion

- secondary_domains: [behavioral-economics, cognitive-psychology]
- broader: [prospect-theory]
- related: [endowment-effect, status-quo-bias, sunk-cost-fallacy, framing-effect, reference-dependence]
- prerequisites: [prospect-theory]

**definition**: Loss Aversion is the empirical regularity, central to Prospect Theory, that the psychological pain of a loss of magnitude X exceeds the psychological pleasure of an equivalent gain of magnitude X by roughly a factor of two, producing systematic asymmetries in choice — risk aversion in the gain domain, risk seeking in the loss domain, and reluctance to accept fair gambles.

**key_claim**: Loss Aversion is the proximal cause of several economically consequential anomalies — the [[endowment-effect]] (people demand more to give up an item than they would pay to acquire it), [[status-quo-bias]], and the disposition effect in investing — making it one of the highest-yield single constructs in behavioral economics for explaining real-world choice.

**warning**: Loss Aversion has been challenged in recent meta-analyses as smaller and more context-sensitive than the canonical "2x" estimate suggests; treating Loss Aversion as a fixed psychological constant — rather than a parameter that varies with stakes, framing, and population — is a form of pseudo-precision the original literature does not actually support.

## Hyperbolic Discounting

- secondary_domains: [behavioral-economics, neuroeconomics]
- aliases: [present-biased preferences]
- broader: [intertemporal-choice]
- related: [present-bias, exponential-discounting, time-preference, delay-discounting, akrasia, self-control]
- prerequisites: [intertemporal-choice]

**definition**: Hyperbolic Discounting is the empirical pattern in which the subjective value of a future reward declines steeply over short delays and then much more gradually over long ones — fitting a hyperbolic rather than exponential function — producing preference reversals: an agent prefers $110 in 31 days over $100 in 30 days, but prefers $100 today over $110 tomorrow.

**key_claim**: Hyperbolic Discounting formally predicts time-inconsistent preferences and is the leading mathematical account of self-control failures, procrastination, and addictive choice; the preference reversals it generates are not noise but a structural consequence of the discount function's shape, which is why exponential-discounting models systematically underpredict these failures.

**warning**: Hyperbolic Discounting is sometimes invoked to argue that humans are "irrational" about the future; the more careful claim is that hyperbolic discounting is *time-inconsistent* with respect to a single agent's own earlier preferences — the agent at t=0 disagrees with the agent at t=29 — which is a coordination problem across temporal selves rather than a defect in any single decision.

## Present Bias

- secondary_domains: [behavioral-economics, self-regulation]
- aliases: [immediacy bias]
- broader: [hyperbolic-discounting]
- related: [hyperbolic-discounting, akrasia, self-control, implementation-intention, commitment-device]
- prerequisites: [hyperbolic-discounting]

**definition**: Present Bias is the asymmetric weighting of immediate versus delayed payoffs in which the *present moment* receives an extra premium beyond what any smooth time-discount function would predict, producing a sharp discontinuity between "now" and "any future at all" that is responsible for much of the predictive power of quasi-hyperbolic (β-δ) discounting models.

**key_claim**: Present Bias predicts that people will rationally pre-commit against their future selves — joining gym memberships they will resent, locking savings into illiquid accounts, deleting apps from phones — because they correctly anticipate that their future self will reweight the immediate moment in ways their current self disapproves of; this is the empirical basis of [[commitment-device]] design.

**warning**: Present Bias is sometimes confused with simple impatience; the distinguishing diagnostic is *preference reversal* — an impatient but time-consistent agent will not change ranking as the decision moment approaches, but a present-biased one will, and only the present-biased pattern licenses the welfare-improving role of commitment devices.

## Status Quo Bias

- secondary_domains: [behavioral-economics, choice-architecture]
- broader: [decision-biases]
- related: [loss-aversion, endowment-effect, default-effect, choice-architecture, nudge-theory, omission-bias]
- prerequisites: [loss-aversion]

**definition**: Status Quo Bias is the tendency to disproportionately prefer the current state of affairs over alternatives, even when the alternatives would be chosen if the current state were not labelled as default — a pattern most cleanly demonstrated in default-option experiments where simply changing which option is pre-selected produces large shifts in chosen behavior.

**key_claim**: Status Quo Bias is an emergent consequence of [[loss-aversion]] applied to a moving reference point: the current state becomes the reference, deviations are coded as losses (which are weighted more heavily than the foregone gains of switching), so the asymmetry shows up as inertia even when the switch is materially attractive.

**warning**: Status Quo Bias is sometimes equated with "laziness" or "irrationality"; in many contexts it is a sensible heuristic — defaults often encode accumulated wisdom, and switching costs are real — so the bias is best framed as systematic deviation from indifference, not as a defect to be eliminated wherever it appears.

## Choice Architecture

- secondary_domains: [behavioral-economics, public-policy, design]
- aliases: [decision architecture]
- broader: [behavioral-economics]
- related: [nudge-theory, default-effect, status-quo-bias, libertarian-paternalism, thaler-richard, sunstein-cass]
- prerequisites: [decision-biases]

**definition**: Choice Architecture is the deliberate design of the context in which decisions are made — the ordering and framing of options, the choice of defaults, the salience of information, the presence or absence of friction — recognizing that there is no neutral way to present a choice and that the architect's design choices systematically shape what is chosen, regardless of intent.

**key_claim**: Choice Architecture establishes that "letting people choose freely" is a coherent principle only relative to a specific architecture; since *some* architecture must exist, the question is not whether to influence choice but which influence to exert, which reframes paternalism from an on/off switch into a design dimension to be argued explicitly rather than denied.

**warning**: Choice Architecture is sometimes presented as costless behavior change; in practice, choice-architecture interventions can backfire when defaults conflict with strong preferences, when the architect misjudges which option is "in the chooser's interest," or when transparency about the architecture undermines its effect — none of which appear in the simplified policy-paper version of the concept.

## Nudge Theory

- secondary_domains: [public-policy, behavioral-economics]
- aliases: [libertarian paternalism]
- broader: [choice-architecture]
- related: [choice-architecture, default-effect, status-quo-bias, thaler-richard, sunstein-cass, behavioral-public-policy]
- prerequisites: [choice-architecture]

**definition**: Nudge Theory, developed by Thaler and Sunstein, is the policy framework that uses small, low-cost, freedom-preserving modifications to choice architecture — opt-out organ donation, default retirement-savings enrollment, salience changes on cafeteria layouts — to steer behavior toward outcomes the chooser would, on reflection, endorse, without restricting the option set or imposing material penalties.

**key_claim**: Nudge Theory's central wager is that population-level behavior can be shifted at scale by interventions whose marginal cost approaches zero, because the existing architecture is already steering choice — switching from a default-no-enrollment to default-yes-enrollment for retirement savings produces multi-percentage-point shifts in participation that incentive-based reforms struggle to match.

**warning**: Nudge Theory has drawn criticism that "small" interventions accumulate into substantial paternalism, that nudges work because they exploit cognitive limitations the citizen has not endorsed, and that effect sizes shrink in pre-registered replications; treating nudges as a universal substitute for incentives or regulation overstates what the evidence supports.

## Satisficing

- secondary_domains: [decision-science, bounded-rationality]
- broader: [bounded-rationality]
- related: [bounded-rationality, heuristics-and-biases, optimization, simon-herbert, fast-and-frugal-heuristics]
- prerequisites: [bounded-rationality]

**definition**: Satisficing, coined by Herbert Simon, is the decision strategy of searching alternatives sequentially and stopping at the first option that meets a pre-specified aspiration level — "good enough" — rather than enumerating the full option set and selecting the global maximum, which is computationally infeasible under realistic time and information constraints.

**key_claim**: Satisficing is not a degraded form of optimization but a *different* solution concept appropriate to environments where the option set is open-ended, evaluation is costly, and time is bounded; in these conditions, satisficing strategies routinely outperform optimization attempts, because the cost of continued search exceeds the expected value of marginal improvement.

**warning**: Satisficing is sometimes treated as synonymous with "settling" or laziness; the original construct presupposes a *deliberate* aspiration level chosen with full awareness of the trade-off, and Satisficing without an articulated aspiration collapses into impulsive acceptance — which is a different failure mode that bounded rationality literature does not endorse.

## Recognition Primed Decision Model

- secondary_domains: [naturalistic-decision-making, expertise-research]
- aliases: [RPD model]
- broader: [naturalistic-decision-making]
- related: [naturalistic-decision-making, expertise, mental-simulation, klein-gary, intuition, pattern-recognition]
- prerequisites: [naturalistic-decision-making]

**definition**: The Recognition Primed Decision Model, developed by Gary Klein, is an account of how experts make rapid decisions in time-pressured, ambiguous, high-stakes settings (firefighters, emergency-room physicians, military commanders) — through *recognition* of the situation as a typical case, retrieval of an associated course of action, and mental *simulation* of that action's likely outcome before commitment, rather than comparison of multiple options.

**key_claim**: The Recognition Primed Decision Model dissolves the apparent contradiction between expert intuition and "rational" decision-making by showing that experts compress option-comparison into pattern-matching against a vast library of cases, and validate their first candidate via mental simulation — which is why expert decisions look both fast and sound while novices need explicit comparison to approximate the same outcome.

**warning**: The Recognition Primed Decision Model is calibrated to *high-validity environments* where pattern-feedback is rapid and reliable; in low-validity environments (long-range geopolitical forecasting, stock picking) the same pattern-matching machinery generates confident but unreliable judgments, so transferring the RPD model out of its evidential home is a documented source of overconfident expert error.

## Naturalistic Decision Making

- secondary_domains: [decision-science, expertise-research, applied-cognitive-psychology]
- aliases: [NDM]
- broader: [decision-science]
- related: [recognition-primed-decision-model, expertise, situation-awareness, klein-gary, ecological-rationality, fast-and-frugal-heuristics]
- prerequisites: [decision-science]

**definition**: Naturalistic Decision Making is the research program studying how experienced practitioners actually make decisions in real-world settings characterized by time pressure, high stakes, ill-defined goals, dynamic conditions, and incomplete information — distinct from classical decision theory by virtue of its descriptive fieldwork orientation and its focus on expertise rather than population-average choice.

**key_claim**: Naturalistic Decision Making demonstrated empirically that expert decision-making in field settings does not look like the option-comparison procedures classical decision theory prescribes; instead it relies on situation assessment, mental simulation, and recognition-driven action selection, which forced classical decision theory to acknowledge a domain where its prescriptions are descriptively wrong and arguably normatively unhelpful.

**warning**: Naturalistic Decision Making findings should not be over-extrapolated to *all* expert judgment; the program's strongest evidence comes from domains where experts get rapid, unambiguous feedback (firefighting, chess), and Daniel Kahneman's collaboration with Gary Klein explicitly delimited where expert intuition is and isn't trustworthy — Naturalistic Decision Making's prescriptions need to be paired with that boundary condition to avoid licensing intuition in unsuitable domains.

## Habit Loop

- domain: behavior-change
- secondary_domains: [behavioral-psychology, neuroscience]
- aliases: [cue-routine-reward loop]
- broader: [habit-formation]
- related: [behavior-change-techniques, implementation-intention, temptation-bundling, cue-reactivity, basal-ganglia, dopamine]
- prerequisites: [habit-formation]

**definition**: The Habit Loop is the three-component cycle — *cue* (a triggering context or stimulus), *routine* (the automatized behavior), *reward* (the outcome that reinforces the cue→routine link) — popularized by Charles Duhigg and grounded in basal-ganglia research on stimulus-response learning, that describes how a deliberate behavior becomes a context-cued automatic response over repetition.

**key_claim**: The Habit Loop predicts that durable behavior change is easier when the *cue* is engineered (consistent context, time-of-day, location anchor) and the *reward* is immediate and reliably linked to the routine; attempts to change the routine without cue-engineering or reward redesign tend to fail because the existing loop's reinforcement structure remains intact.

**warning**: The Habit Loop is a useful simplification but understates the role of *goals* and *motivation* in flexible everyday behavior; treating all behavior change as habit-engineering misses that many target behaviors are goal-directed rather than habitual, and the cue-routine-reward framing applied to genuinely goal-directed action systematically misallocates the change effort.

## Transtheoretical Model

- domain: behavior-change
- secondary_domains: [health-psychology, clinical-psychology]
- aliases: [stages of change, TTM]
- broader: [behavior-change-models]
- related: [behavior-change-techniques, motivational-interviewing, self-efficacy, prochaska-james]
- prerequisites: [behavior-change]

**definition**: The Transtheoretical Model, developed by Prochaska and DiClemente, describes intentional behavior change as movement through six stages — precontemplation, contemplation, preparation, action, maintenance, termination — with stage-matched processes of change (consciousness raising, self-reevaluation, stimulus control, reinforcement management) that predict which intervention is appropriate for a given person at a given moment.

**key_claim**: The Transtheoretical Model claims that mismatched stage-process pairings explain a large share of intervention failure: pushing action-stage techniques (goal-setting, contingency management) onto a precontemplation-stage person produces resistance rather than change, while contemplation-stage techniques (consciousness raising) on someone already in action wastes the action window.

**warning**: The Transtheoretical Model has weakened in the meta-analytic record over the past two decades — stage assessment is unreliable, stage-matched interventions often fail to outperform stage-unmatched ones, and the discrete-stage assumption may misrepresent what is in fact a continuous process; citing the Transtheoretical Model as established science without acknowledging this evidence base is increasingly unsupportable.

## Behavior Change Techniques

- domain: behavior-change
- secondary_domains: [health-psychology, intervention-design]
- aliases: [BCTs, BCT taxonomy]
- broader: [behavior-change]
- related: [habit-loop, transtheoretical-model, implementation-intention, self-monitoring, michie-susan, behaviour-change-wheel]
- prerequisites: [behavior-change]

**definition**: Behavior Change Techniques (BCTs) are the catalogued, atomic ingredients of behavior-change interventions — goal setting, action planning, self-monitoring, social comparison, prompts, contingency management — formalized by Susan Michie and colleagues into a 93-item taxonomy (BCT Taxonomy v1) so that interventions can be described, replicated, and meta-analyzed at the level of mechanism rather than vague brand name.

**key_claim**: Behavior Change Techniques as a taxonomy made the intervention literature analyzable: instead of comparing "intervention A" against "intervention B" as opaque packages, researchers can decompose each into its BCT components and identify which specific techniques drive the effect — a methodological advance that has surfaced replicable mechanism-level findings (e.g., self-monitoring + feedback) and discredited weakly-supported ones.

**warning**: Behavior Change Techniques are often invoked as interchangeable "active ingredients"; in practice their effects are highly context-dependent and interaction-laden — self-monitoring helps motivated participants and can demoralize discouraged ones — so picking BCTs from the menu without theoretical grounding for the target behavior, population, and context routinely produces null intervention results.

## Temptation Bundling

- domain: behavior-change
- secondary_domains: [behavioral-economics, self-regulation]
- broader: [behavior-change-techniques]
- related: [implementation-intention, commitment-device, present-bias, hyperbolic-discounting, milkman-katy]
- prerequisites: [behavior-change-techniques]

**definition**: Temptation Bundling, named and tested by Katy Milkman, is the self-control strategy of pairing an instantly gratifying activity that is easy to overconsume (binge-watching a series, listening to a beloved podcast) exclusively with an aversive but valuable activity (gym workouts, household chores) so that access to the temptation requires engaging in the should-do behavior.

**key_claim**: Temptation Bundling is one of the few self-control strategies with experimental evidence for genuine, not just self-reported, behavior change: in the original gym-and-audiobook study, the bundled-treatment group's gym attendance rose substantially over no-treatment controls, demonstrating that the want/should asymmetry can be re-engineered rather than just willed away.

**warning**: Temptation Bundling depends on the temptation remaining genuinely tempting and the should-do remaining tolerable while bundled; the strategy degrades when the temptation loses novelty or the should-do becomes acutely aversive, and treating Temptation Bundling as a permanent fix rather than a periodically-refreshed scaffold is the documented reason most bundling habits decay within months.
