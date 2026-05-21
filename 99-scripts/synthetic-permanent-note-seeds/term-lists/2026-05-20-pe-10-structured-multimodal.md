---
batch_name: pe-10-structured-multimodal
batch_date: 2026-05-20
default_domain: structured-generation
default_confidence: high
notes: |
  Sixteen concepts covering structured output generation and multimodal
  prompting. The structured output section covers the methods by which
  LLM outputs are constrained to machine-parseable formats (JSON mode,
  grammar-constrained decoding, function schemas, guided generation,
  constrained beam search, tool schema optimisation). The multimodal
  section covers prompting patterns specific to vision-language models
  (VL prompting, image captioning, visual CoT, multimodal few-shot,
  document understanding, chart and table reasoning, interleaved
  image-text, grounded visual reasoning). These two clusters represent
  distinct capability surfaces that are increasingly foundational for
  production AI applications.
---

# Batch: PE-10 Structured Output and Multimodal Prompting

## JSON Mode Prompting

- domain: structured-generation
- secondary_domains: [prompt-engineering, api-integration, llm-reliability]
- aliases: [JSON output prompting, structured JSON generation, JSON constrained generation]
- broader: [structured-prediction-prompting, output-schema-enforcement]
- narrower: []
- related: [output-schema-enforcement, grammar-constrained-decoding, function-schema-design, guided-generation, tool-schema-optimization]
- prerequisites: [prompt-engineering, api-integration, structured-prediction-prompting]
- confidence: high

**definition**: JSON Mode Prompting refers to the combination of prompting strategies and model API settings used to elicit well-formed JSON output from language models, enabling reliable programmatic parsing of model responses. Modern APIs (OpenAI, Anthropic, Google) offer a "JSON mode" or "response format" setting that constrains generation to valid JSON syntax; effective JSON mode prompting supplements this with explicit schema descriptions in the system prompt, worked examples of the target schema, and field-level documentation that guides the model on types, optionality, and enumerated values.

**key_claim**: Structured JSON output generation is the primary mechanism by which LLMs are integrated into software pipelines — the ability to produce machine-parseable responses transforms a language model from a text generator into a structured data processor, making reliable JSON generation a prerequisite for any production system that passes model outputs to downstream code.

**warning**: JSON mode constraints apply only at the syntactic level — the model can produce syntactically valid JSON that is semantically incorrect (wrong types for values, missing required fields, hallucinated keys, values that violate business rules), meaning that JSON mode is necessary but not sufficient for reliable structured output and must be supplemented with schema validation at the application layer.

## Grammar-Constrained Decoding

- domain: structured-generation
- secondary_domains: [llm-decoding, formal-languages, structured-prediction]
- aliases: [constrained generation, grammar-guided generation, GBNF generation, CFG-constrained decoding]
- broader: [guided-generation, constrained-beam-search]
- narrower: []
- related: [guided-generation, constrained-beam-search, json-mode-prompting, output-schema-enforcement, structured-prediction-prompting]
- prerequisites: [llm-decoding, formal-grammar, structured-prediction-prompting]
- confidence: high

**definition**: Grammar-Constrained Decoding is a generation technique in which the language model's token sampling is restricted at each step to only those tokens that can extend the current output while remaining consistent with a formal grammar — such as a context-free grammar (CFG), GBNF (GGUF BNF Format), or regular expression. By masking the logits of tokens that would violate the grammar, the method guarantees that every possible output satisfies the grammar by construction, making it possible to produce valid JSON, YAML, SQL, code, or any other formally defined structure with zero syntactic errors.

**key_claim**: Grammar-constrained decoding provides a hard guarantee of syntactic validity that prompt-based approaches cannot match — no matter how well-prompted a model is, it will occasionally produce malformed structured output on adversarial inputs or edge cases, while grammar constraints enforce structure at the generation level, making downstream parsing failure-free by construction.

**warning**: Grammar-constrained decoding can degrade output quality by forcing the model to commit to token choices that are syntactically valid but semantically poor — if the most likely semantically correct continuation is grammatically invalid under the current constraint state, the model is forced to choose a less likely but grammatically valid alternative, and this can compound into outputs that are syntactically correct but semantically incoherent for complex schemas.

## Function Schema Design

