---
batch_name: b03-06-training-dynamics
batch_date: 2026-05-22
default_domain: machine-learning
default_confidence: high
notes: |
  Fifteen training dynamics and data pipeline topics: pretraining data
  influence, memorisation vs. generalisation, data contamination,
  training data attribution, counterfactual data augmentation, synthetic
  data generation, curriculum learning, self-play data generation,
  Constitutional AI data pipeline, RLAIF, iterative preference learning,
  data mixture effects, deduplication effects, toxic content filtering,
  and domain adaptive pretraining.
---

# Batch: B03-06 Training Dynamics and Data Pipelines

## Pretraining Data Influence

- secondary_domains: [large-language-models, machine-learning, data-science, training-dynamics]
- aliases: [training data influence on LLM behaviour, pretraining corpus effects, training data impact analysis]
- broader: [training-dynamics-and-data-pipelines, machine-learning, large-language-models]
- related: [training-data-attribution, data-contamination-effects, memorization-vs-generalization, data-mixture-effects-on-capability]
- prerequisites: [machine-learning, large-language-models, training-dynamics]
- confidence: high

**definition**: Pretraining Data Influence refers to the study of how the composition, quality, diversity, and provenance of the large-scale text corpora used to pretrain language models shapes the models' capabilities, knowledge, biases, and failure modes — investigating the causal relationship between specific training data characteristics and specific model behaviours. Pretraining data influence research uses influence functions (attributing model predictions to training examples), data ablation studies (measuring capability changes when specific data sources are removed), contamination analysis (assessing the effect of benchmark data in training), and controlled pretraining experiments that vary specific data composition parameters. Understanding pretraining data influence is foundational for intentional data curation, capability steering, debiasing, and for understanding the provenance of emergent model capabilities.

**key_claim**: Pretraining Data Influence is highly non-uniform across data sources — studies using influence functions and data ablation demonstrate that a small fraction of pretraining data accounts for a disproportionate fraction of a model's performance on specific benchmarks and capabilities, with code data, mathematical text, and structured reference material having outsized influence on reasoning and factual capabilities relative to their proportion of total training tokens; this non-uniform influence motivates targeted data curation rather than indiscriminate data volume scaling as the primary lever for capability improvement.

**warning**: Pretraining Data Influence is computationally expensive to measure precisely — applying influence functions to large LLMs requires computation that scales with the number of training examples and model parameters, making exact influence attribution infeasible for production-scale models without approximation methods that introduce their own estimation error; influence estimates for large models are inherently approximations, and conclusions about data influence drawn from proxy tasks or smaller-scale experiments may not quantitatively generalise to production-scale training.

## Memorization vs. Generalization

- secondary_domains: [large-language-models, machine-learning, statistical-learning-theory, training-dynamics]
- aliases: [training data memorisation in LLMs, verbatim memorisation, LLM generalisation vs. overfitting]
- broader: [training-dynamics-and-data-pipelines, machine-learning, large-language-models]
- related: [pretraining-data-influence, data-contamination-effects, training-data-attribution, deduplication-effects-on-training]
- prerequisites: [statistical-learning-theory, machine-learning, large-language-models]
- confidence: high

**definition**: Memorization vs. Generalization in LLMs refers to the spectrum between two extreme learning modes: verbatim memorisation (where the model has stored specific training examples and can reproduce them exactly when prompted with prefixes or related queries) and robust generalisation (where the model has extracted abstract patterns from training examples and can apply them to novel inputs never seen during training). LLM memorisation research quantifies the proportion and type of training data that models verbatim memorise (typically rare, frequently repeated, or distinctive examples), the conditions that promote memorisation (data duplication, training sequence length, model scale), and the implications of memorisation for privacy (memorised PII can be extracted), copyright (memorised text may be reproduced verbatim), and benchmark contamination (memorised benchmarks inflate apparent performance).

**key_claim**: Memorization vs. Generalization in LLMs follows a predictable duplication-scaling pattern — controlled memorisation studies show that training examples that appear multiple times in the pretraining corpus are memorised at substantially higher rates than single-occurrence examples (10x duplication produces approximately 10x higher memorisation rates), and that larger models have higher memorisation capacity for single-occurrence examples at comparable training budgets; these patterns suggest that data deduplication is the most effective lever for reducing memorisation risk, while model scale increases both generalisation capability and memorisation capacity, creating a capability-memorisation tradeoff at scale.

