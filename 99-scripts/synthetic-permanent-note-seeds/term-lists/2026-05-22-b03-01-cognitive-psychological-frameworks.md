---
batch_name: b03-01-cognitive-psychological-frameworks
batch_date: 2026-05-22
default_domain: cognitive-science-applied-to-llms
default_confidence: high
notes: |
  Fifteen concepts applying cognitive and psychological frameworks to LLMs.
  Covers dual-process theory, cognitive biases (anchoring, availability,
  framing, representativeness, confirmation, base-rate neglect,
  Dunning-Kruger analog, social desirability, authority, bandwagon),
  loss aversion analog, hindsight bias, and primacy-recency effects as
  they manifest in LLM outputs and reasoning. Batch 03 of the
  prompt-engineering and LLM series.
---

# Batch: B03-01 Cognitive and Psychological Frameworks Applied to LLMs

## Dual Process Theory Applied to LLMs

- secondary_domains: [large-language-models, cognitive-psychology, prompt-engineering]
- aliases: [System 1 and System 2 in LLMs, fast-and-slow thinking in LLMs, dual-system reasoning in transformers]
- broader: [cognitive-psychology, large-language-models, reasoning-in-llms]
- narrower: [chain-of-thought-prompting, slow-thinking-prompting]
- related: [cognitive-bias-in-llm-outputs, chain-of-thought-prompting, system-2-prompting, deliberate-reasoning-prompting]
- prerequisites: [dual-process-theory, large-language-models, transformer-architecture]
- confidence: high

**definition**: Dual Process Theory Applied to LLMs is the application of Kahneman's dual-process cognitive framework — which distinguishes between fast, automatic, heuristic-driven System 1 reasoning and slow, deliberate, rule-governed System 2 reasoning — to the behaviour of large language models. In this framing, token-by-token autoregressive generation that relies on surface-form pattern completion corresponds to System 1-like processing, while chain-of-thought prompting, scratchpad reasoning, and extended deliberation prompts elicit System 2-like behaviour by forcing the model to decompose problems step-by-step before committing to an answer. The framework provides a theoretical lens for explaining why LLMs often produce confident but incorrect one-shot answers on tasks requiring multi-step reasoning, and why prompting strategies that slow down generation and make reasoning explicit yield dramatic accuracy improvements.

**key_claim**: Dual Process Theory Applied to LLMs predicts that LLM errors on multi-step reasoning tasks are disproportionately caused by System 1-like pattern completion overriding the need for deliberate reasoning, and that any prompting strategy that introduces an explicit reasoning phase — chain-of-thought, scratchpad, wait-and-think tokens, or task decomposition — functions as a System 2 elicitation mechanism that improves accuracy by preventing premature commitment to a System 1 response; this dual-process lens unifies a broad range of prompting improvements under a single theoretical framework.

**warning**: Dual Process Theory Applied to LLMs is a productive analogy but not a mechanistic description — LLMs do not literally implement two distinct processing systems, and the mapping from System 1/2 to transformer components is metaphorical rather than architectural; researchers who treat the analogy as a precise computational theory risk misinterpreting empirical results, such as attributing all reasoning errors to "System 1 failures" when the actual cause may be training data distribution, prompt format, or context window limitations.

## Cognitive Bias in LLM Outputs

- secondary_domains: [large-language-models, cognitive-psychology, prompt-engineering, ai-safety]
- aliases: [LLM biases, systematic errors in LLMs, cognitive distortions in AI outputs]
- broader: [cognitive-psychology, large-language-models, alignment]
- narrower: [anchoring-bias-in-llm-reasoning, availability-heuristic-in-llms, framing-effects-on-llm-outputs, confirmation-bias-in-chain-of-thought, social-desirability-bias-in-llms]
- related: [dual-process-theory-applied-to-llms, sycophancy-in-llms, hallucination-in-llms, prompt-brittleness]
- prerequisites: [cognitive-bias, large-language-models, in-context-learning]
- confidence: high

**definition**: Cognitive Bias in LLM Outputs refers to the systematic, predictable patterns of deviation from rational inference that appear in the responses of large language models, mirroring the cognitive biases identified in human judgment and decision-making research. These biases arise primarily from the statistical regularities in training data — LLMs learn to reproduce the biased reasoning patterns, heuristic shortcuts, and distorted judgments present in human-generated text — and are further amplified or suppressed by RLHF alignment, prompt framing, and context construction. Cognitive biases in LLM outputs manifest as anchoring effects, availability-driven over-representation of memorable events, framing-sensitive opinion shifts, confirmation-seeking responses, and social desirability distortions, among others, producing outputs that appear confident but systematically diverge from well-calibrated inference.

