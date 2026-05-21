---
batch_name: pe-14-cognitive-production
batch_date: 2026-05-20
default_domain: cognitive-science
default_confidence: high
notes: |
  Eighteen concepts across two clusters: cognitive science applied to LLMs and
  prompting (eight terms) and production deployment of prompt-based systems
  (ten terms). The cognitive science cluster draws on established frameworks —
  dual-process theory, cognitive load theory, working memory, schema theory,
  semantic priming, prototype theory, mental simulation, and epistemic
  uncertainty — and analyses how each framework illuminates LLM capabilities
  or prompt design principles. The production cluster covers the engineering
  practices required to deploy, monitor, and iterate on prompts in production:
  versioning, regression testing, latency-quality tradeoffs, caching,
  cost optimisation, monitoring, A/B testing, registry management,
  multi-model routing, and fallback strategies.
---

# Batch: PE-14 Cognitive Science and Production Deployment

## Dual-Process Theory Applied to LLMs

- domain: cognitive-science
- secondary_domains: [llm-theory, prompt-engineering, reasoning]
- aliases: [System 1 / System 2 in LLMs, fast and slow thinking LLMs, dual-process LLM prompting]
- broader: [cognitive-science, llm-theory]
- narrower: []
- related: [cognitive-load-theory-applied-to-llms, chain-of-thought-prompting, world-model-in-llms, mental-simulation-in-llms]
- prerequisites: [cognitive-science, dual-process-theory, chain-of-thought-prompting]
- confidence: medium

**definition**: Dual-Process Theory Applied to LLMs is the application of Kahneman's System 1 / System 2 framework to language model behaviour — treating standard next-token generation as a fast, intuitive, pattern-matching process (System 1 analogue) and chain-of-thought or deliberative reasoning as a slower, resource-intensive, step-by-step process (System 2 analogue). This framing suggests that prompts which require careful reasoning should activate the System 2 mode through explicit instructions ("think step by step", "before answering, reason through this carefully"), while routine retrieval tasks can be handled through direct generation without reasoning chains.

**key_claim**: The dual-process framing predicts the well-documented empirical finding that chain-of-thought prompting most benefits tasks that require deliberate multi-step reasoning (mathematics, logical inference, planning) rather than tasks that benefit from fast pattern retrieval (factual lookup, simple classification), supporting the prescription to use reasoning-eliciting prompts selectively rather than universally.

**warning**: The dual-process analogy is a useful heuristic but not a mechanistic model — LLMs do not have distinct System 1 and System 2 circuits; the analogy maps onto different prompting strategies and their effects, not onto internal model architecture, and extrapolating the analogy too far (e.g., claiming LLMs have genuine reflective awareness) leads to anthropomorphic mischaracterisations of model capabilities.

## Cognitive Load Theory Applied to LLMs

- domain: cognitive-science
- secondary_domains: [prompt-engineering, instructional-design, llm-capabilities]
- aliases: [cognitive load in prompting, extraneous load in prompts, intrinsic cognitive load LLM]
- broader: [cognitive-science, prompt-engineering]
- narrower: []
- related: [dual-process-theory-applied-to-llms, working-memory-constraints-in-prompts, schema-activation-in-prompts, prompt-engineering]
- prerequisites: [cognitive-load-theory, prompt-engineering]
- confidence: medium

**definition**: Cognitive Load Theory Applied to LLMs draws on Sweller's cognitive load theory — which distinguishes intrinsic load (complexity inherent in the task), extraneous load (complexity from poor presentation), and germane load (productive processing that builds schemas) — to analyse how prompt design affects LLM performance. Under this framework, complex prompts with poorly organised instructions, irrelevant context, or ambiguous task framing create extraneous processing demand that degrades task performance, while well-structured prompts with clear instruction hierarchy and progressive task complexity manage cognitive load to improve output quality.

**key_claim**: Extraneous cognitive load in prompts — created by redundant information, inconsistent terminology, unclear task hierarchy, or distracting context — measurably degrades LLM performance by consuming the model's effective context processing capacity, supporting prompt design principles that prioritise clarity, information hierarchy, and elimination of irrelevant context.

