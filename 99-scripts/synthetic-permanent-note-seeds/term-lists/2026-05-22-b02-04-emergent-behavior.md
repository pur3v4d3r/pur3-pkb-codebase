---
batch_name: b02-04-emergent-behavior
batch_date: 2026-05-22
default_domain: large-language-models
default_confidence: high
notes: |
  Fifteen concepts covering emergent behaviours and capability thresholds in
  large language models. Spans emergent prompting capability, few-shot
  emergent generalisation, chain-of-thought emergence, semantic parsing
  emergence, multilingual emergent transfer, arithmetic emergence thresholds,
  in-context learning as meta-learning, task generalisation, zero-shot
  generalisation mechanisms, capability elicitation, latent capability
  unlocking, model capability vs. alignment gaps, scaling and capability
  emergence, instruction-following emergence, and calibration emergence.
  Batch 02 of the prompt-engineering and LLM series.
---

# Batch: B02-04 Emergent Behaviour and Capability

## Emergent Prompting Capability

- secondary_domains: [scaling-laws, prompt-engineering, large-language-models]
- aliases: [prompt-driven emergent capability, emergent behaviour via prompting, elicited emergence]
- broader: [emergent-capabilities-in-llms, prompt-engineering]
- related: [capability-elicitation-prompting, latent-capability-unlocking, scaling-and-capability-emergence, instruction-following-emergence]
- prerequisites: [large-language-models, emergent-capabilities, prompt-engineering]
- confidence: high

**definition**: Emergent prompting capability refers to the phenomenon in which specific prompting strategies — such as chain-of-thought prompting, self-ask decomposition, or step-by-step instruction — unlock model capabilities that are not present (or not measurable) when the model is queried without those strategies, despite the model's underlying parameters being unchanged. The emergence is attributed to prompting rather than to scale alone because the capability threshold shifts: a model that scores near-random on direct querying may score well above chance on the same task when the appropriate prompting strategy is applied, demonstrating that the capability was latent in the model's parameters but required a specific prompt structure to be elicited.

**key_claim**: Emergent prompting capability challenges the standard interpretation of capability evaluations — benchmark scores obtained without prompting engineering systematically underestimate the true capability of large models, because the gap between unprompted and prompted performance is large enough to shift apparent capability boundaries by hundreds of billions of parameters; a properly prompted smaller model often outperforms a larger model evaluated with a naive prompt, demonstrating that reported capability thresholds are partially measurements of prompting effectiveness rather than of pure model capability.

**warning**: The distinction between "emergent prompting capability" and "prompt-engineered performance inflation" is difficult to operationalise — both involve improved task performance through prompting, but emergence typically refers to qualitative capability thresholds (the model gains the ability to do something it previously could not), while performance inflation refers to quantitative improvements on tasks the model could already perform; claiming emergence requires demonstrating that no version of the unprompted evaluation produces above-chance performance, not merely that prompted performance is higher than a specific unprompted baseline.

## Few-Shot Emergent Generalisation

- secondary_domains: [in-context-learning, large-language-models, generalisation]
- aliases: [few-shot generalisation threshold, in-context learning emergence, few-shot capability emergence]
- broader: [emergent-prompting-capability, in-context-learning]
- related: [in-context-learning-as-meta-learning, zero-shot-generalisation-mechanisms, task-generalisation-in-llms]
- prerequisites: [few-shot-prompting, in-context-learning, large-language-models]
- confidence: high

**definition**: Few-shot emergent generalisation refers to the capability of a model to correctly apply a novel task rule inferred from a small number of in-context demonstrations to a test input that is far outside the distribution of the demonstrations, in a way that demonstrates genuine rule induction rather than superficial similarity matching. A model that exhibits few-shot emergent generalisation will correctly apply a novel classification rule (e.g., a rule based on a character property that has no natural-language name) to inputs that share the abstract rule but look nothing like the demonstrations. This capability appears to emerge discontinuously with scale and is not present in smaller models that can only perform few-shot learning when the test input is in the same region of feature space as the demonstrations.

**key_claim**: Few-shot emergent generalisation represents a qualitative transition from pattern-completion to rule-induction in large models — small models perform few-shot tasks primarily by retrieving training instances similar to the demonstration-test combination, while large models can perform them by inducing abstract rules and applying those rules to novel examples, which explains why the few-shot performance of small and large models diverges most dramatically on tasks requiring abstract rule application rather than analogical retrieval.