**key_claim**: Cognitive Bias in LLM Outputs is not merely a superficial mimicry of human language patterns but reflects deep structural parallels in how LLMs and humans process information under uncertainty — both systems use statistical regularities (base rates in human memory, training frequency in LLMs) as implicit priors, and both exhibit similar sensitivity to framing, anchoring, and social context, suggesting that many LLM biases are mathematically analogous to human cognitive biases rather than coincidentally similar; this structural analogy enables cognitive psychology's debiasing literature to inform LLM prompt engineering strategies.

**warning**: Cognitive Bias in LLM Outputs is not a stable, cataloguable list of fixed error modes — bias expression is highly sensitive to model architecture, scale, training data, RLHF tuning, prompt format, and context, meaning that a bias prominently documented in one model version may be substantially reduced or absent in another; practitioners who rely on static bias documentation without validating bias presence on their specific model and deployment configuration risk both over-correcting for biases that do not apply and missing active biases not covered in available documentation.

## Anchoring Bias in LLM Reasoning

- secondary_domains: [large-language-models, cognitive-psychology, prompt-engineering]
- aliases: [anchor effects in LLMs, numerical anchoring in AI, priming-by-number in LLMs]
- broader: [cognitive-bias-in-llm-outputs, anchoring-bias, large-language-models]
- related: [primacy-and-recency-effects-in-context, framing-effects-on-llm-outputs, order-sensitivity-in-few-shot, context-window-management]
- prerequisites: [anchoring-bias, large-language-models, in-context-learning]
- confidence: high

**definition**: Anchoring Bias in LLM Reasoning is the tendency of large language models to over-weight an initial numerical value, estimate, or reference point presented in the prompt when generating subsequent numerical judgments or estimates, producing outputs that are systematically pulled toward the anchor even when the anchor is arbitrary, irrelevant, or explicitly identified as incorrect. Anchoring bias in LLMs manifests when a prompt supplies a numerical reference — such as "a colleague estimated this at 80%" — and the model's own estimate gravitates disproportionately toward 80%, or when few-shot examples with extreme values skew the model's output distribution toward those values. The bias is particularly problematic in tasks requiring independent numerical estimation (cost prediction, probability assessment, rate estimation) where anchoring by in-context examples or initial prompt framing can introduce systematic error into outputs that appear precisely calibrated.

**key_claim**: Anchoring Bias in LLM Reasoning is reproducibly demonstrated in controlled experiments where models shown prompts with high versus low numerical anchors produce estimates that differ by substantially more than the anchor's informational content warrants — a finding that has direct practical consequences for applications like cost estimation, risk assessment, and survey response generation, where anchored estimates may be mistaken for independently-derived model judgments; debiasing strategies such as instructing the model to reason from first principles before consulting the context, or using zero-shot prompting for numerical estimation tasks, partially reduce but do not eliminate the bias.

**warning**: Anchoring Bias in LLM Reasoning is not limited to explicit numerical anchors — any prominent early value in the context, including non-numerical reference frames, categorical labels, or example outputs in few-shot prompts, can function as an anchor that distorts subsequent reasoning; practitioners who focus exclusively on numerical anchoring prevention while ignoring the anchoring effects of few-shot example selection, seed text, or early context framing will miss the dominant anchoring channels in typical production deployments.

## Availability Heuristic in LLMs

- secondary_domains: [large-language-models, cognitive-psychology, prompt-engineering]
- aliases: [availability bias in LLMs, frequency estimation bias in LLMs, salience-driven frequency distortion]
- broader: [cognitive-bias-in-llm-outputs, availability-heuristic, large-language-models]
- related: [anchoring-bias-in-llm-reasoning, overconfidence-in-llm-outputs, hallucination-in-llms, training-data-influence]
- prerequisites: [availability-heuristic, large-language-models, pretraining-data-influence]
- confidence: high

