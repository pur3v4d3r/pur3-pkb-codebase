---
batch_name: b02-02-prompt-sensitivity
batch_date: 2026-05-22
default_domain: prompt-engineering
default_confidence: high
notes: |
  Fifteen concepts covering how LLM outputs vary with surface-level and
  semantic prompt variations. Spans label sensitivity, format sensitivity,
  few-shot order effects, surface-form competition, prompt brittleness,
  adversarial robustness, distribution shift, semantic equivalence,
  paraphrase invariance, cross-lingual transfer, calibration, verbalized
  uncertainty, hedging, overconfidence, and underspecification. Batch 02
  of the prompt-engineering and LLM series.
---

# Batch: B02-02 Prompt Sensitivity and Robustness

## Label Sensitivity in Prompting

- secondary_domains: [in-context-learning, large-language-models, evaluation]
- aliases: [label bias in prompting, demo label effects, in-context label sensitivity]
- broader: [prompt-sensitivity, few-shot-prompting]
- related: [order-sensitivity-in-few-shot, surface-form-competition, prompt-calibration-techniques, format-sensitivity-in-prompting]
- prerequisites: [few-shot-prompting, in-context-learning, large-language-models]
- confidence: high

**definition**: Label sensitivity in prompting refers to the phenomenon in which the specific text strings used as output labels in few-shot demonstrations systematically bias the model's predictions, independent of the semantic content of the labels. Even when two label sets are semantically equivalent (e.g., "positive/negative" vs. "good/bad"), the model's classification accuracy and output distribution shift based on the label tokens' frequency and associations in training data. Label sensitivity also manifests as majority-label bias: when demonstration labels are imbalanced, the model overproduces the majority label, and when the labels in demonstrations are shuffled randomly to create inconsistent signal, many models ignore the label-input correspondence entirely and default to prior-probability answers.

**key_claim**: The dominant signal in in-context learning label slots is not the input-output mapping demonstrated by the examples but the statistical properties of the label tokens themselves — models with strong label sensitivity are implicitly performing label-token frequency-weighted prediction rather than input-conditioned classification, which means that calibrating label tokens (choosing labels with equal training-frequency or remapping them to numerals) can close a large fraction of the performance gap between calibrated and uncalibrated prompts.

**warning**: Label sensitivity is invisible in single-prompt evaluations and only surfaces through systematic ablations that vary the label strings while holding all other prompt components constant; researchers who fix label strings across all experiments will systematically confound model capability with label-token frequency artefacts, leading to incorrect conclusions about the relative performance of different prompting strategies.

## Format Sensitivity in Prompting

- secondary_domains: [prompt-engineering, large-language-models, evaluation]
- aliases: [prompt format effects, output format sensitivity, template sensitivity]
- broader: [prompt-sensitivity, prompt-engineering]
- related: [label-sensitivity-in-prompting, surface-form-competition, prompt-brittleness, semantic-equivalence-in-prompts]
- prerequisites: [prompt-engineering, large-language-models]
- confidence: high

**definition**: Format sensitivity in prompting is the phenomenon in which the structural and typographic presentation of a prompt — delimiter choice, capitalisation, whitespace, separator tokens, markdown formatting, JSON vs. plain-text structure, line breaks, and the ordering of components such as instruction-context-question — systematically affects LLM output quality, even when the semantic content of the prompt is held constant. Format sensitivity arises because LLMs learn associations between surface-form patterns and task types during instruction tuning: JSON structure signals a structured-output task, bullet-point lists signal enumeration tasks, and colon-delimited templates signal question-answering tasks, causing the model to modulate both its output format and its reasoning strategy based on these format signals.

**key_claim**: Format sensitivity in prompting accounts for a surprisingly large share of the variance in reported LLM performance across papers — studies that treat a specific prompt format as the canonical prompt for a task are measuring format-task alignment as much as model capability, and the same underlying model can appear to differ by dozens of percentage points on the same task depending on formatting choices alone, which necessitates format-ablation studies as standard practice in prompt engineering research.

