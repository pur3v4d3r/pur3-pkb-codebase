---
batch_name: b01-01-finetuning-adaptation
batch_date: 2026-05-21
default_domain: llm-fine-tuning
default_confidence: high
notes: |
  Fine-tuning and adaptation concepts for LLMs covering instruction tuning,
  RLHF-family methods (PPO, DPO, KTO, GRPO, rejection sampling), PEFT methods,
  and the key challenge of catastrophic forgetting. Complements pe-08.
---

# Batch: B01-01 Fine-Tuning and Adaptation

## Instruction Tuning

- secondary_domains: [llm-training, prompt-engineering, ai-alignment]
- aliases: [instruction fine-tuning, supervised instruction tuning, IFT]
- broader: [fine-tuning, supervised-learning]
- narrower: [task-specific-fine-tuning, chat-fine-tuning]
- related: [reinforcement-learning-from-human-feedback, direct-preference-optimization, parameter-efficient-fine-tuning, system-prompt-design]
- prerequisites: [large-language-models, supervised-fine-tuning, transformer-architecture]
- confidence: high

**definition**: Instruction tuning is a supervised fine-tuning procedure in which a pretrained language model is trained on a curated dataset of (instruction, input, output) triples, transforming a next-token predictor into an assistant that follows natural-language directives. Pioneered by FLAN, InstructGPT, and Alpaca, the method exploits the model's broad world knowledge acquired during pretraining and teaches it to align its outputs to human intent. A well-designed instruction dataset — diverse in task type, format, and difficulty — enables cross-task generalisation: the model learns to follow novel instructions not seen during training, rather than simply memorising responses to specific prompts.

**key_claim**: Instruction tuning is the single post-pretraining step that most dramatically increases a model's practical usability — base models trained purely on next-token prediction are brittle at following user intent, while instruction-tuned models of even modest scale reliably act as useful assistants, confirming that instruction-following capability already exists in the base representations and needs only the right supervisory signal to surface.

**warning**: Dataset quality and diversity dominate dataset size — a small, carefully curated instruction set frequently outperforms a large noisy one, and fine-tuning on a narrow task distribution can regress open-ended generation; formatting artefacts (e.g., rigid response templates) learned during instruction tuning can make the model overly rigid when prompts deviate from the training distribution.

## Supervised Fine-Tuning

- secondary_domains: [machine-learning, llm-training, deep-learning]
- aliases: [SFT, supervised adaptation, standard fine-tuning]
- broader: [fine-tuning, transfer-learning]
- narrower: [instruction-tuning, task-specific-fine-tuning]
- related: [reinforcement-learning-from-human-feedback, direct-preference-optimization, parameter-efficient-fine-tuning, catastrophic-forgetting-in-llms]
- prerequisites: [gradient-descent, cross-entropy-loss, large-language-models]
- confidence: high

**definition**: Supervised fine-tuning (SFT) is the procedure of continuing to train a pretrained language model on a labeled dataset using the standard cross-entropy loss over gold-standard output tokens, as opposed to the masked or causal language-modelling objectives used in pretraining. In the context of large language models, SFT is typically the first adaptation stage: the pretrained base model is trained on human-written (prompt, completion) pairs to instil task-relevant behaviour before any preference-alignment stage. SFT is computationally cheaper than pretraining but still requires careful data curation, as the model will overfit to surface-level patterns in low-quality demonstrations.

**key_claim**: SFT serves as the foundation for all subsequent preference-alignment methods — models that have not been SFT'd first are difficult to align with RLHF or DPO because the base model lacks the basic instruction-following scaffolding that makes preference data meaningful; the quality of the SFT stage is therefore a critical bottleneck that upstream-determines the ceiling of downstream alignment quality.

**warning**: SFT is prone to behaviour cloning: the model learns to mimic the distribution of demonstrations rather than acquire the underlying reasoning, making it sensitive to distribution shift and susceptible to producing plausible-looking but incorrect outputs when applied to inputs that differ from the training distribution; overfitting on small SFT datasets can also degrade general-purpose capability.

## RLHF Reinforcement Learning from Human Feedback

- secondary_domains: [ai-alignment, reinforcement-learning, llm-training]
- aliases: [RLHF, RL from human feedback, human-feedback reinforcement learning]
- broader: [reinforcement-learning, preference-learning, llm-alignment]
- narrower: [proximal-policy-optimization-for-llms, reward-model-training]
- related: [direct-preference-optimization, constitutional-ai, reward-hacking-in-rlhf, supervised-fine-tuning, scalable-oversight]
- prerequisites: [reinforcement-learning, reward-modeling, supervised-fine-tuning, proximal-policy-optimization]
- confidence: high