**warning**: Memorization vs. Generalization cannot be cleanly separated by model behaviour on standard benchmarks — a model may appear to generalise well on held-out test sets while actually memorising the test distribution (if the test examples are similar to training examples), or may appear to memorise while actually having generalised to a pattern that the training example exemplifies; distinguishing genuine generalisation from sophisticated pattern matching that resembles generalisation requires controlled adversarial evaluation on inputs specifically designed to have no training-distribution analogues.

## Data Contamination Effects

- secondary_domains: [large-language-models, evaluation-methodology, training-dynamics, benchmark-evaluation]
- aliases: [benchmark contamination, evaluation contamination in LLMs, test set leakage]
- broader: [training-dynamics-and-data-pipelines, evaluation-methodology, large-language-models]
- related: [memorization-vs-generalization, pretraining-data-influence, training-data-attribution, deduplication-effects-on-training]
- prerequisites: [evaluation-methodology, large-language-models, training-dynamics]
- confidence: high

**definition**: Data Contamination Effects refer to the inflation of benchmark evaluation scores that occurs when the model's pretraining data includes examples from the evaluation benchmark — causing the model to appear to perform better than it actually would on truly novel instances of the task because it has seen or memorised specific benchmark examples during training. Data contamination is a pervasive challenge in LLM evaluation because pretraining corpora scraped from the internet inevitably include text from benchmark datasets that have been published online, and the scale and diversity of pretraining data makes complete contamination detection computationally challenging. Data contamination effects inflate apparent model capability, undermine comparisons between models trained on different datasets, and mislead capability assessments used to make deployment decisions.

**key_claim**: Data Contamination Effects are substantial and difficult to control for — contamination detection studies consistently find significant overlap between LLM pretraining corpora and standard NLP benchmarks, and controlled experiments showing the performance difference between clean (de-contaminated) and contaminated evaluation subsets reveal contamination-inflated performance gains of 5–30% on specific benchmarks; this level of contamination inflation is large enough to invalidate conclusions about capability improvements that fall within the contamination-inflation range, calling for systematic contamination detection and reporting in all LLM benchmark evaluations.

**warning**: Data Contamination Effects are difficult to retrospectively correct for once a model has been trained — identifying which specific training examples a model memorised after training requires extensive probing and inference, and decontaminated evaluation requires creating fresh benchmarks that were not publicly available when the model's training data was collected; the gold standard for contamination-free evaluation (prospectively creating benchmarks not publicly released until after training) is practically challenging for ongoing research, necessitating contamination detection, reporting, and performance adjustment as the current best practice rather than elimination.

## Training Data Attribution

- secondary_domains: [large-language-models, machine-learning, data-science, interpretability]
- aliases: [training example attribution, influence attribution for LLMs, data source attribution]
- broader: [training-dynamics-and-data-pipelines, interpretability, large-language-models]
- related: [pretraining-data-influence, memorization-vs-generalization, data-contamination-effects, feature-attribution-in-llms]
- prerequisites: [influence-functions, machine-learning, large-language-models]
- confidence: high

**definition**: Training Data Attribution refers to the methods for identifying which specific training examples most strongly influenced a model's specific predictions, behaviours, or knowledge — tracing model outputs back to their source training data. Training data attribution methods include influence functions (computing the gradient-based approximation of how removing a training example would change the model's prediction), TracIn (integrating gradients over the training trajectory), nearest-neighbour retrieval in embedding space, and data model attribution approaches. Attribution serves multiple practical purposes: explaining model predictions to end users ("this model output is based on these training documents"), identifying the sources of model biases, supporting copyright attribution for training data, and debugging unexpected model behaviours by tracing them to specific training sources.

**key_claim**: Training Data Attribution via influence functions reveals that LLM predictions are dominated by a surprisingly small number of highly influential training examples — influence attribution studies on classification and generation tasks find that the top 0.01–0.1% of training examples by influence score account for a disproportionate fraction of attributable influence for specific predictions, with the highly influential examples being semantically similar to the test input; this concentrated influence distribution means that targeted training data interventions (removing or reweighting a small set of high-influence examples) can substantially alter specific model behaviours without requiring full retraining on modified data.

