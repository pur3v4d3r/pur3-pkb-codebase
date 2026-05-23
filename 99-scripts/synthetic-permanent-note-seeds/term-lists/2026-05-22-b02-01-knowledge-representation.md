---
batch_name: b02-01-knowledge-representation
batch_date: 2026-05-22
default_domain: knowledge-representation
default_confidence: high
notes: |
  Fifteen concepts covering how language models represent, ground, and reason
  about world knowledge. Spans semantic grounding, world models, commonsense
  knowledge, ontology, knowledge graphs, and the core reasoning modes
  (temporal, spatial, causal, counterfactual, abductive, deductive,
  inductive, analogical). Batch 02 of the prompt-engineering and LLM series.
---

# Batch: B02-01 Knowledge Representation and Grounding

## Semantic Grounding in LLMs

- secondary_domains: [natural-language-processing, cognitive-science, large-language-models]
- aliases: [grounding in language models, semantic anchoring, symbol grounding in LLMs]
- broader: [knowledge-representation, large-language-models]
- narrower: [entity-linking-in-prompts, coreference-resolution-prompting]
- related: [world-model-in-language-models, commonsense-reasoning-in-llms, ontology-grounded-prompting, symbol-grounding-problem]
- prerequisites: [large-language-models, word-embeddings, distributional-semantics]
- confidence: high

**definition**: Semantic grounding in LLMs refers to the degree to which a language model's internal representations connect linguistic symbols to stable, consistent meanings rather than treating them as purely statistical co-occurrence patterns. A grounded model reliably maps the token sequence "Paris is the capital of France" to a world-fact that constrains downstream inference, rather than merely recalling the phrase because it appeared frequently in training text. Grounding is achieved through a combination of large-scale pretraining on factual corpora, instruction tuning that rewards accurate world-knowledge retrieval, and supplementary mechanisms such as retrieval augmentation or knowledge-graph injection that supply explicit external anchors at inference time.

**key_claim**: The grounding question is not whether LLMs have grounded representations but how robust those representations are under distributional shift — models exhibit superficially grounded behaviour on in-distribution probes while failing on simple paraphrases or cross-lingual reformulations of the same fact, revealing that statistical co-occurrence and true semantic grounding produce indistinguishable behaviour in the large-data regime until the distribution shifts.

**warning**: Conflating fluent factual language generation with genuine semantic grounding is the central diagnostic error in LLM evaluation — a model that confidently generates accurate-sounding text about an entity may have no stable internal representation of that entity's properties, as revealed by inconsistent answers across paraphrased queries; grounding must be tested with adversarial reformulations, not just canonical phrasings.

## World Model in Language Models

- secondary_domains: [cognitive-science, large-language-models, artificial-intelligence]
- aliases: [LLM world model, internal world representation, implicit world knowledge in LLMs]
- broader: [knowledge-representation, large-language-models]
- narrower: [semantic-grounding-in-llms, commonsense-reasoning-in-llms]
- related: [causal-reasoning-in-llms, temporal-reasoning-in-llms, spatial-reasoning-in-llms, model-capability-vs-alignment-gap]
- prerequisites: [large-language-models, transformer-architecture, cognitive-science]
- confidence: high

**definition**: A world model in language models refers to the implicit structured representation of entities, properties, and relations that emerges in the model's parameters as a by-product of predicting text at scale. Unlike an explicit knowledge base or simulation engine, an LLM world model is distributed across billions of parameters and is accessed stochastically through the forward pass rather than through deterministic query. Evidence for world model-like representations comes from experiments showing that models can track entity state through narratives, predict physical simulation outcomes, and answer counterfactual questions in ways that require integrating multiple world facts coherently — capabilities that exceed what pure pattern-matching over surface form would predict.

**key_claim**: Probing studies and activation-patching experiments demonstrate that transformer models do develop linear representations of world-state variables — including position, time, colour, and categorical attributes — that are causally upstream of downstream token predictions, providing the strongest current evidence that LLMs build functional world models, even if those models are incomplete, inconsistently accessed, and not explicitly represented in any interpretable data structure.

