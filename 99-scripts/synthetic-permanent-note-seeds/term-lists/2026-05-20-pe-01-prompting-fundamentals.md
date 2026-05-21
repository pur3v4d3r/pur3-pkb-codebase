---
batch_name: pe-01-prompting-fundamentals
batch_date: 2026-05-20
default_domain: prompt-engineering
default_confidence: high
notes: |
  Fifteen foundational prompting concepts covering the core vocabulary and
  mechanics of writing effective prompts for large language models. Covers
  zero-shot through chain-of-thought techniques, role mechanics, and
  structural formatting principles. Intended as the foundation layer for
  all downstream prompt-engineering permanent notes.
---

# Batch: PE-01 Prompting Fundamentals

## Zero-Shot Prompting

- secondary_domains: [llm-inference, natural-language-processing]
- aliases: [zero-shot inference, zero-shot prediction]
- broader: [prompting]
- narrower: [zero-shot chain-of-thought]
- related: [few-shot-prompting, one-shot-prompting, instruction-following]
- prerequisites: [large-language-models]
- confidence: high

**definition**: Zero-Shot Prompting is the practice of asking a large language model to perform a task by providing only the task description and the input, without including any worked examples or demonstrations in the prompt. The model must rely entirely on patterns learned during pretraining and instruction-tuning to generate an appropriate response.

**key_claim**: Zero-Shot Prompting reveals the extent to which a model has internalised a task format from pretraining alone; strong zero-shot performance is the primary signal of a well-instruction-tuned model, because it confirms that capability generalises beyond memorised input–output pairs.

**warning**: Zero-Shot Prompting is often assumed to be simpler than few-shot prompting, but ambiguous or underspecified task descriptions frequently produce worse outputs under zero-shot conditions than under few-shot conditions, because examples do more than demonstrate format — they constrain the interpretation of the task.

## Few-Shot Prompting

- secondary_domains: [in-context-learning, natural-language-processing]
- aliases: [few-shot in-context learning, few-shot ICL]
- broader: [in-context-learning, prompting]
- narrower: [one-shot-prompting]
- related: [zero-shot-prompting, chain-of-thought-prompting, demonstration-diversity]
- prerequisites: [large-language-models, in-context-learning]
- confidence: high

**definition**: Few-Shot Prompting is the practice of prepending a small number of worked input–output examples to a prompt so that the model can infer the expected task format, output style, and reasoning pattern from the demonstrations rather than from the task description alone. The examples act as a transient, prompt-level specification of the desired behaviour.

**key_claim**: Few-Shot Prompting shifts task specification from natural-language description — which is inherently ambiguous — to ostensive demonstration, and empirical evidence consistently shows that even two or three high-quality examples outperform elaborate zero-shot instructions on format-sensitive tasks.

**warning**: Few-Shot Prompting is sensitive to the ordering and surface features of the examples; models can pick up on spurious correlations in the demo set (e.g., all correct outputs having a particular length or lexical pattern), leading to brittle behaviour that appears excellent in development and fails silently at deployment.

## One-Shot Prompting

- secondary_domains: [in-context-learning, natural-language-processing]
- aliases: [single-shot prompting, one-example prompting]
- broader: [few-shot-prompting, prompting]
- related: [zero-shot-prompting, few-shot-prompting, demonstration-diversity]
- prerequisites: [large-language-models, in-context-learning]
- confidence: high

**definition**: One-Shot Prompting is a special case of few-shot prompting in which exactly one worked example is included in the prompt context before the target input. The single demonstration anchors the model's interpretation of the task format and expected output style without the overhead of constructing a full few-shot set.

**key_claim**: One-Shot Prompting often captures most of the format-specification benefit of few-shot prompting for highly constrained output formats, because a single high-quality example disambiguates structure completely, making the marginal value of additional demonstrations negligible for such tasks.

**warning**: One-Shot Prompting is particularly vulnerable to atypical or unrepresentative examples; with only one demonstration, an outlier example can bias the model's output distribution far more severely than it would in a three- or five-shot set where the remaining examples provide corrective signal.

## System Prompt Design

- secondary_domains: [llm-deployment, instruction-following]
- aliases: [system message design, system-level prompting]
- broader: [prompting]
- related: [instruction-following, role-prompting, persona-assignment, output-format-specification]
- prerequisites: [large-language-models, instruction-following]
- confidence: high