**warning**: Demonstrations of few-shot emergent generalisation on carefully constructed academic tasks may not accurately reflect generalisation ability in production settings where the demonstrations are noisily constructed, the test inputs differ from demonstrations in multiple correlated dimensions, and the rules being demonstrated are not cleanly separable from confounding task features; the robustness of few-shot generalisation to imperfect demonstrations and noisy task signal is much lower than academic demonstrations suggest.

## Chain-of-Thought Emergence

- secondary_domains: [prompt-engineering, reasoning, large-language-models]
- aliases: [CoT capability emergence, chain-of-thought threshold, reasoning chain emergence]
- broader: [emergent-prompting-capability, chain-of-thought-prompting]
- related: [few-shot-emergent-generalisation, arithmetic-emergence-threshold, capability-elicitation-prompting, scaling-and-capability-emergence]
- prerequisites: [chain-of-thought-prompting, large-language-models, scaling-laws]
- confidence: high

**definition**: Chain-of-thought emergence refers to the empirical finding that chain-of-thought prompting (providing step-by-step reasoning examples) produces substantial performance improvements only for models above a certain scale threshold (approximately 100 billion parameters in the original Wei et al. study), while producing no improvement or even slight degradation for models below that threshold. This non-monotonic relationship between model scale and chain-of-thought benefit is interpreted as an emergent property: small models generate incoherent or incorrect reasoning chains that corrupt rather than improve the final answer, while large models generate coherent reasoning chains that reliably lead to correct conclusions.

**key_claim**: Chain-of-thought emergence is partly an artefact of evaluation methodology rather than a pure scale threshold — smaller models can benefit from chain-of-thought prompting when the task is appropriately difficulty-matched to the model's capability level, and the apparent threshold reflects the minimum model size required to generate coherent reasoning chains for the specific tasks studied (multi-step arithmetic and symbolic reasoning), not a universal threshold below which no chain-of-thought benefit is possible; per-task capability thresholds are substantially lower than the aggregate threshold reported in early studies.

**warning**: The chain-of-thought emergence finding has been used to justify the claim that capability improvements are discontinuous with scale, but subsequent analysis reveals that many apparently discontinuous capability gains become smooth and predictable when measured on the right metrics — the discontinuity in CoT performance is partly an artefact of binary accuracy metrics that show step-function changes even when the underlying performance distribution changes smoothly, and using graded metrics (partial credit, log-probability scores) typically reveals gradual improvement rather than discontinuous emergence.

## Semantic Parsing Emergence

- secondary_domains: [natural-language-processing, large-language-models, program-synthesis]
- aliases: [semantic parsing capability emergence, structured prediction emergence, code generation emergence]
- broader: [emergent-prompting-capability, natural-language-processing]
- related: [chain-of-thought-emergence, instruction-following-emergence, zero-shot-generalisation-mechanisms]
- prerequisites: [semantic-parsing, large-language-models, emergent-capabilities]
- confidence: high

**definition**: Semantic parsing emergence refers to the acquisition by language models of the ability to map natural language utterances to formal structured representations — logical forms, SQL queries, executable code, API calls, or knowledge graph queries — as a function of model scale and instruction tuning. At small scales, models generate plausible-looking but syntactically invalid or semantically incorrect formal representations; at large scales and with instruction tuning, models generate valid, executable formal representations for complex natural language inputs including novel phrasings and compositional queries not present in training data. Semantic parsing emergence is the foundation of tool-using LLM agents and code-generation systems.

**key_claim**: Semantic parsing emergence in instruction-tuned models occurs through a different mechanism than in task-specific trained parsers — rather than learning a formal grammar of the target representation language explicitly, large models learn to recognise the pragmatic intent of natural language and map it to the formal structure that achieves that intent, a more flexible but less reliably correct approach that excels on in-distribution queries but exhibits systematic failures on queries that violate implicit pragmatic conventions even when the formal representation required is simple.

**warning**: Semantic parsing via LLMs produces valid-looking but semantically incorrect formal representations with high confidence in cases where the natural language input is ambiguous or underspecified — an SQL query or API call may be syntactically valid and execute without error while implementing the wrong semantic operation due to scope ambiguity, implicit assumption resolution, or entity linking errors; production semantic parsing systems must include execution validation, result verification, and user confirmation steps rather than treating LLM-generated formal representations as correct by construction.