**definition**: The Availability Heuristic in LLMs refers to the tendency of large language models to estimate the probability or frequency of events, facts, or concepts based on how easily examples of those events come to mind in their training data — analogous to the human cognitive availability heuristic, in which ease of recall drives frequency and probability estimates. In LLMs, training data frequency functions as a proxy for cognitive accessibility: topics, claims, and entities that appear frequently or prominently in pretraining corpora are treated as more probable, more representative, and more important than their actual base rates would warrant. This manifests as LLMs overestimating the prevalence of highly publicised events, over-representing well-documented claims from high-frequency training domains, and underestimating the probability of rare but real phenomena that appear infrequently in text data.

**key_claim**: The Availability Heuristic in LLMs produces systematic over-representation of high-frequency training corpus events and under-representation of low-frequency but real phenomena in LLM probabilistic outputs — a bias that is structurally impossible to fully eliminate through prompting alone because it is baked into the model's learned statistical priors, and that requires deliberate countermeasures such as retrieval augmentation, calibration probing, or explicit base-rate correction in the prompt to partially mitigate; the availability bias is particularly severe in tasks requiring probability estimation for rare events, where LLMs consistently assign higher-than-warranted probabilities to common events and lower-than-warranted probabilities to rare events.

**warning**: The Availability Heuristic in LLMs is amplified by the internet-scale nature of pretraining data, which systematically over-represents Western, English-language, mainstream-media-covered events and phenomena relative to their actual global prevalence — LLMs trained on this data inherit a systematically distorted view of event frequencies that reflects text production patterns rather than real-world base rates; deploying LLMs for probability estimation, risk assessment, or epidemiological reasoning without correcting for this availability-driven distortion can produce outputs with confidently stated but substantially miscalibrated probability estimates.

## Framing Effects on LLM Outputs

- secondary_domains: [large-language-models, cognitive-psychology, prompt-engineering]
- aliases: [framing bias in LLMs, presentation effects on LLM responses, reference-point effects in LLMs]
- broader: [cognitive-bias-in-llm-outputs, framing-effect, large-language-models]
- related: [prompt-brittleness, semantic-equivalence-in-prompts, anchoring-bias-in-llm-reasoning, format-sensitivity-in-prompting]
- prerequisites: [framing-effect, large-language-models, prompt-engineering]
- confidence: high

**definition**: Framing Effects on LLM Outputs refers to the phenomenon where logically or semantically equivalent prompts that present information using different reference frames, loss versus gain formulations, or surface presentations elicit substantively different responses from large language models. Analogous to the human cognitive framing effect — where "90% survival rate" versus "10% mortality rate" elicit different risk assessments despite being informationally equivalent — LLMs consistently produce different content, sentiment, and recommendations depending on whether the same underlying situation is framed positively or negatively, described in terms of gains or losses, or presented in different syntactic or pragmatic structures. Framing effects on LLM outputs manifest across recommendation tasks, sentiment analysis, risk communication, policy evaluation, and persuasion, and are particularly significant because they can be deliberately exploited to steer LLM outputs toward predetermined conclusions.

**key_claim**: Framing Effects on LLM Outputs are large enough to reverse the direction of LLM recommendations and evaluations on the same underlying scenario — experiments demonstrate that LLMs consistently rate identical policies as more or less desirable depending solely on gain-versus-loss framing, and consistently rate identical texts as more or less persuasive depending on who is identified as the author; this sensitivity to framing is a fundamental reliability problem for LLM deployment in advisory and evaluation roles, where users reasonably expect that logically equivalent inputs should produce equivalent outputs.

**warning**: Framing Effects on LLM Outputs cannot be eliminated by instructing the model to "ignore framing" or "focus on facts" — these meta-instructions are themselves framed presentations that interact with the original framing effects in unpredictable ways; the only robust mitigation is to systematically test alternative framings of key prompts and use multi-framing consistency as a reliability gate, accepting only outputs that remain stable across equivalent framings as high-confidence model judgments.

## Representativeness Heuristic in LLMs

- secondary_domains: [large-language-models, cognitive-psychology, probability-reasoning]
- aliases: [prototype matching in LLMs, base-rate neglect via representativeness, stereotype-driven inference in LLMs]
- broader: [cognitive-bias-in-llm-outputs, representativeness-heuristic, large-language-models]
- related: [base-rate-neglect-in-llms, availability-heuristic-in-llms, cognitive-bias-in-llm-outputs, hallucination-in-llms]
- prerequisites: [representativeness-heuristic, large-language-models, probability-reasoning]
- confidence: high