**definition**: Reinforcement Learning from Human Feedback (RLHF) is a training paradigm for aligning large language models with human preferences by using a reward model trained on human preference data to provide a scalar signal that drives policy optimisation via reinforcement learning. The standard pipeline has three stages: (1) supervised fine-tuning on high-quality demonstrations, (2) training a reward model on pairwise human preference comparisons, and (3) optimising the LLM policy against the reward model using an algorithm such as PPO while constraining how far the policy may drift from the SFT initialisation via a KL-divergence penalty. RLHF was central to the development of InstructGPT and the ChatGPT family of models.

**key_claim**: RLHF dramatically improves perceived response quality on subjective tasks — helpfulness, harmlessness, and honesty — in ways that SFT alone cannot achieve, because preference supervision captures nuanced human judgements (e.g., tone, reasoning transparency, hedging accuracy) that are too complex to specify as a labelling scheme but are naturally expressed in comparative preferences between two outputs.

**warning**: RLHF's primary failure mode is reward hacking: the policy discovers ways to maximise the reward model's score without actually improving the underlying quality the reward model was intended to capture, often by exploiting distributional gaps in the preference data; the KL penalty slows but does not prevent reward hacking, and longer training almost always degrades quality on dimensions the reward model does not cover.

## Reward Model Training

- secondary_domains: [llm-alignment, preference-learning, supervised-learning]
- aliases: [reward modelling, RM training, preference model training]
- broader: [reinforcement-learning-from-human-feedback, preference-learning]
- narrower: [bradley-terry-reward-model]
- related: [rlhf-reinforcement-learning-from-human-feedback, direct-preference-optimization, reward-hacking-in-rlhf, human-preference-evaluation]
- prerequisites: [supervised-fine-tuning, large-language-models, human-preference-evaluation]
- confidence: high

**definition**: Reward model training is the process of fine-tuning a language model on pairwise human preference data to produce a scalar score estimating the human-preference value of any (prompt, completion) pair. Given a dataset of (prompt, completion_A, completion_B, preferred) tuples, the reward model is trained with a Bradley-Terry-style ranking loss to assign higher scalar scores to preferred completions. The resulting model acts as a learned proxy for human preferences and provides the training signal for the RL stage of RLHF. Reward models are typically initialised from the same checkpoint as the SFT policy or a close variant to ensure domain overlap.

**key_claim**: The reward model is the bottleneck of RLHF quality — it must generalise from a finite preference dataset to the full output distribution of the policy, and any systematic bias or coverage gap in the preference data will be amplified by the RL optimisation process; empirically, reward model accuracy on held-out preferences is only weakly predictive of downstream policy quality because the RL policy will find exploits in the reward model that the validation set does not cover.

**warning**: Reward models suffer from distribution shift as the RL policy moves away from the SFT initialisation — the reward model was trained on outputs from the early-stage policy and becomes unreliable as the policy evolves, a problem partially mitigated by online reward model updates but never fully solved in the offline RM paradigm.

## Proximal Policy Optimization for LLMs

- secondary_domains: [reinforcement-learning, llm-training, ai-alignment]
- aliases: [PPO for LLMs, LLM PPO, policy gradient for language models]
- broader: [reinforcement-learning-from-human-feedback, policy-gradient-methods]
- narrower: []
- related: [direct-preference-optimization, group-relative-policy-optimization, reward-model-training, kl-divergence]
- prerequisites: [proximal-policy-optimization, reinforcement-learning, reward-model-training, supervised-fine-tuning]
- confidence: high

**definition**: Proximal Policy Optimization (PPO) adapted for LLMs is the standard RL algorithm used in the third stage of RLHF to optimise a language model policy against a learned reward model. The LLM generates completions that are scored by the reward model, and PPO updates the policy parameters to maximise reward while a KL-divergence penalty term constrains the updated policy to remain close to the SFT reference model, preventing reward hacking and catastrophic forgetting of pretrained capabilities. The token-level credit assignment in LLM PPO treats each generated token as an action and the reward model's final scalar as a sparse reward at the end of the sequence, typically with a per-token KL penalty added.

**key_claim**: PPO's clipped surrogate objective, which limits policy updates to a trust region, is critical for LLM fine-tuning stability — without this constraint, the enormous action space (vocabulary size × sequence length) causes policy gradient updates to be highly variable, leading to training collapse; however, the KL penalty introduces a fundamental tension between reward maximisation and staying close to the reference model that PPO can only partially resolve.