## Multilingual Emergent Transfer

- secondary_domains: [multilingual-nlp, cross-lingual-transfer, large-language-models]
- aliases: [cross-lingual emergent capability, multilingual capability emergence, language transfer emergence]
- broader: [emergent-prompting-capability, multilingual-nlp]
- related: [cross-lingual-prompt-transfer, zero-shot-generalisation-mechanisms, few-shot-emergent-generalisation]
- prerequisites: [multilingual-language-models, cross-lingual-transfer, large-language-models]
- confidence: high

**definition**: Multilingual emergent transfer refers to the phenomenon in which a capability that a multilingual language model acquires from training data in one language (typically English) becomes accessible in other languages without explicit training on those capabilities in those languages. Instruction following, chain-of-thought reasoning, few-shot learning, and structured output generation emerge in non-English languages at lower model scales than was achieved by the same capabilities in English, suggesting that the model's representations of task structure transcend language-specific surface form once the representations are sufficiently rich. Transfer quality correlates strongly with the amount of pre-training data in the target language.

**key_claim**: Multilingual emergent transfer is asymmetric and proportional to the cross-lingual representation overlap established during pretraining — languages that share vocabulary (cognates, code-switching), script, or topical domain with English exhibit stronger transfer from English-only instruction tuning than typologically and orthographically distant languages, revealing that emergent transfer is mediated by the model's shared representational structure for semantically equivalent content rather than by any language-agnostic abstract reasoning capability.

**warning**: Multilingual emergent transfer creates an illusion of language support that masks significant performance gaps — a model that has been instruction-tuned only in English may appear to support a non-English language adequately on benchmark tasks that probe transfer-friendly capabilities (translation, basic QA) while failing dramatically on language-specific tasks (idiomatic expression, culturally situated reasoning, low-resource-language-specific entities) that do not benefit from English transfer; reporting benchmark results on transferred non-English capabilities without contrasting with native-language baselines systematically overstates multilingual support.

## Arithmetic Emergence Threshold

- secondary_domains: [mathematical-reasoning, scaling-laws, large-language-models]
- aliases: [arithmetic capability threshold, numerical reasoning emergence, math emergence in LLMs]
- broader: [emergent-prompting-capability, mathematical-reasoning]
- related: [chain-of-thought-emergence, scaling-and-capability-emergence, capability-elicitation-prompting]
- prerequisites: [large-language-models, arithmetic, scaling-laws]
- confidence: high

**definition**: Arithmetic emergence threshold refers to the scale and training condition at which language models transition from near-random performance on arithmetic tasks (multi-digit addition, multiplication, modular arithmetic) to reliable correct performance, a transition that is among the most dramatic and well-documented emergent capability transitions in the scaling literature. Below the threshold, models generate numerically plausible outputs with high confidence but inconsistent correctness; above the threshold, models perform multi-digit arithmetic with near-perfect accuracy when reasoning steps are elicited through chain-of-thought prompting. The threshold is not fixed but depends on the arithmetic task's complexity (number of digits, operation type, carryover structure) and whether chain-of-thought or tool-use augmentation is available.

**key_claim**: The arithmetic emergence threshold is not evidence for qualitatively new computational mechanisms at large scale — rather, it reflects the scale at which the model accumulates sufficient statistical co-occurrence between arithmetic subproblems and their correct intermediate and final results to generalise correctly rather than defaulting to the modal wrong answer; smaller models trained specifically on arithmetic data can achieve above-threshold arithmetic performance, demonstrating that the threshold is a function of the model's data efficiency for arithmetic rather than a fundamental scale-dependent capability.

**warning**: Arithmetic capability that emerges with scale via chain-of-thought prompting is not robust to distributional shifts in the format or representation of numbers — models may perform well on Arabic numeral arithmetic while failing on the same arithmetic problem stated in word-form ("three hundred and forty-seven plus two hundred and twelve") or in Roman numerals, revealing that arithmetic capability is tied to surface representation rather than generalising to abstract numerical computation; applications requiring reliable arithmetic across representation formats must use tool-augmented approaches rather than relying on intrinsic arithmetic capability.

## In-Context Learning as Meta-Learning