**warning**: Format sensitivity interacts with instruction-tuning template artefacts in ways that are difficult to predict: formats that closely match the instruction-tuning template used during a model's training will produce dramatically better performance than semantically equivalent formats that deviate from that template, but this advantage is model-specific and changes with each model version, making format-sensitivity calibration a continuous maintenance task in production systems.

## Order Sensitivity in Few-Shot

- secondary_domains: [in-context-learning, prompt-engineering, large-language-models]
- aliases: [few-shot example ordering effects, demonstration order sensitivity, in-context order bias]
- broader: [prompt-sensitivity, few-shot-prompting]
- related: [label-sensitivity-in-prompting, format-sensitivity-in-prompting, surface-form-competition, primacy-and-recency-effects-in-context]
- prerequisites: [few-shot-prompting, in-context-learning, large-language-models]
- confidence: high

**definition**: Order sensitivity in few-shot prompting refers to the documented phenomenon in which the sequence in which demonstrations are presented in a few-shot prompt significantly affects the model's output — both in terms of accuracy and in terms of which output distribution the model selects from. Models display recency bias (over-weighting the last few examples), primacy effects in certain architectures, and strong interactions between example ordering and the model's prior over output labels. The effect is large enough that the same set of examples can produce accuracy variations of 30+ percentage points across orderings, depending on the task and model.

**key_claim**: Order sensitivity in few-shot prompting is primarily a product of positional attention weighting rather than semantic processing of demonstration content — examples positioned closest to the query in the context receive disproportionate attention weight, biasing the model toward the output patterns present in those proximal examples regardless of whether those examples are the most semantically relevant demonstrations for the specific query, which motivates strategies such as query-conditioned example retrieval and active demonstration reordering.

**warning**: Majority of published few-shot prompting results are reported for a single fixed ordering of demonstrations, making it impossible to distinguish task capability from order-luck; rigorous few-shot evaluation requires reporting the mean and variance across multiple random orderings, and the reported ordering should be justified by a selection procedure (e.g., semantic similarity to the test instance) rather than selected as the best of a search over orderings post-hoc.

## Surface Form Competition

- secondary_domains: [in-context-learning, large-language-models, tokenization]
- aliases: [vocabulary competition in prompting, token form bias, surface string competition in ICL]
- broader: [prompt-sensitivity, in-context-learning]
- related: [label-sensitivity-in-prompting, format-sensitivity-in-prompting, prompt-calibration-techniques, verbalized-uncertainty]
- prerequisites: [in-context-learning, tokenization, large-language-models]
- confidence: high

**definition**: Surface form competition is the phenomenon in which multiple surface-form variants of a semantically equivalent label or entity compete with each other in the model's vocabulary distribution, causing the probability mass for the correct label to be split across multiple tokens or token sequences. For example, if the correct answer to a binary classification task is "positive" but the model also assigns probability to "Positive," "POSITIVE," and "pos," the effective probability of the correct answer is underestimated relative to a model that uses a single unambiguous token. Surface form competition is a structural artefact of tokeniser design and training data statistics that systematically biases likelihood-based evaluation metrics toward labels with compact, unambiguous token representations.

**key_claim**: Surface form competition invalidates direct probability comparisons between labels in zero-shot and few-shot classification unless calibration is applied — the raw log-probability of a label token is not a reliable signal of the model's semantic intention, and proper calibration requires normalising by the label's unconditional generation probability (the probability the model assigns to the label in the absence of any specific evidence), a correction that substantially changes the apparent ranking of model responses.

**warning**: Surface form competition is not merely an evaluation artefact — it affects generation outputs in constrained-decoding systems where the model must select from a vocabulary of label tokens, causing the system to select the label whose surface form is most frequently represented by a single high-probability token rather than the label that best matches the semantic evidence, leading to label-selection biases that are invisible to evaluators who look only at the final selected label without inspecting the underlying probability distribution.

## Prompt Brittleness