**warning**: Attributing a rich world model to LLMs based on impressive benchmark performance risks anthropomorphising statistical patterns; models can achieve high scores on world-state tracking tasks via superficial cues (narrative template matching, frequency-based priors) without encoding the causal structure of the underlying world, and the degree of genuine world modelling must be assessed with adversarially controlled stimuli that eliminate surface-form shortcuts.

## Commonsense Reasoning in LLMs

- secondary_domains: [natural-language-processing, cognitive-science, large-language-models]
- aliases: [common sense in LLMs, commonsense knowledge reasoning, everyday reasoning in LLMs]
- broader: [reasoning-in-llms, knowledge-representation]
- narrower: [causal-reasoning-in-llms, temporal-reasoning-in-llms, spatial-reasoning-in-llms]
- related: [world-model-in-language-models, analogical-transfer-in-llms, chain-of-thought-prompting]
- prerequisites: [large-language-models, commonsense-knowledge-bases]
- confidence: high

**definition**: Commonsense reasoning in LLMs is the capacity to draw inferences about everyday physical, social, and causal situations that are so obvious to humans that they are rarely stated explicitly in text. Tasks requiring commonsense include inferring that a dropped object falls, that a person with a headache probably wants quiet, or that using a knife to cut butter is plausible while using a knife to cut air is not. LLMs acquire commonsense knowledge implicitly from large corpora that implicitly encode such facts through typical event descriptions, narrative arcs, and conversational exchanges, but the coverage is uneven because authors omit information assumed to be universally known, creating systematic gaps in what the model infers.

**key_claim**: The primary bottleneck for commonsense reasoning in LLMs is not factual coverage but implicit assumption elicitation — the model's commonsense knowledge is present in its parameters but is often not activated unless the prompt explicitly calls for commonsense inference, meaning that the same model will succeed on a task framed as "apply common sense" and fail on a semantically equivalent task framed as a factual question.

**warning**: Benchmark saturation on commonsense datasets like HellaSwag and WinoGrande does not imply general commonsense competence — models achieve high scores through a combination of pattern matching on dataset-specific artefacts and statistical regularities in narrative structure rather than genuine physical or social world knowledge, as demonstrated by dramatic performance drops when surface-form cues are controlled.

## Ontology-Grounded Prompting

- secondary_domains: [knowledge-engineering, prompt-engineering, natural-language-processing]
- aliases: [ontology-anchored prompting, knowledge-ontology prompting, OWL-grounded prompting]
- broader: [knowledge-graph-augmented-generation, prompt-engineering]
- narrower: [entity-linking-in-prompts]
- related: [knowledge-graph-augmented-generation, semantic-grounding-in-llms, structured-output-prompting]
- prerequisites: [prompt-engineering, ontology, knowledge-representation]
- confidence: high

**definition**: Ontology-grounded prompting is a prompting strategy in which formal ontological structures — class hierarchies, property definitions, axioms, and inter-concept relations drawn from OWL, RDF, or domain-specific schema — are injected into the prompt context to constrain and guide the LLM's generation. By making the ontological framework explicit, the prompt signals the expected semantic categories, valid entity types, and permissible relations, dramatically reducing the rate of type errors, category confusion, and hallucinated entities in structured-output tasks. The technique is particularly effective in biomedical, legal, and engineering domains where precision is non-negotiable and the ontology is authoritative.

**key_claim**: Ontology-grounded prompting reduces LLM hallucination in structured-generation tasks by converting an open-ended generation problem into a constrained classification-and-relation-filling problem, with empirical gains in entity-type consistency and relation validity that far exceed what few-shot examples alone achieve because the ontological schema acts as a formal type system that the model can reference throughout the generation process.

**warning**: Injecting large ontologies into context windows wastes token budget on schema detail that the model may not need; effective ontology-grounded prompting requires selective schema extraction — including only the classes, properties, and axioms relevant to the current subtask — because context window saturation with ontological overhead can degrade generation quality relative to a focused few-shot approach without the schema.

## Knowledge Graph Augmented Generation

