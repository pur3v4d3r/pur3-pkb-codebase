---
batch_name: pe-05-agents-and-evaluation
batch_date: 2026-05-20
default_domain: prompt-engineering
default_confidence: high
notes: |
  Twenty-three concepts covering agentic LLM frameworks and evaluation methods.
  Agentic section covers ReAct, plan-and-execute, reflexion agents, toolformer,
  function calling, multi-agent debate, hierarchical orchestration, scratchpad,
  chain-of-action, task decomposition, critic agents, and self-refine.
  Evaluation section covers LLM-as-judge, CoT faithfulness, hallucination
  detection, factual consistency, prompt sensitivity, benchmark overfitting,
  GSM8K, HotpotQA, calibration, and uncertainty quantification.
---

# Batch: PE-05 Agentic Frameworks and Evaluation

## ReAct Reasoning Acting

- secondary_domains: [agent-frameworks, reasoning]
- aliases: [ReAct, reason-then-act, synergised reasoning and acting]
- broader: [agentic-frameworks]
- related: [plan-and-execute-agents, chain-of-action, agent-scratchpad, tool-use-in-llms, function-calling]
- prerequisites: [chain-of-thought-prompting, large-language-models, tool-use-in-llms]
- confidence: high

**definition**: ReAct Reasoning Acting is a prompting framework in which the language model interleaves reasoning traces (thought steps) with action calls (tool invocations or environment interactions) in an alternating sequence, so each action is preceded by an explicit reasoning step that justifies it and each action result is followed by a reasoning step that interprets the result and plans the next action.

**key_claim**: ReAct Reasoning Acting resolves the core limitation of chain-of-thought-only reasoning for multi-step tasks that require external information: by grounding each reasoning step in real environment feedback rather than allowing the reasoning chain to hallucinate evidence, ReAct substantially reduces compounding errors over long action sequences and produces reasoning traces that are interpretable and revisable by human supervisors.

**warning**: ReAct Reasoning Acting degrades gracefully but not robustly on long-horizon tasks; as the thought-action trace grows, the model's effective context for planning the next action shrinks, and older parts of the trace may be effectively ignored due to attention dilution, causing the model to repeat actions, lose track of prior conclusions, or fail to maintain consistent sub-goal tracking across many steps.

## Plan-and-Execute Agents

- secondary_domains: [agent-frameworks, task-planning]
- aliases: [plan-then-execute, two-phase agent, planner-executor agent]
- broader: [agentic-frameworks]
- related: [react-reasoning-acting, task-decomposition-agents, hierarchical-agent-orchestration, chain-of-action]
- prerequisites: [large-language-models, task-decomposition-agents, agentic-frameworks]
- confidence: high

**definition**: Plan-and-Execute Agents are a two-phase agent architecture in which a planner module first generates a complete multi-step plan for the task before any execution begins, and an executor module then carries out each plan step sequentially — separating the strategic planning function from the tactical execution function to allow higher-quality planning without the distraction of moment-to-moment action selection.

**key_claim**: Plan-and-Execute Agents outperform reactive agents on tasks with predictable structure by front-loading the reasoning about task decomposition: by producing the full plan before execution, the planner can reason about step ordering, anticipate dependencies between sub-tasks, and allocate tool calls efficiently — advantages that reactive interleaved approaches cannot fully realise because each step only reasons about the next immediate action.

**warning**: Plan-and-Execute Agents are brittle when the environment is stochastic or partially observable; if an early execution step produces unexpected results that invalidate the assumptions underlying the remaining plan, the executor has no native mechanism to trigger replanning, and the agent will continue executing a plan that is no longer valid unless explicit replanning triggers are built into the architecture.

## Reflexion Agent Architecture

- secondary_domains: [agent-frameworks, self-improvement]
- aliases: [Reflexion agents, reflective agent, self-reflecting agent]
- broader: [agentic-frameworks, reflexion]
- related: [reflexion, react-reasoning-acting, critic-agents, self-refine, chain-of-verification]
- prerequisites: [large-language-models, agentic-frameworks, reflexion]
- confidence: high

