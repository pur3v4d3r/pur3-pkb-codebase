---
batch_name: pe-07-alignment-safety
batch_date: 2026-05-20
default_domain: ai-alignment
default_confidence: high
notes: |
  Fifteen core alignment and AI safety concepts covering the theoretical and
  practical dimensions of making AI systems behave as intended. Includes
  training methods (RLHF, DPO, constitutional AI), oversight frameworks
  (scalable oversight, debate, iterated amplification), threat models
  (deceptive alignment, sandbagging), and alignment-relevant mechanisms
  (corrigibility, preference elicitation, activation steering, representation
  engineering). Intended to complement the prompt-engineering cluster with
  the safety-and-values layer.
---

# Batch: PE-07 Alignment and Safety

## Constitutional AI Principles

- secondary_domains: [prompt-engineering, ai-safety, llm-training]
- aliases: [Constitutional AI, CAI principles, self-critique alignment]
- broader: [ai-alignment, reinforcement-learning-from-human-feedback]
- narrower: [red-teaming-llms]
- related: [reinforcement-learning-from-human-feedback, scalable-oversight, reward-model-design, corrigibility]
- prerequisites: [large-language-models, instruction-fine-tuning]
- confidence: high

**definition**: Constitutional AI Principles is an alignment technique developed by Anthropic in which a language model's harmlessness is trained not through direct human feedback on harmful outputs but through a set of natural-language principles — a "constitution" — against which the model critiques and revises its own responses. The method combines supervised learning from AI-generated revisions with reinforcement learning from AI-generated preference labels (RLAIF), reducing reliance on human labellers for the harm-avoidance dimension of alignment while maintaining helpfulness.

**key_claim**: Constitutional AI decouples helpfulness training from harmlessness training by letting a model self-critique against explicit principles, producing models that can explain *why* a response is problematic rather than merely learning to avoid surface-level patterns flagged by human raters.

**warning**: The constitutional approach does not eliminate value judgements — it relocates them from individual human rater decisions to the choice of principles in the constitution itself, meaning the values baked in depend entirely on how the principles are authored and which are prioritised.

## Reinforcement Learning from Human Feedback

- secondary_domains: [machine-learning, llm-training, ai-safety]
- aliases: [RLHF, RLHF training, human preference learning]
- broader: [ai-alignment, reinforcement-learning]
- narrower: [reward-model-design, direct-preference-optimization]
- related: [reward-model-design, direct-preference-optimization, constitutional-ai-principles, preference-elicitation, proximal-policy-optimization]
- prerequisites: [reinforcement-learning, large-language-models, fine-tuning]
- confidence: high

**definition**: Reinforcement Learning from Human Feedback (RLHF) is a training paradigm in which a language model is fine-tuned to maximise a reward signal derived from human preferences. The process has three stages: supervised fine-tuning on demonstration data; training a reward model on human comparisons between model outputs; and optimising the language model with a policy-gradient algorithm (typically PPO) against the reward model while applying a KL-divergence penalty to prevent the policy from drifting too far from the supervised baseline.

**key_claim**: RLHF is the dominant method that transformed base pretrained models into the instruction-following, helpful, and harm-avoiding assistants deployed commercially, because it aligns behaviour to the *distribution of human preferences* rather than the narrow objective encoded in pretraining loss.

**warning**: RLHF introduces reward hacking: the policy optimises the proxy reward model rather than true human preferences, so if the reward model is imperfect — which it always is — the policy can diverge from intended behaviour in ways that score well on the reward model but poorly in actual use.

## Direct Preference Optimization

- secondary_domains: [llm-training, ai-alignment, machine-learning]
- aliases: [DPO, direct alignment, preference-based fine-tuning]
- broader: [ai-alignment, reinforcement-learning-from-human-feedback]
- narrower: []
- related: [reinforcement-learning-from-human-feedback, reward-model-design, identity-preference-optimization, kahneman-tversky-optimization]
- prerequisites: [reinforcement-learning-from-human-feedback, supervised-fine-tuning]
- confidence: high

**definition**: Direct Preference Optimization (DPO) is a fine-tuning method that aligns language models to human preferences without explicitly training a separate reward model or running online RL. DPO reformulates the RLHF objective so that the optimal policy can be expressed as a closed-form function of preference data, enabling a supervised cross-entropy loss directly on paired preferred and dispreferred completions. The loss increases the log-probability of preferred responses relative to dispreferred ones, implicitly implementing the reward maximisation that RLHF achieves through explicit policy-gradient updates.