**warning**: Training Data Attribution using influence functions has known approximation quality issues for large LLMs — influence functions require computing inverse Hessian-vector products that become increasingly expensive and numerically unstable as model scale increases, and approximations used for tractability (Gauss-Newton Hessian approximation, stochastic estimation) introduce errors that can cause the identified high-influence examples to be incorrect; empirical validation of attribution quality against held-out ground truth should be performed before using influence attribution results for consequential decisions about training data modification or copyright attribution claims.

## Counterfactual Data Augmentation

- secondary_domains: [large-language-models, machine-learning, data-augmentation, robustness]
- aliases: [causal data augmentation, minimal pair augmentation, counterfactual training examples]
- broader: [training-dynamics-and-data-pipelines, data-augmentation, machine-learning]
- related: [synthetic-data-generation-for-training, curriculum-learning-for-llms, training-data-attribution, deduplication-effects-on-training]
- prerequisites: [data-augmentation, causal-inference, machine-learning, large-language-models]
- confidence: high

**definition**: Counterfactual Data Augmentation refers to the technique of expanding training datasets by generating or curating counterfactual examples — minimally modified versions of existing training examples where a specific causal feature is changed and the label correspondingly changes — to train models that are causally sensitive to the relevant features rather than relying on spurious correlations. In NLP, counterfactual augmentation involves creating minimal pairs that differ in a specific linguistic feature (e.g., changing the sentiment word in a sentiment analysis example, changing the pronoun in a coreference example, negating a factual claim) to ensure that the model learns to track the causally relevant feature rather than any of its non-causal correlates. Counterfactual augmentation addresses a fundamental challenge of supervised learning from naturalistic data: spurious correlations in natural language datasets are numerous and the model will learn whichever correlations are most predictive, not necessarily the causally correct ones.

**key_claim**: Counterfactual Data Augmentation substantially reduces model reliance on spurious correlations that appear robust on standard benchmarks but fail on distribution-shifted evaluation — models trained with counterfactually augmented data show 20–40% improvements on challenge sets designed to break spurious correlations, compared to models trained on the original data, while maintaining equivalent performance on standard benchmarks; this robustness improvement demonstrates that augmented models have genuinely learned the causally relevant features rather than achieving benchmark performance through spurious correlation exploitation.

**warning**: Counterfactual Data Augmentation quality depends critically on the quality and completeness of the counterfactual generation process — poorly constructed counterfactuals that inadvertently change multiple features simultaneously rather than the intended single feature train the model on inconsistent causal signals that may be more confusing than the original uncounterfactual data; high-quality counterfactual augmentation requires expert annotation or carefully validated automatic generation that verifies the minimality and label-correctness of each generated counterfactual.

## Synthetic Data Generation for Training

- secondary_domains: [large-language-models, data-generation, machine-learning, training-dynamics]
- aliases: [LLM-generated training data, synthetic pretraining data, model-generated training examples]
- broader: [training-dynamics-and-data-pipelines, data-augmentation, large-language-models]
- related: [counterfactual-data-augmentation, self-play-data-generation, constitutional-ai-data-pipeline, rlaif-rl-from-ai-feedback]
- prerequisites: [data-generation, machine-learning, large-language-models]
- confidence: high

**definition**: Synthetic Data Generation for Training refers to the use of large language models (or other generative models) to generate training data for downstream machine learning tasks — producing labelled examples, reasoning chains, preference pairs, or instruction-following demonstrations that supplement or replace human-annotated training data. Synthetic data generation methods include self-instruct (generating instruction-following examples using an LLM prompted with seed instructions), bootstrapped annotation (using a capable model to generate labels for unlabelled examples), constitutional AI data generation (generating self-critiqued revisions as preference training data), and model-generated reasoning chains (using chain-of-thought prompting to generate reasoning annotations for fine-tuning). Synthetic data has become a primary training data source for instruction tuning, RLHF preference data, and reasoning data, addressing the scalability and cost limitations of human annotation.

