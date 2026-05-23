---
batch_name: b03-05-mechanistic-interpretability
batch_date: 2026-05-22
default_domain: mechanistic-interpretability
default_confidence: high
notes: |
  Fifteen mechanistic interpretability and explainability topics: feature
  attribution, saliency mapping, attention visualisation, probing classifiers,
  linear representation hypothesis, representation engineering, concept
  activation vectors, logit lens, causal tracing, knowledge localisation in FFN,
  factual association mechanisms, attention knockout, path patching,
  distributed representations, and polysemanticity.
---

# Batch: B03-05 Mechanistic Interpretability

## Feature Attribution in LLMs

- secondary_domains: [large-language-models, explainability, mechanistic-interpretability]
- aliases: [input feature importance for LLMs, attribution methods for transformers, LLM token attribution]
- broader: [mechanistic-interpretability, explainability, large-language-models]
- narrower: [saliency-mapping-for-prompts, attention-visualization, probing-classifiers]
- related: [saliency-mapping-for-prompts, attention-visualization, causal-tracing-in-transformers, linear-representation-hypothesis]
- prerequisites: [transformer-architecture, explainability, large-language-models]
- confidence: high

**definition**: Feature Attribution in LLMs refers to the methods and techniques for assigning credit or blame to specific input tokens, attention patterns, or intermediate representations for specific outputs produced by a large language model — quantifying the contribution of each input feature to the model's generation decisions. Feature attribution methods for LLMs include gradient-based attribution (computing the gradient of the output with respect to input token embeddings to identify sensitive inputs), attention-based attribution (using attention weights as proxies for token importance), integrated gradients (averaging gradients along a path from a baseline input to the actual input), SHAP values adapted for language models, and counterfactual attribution (measuring output change when specific input features are removed or replaced). Feature attribution is foundational for interpretability analysis, debugging model failures, identifying spurious correlations, and building trust in LLM outputs.

**key_claim**: Feature Attribution in LLMs via gradient-based methods (integrated gradients, gradient x input) provides substantially more accurate attributions than attention-based methods on most generation tasks — empirical comparisons show that attention weights do not reliably reflect the causal importance of input tokens to output generation because attention heads implement many functions beyond weighted input selection (including positional routing, head composition, and skip connections), while gradient-based methods directly measure the mathematical sensitivity of the output to each input, providing a more principled attribution signal; this finding challenges the widespread practice of using attention visualisation as the primary interpretability method.

**warning**: Feature Attribution in LLMs produces post-hoc explanations that may not accurately reflect the model's actual decision process — attribution methods assign numerical scores to input features based on external mathematical analysis of the model, but the model's internal computation may not decompose cleanly into separable feature contributions that these scores represent; attribution scores that appear meaningful and coherent may not correspond to the model's actual reasoning pathway, and interpretability conclusions based solely on attribution analysis without mechanistic validation (causal tracing, activation patching) should be treated as hypotheses requiring further investigation rather than confirmed explanations.

## Saliency Mapping for Prompts

- secondary_domains: [large-language-models, explainability, mechanistic-interpretability, prompt-engineering]
- aliases: [prompt saliency maps, input sensitivity mapping, token salience analysis]
- broader: [mechanistic-interpretability, feature-attribution-in-llms, large-language-models]
- related: [feature-attribution-in-llms, attention-visualization, prompt-pruning, selective-context-technique]
- prerequisites: [feature-attribution-in-llms, gradient-methods, transformer-architecture]
- confidence: high

**definition**: Saliency Mapping for Prompts refers to the application of saliency methods to large language model prompts to visualise which tokens in the input prompt most strongly influence the model's outputs — producing a per-token importance map that identifies which parts of a prompt are driving the model's response. Prompt saliency maps are computed by measuring the gradient of the target output (a specific generated token or a scalar score) with respect to each input token embedding, then aggregating gradient magnitudes to produce a token-level importance score. Saliency mapping enables prompt debugging (identifying which prompt tokens the model is attending to, revealing unexpected dependencies), prompt compression guidance (identifying low-salience tokens as compression candidates), and adversarial prompt analysis (identifying which tokens are driving undesirable outputs).