- secondary_domains: [retrieval-augmented-generation, natural-language-processing, knowledge-representation]
- aliases: [KGAG, knowledge-graph RAG, graph-augmented generation, KG-RAG]
- broader: [retrieval-augmented-generation, knowledge-representation]
- narrower: [ontology-grounded-prompting, entity-linking-in-prompts]
- related: [dense-retrieval-for-rag, knowledge-conflict-in-rag, entity-linking-in-prompts, semantic-grounding-in-llms]
- prerequisites: [retrieval-augmented-generation, knowledge-graphs, large-language-models]
- confidence: high

**definition**: Knowledge Graph Augmented Generation (KGAG) is a retrieval-augmented generation architecture in which a structured knowledge graph — rather than or in addition to an unstructured text corpus — serves as the external knowledge source. At query time, the system traverses the KG to extract relevant entity-relation-entity triples or subgraphs, linearises them into natural-language fragments, and injects those fragments alongside the user query into the LLM's prompt. The graph structure enables multi-hop reasoning paths that are difficult to surface through dense vector retrieval over text chunks, because the graph explicitly encodes relational chains that would otherwise need to be inferred through multiple text retrievals.

**key_claim**: KGAG outperforms text-only RAG on multi-hop factual queries because the graph structure explicitly encodes multi-hop relational paths that the retrieval step can traverse deterministically, whereas text-based RAG must recover those paths through multiple independent retrievals whose errors compound multiplicatively; the structured graph also provides a natural mechanism for provenance tracking, enabling exact citation of the triples that support each claim in the generated output.

**warning**: Knowledge graph augmented generation inherits all the staleness and coverage limitations of the underlying KG — entities and relations not represented in the graph are invisible to the system regardless of their presence in connected text corpora, and the KG's schema choices impose a categorical structure on the world that may not match the query's requirements; KGAG systems must include a fallback to text-based retrieval for out-of-KG queries to avoid confident ignorance.

## Entity Linking in Prompts

- secondary_domains: [information-extraction, natural-language-processing, prompt-engineering]
- aliases: [named entity disambiguation in prompts, entity resolution prompting, mention linking]
- broader: [knowledge-graph-augmented-generation, prompt-engineering]
- related: [coreference-resolution-prompting, ontology-grounded-prompting, semantic-grounding-in-llms]
- prerequisites: [named-entity-recognition, entity-linking, prompt-engineering]
- confidence: high

**definition**: Entity linking in prompts refers to the practice of explicitly resolving ambiguous entity mentions in a prompt — or requiring the LLM to perform such resolution as part of its task — by mapping each mention to a canonical identifier in a knowledge base such as Wikidata, Freebase, or a domain ontology. When the prompt consumer is a structured-output system (e.g., a knowledge graph population pipeline), entity linking ensures that all extracted entities refer to the same canonical node rather than generating surface-form variations that break downstream aggregation. As a prompting technique, it involves instructing the model to identify entity mentions, resolve them to canonical IDs, and ground its reasoning on the canonical entity's known properties.

**key_claim**: Explicit entity linking in the prompt significantly improves the factual consistency of LLM outputs in knowledge-intensive tasks because it eliminates surface-form ambiguity — a model that has resolved "the President" to a specific canonical entity with known properties will generate factually consistent claims about that entity across a multi-sentence response, whereas an unlinked model may switch referents mid-response based on contextual salience shifts.

**warning**: Entity linking in prompts can introduce errors of over-specification: forcing the model to commit to a canonical entity ID early in the response may cause it to generate factually correct statements about the canonical entity that are irrelevant or incorrect for the specific sense the user intended, particularly for polysemous entity mentions where the correct referent is context-dependent and not recoverable from the entity name alone.

## Coreference Resolution Prompting

- secondary_domains: [natural-language-processing, discourse-analysis, prompt-engineering]
- aliases: [anaphora resolution prompting, co-reference resolution in LLMs, pronoun disambiguation prompting]
- broader: [prompt-engineering, natural-language-processing]
- related: [entity-linking-in-prompts, semantic-grounding-in-llms, dialogue-state-tracking-prompts]
- prerequisites: [coreference-resolution, natural-language-processing, prompt-engineering]
- confidence: high