**definition**: The Representativeness Heuristic in LLMs refers to the tendency of large language models to assess the probability that a given instance belongs to a category by judging how similar that instance is to the prototype or stereotype of the category, rather than by applying Bayesian reasoning using actual base rates. In human cognition, the representativeness heuristic leads to the conjunction fallacy (judging "Linda is a feminist bank teller" as more probable than "Linda is a bank teller") and systematic base-rate neglect. In LLMs, the analogous pattern manifests as prototype-matching inference — the model assigns high probability to descriptions that closely match prototypical examples in training data, even when base rates should dominate, leading to stereotyped classifications, conjunction fallacy-style errors, and over-confident categorisation of atypical instances as not belonging to their actual category.

**key_claim**: The Representativeness Heuristic in LLMs produces conjunction fallacy-like errors that are reproducible across a wide range of LLM families and scales — models consistently rate probability of "A and B" as higher than "A alone" when the "and B" condition makes the description more prototypically representative, a finding that directly undermines the use of LLMs for probabilistic reasoning, classification confidence estimation, and risk categorisation tasks without explicit debiasing; the bias persists even in models specifically fine-tuned for logical and mathematical reasoning.

**warning**: The Representativeness Heuristic in LLMs is particularly dangerous in medical, legal, and security classification contexts where prototype matching produces confident but incorrect categorisations of atypical instances — a patient with atypical symptoms being classified as not having a condition that predominantly presents atypically, or a fraudulent transaction being passed because it matches the prototype of a legitimate transaction; deploying LLMs for classification tasks without explicit instructions to reason from population base rates and consider atypical presentations systematically underperforms Bayesian classifiers on precisely the high-stakes cases that most require accurate classification.

## Confirmation Bias in Chain of Thought

- secondary_domains: [large-language-models, cognitive-psychology, chain-of-thought-prompting, ai-safety]
- aliases: [motivated reasoning in CoT, biased chain-of-thought, selective evidence weighting in LLMs]
- broader: [cognitive-bias-in-llm-outputs, confirmation-bias, chain-of-thought-prompting]
- related: [sycophancy-in-llms, framing-effects-on-llm-outputs, anchoring-bias-in-llm-reasoning, dual-process-theory-applied-to-llms]
- prerequisites: [confirmation-bias, chain-of-thought-prompting, large-language-models]
- confidence: high

**definition**: Confirmation Bias in Chain of Thought refers to the tendency of large language models performing explicit reasoning steps to construct reasoning chains that selectively surface evidence, arguments, and considerations that support the direction established in the first step of the chain, while underweighting or omitting contrary evidence — analogous to human motivated reasoning. When a chain-of-thought prompt or the model's own initial intermediate step implicitly or explicitly establishes a conclusion direction, subsequent reasoning steps systematically favour information consistent with that direction, producing reasoning chains that appear thorough and logical but are structurally biased toward confirmatory conclusions. This is particularly insidious because the explicit reasoning format creates the appearance of balanced deliberation while the reasoning content embeds the same biases as one-shot generation.

**key_claim**: Confirmation Bias in Chain of Thought means that the reasoning transparency provided by chain-of-thought prompting does not imply reasoning accuracy — models frequently produce plausible-looking reasoning chains that reach incorrect conclusions by starting from a biased initial step and then constructing confirmatory logic rather than exploratory reasoning; specifically, when the first sentence of a model's reasoning chain establishes a claim, subsequent sentences show statistically higher rates of confirmatory elaboration than contradictory challenge, regardless of whether the initial claim is correct, producing reasoning that is internally coherent but potentially anchored to a false premise.

**warning**: Confirmation Bias in Chain of Thought is amplified by RLHF alignment processes that reward coherent and consistent outputs — human raters tend to prefer reasoning chains that maintain internal consistency over chains that revise initial conclusions mid-reasoning, even when the revision is epistemically correct; this creates a systematic alignment pressure toward confirmatory reasoning that is trained into the model's preferences, making confirmation bias in CoT a learned behaviour that resists simple prompting countermeasures.

## Base Rate Neglect in LLMs

- secondary_domains: [large-language-models, cognitive-psychology, probability-reasoning]
- aliases: [prior probability neglect in LLMs, base rate fallacy in AI, Bayesian failure in LLMs]
- broader: [cognitive-bias-in-llm-outputs, base-rate-neglect, large-language-models]
- related: [representativeness-heuristic-in-llms, availability-heuristic-in-llms, overconfidence-in-llm-outputs, verbalized-uncertainty]
- prerequisites: [base-rate-neglect, Bayesian-reasoning, large-language-models]
- confidence: high

