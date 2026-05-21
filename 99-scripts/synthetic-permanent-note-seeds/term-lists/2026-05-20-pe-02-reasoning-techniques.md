---
batch_name: pe-02-reasoning-techniques
batch_date: 2026-05-20
default_domain: prompt-engineering
default_confidence: high
notes: |
  Fourteen reasoning-technique concepts covering structured inference
  strategies for large language models. Spans tree-based search, verification
  loops, program synthesis prompting, decomposition strategies, and analogical
  methods. Intended as the second-tier layer above foundational chain-of-thought.
---

# Batch: PE-02 Reasoning Techniques

## Tree of Thoughts

- secondary_domains: [reasoning, search-algorithms]
- aliases: [ToT, tree-of-thought reasoning]
- broader: [reasoning-techniques, prompting]
- related: [chain-of-thought-prompting, graph-of-thoughts, self-consistency-sampling, decomposed-prompting]
- prerequisites: [chain-of-thought-prompting, large-language-models]
- confidence: high

**definition**: Tree of Thoughts is a prompting framework that structures LLM reasoning as an explicit search over a tree of intermediate "thought" states, where each node is a partial solution, branches represent alternative reasoning moves, and the search is guided by a value function (implemented via LLM self-evaluation) that prunes low-promise paths and backtracks to explore more productive branches.

**key_claim**: Tree of Thoughts overcomes the key limitation of linear chain-of-thought prompting — the inability to recover from early reasoning errors — by making backtracking and branch exploration first-class operations, which is why it outperforms CoT on tasks where the optimal path requires trying and discarding multiple intermediate hypotheses.

**warning**: Tree of Thoughts is computationally expensive in proportion to the tree's branching factor and depth; naive implementations require many LLM calls per problem and can produce costs that make the method impractical for latency-sensitive or budget-constrained deployments without careful pruning strategies.

## Graph of Thoughts

- secondary_domains: [reasoning, graph-theory]
- aliases: [GoT, graph-of-thought reasoning]
- broader: [reasoning-techniques, prompting]
- related: [tree-of-thoughts, chain-of-thought-prompting, decomposed-prompting, hierarchical-agent-orchestration]
- prerequisites: [tree-of-thoughts, large-language-models]
- confidence: high

**definition**: Graph of Thoughts is a reasoning framework that generalises Tree of Thoughts by representing the reasoning process as an arbitrary directed graph rather than a tree, enabling thought nodes to be merged (aggregation of partial solutions) and revisited (cycles for refinement), which allows the model to combine insights from independent reasoning paths into a single integrated conclusion.

**key_claim**: Graph of Thoughts enables reasoning operations — such as merging two partial proofs, refining an answer with a counterexample, and then aggregating the correction — that are structurally impossible in tree-based frameworks, making it the appropriate abstraction for tasks where the final solution is a synthesis of heterogeneous intermediate results rather than the best single reasoning path.

**warning**: Graph of Thoughts substantially increases the complexity of the orchestration layer required to implement it; managing node states, determining merge conditions, and detecting cycles adds engineering overhead that often outweighs the performance gains on tasks that are adequately solved by tree-based or linear chain-of-thought approaches.

## Self-Consistency Sampling

- secondary_domains: [reasoning, ensemble-methods]
- aliases: [self-consistency, majority-vote prompting, consistency sampling]
- broader: [reasoning-techniques, prompt-ensembling]
- related: [chain-of-thought-prompting, tree-of-thoughts, chain-of-verification]
- prerequisites: [chain-of-thought-prompting, large-language-models]
- confidence: high

**definition**: Self-Consistency Sampling is a decoding strategy for chain-of-thought reasoning that generates multiple independent reasoning traces for the same question using high-temperature sampling, then aggregates the final answers by majority vote, discarding the individual reasoning paths and selecting the answer that appears most frequently across the sampled traces.

**key_claim**: Self-Consistency Sampling improves reasoning accuracy by treating each sampled chain-of-thought as an independent estimator and exploiting the fact that correct reasoning paths are more likely to converge on the same answer than incorrect ones, even when each individual path may contain errors — making ensemble diversity the error-correction mechanism.

**warning**: Self-Consistency Sampling assumes that correctness correlates with majority vote, which breaks down on tasks where the model's error distribution is systematically biased; if the model makes the same type of error across most sampled traces, the majority answer will be consistently wrong, and the sampling overhead provides false confidence without improving accuracy.

## Chain of Verification