**warning**: Cognitive load theory was developed to explain human learning and performance, not language model processing — applying it to LLMs assumes a structural parallel between human working memory constraints and LLM attention-based context processing that may not hold in detail; the theory provides useful design intuitions but its specific predictions (such as the split-attention effect or redundancy effect) have not been systematically validated in LLM contexts.

## Working Memory Constraints in Prompts

- domain: cognitive-science
- secondary_domains: [prompt-engineering, llm-capabilities, context-window-management]
- aliases: [effective working memory LLMs, context processing limits, information chunk limits in prompts]
- broader: [cognitive-science, prompt-engineering, long-context-prompting-strategies]
- narrower: []
- related: [cognitive-load-theory-applied-to-llms, long-context-prompting-strategies, context-distillation, working-memory-proxies-in-llms]
- prerequisites: [working-memory-theory, prompt-engineering, long-context-prompting-strategies]
- confidence: medium

**definition**: Working Memory Constraints in Prompts refers to the observation that language models, despite their large context windows, have a limited effective capacity for actively integrating information within a prompt — analogous to human working memory limits. Empirically, models perform better when the information most relevant to the task is located near the generation point (recency bias), when competing or distracting information is minimised, and when complex information is chunked into digestible units rather than presented as a continuous dense block. These observations suggest prompt design should account for effective working memory limitations rather than assuming that all information in the context is equally accessible.

**key_claim**: The "lost in the middle" finding — that language models retrieve information more reliably from the beginning and end of long contexts than from the middle — empirically demonstrates that LLMs have effective working memory constraints that are not fully described by their nominal context window size, and that prompt organisation must account for positional accessibility of information.

**warning**: Working memory constraints in LLMs differ fundamentally from human working memory — LLMs do not have a time-decay-based forgetting mechanism, and their context processing limitations are better described by attention patterns and positional biases than by the capacity-based metaphor of human working memory; the cognitive science analogy provides useful design intuitions but should not be interpreted as a mechanistic claim about LLM internals.

## Schema Activation in Prompts

- domain: cognitive-science
- secondary_domains: [prompt-engineering, cognitive-science, few-shot-prompting]
- aliases: [schema priming in prompts, frame activation, cognitive schema prompting]
- broader: [cognitive-science, prompt-engineering]
- narrower: []
- related: [semantic-priming-effects, prototype-theory-and-llms, cognitive-load-theory-applied-to-llms, few-shot-prompting]
- prerequisites: [schema-theory, prompt-engineering, cognitive-science]
- confidence: medium

**definition**: Schema Activation in Prompts applies schema theory — the cognitive science framework holding that prior knowledge is organised into structured mental schemas that are activated by contextual cues — to the design of prompts. Under this framework, providing the model with context cues that match the schema associated with a target task (e.g., using technical vocabulary, framing the task as expert analysis, or providing few-shot examples in the target style) activates the corresponding knowledge schema and primes the model to produce outputs consistent with that schema. Role prompts, few-shot examples, and domain-specific context framing can all be understood as schema activation techniques.

**key_claim**: Schema activation is the cognitive mechanism underlying the effectiveness of role prompts and few-shot examples — by providing context that matches the schema of an expert in the target domain, the prompt activates the model's learned representations of how experts in that domain reason and write, shifting the generation distribution toward higher-quality, domain-appropriate outputs.

**warning**: Schema activation can cause over-application of a schema — if the activated schema is too narrow or specific, the model may apply it rigidly even in situations where flexibility or a different schema would produce better outputs, analogous to the cognitive science concept of schema-driven errors where prior expectations override accurate perception of new information.

## Semantic Priming Effects

- domain: cognitive-science
- secondary_domains: [prompt-engineering, llm-behaviour, natural-language-processing]
- aliases: [priming effects in LLMs, contextual priming, semantic activation spreading]
- broader: [cognitive-science, prompt-engineering]
- narrower: []
- related: [schema-activation-in-prompts, prototype-theory-and-llms, semantic-similarity-in-prompts, cognitive-load-theory-applied-to-llms]
- prerequisites: [cognitive-science, semantic-priming-theory, prompt-engineering]
- confidence: medium

**definition**: Semantic Priming Effects in LLMs refers to the phenomenon in which words, concepts, or context cues earlier in a prompt influence the generation of subsequent content in ways that go beyond the literal information provided — analogous to the cognitive science finding that exposure to a stimulus lowers the threshold for recognising or generating related stimuli. In prompting contexts, the vocabulary, tone, domain, and conceptual content of the preamble and instructions systematically prime the model's generation toward semantically related content and vocabulary, even for parts of the output that are not directly constrained by the instructions.