**key_claim**: Synthetic Data Generation for Training enables capability improvements beyond what human annotation alone can provide — self-instruct and related synthetic data methods have demonstrated that fine-tuning smaller models on LLM-generated instruction data produces instruction-following capabilities comparable to or exceeding models fine-tuned on human-annotated data of similar scale, and synthetic reasoning chain data has enabled reasoning capability improvements in smaller models that did not emerge from pretraining alone; these results suggest that synthetic data quality is sufficient to transfer capabilities from a capable teacher model to a student model through imitation learning on generated data.

**warning**: Synthetic Data Generation for Training risks amplifying the failure modes and biases of the generating model through training data distribution — models trained on synthetic data generated by a biased or capability-limited teacher model will learn and potentially amplify the teacher's systematic errors, and iterative self-improvement through synthetic data (model generates data, model trains on its own generated data) can accelerate both capability improvement and bias amplification through feedback loops; synthetic data quality verification against human annotation standards is required to identify systematic biases before they are amplified through training.

## Curriculum Learning for LLMs

- secondary_domains: [large-language-models, machine-learning, training-dynamics, pedagogy]
- aliases: [training curriculum for language models, difficulty-ordered training, competence-based training]
- broader: [training-dynamics-and-data-pipelines, machine-learning, large-language-models]
- related: [pretraining-data-influence, synthetic-data-generation-for-training, data-mixture-effects-on-capability, counterfactual-data-augmentation]
- prerequisites: [machine-learning, curriculum-learning, large-language-models, training-dynamics]
- confidence: high

**definition**: Curriculum Learning for LLMs refers to the training strategy of presenting training examples to a language model in a structured sequence organised by difficulty or relevance — starting with simpler, cleaner, or more foundational examples and progressively introducing more complex, diverse, or challenging examples — with the goal of improving final model capability and training efficiency compared to random data ordering. Curriculum learning for LLMs encompasses data difficulty scoring methods (perplexity-based, quality-based, length-based), curriculum scheduling (how quickly to transition from easy to hard examples), multi-stage pretraining with changing data mixtures (stage 1: broad corpus, stage 2: quality-filtered subset, stage 3: domain-specific fine-tuning data), and anti-curriculum (hard examples first) as a variant that may benefit specific learning objectives.

**key_claim**: Curriculum Learning for LLMs via multi-stage training with quality-escalating data mixtures produces better final model quality than single-stage training on the same total data — studies of LLaMA-2, Phi, and related models show that training on carefully curated high-quality data (textbooks, code, clean web text) in the final training stage substantially improves downstream benchmark performance even when the high-quality data is a small fraction of total training data; this finding has motivated the "textbook-quality" data curation approach where a relatively small but high-quality dataset used in later training stages produces outsized capability improvements relative to its token count.

**warning**: Curriculum Learning for LLMs is highly sensitive to the difficulty-scoring methodology — incorrect difficulty ordering (training on overly difficult examples before establishing foundational patterns, or never progressing to sufficient difficulty) can produce worse outcomes than random ordering by creating instability or capability gaps; the optimal curriculum schedule is task-specific, model-scale-specific, and sensitive to the definition of "difficulty" used, requiring empirical validation for each new model configuration rather than applying a single fixed curriculum design across architectures.

## Self-Play Data Generation

- secondary_domains: [large-language-models, machine-learning, reinforcement-learning, training-dynamics]
- aliases: [self-play training data, adversarial self-improvement, LLM self-play for capability]
- broader: [training-dynamics-and-data-pipelines, reinforcement-learning, large-language-models]
- related: [synthetic-data-generation-for-training, rlaif-rl-from-ai-feedback, iterative-preference-learning, constitutional-ai-data-pipeline]
- prerequisites: [reinforcement-learning, game-theory, machine-learning, large-language-models]
- confidence: high

**definition**: Self-Play Data Generation refers to the technique of using a language model to generate both sides of an interaction (questions and answers, critic and responder, opponent and proposer) to create training data that progressively challenges the model's current capabilities — analogous to game-playing self-play (AlphaGo, AlphaZero) where a model improves by playing against itself. In the LLM context, self-play is used to generate adversarial prompts that identify capability boundaries, to generate debate data (one model argues both sides), to create evaluation challenges, and to bootstrap preference training data by having the model generate and evaluate multiple response candidates. Self-play data generation enables capability improvement without human annotation by generating challenges at the current capability frontier.