**definition**: Reflexion Agent Architecture is an agent framework in which the agent maintains an episodic memory of past attempts and their outcomes, uses a self-reflection component to generate verbal summaries of what went wrong in failed attempts, and incorporates these reflections into subsequent attempts — enabling the agent to improve across trials without gradient updates by using language-mediated self-critique as the learning signal.

**key_claim**: Reflexion Agent Architecture demonstrates that language-mediated trial-and-error learning is viable for LLM agents: by externalising failure analysis into explicit reflection notes stored in the agent's memory, the architecture enables systematic improvement over multiple attempts at the same task, achieving performance on complex reasoning and decision-making benchmarks that significantly exceeds that of non-reflective baselines.

**warning**: Reflexion Agent Architecture's improvement depends critically on the quality of the reflection model; if the reflection model fails to identify the true cause of failure (a common occurrence when failures arise from subtle world-model errors rather than obvious reasoning mistakes), the stored reflection notes will encode incorrect causal attributions that guide subsequent attempts in the wrong direction, and the agent may confidently repeat its original errors under the impression that it has learned from them.

## Toolformer

- secondary_domains: [tool-use, self-supervised-learning]
- aliases: [Toolformer model, tool-using LLM]
- broader: [tool-use-in-llms, agentic-frameworks]
- related: [tool-use-in-llms, function-calling, react-reasoning-acting, agentic-frameworks]
- prerequisites: [large-language-models, fine-tuning, tool-use-in-llms]
- confidence: high

**definition**: Toolformer is a method for training language models to use external tools — such as calculators, search engines, calendars, and translation systems — by having the model self-supervise its own tool-use training data: the model generates candidate tool call insertions in text, evaluates whether the tool output improves perplexity on the subsequent tokens, and retains only beneficial tool calls, creating a self-curated dataset for tool-use fine-tuning.

**key_claim**: Toolformer demonstrates that tool-use capability can be bootstrapped from a small number of few-shot tool-use examples without massive human annotation: the self-supervised filtering mechanism leverages the model's own language modelling objective to determine which tool calls are genuinely useful, producing high-quality tool-use training data at scale that enables the model to learn when — and when not — to invoke each tool.

**warning**: Toolformer's self-supervised data generation is biased toward tool calls that reduce perplexity on the immediately following text, which may not align with tool calls that improve final task accuracy; a tool call that retrieves slightly tangential information may reduce perplexity on the next tokens (because it introduces domain vocabulary) while actually degrading the quality of the final answer, meaning the self-supervised signal selects for locally plausible rather than globally useful tool use.

## Function Calling

- secondary_domains: [api-design, tool-use]
- aliases: [structured tool calling, JSON function calling, API tool use]
- broader: [tool-use-in-llms]
- related: [tool-use-in-llms, toolformer, react-reasoning-acting, agentic-frameworks]
- prerequisites: [large-language-models, tool-use-in-llms, json]
- confidence: high

**definition**: Function Calling is a capability of instruction-tuned language models to generate structured, schema-conformant outputs that represent calls to predefined external functions — specifying the function name and argument values in a machine-parseable format (typically JSON) — rather than describing tool use in free-form prose, enabling reliable programmatic parsing and execution of the model's tool invocation decisions.

**key_claim**: Function Calling resolves the reliability gap between the model's intent to use a tool and the downstream system's ability to parse and execute that intent; by constraining the tool-invocation output to a structured schema rather than free text, function calling makes tool use robust to the surface variation and formatting inconsistencies that make prose-based tool invocation pipelines brittle at production scale.

**warning**: Function Calling can produce schema-valid outputs that are semantically incorrect — the function name and argument types may be valid according to the schema while the argument values are hallucinated or inappropriate for the current context; schema validation catches structural errors but not semantic errors, meaning function calling reduces (but does not eliminate) the need for downstream validation of the model's tool invocation decisions.

## Tool Use in LLMs

- secondary_domains: [agentic-frameworks, api-integration]
- aliases: [LLM tool use, external tool integration, augmented language models]
- broader: [agentic-frameworks]
- narrower: [function-calling, toolformer, react-reasoning-acting]
- related: [function-calling, toolformer, react-reasoning-acting, retrieval-augmented-generation]
- prerequisites: [large-language-models, agentic-frameworks]
- confidence: high

