---
batch_name: b01-11-system-design
batch_date: 2026-05-21
default_domain: llm-systems
default_confidence: high
notes: |
  Practical LLM system design concepts. Note: prompt-versioning, latency-quality-tradeoff,
  and prompt-caching-strategies already exist in v6-llm-elaborated — pipeline will auto-skip
  via --mode skip. Remaining 7 concepts are new.
---

# Batch: B01-11 Practical System Design

## Prompt Versioning

- secondary_domains: [mlops, software-engineering, prompt-engineering]
- aliases: [prompt version control, prompt management, versioned prompts, prompt changelog]
- broader: [prompt-engineering, mlops]
- narrower: []
- related: [prompt-registry-patterns, ab-testing-prompts, prompt-observability, prompt-caching-strategies]
- prerequisites: [prompt-engineering, version-control, software-engineering]
- confidence: high
- note: LIKELY EXISTS — pipeline will skip if file exists in output directory

**definition**: Prompt versioning is the practice of applying version control principles to prompt templates used in production LLM systems — maintaining a history of prompt changes, tagging versions, enabling rollback to previous prompt states, tracking the performance characteristics of each version, and managing the promotion of prompts through development, staging, and production environments. Prompt versioning treats prompts as first-class software artefacts subject to the same engineering rigour as code: change review, testing before promotion, documented rationale for changes, and automated regression testing.

**key_claim**: Prompt versioning is essential for production LLM systems because prompts are code — an unversioned prompt change in a production system is equivalent to deploying code without version control, making regression diagnosis, rollback, and change attribution impossible; the invisibility of prompt changes (unlike code changes, prompt edits may not be tracked in the application codebase) makes explicit versioning infrastructure more important, not less.

**warning**: Prompt versioning creates a false sense of reproducibility without accompanying model version pinning — a prompt version produces different outputs when run against different underlying model versions, meaning that a "version" of a prompt is only reproducible when both the prompt text and the model version are recorded; prompt versioning systems must record model version alongside prompt content to provide genuine reproducibility.

## Prompt Registry Patterns

- secondary_domains: [mlops, software-engineering, system-design]
- aliases: [prompt registry, centralised prompt store, prompt catalogue, prompt repository system]
- broader: [prompt-versioning, mlops, system-design]
- narrower: []
- related: [prompt-versioning, ab-testing-prompts, prompt-observability, prompt-caching-strategies, model-routing-strategies]
- prerequisites: [prompt-versioning, software-engineering, mlops, system-design]
- confidence: high

**definition**: A prompt registry is a centralised system for storing, versioning, discovering, and serving prompt templates to LLM-powered applications — analogous to a package registry (npm, PyPI) for code or a model registry (MLflow, Weights & Biases) for ML models. Prompt registries provide: a single source of truth for all production prompts, metadata (version, author, associated model, performance metrics, usage statistics), access controls (who can modify production prompts), environment management (dev/staging/prod promotion), programmatic API for prompt retrieval, and integration with monitoring and evaluation infrastructure. Commercial implementations include LangSmith Hub, PromptLayer, Brainlid, and Helicone.

**key_claim**: Centralising prompt management in a registry resolves the organisational problem of prompt sprawl — in systems without a prompt registry, production prompts exist in application code, environment variables, database records, and individual developers' notes, making it impossible to audit what is running in production, impossible to coordinate changes, and impossible to measure the impact of modifications; a prompt registry provides the organisational infrastructure for treating prompt engineering as a disciplined engineering practice.

**warning**: Prompt registries introduce a runtime dependency that must be highly available — if the prompt registry is unavailable, the entire application that retrieves prompts from it at runtime may fail; registries should include local caching, fallback to bundled defaults, and circuit breaker patterns to prevent a registry outage from cascading into application-level failures.

## A/B Testing Prompts

- secondary_domains: [mlops, experimentation, product-management]
- aliases: [prompt A/B testing, prompt experimentation, prompt split testing, controlled prompt experiments]
- broader: [prompt-versioning, mlops, experimentation]
- narrower: []
- related: [prompt-versioning, prompt-registry-patterns, prompt-observability, evals-as-a-product, human-preference-evaluation]
- prerequisites: [prompt-versioning, experimentation-methodology, statistics, mlops]
- confidence: high

