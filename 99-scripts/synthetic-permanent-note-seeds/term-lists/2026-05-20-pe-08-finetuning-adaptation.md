---
batch_name: pe-08-finetuning-adaptation
batch_date: 2026-05-20
default_domain: llm-fine-tuning
default_confidence: high
notes: |
  Eleven fine-tuning and adaptation concepts covering the methods used to
  specialise pretrained language models for particular tasks or domains.
  Spans full fine-tuning paradigms (instruction fine-tuning, task-specific
  fine-tuning), parameter-efficient methods (LoRA, QLoRA, adapter layers,
  prompt/prefix tuning), and the challenges of adaptation (catastrophic
  forgetting, continual learning, domain adaptation). Also covers the
  tradeoff between fine-tuning and RAG, and self-play as a fine-tuning
  strategy. Intended to complement the alignment cluster.
---

# Batch: PE-08 Fine-Tuning and Adaptation

## Instruction Fine-Tuning

- secondary_domains: [ai-alignment, llm-training, prompt-engineering]
- aliases: [IFT, instruction tuning, FLAN-style tuning, supervised fine-tuning on instructions]
- broader: [fine-tuning, supervised-learning]
- narrower: [task-specific-fine-tuning]
- related: [reinforcement-learning-from-human-feedback, parameter-efficient-fine-tuning, direct-preference-optimization, system-prompt-design]
- prerequisites: [large-language-models, supervised-fine-tuning]
- confidence: high

**definition**: Instruction Fine-Tuning (IFT) is a supervised training procedure in which a pretrained language model is trained on a dataset of (instruction, input, output) triples, teaching the model to follow natural-language directives across diverse tasks. The procedure was popularised by models such as FLAN and InstructGPT and is the primary technique by which base language models — which predict the next token in a corpus — are transformed into assistant models that respond to user queries. A key property of instruction fine-tuning is generalisation: a model trained on a diverse instruction set develops an ability to follow novel instructions not seen during training.

**key_claim**: Instruction fine-tuning is the single step that most dramatically improves the practical usability of a language model — base models trained purely on next-token prediction are unreliable at following user intent, while instruction-tuned models of even modest size can be deployed as useful assistants, demonstrating that the capability exists in the base model but requires the right training signal to surface.

**warning**: The quality and diversity of the instruction dataset matters more than its size — a small, high-quality instruction set often outperforms a large noisy one, but instruction fine-tuning on a narrow task distribution produces a model that follows instructions from that distribution well but may regress on tasks outside it, including open-ended generation.

## Parameter-Efficient Fine-Tuning

- secondary_domains: [machine-learning, llm-training, resource-efficient-ai]
- aliases: [PEFT, parameter-efficient adaptation, efficient fine-tuning]
- broader: [fine-tuning, transfer-learning]
- narrower: [lora-low-rank-adaptation, qlora, adapter-layers, prefix-tuning, prompt-tuning]
- related: [lora-low-rank-adaptation, qlora, adapter-layers, prefix-tuning, prompt-tuning, catastrophic-forgetting-in-llms]
- prerequisites: [fine-tuning, large-language-models, gradient-descent]
- confidence: high

**definition**: Parameter-Efficient Fine-Tuning (PEFT) is a family of techniques for adapting pretrained language models to new tasks or domains by updating only a small fraction of the total parameters, rather than all of them. The motivation is that full fine-tuning of large models is computationally expensive and memory-intensive, and it risks catastrophic forgetting of general capabilities. PEFT methods achieve comparable performance to full fine-tuning on many tasks while updating as few as 0.1–1% of parameters, making it possible to run fine-tuning on consumer hardware and to maintain multiple task-specific adapters on a single backbone.

**key_claim**: PEFT demonstrates that the task-specific information learned during fine-tuning is highly compressible — the delta between a pretrained model and its fine-tuned version lies in a low-dimensional subspace, which is why methods like LoRA that explicitly model this low-rank structure match full fine-tuning performance at a fraction of the compute cost.

**warning**: PEFT methods trained on small datasets are susceptible to overfitting to the adapter parameters while the backbone remains frozen, and different PEFT methods interact differently with the model architecture — results do not transfer cleanly across model families, making empirical validation essential rather than relying on general PEFT claims.

## LoRA Low-Rank Adaptation

- domain: llm-fine-tuning
- secondary_domains: [machine-learning, parameter-efficient-fine-tuning, linear-algebra]
- aliases: [LoRA, Low-Rank Adaptation, low-rank fine-tuning]
- broader: [parameter-efficient-fine-tuning]
- narrower: [qlora, dora]
- related: [parameter-efficient-fine-tuning, qlora, adapter-layers, prefix-tuning, catastrophic-forgetting-in-llms]
- prerequisites: [matrix-factorization, fine-tuning, transformer-attention-mechanism]
- confidence: high