**definition**: Coreference resolution prompting is the prompting technique of instructing a language model to identify and resolve co-referential mentions — pronouns, definite descriptions, demonstratives, and zero anaphora — within a text, attributing each mention to its correct antecedent entity or event. In the context of structured information extraction and question answering, coreference resolution is a prerequisite for correct fact attribution: a model that fails to resolve "he" to the correct antecedent in a multi-sentence passage will make incorrect attributions about entity properties. The prompting strategy can either request the model to perform coreference resolution as an explicit reasoning step before answering or use chain-of-thought formatting to surface the resolution decisions for verification.

**key_claim**: Coreference resolution prompting as an explicit intermediate step in information extraction pipelines reduces attribution errors in multi-entity passages by approximately the same margin as adding dedicated coreference resolver pre-processing, because instruction-tuned LLMs can perform reliable coreference resolution when explicitly asked, but consistently fail to do so implicitly when the resolution is a prerequisite for a downstream task rather than the primary task.

**warning**: LLM-based coreference resolution degrades sharply for distant anaphora — mentions separated by many intervening sentences or complex syntactic structures — and for zero anaphora in pro-drop languages; prompting strategies that assume robust LLM coreference ability will generate subtly incorrect fact attributions in long-document processing pipelines without any surface-level signal of failure.

## Temporal Reasoning in LLMs

- secondary_domains: [natural-language-processing, commonsense-reasoning, large-language-models]
- aliases: [temporal inference in LLMs, time reasoning in language models, event ordering in LLMs]
- broader: [commonsense-reasoning-in-llms, reasoning-in-llms]
- related: [causal-reasoning-in-llms, spatial-reasoning-in-llms, world-model-in-language-models]
- prerequisites: [large-language-models, temporal-expression-extraction, event-ordering]
- confidence: high

**definition**: Temporal reasoning in LLMs is the capacity to represent, manipulate, and draw inferences about time — including event ordering (before/after/during), duration estimation, temporal expression normalisation, relative and absolute date arithmetic, and reasoning about how entity states change over time. Tasks range from simple ordering (did event A occur before event B?) to complex temporal chains (given a series of dated events, what was the state of entity X at time T?) to counterfactual temporal reasoning (if event A had not occurred in year Y, what would the state be now?). LLMs acquire temporal reasoning capability through exposure to news articles, histories, and narratives that encode temporal structure, but performance degrades with increasing temporal chain length and with cross-document temporal integration.

**key_claim**: LLMs exhibit a systematic asymmetry in temporal reasoning: they perform well on forward temporal chains (reasoning from past events to present consequences) but poorly on backward temporal chains (reasoning from present state to required past conditions), because training corpora predominantly represent the forward temporal direction of narrative, leaving backward-inference patterns systematically underrepresented.

**warning**: LLM temporal reasoning is entangled with training data cutoff effects — models frequently report stale facts as current with full confidence because their internal temporal representation does not distinguish between "X was true in training data" and "X is currently true," making temporal reasoning about recent events and dynamic world-states unreliable without explicit retrieval augmentation with dated sources.

## Spatial Reasoning in LLMs

- secondary_domains: [cognitive-science, natural-language-processing, large-language-models]
- aliases: [spatial inference in LLMs, geometric reasoning in language models, spatial cognition in LLMs]
- broader: [commonsense-reasoning-in-llms, reasoning-in-llms]
- related: [temporal-reasoning-in-llms, causal-reasoning-in-llms, world-model-in-language-models]
- prerequisites: [large-language-models, commonsense-reasoning, cognitive-science]
- confidence: high

**definition**: Spatial reasoning in LLMs refers to the ability to represent and reason about the positions, orientations, distances, and spatial relations between objects — including topological relations (inside, adjacent, connected), directional relations (north of, left of, above), metric relations (three metres away), and mental rotation tasks. LLMs acquire spatial knowledge from spatial descriptions in text but lack the grounded sensorimotor experience that anchors human spatial cognition to body and environment. The resulting spatial representations are text-statistical rather than simulation-based, producing brittle performance that is highly sensitive to how spatial relations are linguistically encoded.