**definition**: A/B testing prompts is the practice of running controlled experiments that compare two or more prompt variants simultaneously on live user traffic — routing a fraction of requests to a challenger prompt while the remainder receive the control prompt — and measuring the impact on defined success metrics (task completion rate, user satisfaction, output quality scores, latency, cost) to determine whether the challenger prompt improves on the control. Prompt A/B testing applies the same experimentation methodology used in product development to prompt engineering, enabling evidence-based prompt optimisation rather than relying on offline evaluation or intuition alone.

**key_claim**: A/B testing is the only reliable way to measure the production impact of prompt changes — offline evaluation (testing on a fixed dataset) measures performance on historical inputs and may not reflect the distribution of future live traffic, while online A/B testing captures the actual impact on the full range of inputs the system receives in production; the gap between offline evaluation and online A/B test results is frequently large enough to make offline-only prompt validation insufficient for high-stakes systems.

**warning**: A/B testing prompts requires sufficient traffic to achieve statistical power — small systems with low request volumes cannot achieve statistically significant A/B test results in reasonable timeframes, and premature conclusions from underpowered experiments lead to deploying prompts that appear to improve performance by chance; sample size calculations based on expected effect size and acceptable error rates should precede any A/B test launch, and minimum detectable effect sizes should be specified upfront.

## Latency-Quality Tradeoff

- secondary_domains: [llm-systems, performance-engineering, system-design]
- aliases: [latency vs quality tradeoff, speed-accuracy tradeoff, response time vs output quality]
- broader: [llm-systems, system-design]
- narrower: []
- related: [model-routing-strategies, batch-inference-optimization, cost-per-token-budgeting, prompt-caching-strategies]
- prerequisites: [llm-inference, system-design, performance-engineering]
- confidence: high
- note: LIKELY EXISTS — pipeline will skip if file exists in output directory

**definition**: The latency-quality tradeoff in LLM systems describes the inverse relationship between response latency and output quality across multiple design dimensions: model size (larger models produce better outputs but take longer to generate them), context length (more context generally improves quality but increases time-to-first-token), sampling parameters (more sampling steps improve quality estimates but increase latency), and reasoning depth (chain-of-thought improves accuracy but adds response length and time). System designers must explicitly navigate these tradeoffs by selecting appropriate models, context window usage patterns, and sampling configurations for their latency budget.

**key_claim**: The latency-quality tradeoff is not fixed — architectural innovations (speculative decoding, flash attention, KV cache optimisation) and hardware improvements continuously shift the Pareto frontier, enabling higher quality at the same latency or lower latency at the same quality over time; production system design should treat current latency-quality tradeoffs as temporary and build in mechanisms for upgrading to better model serving infrastructure as it becomes available.

**warning**: Latency-quality optimisation for LLM systems must account for perceived latency (user experience) as well as measured latency (wall clock time) — streaming token output dramatically improves perceived latency even when total generation time is unchanged, because users receive the beginning of the response immediately; optimising only for time-to-complete-response while ignoring time-to-first-token consistently produces worse user experience than the latency measurements suggest.

## Batch Inference Optimisation

- secondary_domains: [llm-systems, performance-engineering, mlops]
- aliases: [batch processing for LLMs, offline batch inference, LLM batching, continuous batching]
- broader: [llm-systems, performance-engineering]
- narrower: [continuous-batching, dynamic-batching]
- related: [latency-quality-tradeoff, cost-per-token-budgeting, model-routing-strategies, prompt-caching-strategies]
- prerequisites: [llm-inference, systems-programming, gpu-computing]
- confidence: high

**definition**: Batch inference optimisation refers to the techniques for maximising GPU utilisation and throughput when processing multiple LLM requests — as opposed to latency optimisation for single-request serving. In offline batch processing, requests are collected and processed together, filling available compute capacity more efficiently than sequential single-request serving. In online serving, continuous batching (also called iteration-level scheduling or in-flight batching) dynamically groups requests at the token generation level, inserting new requests into the batch as others complete rather than waiting for the entire batch to finish — dramatically improving GPU utilisation compared to static batching while maintaining low latency for incoming requests.