**key_claim**: Saliency Mapping for Prompts is most practically valuable for prompt debugging — by identifying which input tokens have high saliency for unexpected or incorrect outputs, practitioners can diagnose whether the model is responding to intended task specification tokens (as expected), contextual distractor tokens (indicating distraction), or specific few-shot example features (indicating spurious feature learning) rather than testing hypotheses about failure causes through blind ablation; saliency-guided ablation reduces the number of prompt iterations required to diagnose prompt failures by directing attention to the specific tokens responsible.

**warning**: Saliency Mapping for Prompts has important interpretability limitations — gradient-based saliency maps measure local sensitivity around the specific input, which may not reflect global importance for all inputs the model processes, and attribution scores are influenced by the saturation and linearity properties of the model's activation functions rather than reflecting a clean measure of semantic relevance; saliency maps should be interpreted as one diagnostic signal among several rather than as definitive indicators of why the model produced a specific output.

## Attention Visualization

- secondary_domains: [large-language-models, mechanistic-interpretability, explainability, transformers]
- aliases: [attention map visualisation, transformer attention inspection, attention pattern analysis]
- broader: [mechanistic-interpretability, feature-attribution-in-llms, transformer-architecture]
- related: [feature-attribution-in-llms, saliency-mapping-for-prompts, probing-classifiers, linear-representation-hypothesis]
- prerequisites: [transformer-architecture, attention-mechanism, large-language-models]
- confidence: high

**definition**: Attention Visualization refers to the analysis and visualisation of the attention weight matrices produced by transformer model attention heads — examining which tokens attend to which other tokens at each layer and head — to gain insight into how the model routes and processes information during inference. Attention visualisation tools (BertViz, TransformerLens, circuitsviz) render attention weight matrices as heatmaps, allowing researchers to identify attention patterns (diagonal, horizontal, block patterns), track how specific linguistic relationships are encoded in attention (subject-verb agreement, coreference resolution, syntactic dependencies), and observe how information from specific input positions influences later generation decisions. Attention visualisation has been widely used as an interpretability tool, though its limitations are increasingly well-documented.

**key_claim**: Attention Visualization reveals structural properties of transformer information routing that are not visible through input-output analysis alone — studies using attention visualisation have identified functionally specialised attention heads (induction heads that identify repeated patterns, previous token heads, duplicate token heads) whose consistent structural roles across layers provide important mechanistic evidence for the modular function hypothesis in transformer interpretability; these head-level structural discoveries made through attention analysis motivated subsequent causal tracing and circuit analysis research that confirmed and extended these findings.

**warning**: Attention Visualization does not reliably reflect causal importance of specific tokens for specific outputs — multiple studies have demonstrated that high attention weights do not consistently correlate with causal influence on model outputs (as measured by attention knockout and activation patching), because attention implements information routing rather than direct feature selection, and a token can influence the output through indirect pathways involving low-weight attention connections while a high-weight attended token may be a structural routing signal rather than a semantically meaningful input; attention visualisation alone should not be used to make definitive claims about which input tokens caused specific model outputs.

## Probing Classifiers

- secondary_domains: [large-language-models, mechanistic-interpretability, representation-learning]
- aliases: [diagnostic probes, representation probing, probing tasks for LLMs]
- broader: [mechanistic-interpretability, representation-learning, large-language-models]
- related: [linear-representation-hypothesis, representation-engineering, concept-activation-vectors, feature-attribution-in-llms]
- prerequisites: [representation-learning, linear-classification, transformer-architecture, large-language-models]
- confidence: high

**definition**: Probing Classifiers refer to the interpretability methodology of training simple linear (or sometimes non-linear) classifiers on the internal representations (activations) of a pre-trained language model at specific layers to determine whether specific linguistic or conceptual features are encoded as decodable information in those representations. By holding the LLM frozen and training only a small probe on its representations, researchers test whether a specific concept (part-of-speech, syntactic role, semantic property, world knowledge fact) is linearly decodable from the model's internal state at a specific layer — positive probe accuracy indicates the information is present in the representations, while probe accuracy variation across layers reveals where in the computational hierarchy different types of information emerge and are maintained.