**definition**: Tool Use in LLMs refers to the capability of language models to invoke external software tools — including search engines, code interpreters, databases, APIs, and calculators — during inference to overcome limitations of parametric knowledge and to perform operations that require precise symbolic computation rather than approximate statistical generation.

**key_claim**: Tool Use in LLMs extends the effective capability frontier of language models beyond what is achievable through generation alone: by delegating precise, verifiable operations (arithmetic, database queries, code execution, real-time information retrieval) to purpose-built tools, the model can focus its generative capacity on reasoning, planning, and communication while tools handle the operations where LLM generation is systematically unreliable.

**warning**: Tool Use in LLMs introduces security attack surfaces that are not present in generation-only systems; external tool calls can trigger side effects, expose sensitive data, or be manipulated by adversarial content in the environment (prompt injection via tool outputs), and the composability of tool calls means that a single compromised tool invocation can cascade through a multi-step agent pipeline with significant real-world consequences.

## Multi-Agent Debate

- secondary_domains: [multi-agent-systems, ensemble-methods]
- aliases: [society of mind prompting, multi-agent argumentation, LLM debate]
- broader: [agentic-frameworks, ensemble-methods]
- related: [critic-agents, self-refine, self-consistency-sampling, agentic-frameworks]
- prerequisites: [large-language-models, agentic-frameworks]
- confidence: high

**definition**: Multi-Agent Debate is a prompting strategy in which multiple instances of a language model each independently generate a response to the same input, then engage in multiple rounds of argumentation where each agent reads the other agents' responses and revises its own position, converging on a final answer through the adversarial dialogue process.

**key_claim**: Multi-Agent Debate achieves error correction through structured disagreement: independent agents often make different errors, and the debate process creates pressure to defend claims with reasoning — exposing unsupported assertions that would survive unchallenged in single-agent generation, empirically improving accuracy on complex reasoning tasks compared to single-agent chain-of-thought or majority voting across independent samples.

**warning**: Multi-Agent Debate exhibits a capitulation failure mode in which minority-position agents abandon correct positions to conform with the majority, especially when the majority agents express their incorrect positions confidently; the social dynamics of argumentation modelled by the LLM can override epistemic standards, meaning debate can increase rather than decrease error rates on tasks where the majority agents initially converge on the wrong answer.

## Hierarchical Agent Orchestration

- secondary_domains: [multi-agent-systems, system-design]
- aliases: [hierarchical agent architecture, orchestrator-subagent pattern, master-worker agent]
- broader: [agentic-frameworks, multi-agent-systems]
- related: [plan-and-execute-agents, task-decomposition-agents, multi-agent-debate, react-reasoning-acting]
- prerequisites: [large-language-models, agentic-frameworks, task-decomposition-agents]
- confidence: high

**definition**: Hierarchical Agent Orchestration is a multi-agent architecture in which an orchestrator agent decomposes a complex task into sub-tasks and delegates each sub-task to specialised subordinate agents, coordinates the results, and synthesises a final response — creating a management layer that abstracts over the implementation details of each sub-task's execution.

**key_claim**: Hierarchical Agent Orchestration enables parallelism and specialisation that flat agent architectures cannot achieve: subordinate agents can be optimised for their specific sub-task types, multiple sub-tasks can be executed concurrently, and the orchestrator's context remains focused on high-level coordination rather than being consumed by the implementation details of every sub-task — improving both throughput and task performance on complex, heterogeneous workflows.

**warning**: Hierarchical Agent Orchestration amplifies the cost of orchestrator-level planning errors; an incorrect decomposition at the top level propagates to all subordinate agents, and the synthesis step cannot recover information that was not delegated for retrieval or computation — making the orchestrator's initial task decomposition a high-stakes single point of failure whose errors are expensive to diagnose because they manifest in the subordinates' outputs rather than in the orchestrator's own actions.

## Agent Scratchpad

- secondary_domains: [agent-frameworks, working-memory]
- aliases: [agent working memory, agent notepad, intermediate reasoning buffer]
- broader: [agentic-frameworks, extended-thinking-architecture]
- related: [react-reasoning-acting, inner-monologue-technique, extended-thinking-architecture, chain-of-action]
- prerequisites: [large-language-models, agentic-frameworks, chain-of-thought-prompting]
- confidence: high