- domain: structured-generation
- secondary_domains: [prompt-engineering, api-integration, tool-use-llms]
- aliases: [tool schema design, function calling schema, OpenAI function schema]
- broader: [tool-use-llms, structured-prediction-prompting]
- narrower: []
- related: [json-mode-prompting, output-schema-enforcement, tool-use-llms, tool-schema-optimization, guided-generation]
- prerequisites: [tool-use-llms, json-schema, prompt-engineering]
- confidence: high

**definition**: Function Schema Design is the practice of authoring the JSON Schema descriptions of tools and functions that are exposed to a language model through a function-calling API, such that the model reliably selects the correct function for a given user request and generates the correct argument structure. A well-designed function schema includes a precise and unambiguous function name and description, parameter names and types that are self-documenting, enumerated values for constrained parameters, clear documentation of required vs. optional parameters, and examples in the description when the parameter semantics are non-obvious.

**key_claim**: Function schema quality is the primary determinant of function-calling reliability — a poorly described schema causes the model to select incorrect functions, generate wrong argument types, hallucinate unsupported parameter names, or fail to call a function when one is appropriate, all of which are failures that cannot be reliably compensated by general instruction prompting when the schema itself is ambiguous.

**warning**: Function schemas have an optimal specificity — over-specified schemas with too many functions or too many parameters cause the model to make incorrect selections from a long menu of options, while under-specified schemas cause ambiguity in argument generation; the practical design principle is to minimise the function surface area and keep parameter semantics orthogonal and self-documenting.

## Structured Prediction Prompting

- domain: structured-generation
- secondary_domains: [prompt-engineering, natural-language-processing, information-extraction]
- aliases: [structured output prompting, IE prompting, extraction prompting]
- broader: [prompt-engineering, structured-generation]
- narrower: [json-mode-prompting, function-schema-design]
- related: [json-mode-prompting, output-schema-enforcement, grammar-constrained-decoding, information-extraction-prompts]
- prerequisites: [prompt-engineering, structured-generation]
- confidence: high

**definition**: Structured Prediction Prompting encompasses the set of prompting strategies used to elicit structured, machine-parseable outputs from language models in the absence of or in addition to API-level structural constraints. Techniques include: providing output templates with placeholders, using delimiters to mark fields (e.g., XML tags, JSON keys), including annotated few-shot examples that demonstrate the exact output structure, instructing the model to think step-by-step before producing the final structured output, and adding explicit validation instructions (e.g., "verify your output conforms to the schema before finalising").

**key_claim**: Structured prediction prompting must work in concert with model-level structural constraints — prompting alone is unreliable for strict structural requirements because language models optimise for fluency rather than format compliance, but prompting provides the semantic guidance that structural constraints lack, making the combination of clear schema instructions and API-level format enforcement significantly more reliable than either alone.

**warning**: Including lengthy schema descriptions and many few-shot examples for structured prediction can push important task context earlier in the prompt out of effective attention range, creating a quality-reliability tradeoff where the prompt length needed for reliable structure may degrade the quality of the semantic content within that structure.

## Output Schema Enforcement

- domain: structured-generation
- secondary_domains: [api-integration, software-engineering, llm-reliability]
- aliases: [schema validation for LLMs, output validation, response schema enforcement]
- broader: [structured-generation, structured-prediction-prompting]
- narrower: []
- related: [json-mode-prompting, grammar-constrained-decoding, function-schema-design, guided-generation, pydantic-output-parsing]
- prerequisites: [json-schema, structured-generation, api-integration]
- confidence: high

**definition**: Output Schema Enforcement refers to the system-level mechanisms used to guarantee that language model outputs conform to a specified schema, combining model-level constraints (JSON mode, grammar-constrained decoding) with application-level validation (Pydantic models, JSON Schema validators, retry logic). A complete output schema enforcement pipeline typically involves: schema definition in a type-safe format, schema injection into the model prompt, API-level format constraints where available, post-generation schema validation, retry-with-error prompting when validation fails, and fallback handling for persistent validation failures.

**key_claim**: Robust output schema enforcement requires defence in depth — relying on any single mechanism (prompt instructions, JSON mode, or runtime validation alone) produces a system with an unacceptable failure rate in production, while layering multiple enforcement mechanisms reduces the failure rate multiplicatively, making schema enforcement architecturally similar to fault-tolerant system design.

**warning**: Retry-with-error prompting — showing the model its malformed output and asking it to fix the error — is effective for simple schema violations but can create failure loops for systematic schema misunderstandings, where the model repeatedly produces the same type of violation because it does not understand the schema constraint; these failures require updating the schema documentation or few-shot examples rather than more retries.

## Constrained Beam Search