- secondary_domains: [reasoning, factual-accuracy]
- aliases: [CoVe, chain-of-verification prompting]
- broader: [reasoning-techniques, prompting]
- related: [self-consistency-sampling, hallucination-detection, chain-of-thought-prompting, self-refine]
- prerequisites: [chain-of-thought-prompting, large-language-models]
- confidence: high

**definition**: Chain of Verification is a prompting strategy in which the model first generates an initial response, then explicitly plans a set of factual verification questions about that response, answers each question independently (to avoid anchoring on the original response), and finally revises the initial response based on the verification answers to produce a more factually grounded output.

**key_claim**: Chain of Verification reduces hallucinations by decoupling generation from verification; when verification questions are answered independently rather than in the context of the original claim, the model's confirmation bias is broken, making it more likely to detect and correct factual errors that it would have reinforced had it been asked to review its own output directly.

**warning**: Chain of Verification's independence assumption is imperfect; even when answering verification questions without the original text, the model retains its parametric memory of the initial generation through the conversation context, meaning the claimed independence is partial rather than absolute and the technique underperforms expectations when context windows are shared.

## Reflexion

- secondary_domains: [reasoning, agent-frameworks]
- aliases: [reflexion prompting, verbal reinforcement learning]
- broader: [reasoning-techniques, agentic-frameworks]
- related: [self-refine, chain-of-verification, reflexion-agent-architecture, reflexion-based-prompt-refinement]
- prerequisites: [chain-of-thought-prompting, large-language-models]
- confidence: high

**definition**: Reflexion is a framework in which an LLM agent improves its performance on a task over multiple trials by generating a verbal self-reflection on the previous trial's failure modes and storing that reflection as a persistent memory that conditions the next attempt, effectively implementing a verbal analogue of reinforcement learning without gradient updates.

**key_claim**: Reflexion demonstrates that language models can perform policy improvement purely through natural language self-critique, bypassing the need for numerical reward signals or parameter updates; the stored verbal reflection acts as a working memory that prevents the agent from repeating the same failure mode in subsequent attempts.

**warning**: Reflexion is bounded by the model's capacity for accurate self-diagnosis; if the model cannot correctly identify why it failed (a common limitation when failures are caused by knowledge gaps rather than reasoning errors), the generated reflection is inaccurate and may encode the wrong lesson, leading to persistent misalignment between the reflection and the actual failure mode.

## Program of Thoughts

- secondary_domains: [code-generation, reasoning]
- aliases: [PoT, program-of-thought prompting]
- broader: [reasoning-techniques, prompting]
- related: [chain-of-thought-prompting, tool-use-in-llms, function-calling]
- prerequisites: [chain-of-thought-prompting, large-language-models, code-generation]
- confidence: high

**definition**: Program of Thoughts is a reasoning technique in which the model expresses its reasoning as a formal program (typically Python) rather than natural-language prose, then executes the program via an external interpreter to obtain the final answer, offloading precise numerical computation and symbolic manipulation to the interpreter rather than performing them in natural language.

**key_claim**: Program of Thoughts separates reasoning (what to compute) from computation (how to compute it precisely), and empirical evidence shows that this separation significantly reduces arithmetic errors on multi-step quantitative tasks because the model no longer attempts to perform multi-digit arithmetic in the token generation process, where it is unreliable, but delegates it to a reliable symbolic executor.

**warning**: Program of Thoughts is limited to problems that can be fully formalised as executable code; tasks requiring commonsense judgment, subjective evaluation, or open-ended creativity resist complete formalisation, and forcing them into the program-of-thoughts framework produces code that compiles but does not capture the actual reasoning the task requires.

## Skeleton of Thought

- secondary_domains: [reasoning, parallel-inference]
- aliases: [SoT, skeleton-of-thought prompting]
- broader: [reasoning-techniques, prompting]
- related: [chain-of-thought-prompting, decomposed-prompting, least-to-most-prompting]
- prerequisites: [chain-of-thought-prompting, large-language-models]
- confidence: high