**key_claim**: Semantic priming in LLMs is a significant source of both prompt design opportunities and unintended prompt artifacts — using domain-specific vocabulary in the system prompt primes the model to use similar vocabulary throughout the response (an opportunity for style consistency), but unintended emotional, political, or stylistic priming in the preamble can influence subsequent model outputs in ways that the prompt author did not intend.

**warning**: Semantic priming effects are hard to control precisely — the model's response to semantic priming is an emergent property of the pre-training distribution that is difficult to predict from first principles, meaning that prompt engineers cannot fully anticipate which vocabulary choices will prime what associations, necessitating empirical testing rather than purely theoretical prompt design.

## Prototype Theory and LLMs

- domain: cognitive-science
- secondary_domains: [llm-theory, natural-language-processing, categorisation]
- aliases: [prototype-based categorisation LLMs, exemplar theory LLMs, typicality effects LLMs]
- broader: [cognitive-science, llm-theory]
- narrower: []
- related: [schema-activation-in-prompts, semantic-priming-effects, world-model-in-llms, few-shot-prompting]
- prerequisites: [prototype-theory, cognitive-science, natural-language-processing]
- confidence: medium

**definition**: Prototype Theory and LLMs examines how Rosch's prototype theory of categorisation — which holds that categories are represented by prototypical members rather than rigid definitions, and that instances are judged as category members by graded similarity to the prototype — maps onto LLM classification and generation behaviour. LLMs trained on human text exhibit typicality effects analogous to human categorisation: they respond more reliably and confidently to typical category members (a robin is a more typical bird than a penguin) than to atypical members, and they use prototypical exemplars as implicit reference points when generating category descriptions.

**key_claim**: Prototype-theory-based prompt design — using typical, central examples in few-shot demonstrations rather than unusual edge cases — activates the most stable and well-defined category representations in the model, producing more reliable classification and description performance than demonstrations based on atypical examples that lie near category boundaries.

**warning**: Prototype effects in LLMs reflect statistical patterns in training data distribution — a category's "prototype" in an LLM is the instance most frequently and centrally associated with the category label in the training corpus, which may not align with the prototype for the target user population, creating domain-specific misalignments that require careful few-shot example selection for each deployment context.

## Mental Simulation in LLMs

- domain: cognitive-science
- secondary_domains: [llm-capabilities, reasoning, world-model-in-llms]
- aliases: [mental model simulation, scenario simulation prompting, predictive simulation LLMs]
- broader: [cognitive-science, llm-capabilities, world-model-in-llms]
- narrower: []
- related: [world-model-in-llms, dual-process-theory-applied-to-llms, chain-of-thought-prompting, physical-reasoning]
- prerequisites: [cognitive-science, world-model-in-llms, llm-capabilities]
- confidence: medium

**definition**: Mental Simulation in LLMs refers to the model's capacity — observed empirically but imperfectly — to simulate the unfolding of events, processes, or scenarios in time, space, or causal structure, as if running an internal mental model of how the world works. When prompted to predict what will happen if a given action is taken, or to trace through the consequences of an event, models sometimes exhibit behaviour consistent with systematic simulation rather than pure pattern recall. Mental simulation capacity is relevant to planning tasks, physical reasoning, social reasoning, and counterfactual reasoning.

**key_claim**: Prompts that explicitly invoke mental simulation — "imagine stepping through this scenario one event at a time" or "trace what would happen physically if X occurred" — elicit more coherent causal reasoning than prompts that request direct answers, suggesting that the simulation capacity exists but requires activation through specific prompting patterns.

**warning**: LLMs fail systematically on tasks that require precise physical, spatial, or temporal simulation — the apparent simulation capacity observed on some tasks does not generalise reliably to all simulation tasks, and overconfident claims about LLM simulation ability based on successes in text-based scenario planning do not predict performance on tasks requiring accurate physical or spatial reasoning.

## Epistemological Uncertainty in LLMs