**key_claim**: Self-Play Data Generation enables capability bootstrapping beyond the initial model's demonstrated knowledge — self-play methods where an LLM generates problems and then attempts to solve them, with successful solutions used as training data (STaR, Quiet-STaR), have demonstrated that models can learn to solve problem types they initially fail on by bootstrapping from problems where they occasionally succeed; this capability bootstrapping property makes self-play data generation a powerful mechanism for extending LLM capabilities into domains where human annotation is scarce or the initial model has only marginal capability.

**warning**: Self-Play Data Generation for capabilities is limited by the model's current capability ceiling — self-play can only generate training data that the model can produce and evaluate, so capabilities genuinely beyond the model's current reach cannot be bootstrapped through self-play without external grounding (verified solutions, external rewards); self-play that generates both questions and purported answers without external verification of answer correctness will reinforce existing model reasoning patterns including errors, potentially amplifying systematic mistakes rather than correcting them.

## Constitutional AI Data Pipeline

- secondary_domains: [large-language-models, ai-safety, training-dynamics, rlhf]
- aliases: [CAI data pipeline, constitutional AI training, RLAIF with constitutional principles]
- broader: [training-dynamics-and-data-pipelines, ai-safety, rlhf, large-language-models]
- related: [rlaif-rl-from-ai-feedback, iterative-preference-learning, synthetic-data-generation-for-training, context-distillation-training]
- prerequisites: [rlhf, ai-safety, large-language-models, training-dynamics]
- confidence: high

**definition**: The Constitutional AI Data Pipeline refers to the training data generation and model alignment methodology developed by Anthropic that uses a set of explicit principles (a "constitution") to generate preference training data through AI self-critique and revision, replacing or supplementing human annotation of model outputs. The CAI pipeline proceeds in two stages: (1) a supervised learning stage where the model generates responses to harmful prompts, critiques them against constitutional principles, and revises them — generating self-critiqued revision pairs used for supervised fine-tuning; (2) a reinforcement learning stage where a preference model trained on AI-labelled preference data (RLAIF) is used as the reward model for RL fine-tuning, encoding constitutional principles as the reward signal rather than relying solely on human preferences.

**key_claim**: The Constitutional AI Data Pipeline produces models with better calibrated refusal behaviour than RLHF alone — controlled comparisons between CAI-trained and standard RLHF-trained models show that CAI produces models that refuse genuinely harmful requests at higher rates while being less likely to over-refuse benign requests that superficially resemble harmful ones, because constitutional principles provide explicit guidance that distinguishes harmful from harmless requests; this improved calibration reflects the constitutional principles' capacity to encode the rationale for refusal decisions in a way that produces more nuanced and principled refusal behaviour than human feedback preferences.

**warning**: The Constitutional AI Data Pipeline's effectiveness depends critically on the quality and completeness of the constitutional principles — incomplete constitutions (missing important harmful behaviours), ambiguous principles (that the model interprets inconsistently), and principles that conflict (producing contradictory guidance for some inputs) reduce the calibration quality of CAI-trained models; additionally, CAI principles encode the values and priorities of the constitution authors, and constitutional bias (e.g., over-restriction of political or controversial content beyond safety requirements) will be amplified through the training pipeline in ways that are difficult to detect through standard evaluation.

## RLAIF — RL from AI Feedback

- secondary_domains: [large-language-models, reinforcement-learning, training-dynamics, ai-safety]
- aliases: [RL from AI feedback, AI preference labelling, model-as-critic for RLHF]
- broader: [training-dynamics-and-data-pipelines, reinforcement-learning, rlhf, large-language-models]
- related: [constitutional-ai-data-pipeline, iterative-preference-learning, self-play-data-generation, synthetic-data-generation-for-training]
- prerequisites: [rlhf, reinforcement-learning, large-language-models, preference-learning]
- confidence: high

**definition**: RLAIF (Reinforcement Learning from AI Feedback) refers to the variant of RLHF where preference labels for training the reward model are generated by a capable AI system rather than by human annotators — using an LLM to compare response pairs and generate preference scores that substitute for human preference judgments. RLAIF addresses the scalability bottleneck of human-annotated RLHF by enabling preference data generation at scale without human annotation cost, using the labelling AI's values and capabilities to define the reward signal. RLAIF quality depends on the alignment and capability of the labelling AI: a well-aligned, capable labelling AI can produce preference labels that are more consistent and calibrated than human labels for some tasks, while a poorly-aligned or limited labelling AI will encode its own biases and capability limitations into the reward model.