**key_claim**: LLM spatial reasoning performance is a function of linguistic familiarity with the spatial description format, not genuine geometric inference — the same spatial problem expressed in canonical route-description format is solved reliably, while an equivalent problem expressed in coordinate-based or survey-description format is solved poorly, confirming that LLMs navigate text descriptions of space rather than computing over any internal geometric representation.

**warning**: Prompting LLMs for spatial reasoning on novel or large-scale geometric configurations (multi-room layouts, city-scale navigation, multi-object stacking) produces fluent but geometrically inconsistent outputs that satisfy local linguistic constraints while violating global spatial coherence; engineers relying on LLM spatial reasoning for safety-critical applications such as robotics path planning or architectural layout should treat LLM outputs as rough drafts requiring formal verification.

## Causal Reasoning in LLMs

- secondary_domains: [causality, cognitive-science, large-language-models]
- aliases: [causal inference in LLMs, cause-and-effect reasoning in language models, causal understanding in LLMs]
- broader: [reasoning-in-llms, commonsense-reasoning-in-llms]
- narrower: [counterfactual-reasoning-prompting]
- related: [temporal-reasoning-in-llms, abductive-reasoning-in-llms, chain-of-thought-prompting, world-model-in-language-models]
- prerequisites: [large-language-models, causal-inference, counterfactual-reasoning]
- confidence: high

**definition**: Causal reasoning in LLMs is the capacity to identify, represent, and draw inferences from causal relations — distinguishing causes from effects, inferring likely causes from observed effects, predicting the consequences of interventions, and reasoning about counterfactual states that would hold if a cause had been different. True causal reasoning requires more than correlation-pattern matching: it requires a structural causal model in which intervention on one variable changes others only along directed causal edges, not through the statistical correlations that exist in the training distribution. LLMs approximate causal reasoning through pattern matching on causal language and narrative structure rather than through any explicit implementation of Pearl's do-calculus or a structural causal model.

**key_claim**: LLMs systematically confuse correlation with causation in tasks that require distinguishing the two — they achieve high accuracy on causal question-answering tasks where causal direction is recoverable from surface-form linguistic cues (e.g., "caused," "led to," "because") but fail at tasks requiring intervention reasoning (e.g., "if we forcibly set X to zero, what happens to Y?") where correct answers require reasoning about the causal graph rather than linguistic patterns in the training data.

**warning**: Chain-of-thought prompting significantly improves LLM causal reasoning but does not eliminate the correlation-causation conflation; even when prompted to reason step-by-step, models may generate a plausible-sounding causal chain that follows textual conventions for causal narrative without respecting the independence assumptions required for valid causal inference, making CoT outputs confident but causally invalid reasoning that is difficult to identify without domain expertise.

## Counterfactual Reasoning Prompting

- secondary_domains: [causality, cognitive-science, prompt-engineering]
- aliases: [counterfactual inference prompting, what-if prompting, hypothetical scenario reasoning]
- broader: [causal-reasoning-in-llms, prompt-engineering]
- related: [causal-reasoning-in-llms, abductive-reasoning-in-llms, chain-of-thought-prompting]
- prerequisites: [causal-reasoning, prompt-engineering, large-language-models]
- confidence: high

**definition**: Counterfactual reasoning prompting is the prompting technique of asking a language model to reason about hypothetical scenarios in which some antecedent fact has been changed — "What would have happened if X had not occurred?" or "How would outcome Y differ if condition Z were altered?" — requiring the model to construct an alternative world consistent with the hypothetical change and derive its consequences. Counterfactual prompting is used in causal analysis, historical reasoning, diagnostic explanation, and evaluation of model causal understanding. Effective counterfactual prompts must clearly specify which facts are being changed, which are held constant, and what the relevant time horizon for consequences is.

