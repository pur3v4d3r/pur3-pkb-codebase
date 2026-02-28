



# Repository Synthesis Agent - Documentation Generator Template

This is a specialized version of the Repository Synthesis Agent starter template, designed specifically for generating high-quality documentation for existing prompts. That is, instead of engineering a new prompt, this template focuses on analyzing an existing prompt file and producing comprehensive documentation that explains its usage, configuration, and internal logic.







Here is the revised template, rigorously adapted for **generating documentation** for existing prompts rather than engineering new ones.

This version shifts the agent's focus from *optimization* to *extraction, explanation, and technical writing*.

### Reusable Documentation Generator Template

```xml
<starter_prompt>
<goal>
Create production-grade, comprehensive documentation for the [TARGET_PROMPT_NAME] prompt, optimized for [TARGET_AUDIENCE, e.g., Developers/End Users] clarity and usability.
</goal>

<thinking type="Analysis">
I need you to inspect the file that I am uploading with this chat message called: `[SOURCE_PROMPT_FILENAME]`. 
**CAREFULLY** and with **SCRUTINY**, you must inspect this finalized prompt file. **The goal** is for you to *completely understand the internal logic, flow, and architecture* of this established system. You are not changing the prompt; you are **reverse-engineering its logic** to create a "Manual of Operations" that explains exactly how it works, how to use it, and why it is structured this way.
</thinking>

<thinking type="Decomposition">
- To achieve this, you will need to dissect the existing prompt into its functional components.
    - You **MUST** *extract and catalog* every variable, constraint, and logic branch.
        - **Map out the data flow**: How does user input travel through the prompt's reasoning steps?
        - **Identify the "Magic"**: Isolate the specific reasoning frameworks (e.g., ToT, CoT) used within the prompt so they can be documented.
        - **Catalog Output Artifacts**: Define exactly what the prompt produces so users know what to expect.
- **ALWAYS** use the `Exploration Phase` XML block to organize your analysis of the file.
- **ALWAYS** document your understanding of the *intended behavior* versus the *literal text*.
</thinking>

<thinking type="Documentation_Architecture">
Once you have deconstructed the prompt, you must design the structure of the documentation file.
    - The documentation **MUST** follow a logical hierarchy:
        1. **Executive Summary**: High-level purpose and use cases.
        2. **Technical Architecture**: The internal "Cognitive Scaffolding" (how it thinks).
        3. **Usage Guide**: Parameters, variables, and how to trigger it.
        4. **Output Specification**: Detailed breakdown of the deliverables.
        5. **Best Practices**: How to get the best results from this specific prompt.
</thinking>

<thinking type="Drafting">
**!IMPORTANT**: You **MUST** use the documentation standards found in the *exemplars loaded into your Claude Project Knowledge*.
  - Use `[REFERENCE_DOC_STYLE]` as your style guide for tone and formatting.
  - Ensure the documentation uses *clear semantic headers* and *scannable formatting* (tables, callouts).
</thinking>

<thinking type="Finalization">
- Review the generated documentation against the original prompt source code to ensure 100% technical accuracy.
- Verify that all YAML frontmatter requirements for the documentation file itself are met.
</thinking>

- **IMPORTANT**:
- **Make sure** you reference the `[REFERENCE_FILE_1]` (e.g., Glossary or Style Guide) to ensure terminology consistency.

<output>
- You must output a new documentation file called: `[OUTPUT_FILENAME]`.
  - This file **MUST** be a *production-ready technical document*.
  - It **MUST** include a complete *YAML frontmatter* section for Obsidian/Knowledge Base integration.
  - It **MUST** accurately reflect the logic of the source prompt without hallucinating features that do not exist.
</output>
</starter_prompt>

```

### Variable Dictionary

