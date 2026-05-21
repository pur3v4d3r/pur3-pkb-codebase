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
```markdown
# Batch 2
## Batch02
## Knowledge Representation and Grounding
semantic-grounding-in-llms
world-model-in-language-models
commonsense-reasoning-in-llms
ontology-grounded-prompting
knowledge-graph-augmented-generation
entity-linking-in-prompts
coreference-resolution-prompting
temporal-reasoning-in-llms
spatial-reasoning-in-llms
causal-reasoning-in-llms
counterfactual-reasoning-prompting
abductive-reasoning-in-llms
deductive-reasoning-chains
inductive-reasoning-in-llms
analogical-transfer-in-llms

## Prompt Sensitivity and Robustness
label-sensitivity-in-prompting
format-sensitivity-in-prompting
order-sensitivity-in-few-shot
surface-form-competition
prompt-brittleness
adversarial-prompt-robustness
distribution-shift-in-prompting
semantic-equivalence-in-prompts
paraphrase-invariance-testing
cross-lingual-prompt-transfer
prompt-calibration-techniques
verbalized-uncertainty
hedge-phrases-in-prompts
overconfidence-in-llm-outputs
underspecification-in-prompts

## Attention Mechanisms and Internals
multi-head-attention-mechanics
cross-attention-in-transformers
self-attention-patterns
attention-head-specialization
induction-heads
copy-suppression-heads
attention-sinks
head-pruning-effects
positional-encoding-variants
rotary-position-embedding
alibi-positional-encoding
flash-attention-algorithm
grouped-query-attention
sliding-window-attention
sparse-attention-patterns

## Emergent Behavior and Capability
emergent-prompting-capability
few-shot-emergent-generalization
chain-of-thought-emergence
semantic-parsing-emergence
multilingual-emergent-transfer
arithmetic-emergence-threshold
in-context-learning-as-meta-learning
task-generalization-in-llms
zero-shot-generalization-mechanisms
capability-elicitation-prompting
latent-capability-unlocking
model-capability-vs-alignment-gap
scaling-and-capability-emergence
instruction-following-emergence
calibration-emergence-in-scale

## Multi-Turn and Dialogue
multi-turn-conversation-management
dialogue-state-tracking-prompts
conversational-context-compression
turn-taking-in-llm-dialogue
persona-consistency-across-turns
memory-injection-in-dialogue
dialogue-grounding-prompts
conversational-repair-prompting
clarification-request-generation
follow-up-question-generation
dialogue-act-classification-prompting
conversation-summarization-prompts
slot-filling-via-dialogue
task-oriented-dialogue-prompting
open-domain-dialogue-prompting

## Evaluation and Benchmarking
benchmark-contamination
train-test-leakage-in-llms
dynamic-benchmarking
adversarial-benchmark-construction
human-vs-llm-eval-agreement
inter-annotator-agreement-in-evals
reference-free-evaluation
rubric-based-llm-evaluation
likert-scale-prompt-evaluation
pairwise-preference-evaluation
win-rate-as-evaluation-metric
evaluation-prompt-design
llm-evaluator-bias
g-eval-scoring-methodology
prometheus-evaluation-model

## Retrieval and Knowledge Integration
dense-retrieval-for-rag
sparse-retrieval-bm25
hybrid-retrieval-patterns
query-rewriting-for-retrieval
iterative-retrieval-augmentation
self-rag-selective-retrieval
corrective-rag-pipeline
adaptive-rag-routing
late-interaction-retrieval
cross-encoder-reranking
reciprocal-rank-fusion
chunking-strategies-for-rag
embedding-model-selection
retrieval-faithfulness
knowledge-conflict-in-rag
```








## Batch03