- domain: structured-generation
- secondary_domains: [llm-decoding, natural-language-generation, structured-prediction]
- aliases: [lexically constrained beam search, constrained decoding, CBC]
- broader: [beam-search-decoding, guided-generation]
- narrower: []
- related: [beam-search-decoding, grammar-constrained-decoding, guided-generation, structured-prediction-prompting]
- prerequisites: [beam-search-decoding, llm-decoding]
- confidence: high

**definition**: Constrained Beam Search is a decoding algorithm that extends beam search by enforcing lexical or structural constraints on the generated sequence, ensuring that specified tokens, phrases, or structural patterns must appear or must not appear in the output. Hard constraints mandate the inclusion of specified tokens (positive constraints) or the exclusion of specified tokens (negative constraints), while soft constraints add a reward signal that encourages but does not mandate specific patterns. The algorithm maintains a beam of partial hypotheses and prunes any that have violated hard constraints or that can no longer satisfy them given the remaining positions.

**key_claim**: Constrained beam search provides a deterministic guarantee that specified content will appear in generated text — enabling applications where faithfulness to source materials or adherence to domain terminology is required (e.g., medical report generation, legal document drafting, machine translation with domain lexicons) — at the cost of potential reduction in output fluency when the constraints conflict with the model's learned generation probabilities.

**warning**: Constrained beam search becomes computationally expensive as the number and complexity of constraints increases — each additional hard constraint can multiply the number of beam states that must be maintained to track constraint satisfaction status, potentially making it slower than unconstrained beam search with a large beam by orders of magnitude for richly constrained generation tasks.

## Guided Generation

- domain: structured-generation
- secondary_domains: [llm-decoding, prompt-engineering, structured-prediction]
- aliases: [logit guidance, token-level generation control, outlines generation]
- broader: [structured-generation, llm-decoding]
- narrower: [grammar-constrained-decoding, constrained-beam-search]
- related: [grammar-constrained-decoding, constrained-beam-search, json-mode-prompting, output-schema-enforcement]
- prerequisites: [llm-decoding, structured-prediction-prompting]
- confidence: high

**definition**: Guided Generation is the broad class of techniques that shape a language model's output at the token-sampling level by modifying logit distributions before sampling, using structural information about the desired output format. This includes grammar-constrained decoding (logit masking based on formal grammar state), regex-guided generation (masking based on partial regex match), JSON schema guided generation (masking based on schema state machine), and custom logit processors that inject external signals into the sampling process. Libraries such as Outlines, Guidance, and LMQL expose these techniques as composable programming abstractions.

**key_claim**: Guided generation reframes language model prompting as a form of constrained programming — rather than hoping the model will follow format instructions probabilistically, guided generation uses the model's probability distribution for semantic content while using formal constraints for structural requirements, achieving the best of both: LLM creativity within hard structural guarantees.

**warning**: Guided generation is implemented at the inference level and is typically not compatible with API-only access to models — it requires either running the model locally (e.g., via vLLM, llama.cpp, or HuggingFace Transformers) or using a provider that exposes logit-level access, which currently excludes most commercial API endpoints and limits its practical applicability to self-hosted deployments.

## Tool Schema Optimization

- domain: structured-generation
- secondary_domains: [prompt-engineering, api-integration, tool-use-llms]
- aliases: [function schema optimization, tool call quality, function schema engineering]
- broader: [function-schema-design, prompt-engineering]
- narrower: []
- related: [function-schema-design, json-mode-prompting, output-schema-enforcement, tool-use-llms, few-shot-tool-calling]
- prerequisites: [function-schema-design, tool-use-llms]
- confidence: high

**definition**: Tool Schema Optimization is the empirical process of iterating on function and tool descriptions to maximise correct tool selection and argument generation accuracy. It involves techniques such as: ablation of individual schema fields to identify which descriptions have the most impact on selection behaviour; A/B testing of alternative description phrasings; adding few-shot examples within tool descriptions; reducing schema surface area by consolidating functions with overlapping semantics; and ordering tools in the schema to influence model selection bias. The process treats the tool schema as a trainable artefact rather than a static documentation product.

**key_claim**: Tool schema optimization can produce substantial improvements in function-calling accuracy for complex multi-tool environments without any changes to the model or base prompt — the description quality, field naming conventions, and schema structure each independently influence tool selection, making schema design a first-class engineering discipline with measurable outcomes.

