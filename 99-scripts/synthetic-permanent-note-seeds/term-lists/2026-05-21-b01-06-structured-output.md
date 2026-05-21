---
batch_name: b01-06-structured-output
batch_date: 2026-05-21
default_domain: prompt-engineering
default_confidence: high
notes: |
  Structured output concepts covering JSON mode, schema-following, grammar-constrained
  decoding, markdown/XML output formatting, regex constraints, and output length control.
---

# Batch: B01-06 Structured Output

## JSON Mode Prompting

- secondary_domains: [llm-inference, api-design, software-engineering]
- aliases: [JSON output forcing, structured JSON generation, JSON-mode API]
- broader: [structured-output-enforcement, prompt-engineering]
- narrower: []
- related: [structured-output-enforcement, grammar-constrained-decoding, schema-following-prompts, xml-structured-prompting, output-length-control]
- prerequisites: [prompt-engineering, api-design, json-format]
- confidence: high

**definition**: JSON mode prompting refers to the combination of API-level enforcement and prompt design techniques that cause a language model to produce outputs conforming to valid JSON syntax. At the API level, JSON mode (available in OpenAI's API, Anthropic's API, and others) activates constrained decoding that guarantees syntactically valid JSON output by limiting the token sampling space to tokens that maintain JSON-validity at each generation step. At the prompt level, JSON mode prompting involves specifying the desired output schema, providing example JSON structures, and instructing the model on how to handle missing values, nested structures, and array formatting.

**key_claim**: API-level JSON mode enforcement solves only the syntactic validity problem — it guarantees that the output parses as valid JSON but does not guarantee that the JSON contains the required keys, that values have the correct types, or that the content is semantically accurate; combining JSON mode with explicit schema validation and schema-following prompts is necessary to achieve both syntactic and semantic correctness.

**warning**: JSON mode can cause subtle semantic failures when the model forces valid JSON by making up values to complete a required structure — a model that must produce a JSON object with a specific schema will invent plausible-looking values for unknown fields rather than leaving them null or raising an error, creating silently wrong outputs that pass JSON validation but contain hallucinated content.

## Structured Output Enforcement

- secondary_domains: [llm-inference, software-engineering, api-design]
- aliases: [constrained output generation, structured generation, output schema enforcement]
- broader: [prompt-engineering, controlled-text-generation]
- narrower: [json-mode-prompting, grammar-constrained-decoding, schema-following-prompts]
- related: [json-mode-prompting, grammar-constrained-decoding, schema-following-prompts, regex-constrained-generation, output-length-control]
- prerequisites: [prompt-engineering, language-model-inference, api-design]
- confidence: high

**definition**: Structured output enforcement encompasses the collection of techniques — at the prompt, API, and inference levels — for ensuring that language model outputs conform to a specified format, schema, or structure. Approaches range from soft enforcement (prompt instructions with examples) to hard enforcement (constrained decoding that restricts the token sampling space to structure-valid tokens at each step). Structured output enforcement is critical for programmatic integration of LLM outputs into downstream software pipelines where format violations cause parsing errors or silent data corruption.

**key_claim**: The reliability gap between soft (prompt-based) and hard (constrained-decoding-based) structured output enforcement is large and practically significant — even with explicit JSON schema instructions and few-shot examples, LLMs produce invalid or non-conforming outputs at rates of 1–10% in production settings, which is unacceptable for automated pipelines; hard enforcement via constrained decoding or grammar-based sampling eliminates this failure mode entirely at the cost of slightly reduced fluency.

**warning**: Constrained decoding-based structured output enforcement changes the model's generation distribution beyond just enforcing format constraints — by restricting which tokens are sampleable at each step, constrained decoding can cause the model to produce grammatically valid but semantically incoherent outputs when the most plausible token is outside the constraint set; the content quality of grammar-constrained outputs should be validated separately from their structural validity.

## Grammar-Constrained Decoding

- secondary_domains: [llm-inference, formal-grammars, controlled-generation]
- aliases: [constrained decoding, grammar-guided generation, CFG-constrained sampling]
- broader: [structured-output-enforcement, llm-decoding]
- narrower: [json-schema-constrained-decoding, regex-constrained-generation]
- related: [structured-output-enforcement, json-mode-prompting, regex-constrained-generation, logit-bias-manipulation, schema-following-prompts]
- prerequisites: [language-model-inference, formal-grammars, context-free-grammars, finite-state-automata]
- confidence: high