- secondary_domains: [prompt-engineering, robustness, large-language-models]
- aliases: [prompt fragility, sensitivity to prompt perturbation, non-robust prompting]
- broader: [prompt-sensitivity, prompt-engineering]
- narrower: [adversarial-prompt-robustness]
- related: [format-sensitivity-in-prompting, label-sensitivity-in-prompting, semantic-equivalence-in-prompts, paraphrase-invariance-testing]
- prerequisites: [prompt-engineering, large-language-models]
- confidence: high

**definition**: Prompt brittleness refers to the property of a prompt in which small, semantically innocuous changes — minor rewordings, punctuation changes, example substitutions, or ordering permutations — cause large drops in task performance. A brittle prompt is one that achieves strong performance because it happens to match specific surface patterns in the model's training data or instruction-tuning template, rather than because it effectively communicates the task semantics. Prompt brittleness is the opposite of semantic robustness: a semantically robust prompt should produce consistent outputs across a broad equivalence class of paraphrases and format variants, whereas a brittle prompt produces consistent outputs only for a narrow neighbourhood around the specific text used during development.

**key_claim**: Prompt brittleness is the central validity threat in reported LLM performance benchmarks — when researchers develop a prompt through a manual search process and report performance for that specific prompt, they are reporting the maximum of a noisy performance distribution over the prompt equivalence class, not the model's true capability on the task, producing systematic overestimation of performance that compounds with the number of iterations of prompt refinement.

**warning**: Prompt brittleness cannot be detected from a single evaluation run; it requires testing the prompt across multiple semantically equivalent variants to estimate the width of the performance distribution, and a production prompt that has been manually refined to high performance on a held-out development set may have been over-fit to that development set's surface features, with brittleness only becoming apparent when the prompt encounters slightly different user phrasings in deployment.

## Adversarial Prompt Robustness

- secondary_domains: [security, prompt-engineering, large-language-models]
- aliases: [robustness to adversarial prompts, adversarial prompting resilience, jailbreak resistance]
- broader: [prompt-sensitivity, prompt-engineering, ai-safety]
- related: [prompt-brittleness, prompt-injection-attacks, distribution-shift-in-prompting]
- prerequisites: [prompt-engineering, adversarial-machine-learning, large-language-models]
- confidence: high

**definition**: Adversarial prompt robustness is the ability of a language model or prompt system to maintain intended behaviour — accuracy, safety constraints, output format, and refusal behaviour — in the face of adversarially crafted inputs designed to elicit unintended outputs. Adversarial prompts include jailbreaks that attempt to override safety restrictions, prompt-injection attacks that substitute attacker-controlled instructions for system-intent instructions, and semantic adversarial examples that produce incorrect outputs by exploiting prompt brittleness. Adversarial robustness is evaluated through red-teaming, automated adversarial prompt search, and transfer attacks that exploit gradient information from white-box model access.

**key_claim**: Adversarial prompt robustness cannot be achieved solely through prompt design — system-prompt instructions to "ignore jailbreaks" are themselves overridable by sufficiently crafted inputs, because the model treats all context tokens through the same attention mechanism regardless of their nominal role; genuine adversarial robustness requires a combination of adversarial training, output monitoring, input filtering, and architectural separation of system and user contexts that treats the adversarial robustness problem as a systems engineering problem rather than a prompting problem.

**warning**: The adversarial robustness landscape evolves continuously — a model that successfully resists a known set of adversarial prompt templates will be vulnerable to novel templates that exploit the same underlying mechanism through different surface forms, creating an arms race between red-teamers and model developers that cannot be resolved by a fixed defensive prompt; organisations deploying models in adversarial environments must continuously update their adversarial test suites and consider architectures with provable safety guarantees rather than relying solely on empirical robustness.

## Distribution Shift in Prompting

- secondary_domains: [machine-learning, robustness, large-language-models]
- aliases: [prompt distribution shift, covariate shift in prompting, out-of-distribution prompting]
- broader: [prompt-sensitivity, robustness]
- related: [prompt-brittleness, semantic-equivalence-in-prompts, cross-lingual-prompt-transfer, prompt-calibration-techniques]
- prerequisites: [distribution-shift, machine-learning, prompt-engineering]
- confidence: high