**warning**: Tool schema optimization results are model-specific — a schema optimised for one model family's function-calling behaviour may perform worse on another model due to differences in how models were trained to interpret tool descriptions, making schema portability across model providers an engineering challenge that requires separate validation for each deployment target.

## Vision-Language Prompting

- domain: multimodal-ai
- secondary_domains: [prompt-engineering, computer-vision, multimodal-llms]
- aliases: [VL prompting, visual prompting, multimodal prompting, image+text prompting]
- broader: [prompt-engineering, multimodal-ai]
- narrower: [image-captioning-prompts, visual-chain-of-thought, multimodal-few-shot, grounded-visual-reasoning]
- related: [image-captioning-prompts, visual-chain-of-thought, multimodal-few-shot, document-understanding-prompts, grounded-visual-reasoning]
- prerequisites: [prompt-engineering, vision-language-models]
- confidence: high

**definition**: Vision-Language Prompting refers to the set of techniques for constructing prompts that combine image and text inputs to steer the behaviour of multimodal language models (VLMs). Effective VL prompting involves decisions about how to describe the visual analysis task in the text portion, how to reference specific image regions or elements, how to use few-shot image+text examples to establish output format and reasoning depth, and how to elicit structured visual reasoning rather than surface-level description. The field adapts principles from text-only prompt engineering to the multimodal setting where the model must integrate two distinct input modalities.

**key_claim**: Vision-language prompting requires a qualitatively different approach to few-shot example design compared to text-only prompting — because visual semantics are not fully expressible in text, the few-shot images themselves carry substantial information that the text cannot replicate, and selecting visually representative examples requires understanding the distribution of visual content rather than just semantic task framing.

**warning**: Vision-language models are particularly susceptible to visual distractors — text in the image that conflicts with the text prompt, image regions irrelevant to the query, and misleading visual context can all override the intent of the text prompt, because the cross-modal attention mechanism may attend more strongly to salient visual features than to the instruction text.

## Image Captioning Prompts

- domain: multimodal-ai
- secondary_domains: [computer-vision, natural-language-generation, prompt-engineering]
- aliases: [image description prompts, visual description prompting, alt-text prompting]
- broader: [vision-language-prompting]
- narrower: []
- related: [vision-language-prompting, visual-chain-of-thought, grounded-visual-reasoning, document-understanding-prompts]
- prerequisites: [vision-language-prompting, vision-language-models]
- confidence: high

**definition**: Image Captioning Prompts are the text instructions provided alongside an image to a vision-language model to control the type, detail level, style, and focus of the generated description. The quality of captioning output varies substantially with prompting choices — a generic "describe this image" produces a different style of description than "list the objects in this image with their positions", "write an alt-text description for accessibility", or "describe the emotional tone of this scene in three sentences". Effective captioning prompts specify: the intended use of the caption, the target audience, the required detail level, the aspects of the image to prioritise or ignore, and any formatting constraints.

**key_claim**: The framing of an image captioning prompt fundamentally determines what the model attends to — models produce more accurate and useful captions when the prompt specifies the purpose and relevant dimensions rather than asking for a generic description, because VLMs have learned different captioning registers from their training data and selecting the right register via prompting is as important as the image content itself.

**warning**: Image captioning models can produce confidently-stated descriptions of image regions they cannot actually resolve — small, blurry, occluded, or ambiguous elements in an image may be described as if they are clearly visible, and the model's language fluency can mask its visual uncertainty, making hallucinations in image descriptions harder to detect than hallucinations in text-only tasks.

## Visual Chain of Thought

- domain: multimodal-ai
- secondary_domains: [prompt-engineering, computer-vision, chain-of-thought-prompting]
- aliases: [visual CoT, multimodal CoT, image reasoning chain]
- broader: [vision-language-prompting, chain-of-thought-prompting]
- narrower: []
- related: [vision-language-prompting, chart-and-table-reasoning, grounded-visual-reasoning, chain-of-thought-prompting, multimodal-few-shot]
- prerequisites: [chain-of-thought-prompting, vision-language-prompting]
- confidence: high

**definition**: Visual Chain of Thought (Visual CoT) is an adaptation of chain-of-thought prompting to multimodal inputs, in which the model is prompted to explicitly reason through visual content step-by-step before producing a final answer. In its basic form, the text prompt instructs the model to describe what it observes, identify relevant elements, reason about their relationships, and then draw a conclusion — externalising the visual reasoning process in the text portion of the output. More advanced forms interleave visual attention operations with reasoning steps, allowing the model to refer back to specific image regions during the reasoning chain.