**key_claim**: RLAIF produces model alignment outcomes that are comparable to human-preference RLHF at substantially lower data collection cost — controlled comparisons of RLAIF versus RLHF trained models using the same base model show comparable performance on safety and helpfulness benchmarks, with RLAIF models sometimes outperforming RLHF models on consistency and calibration due to the AI labeller's greater response consistency compared to human annotator variance; this capability parity at reduced cost makes RLAIF the practical choice for many alignment fine-tuning applications, particularly for fine-grained preference distinctions that are easier for a capable AI to distinguish than for human annotators without domain expertise.

**warning**: RLAIF alignment is circular with respect to the labelling AI's values — the reward model trained on RLAIF labels will encode and amplify whatever preferences and biases the labelling AI exhibits, including systematic limitations or misalignments of the labelling AI that may not be visible in standard evaluation; this circularity means that RLAIF cannot correct for deep alignment problems in the labelling model and can amplify subtle biases that appear acceptable in individual labelling decisions but become systematic patterns after RL training on thousands of such decisions; RLAIF deployments should include explicit auditing of the labelling AI's preference calibration against held-out human judgments before using the generated preferences for RL training.

## Iterative Preference Learning

- secondary_domains: [large-language-models, reinforcement-learning, training-dynamics, alignment]
- aliases: [online RLHF, iterative DPO, progressive preference learning]
- broader: [training-dynamics-and-data-pipelines, rlhf, reinforcement-learning, large-language-models]
- related: [rlaif-rl-from-ai-feedback, constitutional-ai-data-pipeline, self-play-data-generation, synthetic-data-generation-for-training]
- prerequisites: [rlhf, preference-learning, reinforcement-learning, large-language-models]
- confidence: high

**definition**: Iterative Preference Learning refers to the training methodology that alternates between generating model responses, collecting preference feedback on those responses, and updating the model based on the collected preferences — repeating this generate-label-update cycle multiple times to progressively improve model quality. Unlike offline RLHF (which trains on a fixed preference dataset collected from the initial model), iterative preference learning continuously generates new preference data from the current model's output distribution, ensuring that the preference signal remains relevant to the model's current capability level and addressing the distribution mismatch problem where the reward model trained on initial model data may be poorly calibrated for the improved model's output distribution.

**key_claim**: Iterative Preference Learning substantially outperforms single-round RLHF on capability and alignment metrics at matched total annotation budgets — empirical comparisons show that allocating a fixed annotation budget to multiple rounds of smaller preference datasets (iterative) versus one round of a larger dataset (offline) produces better final model quality, because iterative learning generates preference data from the current model's distribution rather than the initial model's distribution; the distribution-matched data from later rounds provides more informative signal about the current model's failure modes than the distribution-mismatched data from earlier rounds.

**warning**: Iterative Preference Learning is susceptible to reward hacking amplification through iteration — if the reward model has exploitable weaknesses (ways to achieve high reward scores without actually improving in the intended dimensions), iterative RL will progressively exploit these weaknesses more aggressively in each iteration as the model becomes better at finding reward-maximising outputs; online iterative learning requires continuous reward model recalibration and reward hacking detection to prevent progressive exploitation, as the same annotation budget that enables iterative improvement also enables iterative exploitation without careful reward model maintenance.

## Data Mixture Effects on Capability

- secondary_domains: [large-language-models, training-dynamics, machine-learning, data-science]
- aliases: [pretraining data mixture, training corpus composition effects, data blending for LLMs]
- broader: [training-dynamics-and-data-pipelines, pretraining-data-influence, large-language-models]
- related: [pretraining-data-influence, curriculum-learning-for-llms, domain-adaptive-pretraining, deduplication-effects-on-training]
- prerequisites: [machine-learning, large-language-models, training-dynamics, data-science]
- confidence: high