**definition**: Distribution shift in prompting refers to the degradation in LLM performance that occurs when the distribution of prompts encountered at deployment diverges from the distribution represented in the model's training data or the specific prompt formats used during instruction tuning. Distribution shift can be domain-specific (prompts about topics not well-represented in training data), format-specific (novel prompt templates not seen during training), linguistic (non-native speaker phrasings, regional dialects, specialised jargon), or task-specific (task formulations that diverge from the canonical forms established during instruction tuning). Identifying and mitigating distribution shift is a core challenge in deploying LLMs on real-world user queries whose distribution cannot be fully anticipated during development.

**key_claim**: Distribution shift in prompting is the most significant operational reliability challenge for deployed LLM systems, because the prompts submitted by real users will never perfectly match the development-time prompt distribution, and the performance degradation from moderate distribution shift is often not detectable through standard evaluation metrics that measure aggregate accuracy over balanced test sets rather than performance on the long-tail of user phrasings.

**warning**: Few-shot examples that significantly reduce distribution shift in development may actually amplify shift at deployment by anchoring the model to the development-time distribution — examples that were representative at development time may be poor representatives of the deployment distribution, causing the model to misinterpret novel deployment-time prompts through the lens of development-time examples; production prompt systems should include mechanisms for dynamically updating example pools based on observed deployment distribution characteristics.

## Semantic Equivalence in Prompts

- secondary_domains: [natural-language-processing, prompt-engineering, evaluation]
- aliases: [semantically equivalent prompts, prompt paraphrase equivalence, meaning-preserving prompt variants]
- broader: [prompt-sensitivity, prompt-engineering]
- related: [paraphrase-invariance-testing, prompt-brittleness, surface-form-competition]
- prerequisites: [prompt-engineering, natural-language-processing, large-language-models]
- confidence: high

**definition**: Semantic equivalence in prompts refers to the property that two prompts that express the same task semantics — the same instructions, constraints, and context, through different surface-form realisations — should produce outputs that are task-equivalently correct. Measuring semantic equivalence is non-trivial because human judges must establish that two prompts are truly equivalent before attributing performance differences to model sensitivity rather than genuine task differences. Semantic equivalence research is methodologically important because it establishes the upper bound on what prompt sensitivity actually measures: if two prompts are truly semantically equivalent and the model produces very different outputs, the model exhibits genuine semantic brittleness rather than sensitivity to genuine task distinctions.

**key_claim**: Establishing true semantic equivalence between prompts requires controlling for all dimensions of variation simultaneously — semantic content, syntactic structure, surface form, discourse organisation, and pragmatic implicature — and empirical evidence from controlled paraphrase studies shows that the vast majority of apparently "equivalent" prompts differ on at least one of these dimensions, which means that most reported prompt sensitivity effects are conflations of multiple distinct sensitivity types rather than clean measurements of semantic sensitivity alone.

**warning**: Over-relying on semantic equivalence as the standard for prompt evaluation can inadvertently penalise informative prompt variation — two prompts may be semantically non-equivalent in a task-relevant way (e.g., one includes a constraint the other omits), but both may be reasonable prompt designs for different user needs; the goal of semantic equivalence testing should be to characterise the model's sensitivity landscape, not to enforce a standard of identical outputs for all prompts.

## Paraphrase Invariance Testing

- secondary_domains: [evaluation, natural-language-processing, prompt-engineering]
- aliases: [prompt paraphrase stability testing, paraphrase robustness evaluation, semantic robustness testing]
- broader: [prompt-sensitivity, evaluation]
- related: [semantic-equivalence-in-prompts, prompt-brittleness, adversarial-prompt-robustness]
- prerequisites: [prompt-engineering, evaluation, paraphrase-generation]
- confidence: high

**definition**: Paraphrase invariance testing is an evaluation methodology that assesses LLM robustness by generating multiple semantically equivalent paraphrases of a prompt or question and measuring the consistency of the model's outputs across these variants. A model with high paraphrase invariance produces the same answer to "What is the capital of France?" regardless of whether the question is phrased as "Name the capital city of France," "Which city serves as the capital of France?," or "France's capital is?" A model with low paraphrase invariance will change its answer for some paraphrases, indicating that its responses are driven by surface-form associations rather than robust semantic understanding. Paraphrase invariance testing is used to diagnose prompt brittleness, estimate the reliability of benchmark results, and identify which task types are most sensitive to phrasing.