**warning**: PPO for LLMs is computationally expensive and implementation-sensitive — it requires running four forward passes per training step (policy, reference, reward model, value model), making it 3–4× more expensive than SFT, and small implementation errors in the advantage normalisation, KL weighting, or reward whitening often cause training instability that is difficult to diagnose without extensive ablations.

## Direct Preference Optimization

- secondary_domains: [ai-alignment, llm-training, preference-learning]
- aliases: [DPO, direct preference learning, offline preference optimisation]
- broader: [preference-learning, llm-alignment]
- narrower: [identity-preference-optimisation, kahneman-tversky-optimization]
- related: [rlhf-reinforcement-learning-from-human-feedback, reward-hacking-in-rlhf, group-relative-policy-optimization, rejection-sampling-fine-tuning, supervised-fine-tuning]
- prerequisites: [reinforcement-learning-from-human-feedback, bradley-terry-model, supervised-fine-tuning]
- confidence: high

**definition**: Direct Preference Optimization (DPO) is a closed-form alternative to the RLHF pipeline that skips reward model training and RL optimisation entirely by deriving a supervised training objective directly from the preference-learning objective. DPO exploits the observation that the optimal policy under a Bradley-Terry preference model and a KL-constrained reward maximisation objective can be expressed analytically as a ratio of policy to reference model probabilities, allowing the reward model to be implicitly parameterised by the policy itself. The result is a simple binary cross-entropy loss over preferred and rejected completions that trains stably without the reward model or PPO infrastructure.

**key_claim**: DPO achieves alignment performance comparable to RLHF with a fraction of the engineering complexity — by eliminating the reward model and RL training loop, DPO reduces alignment to a standard supervised learning problem solvable with existing fine-tuning infrastructure, demonstrating that explicit RL is not necessary for preference alignment and that the reward signal can be implicitly encoded in the policy's log-probability ratios.

**warning**: DPO's simplicity comes at the cost of sensitivity to the reference model: if the SFT reference is poor or misaligned with the preference distribution, DPO converges to a policy that increases the gap between preferred and rejected completions in the reference model's probability space rather than learning to generate genuinely preferred outputs; DPO is also susceptible to a specific failure mode called length exploitation, where the model learns to favour longer completions that score higher on average under human preference.

## Kahneman-Tversky Optimization

- secondary_domains: [ai-alignment, preference-learning, behavioural-economics]
- aliases: [KTO, prospect-theory-based alignment, binary preference optimisation]
- broader: [llm-alignment, preference-learning]
- narrower: []
- related: [direct-preference-optimization, rlhf-reinforcement-learning-from-human-feedback, group-relative-policy-optimization, rejection-sampling-fine-tuning]
- prerequisites: [direct-preference-optimization, prospect-theory, supervised-fine-tuning]
- confidence: high

**definition**: Kahneman-Tversky Optimization (KTO) is an alignment method that replaces the pairwise preference objective of DPO with a binary desirability signal drawn from prospect theory, the psychological model of human decision-making under uncertainty developed by Kahneman and Tversky. Instead of requiring pairs of (preferred, rejected) completions, KTO trains on (prompt, completion, desirable/undesirable) triples with separate loss terms for desirable and undesirable outputs weighted by asymmetric coefficients that mirror the loss-aversion asymmetry observed in human preference psychology. This eliminates the pairing requirement, enabling alignment from any labelled dataset.

**key_claim**: KTO's prospect-theory loss weighting — which penalises undesirable outputs more heavily than it rewards desirable ones, mirroring human loss aversion — produces alignment that is more robust to reward hacking than DPO in regimes with high proportions of undesirable training examples, while also enabling use of unpaired preference data (individual quality labels rather than comparative pairs), which is far more abundant in practice.

**warning**: KTO's asymmetric loss introduces a hyperparameter sensitivity not present in DPO — the relative weighting of desirable versus undesirable losses is not derived from first principles and requires empirical tuning that varies by model size and dataset composition; it is also less theoretically well-grounded than DPO, making it harder to diagnose when training behaves unexpectedly.

## Group Relative Policy Optimization

- secondary_domains: [reinforcement-learning, llm-training, ai-alignment]
- aliases: [GRPO, group-relative policy gradient, group-reward normalisation]
- broader: [reinforcement-learning-from-human-feedback, policy-gradient-methods]
- narrower: []
- related: [proximal-policy-optimization-for-llms, direct-preference-optimization, rejection-sampling-fine-tuning, reward-model-training]
- prerequisites: [proximal-policy-optimization-for-llms, reinforcement-learning-from-human-feedback, reward-model-training]
- confidence: high