- domain: cognitive-science
- secondary_domains: [llm-calibration, alignment, prompt-engineering]
- aliases: [LLM epistemic uncertainty, uncertainty awareness prompting, LLM calibration]
- broader: [cognitive-science, llm-calibration]
- narrower: []
- related: [self-evaluation-prompting, llm-judge-calibration, fact-verification-prompting, cognitive-load-theory-applied-to-llms]
- prerequisites: [epistemology, llm-calibration, prompt-engineering]
- confidence: medium

**definition**: Epistemological Uncertainty in LLMs refers to a model's awareness of, and ability to communicate, the limits and reliability of its own knowledge — distinguishing between what it knows confidently, what it believes with uncertainty, and what it does not know. Well-calibrated epistemic uncertainty expressions improve user trust calibration by signalling when a model's outputs should be verified, and can be elicited through prompting techniques that instruct the model to explicitly state its confidence level, provide hedging language appropriate to its knowledge state, or refuse to answer when uncertainty is too high.

**key_claim**: Epistemic uncertainty expression is a critical safety-relevant prompt engineering concern — models that do not express appropriate uncertainty may state uncertain or incorrect claims with confident language, leading users to over-rely on unverified outputs; prompts that explicitly instruct the model to communicate uncertainty (using phrases like "I'm not certain but…" or "you should verify this") significantly improve user trust calibration in high-stakes domains.

**warning**: Current language models are poorly calibrated with respect to their stated confidence — models may express high confidence in incorrect claims and uncertainty about correct claims, and the calibration varies dramatically by domain, question type, and phrasing; expressed uncertainty should be treated as a qualitative signal rather than a reliable probabilistic estimate without empirical calibration for the specific use case.

## Prompt Versioning

- domain: production-deployment
- secondary_domains: [software-engineering, prompt-engineering, mlops]
- aliases: [prompt version control, prompt versioning system, prompt change management]
- broader: [production-deployment, prompt-engineering]
- narrower: []
- related: [prompt-regression-testing, prompt-registry-management, a-b-testing-prompts, prompt-monitoring-and-alerting]
- prerequisites: [prompt-engineering, software-version-control, mlops]
- confidence: high

**definition**: Prompt Versioning is the practice of applying systematic version control to prompt templates — tracking changes, maintaining history, and managing multiple versions of prompts across development and production environments, analogous to code version control. A prompt versioning system records: the prompt text at each version, the rationale for the change, evaluation metrics before and after the change, the model version the prompt was evaluated with, and the deployment date. Without versioning, prompt changes are difficult to audit, roll back, or diagnose when they cause production quality regressions.

**key_claim**: Prompt versioning is as important as code versioning for LLM-powered applications — prompts are program code in natural language form, and their unversioned modification is a leading cause of unexplained production quality regressions that are difficult to diagnose and fix without a prompt version history to compare against.

**warning**: Prompt versioning must be coupled with model version tracking — a prompt optimised for one model version may produce degraded outputs on a new model version, and version control systems that track prompt changes without tracking the model version the prompt was evaluated against cannot diagnose model-upgrade regressions.

## Prompt Regression Testing

- domain: production-deployment
- secondary_domains: [software-testing, prompt-engineering, mlops]
- aliases: [prompt test suites, prompt quality regression, prompt evaluation CI]
- broader: [production-deployment, prompt-engineering]
- narrower: []
- related: [prompt-versioning, prompt-monitoring-and-alerting, a-b-testing-prompts, prompt-registry-management]
- prerequisites: [prompt-engineering, software-testing, mlops]
- confidence: high

**definition**: Prompt Regression Testing is the practice of maintaining a suite of test cases — prompt inputs with expected or evaluated outputs — and running the prompt against this suite whenever the prompt or the underlying model changes, to detect quality regressions before they reach production. Test cases cover: the happy path, known edge cases, previously problematic inputs (regression tests from past failures), and boundary conditions. Regression test results are typically expressed as aggregate quality metrics (precision on a classification task, preference win rate, factuality score) that can be compared against a baseline.

**key_claim**: Prompt regression testing prevents silent prompt quality degradation — without regression testing, prompt changes or model upgrades may degrade performance on previously handled cases while appearing to improve the target case, creating a whack-a-mole dynamic where fixing one failure introduces new ones; systematic regression testing catches these regressions before deployment.

**warning**: Prompt regression test suites require active maintenance — test cases that were challenging at the time of creation may become trivially easy as models improve, or they may become irrelevant as the application's requirements change, requiring periodic review and augmentation of the test suite to remain an effective quality gate.