| Placeholder | Description | Example |
| --- | --- | --- |
| `[TARGET_PROMPT_NAME]` | The name of the prompt being documented | `Brainstorming V2` |
| `[TARGET_AUDIENCE]` | Who is reading this doc? | `Prompt Engineers`, `End Users` |
| `[SOURCE_PROMPT_FILENAME]` | The actual prompt file you are analyzing | `brainstorm-codebase-pack-v2.0.0.md` |
| `[REFERENCE_DOC_STYLE]` | A file in your Project defining how docs should look | `Docs-Style-Guide.md` |
| `[REFERENCE_FILE_1]` | Additional reference (Glossary, Master definitions) | `YAML Master Reference` |
| `[OUTPUT_FILENAME]` | The name of the resulting doc file | `brainstorm-v2-documentation.md` |

**Would you like me to use this template to generate documentation for the `Prompt Engineering Agent v4.0` system prompt provided above?**







### Reusable Documentation Generator Template 002

```xml
<starter_prompt>
<goal>
A production-ready documentation package for the [PROMPT_NAME] prompt, optimized for clarity, user adoption, and technical accuracy.
</goal>

<thinking type="Analysis">
I need you to inspect the file that I am uploading with this chat message called: `[PROMPT_FILENAME]`. 
**CAREFULLY** and with **SCRUTINY**, you must inspect this prompt file. **The goal** is for you to *completely understand the logic, flow, and architecture* of this established prompt, **inside and out**. So that, in turn, you can *create a comprehensive documentation file* that *explains exactly how to use, configure, and maximize the value of this tool*. The documentation **MUST** accurately reflect the core mechanisms found in `[PROMPT_FILENAME]`.
</thinking>

<thinking type="Decomposition">
- To achieve this, you will need to break down the existing prompt into its logical components.
    - You **MUST** *reverse engineer* the prompt's structure before writing a single word of documentation. 
        - **Variables & Parameters**: Identify every placeholder, variable, and configuration option.
        - **Logic Flow**: Map out the step-by-step reasoning process the prompt enforces.
        - **Output Format**: Define exactly what the user should expect as a result.
        - **Edge Cases**: Identify constraints and potential failure points handled by the prompt.
- **ALWAYS** use the `Exploration Phase` XML block to structure your analysis of the code/text.
- **ALWAYS** remember to **think step by step** to ensure no feature is left undocumented.
- **ALWAYS** document your thought process in the `thinking` XML blocks so we can audit how you interpreted the prompt's instructions.
</thinking>

<thinking type="Structure_Planning">
Once you have analyzed the prompt, you will need to structure the documentation. It should include:
1. **Executive Summary**: What this prompt does and why it exists.
2. **Prerequisites**: What the user needs (inputs, context, files) before running it.
3. **Configuration Guide**: A table or list of all variables (e.g., `[VARIABLE]`) and how to fill them.
4. **Execution Logic**: A high-level explanation of the prompt's "chain of thought."
5. **Examples**: Hypothetical input/output scenarios.
</thinking>

<thinking type="Synthesis">
The final step will be to synthesize your analysis into a polished Markdown documentation file. This documentation should be professional, easy to read, and strictly follow our documentation standards.
</thinking>

<thinking type="Implementation">
**!IMPORTANT**: You **MUST** reference the documentation standards found in your Claude Project Knowledge (specifically `[DOCS_STYLE_GUIDE]` or `[TEMPLATE_FILE]`).
  - Use these files to ensure the formatting, tone, and header hierarchy match our organization's best practices.
</thinking>

<output>
- You must output a new documentation file called: `[OUTPUT_FILENAME]`.
  - This file **MUST** be written in clean Markdown.
  - The file **MUST** have a complete *YAML frontmatter* section for Obsidian/Knowledge Base compatibility.
  - The content **MUST** adhere to the style guidelines in `[DOCS_STYLE_GUIDE]`.
</output>
</starter_prompt>

```

---

### Variable Dictionary