**key_claim**: Paraphrase invariance testing consistently reveals that the standard deviation of LLM performance across paraphrase variants is large enough to reverse accuracy rankings between models — a model that outperforms a competitor on a single canonical prompt phrasing may underperform the competitor when both are evaluated across the full paraphrase distribution, indicating that single-prompt benchmark comparisons are methodologically insufficient for drawing reliable conclusions about relative model capability.

**warning**: Automated paraphrase generation using LLMs or NLP paraphrasers does not guarantee semantic equivalence — automated paraphrases can subtly change the scope of questions, alter quantifier strength, shift pragmatic implicatures, or introduce new domain assumptions, making the resulting "paraphrase invariance" test a test of sensitivity to these subtle changes rather than a clean sensitivity test; human validation of the equivalence of a paraphrase set is essential before using automated paraphrase invariance results to draw diagnostic conclusions.

## Cross-Lingual Prompt Transfer

- secondary_domains: [multilingual-nlp, prompt-engineering, large-language-models]
- aliases: [multilingual prompt transfer, cross-language prompting, language-agnostic prompting]
- broader: [prompt-sensitivity, multilingual-nlp]
- related: [distribution-shift-in-prompting, semantic-equivalence-in-prompts, multilingual-emergent-transfer]
- prerequisites: [prompt-engineering, multilingual-language-models, cross-lingual-transfer]
- confidence: high

**definition**: Cross-lingual prompt transfer is the investigation of whether prompting strategies and performance improvements demonstrated in one language (typically English) generalise to other languages without explicit re-engineering of the prompt for those languages. It encompasses both the empirical phenomenon — that chain-of-thought reasoning prompts, role prompting, and format specifications originally designed in English transfer to non-English languages with varying effectiveness — and the practical engineering challenge of building prompting systems that are language-agnostic or that require only minimal language-specific adaptation. Cross-lingual transfer effectiveness varies dramatically across languages, with high-resource languages showing strong transfer and low-resource languages showing weak transfer due to imbalanced multilingual pretraining.

**key_claim**: Cross-lingual prompt transfer is asymmetric: prompting techniques transfer better from English to other high-resource languages than from any language to English, and better from high-resource to low-resource languages than vice versa, because the model's implicit understanding of task formulation conventions is anchored to English-centric instruction-tuning templates; this asymmetry means that multilingual systems cannot be validated solely on English prompt engineering and must include language-specific validation as a standard deployment requirement.

**warning**: Cross-lingual prompt transfer tests conducted on benchmark translations may overestimate real-world cross-lingual prompt robustness because benchmark translations are produced by professional translators preserving the original's semantic precision, whereas real user queries in non-English languages exhibit different phrasing conventions, levels of formality, and implicit assumptions; production multilingual systems should be validated on native-speaker-generated queries, not translated English queries.

## Prompt Calibration Techniques

- secondary_domains: [calibration, large-language-models, prompt-engineering]
- aliases: [prompt bias correction, output calibration for prompts, in-context calibration]
- broader: [prompt-engineering, calibration]
- related: [label-sensitivity-in-prompting, verbalized-uncertainty, surface-form-competition, overconfidence-in-llm-outputs]
- prerequisites: [prompt-engineering, probability-calibration, large-language-models]
- confidence: high

**definition**: Prompt calibration techniques are methods that adjust a language model's output probabilities or generated text to better reflect the true probability of correct outputs, compensating for systematic biases introduced by the prompt itself. Contextual calibration divides the model's label probabilities by its label probabilities for a content-free prompt (e.g., "N/A"), correcting for prior label biases. Prototypical calibration normalises by the model's probabilities for a prototypical positive and negative example. Verbal calibration instructs the model to express its confidence level in words and then uses the linguistic confidence expression as a calibration signal. Domain calibration uses in-domain examples to estimate the model's miscalibration and applies a learned correction function.