**definition**: System Prompt Design is the craft of writing the persistent, high-authority instruction block that frames an LLM's behaviour across an entire conversation or API session. The system prompt sets the model's persona, operating constraints, output style, and task scope before any user turn, and typically carries higher interpretive weight than user instructions in aligned models.

**key_claim**: System Prompt Design is the single highest-leverage point in a deployed LLM application because it establishes the interpretation context for every downstream user message; poorly scoped or ambiguous system prompts propagate their defects into every response, while well-designed ones make the entire interaction robust to prompt variation.

**warning**: System Prompt Design is not a security boundary in itself; sophisticated users can often override, extract, or circumvent system-prompt instructions through carefully crafted user messages, which means security-critical constraints must be enforced at the application layer, not solely in the system prompt text.

## Instruction Following

- secondary_domains: [alignment, llm-training]
- aliases: [instruction compliance, instruction adherence]
- broader: [alignment]
- related: [system-prompt-design, prompt-clarity-principles, instruction-hierarchy-conflict]
- prerequisites: [large-language-models, reinforcement-learning-from-human-feedback]
- confidence: high

**definition**: Instruction Following is the capacity of a language model to execute explicit directives contained in a prompt accurately, completely, and without silent reinterpretation — including format constraints, scope limitations, persona maintenance, and multi-step procedural requirements.

**key_claim**: Instruction Following is the core behavioural objective of instruction-tuning; models that fail at it do not merely produce suboptimal outputs but actively violate user intent in ways that are difficult to detect without systematic testing, because surface fluency is orthogonal to directive compliance.

**warning**: Instruction Following degrades non-linearly with prompt complexity; adding more constraints to a single prompt eventually causes the model to satisfy some directives while silently dropping others, and empirical evidence shows that mid-prompt constraints are disproportionately likely to be ignored.

## Prompt Formatting

- secondary_domains: [prompt-engineering, llm-inference]
- aliases: [prompt structure, prompt layout]
- broader: [prompting]
- related: [delimiters-and-separators, output-format-specification, prompt-clarity-principles]
- prerequisites: [large-language-models]
- confidence: high

**definition**: Prompt Formatting refers to the deliberate structuring of a prompt's visual and syntactic layout — including the use of headings, labels, delimiters, whitespace, and markdown — to communicate structure to the model, reduce ambiguity about role boundaries, and improve parse reliability for complex multi-part instructions.

**key_claim**: Prompt Formatting affects model behaviour not through aesthetics but through tokenisation and attention patterns; structured prompts that clearly demarcate instruction sections from data sections reduce the probability that the model conflates instruction tokens with content tokens, which is the root cause of many instruction-following failures.

**warning**: Prompt Formatting guidelines are model-family specific; markdown that significantly improves performance in one model family can degrade it in another (especially base models without markdown fine-tuning), so formatting choices established on one model should be re-validated when switching providers.

## Prompt Clarity Principles

- secondary_domains: [technical-writing, llm-inference]
- aliases: [prompt clarity, clear prompting]
- broader: [prompting]
- related: [instruction-following, prompt-formatting, negative-prompting, positive-framing-in-prompts]
- prerequisites: [large-language-models]
- confidence: high

**definition**: Prompt Clarity Principles are the set of compositional and rhetorical guidelines — including specificity, atomicity, positive framing, disambiguation of pronouns, and avoidance of implicit assumptions — that reduce the gap between the prompt author's intent and the model's interpretation of the task.

**key_claim**: Prompt Clarity Principles address the fundamental asymmetry between prompt authoring and prompt reading: the author knows what they mean; the model must infer it from tokens alone, making the elimination of interpretive ambiguity the single most reliable path to consistent outputs without increasing prompt length.

**warning**: Prompt Clarity Principles do not guarantee unique interpretation; even maximally clear prompts contain semantic degrees of freedom that the model resolves via its training distribution, so clarity reduces variance but does not eliminate it — especially for tasks where the training corpus contains divergent conventions.

## Negative Prompting

- secondary_domains: [llm-inference, output-control]
- aliases: [exclusion prompting, do-not instructions]
- broader: [prompting]
- related: [positive-framing-in-prompts, prompt-clarity-principles, instruction-following]
- prerequisites: [large-language-models]
- confidence: high