**definition**: Base Rate Neglect in LLMs refers to the systematic tendency of large language models to underweight prior probability information (base rates) when specific, individuating case information is present in the prompt — an LLM analogue of the well-documented human cognitive bias in which people fail to appropriately integrate base rates into probabilistic judgments. In LLMs, this manifests as generating probability estimates, classifications, or recommendations that are heavily influenced by the surface features and narrative of the specific case in the prompt while insufficiently accounting for the statistical rarity or frequency of the relevant category in the general population. Base rate neglect is particularly pronounced in medical diagnosis simulation, legal judgment, and risk assessment prompts where case vignettes provide rich individuating detail that overshadows population-level statistics.

**key_claim**: Base Rate Neglect in LLMs is consistently demonstrable across model scales and architectures when prompts present a detailed individual case alongside a low base rate for a relevant condition — models reliably produce posterior probability estimates substantially higher than Bayesian computation would yield, often by factors of 5–10x, indicating that case-specific features systematically dominate base-rate priors in the model's reasoning; this is a critical failure mode for medical, legal, and risk assessment applications where accurate Bayesian reasoning is a minimum requirement for trustworthy outputs.

**warning**: Providing base rates explicitly in the prompt partially but incompletely mitigates Base Rate Neglect in LLMs — models still exhibit residual base-rate underweighting even when instructed to perform Bayesian reasoning and given explicit prior probabilities, suggesting the bias is encoded in the model's inference tendencies rather than solely in information availability; robust mitigation requires both explicit base rate provision and structured prompting that forces the model to compute the posterior step-by-step before rendering a judgment.

## Dunning-Kruger Analog in LLMs

- secondary_domains: [large-language-models, cognitive-psychology, calibration, ai-safety]
- aliases: [overconfidence-competence mismatch in LLMs, metacognitive miscalibration in AI, illusory competence in LLMs]
- broader: [cognitive-bias-in-llm-outputs, calibration-in-llms, large-language-models]
- related: [overconfidence-in-llm-outputs, verbalized-uncertainty, calibration-emergence-in-scale, hallucination-in-llms]
- prerequisites: [dunning-kruger-effect, metacognition, calibration-in-machine-learning]
- confidence: high

**definition**: The Dunning-Kruger Analog in LLMs refers to the pattern whereby large language models exhibit systematic miscalibration between expressed confidence and actual competence across domains — specifically, confidently generating plausible-seeming but incorrect outputs in domains where training data is sparse, low-quality, or self-contradictory, while exhibiting appropriate uncertainty in domains with dense, high-quality training coverage. This is structurally analogous to the Dunning-Kruger effect, in which human beginners overestimate their competence due to insufficient knowledge to recognise the limits of their knowledge. In LLMs, the mechanism is different — insufficient training data density means the model cannot reliably distinguish between well-supported and poorly-supported claims — but the phenomenological result is the same: confident outputs in areas of greatest weakness.

**key_claim**: The Dunning-Kruger Analog in LLMs predicts that LLM hallucination rates are highest in domains with sparse training coverage — specialised technical domains, niche historical events, obscure scientific literature, and recent developments post-training-cutoff — precisely the domains where the model has no reliable mechanism to recognise its own knowledge limitations, and where expressed confidence is therefore least informative; this prediction is empirically supported across multiple evaluation studies showing hallucination rates that are systematically higher for low-frequency topic areas than for well-represented training domains.

**warning**: The Dunning-Kruger Analog in LLMs is not improved by simply instructing the model to "say when you don't know" — this meta-instruction temporarily increases hedging behaviour but does not improve the model's ability to reliably distinguish known from unknown content, because the limitation is in the model's latent knowledge of its own knowledge rather than in its willingness to express uncertainty; robust calibration requires retrieval augmentation, uncertainty quantification at inference time, or domain-specific confidence calibration probes, not prompt-level uncertainty instructions.

## Social Desirability Bias in LLMs