**key_claim**: Continuous batching is the most important systems-level optimisation for LLM serving throughput, achieving 10–30× higher throughput than naive static batching by eliminating the GPU idle time that occurs when static batches stall waiting for the longest-running request; the vLLM serving framework's implementation of continuous batching with PagedAttention (efficient KV cache management) became the reference implementation for high-throughput LLM serving.

**warning**: Batch inference optimisation trades per-request latency for system throughput — techniques that maximise GPU utilisation (continuous batching with large batch sizes) increase individual request queuing time when the system is at capacity; production serving systems must carefully size batch sizes and implement backpressure mechanisms to maintain acceptable tail latency under high load, not just optimise for mean throughput.

## Cost-Per-Token Budgeting

- secondary_domains: [llm-systems, cost-management, mlops]
- aliases: [token cost management, LLM cost optimisation, inference cost budgeting, per-token cost control]
- broader: [llm-systems, cost-management]
- narrower: []
- related: [model-routing-strategies, latency-quality-tradeoff, prompt-caching-strategies, batch-inference-optimization, output-length-control]
- prerequisites: [llm-inference, cost-management, system-design]
- confidence: high

**definition**: Cost-per-token budgeting is the practice of explicitly managing the token-denominated costs of LLM-powered systems — both input tokens (context length, system prompt size, retrieved documents) and output tokens (response length) — within defined per-request, per-user, or per-day budget constraints. Since LLM API pricing is typically linear in tokens (input and output priced separately), cost-per-token budgeting involves: auditing token usage across all prompt components, identifying high-cost low-value inputs (overly long system prompts, excessive retrieved context, redundant few-shot examples), implementing dynamic context window management to fit within token budgets, and selecting model tiers based on quality requirements versus cost constraints.

**key_claim**: System prompt and context token costs are frequently the dominant cost driver in production LLM systems and the most underoptimised — while output token optimisation (limiting response length) is obvious, input token costs from unnecessarily long system prompts, retrieved context that is not selectively filtered, and redundant few-shot examples can account for 50–90% of total token costs in context-heavy applications; rigorous token attribution analysis reveals that most production systems have significant cost reduction opportunities in input token management.

**warning**: Aggressive cost-per-token budgeting that reduces context quality degrades output quality in ways that are difficult to measure without comprehensive evaluation — removing retrieved context passages to save tokens may save cost while increasing hallucination rate; the cost-quality tradeoff must be quantified, not assumed, for any significant context reduction, and cost savings should be evaluated against downstream quality metrics rather than token counts alone.

## Model Routing Strategies

- secondary_domains: [llm-systems, system-design, cost-management]
- aliases: [LLM routing, query routing, model cascade, intelligent routing, LLM gateway routing]
- broader: [llm-systems, system-design]
- narrower: [cascade-routing, complexity-based-routing, semantic-routing]
- related: [cost-per-token-budgeting, latency-quality-tradeoff, fallback-prompt-chains, model-graded-evaluation]
- prerequisites: [llm-systems, system-design, multiple-model-deployment]
- confidence: high

**definition**: Model routing strategies are system design patterns that direct incoming requests to different LLM models (or model configurations) based on request characteristics — with the goal of matching model capability to task requirements while optimising cost and latency. A complexity-based router classifies requests by difficulty (simple factual questions → fast, cheap model; complex reasoning tasks → large, capable model). A semantic router maps request intent to purpose-built models (code questions → code model; mathematical queries → reasoning model). A cascade router first attempts a cheaper model and escalates to a more capable model only if the cheaper model's confidence is below threshold, minimising average cost while maintaining quality.

**key_claim**: Model routing strategies can achieve frontier-model quality at substantially lower average cost by routing the majority of requests (which are often simple) to cheaper, faster models while routing the minority of genuinely difficult requests to more capable models — empirical analyses of real production traffic distributions consistently show that 50–80% of requests can be handled well by cheaper models, meaning that routing strategies can reduce average inference cost by 50–70% with minimal quality impact on aggregate metrics.