**definition**: Agent Scratchpad is a designated section of the agent's context window used to record intermediate reasoning steps, tool outputs, partial conclusions, and working hypotheses during multi-step task execution — functioning as an explicit working memory space that accumulates evidence and planning state across a sequence of actions before the final answer is synthesised.

**key_claim**: Agent Scratchpad externalises the agent's working memory into the context window, making the reasoning process auditable and persistent across tool calls; without a dedicated scratchpad, the agent must re-derive intermediate conclusions at each step from the growing action-result trace, introducing redundant computation and risking loss of key intermediate findings that have been pushed out of effective attention range.

**warning**: Agent Scratchpad has finite capacity bounded by the context window, and long-running agentic tasks accumulate scratchpad content that eventually crowds out the original task specification or early important findings; without explicit scratchpad management strategies (compression, summarisation, or structured note-taking), the scratchpad becomes a liability rather than an asset as task length grows.

## Chain of Action

- secondary_domains: [agent-frameworks, planning]
- aliases: [action chain, sequential action execution, action sequence planning]
- broader: [agentic-frameworks, react-reasoning-acting]
- related: [react-reasoning-acting, plan-and-execute-agents, task-decomposition-agents, agent-scratchpad]
- prerequisites: [large-language-models, agentic-frameworks, tool-use-in-llms]
- confidence: high

**definition**: Chain of Action is an agent execution pattern in which a sequence of discrete actions — each consuming the output of the previous action as input — is planned or executed in series to accomplish a complex goal that cannot be achieved by any single action, with the agent maintaining state and context across the action sequence to ensure coherent progress toward the goal.

**key_claim**: Chain of Action formalises the sequential dependency structure of multi-step agentic tasks: by representing task execution as a directed chain where each action's output is a direct input to the next, the architecture makes inter-action dependencies explicit, enables systematic failure localisation (the error can be traced to the specific action step where the chain diverges from the correct trajectory), and supports resumability when a step fails.

**warning**: Chain of Action creates compounding error propagation: an incorrect output at step N is passed as a correct input to step N+1, which builds on the error and passes a further-corrupted output to step N+2, and so on; without validation gates between chain links, errors accumulate multiplicatively, and the chain's final output can be arbitrarily wrong while each individual step appears locally reasonable given its corrupted input.

## Task Decomposition Agents

- secondary_domains: [agent-frameworks, problem-solving]
- aliases: [task decomposition, sub-goal generation, hierarchical task planning]
- broader: [agentic-frameworks, plan-and-execute-agents]
- related: [plan-and-execute-agents, hierarchical-agent-orchestration, decomposed-prompting, least-to-most-prompting]
- prerequisites: [large-language-models, agentic-frameworks, decomposed-prompting]
- confidence: high

**definition**: Task Decomposition Agents are agent systems designed to recursively break complex tasks into smaller, more tractable sub-tasks, either statically before execution begins or dynamically during execution as the agent discovers that a current sub-task requires further subdivision — enabling the agent to handle task complexity that exceeds what a single generation step can address reliably.

**key_claim**: Task Decomposition Agents operationalise the divide-and-conquer principle for LLM reasoning: by reducing each generation step to a manageable cognitive unit, decomposition reduces the per-step reasoning complexity and the associated error rate, and the correctness of the overall solution can be maintained by verifying each sub-task independently before integration — a quality assurance structure unavailable in non-decomposed approaches.

**warning**: Task Decomposition Agents introduce decomposition overhead and risk; the decomposition step itself is a reasoning operation that can fail, producing a set of sub-tasks that together do not cover the original task, that contain duplications, or that impose an ordering that makes later sub-tasks impossible to execute with the outputs of earlier ones — and these structural decomposition errors are harder to detect than sub-task execution errors because they are not visible in any single sub-task's output.

## Critic Agents

- secondary_domains: [agent-frameworks, quality-assurance]
- aliases: [evaluator agent, judge agent, review agent]
- broader: [agentic-frameworks, llm-as-judge]
- related: [llm-as-judge, self-refine, multi-agent-debate, chain-of-verification]
- prerequisites: [large-language-models, agentic-frameworks, llm-as-judge]
- confidence: high