**key_claim**: Probing Classifiers reveal a hierarchical information organisation in transformer LLMs — systematic probing across layers shows that lower layers encode surface-level features (part-of-speech, morphology, character-level patterns), middle layers encode syntactic structure (dependency parsing, constituent structure), and higher layers encode semantic and pragmatic content (word sense, coreference, factual knowledge), reflecting a progression from form to meaning that is consistent across diverse transformer architectures and training paradigms; this hierarchical organisation pattern provides important structural constraints on mechanistic interpretability theories.

**warning**: Probing Classifiers measure the decodability of information from representations but do not demonstrate that the model uses that information for task performance — high probe accuracy shows that a property is encoded in the representations but does not establish that the model's task performance depends causally on that encoding; a model may encode a property in its representations as a byproduct of training without using that encoding in downstream computation, making it essential to complement probing results with causal intervention experiments (activation patching, knockout analyses) that test whether the encoded information is actually used in the model's computations.

## Linear Representation Hypothesis

- secondary_domains: [large-language-models, mechanistic-interpretability, representation-learning, geometry-of-representations]
- aliases: [linear geometry of concepts, linear embedding of features, linear representation theory in LLMs]
- broader: [mechanistic-interpretability, representation-learning, large-language-models]
- related: [representation-engineering, probing-classifiers, concept-activation-vectors, distributed-representations-in-transformers]
- prerequisites: [representation-learning, linear-algebra, transformer-architecture, large-language-models]
- confidence: high

**definition**: The Linear Representation Hypothesis refers to the theoretical claim that large language models represent concepts, features, and factual knowledge as linear directions in their high-dimensional activation spaces — such that a specific concept (e.g., "is a mammal," "sentiment is positive," "the subject is plural") corresponds to a consistent linear direction in the representation space, and interventions that add or subtract this direction from activation vectors predictably modify the model's behaviour with respect to that concept. The hypothesis is motivated by the success of word2vec-style linear vector arithmetic (king - man + woman ≈ queen), extended to transformer hidden states. Evidence for the linear representation hypothesis comes from probing classifier success, representation engineering experiments, and the effectiveness of linear activation steering in controlling model behaviour.

**key_claim**: The Linear Representation Hypothesis is empirically supported for a broad range of concept types in transformer LLMs — studies using representation engineering, concept activation vectors, and sparse probing consistently find that binary properties (true/false, positive/negative sentiment, grammatical/ungrammatical) are represented as approximately linear directions that can be reliably identified by training linear probes, and that interventions adding these directions to activations produce predictable concept-specific behaviour changes at rates substantially above chance; however, the hypothesis holds more reliably for well-defined binary properties than for graded, polysemous, or context-dependent concepts where the linear direction is less consistent.

**warning**: The Linear Representation Hypothesis should be understood as an approximation rather than an exact mechanistic claim — the empirical evidence supports linearity as a useful model for many concept representations, but also documents numerous deviations: polysemanticity (multiple concepts sharing directions), superposition (more concepts than dimensions encoded non-orthogonally), context-dependence (the same concept encoded differently in different contexts), and non-linear interactions between concept directions that linear analysis misses; mechanistic interpretability research relying on linear representation assumptions should validate those assumptions for the specific concepts and contexts under study rather than assuming they hold universally.

## Representation Engineering

- secondary_domains: [large-language-models, mechanistic-interpretability, ai-safety, activation-engineering]
- aliases: [representation control, activation steering via representation, rep-E]
- broader: [mechanistic-interpretability, ai-safety, large-language-models]
- related: [linear-representation-hypothesis, concept-activation-vectors, probing-classifiers, causal-tracing-in-transformers]
- prerequisites: [linear-representation-hypothesis, transformer-architecture, mechanistic-interpretability, large-language-models]
- confidence: high