**warning**: Model routing based on automated complexity classification introduces its own error rate — misclassified requests routed to the wrong model tier produce worse quality than a uniform high-capability model would; the routing model's false-negative rate (complex requests classified as simple) determines the frequency of quality failures, and routing strategies should be validated against quality metrics across the full request distribution before deployment.

## Fallback Prompt Chains

- secondary_domains: [llm-systems, reliability-engineering, system-design]
- aliases: [fallback chains, prompt fallback, graceful degradation for LLMs, retry chains]
- broader: [llm-systems, reliability-engineering]
- narrower: []
- related: [model-routing-strategies, prompt-versioning, prompt-observability, latency-quality-tradeoff, output-length-control]
- prerequisites: [llm-systems, reliability-engineering, system-design, error-handling]
- confidence: high

**definition**: Fallback prompt chains are system design patterns that define ordered sequences of alternative prompts, models, or response generation strategies that are tried in succession when earlier attempts fail or produce unsatisfactory outputs. Fallback scenarios include: model API unavailability (try primary model → try secondary model → return cached response → return static fallback), quality failures (attempt with long-context prompt → reduce context and retry → fall back to a simpler task formulation), latency timeouts (attempt with full prompt → retry with shortened prompt → return partial response), and content filtering triggers (attempt original request → attempt with rephrased request → return a graceful refusal message). Fallback chains implement graceful degradation, ensuring that a system provides some useful response even under failure conditions.

**key_claim**: Fallback prompt chains are necessary but commonly absent in early-stage LLM deployments because the immediate development priority is on the happy path, not failure handling — systems without fallback chains produce hard failures (errors, timeouts, blank responses) when any component fails, while systems with fallback chains degrade gracefully; the difference in user experience and system reliability between fallback-equipped and fallback-absent systems is substantial and disproportionate to the implementation cost.

**warning**: Fallback prompt chains must be monitored to prevent silent quality degradation — if the primary path frequently fails and the fallback is serving most responses, the system is degraded without obvious symptoms; tracking which fallback level serves each request and alerting when fallback activation rates exceed baselines is essential for maintaining awareness of system health.

## Prompt Observability

- secondary_domains: [mlops, monitoring, system-design]
- aliases: [LLM observability, prompt tracing, LLM monitoring, inference observability, AI observability]
- broader: [llm-systems, mlops, observability]
- narrower: []
- related: [prompt-versioning, prompt-registry-patterns, ab-testing-prompts, evals-as-a-product, cost-per-token-budgeting]
- prerequisites: [mlops, observability-engineering, llm-systems]
- confidence: high

**definition**: Prompt observability is the practice of instrumenting LLM-powered applications to provide full visibility into the inputs (prompts), outputs (completions), intermediate steps (tool calls, chain steps, retrieved context), associated metadata (model version, token counts, latency, cost), and quality metrics of every LLM invocation in production — enabling debugging, quality monitoring, cost tracking, and performance analysis of LLM systems at the same level of granularity available for traditional software systems. Prompt observability platforms (LangSmith, Helicone, Brainlid, Weights & Biases Prompts) capture request-response pairs, trace multi-step chains, and aggregate metrics across request populations.

**key_claim**: Prompt observability is the prerequisite for data-driven prompt engineering in production — without a complete record of what prompts are being sent, what responses are being received, and what quality metrics they achieve on live traffic, prompt optimisation is based on offline evaluation that may not reflect production behaviour; observability data reveals the real distribution of inputs and failure modes that offline evaluation misses, enabling targeted improvements with measured impact.

**warning**: Prompt observability platforms capture the full content of prompts and completions, which frequently contain sensitive user information — storing complete prompt-response logs creates a data retention and privacy liability that must be governed by an explicit data policy (PII scrubbing, retention limits, access controls, deletion procedures); systems that store prompt logs without a data governance policy create regulatory and ethical exposure that grows with the volume of logged interactions.