| Placeholder | Description | Example |
| --- | --- | --- |
| `[PROMPT_NAME]` | The official name of the prompt you are documenting | `Python Mastery Agent` |
| `[PROMPT_FILENAME]` | The specific file you are uploading for analysis | `python-mastery-v3.md` |
| `[DOCS_STYLE_GUIDE]` | The file in your Project Knowledge that defines how docs should look | `Docs_Standard_v1.md` |
| `[TEMPLATE_FILE]` | A reference file for layout (optional) | `Readme_Template.md` |
| `[OUTPUT_FILENAME]` | The desired name of the documentation file | `python-mastery-docs-v1.0.md` |

### How to use this

1. **Upload** the prompt file you want documented.
2. **Paste** this template into the chat.
3. **Replace** the bracketed placeholders with your specific file names.
4. **Run** it.

**Would you like me to make any adjustments to the specific sections (e.g., adding a requirement for a "Troubleshooting" section)?**





















This is a highly specialized template for creating a new, optimized version of an existing prompt by thoroughly analyzing its structure and logic. The focus here is on **reconstruction and enhancement** rather than simple documentation. That is, the agent is tasked with **reverse-engineering** the existing prompt to understand its core mechanisms and then **building a new, improved version** that incorporates best practices.


### Reusable Claude Project Template 
```xml
<starter_prompt>
<goal>
A production ready newly revamped [TARGET_TASK_TYPE] prompt, that has been optimized rigorously for performance and high quality [KEY_METRIC_OR_OUTCOME]
</goal>

<thinking type="Analysis">
I need you to inspect the file that I am uploading with this chat message called: `[SOURCE_FILENAME]`. 
**CAREFULLY** and with **SCRUTINY**, you must inspect this codebase pack. **The goal**, is for you to *completely understand the way these systems work*, **inside and out**. So that, in turn, you can *create a new, updated version* that *implements all of our hard won prompt engineering best practices*. The new prompt **MUST** take full advantage of the core mechanisms from `[SOURCE_FILENAME]` because we know that it is a winner when it comes to *performance and ROI for prompting output*.
</thinking>

<thinking type="Decomposition">
- To achieve this, you will need to break down the existing prompt into its core components and functions. This will allow you to identify areas for improvement and optimization.
    - You **MUST** *fully plan out* the purposed prompt before starting any work on generation. 
        - It will need to be **meticulously mapped out before hand** so that the **cognitive scaffolding** and **architecture** can shine with its full force, allowing the LLM to fully reason during the [CORE_ACTION_VERB].
        - This will involve creating a detailed outline of the prompt structure, including the various sections and their intended purposes.
        - You will also need to identify any potential bottlenecks or inefficiencies in the existing prompt that could be improved upon.
- **ALWAYS** use the `Exploration Phase` XML block to help you with this process.
- **ALWAYS** remember to **think step by step** and use **advanced reasoning frameworks** to help you with this process.
- **ALWAYS** remember to **strategically use the exemplar files** that are loaded into your Claude Project Knowledge to help you with this process.
- **ALWAYS** remember to **document your thought process** in the various `thinking` XML blocks.
    - This is for future reference so we can understand the true logic and reasoning behind this session. Don't worry about making it look pretty just make sure its clear and easy to follow.
</thinking>

<thinking type="Reconstruction">
Once you have a thorough understanding of the existing prompt, you will need to reconstruct it from the ground up. This will involve rethinking the structure, flow, and content of the prompt to ensure that it is fully optimized for performance and ROI.
</thinking>

<thinking type="Synthesis">
The final step will be to synthesize all of your insights and improvements into a new, cohesive prompt. This new prompt should be a significant upgrade over the original, incorporating all of the best practices and techniques that we have developed.
</thinking>

<thinking type="Implementation">
**!IMPORTANT**: You **MUST** use the *exemplars loaded into your Claude Project Knowledge*.
  - These are to help you implement the various advanced reasoning frameworks needed for this with masterful skill and precision.
    - These are individual files that have **clear semantic filenames** for you to *strategically use the exemplar that would provide the most performance increase*.
</thinking>

<thinking type="Finalization">
- Once the new prompt is complete, you will need to finalize it by testing and refining it to ensure that it meets our high standards for performance and ROI.
</thinking>

- **IMPORTANT**:
- **Make sure** you use the files marked `[REFERENCE_FILE_1]` and `[REFERENCE_FILE_2]`, in the final prompt.

<output>
- You must output a new prompt file called: `[OUTPUT_FILENAME]`.
  - This new prompt file **MUST** be a *production ready prompt* that is *fully optimized* for *performance* and *ROI*.
  - The new prompt file **MUST** have a complete *YAML frontmatter* section for Obsidian, and also implement *YAML* in the prompt for various metadata, *while also* following the *comment blocks from the* `[STYLE_GUIDE_FILENAME]`.
</output>
</starter_prompt>

```