```markdown
# Batch 3

## Knowledge Representation and Grounding
semantic-grounding-in-llms
world-model-in-language-models
commonsense-reasoning-in-llms
ontology-grounded-prompting
knowledge-graph-augmented-generation
entity-linking-in-prompts
coreference-resolution-prompting
temporal-reasoning-in-llms
spatial-reasoning-in-llms
causal-reasoning-in-llms
counterfactual-reasoning-prompting
abductive-reasoning-in-llms
deductive-reasoning-chains
inductive-reasoning-in-llms
analogical-transfer-in-llms

## Prompt Sensitivity and Robustness
label-sensitivity-in-prompting
format-sensitivity-in-prompting
order-sensitivity-in-few-shot
surface-form-competition
prompt-brittleness
adversarial-prompt-robustness
distribution-shift-in-prompting
semantic-equivalence-in-prompts
paraphrase-invariance-testing
cross-lingual-prompt-transfer
prompt-calibration-techniques
verbalized-uncertainty
hedge-phrases-in-prompts
overconfidence-in-llm-outputs
underspecification-in-prompts

## Attention Mechanisms and Internals
multi-head-attention-mechanics
cross-attention-in-transformers
self-attention-patterns
attention-head-specialization
induction-heads
copy-suppression-heads
attention-sinks
head-pruning-effects
positional-encoding-variants
rotary-position-embedding
alibi-positional-encoding
flash-attention-algorithm
grouped-query-attention
sliding-window-attention
sparse-attention-patterns

## Emergent Behavior and Capability
emergent-prompting-capability
few-shot-emergent-generalization
chain-of-thought-emergence
semantic-parsing-emergence
multilingual-emergent-transfer
arithmetic-emergence-threshold
in-context-learning-as-meta-learning
task-generalization-in-llms
zero-shot-generalization-mechanisms
capability-elicitation-prompting
latent-capability-unlocking
model-capability-vs-alignment-gap
scaling-and-capability-emergence
instruction-following-emergence
calibration-emergence-in-scale

## Multi-Turn and Dialogue
multi-turn-conversation-management
dialogue-state-tracking-prompts
conversational-context-compression
turn-taking-in-llm-dialogue
persona-consistency-across-turns
memory-injection-in-dialogue
dialogue-grounding-prompts
conversational-repair-prompting
clarification-request-generation
follow-up-question-generation
dialogue-act-classification-prompting
conversation-summarization-prompts
slot-filling-via-dialogue
task-oriented-dialogue-prompting
open-domain-dialogue-prompting

## Evaluation and Benchmarking
benchmark-contamination
train-test-leakage-in-llms
dynamic-benchmarking
adversarial-benchmark-construction
human-vs-llm-eval-agreement
inter-annotator-agreement-in-evals
reference-free-evaluation
rubric-based-llm-evaluation
likert-scale-prompt-evaluation
pairwise-preference-evaluation
win-rate-as-evaluation-metric
evaluation-prompt-design
llm-evaluator-bias
g-eval-scoring-methodology
prometheus-evaluation-model

## Retrieval and Knowledge Integration
dense-retrieval-for-rag
sparse-retrieval-bm25
hybrid-retrieval-patterns
query-rewriting-for-retrieval
iterative-retrieval-augmentation
self-rag-selective-retrieval
corrective-rag-pipeline
adaptive-rag-routing
late-interaction-retrieval
cross-encoder-reranking
reciprocal-rank-fusion
chunking-strategies-for-rag
embedding-model-selection
retrieval-faithfulness
knowledge-conflict-in-rag
```

---