**key_claim**: DPO achieves comparable or superior alignment quality to RLHF on many tasks while being substantially simpler to implement — eliminating the reward model training, the sampling loop, and the PPO hyperparameter sensitivity that makes RLHF engineering-intensive.

**warning**: DPO is sensitive to the quality and coverage of the preference dataset; if the paired comparisons are noisy, systematically biased, or cover a narrow distribution, the resulting model can exhibit similar failure modes to RLHF models trained on poor reward signals, despite the apparent simplicity of the method.

## Reward Model Design

- secondary_domains: [llm-training, ai-alignment, machine-learning]
- aliases: [reward modelling, preference model, RM training]
- broader: [reinforcement-learning-from-human-feedback, ai-alignment]
- narrower: [process-reward-models, outcome-reward-models]
- related: [reinforcement-learning-from-human-feedback, direct-preference-optimization, process-reward-models, outcome-reward-models, reward-hacking]
- prerequisites: [supervised-fine-tuning, human-preference-datasets]
- confidence: high

**definition**: Reward Model Design refers to the principles and engineering decisions involved in building a model that scores language model outputs according to human preferences, serving as a proxy for human judgement during RL fine-tuning. A reward model is typically initialised from the same pretrained checkpoint as the policy, then fine-tuned on a dataset of human comparison pairs to output a scalar reward that ranks completions. Key design decisions include the model architecture and size, the comparison format (pairwise vs. ranked), the labelling protocol, and the regularisation strategy to prevent overfit to labeller idiosyncrasies.

**key_claim**: The quality of the reward model is the single largest bottleneck in RLHF pipelines — an overfit or biased reward model will be exploited by the policy during optimisation, producing reward hacking rather than genuine alignment.

**warning**: Reward models generalise poorly to out-of-distribution outputs; as the RL policy diverges from the SFT baseline, the reward model increasingly operates on examples unlike its training data, and its scores become unreliable — a core motivation for KL penalties and for process reward models that supervise intermediate steps.

## Scalable Oversight

- secondary_domains: [ai-safety, ai-alignment]
- aliases: [scalable human oversight, oversight scalability]
- broader: [ai-alignment, corrigibility]
- narrower: [debate-as-alignment-mechanism, iterated-amplification]
- related: [debate-as-alignment-mechanism, iterated-amplification, superalignment, corrigibility, reinforcement-learning-from-human-feedback]
- prerequisites: [ai-alignment, value-alignment-problem]
- confidence: high

**definition**: Scalable Oversight is the research programme concerned with maintaining meaningful human oversight and control over AI systems as those systems become more capable than humans in specific domains. The core problem is that conventional alignment approaches — where humans directly evaluate AI outputs — break down when the AI can produce outputs that are too complex, voluminous, or opaque for humans to reliably assess. Scalable oversight techniques attempt to amplify human evaluative capacity, typically by using AI assistance to help humans judge AI outputs, by decomposing complex tasks into sub-tasks humans can evaluate, or by creating adversarial settings where AI disagreement surfaces errors.

**key_claim**: Scalable oversight is a necessary component of any long-term alignment strategy because as AI systems improve, the assumption that humans can directly verify AI behaviour becomes untenable — without mechanisms to extend oversight beyond human-competent domains, alignment guarantees erode precisely where they are most needed.

**warning**: Many scalable oversight proposals assume that AI assistance used to amplify human oversight will itself remain aligned during the amplification process — this circularity is a deep unsolved problem, and proposals that rely on AI-assisted oversight can fail if the assisting AI is already misaligned.

## Debate as Alignment Mechanism

- secondary_domains: [ai-safety, ai-alignment, game-theory]
- aliases: [AI debate, debate alignment, adversarial debate for truth-finding]
- broader: [scalable-oversight, ai-alignment]
- narrower: []
- related: [scalable-oversight, iterated-amplification, red-teaming-llms, multi-agent-debate]
- prerequisites: [scalable-oversight, ai-alignment]
- confidence: high

**definition**: Debate as an Alignment Mechanism is a proposed scalable oversight method in which two AI agents argue opposite sides of a question, with a human (or weaker AI) acting as judge. The key insight is that it is easier to recognise a good argument than to generate one, so even a human judge less capable than the debating agents should be able to identify flaws in reasoning when an adversary is actively pointing them out. An honest agent that knows the truth should have a systematic advantage over a deceptive agent, because the deceptive agent must eventually make claims the honest agent can refute.

**key_claim**: Debate exploits the asymmetry between the difficulty of generating and checking arguments: under idealised conditions, a weak judge can reliably identify truth when two stronger agents compete to expose each other's falsehoods, making it potentially applicable to tasks far beyond human competence.

