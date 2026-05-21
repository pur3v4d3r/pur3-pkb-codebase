---
title: V6 Pipeline Starter Prompts
aliases:
  - V6 Pipeline Prompts
  - Permanent Note Pipeline Starters
  - V6 Seed and Enhancement Prompts
  - Pipeline Kickoff Prompts
type: reference-note
status: evergreen
confidence: high

tags:
  - reference-note
  - pkb/permanent-notes
  - pipeline/v6
  - prompt-engineering/starter-prompts
  - workflow/automation
  - obsidian/pkb

domain: knowledge-management
created: 2026-05-12
updated: 2026-05-12

# Pipeline Context
pipeline-version: v6
pipeline-location: "99-scripts/report-extraction-to-permanent-notes-building-v6"
notes-location: "999-report-organizing/_permanent-notes/v6-llm-elaborated"

prompt-types:
  - seeding-permanent-notes
  - enhancing-existing-permanent-notes

related:
  - "[[report-extraction-to-permanent-notes-building-v6]]"
  - "[[v6-llm-elaborated]]"
  - "[[permanent-note-seed-agent-v1.0.0]]"
  - "[[reports-to-permanent-notes-agent-prompt]]"

prerequisites:
  - "[[V6 Pipeline README]]"
  - "[[Permanent Note Methodology]]"

see-also:
  - "[[Zettelkasten Method]]"
  - "[[PKB Architecture]]"
  - "[[Prompt Engineering Patterns]]"

broader:
  - "[[Pipeline Workflows]]"
  - "[[PKB Automation]]"
---




# V6 Pipeline - Seeding Permanent Notes

I have a pipeline for creating permanent notes for my Obsidian based PKB. The pipeline is a V6.
What I need you todo is to review the pipeline and accompyning files, so you understand how everything works.
- You will find all the information you need in side the pipleine folders.

## Key Locations for Pipeline Reference

Here are the main key locations for you to learn how the pipline works, the ins and outs, and how it runs.
`D:\10_pur3v4d3r's-vault\99-scripts\report-extraction-to-permanent-notes-building-v6` -> V6 Pipeline
`D:\10_pur3v4d3r's-vault\99-scripts\report-extraction-to-permanent-notes-building-v6\README.md` -> Pipeline V6 README
`D:\10_pur3v4d3r's-vault\999-report-organizing\_permanent-notes\v6-llm-elaborated` -> Home of current permanent notes.

## TASK
1. Review the V6 pipeline and accompanying files to understand how everything works.
2. Create the seeds for the permanent note pipeline to use, to create the corresponding permanent notes.
3. After you have created the seeds for the permanent notes, run the pipeline on the seeds you just created, creating the permanent notes.
4. Please feel free to ask any question you have.

**NOTE**: NO DRY RUN, and you dertermin the batch sizing for the seeds.
### Notes to create Seeds for:

`````markdown
# Prompting Fundamentals
zero-shot-prompting
few-shot-prompting
one-shot-prompting
system-prompt-design
instruction-following
prompt-formatting
prompt-clarity-principles
negative-prompting
positive-framing-in-prompts
delimiters-and-separators
role-prompting
persona-assignment
output-format-specification
chain-of-thought-prompting
step-back-prompting

# Reasoning Techniques
tree-of-thoughts
graph-of-thoughts
self-consistency-sampling
chain-of-verification
reflexion
program-of-thoughts
skeleton-of-thought
least-to-most-prompting
decomposed-prompting
analogical-prompting
metacognitive-prompting
self-ask-prompting
directional-stimulus-prompting
contrastive-chain-of-thought

# Extended Thinking and Metacognition
extended-thinking-architecture
thinking-tag-semantics
interleaved-thinking-mode
metacognitive-scaffolding
inner-monologue-technique
latent-reasoning-space
thinking-budget-allocation
cognitive-asymmetry-in-llms

# In-Context Learning
in-context-learning
few-shot-example-selection
example-ordering-effects
demonstration-diversity
label-sensitivity-in-icl
retrieval-augmented-few-shot
analogical-in-context-learning

# Prompt Optimization
automatic-prompt-engineering
gradient-free-prompt-optimization
dspy-framework
prompt-tuning
soft-prompting
prefix-tuning
prompt-compression
prompt-paraphrasing
prompt-ensembling
boosted-prompt-ensembles
evolutionary-prompt-optimization
reflexion-based-prompt-refinement

# Retrieval-Augmented Generation
retrieval-augmented-generation
dense-passage-retrieval
hyde-hypothetical-document-embeddings
self-rag
corrective-rag
iterative-retrieval
knowledge-intensive-nlp
demonstrate-search-predict

# Agentic Frameworks
react-reasoning-acting
plan-and-execute-agents
reflexion-agent-architecture
toolformer
function-calling
tool-use-in-llms
multi-agent-debate
hierarchical-agent-orchestration
agent-scratchpad
chain-of-action
task-decomposition-agents
critic-agents
self-refine

# Evaluation and Quality
llm-as-judge
chain-of-thought-faithfulness
hallucination-detection
factual-consistency-evaluation
prompt-sensitivity-analysis
benchmark-overfitting
gsm8k-benchmark
hotpotqa-benchmark
calibration-in-llms
uncertainty-quantification-llms

# Architecture and Attention
transformer-attention-mechanism
context-window-management
attention-sink-phenomenon
lost-in-the-middle-effect
position-encoding-effects
token-budget-management
kv-cache-mechanics
speculative-decoding

# Failure Modes and Mitigations
prompt-injection
jailbreaking
sycophancy-in-llms
hallucination-taxonomy
distractor-sensitivity
instruction-hierarchy-conflict
overthinking-in-llms
reward-hacking

# Advanced Patterns
meta-prompting
system-2-prompting
chain-of-density-technique
socratic-prompting
maieutic-prompting
self-play-prompting
constitutional-ai-method
red-teaming-llms

`````






