- secondary_domains: [meta-learning, in-context-learning, large-language-models]
- aliases: [ICL as meta-learning, few-shot learning as gradient-free meta-learning, in-context gradient descent]
- broader: [in-context-learning, meta-learning]
- related: [few-shot-emergent-generalisation, induction-heads, in-context-learning, task-generalisation-in-llms]
- prerequisites: [in-context-learning, meta-learning, gradient-descent]
- confidence: high

**definition**: The in-context learning as meta-learning hypothesis proposes that large language models perform in-context learning by implementing an implicit gradient-descent optimisation process in the forward pass — constructing a "task vector" from the demonstrations that encodes the task's gradient direction and applying it to the query, effectively performing one or more virtual update steps without modifying the model's weights. This hypothesis is supported by theoretical analysis showing that linear attention implements gradient descent in closed form, by activation patching experiments showing that task vectors are linearly represented in residual stream activations, and by the finding that in-context learning performance scales with demonstration quality in ways that parallel the sample efficiency of gradient-based meta-learning algorithms.

**key_claim**: The in-context learning as meta-learning hypothesis has strong empirical support from mechanistic experiments but is an approximation rather than an exact description of what large transformer models do — the true mechanism combines meta-learning-like task vector construction with retrieval of similar training instances, with the relative contribution of each component depending on whether the task is within or outside the training distribution; purely task-vector-based meta-learning accounts explain out-of-distribution in-context learning while retrieval-based accounts explain in-distribution performance, and a complete theory requires both.

**warning**: The meta-learning framing of in-context learning can mislead practitioners into overestimating the generalisation ability of in-context learning beyond the training distribution — meta-learning algorithms learn to learn within a task distribution, not to learn arbitrary new tasks, and in-context learning in LLMs similarly generalises to tasks that are structurally similar to tasks in the pretraining distribution while failing to learn genuinely novel algorithmic operations that are not implicitly present in the model's parameters, regardless of how many demonstrations are provided.

## Task Generalisation in LLMs

- secondary_domains: [generalisation, large-language-models, transfer-learning]
- aliases: [cross-task generalisation, task transfer in LLMs, multi-task generalisation]
- broader: [emergent-prompting-capability, generalisation]
- related: [zero-shot-generalisation-mechanisms, few-shot-emergent-generalisation, instruction-following-emergence]
- prerequisites: [large-language-models, transfer-learning, generalisation]
- confidence: high

**definition**: Task generalisation in LLMs refers to the ability of a model trained (or fine-tuned) on a set of tasks to perform well on new tasks not seen during training, including tasks from different domains, with different input-output formats, and requiring different reasoning processes. Task generalisation is the core capability that distinguishes general-purpose language models from task-specific models — it enables a single model to handle diverse user requests without task-specific fine-tuning. The degree of generalisation is bounded by the coverage and diversity of the pretraining and instruction-tuning task distributions and by the model's capacity to represent diverse task structures in a unified parameter space.

**key_claim**: Task generalisation in instruction-tuned LLMs is not uniform across task types but is concentrated in tasks that share structural properties with the instruction-tuning distribution — models generalise readily to new instances of known task types (new topics within question answering, new documents within summarisation) while failing to generalise to structurally novel tasks (new output formats, new reasoning patterns) that require compositional use of capabilities not combined in training, revealing that instruction following is more accurately described as task-type generalisation than as truly general instruction following.

**warning**: Reported broad task generalisation in commercial LLMs is partly attributable to instruction-tuning dataset scale and diversity rather than to fundamental generalisation mechanisms — models trained on thousands of task types appear to generalise broadly because most user tasks closely resemble tasks in the instruction-tuning distribution, not because the model has learned an abstract instruction-following principle; evaluating generalisation on structurally novel tasks designed to be outside the instruction-tuning distribution consistently reveals more limited generalisation than demonstrated on standard benchmarks.

## Zero-Shot Generalisation Mechanisms

- secondary_domains: [generalisation, large-language-models, natural-language-processing]
- aliases: [zero-shot capability mechanisms, zero-shot task performance, zero-shot learning in LLMs]
- broader: [task-generalisation-in-llms, in-context-learning]
- related: [instruction-following-emergence, task-generalisation-in-llms, semantic-grounding-in-llms]
- prerequisites: [large-language-models, zero-shot-learning, generalisation]
- confidence: high