## Latency-Quality Tradeoff

- domain: production-deployment
- secondary_domains: [mlops, prompt-engineering, infrastructure]
- aliases: [inference latency vs quality, speed-accuracy tradeoff LLMs, latency-accuracy Pareto]
- broader: [production-deployment, mlops]
- narrower: []
- related: [cost-per-token-optimization, multi-model-routing, prompt-caching-strategies, fallback-prompt-strategies]
- prerequisites: [llm-inference, production-deployment]
- confidence: high

**definition**: The Latency-Quality Tradeoff in LLM systems describes the fundamental engineering tension between response latency (time to first token and time to complete token) and output quality — techniques that improve quality (larger models, longer generation, chain-of-thought reasoning, best-of-N selection) typically increase latency and cost, while techniques that reduce latency (smaller models, speculative decoding, shorter outputs) often reduce quality. Managing this tradeoff requires identifying the quality floor required for the specific application and then optimising for minimum latency given that constraint.

**key_claim**: The latency-quality Pareto frontier varies by application — conversational applications typically require latency < 2 seconds for user experience acceptability, which constrains the model size and generation strategy independently of quality considerations; analytical applications can tolerate multi-second or multi-minute latency in exchange for higher quality, creating fundamentally different system design requirements for the same underlying models.

**warning**: Latency measurement must account for tail latency (99th percentile) rather than just median latency — LLM inference has high variance latency due to variable output length, batching effects, and infrastructure variability, and systems designed for median latency requirements will frequently violate user experience thresholds due to tail latency spikes.

## Prompt Caching Strategies

- domain: production-deployment
- secondary_domains: [infrastructure, prompt-engineering, cost-optimization]
- aliases: [KV cache reuse, prefix caching, prompt cache management]
- broader: [production-deployment, cost-per-token-optimization]
- narrower: []
- related: [cost-per-token-optimization, latency-quality-tradeoff, multi-model-routing, prompt-versioning]
- prerequisites: [llm-inference, kv-cache, production-deployment]
- confidence: high

**definition**: Prompt Caching Strategies refer to techniques for reducing the computational cost and latency of LLM inference by caching and reusing the key-value (KV) cache computed for the prompt prefix — specifically the system prompt and any fixed context that does not change between requests. When a new request arrives with the same prompt prefix as a previous request, the cached KV states for that prefix can be reused directly, avoiding recomputation. Many inference providers and APIs now support prompt caching as a cost-reduction feature; effective cache utilisation requires structuring prompts with fixed prefixes and dynamic suffixes.

**key_claim**: Prompt caching is one of the highest-leverage cost optimisation techniques available for production LLM applications with repeated prompt structure — applications with long system prompts processed across millions of requests can achieve 50–90% reduction in compute costs for the system prompt prefix by structuring prompts to maximise cache hit rates, with commensurate latency benefits due to reduced computation.

**warning**: Prompt caching invalidation requires careful management — cached KV states become stale when the prompt prefix changes (e.g., during system prompt updates), and stale cache usage can cause the model to respond based on the old system prompt rather than the updated one; cache invalidation policies must be coordinated with prompt versioning to prevent stale cache states from causing silent behaviour regressions.

## Cost Per Token Optimisation

- domain: production-deployment
- secondary_domains: [mlops, infrastructure, prompt-engineering]
- aliases: [token cost optimization, LLM cost management, inference cost reduction]
- broader: [production-deployment, mlops]
- narrower: []
- related: [latency-quality-tradeoff, prompt-caching-strategies, multi-model-routing, fallback-prompt-strategies]
- prerequisites: [llm-inference, production-deployment, token-economics]
- confidence: high

**definition**: Cost Per Token Optimisation encompasses the engineering practices for reducing the monetary cost of LLM inference at scale, measured in dollars per million input or output tokens. Optimisation strategies include: prompt compression (reducing input token count through summarisation or extraction), output length control (instructing models to be concise), model routing (using smaller, cheaper models for simpler queries), prompt caching (reusing KV states for repeated prefixes), batching (grouping requests to improve GPU utilisation), and quantisation (using lower-precision model weights to reduce memory and compute). Each strategy involves trade-offs with output quality and system complexity.