# V6 Pipeline - Enhancing Existing Permanent Notes

I have a pipeline for creating permanent notes for my Obsidian based PKB. The pipeline is a V6.
What I need you todo is to review the pipeline and accompyning files, so you understand how everything works.
- You will find all the information you need in side the pipleine folders.

## Key Locations for Pipeline Reference

Here are the main key locations for you to learn how the pipline works, the ins and outs, and how it runs.
`D:\10_pur3v4d3r's-vault\99-scripts\report-extraction-to-permanent-notes-building-v6` -> V6 Pipeline
`D:\10_pur3v4d3r's-vault\99-scripts\report-extraction-to-permanent-notes-building-v6\README.md` -> Pipeline V6 README
`D:\10_pur3v4d3r's-vault\999-report-organizing\_permanent-notes\v6-llm-elaborated` -> Home of current permanent notes.

## TASK
1. Review the V6 pipeline and accompanying files to understand how everything works.
2. Run the Enhancement Pipeline on permanent notes that have not been run through yet.
3. Please feel free to ask any question you have.

Please feel free to ask any question you have.

### Recent Additions to the Permanent Note Dipository that need to be enhanced:

`````markdown

# Alignment and Safety
constitutional-ai-principles
reinforcement-learning-from-human-feedback
direct-preference-optimization
reward-model-design
scalable-oversight
debate-as-alignment-mechanism
iterated-amplification
superalignment
sandbagging-in-llms
deceptive-alignment
value-alignment-problem
corrigibility
preference-elicitation
activation-steering
representation-engineering

# Fine-Tuning and Adaptation
instruction-fine-tuning
parameter-efficient-fine-tuning
lora-low-rank-adaptation
qlora
adapter-layers
prompt-fine-tuning-vs-rag
domain-adaptation-llms
catastrophic-forgetting-in-llms
continual-learning-llms
task-specific-fine-tuning
self-play-fine-tuning

# Tokenization and Vocabulary
byte-pair-encoding
tokenization-artifacts
token-boundary-effects
vocabulary-size-tradeoffs
subword-tokenization
tokenizer-sensitivity
cross-lingual-tokenization
whitespace-token-effects

# Embeddings and Semantic Space
text-embedding-models
semantic-similarity-in-prompts
cosine-similarity-retrieval
embedding-space-geometry
late-chunking
sentence-transformers
bi-encoder-vs-cross-encoder
matryoshka-representation-learning
contrastive-learning-embeddings

# Structured Output and Grounding
json-mode-prompting
grammar-constrained-decoding
function-schema-design
structured-prediction-prompting
output-schema-enforcement
constrained-beam-search
guided-generation
tool-schema-optimization

# Multimodal Prompting
vision-language-prompting
image-captioning-prompts
visual-chain-of-thought
multimodal-few-shot
document-understanding-prompts
chart-and-table-reasoning
interleaved-image-text-prompting
grounded-visual-reasoning

# Memory Systems and Long Context
episodic-memory-in-agents
external-memory-augmentation
memory-augmented-neural-networks
compressive-memory-mechanisms
long-context-prompting-strategies
needle-in-a-haystack-evaluation
context-distillation
summarization-as-compression
working-memory-proxies-in-llms

# Decoding and Sampling
temperature-sampling
top-p-nucleus-sampling
top-k-sampling
beam-search-decoding
min-p-sampling
repetition-penalty
frequency-penalty-effects
contrastive-decoding
speculative-sampling
best-of-n-sampling

# Knowledge and Grounding
knowledge-graph-augmented-llms
entity-linking-in-prompts
fact-verification-prompting
knowledge-conflict-resolution
parametric-vs-contextual-knowledge
closed-book-vs-open-book-qa
grounded-generation
world-model-in-llms

# Code Generation and Reasoning
code-prompting-strategies
execution-feedback-prompting
self-debugging-llm
code-chain-of-thought
test-driven-prompting
docstring-guided-generation
repair-prompting
pseudocode-intermediate-step

# Evaluation Frameworks
lm-evaluation-harness
big-bench-benchmark
helm-holistic-evaluation
mt-bench
arena-elo-rating
self-evaluation-prompting
llm-judge-calibration
process-reward-models
outcome-reward-models
human-preference-datasets

# Cognitive Science Foundations
dual-process-theory-applied-to-llms
cognitive-load-theory-applied-to-llms
working-memory-constraints-in-prompts
schema-activation-in-prompts
semantic-priming-effects
prototype-theory-and-llms
mental-simulation-in-llms
epistemological-uncertainty-in-llms

# Production and Deployment
prompt-versioning
prompt-regression-testing
latency-quality-tradeoff
prompt-caching-strategies
cost-per-token-optimization
prompt-monitoring-and-alerting
a-b-testing-prompts
prompt-registry-management
multi-model-routing
fallback-prompt-strategies

`````
