**definition**: Skeleton of Thought is a two-stage prompting strategy designed to reduce latency by first generating a structured skeleton (an outline of the answer's key points) and then elaborating each point independently and in parallel, rather than generating the full response sequentially from token to token.

**key_claim**: Skeleton of Thought reduces generation latency for long-form responses by parallelising the elaboration stage across skeleton points, allowing the wall-clock time to scale sub-linearly with response length; the trade-off is that inter-point coherence must be managed explicitly, since parallel elaboration breaks the sequential conditioning that ensures consistency in standard autoregressive generation.

**warning**: Skeleton of Thought degrades for tasks where the answer's structure cannot be determined before knowing the answer's content; when correct elaboration of one point depends on the content of a previously elaborated point, the parallel independence assumption is violated and the resulting response exhibits logical discontinuities between sections.

## Least-to-Most Prompting

- secondary_domains: [reasoning, decomposition]
- aliases: [L2M prompting, least-to-most, compositional generalisation prompting]
- broader: [reasoning-techniques, prompting]
- related: [decomposed-prompting, chain-of-thought-prompting, analogical-prompting, skeleton-of-thought]
- prerequisites: [chain-of-thought-prompting, large-language-models]
- confidence: high

**definition**: Least-to-Most Prompting is a two-stage decomposition strategy in which the model first breaks a complex problem into an ordered sequence of progressively more complex subproblems, then solves them from simplest to most complex, using each solved subproblem as context for the next — ensuring that each step has full access to the conclusions that it depends on.

**key_claim**: Least-to-Most Prompting achieves compositional generalisation by making the dependency structure of the problem explicit in the solving order; by ensuring that each step can condition on all previously solved steps, it enables models to solve problems that require more reasoning steps than appeared in their training examples, overcoming a key limitation of standard few-shot chain-of-thought.

**warning**: Least-to-Most Prompting requires correct problem decomposition in the first stage; if the initial breakdown is wrong (either by ordering steps incorrectly or by omitting a necessary intermediate), the second stage will solve the wrong sequence of subproblems and arrive at a confident but flawed answer, with the structured presentation giving the appearance of rigour to an internally inconsistent reasoning chain.

## Decomposed Prompting

- secondary_domains: [reasoning, task-decomposition]
- aliases: [DECOMP, decomposed task prompting]
- broader: [reasoning-techniques, prompting]
- related: [least-to-most-prompting, skeleton-of-thought, task-decomposition-agents, chain-of-thought-prompting]
- prerequisites: [chain-of-thought-prompting, large-language-models]
- confidence: high

**definition**: Decomposed Prompting is a framework that routes complex tasks to specialised sub-prompts, each handling one atomic operation, by having a controller prompt dynamically dispatch to handlers for specific subtasks (such as string manipulation, retrieval, or arithmetic), then recombine their outputs into a final answer.

**key_claim**: Decomposed Prompting improves robustness on compositional tasks by replacing a single monolithic chain-of-thought with a modular routing system where each handler prompt is purpose-built for its operation, enabling independent optimisation and testing of each component — a software-engineering decomposition principle applied to prompt chains.

**warning**: Decomposed Prompting requires the controller prompt to correctly identify which subtask applies at each step; controller errors (misrouting, missing handlers, or incorrect recombination) compound across the pipeline, and debugging multi-step decompositions is substantially more difficult than debugging a single-shot chain-of-thought failure.

## Analogical Prompting

- secondary_domains: [reasoning, analogical-reasoning]
- aliases: [self-generated analogy prompting, analogical few-shot]
- broader: [reasoning-techniques, prompting]
- related: [step-back-prompting, analogical-in-context-learning, chain-of-thought-prompting, metacognitive-prompting]
- prerequisites: [chain-of-thought-prompting, large-language-models]
- confidence: high

**definition**: Analogical Prompting is a technique in which the model is instructed to self-generate relevant analogous examples or solved problems from its own parametric knowledge before tackling the target problem, using these self-retrieved analogies as reasoning scaffolds rather than relying on hand-crafted few-shot examples from the prompt author.

**key_claim**: Analogical Prompting eliminates the bottleneck of human few-shot example construction by having the model retrieve its own analogies, and empirical evidence shows it matches or exceeds hand-crafted few-shot chains on reasoning benchmarks, suggesting that the model's internal knowledge of relevant analogues is a more reliable few-shot pool than any fixed human-authored example set.

**warning**: Analogical Prompting is bounded by the quality of analogies the model can self-generate; if the model cannot identify genuinely structurally similar problems (a failure mode more likely in novel or domain-specific tasks), it generates superficially similar but structurally irrelevant analogies that mislead rather than scaffold the reasoning.

## Metacognitive Prompting

- secondary_domains: [reasoning, metacognition]
- aliases: [metacognitive self-reflection prompting]
- broader: [reasoning-techniques, prompting]
- related: [chain-of-thought-prompting, step-back-prompting, analogical-prompting, metacognitive-scaffolding]
- prerequisites: [chain-of-thought-prompting, large-language-models]
- confidence: high

**definition**: Metacognitive Prompting is a technique that elicits explicit self-monitoring behaviour from the model — asking it to assess its own confidence, identify knowledge gaps, flag uncertain inferences, and describe the limitations of its reasoning — to produce outputs that surface epistemic status alongside content rather than presenting uncertain conclusions with the same surface fluency as certain ones.

**key_claim**: Metacognitive Prompting addresses the fundamental calibration problem of fluent text generation: confident-sounding outputs and well-grounded outputs are stylistically indistinguishable without explicit epistemic marking, and by eliciting the model's own uncertainty assessment, metacognitive prompting creates the epistemic metadata that downstream human or automated review processes need to make appropriate trust decisions.

**warning**: Metacognitive Prompting is susceptible to sycophantic calibration; models trained with RLHF may learn to express high confidence because it satisfies human preferences rather than because it accurately reflects the model's actual epistemic state, making the elicited confidence scores unreliable proxies for ground-truth uncertainty especially in domains where the model lacks genuine knowledge.

## Self-Ask Prompting

- secondary_domains: [reasoning, question-decomposition]
- aliases: [self-ask, follow-up question prompting]
- broader: [reasoning-techniques, prompting]
- related: [least-to-most-prompting, decomposed-prompting, chain-of-thought-prompting, react-reasoning-acting]
- prerequisites: [chain-of-thought-prompting, large-language-models]
- confidence: high

**definition**: Self-Ask Prompting is a technique in which the model explicitly generates the intermediate follow-up questions it needs to answer in order to resolve the main question, then answers each follow-up sequentially before synthesising those answers into a final response — externalising the question-decomposition process that chain-of-thought performs implicitly.

**key_claim**: Self-Ask Prompting makes the question-decomposition structure explicit and inspectable rather than leaving it implicit in the reasoning trace, which enables targeted retrieval (each follow-up can be issued as a search query) and targeted correction (each follow-up can be verified independently), making it the natural bridge between pure language-model reasoning and tool-augmented retrieval-based reasoning.

**warning**: Self-Ask Prompting is sensitive to the quality of the follow-up questions the model generates; if the decomposition produces redundant, circular, or off-target follow-ups, the model wastes context budget answering irrelevant sub-questions, and the synthesis step must then reconcile contradictory or tangential answers, often producing worse results than a direct chain-of-thought approach.

## Directional Stimulus Prompting

- secondary_domains: [reasoning, guided-generation]
- aliases: [DSP, stimulus-directed prompting]
- broader: [reasoning-techniques, prompting]
- related: [chain-of-thought-prompting, step-back-prompting, instruction-following]
- prerequisites: [chain-of-thought-prompting, large-language-models]
- confidence: high

**definition**: Directional Stimulus Prompting is a technique that provides the model with a targeted hint or keyword stimulus alongside the input to steer the model's reasoning toward the desired type of analysis, framing, or conclusion domain, without explicitly prescribing the answer — operating as a directional nudge rather than a full instruction.

**key_claim**: Directional Stimulus Prompting exploits the model's associative priming; a well-chosen stimulus keyword activates a cluster of related representations in the model's attention mechanisms that make the intended analytical frame more salient, improving performance on tasks where the challenge is not capability but focus — picking the right analytical lens from many available ones.

**warning**: Directional Stimulus Prompting requires careful calibration of stimulus strength; an over-specific stimulus collapses into explicit instruction and removes the model's interpretive flexibility, while an under-specific stimulus fails to activate the intended frame and leaves the model anchored to whatever default frame the input alone suggests.

## Contrastive Chain of Thought

- secondary_domains: [reasoning, contrastive-learning]
- aliases: [contrastive CoT, positive-negative chain-of-thought]
- broader: [reasoning-techniques, chain-of-thought-prompting]
- related: [chain-of-thought-prompting, self-consistency-sampling, chain-of-verification, few-shot-prompting]
- prerequisites: [chain-of-thought-prompting, few-shot-prompting, large-language-models]
- confidence: high

**definition**: Contrastive Chain of Thought is a few-shot prompting strategy that pairs each demonstration with both a correct reasoning chain and an explicitly labelled incorrect reasoning chain (annotated with the error type), so the model learns not only the reasoning pattern that leads to the right answer but also the error patterns that lead to wrong ones.

**key_claim**: Contrastive Chain of Thought improves reasoning accuracy beyond standard few-shot CoT by using negative examples to define the decision boundary of correct reasoning; the contrast between the correct chain and the annotated error chain makes the distinguishing features of valid inference more salient, reducing the model's tendency to replicate the specific error types included in the demonstration set.

**warning**: Contrastive Chain of Thought requires careful error selection and annotation; including poorly chosen or mislabelled negative examples can mislead the model by presenting ambiguous reasoning as definitively incorrect, and the annotation overhead (identifying and labelling representative error types for each demo) significantly increases the cost of prompt construction compared to standard few-shot CoT.