**definition**: Critic Agents are specialised agent components whose role is to evaluate the outputs of other agents or the generating agent itself, identifying errors, inconsistencies, policy violations, or quality deficiencies and providing structured feedback that the generating agent uses to revise its outputs — implementing a separation of generation and evaluation concerns within a multi-agent pipeline.

**key_claim**: Critic Agents improve output quality by externalising the evaluation function: a model that generates and evaluates its own output in the same forward pass cannot maintain full independence between the generation and evaluation perspectives, but a dedicated critic agent — which may use a different model, different prompting strategy, or different context — applies genuinely independent evaluation criteria, reducing the self-serving bias that afflicts single-agent self-critique.

**warning**: Critic Agents can introduce critic-induced degradation when the critic's evaluation criteria are misaligned with the actual quality objective; a critic that penalises verbosity may cause the generator to produce responses that satisfy the critic while omitting information the user needs, and a critic that rewards confident-sounding claims may incentivise the generator to sound more certain than the evidence warrants — making critic alignment a critical design consideration alongside generator alignment.

## Self-Refine

- secondary_domains: [iterative-refinement, self-improvement]
- aliases: [iterative self-refinement, self-improvement loop, generate-refine loop]
- broader: [agentic-frameworks, reflexion]
- related: [reflexion, critic-agents, chain-of-verification, reflexion-based-prompt-refinement]
- prerequisites: [large-language-models, chain-of-thought-prompting]
- confidence: high

**definition**: Self-Refine is an iterative prompting framework in which a model generates an initial response, then generates feedback on that response, then generates a revised response incorporating the feedback — repeating this generate-feedback-refine cycle multiple times until a stopping criterion is met, without any external feedback or additional training.

**key_claim**: Self-Refine demonstrates that LLMs can serve as their own quality-improvement mechanisms on many tasks: the same model that made the initial errors often has sufficient meta-knowledge to identify those errors when prompted to critique rather than generate, and applying this critique iteratively produces outputs that measurably outperform single-pass generation on tasks including dialogue generation, code writing, and mathematical reasoning.

**warning**: Self-Refine has a ceiling determined by the model's evaluation capability; if the model cannot reliably identify the errors in its own outputs (which is often the case for subtle factual errors or complex logical fallacies), the feedback loop will not converge toward the correct answer but will instead converge toward a local optimum defined by the model's evaluation standards — which may be systematically lower than the true quality standard the user requires.

## LLM as Judge

- secondary_domains: [evaluation, quality-assurance]
- aliases: [model-based evaluation, LLM evaluator, GPT-as-judge]
- broader: [evaluation-methods, agentic-frameworks]
- related: [critic-agents, chain-of-thought-faithfulness, hallucination-detection, factual-consistency-evaluation]
- prerequisites: [large-language-models, evaluation-methods]
- confidence: high

**definition**: LLM as Judge is an evaluation paradigm in which a language model, rather than a human annotator or a programmatic metric, is used to assess the quality, correctness, helpfulness, or safety of another model's outputs — leveraging the LLM's language understanding and task knowledge to provide scalable, nuanced evaluations that approximate expert human judgement at a fraction of the annotation cost.

**key_claim**: LLM as Judge enables evaluation at scales and granularities that human annotation cannot support, making it the practical foundation for evaluating open-ended generation tasks where reference-based metrics (BLEU, ROUGE, exact match) are inadequate; empirical studies show that well-prompted LLM judges achieve agreement rates with human annotators comparable to inter-human agreement on many text quality dimensions.

**warning**: LLM as Judge inherits systematic biases from the judge model's training, including preference for verbosity, familiarity with certain writing styles, positional bias (favouring the first of two options presented), and self-enhancement bias (models tend to rate outputs resembling their own training data more favourably) — biases that can corrupt evaluation results in ways that are hard to detect without extensive calibration against human judgements.

## Chain of Thought Faithfulness

- secondary_domains: [interpretability, evaluation]
- aliases: [CoT faithfulness, reasoning trace fidelity, thought-action coherence]
- broader: [evaluation-methods, chain-of-thought-prompting]
- related: [chain-of-thought-prompting, hallucination-detection, llm-as-judge, factual-consistency-evaluation]
- prerequisites: [chain-of-thought-prompting, large-language-models, evaluation-methods]
- confidence: high