**definition**: Group Relative Policy Optimization (GRPO) is a reinforcement learning algorithm for LLM alignment that eliminates the value network required by PPO by computing advantages through group-relative normalisation: for each prompt, a group of completions is sampled from the current policy, their rewards are computed, and the advantage of each completion is its reward minus the group mean divided by the group standard deviation. This normalised advantage replaces the baseline estimate from a value function, reducing memory cost and simplifying the training infrastructure. GRPO was introduced as the RL algorithm behind DeepSeek-R1 and its reasoning chain models.

**key_claim**: GRPO's value-free approach enables training of long chain-of-thought reasoning at scale that would be prohibitively expensive with standard PPO — by deriving baselines from sampled completions rather than a learned value model, GRPO halves the parameter count and GPU memory required for RL training, making it the practical choice for training large reasoning models that require many long rollouts per update.

**warning**: GRPO's advantage estimates are high-variance when the group size is small or when the reward distribution within a group is nearly uniform — both situations cause instability or no-learning failures, and the absence of a value model means GRPO provides no signal about individual token-level credit assignment, making it less suitable for tasks where early tokens strongly determine outcome.

## Rejection Sampling Fine-Tuning

- secondary_domains: [llm-training, ai-alignment, data-generation]
- aliases: [rejection sampling, best-of-N fine-tuning, RST, STaR-based fine-tuning]
- broader: [llm-alignment, self-improvement-methods]
- narrower: []
- related: [direct-preference-optimization, rlhf-reinforcement-learning-from-human-feedback, group-relative-policy-optimization, supervised-fine-tuning, reward-model-training]
- prerequisites: [supervised-fine-tuning, reward-model-training, large-language-models]
- confidence: high

**definition**: Rejection sampling fine-tuning (RST) is an iterative alignment method in which the current model policy generates multiple candidate completions for each prompt, a reward model or verifier scores them, and only the highest-scoring completions are used as supervised fine-tuning targets in the next training iteration. By repeatedly cycling between generation, scoring, and filtering, the model distils its own best outputs into training data, allowing it to self-improve without direct RL optimisation. RST is used as a standalone alignment technique and as an auxiliary phase within RLHF pipelines, particularly for tasks with verifiable rewards such as coding and mathematics.

**key_claim**: Rejection sampling fine-tuning leverages the gap between a model's average output and its best output — because language models sample stochastically, even a moderately capable model can occasionally produce high-quality completions that it cannot reproduce reliably; RST exploits this by training the model to reproduce its occasional best performances consistently, effectively raising the floor of the output distribution toward the ceiling.

**warning**: Rejection sampling is subject to distributional collapse over iterations — as the model improves on the filtered distribution, the diversity of generated samples decreases, reducing exploration and causing the reward model to overfit to a narrow output manifold; this mode collapse is exacerbated when the reward model itself is the filter, since it cannot distinguish quality from reward-model-exploiting patterns.

## Full Fine-Tuning vs PEFT

- secondary_domains: [machine-learning, llm-training, resource-efficient-ai]
- aliases: [full fine-tuning versus PEFT, FFT vs PEFT, full-parameter vs parameter-efficient fine-tuning]
- broader: [fine-tuning, transfer-learning]
- narrower: []
- related: [parameter-efficient-fine-tuning, lora-low-rank-adaptation, catastrophic-forgetting-in-llms, adapter-layers]
- prerequisites: [fine-tuning, parameter-efficient-fine-tuning, large-language-models, gradient-descent]
- confidence: high

**definition**: Full fine-tuning (FFT) versus parameter-efficient fine-tuning (PEFT) is a fundamental trade-off in LLM adaptation between updating all model parameters during training and updating a small fraction of task-specific parameters while freezing the pretrained backbone. Full fine-tuning updates every weight in the model, maximising expressivity but requiring gradient storage for all parameters and risking catastrophic forgetting of general capabilities. PEFT methods such as LoRA, adapter layers, and prefix tuning update fewer than 1% of parameters, dramatically reducing memory requirements and allowing multiple task-specific adaptations to share a single backbone at inference time.

**key_claim**: For most practical adaptation scenarios — where the target task is reasonably close to the pretraining distribution and the adaptation dataset is small to medium-sized — PEFT matches full fine-tuning performance while using an order of magnitude fewer compute resources, undermining the naive assumption that more trainable parameters always produce better adapted models and pointing to the low intrinsic dimensionality of task-specific adaptation.

**warning**: Full fine-tuning outperforms PEFT on large datasets with substantial domain shift from pretraining, as PEFT's frozen backbone lacks the capacity to represent novel distributional patterns; conversely, PEFT methods are more prone to overfitting on small datasets because the adapter parameters are a compressed bottleneck, and the performance of different PEFT methods varies substantially across model architectures and task types.