**key_claim**: Prompt calibration transforms label-sensitivity artefacts from confounds into correctable biases — the key insight is that a model's miscalibration on a specific prompt is not random but is a systematic function of the prompt's surface form and the model's training distribution, meaning that a small held-out calibration set can reliably estimate the correction factor needed to remove the systematic bias and produce calibrated probability estimates.

**warning**: Prompt calibration techniques that rely on the model's self-assessed confidence (verbal calibration) can themselves be subject to overconfidence and underconfidence biases — the model's language about its own uncertainty is not a direct readout of its internal probability distribution but is a learned linguistic behaviour that may diverge substantially from the calibration implied by the raw output probabilities, and the two should be measured independently rather than assumed to agree.

## Verbalized Uncertainty

- secondary_domains: [calibration, natural-language-generation, large-language-models]
- aliases: [linguistic confidence expression, verbal probability estimation, LLM uncertainty language]
- broader: [prompt-calibration-techniques, uncertainty-quantification]
- related: [hedge-phrases-in-prompts, overconfidence-in-llm-outputs, prompt-calibration-techniques]
- prerequisites: [large-language-models, uncertainty-quantification, calibration]
- confidence: high

**definition**: Verbalized uncertainty is the expression of a language model's confidence or uncertainty about its outputs through natural-language hedging phrases, explicit probability statements, or explicit invitations for the user to verify — "I believe," "I am fairly confident that," "with approximately 80% confidence," "you should verify this," — rather than through numerical probability scores or structured confidence metadata. Verbalized uncertainty is practically important because most LLM deployments surface only the text output, not the underlying probability distribution, making verbal uncertainty cues the primary signal available to users for assessing output reliability. However, verbalized uncertainty expressions are learned linguistic behaviours and need not be calibrated to the model's actual internal probabilities.

**key_claim**: Verbalized uncertainty is systematically miscalibrated in instruction-tuned models: post-RLHF fine-tuning reduces the frequency of hedging language in outputs because human raters penalise expressions of uncertainty as signs of weakness or incompetence, training the model to produce confident-sounding outputs regardless of its actual internal uncertainty, which makes the absence of verbal hedges a poor indicator of high actual confidence in aligned models.

**warning**: Prompting strategies that instruct the model to "express your confidence level" or "only answer if you are sure" do not reliably reduce hallucination — the model learns to comply with the surface form of the instruction by generating appropriate hedging language even for hallucinated content, producing outputs that sound appropriately uncertain but are still factually incorrect; verbal uncertainty expressions should be treated as unreliable proxies for actual model confidence and supplemented with external verification mechanisms.

## Hedge Phrases in Prompts

- secondary_domains: [pragmatics, prompt-engineering, natural-language-generation]
- aliases: [hedging in LLM outputs, epistemic modality in prompts, uncertainty phrases in prompts]
- broader: [verbalized-uncertainty, prompt-engineering]
- related: [verbalized-uncertainty, overconfidence-in-llm-outputs, underspecification-in-prompts]
- prerequisites: [prompt-engineering, pragmatics, natural-language-processing]
- confidence: high

**definition**: Hedge phrases in prompts and LLM outputs are linguistic expressions that signal epistemic uncertainty or reduced commitment to the truth of a proposition — phrases such as "it seems," "I believe," "it is possible that," "approximately," "as far as I know," and "you may want to verify this." As prompt components, hedge phrases can be used to modulate the model's confidence expression by including or excluding hedging instructions in the system prompt. As output features, hedge phrases serve as pragmatic signals to users about output reliability. The frequency and calibration of hedge phrases in LLM outputs have been studied in the context of both information reliability and user trust.

**key_claim**: Hedge phrases in LLM outputs are disproportionately absent for hallucinated content and disproportionately present for true content, an inversion of their intended signal function — models have learned to express uncertainty about well-known facts (because training data contains many debates and qualifications about prominent topics) and to express confidence about obscure or fabricated facts (because training data contains fewer challenges to specific claims about niche topics), making hedge phrases anti-informative relative to their face value.