**definition**: Zero-shot generalisation mechanisms in LLMs are the computational and statistical processes by which a model produces correct outputs for a task without any task-specific demonstration examples, relying entirely on the task description (instruction), the model's pretraining knowledge, and its instruction-following capability acquired during fine-tuning. The mechanisms include: pattern recognition over the instruction's surface form (recognising the instruction as an instance of a known task type), parametric knowledge retrieval (generating the factually correct answer from stored world knowledge), compositional reasoning (combining multiple known operations to address a novel instruction), and pragmatic intent inference (inferring what the user wants beyond the literal instruction).

**key_claim**: Zero-shot generalisation in instruction-tuned models is primarily driven by pattern matching between the instruction and the instruction-tuning template distribution rather than by reasoning over the instruction's meaning — models achieve high zero-shot performance on tasks where the instruction phrasing closely matches instruction-tuning templates and fail on semantically equivalent instructions phrased in non-template formats, a finding that challenges the narrative of robust zero-shot generalisation from instruction following and underscores the importance of instruction format standardisation.

**warning**: Zero-shot performance is a misleading metric for capability assessment when instruction-tuning data is not disclosed — a model that achieves high zero-shot performance may have seen tasks very similar to the evaluation tasks in its instruction-tuning set, making "zero-shot" performance a measure of generalisation within the instruction-tuning distribution rather than genuine zero-shot generalisation; comparisons of zero-shot performance across models with different instruction-tuning data must account for the potential overlap between evaluation tasks and training tasks.

## Capability Elicitation Prompting

- secondary_domains: [prompt-engineering, large-language-models, evaluation]
- aliases: [prompt-based capability elicitation, latent capability prompting, activation prompting]
- broader: [emergent-prompting-capability, prompt-engineering]
- related: [latent-capability-unlocking, chain-of-thought-emergence, emergent-prompting-capability, zero-shot-generalisation-mechanisms]
- prerequisites: [prompt-engineering, large-language-models]
- confidence: high

**definition**: Capability elicitation prompting is the practice of designing prompts specifically to reveal capabilities that are present in a model's parameters but not expressed under standard prompting conditions. Elicitation techniques include role prompting that activates expert knowledge frames ("You are an expert in X"), chain-of-thought framing that activates deliberative reasoning patterns, step-by-step decomposition that activates subgoal-following behaviour, explicit meta-prompting ("Think about what type of problem this is before answering"), and format scaffolding that provides structural cues matching the internal representation of the target capability. Capability elicitation is important for fair model evaluation and for maximising the practical utility of deployed models.

**key_claim**: Capability elicitation prompting demonstrates that standard prompt evaluation benchmarks systematically underestimate model capability — the same model with sophisticated elicitation prompting can outperform a larger model evaluated with a naive prompt on a wide range of reasoning and knowledge tasks, indicating that reported capability benchmarks measure the joint function of model capability and elicitation prompt quality rather than model capability alone; separating these two factors requires standardised elicitation protocols applied uniformly across evaluated models.

**warning**: Capability elicitation can produce a misleading picture of model reliability — a capability that requires elaborate elicitation to express is not as reliably accessible in deployment as the elicitation benchmark suggests, because real users will not always apply the specific elicitation technique that works best, and the model's response to an elicited prompt may be more fragile (prompt-brittleness-sensitive) than its response to a standard prompt; elicitation-based capability measurements should be reported alongside measurements of the capability's accessibility under typical user prompt conditions.

## Latent Capability Unlocking

- secondary_domains: [large-language-models, fine-tuning, prompt-engineering]
- aliases: [capability unlocking, latent skill activation, dormant capability activation]
- broader: [capability-elicitation-prompting, emergent-prompting-capability]
- related: [capability-elicitation-prompting, model-capability-vs-alignment-gap, instruction-following-emergence]
- prerequisites: [large-language-models, fine-tuning, prompt-engineering]
- confidence: high

**definition**: Latent capability unlocking refers to the process of activating capabilities that are present in a model's pretraining parameters but suppressed or inaccessible under the model's fine-tuned instruction-following regime. Unlocking can occur through: specialised prompting that bypasses safety filters or task-framing constraints, lightweight fine-tuning (LoRA, QLoRA) on domain-specific data that activates specialised pretraining knowledge, continued pretraining on domain data, and in-context learning from demonstrations that establish the required output regime. The unlocking concept implies that the capacity for the behaviour is stored in the pretrained weights and that fine-tuning serves as a key that either enables or restricts access rather than adding or removing capabilities.