**definition**: Grammar-constrained decoding is a class of inference algorithms that restrict the token sampling distribution at each generation step to tokens that can legally extend the current partial output within a specified formal grammar — such as a context-free grammar (CFG), a JSON schema, a regular expression, or a Backus-Naur Form specification. At each step, a constraint engine computes the set of valid next tokens by advancing the grammar's state machine and masks out invalid tokens before sampling, guaranteeing that the final output is syntactically valid according to the grammar. Libraries such as Outlines, LM-Format-Enforcer, and Guidance implement grammar-constrained decoding for common formats.

**key_claim**: Grammar-constrained decoding provides provable format guarantees that prompt engineering cannot — by operating at the token sampling level rather than the instruction level, it is impossible (by construction) for the model to produce output that violates the specified grammar, making it the only reliable mechanism for integrating LLMs into systems that require strict format compliance for safety-critical or automated processing pipelines.

**warning**: Grammar-constrained decoding degrades inference speed because constraint enforcement requires maintaining and advancing the grammar state machine at every generation step, adding latency proportional to grammar complexity; for complex schemas with deep nesting and many alternatives, constraint enforcement can add 20–50% inference overhead, and the constraint engine itself may contain bugs that produce over-constraining (rejecting valid outputs) or under-constraining (accepting invalid outputs) behaviour.

## Schema-Following Prompts

- secondary_domains: [prompt-engineering, api-design, structured-data]
- aliases: [schema-guided prompting, schema-adherent generation, type-safe prompting]
- broader: [structured-output-enforcement, prompt-engineering]
- narrower: []
- related: [json-mode-prompting, grammar-constrained-decoding, structured-output-enforcement, xml-structured-prompting, output-length-control]
- prerequisites: [prompt-engineering, json-schema, api-design]
- confidence: high

**definition**: Schema-following prompts are prompt structures that explicitly convey the desired output schema to the model, typically by providing a JSON Schema, Pydantic model definition, TypeScript interface, or annotated example output alongside the task instruction. The schema specification communicates required fields, data types, optional fields, nesting structure, and format constraints, allowing the model to understand exactly what structure the output should conform to. Effective schema-following prompts typically include: the schema definition, a concrete filled example, instructions for handling missing values, and explicit error handling guidance.

**key_claim**: Schema-following prompts that include concrete examples of filled schemas are substantially more reliable than schema-following prompts that only include the schema definition — models have limited ability to consistently infer the expected output format from an abstract schema, but a single filled example provides a template that dramatically reduces format errors even without constrained decoding.

**warning**: Schema-following prompts create an implicit assumption that the model will always have sufficient information to fill the schema — when required fields cannot be populated from the available context, the model tends to hallucinate values rather than return null or raise an explicit error; schema prompts should explicitly instruct the model to use a designated null sentinel value and explain what to do when information is unavailable.

## Markdown Output Prompting

- secondary_domains: [prompt-engineering, content-formatting, documentation]
- aliases: [markdown formatting prompts, rich text output prompting, markdown generation]
- broader: [structured-output-enforcement, prompt-engineering]
- narrower: []
- related: [xml-structured-prompting, schema-following-prompts, output-length-control, json-mode-prompting]
- prerequisites: [prompt-engineering, markdown-format]
- confidence: high

**definition**: Markdown output prompting refers to prompt design techniques that cause LLMs to produce responses formatted in Markdown syntax — with appropriate use of headers, bullet lists, bold and italic text, code blocks, tables, and blockquotes — rather than plain text. Markdown output prompting is relevant for content generation (technical documentation, README files, blog posts), chat interfaces that render markdown (Obsidian, GitHub, Notion), and automated pipelines that convert LLM outputs to HTML or PDF. Effective markdown prompting specifies the desired document structure, heading hierarchy, when to use lists versus prose, and code block language tags.

**key_claim**: Markdown output prompts that provide a structural skeleton (e.g., specifying heading levels and approximate content for each section) produce more consistently structured outputs than prompts that simply request "markdown format" — without structural guidance, models choose markdown elements based on aesthetic preference rather than semantic appropriateness, producing inconsistent heading levels and gratuitous bullet lists that fragment information that should be prose.

**warning**: Over-relying on markdown formatting instructions can produce outputs that prioritise visual structure over substantive content — models trained on markdown-heavy instruction datasets are biased toward producing heavily formatted responses with shallow content in each bullet point rather than substantive prose; explicitly instructing the model to prefer prose and use lists sparingly counteracts this bias.

## XML Structured Prompting

- secondary_domains: [prompt-engineering, structured-data, llm-interaction]
- aliases: [XML prompt format, XML-tagged prompting, XML output structuring]
- broader: [structured-output-enforcement, prompt-engineering]
- narrower: []
- related: [json-mode-prompting, schema-following-prompts, markdown-output-prompting, grammar-constrained-decoding]
- prerequisites: [prompt-engineering, xml-format]
- confidence: high