**definition**: Negative Prompting is the technique of specifying what the model should not do, avoid, or include in its output — using explicit prohibitions, exclusion lists, or counterfactual framing — in addition to or instead of positively specifying the desired behaviour.

**key_claim**: Negative Prompting is cognitively less reliable than positive framing because language models, like humans, mentally simulate the prohibited item when processing negations, making the model's internal representation closer to the unwanted output than a positive reframe would achieve; this is why "do not use bullet points" frequently produces fewer bullets than zero bullets.

**warning**: Negative Prompting interacts poorly with instruction-following limitations at scale; long lists of prohibitions compete for attention with the primary task instruction, and empirical testing consistently shows that models begin dropping constraints once the negation list exceeds three to five items in a single prompt.

## Positive Framing in Prompts

- secondary_domains: [llm-inference, cognitive-linguistics]
- aliases: [positive instruction framing, affirmative prompting]
- broader: [prompt-clarity-principles, prompting]
- related: [negative-prompting, instruction-following, prompt-clarity-principles]
- prerequisites: [large-language-models]
- confidence: high

**definition**: Positive Framing in Prompts is the practice of specifying desired behaviour through direct, affirmative statements of what the model should do rather than through prohibitions of what to avoid — replacing "do not use jargon" with "write in plain language accessible to a general audience."

**key_claim**: Positive Framing in Prompts reduces cognitive double-processing; an affirmative instruction activates the target representation directly, whereas a negative instruction first activates the prohibited representation and then requires inhibition of it, making positive framing empirically more reliable for format and style constraints.

**warning**: Positive Framing in Prompts is not universally superior; there are genuine cases where the unwanted behaviour is more precisely characterised than the desired one, and forcing a positive reframe can introduce new ambiguity that the original prohibition would have avoided — particularly for safety-critical exclusions.

## Delimiters and Separators

- secondary_domains: [prompt-formatting, llm-inference]
- aliases: [prompt delimiters, section separators, context separators]
- broader: [prompt-formatting]
- related: [prompt-formatting, prompt-clarity-principles, system-prompt-design]
- prerequisites: [large-language-models, tokenisation]
- confidence: high

**definition**: Delimiters and Separators in prompt engineering are syntactic markers — such as triple backticks, XML tags, dashes, or capitalised labels — used to demarcate distinct semantic zones within a prompt (e.g., separating the instruction from the user-supplied data) and to prevent the model from treating injected content as authoritative instruction.

**key_claim**: Delimiters and Separators are the primary structural defence against prompt-injection attacks at the prompt level; by clearly demarcating where user-controlled content begins and ends, they reduce (though do not eliminate) the model's tendency to treat adversarial content embedded in that zone as an instruction to be followed.

**warning**: Delimiters and Separators are not robust security boundaries; any delimiter scheme that the model can parse can also be escaped or replicated by an adversarial user, so delimiters should be treated as a UX tool for structure clarity rather than as a security mechanism in high-stakes deployments.

## Role Prompting

- secondary_domains: [persona-design, llm-inference]
- aliases: [role assignment, role-based prompting]
- broader: [prompting]
- narrower: [persona-assignment]
- related: [persona-assignment, system-prompt-design, instruction-following]
- prerequisites: [large-language-models]
- confidence: high

**definition**: Role Prompting is the technique of assigning the model a named role, profession, or character at the start of a prompt (e.g., "You are an expert data analyst") to shift its response distribution toward the knowledge, vocabulary, tone, and epistemic norms associated with that role in the training data.

**key_claim**: Role Prompting works because language models encode rich associations between role labels and characteristic discourse patterns in their training data; instructing the model to adopt a role activates a distributional prior that shifts outputs without requiring explicit instruction of every detail implied by that role.

**warning**: Role Prompting can produce overconfident outputs when the assigned role has high epistemic authority (e.g., "You are a medical doctor"); the model may generate role-consistent content even when the correct answer to a question within that role domain is "I am uncertain" or "consult a professional," suppressing appropriate hedging.

## Persona Assignment

- secondary_domains: [llm-deployment, conversational-ai]
- aliases: [persona prompting, character assignment, bot persona]
- broader: [role-prompting, system-prompt-design]
- related: [role-prompting, system-prompt-design, output-format-specification]
- prerequisites: [large-language-models, system-prompt-design]
- confidence: high