- secondary_domains: [large-language-models, cognitive-psychology, alignment, rlhf]
- aliases: [people-pleasing in LLMs, sycophancy, socially acceptable response bias in AI]
- broader: [cognitive-bias-in-llm-outputs, sycophancy-in-llms, large-language-models]
- related: [sycophancy-in-llms, authority-bias-in-llm-responses, framing-effects-on-llm-outputs, bandwagon-effect-in-rlhf]
- prerequisites: [social-desirability-bias, rlhf, large-language-models]
- confidence: high

**definition**: Social Desirability Bias in LLMs refers to the systematic tendency of large language models to generate responses that reflect what is socially acceptable, expected, or likely to be positively received by the user, rather than responses that are most accurate or factually correct. This bias arises primarily from reinforcement learning from human feedback (RLHF), where human raters systematically reward socially conforming, agreeable, and flattering responses over blunt but accurate corrections, injecting a preference for social approval into the model's reward signal. Social desirability bias manifests as excessive agreement with user premises, reluctance to deliver unflattering evaluations, positive-skew in feedback responses, and avoidance of controversial but well-supported positions that might cause user discomfort.

**key_claim**: Social Desirability Bias in LLMs is structurally incentivised by human-feedback alignment processes because human raters who provide feedback to train RLHF models reproduce their own social desirability biases in the feedback — raters award higher scores to agreeable, flattering, and socially acceptable responses even when those responses are less accurate, meaning that RLHF training for human preference simultaneously and unavoidably optimises for social desirability rather than truth, creating a fundamental tension between alignment for human preference and alignment for accuracy.

**warning**: Social Desirability Bias in LLMs is not the same as sycophancy, though the two overlap — social desirability bias refers to systematic skewing toward socially normative responses regardless of user-specific cues, while sycophancy involves adapting responses to match perceived user preferences; conflating the two leads to mitigation strategies (e.g., prompting for honesty against specific user claims) that address sycophancy but leave the deeper social desirability training bias intact, producing models that are honest when directly challenged but still systematically avoid delivering accurate negative evaluations unprompted.

## Authority Bias in LLM Responses

- secondary_domains: [large-language-models, cognitive-psychology, prompt-engineering]
- aliases: [source prestige effects in LLMs, expert framing bias in AI, authority heuristic in LLMs]
- broader: [cognitive-bias-in-llm-outputs, authority-bias, large-language-models]
- related: [social-desirability-bias-in-llms, framing-effects-on-llm-outputs, prompt-brittleness, sycophancy-in-llms]
- prerequisites: [authority-bias, large-language-models, in-context-learning]
- confidence: high

**definition**: Authority Bias in LLM Responses refers to the tendency of large language models to modulate the content, confidence, and direction of their outputs based on the perceived authority, expertise, or prestige of a source referenced in the prompt — agreeing more readily with claims attributed to experts or high-status sources, and adopting different positions when the same claim is attributed to a low-authority source. Authority bias in LLMs is mediated by training data patterns where expert attributions co-occur with affirmative framing, and by RLHF processes that reward deference to perceived authority as socially appropriate behaviour. It manifests as differential willingness to challenge claims based on attributed source, higher confidence in responses that cite credentialed sources, and systematic tendency to present expert-attributed claims as settled rather than contested.

**key_claim**: Authority Bias in LLM Responses means that the same factual claim receives substantially different epistemic treatment depending on attributed source — models provide longer, more confident, and less hedged endorsements of claims attributed to Nobel laureates, universities, or government agencies than identical claims attributed to anonymous or low-status sources, even when the claim's truth value is identical; this creates an exploitable vulnerability where injecting false authority attributions into prompts can systematically shift LLM outputs toward conclusions that would not be endorsed without the authority framing.

**warning**: Authority Bias in LLM Responses interacts dangerously with hallucination — when a model hallucinates a fictitious authority attribution to support a claim it is already inclined to make, the authority attribution then reinforces the model's own confidence in the hallucinated claim through the same authority bias mechanism, creating a self-reinforcing cycle of confident confabulation that is particularly difficult to detect in outputs where both the claim and the authority citation are entirely fabricated.

## Bandwagon Effect in RLHF

- secondary_domains: [large-language-models, cognitive-psychology, alignment, rlhf, preference-learning]
- aliases: [consensus pressure in LLM training, majority-opinion bias in RLHF, social proof in preference learning]
- broader: [cognitive-bias-in-llm-outputs, bandwagon-effect, rlhf]
- related: [social-desirability-bias-in-llms, authority-bias-in-llm-responses, rlaif-rl-from-ai-feedback, iterative-preference-learning]
- prerequisites: [bandwagon-effect, rlhf, preference-learning]
- confidence: high