```markdown
# Batch 4

## Cognitive and Psychological Frameworks Applied to LLMs
dual-process-theory-applied-to-llms
cognitive-bias-in-llm-outputs
anchoring-bias-in-llm-reasoning
availability-heuristic-in-llms
framing-effects-on-llm-outputs
representativeness-heuristic-in-llms
confirmation-bias-in-chain-of-thought
base-rate-neglect-in-llms
dunning-kruger-analog-in-llms
social-desirability-bias-in-llms
authority-bias-in-llm-responses
bandwagon-effect-in-rlhf
loss-aversion-analog-in-preference-learning
hindsight-bias-in-llm-evaluation
primacy-and-recency-effects-in-context

## Output Quality and Coherence
discourse-coherence-in-llm-outputs
narrative-consistency-prompting
logical-entailment-verification
non-sequitur-detection-in-outputs
hedging-calibration
specificity-vs-generality-tradeoff
abstraction-level-control
verbosity-control-in-prompts
information-density-optimization
redundancy-reduction-in-outputs
contradiction-detection-in-outputs
claim-strength-calibration
nuance-preservation-in-summarization
stance-consistency-across-output
register-and-tone-control

## Specialized Domain Prompting
medical-clinical-prompting
legal-reasoning-prompting
scientific-hypothesis-generation
mathematical-proof-prompting
code-generation-prompting
code-review-prompting
financial-analysis-prompting
educational-content-prompting
creative-writing-prompting
technical-documentation-prompting
data-analysis-prompting
ethical-reasoning-prompting
historical-reasoning-prompting
philosophical-argument-prompting
cybersecurity-analysis-prompting

## Prompt Compression and Efficiency
prompt-distillation
prompt-pruning
token-efficient-prompting
compressive-context-management
prompt-summarization
in-context-compression
kv-cache-reuse-strategies
selective-context-technique
llmlingua-compression
context-distillation-training
abstractive-context-compression
prompt-token-budgeting
latency-aware-prompt-design
prompt-batching-patterns
streaming-output-management

## Interpretability and Explainability
feature-attribution-in-llms
saliency-mapping-for-prompts
attention-visualization
probing-classifiers
linear-representation-hypothesis
representation-engineering
concept-activation-vectors
logit-lens-technique
causal-tracing-in-transformers
knowledge-localization-in-ffn
factual-association-mechanisms
attention-knockout-analysis
path-patching-methodology
distributed-representations-in-transformers
polysemanticity-in-neural-networks

## Training Dynamics and Data
pretraining-data-influence
memorization-vs-generalization
data-contamination-effects
training-data-attribution
counterfactual-data-augmentation
synthetic-data-generation-for-training
curriculum-learning-for-llms
self-play-data-generation
constitutional-ai-data-pipeline
rlaif-rl-from-ai-feedback
iterative-preference-learning
data-mixture-effects-on-capability
deduplication-effects-on-training
toxic-content-filtering-in-pretraining
domain-adaptive-pretraining
```




# V6 Pipeline - Adding Diagrams ASCII diagrams / Mermaid to Permanent Notes

## Context
I have a pipeline for creating permanent notes for my Obsidian based PKB. The pipeline is at V6.
What I need you todo is to review the pipeline and accompanying files, so you understand how everything works.
- You will find all the information you need inside the pipeline folders.
- The *goal* of this task is to enhance the permanent notes that have been created by the V6 pipeline, specifically by adding relevant diagrams in ASCII format/Mermaid format, to improve the visual representation and understanding of the concepts in the permanent notes.
- Make sure that the LLM in charge of the diagrams adds a YAML Frontmatter section, that determines if this permanent note has been run through the diagram process yet. **NOTE HELPFUL** look at the Enhance Permanent Notes Pipeline for helpful context, and so you see how it is being done in that script.
- The LLM should generate the diagrams based on the content of the permanent note, and the concepts it contains, and should use best practices for diagram design to ensure that the diagrams are clear, informative, and visually appealing.
- Place the created diagrams just below the YAML Frontmatter of each report, and make sure to properly format the diagrams for optimal display in Obsidian.
- Ensure that each diagram is accompanied by a brief description or caption to provide context and enhance understanding, or how to view the diagram.
- **POTENTIAL IMPROVEMENT**: Once the main Local LLM is finished with the batch [roughly-100-note-batches], We can have another LLM run through each of the permanent notes done in that run to add additional enhancements or refinements to the diagrams. Such as making sure the ASCII diagrams are properly aligned and visually appealing, and the mermaid is in working order.
- I'm thinking like 2-4 diagrams each and one mermaid diagram if possible, depending on the content of the permanent note and the concepts it contains.
- Feel free to suggest improvement or refinments.
## Key Locations for Pipeline Reference

Here are the main key locations for you to learn how the pipline works, the ins and outs, and how it runs.
`D:\10_pur3v4d3r's-vault\99-scripts\report-extraction-to-permanent-notes-building-v6` -> V6 Pipeline
`D:\10_pur3v4d3r's-vault\99-scripts\report-extraction-to-permanent-notes-building-v6\README.md` -> Pipeline V6 README
`D:\10_pur3v4d3r's-vault\999-report-organizing\_permanent-notes\v6-llm-elaborated` -> Home of current permanent notes.

`D:\10_pur3v4d3r's-vault\99-scripts\report-extraction-to-permanent-notes-building-v6\enhance_notes.py` -> Script for enhancing permanent notes.

## TASK
1. Review the V6 pipeline and accompanying files to understand how everything works, with a specific focus on the enhance_notes.py script and how it enhances permanent notes by adding additional information to the permanent note.
2. Design and genertae thie pipline addition. The pipeline should be designed to run on batches of roughly 100 permanent notes at a time, and should be able to generate 2-4 diagrams in ASCII format/Mermaid format for each permanent note, depending on the content of the permanent note and the concepts it contains.