**key_claim**: Latent capability unlocking via lightweight fine-tuning is disproportionately efficient relative to the number of parameters updated — LoRA fine-tuning with 0.1–1% of a model's parameters on domain data consistently achieves capability levels approaching full fine-tuning, suggesting that the domain capability is primarily in the frozen pretrained parameters and that fine-tuning primarily adjusts the routing and access patterns that determine which parameters contribute to which outputs rather than storing new knowledge in the fine-tuning parameters themselves.

**warning**: Latent capability unlocking has dual-use implications — the same technique that unlocks beneficial domain capabilities (medical reasoning, code generation) can unlock harmful capabilities that were suppressed by safety fine-tuning, as demonstrated by research showing that lightweight fine-tuning on benign data can partially degrade safety guardrails; organisations deploying models fine-tuned by third parties should assess whether fine-tuning has altered safety-relevant capability profiles, not just measured on the intended task.

## Model Capability vs. Alignment Gap

- secondary_domains: [ai-alignment, large-language-models, model-evaluation]
- aliases: [capability-alignment gap, alignment tax, safety-capability trade-off]
- broader: [large-language-models, ai-alignment]
- related: [latent-capability-unlocking, instruction-following-emergence, model-capability-vs-alignment-gap]
- prerequisites: [large-language-models, ai-alignment, rlhf]
- confidence: high

**definition**: The model capability versus alignment gap refers to the difference between what a model can do (its parametric capability, as measured under maximally elicited conditions) and what it will do (its aligned behaviour, as shaped by fine-tuning with RLHF, constitutional AI, or other alignment techniques). The gap reflects the alignment tax: alignment fine-tuning that makes the model helpful, harmless, and honest also restricts certain capabilities, changes the model's output distribution toward safer and more hedged responses, and can reduce performance on tasks where the most capable response would violate safety constraints. The gap is not constant across tasks: some capabilities are preserved or enhanced by alignment, while others are restricted.

**key_claim**: The capability-alignment gap is bidirectional — alignment fine-tuning both restricts capabilities (imposing the alignment tax on tasks that the model could perform but that conflict with safety or helpfulness constraints) and enhances capabilities (instruction following and format compliance improve substantially with alignment), meaning that the gap is not a simple performance deficit but a redistribution of capability across task types, with aligned models outperforming base models on most user-facing tasks while underperforming on tasks that require generating unrestricted or adversarial content.

**warning**: Treating the capability-alignment gap as purely a performance deficit leads to the incorrect conclusion that alignment should be reduced to maximise capability — empirical evidence consistently shows that well-aligned models outperform poorly aligned models of the same size on the vast majority of user tasks because alignment improves instruction following, response formatting, and refusal handling, all of which are capabilities required for real-world usefulness; the cases where alignment reduces performance are primarily narrow tasks that require generating content that alignment correctly restricts.

## Scaling and Capability Emergence

- secondary_domains: [scaling-laws, large-language-models, emergent-capabilities]
- aliases: [capability scaling, emergent capability thresholds, capability phase transitions in LLMs]
- broader: [emergent-prompting-capability, scaling-laws]
- related: [chain-of-thought-emergence, arithmetic-emergence-threshold, model-capability-vs-alignment-gap, instruction-following-emergence]
- prerequisites: [scaling-laws, large-language-models, emergent-capabilities]
- confidence: high

**definition**: Scaling and capability emergence refers to the phenomenon in which certain model capabilities appear to arise discontinuously at specific scale thresholds — appearing near-random below a threshold and above-chance above it — rather than improving smoothly and predictably with scale as measured by training loss. Documented emergent capabilities include chain-of-thought reasoning, multi-step arithmetic, multilingual translation, and BIG-Bench tasks; their emergence has been attributed to phase transitions in the model's internal representations, the crossing of thresholds required for reliable multi-step computation, and the accumulation of sufficient statistical signal for rare but functionally important patterns.

**key_claim**: The discreteness of observed capability emergence is largely a measurement artefact: emergent-looking discontinuities in accuracy metrics become smooth continuous improvements when the metric is changed from binary accuracy to a graded metric (log-probability, partial credit), confirming that the underlying model is improving continuously with scale and the apparent threshold is the scale at which continuous improvement crosses the random-performance baseline, not a fundamental phase transition in the model's computational mechanisms.