**key_claim**: Counterfactual reasoning prompting reveals whether a model has causal knowledge versus correlational knowledge of a domain: a model with only correlational knowledge generates counterfactuals by interpolating the training distribution around the changed variable (producing near-minimal changes to the observed world), while a model with causal knowledge correctly propagates intervention effects along causal paths, including surprising downstream consequences that would not be predicted by correlation.

**warning**: Models exhibit a systematic "minimal counterfactual" bias — they tend to change as few things as possible when constructing a counterfactual world, which produces plausible-sounding but causally shallow responses that overlook second-order and distal consequences; counterfactual prompts must explicitly instruct the model to trace downstream effects across the full causal graph rather than accepting the first minimal-change alternative that satisfies the stated hypothetical.

## Abductive Reasoning in LLMs

- secondary_domains: [logic, cognitive-science, large-language-models]
- aliases: [inference to best explanation in LLMs, hypothesis generation in LLMs, abductive inference prompting]
- broader: [reasoning-in-llms, commonsense-reasoning-in-llms]
- related: [causal-reasoning-in-llms, deductive-reasoning-chains, inductive-reasoning-in-llms, counterfactual-reasoning-prompting]
- prerequisites: [large-language-models, logic, abductive-inference]
- confidence: high

**definition**: Abductive reasoning in LLMs is the capacity to infer the most plausible explanation for a set of observations — to generate hypotheses that best account for the evidence, rather than deducing conclusions from premises (deductive) or generalising from instances to rules (inductive). Formally known as "inference to the best explanation," abduction underlies diagnostic reasoning in medicine, fault diagnosis in engineering, and narrative comprehension in everyday cognition. LLMs perform abductive reasoning by generating candidate explanations and implicitly ranking them by prior probability and explanatory fit with the observations, a process that is heavily influenced by the frequency with which similar explanation-observation pairs appeared in training text.

**key_claim**: LLMs exhibit abductive reasoning biases that mirror cognitive biases in human explanation-generation: they prefer simple explanations over complex ones (parsimony bias), familiar explanation-types over novel ones (availability bias), and explanations that are locally consistent with the immediate observation over globally consistent ones that require integrating multiple evidence sources, producing abductive outputs that are plausible for typical cases but fail on atypical evidence combinations.

**warning**: Abductive reasoning in LLMs is particularly vulnerable to prior-dominated outputs: the model generates the most probable explanation given the training distribution rather than the explanation best supported by the specific evidence in the prompt, meaning that a rare-but-correct explanation for unusual evidence will be systematically suppressed in favour of the common explanation, requiring explicit prompt instructions to consider explanations of varying prior probability and evaluate them against the specific evidence.

## Deductive Reasoning Chains

- secondary_domains: [logic, mathematics, large-language-models]
- aliases: [deductive inference in LLMs, logical deduction prompting, syllogistic reasoning in LLMs]
- broader: [reasoning-in-llms]
- related: [inductive-reasoning-in-llms, abductive-reasoning-in-llms, chain-of-thought-prompting, causal-reasoning-in-llms]
- prerequisites: [large-language-models, formal-logic, deductive-inference]
- confidence: high

**definition**: Deductive reasoning chains in LLMs are sequences of inference steps in which conclusions are derived necessarily from given premises according to valid logical rules, producing outputs that are guaranteed to be true if the premises are true. In the prompting context, deductive reasoning chains are elicited through chain-of-thought formatting that asks the model to state the relevant premises, identify the applicable inference rule, and derive the conclusion step by step. LLMs can perform simple deductive syllogisms reliably but degrade on multi-step deductive chains, negation, embedded quantifiers, and premises that conflict with world knowledge (the model tends to accept plausible-sounding conclusions even when they do not follow deductively from the given premises).

**key_claim**: The primary failure mode of LLMs in deductive reasoning is belief bias — the tendency to accept valid arguments with believable conclusions and reject valid arguments with counterintuitive conclusions regardless of logical form, demonstrating that LLMs evaluate deductive conclusions by their posterior probability under the training distribution rather than by the validity of the inference from the stated premises, a conflation that makes chain-of-thought deductive reasoning unreliable for logical reasoning in novel or adversarial premise configurations.