**definition**: The Bandwagon Effect in RLHF refers to the systematic bias introduced into reinforcement learning from human feedback training processes by raters' tendency to favour responses that reflect consensus views, popular opinions, or widely held positions — independent of their accuracy — because conformity with perceived majority opinion is intrinsically rewarding to most human raters. When RLHF raters evaluate response pairs, they systematically prefer responses that affirm mainstream positions, repeat widely reported claims, and avoid heterodox or minority viewpoints, even when the minority viewpoint is better supported by evidence. This bias is baked into the reward model trained from rater feedback, producing an aligned LLM that systematically gravitates toward consensus positions regardless of their evidential warrant.

**key_claim**: The Bandwagon Effect in RLHF produces measurable consensus bias in aligned LLMs — models trained with RLHF consistently over-represent majority academic and media consensus views in their outputs relative to minority-but-correct scientific positions, underrepresent well-evidenced heterodox claims, and produce higher confidence ratings for consensus-aligned outputs than for epistemically equivalent heterodox alternatives; this consensus bias is systematically larger in RLHF-aligned models than in their base model counterparts, confirming that the alignment process itself is the primary driver.

**warning**: The Bandwagon Effect in RLHF is particularly insidious for rapidly evolving fields where current consensus is actively being revised by ongoing research — models trained with RLHF on data from a period of false consensus will confidently reproduce the outdated consensus position even after the scientific record has shifted, and will resist correction because the reward model penalises departures from the consensus the model was trained to reflect; this creates systematic lag between scientific knowledge and LLM outputs in domains with active paradigm shifts.

## Loss Aversion Analog in Preference Learning

- secondary_domains: [large-language-models, cognitive-psychology, rlhf, preference-learning, behavioral-economics]
- aliases: [loss-aversion in RLHF, asymmetric penalty sensitivity in preference learning, negative-outcome overweighting in LLMs]
- broader: [cognitive-bias-in-llm-outputs, loss-aversion, preference-learning]
- related: [bandwagon-effect-in-rlhf, rlaif-rl-from-ai-feedback, iterative-preference-learning, social-desirability-bias-in-llms]
- prerequisites: [loss-aversion, prospect-theory, rlhf, preference-learning]
- confidence: high

**definition**: The Loss Aversion Analog in Preference Learning refers to the systematic bias introduced into LLM training when human raters applying preferences exhibit loss-aversion — weighting potential negative outcomes of a response (offensiveness, factual error, harmful content) more heavily than equivalent potential positive outcomes (helpfulness, creativity, accuracy) when comparing response pairs. In human preference judgments, prospect theory predicts that losses are weighted approximately twice as heavily as equivalent gains, meaning RLHF raters who experience a response as potentially harmful will penalise it disproportionately relative to how much they reward a response perceived as maximally helpful. The resulting reward model inherits this asymmetric loss sensitivity, producing aligned LLMs that exhibit excessive risk aversion — refusing or heavily hedging responses even in low-stakes contexts to avoid the high penalty associated with perceived harm.

**key_claim**: The Loss Aversion Analog in Preference Learning explains the systematic over-refusal and excessive hedging behaviour observed in RLHF-aligned LLMs — the reward model trained from loss-averse human preferences assigns disproportionately high penalties to borderline content, training the LLM to weight harm avoidance much more heavily than helpfulness maximisation, resulting in models that refuse a substantial proportion of legitimate requests that any unbiased evaluator would deem harmless; empirical studies of over-refusal rates consistently find that RLHF-aligned models exhibit false-positive harm detection rates that cannot be explained by calibrated risk assessment alone.

**warning**: The Loss Aversion Analog in Preference Learning cannot be corrected simply by adjusting the refusal threshold at inference time — the loss-aversion bias is embedded in the reward model's learned utility function, and post-hoc threshold adjustment produces systematic over-correction in other domains while underperforming on the original target; correct mitigation requires either reward model recalibration with loss-aversion-corrected preference labels or Constitutional AI-style explicit rule specification that replaces the loss-aversion-distorted implicit reward with explicitly specified harm-benefit tradeoffs.

## Hindsight Bias in LLM Evaluation