**key_claim**: Cost per token optimisation is often the determining factor for production LLM application viability — applications that are technically functional at development scale frequently become economically unviable at production scale without systematic cost optimisation, making cost analysis a first-class engineering concern from early development rather than a post-launch optimisation.

**warning**: Cost optimisation that reduces output quality may have hidden costs that exceed the direct inference savings — if cost-optimised outputs require more human review, produce higher user churn, or generate downstream errors that require correction, the total cost of ownership may be higher than for the more expensive higher-quality approach, requiring total cost of ownership analysis rather than inference cost analysis alone.

## Prompt Monitoring and Alerting

- domain: production-deployment
- secondary_domains: [mlops, observability, prompt-engineering]
- aliases: [prompt quality monitoring, LLM output monitoring, production prompt observability]
- broader: [production-deployment, mlops]
- narrower: []
- related: [prompt-regression-testing, prompt-versioning, a-b-testing-prompts, prompt-registry-management]
- prerequisites: [mlops, observability, production-deployment]
- confidence: high

**definition**: Prompt Monitoring and Alerting refers to the production observability practices applied to LLM-powered applications — collecting, analysing, and alerting on prompt inputs, model outputs, latency, cost, and quality metrics in real time. Monitoring covers: output quality degradation detection (using automated quality metrics or sample-based human review), anomalous input detection (identifying queries outside the training distribution or policy boundaries), latency and cost tracking, safety and policy violation detection, and user satisfaction signals. Effective alerting notifies on-call teams when quality or safety metrics cross defined thresholds.

**key_claim**: Production LLM systems without monitoring are operationally blind — unlike deterministic software where errors produce exceptions, LLM quality degradation is gradual and silent (outputs continue to be generated but at lower quality), making automated monitoring with defined quality thresholds the only reliable mechanism for detecting production quality regressions.

**warning**: Monitoring metrics for LLM outputs are imperfect proxies for the quality dimensions that matter — automated metrics (BLEU, ROUGE, perplexity, self-consistency scores) capture some quality dimensions but miss others (creativity, safety, reasoning correctness), and monitoring systems that rely entirely on automated metrics without human-in-the-loop review will fail to catch quality failures that fall in the gap between the metrics.

## A/B Testing Prompts

- domain: production-deployment
- secondary_domains: [experimentation, prompt-engineering, mlops]
- aliases: [prompt A/B testing, prompt split testing, prompt experimentation]
- broader: [production-deployment, experimentation]
- narrower: []
- related: [prompt-versioning, prompt-regression-testing, prompt-monitoring-and-alerting, prompt-registry-management]
- prerequisites: [a-b-testing, prompt-engineering, production-deployment]
- confidence: high

**definition**: A/B Testing Prompts is the application of controlled experimentation principles to prompt optimisation — splitting production traffic between two or more prompt variants and measuring outcome metrics (quality scores, user satisfaction, task completion rates, engagement) to determine which variant performs better. Prompt A/B testing requires: a reliable traffic splitting mechanism, sample size calculation to detect meaningful effect sizes with statistical power, a defined primary metric and guardrail metrics, and statistical significance testing before concluding the experiment. The result is an empirical quality comparison that is robust to the subjective biases of offline prompt evaluation.

**key_claim**: A/B testing is the gold standard for prompt optimisation decisions in production — offline evaluation metrics frequently fail to predict production performance due to distribution mismatch between test datasets and production traffic, and A/B testing against production traffic with real users and real queries provides the only reliable signal that a prompt change will improve the metric it was designed to improve.

**warning**: A/B testing prompts requires careful metric selection — optimising for easy-to-measure metrics (click-through rate, response length) rather than the true quality dimension of interest (user satisfaction, task accuracy) can cause the winning prompt variant to be the one that games the measurement metric rather than genuinely performing better, a form of Goodhart's law applied to prompt optimisation.

## Prompt Registry Management

- domain: production-deployment
- secondary_domains: [software-engineering, mlops, prompt-engineering]
- aliases: [prompt registry, prompt store, prompt management system, prompt catalog]
- broader: [production-deployment, prompt-engineering]
- narrower: []
- related: [prompt-versioning, prompt-regression-testing, a-b-testing-prompts, prompt-monitoring-and-alerting]
- prerequisites: [prompt-engineering, software-engineering, mlops]
- confidence: high