**definition**: XML structured prompting is a prompt engineering pattern that uses XML-style tags to delimit sections of both the prompt input and the expected output, leveraging the models' training on XML-tagged content (code, HTML, data formats) to produce reliably structured responses. In the input, XML tags segment prompt components: `<instructions>`, `<context>`, `<examples>`, `<query>`. In the output, XML tags structure response components: `<reasoning>`, `<answer>`, `<confidence>`. Anthropic specifically recommends XML-tagged prompting for Claude models and provides guidance on tag naming conventions. The pattern is particularly effective for multi-section outputs that downstream parsers need to extract reliably.

**key_claim**: XML structured prompting provides better output demarcation than markdown for programmatic extraction because XML tags are unambiguous syntactic delimiters that do not occur naturally in prose, making regex or parser-based extraction of tagged sections reliable; markdown headers are more ambiguous and can occur in quoted content, while XML tags in a specified schema are extractable without false positives.

**warning**: XML structured prompting creates a dependency on the model consistently producing the specified tag structure — while this is reliable for short, well-defined outputs, the model may omit, misspell, or partially complete XML tags in long outputs or complex multi-step tasks, causing parsing failures; including explicit validation of required tags in post-processing pipelines is necessary for production robustness.

## Regex-Constrained Generation

- secondary_domains: [llm-inference, controlled-generation, data-extraction]
- aliases: [regex-guided generation, pattern-constrained decoding, regex output forcing]
- broader: [grammar-constrained-decoding, structured-output-enforcement]
- narrower: []
- related: [grammar-constrained-decoding, logit-bias-manipulation, structured-output-enforcement, output-length-control]
- prerequisites: [regular-expressions, grammar-constrained-decoding, language-model-inference]
- confidence: high

**definition**: Regex-constrained generation is a constrained decoding technique that restricts token sampling to tokens consistent with a regular expression pattern at each generation step, guaranteeing that the final output matches the specified regex. By compiling the regex into a finite state automaton and advancing the automaton state with each generated token, the constraint engine can determine at each step which tokens can legally appear next; tokens that would cause the automaton to reach a dead state are masked before sampling. This technique is used to enforce precise output formats such as dates, phone numbers, product codes, identifiers, and fixed-length numeric outputs.

**key_claim**: Regex-constrained generation is the appropriate tool when the output format is expressible as a regular language but too precise or too low-level to reliably produce through prompt instructions alone — it is faster to implement and more computationally efficient than full CFG-based constraint, making it the right choice for simple pattern enforcement while CFG-based constraint is reserved for context-sensitive structural requirements.

**warning**: Regex-constrained generation applies only to the surface form of the output and cannot constrain semantic content — a regex that enforces a date format (YYYY-MM-DD) guarantees a syntactically valid date string but not that the date is semantically meaningful in context or that it is factually correct; all semantic correctness checking must be handled separately from the format constraint.

## Output Length Control

- secondary_domains: [prompt-engineering, llm-inference, user-experience]
- aliases: [response length control, verbosity control, token budget management, length specification]
- broader: [prompt-engineering, structured-output-enforcement]
- narrower: []
- related: [structured-output-enforcement, json-mode-prompting, markdown-output-prompting, logit-bias-manipulation, repetition-penalty]
- prerequisites: [prompt-engineering, language-model-inference]
- confidence: high

**definition**: Output length control encompasses the prompt design and API parameter techniques for constraining or directing the length of language model responses. API-level controls include `max_tokens` (hard ceiling on token count) and stop sequences (terminating generation at specific tokens or patterns). Prompt-level controls include explicit length instructions ("in one paragraph", "in exactly three bullet points", "no more than 100 words"), implicit length anchoring through examples that demonstrate the desired response length, and structural constraints that bound the number of sections or items. Length control is important for latency management, cost control, UI layout constraints, and matching response verbosity to user expectations.

**key_claim**: The most reliable prompt-level length control technique is providing a concrete structural constraint (e.g., "output exactly 3 bullet points") rather than a word or sentence count instruction — models cannot reliably estimate word counts mid-generation and will frequently overshoot or undershoot count-based targets, while structural constraints that match the natural granularity of the task (number of items, number of steps) are followed more consistently.

**warning**: Hard `max_tokens` truncation at the API level produces responses that are cut off mid-sentence, mid-word, or mid-JSON structure — while this prevents runaway long responses, it produces broken outputs that may be worse than shorter but complete responses; combining a soft prompt-level length instruction with a `max_tokens` ceiling set 20–30% above the expected length provides safety against runaway generation while maintaining output completeness.