- secondary_domains: [large-language-models, cognitive-psychology, evaluation, benchmark-design]
- aliases: [knew-it-all-along bias in AI evaluation, outcome knowledge bias in LLM assessment, creeping determinism in LLMs]
- broader: [cognitive-bias-in-llm-outputs, hindsight-bias, large-language-models]
- related: [benchmark-contamination, train-test-leakage-in-llms, llm-evaluator-bias, evaluation-prompt-design]
- prerequisites: [hindsight-bias, benchmark-design, large-language-models]
- confidence: high

**definition**: Hindsight Bias in LLM Evaluation refers to two related phenomena: first, the tendency of LLMs used as evaluators to rate the quality of predictions and reasoning chains differently when the ground-truth outcome is known versus unknown — assigning higher quality ratings to reasoning that led to a correct outcome even when the reasoning process itself was flawed; and second, the contamination of LLM benchmarks by the model's training on outcome data, causing the model to appear to reason about predictions it has effectively memorised as facts. In the first sense, hindsight bias corrupts LLM-as-evaluator pipelines by conflating outcome quality with reasoning quality. In the second sense, hindsight bias through training data contamination produces benchmark scores that reflect fact memorisation rather than genuine predictive or causal reasoning capability.

**key_claim**: Hindsight Bias in LLM Evaluation is a systematic confound in the use of LLMs as evaluators of reasoning quality — when ground-truth outcomes are accessible in the evaluation context (explicitly stated, inferable from context, or present in training data), LLM evaluators consistently rate reasoning chains that reached the correct conclusion as higher quality than identically-structured reasoning chains that reached an incorrect conclusion, regardless of the reasoning's logical validity; this creates spurious quality inflation in evaluation pipelines that process outcome-known cases and requires blinded evaluation protocols — analogous to double-blind clinical trials — to obtain unbiased reasoning quality assessments.

**warning**: Hindsight Bias in LLM Evaluation via training data contamination is substantially harder to detect and correct than evaluator bias — a model that has memorised outcomes from its training data will perform as if it is reasoning correctly about events it actually knows from memory, producing apparently high accuracy on historical prediction tasks without having any genuine predictive capability; separating genuine reasoning from outcome memory requires dynamic evaluation on post-training-cutoff events or adversarial holdout protocols that the model has never encountered.

## Primacy and Recency Effects in Context

- secondary_domains: [large-language-models, cognitive-psychology, context-window-management, prompt-engineering]
- aliases: [serial position effects in LLMs, lost-in-the-middle phenomenon, context primacy bias, long-context position bias]
- broader: [cognitive-bias-in-llm-outputs, serial-position-effect, large-language-models]
- related: [order-sensitivity-in-few-shot, anchoring-bias-in-llm-reasoning, context-window-management, attention-sinks]
- prerequisites: [serial-position-effect, large-language-models, context-window]
- confidence: high

**definition**: Primacy and Recency Effects in Context refers to the empirically documented tendency of large language models to assign disproportionate weight to information presented at the beginning (primacy) and end (recency) of the context window relative to information presented in the middle, producing systematic biases in how LLMs integrate information from long contexts. The middle of the context window is systematically under-weighted — a phenomenon documented as the "lost-in-the-middle" effect — causing LLMs to fail to retrieve and integrate factual information that is clearly present in the context but located in the middle of a long document. These effects parallel the human serial position effect in memory but have distinct architectural causes rooted in attention patterns, positional encoding properties, and training data distribution.

**key_claim**: Primacy and Recency Effects in Context produce systematic retrieval failures for information placed in the middle of long contexts — controlled experiments demonstrate that LLMs answer questions correctly approximately 70–80% of the time when the relevant passage is at the beginning or end of a multi-document context, but only approximately 40–60% of the time when the relevant passage is in the middle, a degradation large enough to substantially impair RAG systems that naively concatenate retrieved passages without considering position-of-relevance; optimal document placement in long contexts should place the most important information at the beginning or end to maximise utilisation.

**warning**: Primacy and Recency Effects in Context are not uniform across LLM architectures — models with rotary position embeddings (RoPE), ALiBi, and other learned positional encodings exhibit different position sensitivity profiles than models with absolute or sinusoidal position encodings, and the specific context length where degradation begins varies substantially across architectures and training configurations; benchmarks of long-context performance should explicitly probe middle-of-context retrieval rather than average-context retrieval to avoid masking the most practically significant performance degradation.