**definition**: Chain of Thought Faithfulness is the degree to which a model's explicitly generated reasoning trace accurately reflects the internal computational process that produced the final answer — measuring whether the stated reasoning is the actual causal mechanism behind the conclusion or a post-hoc rationalisation constructed to appear logically compelling while the answer was determined by other means.

**key_claim**: Chain of Thought Faithfulness is a critical evaluation dimension for reasoning transparency because unfaithful reasoning traces are misleading in exactly the cases where reasoning visibility is most needed; a model that produces a plausible but fabricated reasoning chain gives operators false confidence in the traceability of its decisions, making unfaithful CoT more dangerous than no CoT at all from an oversight perspective.

**warning**: Chain of Thought Faithfulness is currently unmeasurable with complete reliability: there is no definitive method to verify whether a stated reasoning step causally influenced the final token predictions or was generated independently, and indirect faithfulness tests (such as corrupting reasoning steps and measuring answer changes) are imperfect proxies that can give misleading faithfulness estimates on specific task types.

## Hallucination Detection

- secondary_domains: [factuality, evaluation]
- aliases: [hallucination identification, factual error detection, confabulation detection]
- broader: [evaluation-methods, hallucination-taxonomy]
- related: [hallucination-taxonomy, factual-consistency-evaluation, llm-as-judge, chain-of-verification]
- prerequisites: [large-language-models, evaluation-methods, natural-language-inference]
- confidence: high

**definition**: Hallucination Detection is the task of automatically identifying whether a language model's output contains fabricated, unsupported, or factually incorrect claims — including both intrinsic hallucinations (contradictions of provided source material) and extrinsic hallucinations (unverifiable claims not derivable from the source) — using methods ranging from NLI-based entailment checking to retrieval-based verification and LLM-as-judge approaches.

**key_claim**: Hallucination Detection is a prerequisite for deploying language models in high-stakes applications, but it remains an open research problem rather than a solved engineering challenge; current detection methods have substantial false negative rates on subtle factual errors, and the methods that are most accurate (human expert review) are not scalable, creating a reliability gap between what is measurable and what is deployable.

**warning**: Hallucination Detection systems trained on one domain or hallucination type often fail to generalise to others; a detector calibrated on Wikipedia-style factual claims may miss domain-specific technical errors, and a detector that identifies citation hallucinations may completely miss logical hallucinations where the claims are individually accurate but their stated causal relationship is fabricated — making coverage across hallucination types a critical but rarely evaluated dimension.

## Factual Consistency Evaluation

- secondary_domains: [evaluation, natural-language-inference]
- aliases: [factual consistency, source grounding evaluation, faithfulness evaluation]
- broader: [evaluation-methods, hallucination-detection]
- related: [hallucination-detection, hallucination-taxonomy, llm-as-judge, chain-of-thought-faithfulness]
- prerequisites: [large-language-models, natural-language-inference, evaluation-methods]
- confidence: high

**definition**: Factual Consistency Evaluation is the assessment of whether a generated text is consistent with a given reference source — such as a retrieved document, a conversation history, or a provided fact base — measuring the degree to which the generation introduces claims that are not supported by or contradict the reference, independently of the generation's absolute factual accuracy relative to world knowledge.

**key_claim**: Factual Consistency Evaluation decouples source grounding from world-knowledge accuracy, enabling evaluation of RAG and summarisation systems on the tractable question of "does this generation faithfully represent its source?" rather than the intractable question of "is this generation true?"; this decomposition makes factual consistency a practically measurable evaluation target that can be automated at scale, unlike global factual accuracy.

**warning**: Factual Consistency Evaluation metrics can be gamed by generations that are technically consistent with the source but misleading to the reader; a generation that omits critical context from the source, cherry-picks only the source's uncertainty statements, or frames source content in a misleading way may score high on consistency metrics while providing a substantially distorted picture of the source's content — highlighting the gap between consistency and usefulness as evaluation objectives.

## Prompt Sensitivity Analysis

- secondary_domains: [robustness, evaluation]
- aliases: [prompt robustness evaluation, instruction sensitivity, prompt fragility testing]
- broader: [evaluation-methods, prompt-optimization]
- related: [prompt-paraphrasing, benchmark-overfitting, llm-as-judge, label-sensitivity-in-icl]
- prerequisites: [large-language-models, evaluation-methods, prompt-formatting]
- confidence: high