**definition**: LoRA (Low-Rank Adaptation) is a parameter-efficient fine-tuning method that approximates the weight updates during fine-tuning as the product of two low-rank matrices. For each weight matrix W that would be updated, LoRA instead trains two smaller matrices A (d×r) and B (r×k) where the rank r is much smaller than the original dimensions, and the effective weight update is ΔW = BA. During inference, the LoRA weights can be merged into the original weights at zero additional cost, or kept separate to allow hot-swapping of different adaptations. The original weights are frozen throughout training, so only the low-rank matrices are updated.

**key_claim**: LoRA's effectiveness confirms the low-rank intrinsic dimensionality hypothesis for fine-tuning: weight updates during adaptation occupy a very low-dimensional subspace of the full weight space, meaning that fine-tuning with rank-4 or rank-8 matrices can match full fine-tuning despite being orders of magnitude smaller, because the task-specific information is structurally concentrated.

**warning**: The choice of rank is a significant hyperparameter — too low a rank may underfits the task while too high a rank eliminates the parameter savings without improving quality, and applying LoRA to the correct set of weight matrices (e.g., attention only vs. all linear layers) requires empirical tuning that varies by model architecture and task.

## QLoRA

- domain: llm-fine-tuning
- secondary_domains: [machine-learning, quantization, parameter-efficient-fine-tuning]
- aliases: [Quantised LoRA, QLoRA fine-tuning, 4-bit fine-tuning]
- broader: [lora-low-rank-adaptation, model-quantization]
- narrower: []
- related: [lora-low-rank-adaptation, parameter-efficient-fine-tuning, model-quantization, bitsandbytes]
- prerequisites: [lora-low-rank-adaptation, model-quantization, fine-tuning]
- confidence: high

**definition**: QLoRA (Quantised Low-Rank Adaptation) is a fine-tuning method that combines 4-bit quantisation of the frozen base model with LoRA adaptation of the trainable low-rank matrices, enabling fine-tuning of models that would otherwise not fit in GPU memory. Introduced by Dettmers et al. (2023), QLoRA uses a novel 4-bit NormalFloat (NF4) quantisation data type, double quantisation to reduce memory further, and paged optimisers to manage memory spikes during gradient computation. The result is that a 65B-parameter model can be fine-tuned on a single 48 GB GPU with performance comparable to full 16-bit fine-tuning.

**key_claim**: QLoRA fundamentally democratised large-model fine-tuning by reducing the hardware requirements from multi-GPU clusters to single-consumer GPUs, demonstrating that the information bottleneck in fine-tuning is not VRAM-limited in the way previously assumed and that quantisation noise in the frozen backbone is small enough to be compensated by the LoRA adapter layers.

**warning**: QLoRA's quantisation introduces irreducible noise in the frozen backbone weights, which can accumulate with longer training or when fine-tuning on tasks that require precise numerical outputs — for applications where small errors matter (e.g., code generation, mathematical reasoning), full-precision or 8-bit fine-tuning may be preferable despite the higher memory cost.

## Adapter Layers

- secondary_domains: [machine-learning, parameter-efficient-fine-tuning, transfer-learning]
- aliases: [adapters, bottleneck adapters, Houlsby adapters, task adapters]
- broader: [parameter-efficient-fine-tuning]
- narrower: []
- related: [parameter-efficient-fine-tuning, lora-low-rank-adaptation, prefix-tuning, prompt-tuning]
- prerequisites: [fine-tuning, transformer-attention-mechanism, transfer-learning]
- confidence: high

**definition**: Adapter Layers are small bottleneck modules inserted within the layers of a pretrained transformer model, trained while the original model weights are frozen. The canonical architecture (Houlsby et al., 2019) inserts an adapter after each attention sub-layer and feed-forward sub-layer; each adapter consists of a down-projection to a small hidden size, a non-linearity, and an up-projection back to the original dimension. Only the adapter weights are updated during task-specific fine-tuning, preserving the pretrained representations and allowing a single backbone to serve multiple tasks simultaneously by swapping adapter sets.

**key_claim**: Adapter layers demonstrated the viability of the modular adaptation paradigm — that a frozen pretrained model can be specialised for diverse tasks through small trainable additions rather than full retraining, establishing the conceptual foundation for the entire PEFT research direction that LoRA later refined with lower parameter counts.

**warning**: Adapters add inference latency because they introduce additional forward-pass operations that cannot be trivially merged with the original weights (unlike LoRA), making them less deployment-friendly than methods that support weight merging, especially in latency-sensitive production environments.

## Prompt Fine-Tuning vs RAG