**key_claim**: Visual chain-of-thought dramatically improves accuracy on tasks requiring multi-step visual reasoning — such as diagram interpretation, spatial relationship reasoning, and mathematical figure analysis — by forcing the model to commit to intermediate visual observations that can be checked, rather than directly mapping visual input to an answer in a way that is opaque and error-prone.

**warning**: Visual CoT can introduce a new class of hallucination where the model generates plausible-sounding but visually incorrect reasoning steps — because the model is producing natural language, its reasoning chains can satisfy linguistic coherence even when they are visually inaccurate, making it important to evaluate the intermediate reasoning steps independently from the final answer.

## Multimodal Few-Shot

- domain: multimodal-ai
- secondary_domains: [prompt-engineering, in-context-learning, computer-vision]
- aliases: [multimodal ICL, image-text few-shot, visual few-shot prompting]
- broader: [vision-language-prompting, few-shot-prompting]
- narrower: []
- related: [vision-language-prompting, visual-chain-of-thought, few-shot-prompting, semantic-similarity-in-prompts]
- prerequisites: [few-shot-prompting, vision-language-prompting]
- confidence: high

**definition**: Multimodal Few-Shot Prompting extends the few-shot in-context learning paradigm to multimodal inputs by providing interleaved (image, text) example pairs that demonstrate the desired task format before the target query. In a multimodal few-shot prompt, each demonstration consists of an image and a corresponding text response that shows the model what kind of answer is expected for that type of visual input. The selection of appropriate example images, the construction of the accompanying text demonstrations, and the ordering of examples are all prompt engineering decisions with significant impact on final output quality.

**key_claim**: Multimodal few-shot prompting enables VLMs to perform specialised visual analysis tasks — such as radiological image interpretation, industrial defect detection, or document information extraction — without fine-tuning, by providing visual examples that constrain the distribution of expected outputs in ways that text instructions alone cannot express.

**warning**: Multimodal few-shot prompting is sensitive to the visual similarity between demonstration images and the test image — when test images differ significantly in style, lighting, viewpoint, or domain from the demonstration images, the few-shot examples may establish a misleading prior that degrades performance relative to zero-shot prompting, which does not constrain the response distribution toward a visually dissimilar example set.

## Document Understanding Prompts

- domain: multimodal-ai
- secondary_domains: [information-extraction, computer-vision, prompt-engineering]
- aliases: [document AI prompts, visual document understanding, document parsing prompts]
- broader: [vision-language-prompting]
- narrower: []
- related: [vision-language-prompting, chart-and-table-reasoning, image-captioning-prompts, json-mode-prompting, structured-prediction-prompting]
- prerequisites: [vision-language-prompting, structured-prediction-prompting]
- confidence: high

**definition**: Document Understanding Prompts are prompting strategies designed for VLM-based processing of scanned or rendered documents — invoices, contracts, forms, academic papers, presentations — where text, tables, figures, and layout all carry semantic information. Effective document understanding prompts specify the extraction target precisely (e.g., "extract all line items from the invoice table and return as a JSON array"), instruct the model on how to handle uncertain or partially visible text, and often combine visual prompting with structured output instructions to produce machine-parseable extraction results. This is a key modality for enterprise document automation.

**key_claim**: Document understanding with VLMs supersedes traditional OCR + rule-based extraction pipelines on complex layouts because the model can jointly reason about text content, visual layout, and document structure — but this power comes with the requirement for more sophisticated prompting that explicitly frames the document type and the extraction semantics, since generic description prompts produce descriptive rather than structured outputs.

**warning**: Document understanding prompts are highly sensitive to document quality — when input documents have poor scan quality, unusual layouts, or handwritten elements, VLMs can produce confident but incorrect extractions without signalling uncertainty, making human review and confidence-based routing essential for production document processing pipelines.

## Chart and Table Reasoning

- domain: multimodal-ai
- secondary_domains: [data-visualisation, prompt-engineering, computer-vision]
- aliases: [chart reasoning prompts, table understanding, visual data reasoning]
- broader: [vision-language-prompting, visual-chain-of-thought]
- narrower: []
- related: [visual-chain-of-thought, document-understanding-prompts, grounded-visual-reasoning, numerical-reasoning-prompts]
- prerequisites: [vision-language-prompting, visual-chain-of-thought]
- confidence: high