**warning**: Long deductive chains in LLMs accumulate errors multiplicatively — each inference step has a non-zero error probability, and since later steps depend on earlier ones, a single error in an early step propagates to corrupt all downstream conclusions, making deductive chain reliability decrease geometrically with chain length; formal theorem provers, constraint solvers, or verification tools should be integrated as external validators for high-stakes deductive reasoning rather than relying on LLM self-consistency.

## Inductive Reasoning in LLMs

- secondary_domains: [epistemology, cognitive-science, large-language-models]
- aliases: [pattern generalisation in LLMs, inductive inference prompting, rule induction in LLMs]
- broader: [reasoning-in-llms]
- related: [deductive-reasoning-chains, abductive-reasoning-in-llms, few-shot-prompting, in-context-learning-as-meta-learning]
- prerequisites: [large-language-models, inductive-inference, epistemology]
- confidence: high

**definition**: Inductive reasoning in LLMs is the capacity to generalise from specific instances to general rules or patterns — to observe multiple examples sharing a common property and infer a rule that applies beyond the observed cases. In the prompting context, inductive reasoning is at the core of few-shot in-context learning: the model observes input-output pairs and induces a task rule that it applies to novel inputs. LLMs are extraordinarily capable at certain forms of induction (pattern recognition in structured sequences, linguistic rule inference from examples) but are biased by the frequency of rules in the training distribution and by the surface form of the examples provided.

**key_claim**: LLMs perform inductive reasoning primarily through instance-based retrieval of similar training examples rather than explicit rule induction — they infer the task rule by finding the most similar training patterns to the in-context examples and applying those patterns to the test input, which produces accurate generalisation when the task rule is common in training data and fails when the rule is novel or requires abstraction beyond surface-form similarity.

**warning**: The in-context generalisation produced by LLM inductive reasoning is sample-inefficient and format-sensitive in ways that genuine rule induction is not: changing the surface format of examples while preserving the underlying rule can completely disrupt induction, and adding examples that are individually consistent with two conflicting rules produces unstable generalisation that switches between the rules based on recency or frequency effects rather than reliably resolving to the correct rule.

## Analogical Transfer in LLMs

- secondary_domains: [cognitive-science, learning-theory, large-language-models]
- aliases: [analogical reasoning in LLMs, structure mapping in language models, analogical inference prompting]
- broader: [reasoning-in-llms, commonsense-reasoning-in-llms]
- related: [inductive-reasoning-in-llms, few-shot-emergent-generalization, chain-of-thought-prompting, semantic-grounding-in-llms]
- prerequisites: [large-language-models, analogical-reasoning, structure-mapping-theory]
- confidence: high

**definition**: Analogical transfer in LLMs is the capacity to recognise structural similarity between a source domain with a known solution and a target domain with an unknown problem, and to adapt the source solution to the target by mapping corresponding structural elements. A high-performing analogical system identifies that the deep relational structure of the two domains is isomorphic, not merely that surface features are similar, and generates a target solution that respects the structural constraints of the target domain. LLMs show impressive analogical ability on word-analogy tasks and explicit A:B::C:? formats but struggle with multi-relational structure mapping across complex scenarios where the relational mapping is not lexically cued.

**key_claim**: LLM analogical transfer is primarily driven by surface similarity and lexical overlap between source and target domains rather than by deep structural alignment — models achieve high performance on analogical reasoning benchmarks by exploiting co-occurrence patterns between analogical pairs in training data, but fail on novel analogies where the structural isomorphism must be discovered rather than recalled, confirming that LLM analogical ability is a form of sophisticated retrieval rather than the relational abstraction that characterises human analogical reasoning.

**warning**: Prompting LLMs with analogical instructions ("this problem is like X, solve it the same way") can introduce analogical interference — if the source analogy is imperfect, the model will import incorrect structural mappings from the source that corrupt the target solution; analogical prompting requires explicit verification that the structural mapping between source and target is valid for the specific aspect of the problem being transferred.