**warning**: Instructing an LLM to hedge all uncertain outputs via system-prompt instructions can degrade user experience and information utility by producing over-hedged outputs that express uncertainty about well-established facts; effective hedge-phrase management requires calibrating the instruction to the specific domain's knowledge reliability rather than applying a blanket hedging policy, and must be paired with mechanisms that ground hedging in actual knowledge reliability rather than stylistic compliance.

## Overconfidence in LLM Outputs

- secondary_domains: [calibration, reliability, large-language-models]
- aliases: [LLM overconfidence, miscalibrated confidence in LLMs, hallucination confidence, confident hallucination]
- broader: [calibration, prompt-sensitivity]
- related: [verbalized-uncertainty, hedge-phrases-in-prompts, prompt-calibration-techniques, benchmark-contamination]
- prerequisites: [large-language-models, calibration, uncertainty-quantification]
- confidence: high

**definition**: Overconfidence in LLM outputs refers to the systematic tendency of language models to generate outputs with higher apparent confidence than is warranted by the evidence — producing definitive assertions about uncertain facts, failing to hedge claims that should be hedged, generating specific numerical values where ranges would be more appropriate, and constructing plausible-sounding but fabricated supporting details with the same fluency and confidence as accurate statements. Overconfidence is a function of both the model architecture (autoregressive generation has no inherent mechanism for declining to generate) and the training signal (RLHF rewards fluent, confident-sounding responses because human raters tend to prefer them).

**key_claim**: Overconfidence in LLM outputs is a structural property of the RLHF training paradigm — human preference raters systematically prefer confident, fluent responses over hedged, uncertain ones even when the hedged responses are more epistemically accurate, creating a training signal that rewards confident generation and inadvertently trains the model to suppress uncertainty expression, making overconfidence an alignment failure rather than a knowledge failure.

**warning**: Overconfidence is most dangerous for facts that are plausible but incorrect — the model generates confidently wrong information in the style and register of authoritative sources, making the error difficult to detect without domain expertise or fact-checking; this is particularly acute for numerical claims, citations, and biographical details where errors are easy to fabricate and difficult for users to identify without external verification, necessitating systematic fact-checking pipelines for any application where factual accuracy is critical.

## Underspecification in Prompts

- secondary_domains: [prompt-engineering, large-language-models, evaluation]
- aliases: [ambiguous prompts, underspecified task prompts, prompt ambiguity, prompt vagueness]
- broader: [prompt-sensitivity, prompt-engineering]
- related: [prompt-brittleness, semantic-equivalence-in-prompts, distribution-shift-in-prompting]
- prerequisites: [prompt-engineering, large-language-models]
- confidence: high

**definition**: Underspecification in prompts refers to the condition in which a prompt fails to fully specify the intended task, leaving multiple interpretations equally consistent with the prompt text. An underspecified prompt is one where multiple different behaviours all satisfy the literal instruction, and the model's choice among those behaviours is determined by its training distribution rather than by the user's actual intent. Common forms of underspecification include ambiguous scope (is the instruction to summarise the document as a whole or section by section?), missing output format constraints (length, structure, terminology), omitted audience specification, unclear success criteria, and absent constraints on the model's knowledge sources (should it use only information in the context or also its parametric knowledge?).

**key_claim**: Underspecification in prompts is the primary cause of prompt brittleness and performance variability across deployments — the model is not behaving inconsistently across prompt variants but is consistently selecting its preferred interpretation of an ambiguous instruction, and the apparent sensitivity to prompt variation is actually sensitivity to which interpretation each variant cues, not sensitivity to irrelevant surface form; eliminating underspecification through explicit constraint specification is therefore more effective at improving prompt robustness than stylistic refinement.

**warning**: Eliminating all underspecification from a prompt is often counterproductive for generative tasks where the user genuinely wants the model to use creative judgment — overly specified prompts constrain the output space to match the prompt author's assumptions rather than the user's actual needs, and the right level of specification is task-dependent; the engineering goal should be to resolve specification ambiguities that lead to task failures while preserving specification flexibility that enables appropriate contextual adaptation.