**definition**: Chart and Table Reasoning refers to the specialised prompting strategies and evaluation considerations for tasks where a vision-language model must extract data, identify trends, compute derived statistics, or answer analytical questions from visual representations of quantitative data. Effective prompts for chart and table reasoning typically combine visual chain-of-thought instructions with explicit guidance to read axis labels and scales before interpreting trends, to identify the chart type before making data claims, and to express numerical uncertainty when data values are difficult to read precisely from the visual representation.

**key_claim**: Chart and table reasoning is among the most challenging multimodal tasks for current VLMs because it requires integrating spatial reasoning (where is a data point?), visual processing (what value does this bar/point represent?), and quantitative reasoning (what is the trend/comparison/statistic?) in a way that errors compound across steps — making explicit visual CoT prompts that decompose these sub-tasks significantly more reliable than direct answer prompts.

**warning**: VLMs systematically underperform on precise numerical reading from charts — the models tend to produce approximate values that are in the right range but incorrect at the level of precision suggested by their confident phrasing, and they frequently misread logarithmic scales, dual-axis charts, and stacked bar charts in ways that produce directionally plausible but numerically wrong conclusions.

## Interleaved Image-Text Prompting

- domain: multimodal-ai
- secondary_domains: [prompt-engineering, multimodal-llms, in-context-learning]
- aliases: [mixed-modality prompting, interleaved multimodal prompting, image-text interleaving]
- broader: [vision-language-prompting, multimodal-few-shot]
- narrower: []
- related: [multimodal-few-shot, vision-language-prompting, visual-chain-of-thought, document-understanding-prompts]
- prerequisites: [vision-language-prompting, multimodal-few-shot]
- confidence: high

**definition**: Interleaved Image-Text Prompting is a prompting paradigm for models that support arbitrary interleaving of image and text tokens within a single prompt, allowing images to appear at any position in the input sequence rather than only as a prefix or suffix. This enables richer prompting structures such as image-then-question-then-image-then-analysis patterns, multi-image comparison tasks, sequential visual reasoning chains where intermediate text instructions reference specific images, and multi-turn dialogues that mix image and text turns. Models like GPT-4V, Gemini, and LLaVA series support varying degrees of interleaving capability.

**key_claim**: Interleaved image-text prompting enables a qualitatively new class of visual reasoning tasks — those requiring comparative analysis across multiple images, sequential visual observation, or cross-modal reference in multi-step reasoning — that cannot be expressed in prefix-image prompting architectures, making it the enabling capability for advanced visual agents and complex document analysis workflows.

**warning**: The relative positioning of image and text elements in an interleaved prompt can create unexpected attention patterns — models may attend more strongly to whichever modality appears most recently before the generation target, meaning that the order of image and text elements in a multi-turn interleaved prompt is a significant prompt design variable with empirically measurable effects on output quality.

## Grounded Visual Reasoning

- domain: multimodal-ai
- secondary_domains: [computer-vision, prompt-engineering, spatial-reasoning]
- aliases: [visual grounding, spatially grounded reasoning, region-referenced visual reasoning]
- broader: [vision-language-prompting, visual-chain-of-thought]
- narrower: []
- related: [vision-language-prompting, visual-chain-of-thought, chart-and-table-reasoning, document-understanding-prompts]
- prerequisites: [vision-language-prompting, visual-chain-of-thought]
- confidence: high

**definition**: Grounded Visual Reasoning refers to the capability and prompting strategies by which a vision-language model reasons about specific, localised regions of an image — naming, describing, comparing, or drawing conclusions about particular objects, spatial relationships, or image areas rather than the image globally. Grounded reasoning requires the model to (a) identify the relevant spatial region(s) for a given question, (b) attend to those regions for detailed visual interpretation, and (c) produce a response that is connected to specific visual evidence. Prompting for grounded reasoning often involves region descriptions, coordinate-based references (bounding boxes), or instructions to cite specific image elements in the response.

**key_claim**: Grounded visual reasoning is a more reliable evaluation target than holistic image description because it provides a verifiable correspondence between the model's stated reasoning and specific visual evidence — a model that says "the red object in the upper left corner is a sphere" can be checked against the image, while a holistic "this image shows a colorful room" is harder to falsify, making grounding a key component of trustworthy visual AI systems.

**warning**: Prompting for grounded visual reasoning can produce over-confident localisation — models may confidently claim that a response is grounded in a specific image region when the region they reference does not actually support their claim, producing a false appearance of evidence-based reasoning that can mislead human reviewers who trust the model's spatial references without verification.