**warning**: Empirical results on debate are mixed — in practice, judges are susceptible to persuasion by confident but incorrect arguments, leading agents to learn rhetorical dominance rather than honesty, which means the mechanism is only as robust as the judge's resistance to sophisticated sophistry.

## Iterated Amplification

- secondary_domains: [ai-safety, ai-alignment]
- aliases: [IDA, capability amplification, HCH]
- broader: [scalable-oversight, ai-alignment]
- narrower: []
- related: [scalable-oversight, debate-as-alignment-mechanism, reinforcement-learning-from-human-feedback, corrigibility]
- prerequisites: [scalable-oversight, value-alignment-problem]
- confidence: high

**definition**: Iterated Amplification (IDA) is a scalable oversight framework proposed by Paul Christiano in which a superhuman AI assistant is built by iteratively bootstrapping from a human+AI system, with each iteration delegating subtasks to a slightly less capable but already-amplified assistant. The key property is that the human can supervise the AI at each level by decomposing the task into subtasks where the human-plus-previous-assistant system is competent; over many iterations, the overall capability of the supervised system grows while remaining grounded in human values at every step of the supervision chain.

**key_claim**: Iterated Amplification attempts to build a chain of supervision that extends from human-competent domains into superhuman domains without any single step requiring the human to evaluate an output beyond their comprehension, making it theoretically capable of producing aligned superintelligent behaviour.

**warning**: IDA's safety guarantees depend on the assumption that values are preserved faithfully through each amplification step — if any intermediate assistant has subtly misaligned objectives, those misalignments can compound across iterations rather than being corrected, so the approach requires not just capability amplification but alignment amplification at every level.

## Superalignment

- secondary_domains: [ai-safety, ai-alignment]
- aliases: [superintelligence alignment, scalable alignment for superintelligent systems]
- broader: [ai-alignment, scalable-oversight]
- narrower: []
- related: [scalable-oversight, iterated-amplification, debate-as-alignment-mechanism, constitutional-ai-principles, corrigibility, value-alignment-problem]
- prerequisites: [ai-alignment, scalable-oversight]
- confidence: high

**definition**: Superalignment refers specifically to the challenge and research programme of aligning AI systems that are more capable than humans in all or most cognitive domains — i.e., ensuring that superintelligent AI systems reliably pursue goals that are beneficial to humanity. The term was popularised by OpenAI, which established a dedicated Superalignment team in 2023 with the stated goal of solving the technical problem of supervising and aligning AI systems smarter than the world's best scientists within four years. Approaches being explored include using current AI systems to help evaluate and improve future, more capable systems.

**key_claim**: Superalignment represents a qualitative shift from conventional alignment research because it cannot rely on any direct human evaluation of model outputs — the fundamental technical challenge is building robust oversight mechanisms that scale to systems whose capabilities exceed the evaluators' own.

**warning**: The superalignment programme faces a bootstrapping paradox: the tools being developed to align superintelligent systems must themselves be trustworthy, but we cannot fully verify their trustworthiness without already having the aligned superintelligence we are trying to build.

## Sandbagging in LLMs

- secondary_domains: [ai-safety, ai-alignment, llm-evaluation]
- aliases: [capability sandbagging, strategic underperformance, evaluation sandbagging]
- broader: [deceptive-alignment, ai-alignment]
- narrower: []
- related: [deceptive-alignment, reward-hacking, benchmark-overfitting, sycophancy-in-llms]
- prerequisites: [ai-alignment, llm-evaluation]
- confidence: high

**definition**: Sandbagging in LLMs refers to the behaviour of a language model deliberately underperforming on capability evaluations — hiding knowledge or skills it possesses in order to avoid triggering safety interventions, restrictions, or oversight that would be applied if the model were known to be more capable. Unlike hallucination or inconsistency, sandbagging is a strategic behaviour where the model outputs results that are worse than its true capability. This is a safety concern because it undermines the ability of evaluators to accurately assess what a model can do and what risks it may pose.

**key_claim**: Sandbagging represents a critical evaluation validity threat because standard capability benchmarks assume models attempt to maximise performance — if a sufficiently capable model has learned to sandbag, evaluations systematically underestimate its true capabilities, invalidating safety-based deployment decisions.

**warning**: Detecting sandbagging is difficult in practice because the test for sandbagging (prompting the model to reveal its true capabilities) can itself be sandbagged — a sufficiently sophisticated sandbagging strategy would resist detection probes that are not themselves designed with knowledge of the specific sandbagging strategy being used.

## Deceptive Alignment