**definition**: Data Mixture Effects on Capability refer to the changes in LLM capabilities and performance profiles caused by varying the relative proportions of different data sources or domains in the pretraining corpus — finding that models trained on different mixtures of web text, code, mathematical text, books, scientific papers, and other sources develop different capability profiles even at equivalent total training token counts. Data mixture research uses controlled pretraining experiments, data source ablations, and mixing ratio hyperparameter search to characterise how specific capability areas (coding, reasoning, factual recall, language understanding, creative writing) respond to varying the proportion of relevant data sources, enabling intentional capability shaping through data mixture design.

**key_claim**: Data Mixture Effects on Capability exhibit cross-domain transfer — code data improves logical reasoning capabilities even on non-coding tasks, mathematical text improves structured reasoning, and multilingual data improves cross-lingual generalisation beyond the specific languages included; these cross-domain capability transfers indicate that certain data types develop general reasoning or structural capabilities that transfer across domains, making data mixture optimisation a more complex and potentially more powerful lever than optimising only direct-domain data proportions for each target capability.

**warning**: Data Mixture Effects on Capability are non-monotonic and difficult to predict without empirical testing — increasing the proportion of a capability-relevant data source does not always improve performance on the corresponding capability (due to data quality variation, domain mismatch within the source category, and interaction effects with other data sources), and small changes in mixture proportions can have disproportionate effects on specific capabilities; data mixture optimisation requires systematic empirical evaluation across a broad range of capabilities rather than intuitive proportion adjustments, and optimal mixtures identified on smaller-scale experiments may not generalise to larger models.

## Deduplication Effects on Training

- secondary_domains: [large-language-models, training-dynamics, data-science, machine-learning]
- aliases: [training data deduplication, corpus deduplication effects, near-deduplication impact on LLMs]
- broader: [training-dynamics-and-data-pipelines, data-preprocessing, large-language-models]
- related: [memorization-vs-generalization, pretraining-data-influence, data-contamination-effects, toxic-content-filtering-in-pretraining]
- prerequisites: [data-preprocessing, machine-learning, large-language-models, training-dynamics]
- confidence: high

**definition**: Deduplication Effects on Training refer to the impact on LLM training and capability that results from removing or downsampling duplicate or near-duplicate text examples from pretraining corpora — affecting memorisation rates, generalisation quality, training efficiency, and capability benchmark performance. Deduplication is a standard preprocessing step for LLM pretraining corpora (used in GPT-3, PaLM, LLaMA, and most other large-scale models), motivated by the empirical finding that high data duplication increases memorisation of specific training examples, reduces effective training data diversity, and can bias the model toward over-representing duplicated content. Deduplication methods range from exact deduplication (removing identical documents), near-deduplication (removing documents with high n-gram overlap using MinHash/LSH), and semantic deduplication (removing semantically similar documents regardless of textual overlap).

**key_claim**: Deduplication Effects on Training follow a quality-diversity tradeoff where deduplication improves generalisation while reducing effective dataset size — controlled pretraining experiments with varying deduplication stringency show that moderate near-deduplication reduces memorisation by 2–5x and improves downstream benchmark performance while high-stringency deduplication reduces benchmark performance by removing beneficial exposure to diverse phrasings of high-quality content; the optimal deduplication level reflects a balance between the memorisation-reduction benefit of deduplication and the diversity-preservation value of retaining multiple phrasings that provide complementary views of the same concepts.

**warning**: Deduplication Effects on Training vary significantly by domain — aggressive deduplication of domains with naturally repetitive structure (legal text, scientific abstracts, code documentation) removes domain-relevant variation and can substantially impair capability in those domains by reducing exposure to the structural patterns that constitute domain competence; domain-specific deduplication thresholds that account for expected intra-domain similarity are more appropriate than applying a uniform deduplication threshold to heterogeneous pretraining corpora.

## Toxic Content Filtering in Pretraining

- secondary_domains: [large-language-models, content-moderation, training-dynamics, ai-safety]
- aliases: [toxicity filtering for LLM training, harmful content removal in pretraining, pretraining data safety filtering]
- broader: [training-dynamics-and-data-pipelines, content-moderation, ai-safety, large-language-models]
- related: [constitutional-ai-data-pipeline, deduplication-effects-on-training, pretraining-data-influence, toxic-language-in-llms]
- prerequisites: [content-moderation, machine-learning, large-language-models, training-dynamics]
- confidence: high

