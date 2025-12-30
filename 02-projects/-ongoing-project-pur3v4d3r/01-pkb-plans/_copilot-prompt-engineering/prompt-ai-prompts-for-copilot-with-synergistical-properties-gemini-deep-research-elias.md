---
title: Prompt_AI-Prompts-for-Copilot-with-Synergistical-Properties_Gemini-Deep-Research_Elias
aliases:
  - AI-Augmented Vault Prompts
  - Gemini Deep Research Copilot Prompt Library
  - Synergistic Copilot Prompts - Gemini Deep Research
tags:
  - prompt-engineering/llm
  - tools/ai/gemini
  - tools/obsidian/copilot
  - workflows/pkm/automation
status: seedling
created: 2024-09-29
updated: 2024-09-29
source: "[[AI Persona Instruction Set -  Elias, the Prompt Architect]]"
related:
  - "[[Draft_Prompts-for-Generating-Copilot-Prompts_Pur3v4d3r]]"
date created: Sunday, September 28th 2025, 11:34:38 pm
date modified: Monday, September 29th 2025, 12:19:55 am
---

#### Sources:

[^1]: [[Draft_Prompts-for-Generating-Copilot-Prompts_Pur3v4d3r]]
[^2]: [[AI Persona Instruction Set -  Elias, the Prompt Architect]]
[^3]: [[Types of Notes]]
[^4]: [[Note-Taking for Different Subjects and Contexts]]
[^5]: [[Outline Note Method]]
[^6]: [[ref_chatgpt_research_guide-to-moc's_2025-09-23]]
[^7]: [[Visual and Associative Methods for Note Taking]]
[^8]: [[How to Properly Cite a Source]]
[^9]: [[Advanced Search Engine Use]]
[^10]: [[ChatGPT Universal Smart Note Template SOP]]
[^11]: [[00 Inbox/00_File/REF_Gemini-Deep-Research_Obsidian-Knowledge-Research-Guide_2025-09-12]]
[^12]: [[Workflow for Evaluating Sources and Information]]
[^13]: [[Source Evaluation - A Three Tiered Approach]]
[^14]: [[ref_notes_guide-to-active-reading-by-ai's_2025-09-24]]
[^15]: [[The SQ3R Active Reading Method]]
[^16]: [[Common Logical Fallacies]]
[^17]: [[Document Your Searches during Research]]
[^18]: [[Function of Notes is Important]]
[^19]: [[Active Vs Passive Processing in Notes]]
[^20]: [[The Toulmin Model]]

> [!the-purpose]
> This is a prompt created using the Elias Prompt Architect Gem, its purpose is to generate Synergistical Prompts using my current Obsidian Plugins.
> - These are some important reference links:
> 
>   - [[Draft_Prompts-for-Generating-Copilot-Prompts_Pur3v4d3r]] - This is a link to the original Prompt used.
> 
>   - [[AI Persona Instruction Set -  Elias, the Prompt Architect]] - This is a link to Persona that was use to create this. 

# The AI-Augmented Vault: A Master Reference of Synergistic Copilot Prompts for the Advanced Obsidian User

## Introduction: Architecting Intelligence in Your Obsidian Vault

This document serves as a master reference for the advanced Obsidian practitioner—the PKM Systems Architect and AI Integration Specialist. It is not a mere list of prompts; it is a strategic guide for architecting intelligence within a knowledge vault. The central thesis is the elevation of an AI assistant like Copilot from a content generator to an intelligent orchestration layer. This layer translates natural language intent into precise, executable actions across a synergistic stack of community plugins. The prompts contained herein are designed to solve concrete PKM challenges by leveraging this powerful paradigm, transforming your vault from a passive repository of information into a dynamic, responsive knowledge system. To fully harness this potential, three core operational concepts must be understood.

### The Code as Output Paradigm

The most profound shift in leveraging AI within Obsidian is moving from generating human-readable prose to generating machine-executable code. The true synergy between Copilot and the specified plugin stack emerges when the AI's primary output is not text to be read, but a syntactically perfect script or query to be executed by another plugin. This transforms the act of prompting from "writing" into a form of "declarative programming" for one's PKM system.

For instance, instead of asking Copilot to "list my urgent projects," one instructs it to "generate a Dataview query that creates a table of all notes tagged '#project' where the 'status' field is not 'complete' and the 'due' date is within the next seven days, sorted by due date." The output is not a static list but a dynamic, self-updating Dataview code block. Similarly, a prompt can instruct Copilot to generate a complex JavaScript snippet utilizing the

`ExcalidrawAutomate` API to visualize a process, effectively turning a textual description into a programmatic diagram. This approach delegates the cognitive load of remembering complex syntax (DQL, JavaScript, etc.) to the AI, allowing the user to operate at a higher level of abstraction, focusing on intent rather than implementation.

### The Structured Data Contract

The plugins within an advanced Obsidian vault do not operate in isolation; they form an ecosystem bound by an implicit "data contract." The effectiveness of this system hinges on the consistency and integrity of the data flowing between its components. A Dataview query that searches for tasks due today is rendered useless if the tasks are not formatted in a way the Tasks plugin and Dataview can parse. A query that aggregates data from daily notes will fail if the Periodic Notes plugin is not configured to create files with a predictable naming convention and folder structure.

The prompts in this reference are engineered to make Copilot a powerful enforcer of this data contract. It can be instructed to act as an "ETL" (Extract, Transform, Load) engine for your knowledge. It can extract unstructured information from a meeting transcript, transform it into a structured format with Linter-compliant YAML frontmatter and Dataview-compatible inline fields, and load it into a new note. By ensuring that all data, whether captured or generated, adheres to the vault's established standards, Copilot guarantees the interoperability and reliability of the entire plugin-driven system.

### The Semantic Formatting Layer

In an AI-augmented vault, formatting transcends aesthetics; it becomes a method for embedding machine-readable meaning directly into the content. Callouts, for example, are no longer just colored boxes. When used with a consistent schema, such as `[!summary]`, `[!decision]`, or `[!risk]`, they become semantic containers that structure information for both human cognition and future machine processing. The Callout Manager plugin further enhances this by allowing the creation of a custom, vault-specific semantic language.

A raw text summary from an AI is of limited value, as it requires the user to perform the subsequent cognitive step of parsing and categorization. The prompts in this guide instruct Copilot to perform this step itself. A prompt might ask the AI to "analyze this article, place the main thesis in a `[!thesis]` callout, list supporting arguments in a `[!arguments]` callout, and identify counterarguments in a `[!critique]` callout." This pre-processing transforms a flat document into a structured object. The resulting note is not only easier for a human to scan but is also structured for more precise future queries, analysis, and synthesis by either the user or another AI-driven process.

## Plugin Synergy Matrix

This matrix provides a high-level overview of the inter-plugin synergies explored in this document. It serves as a map to the possible integrations, allowing for non-linear navigation based on the desired combination of tools.

|**Core Plugin**|**Information Capture**|**Note Processing**|**Project Management**|**Creative Ideation**|**Vault Maintenance**|
|---|---|---|---|---|---|
|**Dataview**|Generates DQL to find untriaged notes.|Creates summary tables from note metadata.|Generates dynamic project dashboards & reports.|Creates tables of related concepts for brainstorming.|Generates DQL to find notes missing metadata.|
|**Tasks**|Extracts action items into `[due::]` formatted tasks.|Identifies implicit tasks in prose and formats them.|Creates structured task breakdowns for new projects.|Generates checklists for creative processes.|Finds and reformats non-standard task entries.|
|**Periodic Notes**|Populates daily notes with captured items for review.|Summarizes weekly activity for weekly review notes.|Populates daily notes with today's project tasks.|Seeds daily notes with creative prompts.|N/A|
|**Quick Add**|N/A|Formats text for batch processing via QuickAdd macros.|Generates structured data for QuickAdd project templates.|N/A|Generates instructions for a QuickAdd capture macro.|
|**Callout Manager**|Structures captured content using semantic callouts.|Refactors notes into structured callout-based summaries.|Formats project updates within `[!update]` callouts.|Organizes brainstormed ideas into custom callouts.|Wraps linting reports in `[!lint-report]` callouts.|
|**Highlighter**|Highlights key terms and entities in captured text.|Identifies and highlights inconsistencies in notes.|Highlights overdue tasks or critical path items.|Highlights novel ideas or keywords in generated text.|N/A|
|**Excalidraw**|N/A|Generates `ExcalidrawAutomate` script to visualize note links.|Generates `ExcalidrawAutomate` script for Gantt/timeline charts.|Generates `ExcalidrawAutomate` script for mind maps/flowcharts.|N/A|
|**Linter**|Generates content that pre-emptively conforms to Linter rules.|Reformats existing notes to match Linter standards.|Creates project notes with Linter-compliant YAML.|N/A|Generates custom regex rules for the Linter plugin.|

Export to Sheets

## Table of Contents

- (#section-1-information-capture--triage)
    
    - (#prompt-11-the-universal-triage-processor)
        
    - (#prompt-12-atomic-note-deconstructor-from-lecture)
        
- (#section-2-note-processing--synthesis)
    
    - (#prompt-21-generate-a-dynamic-moc-from-note-metadata)
        
    - Prompt 2.2: Visualizing Note Connections with Excalidraw
        
    - (#prompt-23-refactor-prose-into-a-structured-dataview-table)
        
- (#section-3-dynamic-project-management)
    
    - (#prompt-31-generate-a-full-project-plan-from-a-brief)
        
    - (#prompt-32-draft-a-weekly-project-status-report)
        
- (#section-4-creative-ideation--visualization)
    
    - (#prompt-41-generate-a-mind-map-from-brainstormed-list)
        
    - (#prompt-42-generate-a-flowchart-from-process-description)
        
- (#section-5-vault-maintenance--quality-control)
    
    - (#prompt-51-generate-a-notes-needing-attention-dashboard)
        
    - (#prompt-52-generate-custom-regex-rules-for-linter)

---

## Section 1: Information Capture & Triage

_Objective: To streamline the process of capturing raw, unstructured information and transforming it into well-structured, actionable notes that conform to the vault's "data contract."_

### Prompt 1.1: The Universal Triage Processor

#### Objective

To process a block of unstructured text (e.g., meeting transcript, web clipping, voice note transcription) and transform it into a standardized, structured, and actionable note that is immediately integrated into the vault's PKM system.

#### Plugin Synergy

- **Copilot:** Performs the core analysis, summarization, extraction, and formatting.
    
- **Tasks:** All identified action items are formatted using the Dataview-compatible inline field syntax (e.g., ``, `[priority:: high]`), making them instantly queryable.
    
- **Callout Manager:** The output is semantically structured using a predefined set of custom callouts (e.g., `[!summary]`, `[!decision]`, `[!open-question]`), which makes the note highly scannable and organizes information by its function.
    
- **Highlighter:** Key entities, names, project codes, and dates are marked with the standard Markdown `==highlight==` syntax for visual emphasis.
    
- **Linter:** The generated YAML frontmatter is constructed to be pre-emptively compliant with vault-wide Linter rules, ensuring consistency from the moment of creation.
    

#### The Master Prompt

```
Act as a PKM Triage Specialist for Obsidian. Your task is to process the following unstructured text and transform it into a highly structured, actionable note. Adhere strictly to the following formatting rules:

1. **YAML Frontmatter:**
    
    - Generate a `---` delimited YAML block at the very top.
        
    - Include `type: "meeting-note"` (or `clipping-note`, `fleeting-note` as appropriate).
        
    - Include `status: "triage"`.
        
    - Include `created: "YYYY-MM-DDTHH:mm"`.
        
    - Extract the source URL or context and add it as `source: "URL or Context"`.
        
    - Identify and add relevant tags (e.g., `tags: [project/alpha, team/engineering]`).
        
2. **Semantic Structure using Callouts:**
    
    - **`[!summary]`:** A concise, one-paragraph summary of the entire text.
        
    - **`[!participants]`:** A bulleted list of all mentioned participants, formatted as `[[wikilinks]]`.
        
    - **`[!decisions]`:** A numbered list of key decisions made.
        
    - **`[!open-questions]`:** A bulleted list of unresolved questions or topics for follow-up.
        
3. **Action Items (Tasks Plugin Integration):**
    
    - Create a section titled `## Action Items`.
        
    - Extract every actionable task.
        
    - Format each task as a standard Obsidian task: `- [ ] Task description`.
        
    - If a deadline is mentioned, append ``.
        
    - If a person is assigned, add their wikilink `[[Person Name]]`.
        
    - If urgency is implied (e.g., "ASAP", "critical"), append `[priority:: high]`. Otherwise, use `[priority:: medium]`.
        
4. **Highlighting:**
    
    - Throughout the entire generated note (within callouts and tasks), enclose all project names, key terms, specific dates, and monetary values in `==highlight==`.
        

Process the following text:

```
""" [Paste unstructured text here] """`

#### How It Works

This prompt operates as a multi-stage processing pipeline. It instructs the AI to not just understand the content, but to categorize and format it according to a strict schema.

1. **Deconstruction:** The AI first reads the entire text to understand the context, identify participants, locate decisions, and flag action items.
    
2. **Extraction & Categorization:** It then performs targeted extractions based on the prompt's rules. It pulls out names for the `participants` callout, firm commitments for the `decisions` callout, and unresolved issues for the `open-questions` callout.
    
3. **Transformation & Formatting:** This is the critical step where synergy occurs. The AI transforms the extracted information into the required formats. Actionable statements become Tasks-plugin compatible list items. Key entities are wrapped in highlight syntax. A compliant YAML block is synthesized from the content.
    
4. **Assembly:** Finally, the AI assembles these formatted components into a single, cohesive Markdown note, ready for insertion into the vault.
    

#### Example Usage

**Input Text:** `"Okay team, quick sync on Project Phoenix. Alice, Bob, and I met. We decided to go with the new cloud provider, effective next Monday, which is the 21st. Bob needs to get the final contract signed by this Friday, that's super important. Alice, can you prepare the migration plan? Let's aim to have a draft by the end of the month. I'm also not clear on the budget impact, we need to circle back on that."`

**AI Output:**

## `--- type: "meeting-note" status: "triage" created: "2024-07-15T10:30" source: "Project Phoenix Sync" tags: [project/phoenix, team/engineering]

> [!summary] A sync meeting for ==Project Phoenix== where the team decided to switch to a new cloud provider. Key tasks were assigned for contract signing and migration planning, with an open question remaining about the budget.

> [!participants]
> 
> - [[Alice]] -]
> 
> - [[User Name]]

> [!decisions]
> 
> 1. The team will proceed with the new cloud provider, starting ==2024-07-21==.

> [!open-questions]
> 
> - What is the overall budget impact of this decision?

## Action Items

- [ ]] to get the final contract signed [due:: 2024-07-19][priority:: high]
    
- [ ][[Alice]] to prepare the draft migration plan [due:: 2024-07-31][priority:: medium]`
    

#### Customization & Iteration

- **Custom Callouts:** Modify the callout types in the prompt (e.g., `[!risks]`, `[!next-steps]`) to match your custom callouts defined in the Callout Manager plugin.
    
- **YAML Schema:** Adjust the YAML fields (`type`, `status`, etc.) to align with your vault's metadata standards and Dataview queries.
    
- **Task Metadata:** Add or change the default task metadata. For example, you could add `` or a custom field like `[effort:: low]`.
    

### Prompt 1.2: Atomic Note Deconstructor from Lecture

#### Objective

To analyze a long-form, monolithic text (such as a lecture transcript or a detailed article) and deconstruct it into a series of smaller, interconnected atomic notes, each focusing on a single core concept.

#### Plugin Synergy

- **Copilot:** Identifies the distinct, self-contained concepts within the source text and generates the content, title, and metadata for each new atomic note.
    
- **Quick Add:** The final output is formatted as a structured list that can be processed by a QuickAdd macro. This bypasses manual file creation, allowing for the batch generation of multiple notes from a single command. This leverages QuickAdd's scripting and macro capabilities to automate vault operations.
    
- **Linter:** The generated YAML for each prospective note is designed to be Linter-compliant, often including a standard set of tags (e.g., `#atomic`, `#source/lecture-name`) to ensure immediate organizational consistency.
    

#### The Master Prompt

```
`Act as a Knowledge Architect for Obsidian. Your task is to analyze the following long-form text and deconstruct it into 3-5 distinct, atomic notes. Each atomic note must focus on a single, core, self-contained concept.

For your final output, generate a single Markdown code block containing a list of these potential notes. For each note in the list, provide the following, precisely in this format:

- **Filename:** A concise, descriptive filename in kebab-case (e.g., `the-concept-of-cognitive-load.md`).
    
- **YAML:** A valid YAML block containing:
    
    - `title:` The full, human-readable title of the note.
        
    - `tags:` An array including `atomic` and a relevant subject tag (e.g., `psychology/learning`).
        
    - `source:` A wikilink to the original source note (e.g., `]`).
        
- **Content:** A 2-3 sentence summary of the core concept.
    
- **Links:** A bulleted list of wikilinks to the other atomic notes you have identified in this process. This creates the initial web of connections.
    

Here is an example structure for a single note entry:
```

### Filename: concept-name.md

## **YAML:**

## title: Concept Name tags: [atomic, subject/area] source:]

**Content:** This is the concise summary of the single core concept. It explains the idea in isolation.

**Links:**

- [[other-concept-1]]
    
- [[other-concept-2]]
    

#### How It Works

This prompt guides the AI through a process of conceptual analysis and structured output generation, designed specifically for automation.

1. **Conceptual Chunking:** The AI first reads the source text to identify the primary themes or ideas. The instruction to find "3-5 distinct, atomic notes" guides it to look for logical breaks and self-contained arguments.
    
2. **Abstraction and Summarization:** For each identified "chunk," the AI synthesizes the information into a concise summary (the `Content`) and devises a descriptive title and filename.
    
3. **Interlinking:** Crucially, after identifying all the concepts, the AI establishes the relationships between them, generating the list of `[[wikilinks]]` for each note. This step is vital for creating a connected web of thought rather than a folder of isolated files.
    
4. **Structured Formatting:** The AI then formats this entire analysis into a single, machine-parsable block. The use of clear headings (`### Filename`, `**YAML:**`, etc.) is intentional, as it makes it easy for a QuickAdd JavaScript macro to parse this text, loop through each entry, and execute the `app.vault.create()` command with the provided filename and content.
    

#### Example Usage

**Input Text (Abridged):** `"...Cognitive Load Theory suggests that working memory is limited. There are three types: intrinsic, which is the inherent difficulty of the topic; extraneous, which is the unnecessary mental work created by how information is presented; and germane, which is the effort dedicated to building schemas. Effective instructional design aims to minimize extraneous load to free up resources for germane load..."`

**AI Output:**

`### Filename: cognitive-load-theory-overview.md

## **YAML:**

## title: Cognitive Load Theory Overview tags: [atomic, psychology/learning] source:]

**Content:** Cognitive Load Theory posits that human working memory is a limited resource for processing new information. Learning is optimized when the cognitive load imposed by instructional materials is managed effectively.

**Links:**

- [[types-of-cognitive-load]]
    
- [[managing-extraneous-load]]

---

### Filename: types-of-cognitive-load.md

## **YAML:**

## title: The Three Types of Cognitive Load tags: [atomic, psychology/learning] source:]

**Content:** Cognitive load is categorized into three types. Intrinsic load is the inherent complexity of the material. Extraneous load is generated by non-optimal instructional design. Germane load is the productive effort of schema construction and learning.

**Links:**

- [[cognitive-load-theory-overview]]
    
- [[managing-extraneous-load]]

---

### Filename: managing-extraneous-load.md

## **YAML:**

## title: Managing Extraneous Cognitive Load tags: [atomic, psychology/learning] source:]

**Content:** The primary goal of effective instructional design is to minimize extraneous cognitive load. This frees up working memory capacity, allowing the learner to dedicate more mental resources to germane load, which is directly related to understanding and schema formation.

**Links:**

- [[cognitive-load-theory-overview]]
    
- [[types-of-cognitive-load]]`
    

#### Customization & Iteration

- **QuickAdd Macro:** This prompt's output is designed to be the input for a custom QuickAdd macro. The user must create a JavaScript file that parses this specific text structure to create the notes.
    
- **YAML Fields:** The YAML structure can be expanded to include other standard fields, such as `aliases` or a `status` field, by simply adding them to the prompt's template.
    
- **Number of Notes:** The user can adjust the "3-5" constraint to encourage the AI to be more or less granular in its deconstruction, depending on the density of the source material.

---

## Section 2: Note Processing & Synthesis

_Objective: To leverage AI to analyze, refactor, and synthesize information from existing notes, deepening understanding and revealing hidden connections._

### Prompt 2.1: Generate a Dynamic MOC from Note Metadata

#### Objective

To create a dynamic, self-updating Map of Content (MOC) note by generating sophisticated Dataview queries that automatically collate and organize notes based on their metadata (tags, folders, YAML fields).

#### Plugin Synergy

- **Copilot:** Acts as a Dataview Query Language (DQL) expert, translating a user's natural language request for a MOC into precise, functional, and well-formatted DQL code.
    
- **Dataview:** Executes the AI-generated queries within the MOC note, rendering live, interactive tables and lists that reflect the current state of the vault.
    
- **Callout Manager:** The generated DQL code blocks can be wrapped in descriptive, foldable callouts, making the MOC clean, organized, and easy to navigate.
    

#### The Master Prompt

```
`Act as an Obsidian Dataview expert. I need to create a Map of Content (MOC) note for a specific topic. Your task is to generate the complete Markdown for this MOC, including explanatory text and multiple advanced Dataview queries.

The MOC should be about: ****

Generate the MOC with the following structure:

1. **Introduction:** A brief, one-paragraph introduction to the topic of the MOC.
    
2. **Core Concepts (Table View):**
    
    - Create a foldable callout `> [!abstract]- Core Concepts`
        
    - Inside, generate a Dataview `TABLE` query.
        
    - The table should list notes tagged with `#ai/concepts` OR `#pkm/concepts`.
        
    - Display the following columns:
        
        - The note's file link (as "Concept").
            
        - The `summary` field from the note's YAML (as "Summary").
            
        - The `file.mtime` (as "Last Modified").
            
    - Sort the table by `file.mtime` in descending order.
        
3. **Projects & Case Studies (Grouped List View):**
    
    - Create a foldable callout `> [!example]- Projects & Case Studies`
        
    - Inside, generate a Dataview `LIST` query.
        
    - The query should find all notes in the `"Projects/AI"` folder OR tagged `#casestudy`.
        
    - It must filter out any notes with `status: "archived"` in their YAML.
        
    - Use `GROUP BY` to group the results by the `project-type` YAML field.
        
4. **Unprocessed Fleeting Notes (Task View):**
    
    - Create a foldable callout `> [!todo]- Triage Queue`
        
    - Inside, generate a Dataview `TASK` query.
        
    - The query should find all incomplete tasks located in notes with the YAML field `status: "triage"` AND the tag `#ai`.
        

For each Dataview query, add a short sentence of commentary directly above the code block explaining what it does.`
```

#### How It Works

This prompt exemplifies the "Code as Output" paradigm by treating the AI as a specialized programmer.

1. **Intent Translation:** The user provides a high-level topic. The AI translates this intent into specific metadata markers (`#ai/concepts`, `"Projects/AI"` folder, etc.) that are likely to exist in a well-organized vault.
    
2. **DQL Generation:** The AI constructs the DQL queries using advanced features. It knows to use `TABLE` for structured data display, `LIST` with `GROUP BY` for categorized views, and `TASK` for actionable items. It correctly applies
    

    `FROM`, `WHERE`, `SORT`, and custom column aliasing (`AS "Header"`) to meet the prompt's requirements.

    
3. **Structural Formatting:** The AI wraps the queries in foldable callouts, a best practice for complex dashboards. This creates a clean user interface where details can be progressively disclosed, preventing the user from being overwhelmed by long lists of results upon opening the note.
    
4. **Annotation:** The inclusion of commentary for each query is a crucial feature. It makes the MOC not just a tool, but a learning resource, helping the user understand the DQL they are using and empowering them to modify it later.
    

#### Example Usage

**User Input:** The user replaces `` with "My Research on Quantum Computing". They adjust the tags and folders to match their vault structure (e.g., `#quantum/concepts`, `"Research/Quantum"`).

**AI Output (Abridged):**

`# MOC: Quantum Computing Research

This Map of Content serves as a central hub for all notes, projects, and resources related to my research on Quantum Computing. It dynamically updates as new notes are added and existing ones are modified.

> [!abstract]- Core Concepts This table lists the fundamental concepts in my quantum computing research, sorted by the most recently modified. dataview TABLE summary AS "Summary", file.mtime AS "Last Modified" FROM #quantum/concepts SORT file.mtime DESC

> [!example]- Projects & Experiments This list shows active projects and experiments, grouped by their type (e.g., simulation, literature review).

> [!todo]- Triage Queue These are unprocessed tasks from fleeting notes related to quantum computing that require attention.

#### How It Works

This prompt is a powerful demonstration of AI-driven automation, translating semantic structure into visual geometry.

1. **Semantic Parsing:** The AI reads the provided note content not just as text, but as a structure of ideas. It identifies a main theme, key supporting terms, and explicit connections (wikilinks).
    
2. **API Mapping:** It maps these identified semantic elements to specific `ExcalidrawAutomate` API calls. The central topic becomes a styled `ea.addRect()`. Concepts become `ea.addText()` elements. Wikilinks become `ea.addEllipse()` elements. Relationships become `ea.connectObjects()` calls.
    
3. **Algorithmic Layout:** The prompt guides the AI to perform a simple algorithmic layout task. By specifying positions (e.g., semi-circles above and below a central point), it forces the AI to calculate coordinates for each element, resulting in an organized, readable diagram rather than a random scattering of nodes.
    
4. **Code Generation:** The final output is a complete, ready-to-execute script. A user can paste this into a Templater template, and upon insertion, it will instantly draw the concept map in the active Excalidraw file.
    

#### Example Usage

**Input Note Content:** `"## The Zettelkasten Method. The Zettelkasten method is a knowledge management system focused on creating a network of atomic notes. The core principles are atomicity (one idea per note) and dense linking. This facilitates emergent insights by connecting ideas in novel ways. It was popularized by [[Niklas Luhmann]]. See also [[Evergreen Notes]]."`

**AI Output (Abridged JavaScript):**

#### Customization & Iteration

- **Layout Algorithms:** Experiment with different layout instructions. Ask the AI to arrange nodes in a "top-down hierarchy" or a "hub-and-spoke model."
    
- **Styling:** Add more specific styling instructions to the prompt, such as changing `ea.style.strokeColor`, `ea.style.roughness`, or `ea.style.fontFamily` for different node types.
    
- **Data Source:** Instead of pasting note content, this prompt could be adapted to work on the output of a DataviewJS query, allowing for the visualization of relationships between multiple notes.
    

### Prompt 2.3: Refactor Prose into a Structured Dataview Table

#### Objective

To convert an unstructured paragraph or list of prose describing multiple items (e.g., book summaries, project updates, product comparisons) into a clean, structured Markdown table that uses Dataview inline fields, making the information instantly queryable.

#### Plugin Synergy

- **Copilot:** Performs the natural language understanding to parse the prose, extract key attributes for each item, and reformat the data into a Markdown table.
    
- **Dataview:** The generated table is immediately machine-readable by Dataview because the AI is instructed to use the `Key:: Value` inline field syntax within the table cells. This transforms static text into a live data source.
    
- **Linter:** The prompt can enforce consistent formatting for the table headers and alignment, adhering to Markdown best practices that the Linter plugin can check.
    

#### The Master Prompt

```
`Act as a Data Structuring Specialist for Obsidian. Your task is to convert the following block of unstructured prose into a structured Markdown table.

The table should have the following columns:

- **Item**
    
- **Status**
    
- **Owner**
    
- **Key Takeaway**
    

For the content within the cells, you must adhere to these formatting rules:

1. The "Item" column should contain the name of the item, formatted as a `[[wikilink]]` if possible.
    
2. The "Status" column must contain ONLY the status value, formatted as a Dataview inline field. Example: `Status:: In Progress`.
    
3. The "Owner" column must contain the assigned person's name, formatted as a Dataview inline field with a wikilink. Example: `Owner::]`.
    
4. The "Key Takeaway" column should contain a concise summary of the item's description.
    

Here is the prose to convert:

```
""" [Paste unstructured text here] """`

#### How It Works

This prompt automates the tedious process of data normalization, enforcing the "Structured Data Contract" on pre-existing, messy information.

1. **Entity Recognition:** The AI reads the prose and identifies the distinct items being discussed. For each item, it then looks for associated attributes like a status, a person responsible, and a description.
    
2. **Attribute Mapping:** It maps the identified attributes to the specified table columns. For example, it recognizes "is on track" as `Status:: In Progress` and "John is handling it" as `Owner::]`.
    
3. **Syntax Injection:** This is the key step. The AI doesn't just place the text in the table; it wraps the relevant data points in the `Key:: Value` syntax. This injection of syntax is what makes the output machine-readable and unlocks the synergy with Dataview.
    
4. **Table Generation:** Finally, it assembles the extracted and formatted data into a standard, Linter-friendly Markdown table.
    

#### Example Usage

**Input Text:** `"Okay, for the Q3 initiatives: the 'New User Onboarding' project is on track and is being led by]. The main point is to simplify the signup flow. The 'API Documentation Overhaul' is currently blocked, and] is waiting for feedback from the product team. We need to document the new endpoints. Lastly, the 'Mobile App Redesign' is complete, [[Maria Garcia]] finished it last week. It's a total visual refresh."`

**AI Output:**

`| Item | Status | Owner | Key Takeaway |

|---|---|---|---| | [[New User Onboarding]] | Status:: On Track | Owner::] | Simplify the user signup flow. | |] | Status:: Blocked | Owner::] | Needs feedback to document new endpoints. | |] | Status:: Complete | Owner:: [[Maria Garcia]] | A complete visual refresh has been implemented. |`

This output table can now be queried from other notes. For example, a query on Sarah Chen's personal page like `TABLE file.link as Initiative, Status FROM "Projects" WHERE Owner =]` would now correctly pull in the "New User Onboarding" project.

#### Customization & Iteration

- **Column Schema:** The power of this prompt lies in its customizability. Define any set of columns relevant to your data (e.g., `Priority`, `DueDate`, `Budget`).
    
- **Data Types:** Instruct the AI to format other data types as inline fields, such as dates (`DueDate:: 2024-08-01`) or numbers (`Budget:: 5000`).
    
- **Source Flexibility:** This prompt can be adapted for a wide range of inputs, from meeting notes and email summaries to product reviews and literature comparison notes.

---

## Section 3: Dynamic Project Management

_Objective: To automate the creation, tracking, and reporting of projects within Obsidian, using AI to bridge the gap between planning and execution._

### Prompt 3.1: Generate a Full Project Plan from a Brief

#### Objective

To take a high-level, natural language project brief and instantly generate a comprehensive, well-structured project plan note that is pre-populated with tasks, metadata, and semantic sections.

#### Plugin Synergy

- **Copilot:** Analyzes the brief, brainstorms a work breakdown structure, and generates the entire Markdown content for the project plan.
    
- **Tasks:** The generated work breakdown structure is a nested list of tasks, with dependencies (`[id::...]`, `[dependsOn::...]`) and placeholder due dates (``) formatted for the Tasks plugin and Dataview.
    
- **Callout Manager:** The document is structured using custom project management callouts like `[!goals]`, `[!scope]`, `[!stakeholders]`, and `[!risks]`, making the plan easy to read and parse.
    
- **Linter:** The generated YAML frontmatter is designed to be compliant with established project note standards (e.g., `type: project`, `status: planning`), ensuring consistency across the vault.
    

#### The Master Prompt

```
`Act as a Senior Project Manager using Obsidian. Your task is to create a comprehensive project plan note based on the following project brief.

The output must be a single, complete Markdown note adhering to this structure:

1. **YAML Frontmatter:**
    
    - `title:` The project title.
        
    - `type: project`
        
    - `status: planning`
        
    - `manager:` "]"
        
    - `tags: [project]`
        
    - `created: YYYY-MM-DD`
        
2. **Project Overview Section:**
    
    - Use a `> [!goals]` callout to list the primary objectives of the project (2-3 bullet points).
        
    - Use a `> [!scope]` callout to define what is in-scope and out-of-scope.
        
    - Use a `> [!stakeholders]` callout to list key stakeholders as `[[wikilinks]]`.
        
3. **Work Breakdown Structure (WBS):**
    
    - Create a `## Work Breakdown Structure` heading.
        
    - Generate a detailed, nested list of tasks required to complete the project. Use at least three phases (e.g., Phase 1: Research, Phase 2: Development, Phase 3: Launch).
        
    - Format every item as an Obsidian task (`- [ ]`).
        
    - For major milestone tasks, add a unique ID: `[id:: phase1-complete]`.
        
    - For tasks that depend on a milestone, use `[dependsOn:: phase1-complete]`.
        
    - Assign placeholder due dates to key deliverables in the format ``.
        
4. **Risks & Mitigation:**
    
    - Create a `## Risk Assessment` heading.
        
    - Use a `> [!warning]- Potential Risks` foldable callout to list 2-3 potential risks identified from the brief.
        

Here is the project brief:

```
""" [Paste project brief here] """`

#### How It Works

This prompt automates the administrative overhead of starting a new project, allowing the user to move directly to refinement and execution.

1. **Brief Ingestion:** The AI parses the user's brief, extracting the project's name, core goals, and any mentioned stakeholders or deliverables.
    
2. **Conceptual Expansion:** Based on the brief, the AI uses its general knowledge of project management to brainstorm a logical work breakdown structure. It infers typical phases and tasks associated with the type of project described.
    
3. **Structured Generation:** The AI then populates the predefined template. It fills in the callouts with summarized information, builds the nested task list, and injects the correct Tasks plugin syntax for IDs and dependencies. This enforces the "Structured Data Contract" from the project's inception.
    
4. **Semantic Formatting:** The use of callouts provides immediate visual structure, separating the project's "why" (goals, scope) from its "how" (WBS), which aligns with the "Semantic Formatting" principle.
    

#### Example Usage

**Input Brief:** `"We need to launch a new marketing website for our product, 'FusionCRM'. The goal is to increase lead generation by 20%. It needs to be live by the end of Q3. The marketing team, led by], will provide the content. The web dev team, managed by me, will build it."`

**AI Output:**

## `--- title: New Marketing Website for FusionCRM type: project status: planning manager: "]" tags: [project, marketing] created: 2024-07-15

> [!goals]
> 
> - Launch a new marketing website for the 'FusionCRM' product.
> 
> - Increase qualified lead generation by 20% within the first quarter post-launch.
> 
> - Go live by the end of Q3.

> [!scope] **In-Scope:**
> 
> - Full redesign and development of the public-facing website.
> 
> - Integration with the existing lead capture system. **Out-of-Scope:**
> 
> - A new backend CRM system.
> 
> - Internationalization (launching in English only).

> [!stakeholders] -] (Marketing Lead) -] (Development Lead)

## Work Breakdown Structure

- **Phase 1: Discovery & Planning**
    
    - [ ] Finalize sitemap and user flows [due:: 2024-07-31]
        
    - [ ] Marketing to deliver final copy and assets [due:: 2024-08-15][id:: content-ready]
        
- **Phase 2: Development & Implementation**
    
    - [ ] Develop front-end templates [dependsOn:: content-ready]
        
    - [ ] Implement CMS and integrate lead capture forms
        
    - [ ] Milestone: Development Complete [due:: 2024-09-15][id:: dev-complete]
        
- **Phase 3: Testing & Launch**
    
    - [ ] Conduct QA and cross-browser testing [dependsOn:: dev-complete]
        
    - [ ] Deploy to production environment
        
    - [ ] Final Launch [due:: 2024-09-30]
        

## Risk Assessment

> [!warning]- Potential Risks
> 
> - **Content Delays:** Marketing team providing content later than the deadline could impact the development timeline.
> 
> - **Technical Debt:** Unforeseen issues with the existing lead capture system could complicate integration.`

#### Customization & Iteration

- **Project Templates:** This prompt can be saved as a template itself (e.g., in Templater). The user can then have different versions for different types of projects (e.g., "Software Project Plan," "Research Project Plan") with different phases and callouts.
    
- **Task Granularity:** Adjust the prompt to ask for a more or less detailed WBS depending on the project's complexity.
    
- **Custom YAML:** Add more project-specific YAML fields like `budget`, `priority`, or `team-members`.
    

### Prompt 3.2: Draft a Weekly Project Status Report

#### Objective

To semi-automate the creation of a weekly project status report by generating a note that includes AI-written summaries alongside dynamic Dataview queries that pull in real-time progress data.

#### Plugin Synergy

- **Copilot:** Generates the natural language summary of the week's progress and, critically, generates the DQL queries needed to pull the supporting data.
    
- **Dataview:** Executes the generated queries to list all tasks completed and notes modified within the project's scope during the past week, providing objective evidence for the report.
    
- **Periodic Notes:** The prompt is designed to be run within a Weekly Note. It leverages the file's title or creation date to automatically set the date ranges for the Dataview queries, making the report context-aware.
    
- **Callout Manager:** The report is structured with callouts like `[!summary]` for the AI's narrative and `[!data]` for the Dataview-generated lists, separating subjective analysis from objective data.
    

#### The Master Prompt

```
`Act as a Project Coordinator preparing a weekly status report in Obsidian. The report is for the project: **[[Project Name]]**.

This report is being generated inside my weekly note for the week of ****. Use this context to set the date ranges for all queries.

Generate a Markdown report with the following sections:

1. **Executive Summary:**
    
    - Create a `> [!summary]` callout.
        
    - Inside, write a 2-3 sentence summary of the project's status. Mention overall progress (on-track, delayed, etc.), key accomplishments this week, and any new blockers. Base this summary on the data that will be pulled by the queries below.
        
2. **Accomplishments This Week:**
    
    - Create a `> [!done]- Completed Tasks` foldable callout.
        
    - Explain that this section lists all tasks related to the project that were completed in the past 7 days.
        
    - Generate a Dataview `TASK` query that finds all completed tasks from the folder `"Projects/ProjectFolder"` (or notes tagged `#project/name`) WHERE the `completion` date is within the last 7 days.
        
3. **Active Work & Documents:**
    
    - Create a `> [!info]- Modified Notes` foldable callout.
        
    - Explain that this lists all project documents that were actively worked on this week.
        
    - Generate a Dataview `LIST` query that finds all notes from `"Projects/ProjectFolder"` (or tagged `#project/name`) WHERE `file.mtime` is within the last 7 days.
        
4. **Upcoming Priorities:**
    
    - Create a `## Next Week's Focus` section.
        
    - Generate a bulleted list of 2-3 key priorities for the upcoming week, inferred from the project's goals and the tasks that are not yet complete.`
        
```

#### How It Works

This prompt creates a powerful hybrid workflow, combining AI's summarization capabilities with Dataview's real-time data retrieval.

1. **Contextual Awareness:** The prompt explicitly tells the AI its context (a specific project, a specific week). This allows the AI to tailor its output, particularly the date ranges in the DQL. It understands that "this week" means `date(today) - dur(7 days)`.
    
2. **Data-Driven Summary:** The AI is instructed to write its summary _based on the data the queries will pull_. This forces a more grounded and accurate narrative. It effectively "pre-runs" the queries in its own context to inform the summary.
    
3. **"Code as Output" for Data:** The AI generates the precise DQL needed to surface the objective facts: what was finished, and what was worked on. This saves the user from having to write these queries manually each week.
    
4. **Forward-Looking Synthesis:** The final section requires the AI to synthesize information and make reasonable projections about future priorities, demonstrating a higher level of analysis than simple data retrieval.
    

#### Example Usage

**User Input:** The user runs this prompt in their weekly note `2024-W29.md`, replacing `[[Project Name]]` with `]` and the project folder with `"Projects/FusionCRM"`.

**AI Output:**

`## Weekly Status Report:] - Week 29

> [!summary] Progress on the FusionCRM Website is on-track. This week saw the completion of the initial planning phase, with final copy and assets delivered by marketing. The development team has begun work on the front-end templates. No new blockers were identified.

> [!done]- Completed Tasks This section lists all tasks for the FusionCRM Website project that were completed in the past 7 days. dataview TASK FROM "Projects/FusionCRM" WHERE completion >= date(today) - dur(7 days)

> [!info]- Modified Notes This lists all project documents that were actively worked on this week.

## Next Week's Focus

- Begin implementation of the CMS and lead capture forms.
    
- Conduct initial review of the front-end templates with the marketing team.
    
- Finalize the QA and testing plan.
    

#### How It Works

This prompt offloads the complex tasks of layout calculation and programmatic drawing to the AI.

1. **Structural Interpretation:** The AI's first task is to parse the indentation of the bulleted list to understand its parent-child relationships. This is a classic tree-structure problem.
    
2. **Geometric Translation:** The core of the prompt is instructing the AI to translate this logical tree into a geometric layout. The instruction to use "trigonometric functions" and a "radial" layout is a specific technical hint that guides the AI towards a common and effective algorithm for mind map generation.
    
3. **API-Specific Code Generation:** The AI then generates the JavaScript, making precise calls to the `ExcalidrawAutomate` API. It creates elements, assigns them IDs, calculates their positions, styles them, and then connects them, following the logic derived from the list.
    
4. **Executable Output:** The final script is a self-contained program. When run via Templater, it executes the entire sequence of operations, resulting in a complete, well-organized mind map appearing in a new tab, often in less time than it would take to draw the central topic manually.
    

#### Example Usage

**Input:** The user provides the nested list as shown in the master prompt.

**AI Output (Conceptual JavaScript):**

#### Customization & Iteration

- **Diagram Type:** Modify the prompt to create different diagrams from the same list data. Ask for a "top-down organizational chart" or a "left-to-right horizontal tree."
    
- **Styling Details:** Provide more granular styling instructions. For example: "Make the arrows connecting to 'Capture' nodes red" or "Use a dashed line for 'Organize' sub-branches."
    
- **Input Format:** Adapt the prompt to parse other structured text formats, such as a Markdown table or a numbered outline.
    

### Prompt 4.2: Generate a Flowchart from Process Description

#### Objective

To translate a natural language description of a sequential process, including conditional logic (if/then/else), into a formal, standards-compliant flowchart diagram in Excalidraw.

#### Plugin Synergy

- **Copilot:** Performs advanced natural language processing to understand the logical flow, decision points, and outcomes described in the text. It then translates this logic into an `ExcalidrawAutomate` script.
    
- **Excalidraw:** Executes the script to render the flowchart, using different shapes for different types of steps (rectangles for processes, diamonds for decisions) as programmatically defined by the AI.
    
- **Templater / Quick Add:** Serves as the execution environment for the generated JavaScript.
    

#### The Master Prompt

```
`Act as an expert` ExcalidrawAutomate` script developer. Your task is to create a JavaScript script that generates a flowchart based on a procedural text description.

The script must adhere to these rules:

1. **Initialization:** Start with `const ea = ExcalidrawAutomate;` and `ea.reset();`.
    
2. **Shape Conventions:**
    
    - Use `ea.addRect()` for process steps.
        
    - Use `ea.addDiamond()` for decision points (e.g., "if/else" statements).
        
    - Use `ea.addEllipse()` for start and end terminators.
        
3. **Logical Flow:**
    
    - Analyze the text to identify the sequence of steps and the conditional branches.
        
    - Lay out the diagram in a top-down manner.
        
    - For decision points, create two branching paths (e.g., a "Yes" path and a "No" path).
        
4. **Connections:**
    
    - Use `ea.connectObjects()` to connect all elements with straight arrows (`roughness: 0`).
        
    - For the arrows coming from a decision diamond, add text labels ("Yes" / "No") to the arrows.
        
5. **Rendering:**
    
    - Use `await ea.create({onNewPane: true, filename: "Process Flowchart"});` to generate the drawing.
        

Generate ONLY the JavaScript code, enclosed in a `javascript` block. Use the following process description:

""" The process starts with a user submitting a form. First, we validate the input. If the input is invalid, we show an error message and the process ends. If the input is valid, we save the data to the database. After saving, we send a confirmation email to the user. Then the process ends. """
```

#### Customization & Iteration

- **Complex Logic:** Test the AI with more complex logic, including nested if-statements or loops ("Repeat steps A and B until condition C is met").
    
- **Swimlanes:** For processes involving multiple actors, instruct the AI to create a swimlane diagram by grouping nodes for each actor within larger bounding boxes.
    
- **Styling:** Request specific colors for different paths (e.g., "Color the 'success' path green and the 'error' path red").

---

## Section 5: Vault Maintenance & Quality Control

_Objective: To employ AI as a vigilant assistant for maintaining vault hygiene, enforcing standards, and identifying inconsistencies._

### Prompt 5.1: Generate a "Notes Needing Attention" Dashboard

#### Objective

To create a centralized maintenance dashboard note that uses a series of Dataview queries to automatically identify files across the vault that are missing required metadata or otherwise fail to meet quality standards.

#### Plugin Synergy

- **Copilot:** Acts as a DQL generator, translating high-level descriptions of vault standards (e.g., "all project notes must have a manager") into precise and effective Dataview queries.
    
- **Dataview:** Executes the queries to dynamically generate lists of non-compliant notes, creating a live "to-do" list for vault maintenance.
    
- **Callout Manager:** Each Dataview query is wrapped in a descriptive, foldable callout, which keeps the dashboard clean, organized, and easy to use. The user can expand only the sections they wish to address.
    

#### The Master Prompt

```
`Act as an Obsidian Vault Maintainer. I need to create a "Vault Health Dashboard" note. Your task is to generate the complete Markdown for this dashboard.

The dashboard should identify several common types of incomplete or non-standard notes using Dataview queries. Each query must be placed inside its own foldable callout.

Generate the dashboard with the following sections:

1. **Notes Missing Status:**
    
    - Create a callout: `> [!check]- Notes Missing a 'status' YAML field`
        
    - Inside, generate a Dataview `LIST` query that finds all notes in the vault that do NOT have the `status` field in their YAML frontmatter (`WHERE!status`). Exclude notes in the "Templates" folder.
        
2. **Untriaged Fleeting Notes:**
    
    - Create a callout: `> [!todo]- Untriaged Fleeting Notes`
        
    - Inside, generate a Dataview `LIST` query that finds all notes with `status: "triage"` in their YAML.
        
3. **Projects Without a Manager:**
    
    - Create a callout: `> [!warning]- Projects Missing a Manager`
        
    - Inside, generate a Dataview `TABLE` query that finds all notes with `type: "project"` in their YAML but are missing the `manager` field (`WHERE type = "project" AND!manager`). Show the `file.mtime` as "Last Modified".
        
4. **Notes Without Tags:**
    
    - Create a callout: `> [!info]- Notes Without Any Tags`
        
    - Inside, generate a Dataview `LIST` query that finds all notes where the number of tags is zero (`WHERE length(file.tags) = 0`). Exclude notes in the "Templates" and "Assets" folders.
        
5. **Stubs/Empty Notes:**
    
    - Create a callout: `> [!bug]- Stub Notes (less than 50 words)`
        
    - Inside, generate a DataviewJS query that lists all notes where the content length is less than 50 words.`
        
```

#### How It Works

This prompt automates the creation of a powerful diagnostic tool for any Obsidian vault.

1. **Standardization Rules:** The prompt defines a set of quality standards in plain English (e.g., notes must have a status, projects must have a manager).
    
2. **DQL Translation:** Copilot translates each of these rules into the corresponding DQL. It correctly uses negation (`!status`) , chained conditions (
    

    `WHERE type = "project" AND!manager`) , and functions (

    

    `length(file.tags)`) to build the queries.

    
3. **Advanced Query Generation:** For the "Stub Notes" rule, the prompt specifically asks for a DataviewJS query, demonstrating the ability to request more advanced code when DQL is insufficient. The AI would generate a `dv.pages()` script that filters based on `file.content.length`.
    
4. **Dashboard Assembly:** The AI assembles these queries into the final note, using the specified callouts to create a clean, organized, and user-friendly interface for vault maintenance tasks.
    

#### Example Usage

**User Input:** The user runs the prompt as is.

**AI Output:**

`# Vault Health Dashboard

This dashboard dynamically identifies notes that may require attention or are missing key metadata.

> [!check]- Notes Missing a 'status' YAML field dataview LIST FROM!"Templates" WHERE!status

> [!todo]- Untriaged Fleeting Notes

> [!warning]- Projects Missing a Manager

> [!info]- Notes Without Any Tags

> [!bug]- Stub Notes (less than 50 words)