**definition**: Prompt Sensitivity Analysis is the systematic evaluation of how much a model's performance varies across semantically equivalent or minimally different prompt formulations — measuring the instability in model outputs caused by surface-level changes to the instruction wording, question framing, or few-shot example selection, to quantify and diagnose prompt fragility.

**key_claim**: Prompt Sensitivity Analysis reveals that reported benchmark performance is often contingent on the specific prompt formulation used, not just the model's underlying capability; high sensitivity scores indicate that performance numbers are not reproducible across natural prompt variations, making sensitivity analysis an essential component of rigorous LLM evaluation that is systematically underreported in published benchmarks.

**warning**: Prompt Sensitivity Analysis requires many evaluation runs to produce statistically reliable sensitivity estimates, and the cost scales with both the number of prompt variants and the benchmark size; in practice, most published evaluations use a single prompt formulation per task, meaning that apparent capability differences between models may reflect prompt-model interaction effects rather than genuine capability differences.

## Benchmark Overfitting

- secondary_domains: [evaluation, meta-learning]
- aliases: [benchmark contamination, dataset contamination, benchmark saturation]
- broader: [evaluation-methods]
- related: [gsm8k-benchmark, hotpotqa-benchmark, calibration-in-llms, prompt-sensitivity-analysis]
- prerequisites: [large-language-models, evaluation-methods, machine-learning]
- confidence: high

**definition**: Benchmark Overfitting refers to the phenomenon in which a model achieves high scores on a specific evaluation benchmark due to exposure to the benchmark's questions or answers during pretraining or fine-tuning, rather than due to genuine capability in the skill the benchmark was designed to measure — contaminating benchmark performance as an indicator of generalisation ability.

**key_claim**: Benchmark Overfitting is endemic in frontier LLM evaluation because the training corpora of large language models often contain benchmark data from the internet, and the distinction between "the model memorised this benchmark item" and "the model has the skill this item tests" is not detectable from accuracy scores alone; this contamination invalidates benchmark comparisons as capability measurements to an unknown degree that is rarely disclosed or measured.

**warning**: Benchmark Overfitting cannot be fully prevented by held-out evaluation sets because new benchmarks eventually become training data for the next generation of models; this creates an evaluation arms race where benchmarks must be continuously created to stay ahead of training data coverage, and the community's reliance on saturated benchmarks for capability claims introduces systematic overestimation of progress that misleads both researchers and practitioners.

## GSM8K Benchmark

- secondary_domains: [evaluation, mathematics]
- aliases: [GSM8K, Grade School Math 8K, elementary math reasoning benchmark]
- broader: [benchmark-overfitting, evaluation-methods]
- related: [benchmark-overfitting, chain-of-thought-prompting, calibration-in-llms, hotpotqa-benchmark]
- prerequisites: [large-language-models, evaluation-methods, chain-of-thought-prompting]
- confidence: high

**definition**: GSM8K Benchmark is an evaluation dataset of approximately 8,500 grade-school-level mathematical word problems requiring multi-step arithmetic reasoning, designed to test LLMs' ability to perform elementary mathematical reasoning through natural language problem solving — serving as a standard benchmark for measuring step-by-step numerical reasoning capability.

**key_claim**: GSM8K Benchmark became the primary benchmark driving chain-of-thought research because it is difficult enough to differentiate models that reason in steps from those that attempt direct answer prediction, yet tractable enough for meaningful progress to be measured; its problems require genuine multi-step reasoning but not advanced mathematical knowledge, making it a clean test of the reasoning process rather than the knowledge of mathematical techniques.

**warning**: GSM8K Benchmark has been heavily saturated by frontier models and is increasingly affected by benchmark contamination; models now routinely achieve near-perfect scores on GSM8K, and these scores reflect a combination of genuine mathematical reasoning improvement and training-data contamination that is practically impossible to disentangle — making GSM8K a weak discriminator for comparing current frontier models and an unreliable signal for extrapolating mathematical reasoning to harder problems.

## HotpotQA Benchmark