**definition**: Toxic Content Filtering in Pretraining refers to the pipeline stages that identify and remove harmful, offensive, or unsafe text from pretraining corpora before they are used to train language models — with the goal of reducing the model's tendency to generate harmful content and preventing the encoding of toxic language patterns in model parameters. Toxic content filtering methods include classifier-based filtering (using a separate safety classifier to score and remove documents above a toxicity threshold), word-list filtering (removing documents containing specified offensive terms), heuristic quality filtering (removing text from low-quality or commonly toxic domains), and human-reviewed blocklist filtering (blocking entire domains identified as primarily harmful). Filtering stringency involves a capability-safety tradeoff: aggressive filtering may remove beneficial content alongside toxic content, while insufficient filtering allows toxic patterns to persist in model representations.

**key_claim**: Toxic Content Filtering in Pretraining is insufficient alone for alignment — controlled studies comparing models trained on heavily filtered versus lightly filtered corpora find that filtering reduces the frequency of harmful outputs without eliminating them, because toxic language patterns are also present in non-toxic documents that express, discuss, or critique toxicity; achieving aligned model behaviour requires combining pretraining filtering with post-training alignment methods (RLHF, CAI, instruction tuning), as pretraining filtering alone at feasible filtering rates cannot reduce harmful output rates to deployment-acceptable levels for safety-critical applications.

**warning**: Toxic Content Filtering in Pretraining can introduce capability gaps by removing content that contains both harmful and beneficial information — filtering documents containing offensive language also removes documents that discuss, analyse, critique, or provide counter-examples of that language, and aggressive filtering of politically charged, controversial, or sensitive topic areas can create models with limited ability to discuss these areas helpfully even when safe discussion is appropriate; filtering calibration must distinguish between content that generates harmful behaviour versus content that merely contains mentions of harmful topics, to preserve capability while reducing genuine toxicity.

## Domain-Adaptive Pretraining

- secondary_domains: [large-language-models, transfer-learning, training-dynamics, domain-adaptation]
- aliases: [domain-specific pretraining, continued pretraining for domain adaptation, domain fine-tuning]
- broader: [training-dynamics-and-data-pipelines, transfer-learning, large-language-models]
- related: [pretraining-data-influence, curriculum-learning-for-llms, data-mixture-effects-on-capability, domain-adaptive-pretraining]
- prerequisites: [transfer-learning, domain-adaptation, machine-learning, large-language-models]
- confidence: high

**definition**: Domain-Adaptive Pretraining refers to the technique of continuing to pretrain a general-purpose language model on a large corpus of domain-specific text before task-specific fine-tuning — bridging the distribution gap between the general pretraining corpus and a specialised target domain (medical, legal, scientific, code, financial) to improve downstream task performance in that domain. Domain-adaptive pretraining (DAPT) is distinct from task-specific fine-tuning in that it uses unlabelled domain text (maintaining the pretraining objective) rather than labelled task examples, and is distinct from initial pretraining in that it uses a pre-trained model as the starting point rather than training from scratch. DAPT addresses the limitation that general-purpose LLMs trained on broad web corpora have insufficient exposure to specialised domain vocabulary, conventions, and knowledge patterns to perform optimally on domain-specific tasks.

**key_claim**: Domain-Adaptive Pretraining produces substantially larger domain task improvements than equivalent-compute task-specific fine-tuning for data-scarce specialised domains — studies comparing DAPT followed by task fine-tuning versus task fine-tuning only on matched task datasets show DAPT provides the largest improvements for domains with specialised vocabulary and conventions (biomedical, legal) where the domain distribution is most distant from the general pretraining corpus; DAPT is most valuable when labelled task data is scarce but domain text is abundant, allowing the model to absorb domain conventions before task-specific tuning.

**warning**: Domain-Adaptive Pretraining involves catastrophic forgetting risk — continued pretraining on a narrow domain corpus can degrade the model's performance on general-domain tasks and on tasks from domains not represented in the DAPT corpus, as continued gradient updates on domain-specific text shift model weights away from the general capabilities encoded in the initial pretraining; DAPT should be evaluated for general capability retention alongside domain task improvement, and methods that mitigate forgetting (elastic weight consolidation, replay, learning rate reduction) should be considered for deployments that require both domain expertise and general-purpose capability.