- domain: llm-fine-tuning
- secondary_domains: [retrieval-augmented-generation, prompt-engineering]
- aliases: [fine-tuning vs RAG, FT vs RAG tradeoff, parametric vs retrieval knowledge]
- broader: [fine-tuning, retrieval-augmented-generation]
- narrower: []
- related: [retrieval-augmented-generation, instruction-fine-tuning, parameter-efficient-fine-tuning, domain-adaptation-llms, knowledge-conflict-resolution]
- prerequisites: [fine-tuning, retrieval-augmented-generation]
- confidence: high

**definition**: The Fine-Tuning vs RAG tradeoff is the strategic decision between two approaches to improving a language model's behaviour in a specific domain or task: (1) fine-tuning, which bakes knowledge or behaviour into the model's weights through additional training; and (2) Retrieval-Augmented Generation (RAG), which supplies relevant information at inference time through retrieval from an external corpus. Fine-tuning is better suited to instilling persistent behavioural patterns, style, or task formats, while RAG is better suited to providing factual knowledge that changes over time or that is too voluminous to be encoded in model weights.

**key_claim**: The choice between fine-tuning and RAG is not binary — the two approaches are complementary rather than mutually exclusive, and the most effective production systems often combine them: fine-tuning for behavioural alignment (format, tone, task adherence) and RAG for factual grounding (up-to-date, source-attributable information).

**warning**: A common error is using fine-tuning to inject factual knowledge into model weights as a substitute for retrieval — this approach is expensive to update, prone to hallucination when knowledge is incomplete, and lacks source attribution, whereas RAG supports all three requirements natively.

## Domain Adaptation LLMs

- secondary_domains: [llm-training, transfer-learning, nlp]
- aliases: [domain-adaptive pretraining, domain-specific LLMs, domain specialisation]
- broader: [fine-tuning, transfer-learning]
- narrower: []
- related: [instruction-fine-tuning, catastrophic-forgetting-in-llms, continual-learning-llms, prompt-fine-tuning-vs-rag, task-specific-fine-tuning]
- prerequisites: [fine-tuning, large-language-models, transfer-learning]
- confidence: high

**definition**: Domain Adaptation for LLMs refers to the set of techniques used to specialise a general-purpose language model for a specific domain — such as medicine, law, finance, or code — by further training on domain-specific corpora, task data, or combinations thereof. Approaches range from domain-adaptive pretraining (DAPT), where the model continues pretraining on in-domain text before task fine-tuning, to domain-specific instruction fine-tuning, to retrieval augmentation with domain corpora. Effective domain adaptation improves the model's use of domain terminology, reasoning patterns, and implicit knowledge while preserving general language capabilities.

**key_claim**: Domain adaptation via continued pretraining on domain text provides the most durable improvements to domain-specific performance because it updates the model's internal representations of domain concepts rather than merely teaching output formats, but it is expensive and risks catastrophic forgetting of general capabilities without careful regularisation.

**warning**: Domain adaptation can create a false confidence in the model's expertise — a model adapted to medical text may produce fluent medical-sounding responses that are factually incorrect in subtle domain-specific ways, so domain-adapted models require more stringent evaluation on domain-specific factual accuracy, not less.

## Catastrophic Forgetting in LLMs

- secondary_domains: [machine-learning, continual-learning, llm-training]
- aliases: [catastrophic interference, catastrophic forgetting, neural network forgetting]
- broader: [continual-learning-llms, fine-tuning]
- narrower: []
- related: [continual-learning-llms, parameter-efficient-fine-tuning, domain-adaptation-llms, elastic-weight-consolidation]
- prerequisites: [fine-tuning, neural-networks, gradient-descent]
- confidence: high

**definition**: Catastrophic Forgetting in LLMs (also called catastrophic interference) is the tendency of a neural network to abruptly lose performance on previously learned tasks when it is trained on new data. In the context of language models, fine-tuning on task-specific data causes the model's weights to be shifted in ways that degrade its generalisation capabilities on the pretraining distribution and other tasks — the model "forgets" what it knew before, because gradient updates that optimise for the new task overwrite parameters that were critical for prior tasks. The severity is proportional to the distance between the new task distribution and the original training distribution.

**key_claim**: Catastrophic forgetting is the primary reason parameter-efficient fine-tuning methods (which freeze most weights) and regularisation-based approaches have become standard practice — full fine-tuning of large models on task data is dangerous precisely because the model's general capabilities, which took enormous resources to acquire, can be degraded rapidly by narrow supervision signals.

**warning**: Catastrophic forgetting does not always manifest as a visible regression on held-out benchmarks — it can appear as subtle degradation in long-form coherence, cross-domain generalisation, or robustness to out-of-distribution prompts, making it easy to overlook in standard fine-tuning evaluations that only measure target-task performance.