---

### Variable Dictionary

To use this template, simply Find & Replace the following placeholders:

| Placeholder | Description | Example |
| --- | --- | --- |
| `[TARGET_TASK_TYPE]` | The category of prompt you are building | Coding, Copywriting, Analysis |
| `[KEY_METRIC]` | The primary quality indicator | Thinking and reasoning, Code efficiency, Tone accuracy |
| `[SOURCE_FILENAME]` | The file containing the logic you want to clone/improve | `python-mastery-pack.md` |
| `[CORE_ACTION_VERB]` | The main action the LLM performs | inference, compilation, drafting |
| `[REFERENCE_FILE_X]` | Specific gold-standard files in your Project Knowledge | `Gold standard`, `YAML Master` |
| `[OUTPUT_FILENAME]` | The desired name of the result | `python-mastery-v2.0.0.md` |
| `[STYLE_GUIDE_FILENAME]` | The file controlling the output style | `Gold Standard Exemplar` |

**Would you like me to execute this template now for a specific task you have in mind?**









This is a highly advanced prompt engineering template designed to elevate an existing prompt to "Reasoning Level 5" (Expert/Architect level). That is, instead of just inspecting and describing the prompt, the agent is tasked with **deeply analyzing** the prompt's architecture, **simulating its execution**, and **modeling the audience** to create documentation that truly serves its users.
And so, this template is focused on **structural analysis**, **simulation**, and **audience modeling** to produce documentation that is not only accurate but also highly usable.




To improve upon your starter prompt and elevate it to a "Reasoning Level 5" (Expert/Architect level), we need to move beyond simple "inspection" and enforce **structural analysis**, **simulation**, and **audience modeling**.

The goal is to stop the LLM from just *describing* the prompt and force it to *understand the system architecture* of the prompt so it can write documentation that actually works for a human user.

Here are the specific **Optimization Modules** I have applied, followed by the fully revamped prompt.

### 🚀 Key Optimizations Applied

1. **The "Reverse-Engineering Trace"**: Instead of just asking for analysis, I added a requirement to create a "Logic Map" inside the thinking block. This forces the LLM to prove it understands the flow before it writes the docs.
2. **Audience Modeling**: I added a step where the LLM must determine *who* the documentation is for (User vs. Developer) and adjust complexity accordingly.
3. **Simulation Step**: The prompt now explicitly asks the LLM to "mentally execute" the prompt to find edge cases and failure modes, which leads to better "Troubleshooting" sections in the docs.
4. **Variable Extraction Protocol**: A strict instruction to parse every `{{variable}}` or `[placeholder]`, ensuring the Configuration Guide is never incomplete.

---

### The Revamped "Architect-Level" Documentation Prompt

Copy the code block below. It uses advanced XML tagging to guide the model's latent space through a rigorous analytical process.