**definition**: Prompt Registry Management refers to the practice of maintaining a centralised repository — the prompt registry — that stores, versions, and governs all production prompts used across an organisation or application. A prompt registry provides: a single source of truth for prompt definitions, version history and rollback capability, metadata (model version, evaluation metrics, deployment dates, owners), access control and approval workflows for prompt changes, and search and discovery for prompt reuse. The registry enables coordination across teams working with multiple LLM-powered features and prevents prompt sprawl in which different teams independently maintain overlapping prompts.

**key_claim**: Prompt registry management becomes essential at scale — organisations with more than a few LLM-powered features quickly accumulate dozens or hundreds of prompts across products and teams, and without a registry these prompts exist as fragmented configuration strings in code repositories, databases, and documentation files, making it impossible to audit, update, or reason about the organisation's total prompt inventory.

**warning**: Prompt registries create dependency management complexity — when a shared base prompt is updated in the registry, all features that depend on it must be re-evaluated and potentially updated, creating a dependency graph that must be managed explicitly to prevent registry-wide regression from a single prompt change.

## Multi-Model Routing

- domain: production-deployment
- secondary_domains: [mlops, infrastructure, prompt-engineering]
- aliases: [model routing, LLM router, intelligent model selection, query routing]
- broader: [production-deployment, mlops]
- narrower: []
- related: [latency-quality-tradeoff, cost-per-token-optimization, fallback-prompt-strategies, prompt-registry-management]
- prerequisites: [production-deployment, mlops, llm-capabilities]
- confidence: high

**definition**: Multi-Model Routing is a production infrastructure pattern in which incoming queries are classified and routed to different language models based on query characteristics — typically balancing cost, latency, and quality requirements. A router analyses each query and directs it to the cheapest and fastest model capable of handling it at acceptable quality: simple factual queries go to a small, fast, cheap model; complex reasoning tasks go to a large, capable, expensive model; domain-specific queries may go to a fine-tuned specialist model. Routing logic can be rule-based, classification-model-based, or LLM-based.

**key_claim**: Multi-model routing reduces inference costs by 50–80% in applications with heterogeneous query complexity distributions — the insight is that production traffic contains a mix of simple and complex queries, and routing all traffic through a large expensive model overpays for the simple queries while routing everything through a small cheap model under-serves the complex queries; the router exploits this distribution.

**warning**: Router errors create tail quality failures — when the router misclassifies a complex query as simple and routes it to a small model, the user receives a degraded response that the system does not recognise as suboptimal (because the small model still produces a fluent, plausible-looking output), making routing errors difficult to detect without quality monitoring and creating a failure mode that is systematically harder to catch than model errors.

## Fallback Prompt Strategies

- domain: production-deployment
- secondary_domains: [reliability-engineering, prompt-engineering, mlops]
- aliases: [prompt fallback, model fallback chain, degraded-mode prompt, graceful degradation]
- broader: [production-deployment, reliability-engineering]
- narrower: []
- related: [multi-model-routing, latency-quality-tradeoff, prompt-monitoring-and-alerting, prompt-registry-management]
- prerequisites: [production-deployment, reliability-engineering, prompt-engineering]
- confidence: high

**definition**: Fallback Prompt Strategies are reliability patterns for LLM applications that define graceful degradation behaviours when primary model calls fail or produce unacceptable outputs — analogous to try-catch error handling in traditional software. A fallback chain might specify: try the primary model; if unavailable, try a secondary model API; if the response fails quality checks, retry with a simplified prompt; if quality remains insufficient, return a safe default response. Fallback strategies ensure that model unavailability or quality failures produce bounded, predictable degradation rather than application errors that surface to users.

**key_claim**: Fallback prompt strategies are a critical reliability engineering requirement for production LLM applications — primary model APIs have non-trivial downtime rates and latency spikes, quality failures are stochastic, and applications without defined fallback behaviour will surface unexpected errors to users when these events occur; the fallback chain is the LLM application's equivalent of error handling and defensive programming.

**warning**: Fallback strategies introduce response inconsistency — a user who receives a primary-model response and then a fallback-model response to similar queries may observe noticeable quality or style differences that create a confusing user experience, requiring that fallback responses be designed to blend with primary responses as much as possible or be explicitly communicated to users as operating in a reduced-capability mode.