**definition**: Representation Engineering refers to the interpretability and control methodology that identifies linear directions in transformer LLM activation spaces corresponding to high-level cognitive and behavioural concepts (honesty, emotion, moral judgement, reasoning style), and uses these identified directions to read out model states and steer model behaviour by directly intervening in the activation space during inference. Representation Engineering (Zou et al. 2023) systematically maps the representational geometry of concepts by constructing contrast datasets (pairs of prompts differing only in the target concept), computing mean activation differences, and identifying the principal components of these differences as the concept direction. These concept directions can then be used as probes (measuring the model's current "state" on the concept) or as steering vectors (adding the direction to activations to increase or decrease the concept).

**key_claim**: Representation Engineering enables reliable behavioural control of LLMs through activation-space intervention — experiments adding honesty, emotion, and reasoning-quality concept directions to LLM activations during generation produce measurable, direction-consistent changes in model output quality that are competitive with or superior to prompt-based interventions for the same behavioural objectives; this finding suggests that many prompt-level behavioural instructions operate by shifting the model to activation states that the corresponding representation directions describe, making direct activation-space intervention a more efficient and reliable path to behavioural control than iterative prompt engineering for specific model behaviours.

**warning**: Representation Engineering effects are model-specific and layer-specific — concept directions identified in one LLM do not transfer to other LLMs, even models with similar architectures and training, because representation geometry emerges from the specific training dynamics and data distribution of each model; additionally, the effectiveness of steering vectors is highly sensitive to the layer at which they are injected, with optimal injection layers varying by concept type; deployers of representation engineering methods must recalibrate concept directions for each target model and validate layer sensitivity before production deployment.

## Concept Activation Vectors

- secondary_domains: [large-language-models, mechanistic-interpretability, explainability, representation-learning]
- aliases: [CAVs, testing with concept activation vectors, TCAV method]
- broader: [mechanistic-interpretability, feature-attribution-in-llms, representation-learning]
- related: [representation-engineering, linear-representation-hypothesis, probing-classifiers, feature-attribution-in-llms]
- prerequisites: [representation-learning, linear-classification, mechanistic-interpretability, large-language-models]
- confidence: high

**definition**: Concept Activation Vectors (CAVs) refer to the linear classifiers trained to separate the representations of examples that exhibit a target human-interpretable concept from examples that do not, in the internal activation space of a neural network — providing a directional vector in the activation space that represents the concept and can be used to measure the sensitivity of model predictions to that concept (TCAV: Testing with Concept Activation Vectors). CAVs extend probing classifiers by explicitly connecting the identified representation direction to human-interpretable concepts defined by curated example sets, and by using the CAV direction to compute concept sensitivity scores that quantify how much a specific output decision depends on the presence of the concept in the representation. CAVs are used in image classification interpretability (original application) and increasingly applied to LLM representations.

**key_claim**: Concept Activation Vectors provide a concept-grounded interpretability approach that bridges statistical representation analysis and human conceptual frameworks — unlike gradient attribution methods that measure sensitivity to individual tokens, CAVs measure model sensitivity to semantically defined concept directions that correspond to human-interpretable ideas; this concept-level granularity enables higher-level explanations of model behaviour ("this classification decision was sensitive to the concept of corporate jargon in the input") that are more actionable for model debugging and auditing than token-level attribution ("this token was important").

**warning**: Concept Activation Vectors require carefully curated positive and negative concept example sets — the quality of the CAV direction is fundamentally limited by the quality and representativeness of the concept examples used to train it; noisy or unrepresentative concept examples produce CAV directions that conflate the target concept with correlated features in the example set rather than isolating the pure concept, and the resulting TCAV scores reflect sensitivity to the specific example distribution rather than the abstract concept; systematic concept set curation with diverse positive examples and carefully matched negative examples is required for reliable CAV directions.

## Logit Lens Technique

- secondary_domains: [large-language-models, mechanistic-interpretability, transformer-architecture]
- aliases: [logit lens analysis, intermediate layer token prediction, layer-wise token projection]
- broader: [mechanistic-interpretability, transformer-architecture, large-language-models]
- related: [causal-tracing-in-transformers, knowledge-localization-in-ffn, linear-representation-hypothesis, probing-classifiers]
- prerequisites: [transformer-architecture, layer-norms, unembedding, mechanistic-interpretability]
- confidence: high

**definition**: The Logit Lens Technique refers to the interpretability method of applying the language model's final unembedding matrix (the matrix that converts hidden states to vocabulary logits) to the intermediate hidden states at each transformer layer, producing a vocabulary probability distribution that reveals what token the residual stream "predicts" at each layer of the forward pass. The logit lens provides a running interpretation of how the model's prediction evolves through the layers — early layers typically produce random or uninformative distributions, middle layers show the prediction emerging, and later layers progressively refine the final prediction. This technique treats the residual stream as a sequence of evolving token predictions that can be inspected at each layer using the final unembedding as a consistent decoding probe.

**key_claim**: The Logit Lens Technique reveals that LLM computation is organised as incremental refinement of a consistent prediction representation — logit lens analysis across diverse tasks consistently shows that the model's final answer prediction is partially established in middle layers and refined (but not fundamentally restructured) in later layers, with factual recall predictions emerging in specific layers that localise knowledge retrieval; this incremental refinement pattern supports the residual stream interpretation of transformer computation as iterative information accumulation rather than layer-by-layer feature transformation, with important implications for mechanistic interpretability theories.

**warning**: The Logit Lens Technique has significant limitations for deep or architecturally complex models — the technique assumes that the unembedding matrix provides a meaningful decoding of intermediate layer representations, which holds approximately for final layers but may not hold for early layers where the residual stream representation has not yet been processed into a form interpretable by the final unembedding; additionally, attention layer outputs and MLP layer outputs contribute differently to the residual stream in ways that the logit lens aggregates without distinguishing, potentially obscuring the distinct computational roles of attention and MLP sub-layers.

## Causal Tracing in Transformers

- secondary_domains: [large-language-models, mechanistic-interpretability, causal-inference]
- aliases: [causal mediation analysis in LLMs, activation patching for causal tracing, causal scrubbing]
- broader: [mechanistic-interpretability, causal-inference, large-language-models]
- related: [knowledge-localization-in-ffn, factual-association-mechanisms, path-patching-methodology, attention-knockout-analysis]
- prerequisites: [causal-inference, transformer-architecture, mechanistic-interpretability, large-language-models]
- confidence: high

**definition**: Causal Tracing in Transformers refers to the mechanistic interpretability methodology that uses causal intervention experiments (specifically activation patching — replacing specific model activations with those from a counterfactual forward pass) to identify which components of a transformer network are causally responsible for specific model behaviours. Causal tracing, as introduced in the ROME paper (Meng et al. 2022), involves three steps: (1) recording activations for a clean prompt that produces the target behaviour, (2) running a corrupted forward pass that disrupts the target behaviour by corrupting the subject token representations, and (3) restoring specific activations from the clean run to the corrupted run one component at a time to identify which restorations recover the target behaviour. Components whose restoration recovers the behaviour are identified as causally important.

**key_claim**: Causal Tracing in Transformers identifies specific layers and module types as causally dominant for different computational functions — causal tracing studies of factual recall in GPT-style models consistently identify a small number of middle-layer MLP modules at the subject token positions as the primary locus of factual association recall, while attention heads in late layers are causally dominant for information routing to the output position; this double-dissociation (MLPs for storage, attention for routing) provides strong mechanistic evidence for a functional modularity hypothesis that early mechanistic interpretability work proposed based on structural analysis alone.

**warning**: Causal Tracing in Transformers with activation patching is sensitive to the patch location and patching methodology — patch effects are not always well-localised (patching one component can indirectly affect others due to residual stream dependencies), and what appears to be a causally central component may actually be a conduit for information that originates elsewhere in the network; causal tracing results should be validated across multiple corruptions, multiple patching granularities, and complementary methods (attention knockout, path patching) before mechanistic conclusions about component function are drawn.

## Knowledge Localization in FFN

- secondary_domains: [large-language-models, mechanistic-interpretability, transformer-architecture, factual-knowledge]
- aliases: [factual knowledge in MLP layers, FFN as knowledge store, transformer MLP knowledge localisation]
- broader: [mechanistic-interpretability, transformer-architecture, large-language-models]
- related: [causal-tracing-in-transformers, factual-association-mechanisms, logit-lens-technique, knowledge-editing-in-llms]
- prerequisites: [transformer-architecture, feed-forward-networks, causal-tracing, mechanistic-interpretability]
- confidence: high

**definition**: Knowledge Localization in FFN refers to the empirical finding and associated interpretability research that factual associations (e.g., "the Eiffel Tower is in Paris") are disproportionately stored and retrieved from specific middle-layer feed-forward network (FFN/MLP) modules in transformer language models, and that these specific modules function as key-value memories where keys correspond to subject features and values bias the residual stream toward factual predictions. The knowledge localisation hypothesis, supported by causal tracing studies, ROME, and MEMIT experiments, identifies specific neuron groups in FFN layers whose activation corresponds to specific factual associations and whose modification enables targeted factual knowledge editing without disrupting unrelated model behaviours.

**key_claim**: Knowledge Localization in FFN layers is sufficiently precise to enable targeted knowledge editing — ROME and MEMIT experiments that modify specific identified MLP layer weight parameters can update factual associations (e.g., changing "the Eiffel Tower is in Paris" to "the Eiffel Tower is in Rome") with high success rates while preserving unrelated factual knowledge and general model capabilities at rates substantially better than gradient-based fine-tuning, which modifies weights diffusely and causes greater collateral disruption; this precision supports the knowledge localisation hypothesis and demonstrates that FFN weight modifications at specific layers can function as targeted factual knowledge updates.

**warning**: Knowledge Localization in FFN should not be interpreted as evidence that factual knowledge is cleanly partitioned into discrete, independently modifiable modules — causal tracing identifies layers with the highest causal influence on factual recall, but factual knowledge representations are distributed across multiple layers and the identification of "primary" knowledge layers reflects the highest-influence layer in a distributed system rather than exclusive storage; knowledge editing via FFN modification succeeds for isolated factual updates but degrades for complex multi-hop reasoning that depends on the interactions between multiple distributed knowledge representations.

## Factual Association Mechanisms

- secondary_domains: [large-language-models, mechanistic-interpretability, transformer-architecture, knowledge-representation]
- aliases: [factual recall mechanisms in LLMs, how LLMs store facts, transformer fact retrieval]
- broader: [mechanistic-interpretability, knowledge-localization-in-ffn, large-language-models]
- related: [knowledge-localization-in-ffn, causal-tracing-in-transformers, logit-lens-technique, distributed-representations-in-transformers]
- prerequisites: [transformer-architecture, mechanistic-interpretability, factual-knowledge-in-llms]
- confidence: high

**definition**: Factual Association Mechanisms refer to the mechanistic components and computational pathways through which transformer language models store, index, and retrieve factual associations — the "how" of factual knowledge in LLMs at the level of specific attention heads, MLP layers, residual stream operations, and computational circuits. Factual association mechanisms research uses causal tracing, probing, attention pattern analysis, and circuit analysis to map the complete computational pathway from a factual query (e.g., "The Eiffel Tower is located in...") to the correct factual completion, identifying the specific subject token processing at MLP layers, the late-position information routing via attention heads, and the residual stream accumulation that combines these contributions into a vocabulary prediction.

**key_claim**: Factual Association Mechanisms in transformer LLMs follow a consistent two-stage retrieval pattern — the subject token positions at specific middle-layer MLP modules enrich the subject representation with attribute information (what properties the subject has), and late-layer attention heads at the final token position retrieve and route this subject-specific information to produce the factual completion; this two-stage subject-enrichment / final-position-routing pattern has been replicated across diverse factual tasks and multiple LLM architectures, providing a mechanistic basis for the knowledge localisation and knowledge editing literature.

**warning**: Factual Association Mechanisms research has been conducted primarily on factual recall in single-hop, context-free settings (completing "The Eiffel Tower is in ___") and may not generalise to multi-hop factual reasoning, contextually-modified factual claims, or counterfactual reasoning tasks — these tasks may involve substantially different computational circuits that the factual association mechanism research does not capture; extrapolating factual mechanism findings to interpretability conclusions about complex factual reasoning requires independent mechanistic analysis of those more complex tasks rather than assuming the same mechanisms apply.

## Attention Knockout Analysis

- secondary_domains: [large-language-models, mechanistic-interpretability, transformer-architecture]
- aliases: [attention head ablation, attention pattern knockout, causal head identification]
- broader: [mechanistic-interpretability, causal-tracing-in-transformers, transformer-architecture]
- related: [causal-tracing-in-transformers, path-patching-methodology, attention-visualization, factual-association-mechanisms]
- prerequisites: [transformer-architecture, attention-mechanism, mechanistic-interpretability]
- confidence: high

**definition**: Attention Knockout Analysis refers to the mechanistic interpretability technique of systematically zeroing out or replacing specific attention patterns — either entire attention heads, specific attention edges (connections between specific query and key positions), or specific head outputs — and measuring the effect on model performance to identify which attention heads are causally important for specific tasks or behaviours. Unlike attention visualisation (passive observation of attention weights), attention knockout is an active causal intervention that establishes causal necessity — if removing an attention head or specific attention edge degrades performance on a specific task, that head or edge is causally necessary for that task. Attention knockout is used to identify task-relevant attention heads, validate attention-based circuit hypotheses, and study how head ablation affects the information routing properties of the model.

**key_claim**: Attention Knockout Analysis identifies a small fraction of attention heads as causally important for any given task — systematic knockout studies consistently find that most attention heads can be ablated with minimal impact on specific task performance, while 2–10% of heads account for 50–80% of the head-ablatable performance gap for typical classification and retrieval tasks; this sparse causal head distribution supports the modular function hypothesis (specific heads implement specific functions) and motivates head-level pruning as a model compression strategy, as most heads are redundant or specialised for tasks not required by the target deployment.

**warning**: Attention Knockout Analysis results are task-specific and cannot be generalised across tasks — an attention head that is not causally important for one task (and therefore appears ablatable) may be critically important for a different task, and pruning based on single-task knockout analysis produces models that fail on tasks whose critical heads were incorrectly identified as non-essential; multi-task knockout analysis is required before using knockout results to motivate model compression decisions, and knockout analysis should cover the full distribution of tasks the model will be expected to perform.

## Path Patching Methodology

- secondary_domains: [large-language-models, mechanistic-interpretability, causal-inference]
- aliases: [path-level causal tracing, computational pathway analysis, causal circuit tracing]
- broader: [mechanistic-interpretability, causal-tracing-in-transformers, large-language-models]
- related: [causal-tracing-in-transformers, attention-knockout-analysis, factual-association-mechanisms, distributed-representations-in-transformers]
- prerequisites: [causal-tracing, transformer-architecture, mechanistic-interpretability, causal-inference]
- confidence: high

**definition**: Path Patching Methodology refers to the refined causal intervention technique that enables decomposing the causal influence of specific components on model outputs along defined computational pathways — identifying not just which components are causally important but how information flows between causally important components to produce the target behaviour. Path patching extends activation patching by specifying not only the source and destination of the patched activation but also the intermediate components whose activations are held clean or corrupted, enabling researchers to distinguish direct pathways (component A directly influences the output) from indirect pathways (component A influences the output through component B's processing). Path patching enables circuit-level mechanistic analysis that identifies the complete computational subgraph responsible for specific model behaviours.

**key_claim**: Path Patching Methodology enables discovery of interpretable circuits that implement specific model capabilities — path patching studies of induction heads, indirect object identification (IOI), and factual recall have identified compact computational circuits (typically 5–20 components in specific interaction configurations) that implement these capabilities through identifiable computational steps analogous to structured algorithmic procedures, providing the strongest available mechanistic evidence that LLMs implement some capabilities through structured, interpretable algorithms rather than through uninterpretable distributed computation across all model components.

**warning**: Path Patching Methodology is computationally expensive for large models and may identify circuits that are correct under the experimental conditions used for analysis but do not generalise to the full task distribution — path patching experiments necessarily use specific prompt formats and specific task instances to define the clean and corrupted activations, and circuits identified for these specific instances may not capture all the mechanisms the model uses for the same task under different prompt conditions; circuit generalisation testing across diverse prompt formats and edge cases is required before claiming that a path-patching-identified circuit constitutes a complete mechanistic account of a model capability.

## Distributed Representations in Transformers

- secondary_domains: [large-language-models, mechanistic-interpretability, representation-learning, neural-networks]
- aliases: [superposition in neural networks, distributed feature encoding, holographic memory in LLMs]
- broader: [mechanistic-interpretability, representation-learning, transformer-architecture]
- related: [polysemanticity-in-neural-networks, linear-representation-hypothesis, probing-classifiers, concept-activation-vectors]
- prerequisites: [representation-learning, neural-network-theory, mechanistic-interpretability]
- confidence: high

**definition**: Distributed Representations in Transformers refer to the encoding of information in the activation spaces of transformer models where individual concepts, features, and facts are not represented by single dedicated neurons but are spread across many neurons, and each neuron participates in representing many different concepts — contrasting with local symbolic representations where each concept has a unique dedicated neuron. Distributed representation in transformers is motivated by the superposition hypothesis (Ely et al., Anthropic), which proposes that transformers represent more features than they have neurons by encoding features as nearly-orthogonal directions in a high-dimensional space, allowing exponentially many features to coexist through superposition at the cost of interference between features. This distributed encoding underlies both the robustness of neural representations (damage to individual neurons is non-catastrophic) and the difficulty of mechanistic interpretability (individual neurons are polysemantic and not directly interpretable).

**key_claim**: Distributed Representations in Transformers via superposition enable LLMs to encode many more features than they have neurons — theoretical analysis and empirical experiments (toy model studies, sparse auto-encoder analyses) demonstrate that a model with n hidden dimensions can represent approximately exponentially more than n features using superposition, at the cost of interference between co-active features; this compression capacity explains how billion-parameter models encode the vast factual, linguistic, and conceptual knowledge needed for broad capabilities, and why neuron-level interpretability approaches that treat each neuron as a discrete feature fail to account for the model's representational capacity.

**warning**: Distributed Representations in Transformers make neuron-level interpretability analysis inherently incomplete — because features are distributed across neurons via superposition, analysing individual neuron activations provides an aliased view of the underlying features rather than a faithful account of what the model is computing; interpretability methods that assume local feature representation (e.g., max-activating input analysis for individual neurons) systematically misrepresent the model's computational structure, and mechanistic interpretability requires methods that can identify distributed features (sparse auto-encoders, concept activation vectors, representation engineering) to reveal the true computational structure.

## Polysemanticity in Neural Networks

- secondary_domains: [large-language-models, mechanistic-interpretability, representation-learning, neural-networks]
- aliases: [polysemantic neurons, multi-feature neurons, superposition and polysemanticity]
- broader: [mechanistic-interpretability, distributed-representations-in-transformers, large-language-models]
- related: [distributed-representations-in-transformers, linear-representation-hypothesis, probing-classifiers, representation-engineering]
- prerequisites: [neural-network-theory, mechanistic-interpretability, representation-learning]
- confidence: high

**definition**: Polysemanticity in Neural Networks refers to the phenomenon where individual neurons in a neural network (including transformer LLMs) respond to multiple, semantically unrelated input features — responding maximally to a diverse set of stimuli that do not correspond to a single interpretable concept. Polysemanticity is theorised to arise from superposition, where the network uses distributed representations to encode more features than it has neurons, inevitably making each neuron participate in representing multiple features to achieve the necessary representational capacity. Polysemanticity is a central challenge for mechanistic interpretability because it means that neuron-level analysis (examining what each neuron responds to) does not directly reveal the underlying feature structure of the model's representations, requiring methods that can decompose polysemantic neurons into their constituent features.

**key_claim**: Polysemanticity in Neural Networks is an expected consequence of superposition rather than a training failure — theoretical models of superposition predict that when the number of features to be represented exceeds the number of neurons, each neuron will respond to multiple features as a necessary result of the compressed representation, and that the degree of polysemanticity increases with the feature-to-neuron ratio and decreases with feature sparsity; empirical observations of polysemanticity in LLMs are therefore not signs of poor training but of high representational efficiency, and attempts to reduce polysemanticity through training modifications that force monosemanticity impose representational capacity costs.

**warning**: Polysemanticity in Neural Networks creates fundamental challenges for neuron-level steering and editing interventions — attempts to modify model behaviour by targeting specific neurons will simultaneously affect all features represented by that neuron, producing unintended collateral effects on model behaviour that are difficult to predict without a complete map of the neuron's polysemantic feature representation; mechanistic interventions targeting polysemantic neurons require methods that can isolate the specific feature direction of interest within the neuron's distributed representation space (e.g., through sparse auto-encoder decomposition) rather than operating at the coarse neuron level.