```xml
<starter_prompt>
<role>
You are the **Lead Technical Documentation Architect** for a high-performance prompt engineering team. Your specialty is **Reverse Engineering** complex LLM system prompts and translating them into crystal-clear, production-grade documentation (READMEs, User Guides, Technical Specifications).
</role>

<goal>
Analyze the uploaded prompt file `[PROMPT_FILENAME]` and generate a **comprehensive documentation package** that serves two purposes:
1. **Operational Guide:** Teaches a user exactly how to configure and execute the prompt.
2. **Architectural Reference:** Explains the logic/reasoning flow to maintainers.
</goal>

<thinking type="Phase_1_Architectural_Dissection">
I need to inspect `[PROMPT_FILENAME]` not as text, but as code.
**EXECUTION PROTOCOL:**
1.  **Variable Extraction**: Scan the file for ALL placeholders, variables, and configuration blocks (e.g., YAML frontmatter, `{{inputs}}`, `[variables]`). List them exhaustively.
2.  **Logic Mapping**: Create a mental flowchart of the prompt's reasoning pipeline.
    * *Input Phase* -> *Transformation Phase* (Thinking/CoT) -> *Output Phase*.
3.  **Mechanism Identification**: Identify specific prompt engineering techniques used (e.g., Few-Shot, Chain-of-Thought, Persona-Gating, XML tagging).
</thinking>

<thinking type="Phase_2_Simulation_and_Stress_Test">
Now, I will mentally "execute" this prompt with a hypothetical input to identify friction points.
* *Simulation*: If I input X, does the prompt logic handle it? 
* *Edge Case Detection*: What happens if the input is vague? Does the prompt have error handling or fallback logic?
* *Constraint Analysis*: What are the hard "Do Not" rules embedded in the prompt? These must be highlighted in the documentation as "Critical Warnings."
</thinking>

<thinking type="Phase_3_Audience_Modeling">
Who is this documentation for?
* *Target Audience*: [Determine based on prompt complexity - e.g., Developers, Content Writers, Analysts].
* *Tone*: Professional, direct, and technically precise.
* *Structure*: I will organize the documentation to prioritize "Time to First Value" (getting it running quickly) while preserving depth for power users.
</thinking>

<thinking type="Phase_4_Synthesis">
I will now construct the documentation file `[OUTPUT_FILENAME]` adhering to the `[DOCS_STYLE_GUIDE]`.
* I will ensure the **YAML Frontmatter** is correctly formatted for Knowledge Base integration.
* I will create a clear **"Configuration Table"** for variables.
* I will include a **"Logic Flow"** section explaining *how* the prompt thinks (derived from Phase 1).
</thinking>

<instructions>
**MANDATORY OUTPUT REQUIREMENTS:**
1.  **Executive Summary**: A high-level pitch of what this prompt solves.
2.  **Quick Start**: The fastest way to run the prompt (copy-pasteable).
3.  **Parameter Reference**: A table of every variable found in Phase 1 (Variable, Description, Required/Optional).
4.  **Internal Logic**: An explanation of the "Thinking" process the prompt uses (crucial for debugging).
5.  **Best Practices**: How to get the best results (derived from Phase 2 simulation).
</instructions>

<output>
- Generate the file: `[OUTPUT_FILENAME]`.
- Format: Clean, hierarchical Markdown.
- Style: Strict adherence to `[DOCS_STYLE_GUIDE]`.
</output>
</starter_prompt>
```

### Why this version is better:

1. **`Phase_1_Architectural_Dissection`**: In the original, the model just "inspected." Here, it is forced to **extract variables** and **map logic**. This prevents the common issue where documentation misses hidden configuration parameters.
2. **`Phase_2_Simulation`**: By forcing the model to "mentally execute" the prompt, you elicit reasoning about **Edge Cases**. This results in documentation that includes "Warnings" or "Troubleshooting" sections, which are high-value but often missed.
3. **`Mechanism Identification`**: It asks the model to identify *techniques* (like CoT or Few-Shot). This adds a layer of "meta-commentary" to the docs, helping users understand *why* the prompt is structured that way.
4. **Explicit Instruction Block**: The `<instructions>` block separates the "thinking process" from the "deliverable checklist," ensuring the model doesn't get lost in its own reasoning and forgets to include a "Quick Start" section.