# Starter Prompt for Generating Permanent Note Candidates from Gaps in the Note Network

```markdown
# Concept Inventory and Gap Analysis

This is a list of my permanent notes in obsidian, use this to come up with a set of 100 new permanent notes that are missing from this set of permanent notes, and can be created.
List them like this for easy copy and paste ability

```markdown
# Cognitive Science
attention-restoration-theory
cognitive-load-and-affect
cognitive-load
worked-example-variability
semantic-priming
```












# Starter Prompt for Running Pipeline for Synthetic Seed

```markdown
# Pipeline with Seeds

I have a pipeline for creating/modifying permanent notes for my PKB in Obsidian.
I need you to review the readme's so you get the flow of it and then run the pipeline STARTING FROM the `D:\10_pur3v4d3r's-vault\99-scripts\synthetic-permanent-note-seeds`

# GoaL
50-100 New Permanent Notes in the vault, seeded from scratch with no human-written input, based on gaps in the existing note network.

## How the Pipeline Should Run From This Starting Point
- Should be something like this:

`Checks the original permanent notes folder for concepts to create` -> `Generate the list of concepts to be made into permanent notes` -> `Turn that into JSON files for the V6 Pipeline to read` -> `Runs the V6 Pipeline to generate permanent notes from the JSON files` -> `Output the generated permanent notes into the appropriate directory in Obsidian.`


# Key Locations for Pipeline Reference
Here are the main key locations for you to learn how the pipline works, the ins and outs, and how it runs.

`D:\10_pur3v4d3r's-vault\99-scripts\report-extraction-to-permanent-notes-building-v3` -> V3 pipeline
`D:\10_pur3v4d3r's-vault\99-scripts\report-extraction-to-permanent-notes-building-v4` -> V4 pipeline
`D:\10_pur3v4d3r's-vault\99-scripts\report-extraction-to-permanent-notes-building-v5` -> V5 pipeline
`D:\10_pur3v4d3r's-vault\99-scripts\report-extraction-to-permanent-notes-building-v6` -> V6 Pipeline

`D:\10_pur3v4d3r's-vault\999-report-organizing\_permanent-notes\v6-llm-elaborated` -> Home of current permanent notes.
```
NOTE: Scan the permanent notes folder for wiki-links without notes, use those as seeds for the pipeline to generate new permanent notes from, filling in gaps.




# Starter Prompt For Custom List of Permanent Note Seeds

```markdown
# Pipeline with Seeds