## Continual Learning LLMs

- secondary_domains: [machine-learning, llm-training]
- aliases: [lifelong learning, sequential learning, online learning for LLMs]
- broader: [machine-learning, fine-tuning]
- narrower: []
- related: [catastrophic-forgetting-in-llms, parameter-efficient-fine-tuning, domain-adaptation-llms, elastic-weight-consolidation, knowledge-distillation]
- prerequisites: [fine-tuning, catastrophic-forgetting-in-llms]
- confidence: high

**definition**: Continual Learning for LLMs is the research area concerned with enabling language models to acquire new knowledge and skills sequentially — without forgetting previously learned capabilities and without access to all historical training data simultaneously. The challenge is that standard stochastic gradient descent optimises for the current batch, causing catastrophic forgetting of earlier knowledge. Continual learning methods include regularisation approaches (preventing important weights from changing), architectural approaches (expanding capacity for new knowledge), and replay approaches (maintaining a buffer of past data or generated exemplars to interleave with new training).

**key_claim**: Continual learning is essential for deploying language models in dynamic real-world environments where knowledge, norms, and user requirements evolve — a model that can only be updated by full retraining is impractical at scale, so continual learning methods that enable targeted knowledge updates are a prerequisite for sustainable long-term deployment.

**warning**: Continual learning methods that use a replay buffer — storing past training examples to prevent forgetting — raise privacy and copyright concerns, especially in domains where training data is sensitive, making the choice between replay and regularisation approaches partly a legal and ethical decision rather than purely a technical one.

## Task-Specific Fine-Tuning

- secondary_domains: [machine-learning, nlp, transfer-learning]
- aliases: [task-adaptive fine-tuning, supervised task fine-tuning, downstream fine-tuning]
- broader: [fine-tuning, instruction-fine-tuning]
- narrower: []
- related: [instruction-fine-tuning, domain-adaptation-llms, catastrophic-forgetting-in-llms, parameter-efficient-fine-tuning]
- prerequisites: [fine-tuning, large-language-models, transfer-learning]
- confidence: high

**definition**: Task-Specific Fine-Tuning refers to the process of further training a pretrained language model on labelled data from a specific target task — such as sentiment classification, question answering, natural language inference, or summarisation — to improve its performance on that task. Unlike instruction fine-tuning, which trains across diverse task formats to improve general instruction-following, task-specific fine-tuning is narrowly targeted at optimising for a single task's metric. It typically requires a labelled dataset for the target task and is evaluated by the task's primary benchmark metric.

**key_claim**: Task-specific fine-tuning remains the most reliable approach for achieving state-of-the-art performance on well-defined tasks with sufficient labelled data, because it directly optimises the model for the evaluation distribution — but its narrowness is also its limitation, as it trades breadth of capability for depth in a single domain.

**warning**: Task-specific fine-tuning on small datasets frequently overfits to annotation artefacts rather than the underlying task structure, producing models that score well on the specific benchmark but fail on slight paraphrases or held-out distributions — a consistent problem in the GLUE/SuperGLUE era that drove the move toward instruction-tuned generalist models.

## Self-Play Fine-Tuning

- domain: llm-fine-tuning
- secondary_domains: [ai-alignment, reinforcement-learning, game-theory]
- aliases: [SPIN, self-play training, self-improvement via self-play]
- broader: [fine-tuning, reinforcement-learning-from-human-feedback]
- narrower: []
- related: [reinforcement-learning-from-human-feedback, direct-preference-optimization, self-refine, self-consistency-sampling, iterated-amplification]
- prerequisites: [fine-tuning, reinforcement-learning-from-human-feedback]
- confidence: high

**definition**: Self-Play Fine-Tuning (SPIN) is a method for improving a language model's capabilities without additional human-labelled data by training the model to distinguish its own outputs from human-written text. The model acts as both a generator (producing synthetic training examples) and a discriminator (learning to identify them as inferior to human text), creating a self-improving loop analogous to GAN training. Over iterations, the generator improves to produce outputs that are harder to distinguish from human text, effectively distilling the patterns in the human data more thoroughly than a single supervised fine-tuning pass.

**key_claim**: Self-play fine-tuning demonstrates that the supervision signal in human-written text can be extracted iteratively without additional human annotation — the quality gap between model outputs and human text itself encodes a meaningful learning signal that the model can exploit through the discriminator objective, effectively providing a form of curriculum that tightens as the model improves.

**warning**: Self-play fine-tuning can introduce or amplify existing biases in the model's outputs if the generator component drifts toward a mode collapse — producing a narrow distribution of high-confidence outputs that fool the discriminator but poorly represent the diversity of the original human text distribution.