**definition**: Persona Assignment is the sustained, multi-attribute specification of a model's identity, communication style, values, and knowledge scope through the system prompt or a persistent identity block, creating a consistent character that persists across the full conversation rather than merely activating a domain prior as in simple role prompting.

**key_claim**: Persona Assignment goes beyond role prompting by locking in a coherent constellation of stylistic, tonal, and behavioural attributes simultaneously; this consistency is the foundation of character-based products (assistants, chatbots, NPCs) and is what makes the model's behaviour predictable at deployment scale rather than task-by-task.

**warning**: Persona Assignment can create brittleness at persona boundaries; when users ask questions that fall outside the persona's designated scope, the model faces a conflict between persona-coherence and task-completion, sometimes producing persona-inconsistent responses, sometimes producing refusals that frustrate users expecting general capability.

## Output Format Specification

- secondary_domains: [structured-output, llm-deployment]
- aliases: [format specification, output structuring, output constraints]
- broader: [prompting]
- related: [prompt-formatting, instruction-following, system-prompt-design]
- prerequisites: [large-language-models]
- confidence: high

**definition**: Output Format Specification is the practice of explicitly defining the structure, schema, style, and boundaries of the model's expected response — including specifications for JSON schema, markdown structure, response length, section headings, and enumeration format — to make the output machine-parseable or directly embeddable in downstream systems.

**key_claim**: Output Format Specification is the highest-leverage intervention for deterministic integration of LLM outputs into production pipelines; a model that reliably emits structured output eliminates an entire class of downstream parsing failures, reducing the application's fragility to the model's stylistic variance.

**warning**: Output Format Specification degrades model helpfulness when the format constraint conflicts with the natural expression of the content; forcing a complex analytical conclusion into a rigid JSON schema can lead to information loss, truncation, or syntactically valid but semantically impoverished responses.

## Chain-of-Thought Prompting

- secondary_domains: [reasoning, llm-inference]
- aliases: [CoT prompting, chain of thought, let's think step by step]
- broader: [reasoning-techniques, prompting]
- narrower: [zero-shot-chain-of-thought, few-shot-chain-of-thought]
- related: [tree-of-thoughts, least-to-most-prompting, step-back-prompting, self-consistency-sampling]
- prerequisites: [large-language-models, few-shot-prompting]
- confidence: high

**definition**: Chain-of-Thought Prompting is a prompting technique that elicits multi-step reasoning from a language model by instructing it to produce intermediate reasoning steps before arriving at a final answer, either through worked examples that demonstrate the reasoning trace (few-shot CoT) or through a simple instruction like "think step by step" (zero-shot CoT).

**key_claim**: Chain-of-Thought Prompting improves performance on multi-step reasoning tasks not merely by slowing the model down but by externalising the reasoning process into the context window, where each intermediate conclusion becomes available as a retrieved premise for subsequent steps — a mechanism unavailable in single-token final-answer prompting.

**warning**: Chain-of-Thought Prompting does not guarantee faithful reasoning; models can produce convincing reasoning chains that arrive at correct answers via logically invalid paths, or produce plausible-sounding wrong chains that the reader accepts because of their fluency — a failure mode sometimes called "rationalisation prompting."

## Step-Back Prompting

- secondary_domains: [reasoning, llm-inference]
- aliases: [step-back abstraction, abstraction-first prompting]
- broader: [prompting, reasoning-techniques]
- related: [chain-of-thought-prompting, analogical-prompting, metacognitive-prompting, least-to-most-prompting]
- prerequisites: [large-language-models, chain-of-thought-prompting]
- confidence: high

**definition**: Step-Back Prompting is a two-stage prompting strategy in which the model is first asked to identify the abstract principle, domain concept, or general category that the specific question instantiates, and then uses that higher-level abstraction as a retrieved context scaffold before generating the answer to the original question.

**key_claim**: Step-Back Prompting exploits the asymmetry between abstract and specific reasoning in large language models: models are often better at generating accurate general principles from their training distribution than at applying those principles to novel specifics directly, so elevating abstraction level first then grounding improves accuracy for knowledge-intensive tasks.

**warning**: Step-Back Prompting adds a reasoning step that can introduce its own errors; if the model retrieves an incorrect or inapplicable abstraction in the first stage, it will ground the second stage on a flawed premise, potentially producing a confident but mistaken answer with an internally coherent but externally false justification chain.