I have a pipeline for creating/modifying permanent notes for my PKB in Obsidian.
I need you to review the readme's so you get the flow of it and then run the pipeline STARTING FROM the `D:\10_pur3v4d3r's-vault\99-scripts\synthetic-permanent-note-seeds`
You are going to turn the following list of potential permanent note topics into seeds for the V6 Pipeline to generate permanent notes from. These are topics that I have identified as missing from my current note network, and I want to use the pipeline to generate high-quality permanent notes on these topics.
- Which can be done in batches of 10-20 to make it more manageable, but the end goal is to have all of these topics turned into permanent notes in my vault.
- You will need to turn each of these topics into a JSON file that the V6 Pipeline can read, and then run the pipeline to generate the permanent notes from these JSON files.

# GoaL
Turn this list of potential permanent notes into seed for the V6 Pipeline.

## How the Pipeline Should Run From This Starting Point
- Should be something like this:

`Checks the original permanent notes folder for concepts to create` -> `Generate the list of concepts to be made into permanent notes` -> `Turn that into JSON files for the V6 Pipeline to read` -> `Runs the V6 Pipeline to generate permanent notes from the JSON files` -> `Output the generated permanent notes into the appropriate directory in Obsidian.`


# Key Locations for Pipeline Reference
Here are the main key locations for you to learn how the pipline works, the ins and outs, and how it runs.

`D:\10_pur3v4d3r's-vault\99-scripts\report-extraction-to-permanent-notes-building-v3` -> V3 pipeline
`D:\10_pur3v4d3r's-vault\99-scripts\report-extraction-to-permanent-notes-building-v4` -> V4 pipeline
`D:\10_pur3v4d3r's-vault\99-scripts\report-extraction-to-permanent-notes-building-v5` -> V5 pipeline
`D:\10_pur3v4d3r's-vault\99-scripts\report-extraction-to-permanent-notes-building-v6` -> V6 Pipeline

`D:\10_pur3v4d3r's-vault\999-report-organizing\_permanent-notes\v6-llm-elaborated` -> Home of current permanent notes.

# Custom List of Permanent Note Seeds


```







# Enhance permanent notes pipeline

I have a pipeline for enhancing permanent notes that it has created. It uses local LLM. I want you to run this pipeline on 100 notes.
Review the pipeline for context and details.

# Key Locations for Pipeline Reference
Here are the main key locations for you to learn how the pipeline works, the ins and outs, and how it runs.

`D:\10_pur3v4d3r's-vault\99-scripts\report-extraction-to-permanent-notes-building-v3` -> V3 pipeline
`D:\10_pur3v4d3r's-vault\99-scripts\report-extraction-to-permanent-notes-building-v4` -> V4 pipeline
`D:\10_pur3v4d3r's-vault\99-scripts\report-extraction-to-permanent-notes-building-v5` -> V5 pipeline
`D:\10_pur3v4d3r's-vault\99-scripts\report-extraction-to-permanent-notes-building-v6` -> V6 Pipeline


`D:\10_pur3v4d3r's-vault\999-report-organizing\_permanent-notes\v6-llm-elaborated` -> Home of current permanent notes.














# Starter Prompt for Running Pipeline for Synthetic Seed

```markdown
# Pipeline with Seeds

I have a pipeline for creating/modifying permanent notes for my PKB in Obsidian.
I need you to review the readme's so you get the flow of it and then run the pipeline STARTING FROM the `D:\10_pur3v4d3r's-vault\99-scripts\synthetic-permanent-note-seeds`


## How the Pipeline Should Run From This Starting Point
- Should be something like this:

`Checks the original permanent notes folder for concepts to create` -> `Generate the list of concepts to be made into permanent notes` -> `Turn that into JSON files for the V6 Pipeline to read` -> `Runs the V6 Pipeline to generate permanent notes from the JSON files` -> `Output the generated permanent notes into the appropriate directory in Obsidian.`


# Key Locations for Pipeline Reference
Here are the main key locations for you to learn how the pipeline works, the ins and outs, and how it runs.

`D:\10_pur3v4d3r's-vault\99-scripts\report-extraction-to-permanent-notes-building-v3` -> V3 pipeline
`D:\10_pur3v4d3r's-vault\99-scripts\report-extraction-to-permanent-notes-building-v4` -> V4 pipeline
`D:\10_pur3v4d3r's-vault\99-scripts\report-extraction-to-permanent-notes-building-v5` -> V5 pipeline
`D:\10_pur3v4d3r's-vault\99-scripts\report-extraction-to-permanent-notes-building-v6` -> V6 Pipeline

`D:\10_pur3v4d3r's-vault\999-report-organizing\_permanent-notes\v6-llm-elaborated` -> Home of current permanent notes.

````markdown
pre-frontal-cortex




































# Concept Inventory and Gap Analysis

This is a list of my permanent notes in obsidian, use this to come up with a set of 100 new permanent notes that are missing from this set of permanent notes, and can be created.
List them like this for easy copy and paste ability

```markdown
# Cognitive Science
attention-restoration-theory
cognitive-load-and-affect
cognitive-load
worked-example-variability
semantic-priming
```