- secondary_domains: [evaluation, multi-hop-reasoning]
- aliases: [HotpotQA, multi-hop question answering benchmark]
- broader: [benchmark-overfitting, evaluation-methods]
- related: [benchmark-overfitting, iterative-retrieval, dense-passage-retrieval, retrieval-augmented-generation]
- prerequisites: [large-language-models, evaluation-methods, information-retrieval]
- confidence: high

**definition**: HotpotQA Benchmark is a multi-hop question answering dataset that requires reasoning over two or more Wikipedia documents to answer each question, specifically designed to evaluate a model's ability to perform multi-step reasoning by identifying supporting facts across multiple passages and synthesising them into a coherent answer.

**key_claim**: HotpotQA Benchmark exposes the distinction between retrieval accuracy and reasoning accuracy: a system can retrieve both relevant documents correctly but still fail to synthesise the multi-hop reasoning chain, and conversely a system can appear to answer correctly by exploiting statistical shortcuts in the dataset without performing genuine multi-hop reasoning — making HotpotQA evaluation results difficult to interpret as pure measures of either retrieval or reasoning capability.

**warning**: HotpotQA Benchmark's multi-hop structure has been found to be partially shortcuttable: many questions in the dataset can be answered using only one of the required supporting passages rather than genuinely integrating both, because the question wording or answer pattern provides sufficient signal without multi-hop reasoning; models that exploit these shortcuts achieve competitive scores without developing the intended multi-hop reasoning capability.

## Calibration in LLMs

- secondary_domains: [evaluation, uncertainty-quantification]
- aliases: [LLM calibration, confidence calibration, probability calibration]
- broader: [evaluation-methods, uncertainty-quantification-llms]
- related: [uncertainty-quantification-llms, hallucination-detection, benchmark-overfitting, calibration]
- prerequisites: [large-language-models, probability-theory, evaluation-methods]
- confidence: high

**definition**: Calibration in LLMs is the alignment between a model's expressed confidence in its responses and the actual accuracy of those responses — a well-calibrated model expresses 80% confidence only on claims it gets right 80% of the time, while an overconfident model expresses high certainty on claims it gets wrong and an underconfident model expresses low certainty on claims it reliably gets right.

**key_claim**: Calibration in LLMs is a critical safety property for high-stakes applications: a poorly calibrated model that is confidently wrong is more dangerous than an accurately uncertain one, because overconfidence suppresses the user's natural scepticism and reduces the likelihood of verification, making calibration failure a precursor to harm in domains such as medical advice, legal interpretation, and financial guidance.

**warning**: Calibration in LLMs is frequently degraded by RLHF training; reinforcement learning from human feedback tends to reward confident, assertive responses because human raters often prefer confident answers over hedged ones, systematically training models toward overconfidence — meaning calibration and perceived response quality are in tension, and improving one often comes at the cost of degrading the other.

## Uncertainty Quantification LLMs

- secondary_domains: [evaluation, reliability]
- aliases: [LLM uncertainty quantification, epistemic uncertainty in LLMs, UQ for language models]
- broader: [evaluation-methods, calibration-in-llms]
- related: [calibration-in-llms, hallucination-detection, llm-as-judge, prompt-sensitivity-analysis]
- prerequisites: [large-language-models, probability-theory, calibration-in-llms]
- confidence: high

**definition**: Uncertainty Quantification for LLMs is the set of methods for estimating and communicating the degree of uncertainty in a language model's predictions, distinguishing between aleatoric uncertainty (inherent ambiguity in the task or query) and epistemic uncertainty (the model's lack of knowledge about the correct answer), to enable users and downstream systems to make risk-appropriate decisions based on model outputs.

**key_claim**: Uncertainty Quantification for LLMs is technically challenging because language model probabilities are not raw measures of epistemic uncertainty — they reflect the training distribution's frequency of tokens, not the model's knowledge state — and eliciting calibrated uncertainty from language models requires either specialised training objectives, ensemble methods, or auxiliary uncertainty models rather than naive confidence scores from the generation process.

**warning**: Uncertainty Quantification for LLMs based on token-level probabilities fails for high-level semantic uncertainty: a model may assign high probability to each token in a response while being deeply uncertain about the overall claim, and conversely may express high semantic confidence (e.g., "I am certain that...") while generating tokens at relatively low probability; bridging the gap between token-level probability and sentence-level semantic confidence remains an open research problem.