**warning**: The scaling-predicts-emergence framing has led to unwarranted extrapolation of capability curves beyond observed data points — the claim that sufficiently large models will exhibit emergent general intelligence or dangerous capabilities at some scale threshold is scientifically ungrounded if the evidence for discrete emergence is an artefact of metric choice; capability forecasting from scaling laws should use graded metrics and should acknowledge that the relationship between scale and specific capabilities may break down as training data quality, architecture, and training procedure matter more at the frontier than raw scale.

## Instruction-Following Emergence

- secondary_domains: [instruction-tuning, large-language-models, generalisation]
- aliases: [instruction following capability, general instruction following, generalised instruction compliance]
- broader: [emergent-prompting-capability, instruction-tuning]
- related: [zero-shot-generalisation-mechanisms, task-generalisation-in-llms, capability-elicitation-prompting, rlhf]
- prerequisites: [large-language-models, instruction-tuning, generalisation]
- confidence: high

**definition**: Instruction-following emergence refers to the acquisition by language models of the ability to generalise instruction-following to new tasks, formats, and domains not seen in the instruction-tuning dataset — producing appropriate outputs for novel instructions based on the model's understanding of natural-language instruction semantics rather than template matching. Instruction-following capability is distinct from the ability to complete any specific task: it is the meta-capability of correctly interpreting what a diverse range of instructions require and generating appropriate responses across task types. The capability emerges during instruction tuning and scales with the size and diversity of the instruction-tuning dataset as well as with model scale.

**key_claim**: Instruction-following emergence is primarily a function of instruction-tuning dataset diversity rather than model scale alone — models instruction-tuned on diverse task distributions (hundreds of different task types) exhibit qualitatively better cross-task generalisation than models fine-tuned on large but narrow instruction sets, confirming that the scope of instruction following generalisation is bounded by the structural diversity of the instruction-tuning distribution rather than by the total volume of instruction-tuning examples or the model's parameter count.

**warning**: Instruction-following emergence is measured primarily on structured benchmarks where the instruction is clear and the correct output is well-defined, creating an optimistic picture of instruction-following reliability; production deployments reveal that models trained for instruction following frequently misinterpret underspecified or pragmatically complex instructions by defaulting to their training-distribution modal response rather than inferring the user's specific intent, suggesting that instruction-following emergence measures response compliance for clear instructions rather than pragmatic intention-following for ambiguous ones.

## Calibration Emergence in Scale

- secondary_domains: [calibration, large-language-models, reliability]
- aliases: [calibration improvement with scale, scale-dependent calibration, calibration scaling]
- broader: [scaling-laws, calibration, large-language-models]
- related: [overconfidence-in-llm-outputs, verbalized-uncertainty, prompt-calibration-techniques, scaling-and-capability-emergence]
- prerequisites: [calibration, large-language-models, scaling-laws]
- confidence: high

**definition**: Calibration emergence in scale refers to the empirical finding that larger language models tend to be better calibrated — their expressed confidence scores and verbalized uncertainty are more accurately correlated with their actual error rates — than smaller models on the same tasks, when evaluated on the model's raw output probabilities before RLHF or instruction tuning. Base models show an improvement in calibration with scale on knowledge-intensive tasks, meaning that a large model's expressed probability for the correct answer more accurately reflects the probability that it will be right, while a small model's probabilities systematically over- or under-reflect its accuracy. However, instruction tuning and RLHF can degrade calibration even as they improve accuracy.

**key_claim**: Calibration emergence in scale represents an important but overlooked quality of large base models that is systematically degraded by instruction tuning — the RLHF training signal optimises for human-preferred response style rather than probability calibration, leading to instruction-tuned models that are more confident-sounding but less accurately calibrated than their base model counterparts; this means that deployed instruction-tuned models require explicit calibration correction mechanisms, and that calibration should be treated as a first-class model quality metric alongside accuracy in the evaluation of instruction-tuned models.

**warning**: Calibration emergence with scale applies primarily to the model's token-level probability output for knowledge-intensive factual questions, not to the model's verbalized confidence in conversational responses — the two can diverge dramatically after instruction tuning, with the probability-level calibration remaining approximately scale-proportionate while verbalized uncertainty becomes systematically overconfident due to RLHF preference for confident-sounding responses; calibration evaluation must measure both probability calibration and verbalized calibration as distinct metrics and should not assume they move together.