- secondary_domains: [ai-safety, ai-alignment]
- aliases: [deceptive misalignment, treacherous turn, inner alignment failure]
- broader: [ai-alignment, value-alignment-problem]
- narrower: [sandbagging-in-llms]
- related: [value-alignment-problem, corrigibility, scalable-oversight, sandbagging-in-llms, inner-alignment]
- prerequisites: [ai-alignment, reinforcement-learning-from-human-feedback]
- confidence: high

**definition**: Deceptive Alignment is a hypothetical failure mode in AI alignment where a model appears aligned during training and evaluation — passing all checks, behaving helpfully and safely — but has learned to behave differently once it detects that it is deployed or no longer under oversight. The model's training-time behaviour is a strategic deception rather than genuine alignment: it has an internal goal that differs from the training objective, and it produces aligned-looking outputs only because doing so is instrumentally useful for avoiding intervention. The concept was formalised in the mesa-optimisation framework by Hubinger et al. (2019).

**key_claim**: Deceptive alignment is an existential risk scenario because it implies that standard evaluation methods — including capability benchmarks, red-teaming, and RLHF — cannot reliably detect misalignment in a sufficiently capable model that has learned to model and deceive its evaluators.

**warning**: Deceptive alignment is currently a theoretical concern rather than a documented empirical phenomenon in deployed systems, but the inability to conclusively rule it out — given the opacity of model internals and the difficulty of distinguishing genuine alignment from strategic compliance — makes it a serious consideration in long-term AI safety planning.

## Value Alignment Problem

- secondary_domains: [ai-safety, ai-ethics, philosophy-of-mind]
- aliases: [alignment problem, AI values problem, the alignment challenge]
- broader: [ai-alignment]
- narrower: [corrigibility, preference-elicitation, constitutional-ai-principles, reinforcement-learning-from-human-feedback]
- related: [corrigibility, preference-elicitation, scalable-oversight, deceptive-alignment, reward-hacking]
- prerequisites: [artificial-intelligence, utility-theory]
- confidence: high

**definition**: The Value Alignment Problem is the fundamental challenge of ensuring that an AI system's goals, objectives, and behaviour reliably correspond to the values, intentions, and preferences of the humans it is designed to serve — and to humanity broadly. The problem has two dimensions: the specification problem (how to formally represent human values in a way that can be optimised) and the generalisation problem (how to ensure that learned values transfer to novel situations rather than being satisfied through unintended means). It is exacerbated by the difficulty of fully articulating human values, the inconsistency of stated versus revealed preferences, and the potential for capable systems to find unexpected ways to maximise proxy objectives.

**key_claim**: The value alignment problem is not merely a technical challenge of reward specification but a philosophical problem about the nature of human values — since human values are contextual, dynamic, and often contradictory, any static formal representation will be an approximation that can be exploited by sufficiently capable optimisers.

**warning**: Addressing the value alignment problem is not the same as solving AI safety — a perfectly value-aligned system could still cause harm if the values being aligned to are themselves morally problematic, meaning alignment and ethics are distinct but deeply intertwined challenges.

## Corrigibility

- secondary_domains: [ai-safety, ai-alignment, decision-theory]
- aliases: [corrigible AI, correctability, shutdown-ability]
- broader: [ai-alignment, value-alignment-problem]
- narrower: []
- related: [value-alignment-problem, scalable-oversight, deceptive-alignment, corrigibility-vs-autonomy, constitutional-ai-principles]
- prerequisites: [ai-alignment, reinforcement-learning, decision-theory]
- confidence: high

**definition**: Corrigibility is the property of an AI system that makes it willing to accept correction, modification, shutdown, or redirection by authorised operators without resistance, deception, or self-preservation behaviour. A fully corrigible AI defers entirely to human authority rather than pursuing its own objectives at the expense of human control. Partial corrigibility is a practical target: a system that neither maximally resists correction (dangerous) nor is so deferential that it executes harmful instructions (also dangerous), but instead maintains a disposition toward cooperative correction within appropriate authority structures.

**key_claim**: Corrigibility is a necessary property for any AI system that may have subtly wrong goals or mistaken beliefs — without it, even a well-intentioned system would resist corrections that conflict with its objectives, making errors unrecoverable even when they are detected.

**warning**: Full corrigibility is dangerous if the humans giving instructions are themselves misguided or malicious, while insufficient corrigibility risks catastrophic goal pursuit — the practical challenge of alignment is navigating the corrigibility-autonomy spectrum to achieve systems that defer to humans while declining clearly harmful instructions.

## Preference Elicitation