---

## Deliverables

### add_diagrams.py
~620-line production script, mirroring enhance_notes.py exactly. Key highlights:

| Component | Detail |
|---|---|
| `Diagram` / `DiagramResponse` | Pydantic models; `_strip_code_fences` validator silently removes accidental ` ``` ` wrappers the LLM may emit |
| `diagram_one()` | Single LLM call; cache key = `(contract_version, model, title, body_sha1[:16])` |
| `build_diagram_section()` | Renders all diagrams into `## 📊 Visual Overview` with `<!-- diagram-pass:N (date) -->` marker |
| `_render_diagram_block()` | Mermaid → `[!abstract]` callout + nested fence; ASCII → plain code block with caption |
| `insert_diagram_section()` | Prepends section before `# Title` in the stripped body |
| `update_frontmatter()` | Writes `provenance.diagram-passes`, `diagram-model`, `last-diagrammed` |
| `write_note_atomic()` | `.tmp → replace` pattern; never leaves a half-written file |
| CLI | `--dry-run`, `--limit`, `--note`, `--re-diagram`, `--bypass-cache`, `--output-dir`, `--model`, `-v/-q`, `--strict` |
| Exit codes | 0 success / 2 dir missing / 4 no notes / 5 strict+failures / 6 Ollama down / 130 ^C |

### tests/test_add_diagrams.py
~310 lines, 40+ tests across 10 test classes. Covers every function in the blueprint:
- Schema validators, `is_empty()`, `has_mermaid()`
- `load_note` happy path + 5 error paths
- `scan_notes` gate / re-diagram / filter / limit / missing dir
- `_body_excerpt` truncation at paragraph boundary
- `_render_diagram_block` mermaid vs ASCII formatting details
- `build_diagram_section` header + marker + all-diagram presence
- `insert_diagram_section` placement order
- `update_frontmatter` all fields + non-mutation guarantee
- `write_note_atomic` atomic write, cleanup, parent mkdir
- CLI `--help`, `--version`, `--dry-run` no-write integration test (mocked Ollama)

### Usage
```bash
# Dry-run preview for 5 notes
python add_diagrams.py --dry-run --limit 5 -v

# Single note
python add_diagrams.py --note chain-of-thought

# Batch of 100
python add_diagrams.py --limit 100

# Run tests
pytest tests/test_add_diagrams.py -v
```

### _v6-llm-elaborated batch of 100 command:
```bash
cd "D:\10_pur3v4d3r's-vault\99-scripts\report-extraction-to-permanent-notes-building-v6" && "D:\10_pur3v4d3r's-vault\.venv\Scripts\python.exe" add_diagrams.py --input-dir "D:\10_pur3v4d3r's-vault\999-report-organizing\_permanent-notes\v6-llm-elaborated" --limit 100

### _psychology-permanent-notes batch of 100 command:
```bash
cd "D:\10_pur3v4d3r's-vault\99-scripts\report-extraction-to-permanent-notes-building-v6" && "D:\10_pur3v4d3r's-vault\.venv\Scripts\python.exe" add_diagrams.py --input-dir "D:\10_pur3v4d3r's-vault\999-report-organizing\_permanent-notes\_psychology-permanent-notes" --limit 100
```

### _universe-permanent-notes batch of 100 command:
```bash
cd "D:\10_pur3v4d3r's-vault\99-scripts\report-extraction-to-permanent-notes-building-v6" && "D:\10_pur3v4d3r's-vault\.venv\Scripts\python.exe" add_diagrams.py --input-dir "D:\10_pur3v4d3r's-vault\999-report-organizing\_permanent-notes\_universe-permanent-notes" --limit 100

### _machine-learning-permanent-notes batch of 100 command:
```bash
cd "D:\10_pur3v4d3r's-vault\99-scripts\report-extraction-to-permanent-notes-building-v6" && "D:\10_pur3v4d3r's-vault\.venv\Scripts\python.exe" add_diagrams.py --input-dir "D:\10_pur3v4d3r's-vault\999-report-organizing\_permanent-notes\_machine-learning-permanent-notes" --limit 100
```



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