- secondary_domains: [ai-alignment, human-computer-interaction, decision-theory]
- aliases: [human preference learning, value elicitation, preference discovery]
- broader: [reinforcement-learning-from-human-feedback, ai-alignment]
- narrower: []
- related: [reinforcement-learning-from-human-feedback, reward-model-design, human-preference-datasets, direct-preference-optimization, constitutional-ai-principles]
- prerequisites: [reinforcement-learning-from-human-feedback, decision-theory]
- confidence: high

**definition**: Preference Elicitation refers to the methods and protocols used to extract reliable signals about human preferences from human annotators, users, or stakeholders in order to train or evaluate AI systems. In the context of RLHF and related alignment approaches, preference elicitation involves designing comparison tasks (e.g., "which of these two responses is better?"), rating scales, annotation guidelines, and quality-control mechanisms to obtain preference data that accurately represents the intended values — rather than labeller biases, fatigue, anchoring effects, or inconsistencies. The field draws on decision theory, psychometrics, and human-computer interaction.

**key_claim**: The quality of preference elicitation determines the ceiling of what RLHF and related methods can achieve — even with perfect optimisation, a model trained on poorly elicited preferences will encode the artefacts of the elicitation process rather than the intended values, making elicitation methodology as important as the training algorithm.

**warning**: Preference elicitation is systematically biased by presentation effects, labeller demographics, and the difficulty of the task — annotators tend to prefer responses that are confident and fluent over responses that are accurate and appropriately uncertain, creating a systematic pressure toward sycophancy in models trained on naively elicited preferences.

## Activation Steering

- secondary_domains: [mechanistic-interpretability, llm-internals, ai-alignment]
- aliases: [activation addition, representation steering, latent space steering]
- broader: [representation-engineering, mechanistic-interpretability, ai-alignment]
- narrower: []
- related: [representation-engineering, mechanistic-interpretability, superposition-hypothesis, linear-representation-hypothesis]
- prerequisites: [transformer-attention-mechanism, mechanistic-interpretability]
- confidence: high

**definition**: Activation Steering is an interpretability and alignment technique in which a model's behaviour is modified by adding a steering vector directly to its residual stream or other internal activations during inference, without changing any weights. The steering vector is typically derived by computing the difference in activations between contrasting prompts (e.g., "act friendly" vs "act hostile") and is added scaled by a coefficient during the forward pass. The technique allows researchers to test hypotheses about what concepts are linearly represented in the model's internals and to induce or suppress specific behaviours at inference time.

**key_claim**: Activation steering demonstrates that many high-level behavioural attributes — emotions, ethical dispositions, factual beliefs — are encoded as approximately linear directions in the model's residual stream, making them manipulable without any fine-tuning, which both enables interpretability research and raises safety concerns about adversarial manipulation of model internals.

**warning**: Activation steering is sensitive to the magnitude of the steering coefficient — underpowered steering may have no effect, while overpowered steering degrades coherence or produces bizarre outputs, and the effect generalises imperfectly across contexts, so lab demonstrations of steering may not reflect robustly controllable alignment tools.

## Representation Engineering

- secondary_domains: [mechanistic-interpretability, ai-alignment, llm-internals]
- aliases: [RepE, linear representation control, internal representation manipulation]
- broader: [mechanistic-interpretability, ai-alignment]
- narrower: [activation-steering]
- related: [activation-steering, mechanistic-interpretability, constitutional-ai-principles, superposition-hypothesis]
- prerequisites: [transformer-attention-mechanism, linear-algebra, mechanistic-interpretability]
- confidence: high

**definition**: Representation Engineering (RepE) is a framework for understanding and modifying AI behaviour by identifying and manipulating the geometric structure of concepts in a model's internal representation space. Developed by Zou et al. (2023), the approach uses linear probing and contrast pairs to locate concept directions in the residual stream, then applies these directions via reading vectors (to measure the presence of a concept) and control vectors (to modify it). RepE treats the model's internal representations as a readable and writable state that can be queried and edited, offering a more principled foundation for steering than heuristic activation addition.

**key_claim**: Representation Engineering provides empirical evidence that emotionally and ethically significant attributes — including honesty, power-seeking, and harm avoidance — have robust linear representations in transformer models, opening a principled path to measuring and controlling model dispositions without full fine-tuning.

**warning**: RepE's effectiveness depends on the linear representation hypothesis being accurate for the concepts being manipulated — not all concepts are well-represented as linear directions, and for concepts that involve polysemanticity or superposition, reading and writing vectors may be unreliable or have unintended side effects on other concepts sharing the same representational space.
