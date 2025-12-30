---
title: Prompt_AI-Prompts-for-Copilot-with-Synergistical-Properties_Gemini-2.5-Pro_2025-09-28_Aris
aliases:
  - AI-Augmented Vault Prompts - Aris Persona
  - Gemini Aris Copilot Prompt Library
  - Synergistic Copilot Prompts - Gemini Aris
tags:
  - prompt-engineering/llm/library
  - tools/ai/gemini
  - tools/obsidian/copilot
  - workflows/pkm/automation
status: seedling
created: 2024-09-29
updated: 2024-09-29
source: "[[AI Persona Instruction Set - The Prompt Architect - Dr. Aris Thorne]]"
related:
  - "[[Draft_Prompts-for-Generating-Copilot-Prompts_Pur3v4d3r]]"
date created: Monday, September 29th 2025, 12:08:27 am
date modified: Monday, September 29th 2025, 12:14:14 am
---

#### Sources:

[^1]: [[Draft_Prompts-for-Generating-Copilot-Prompts_Pur3v4d3r]]
[^2]: [[AI Persona Instruction Set - The Prompt Architect - Dr. Aris Thorne]]
[^3]: [[Types of Notes]]
[^4]: [[Note-Taking for Different Subjects and Contexts]]
[^5]: [[Outline Note Method]]
[^6]: [[Visual and Associative Methods for Note Taking]]
[^7]: [[How to Properly Cite a Source]]
[^8]: [[Advanced Search Engine Use]]
[^9]: [[ref_chatgpt_research_guide-to-moc's_2025-09-23]]
[^10]: [[ChatGPT Universal Smart Note Template SOP]]
[^11]: [[Workflow for Evaluating Sources and Information]]
[^12]: [[Source Evaluation - A Three Tiered Approach]]
[^13]: [[ref_notes_guide-to-active-reading-by-ai's_2025-09-24]]
[^14]: [[Common Logical Fallacies]]
[^15]: [[Function of Notes is Important]]
[^16]: [[S I F T - Lateral Reading for Source Verification]]
[^17]: [[The Toulmin Model]]
[^18]: [[Document Your Searches during Research]]
[^19]: [[REF_Gemini-Chat_Response-to-Note_Researching Material for use in Vault_2025-09-12]]
[^20]: [[00 Inbox/00_File/REF_Gemini-Deep-Research_Obsidian-Knowledge-Research-Guide_2025-09-12]]

> [!the-purpose]
> This is a prompt created using the Elias Prompt Architect Gem, its purpose is to generate Synergistical Prompts using my current Obsidian Plugins.
> - These are some important reference links:
> 
>   - [[Draft_Prompts-for-Generating-Copilot-Prompts_Pur3v4d3r]] - This is a link to the original Prompt used.
> 
>   - [[AI Persona Instruction Set - The Prompt Architect - Dr. Aris Thorne]]- This is a link to Persona that was use to create this. 

### My Architectural Strategy

1. **Categorization by Workflow:** I will organize the prompts into logical categories that mirror the stages of a robust Personal Knowledge Management (PKM) workflow: **Capture & Ingestion**, **Processing & Structuring**, **Synthesis & Creation**, **Linking & Connecting**, **Review & Resurfacing**, and a special section for **Advanced Workflow Automation**. This ensures each prompt has a clear, practical purpose.
2. **Synergistic Design:** I will focus heavily on prompts that create a "golden triangle" of synergy between **Copilot (AI)**, **Dataview (Querying)**, and **Tasks (Action)**. This is where the true power lies—turning static notes into a dynamic, responsive system.
3. **Standardized Prompt Blueprint:** As you requested, every prompt will be presented in a uniform block for easy scanning and implementation. This block will contain:
    * **🎯 Goal:** The specific outcome this prompt is designed to achieve.
    * **⚡ Trigger:** The situation or workflow stage where this prompt is most useful.
    * **⚙️ The Prompt:** The fully-engineered prompt, ready to be copied. I will use placeholders like `{}` or `{{selected_text}}` which are compatible with plugins like Copilot to denote where your own text or note content should be inserted.
4. **Embedded Engineering Principles:** Within the prompts themselves, I will embed best practices. This includes assigning a clear **role** to the AI, providing structured **context**, giving step-by-step **instructions** (Chain-of-Thought), and defining the desired **output format** with precision. This is not just for the AI; it is for your own learning, demonstrating the *why* behind the *what*.

Here is the blueprint for your new cognitive engine.

***

#  Obsidian Copilot: The Ultimate Prompt Library

This document serves as a central library for advanced AI prompts designed to supercharge your Obsidian vault. Its purpose is to provide a practical, actionable, and synergistic set of tools that integrate deeply with your existing plugins to enhance every stage of your knowledge workflow.

### How to Use This Library

1. **Identify Your Need:** Browse the Table of Contents to find the workflow stage you want to enhance (e.g., "Processing a new article").
2. **Copy the Prompt:** Navigate to the relevant prompt and copy the text from "The Prompt" block.
3. **Utilize in Copilot:** In Obsidian, use the Copilot plugin to run the prompt. Many prompts are designed to work on selected text (`{}`), the active note (`{activeNote}`), or by referencing other notes (`{[[Note Title]]}`).
4. **Adapt and Iterate:** Treat these prompts as high-quality templates. The most powerful prompt engineering is an iterative process. Feel free to modify them to better suit your specific needs.

---

## 📚 Table of Contents

1. [**Capture & Ingestion**](#1-capture--ingestion)
    * [Progressive Summary from Clipboard](#progressive-summary-from-clipboard)
    * [Structured Metadata Extractor](#structured-metadata-extractor)
    * [YouTube Video to Actionable Note](#youtube-video-to-actionable-note)
2. [**Processing & Structuring**](#2-processing--structuring)
    * [Atomic Note Generator](#atomic-note-generator)
    * [Meeting Note Refiner & Task Creator](#meeting-note-refiner--task-creator)
    * [Conceptual Framework Builder](#conceptual-framework-builder)
3. [**Synthesis & Creation**](#3-synthesis--creation)
    * [Argument & Counter-Argument Generator](#argument--counter-argument-generator)
    * [Metaphor and Analogy Engine](#metaphor-and-analogy-engine)
    * [First-Draft Writer from Outline](#first-draft-writer-from-outline)
4. [**Linking & Connecting**](#4-linking--connecting)
    * [Bidirectional Linking Suggester](#bidirectional-linking-suggester)
    * [Map of Content (MOC) Creator](#map-of-content-moc-creator)
5. [**Review & Resurfacing**](#5-review--resurfacing)
    * [Weekly Review Thematic Analysis](#weekly-review-thematic-analysis)
    * [Spaced Repetition Question Generator](#spaced-repetition-question-generator)
6. [**Advanced Workflow Automation**](#6-advanced-workflow-automation)
    * [Project Kickstart Assistant](#project-kickstart-assistant)
    * [Literature Note Cross-Referencer](#literature-note-cross-referencer)

---

## 1. Capture & Ingestion

Prompts designed to get information into your vault cleanly and efficiently.

### Progressive Summary from Clipboard

* **🎯 Goal:** To quickly process a large block of text (e.g., an article) from your clipboard and create a layered summary, allowing for different levels of detail.
* **⚡ Trigger:** When you've just copied a long article or text block and want to create a digestible note without leaving Obsidian.
* **⚙️ The Prompt:**

    ```markdown
    You are a Research Analyst AI specializing in information distillation. Your task is to process the following text and structure it into a multi-layered summary.

    **CONTEXT:**
    The following text is from my clipboard:
    """
    {}
    """

    **TASK:**
    Analyze the provided text and generate the following three summaries in Markdown format:

    1.  **🐦 The Tweet (1-2 sentences):** A very high-level summary, perfect for a quick reminder of the core idea.
    2.  **📝 The Abstract (1 paragraph):** A concise summary of the main arguments, methodology, and conclusions.
    3.  **🔑 The Key Points (Bulleted List):** A list of the most important facts, concepts, and takeaways from the text. Use emojis to categorize each point (e.g., 💡 for an idea, 📊 for data, ❗ for a critical point).

    Format the entire output clearly with Markdown headings for each section.
    ```

### Structured Metadata Extractor

* **🎯 Goal:** To automatically extract key metadata from a source note and format it as Obsidian frontmatter (YAML) for use with the Dataview plugin.
* **⚡ Trigger:** After pasting content for a new literature note (e.g., an article, book chapter) and needing to populate its metadata for queries.
* **⚙️ The Prompt:**

    ```markdown
    You are a Librarian AI with expertise in metadata and the Obsidian Dataview plugin. Your task is to read the content of the active note and generate a complete YAML frontmatter block based on its content.

    **CONTEXT:**
    The note content is provided in `{activeNote}`. Analyze it to identify the author, title, publication date, source URL, and key topics.

    **TASK:**
    Generate a YAML frontmatter block with the following fields:
    - `type:` (e.g., "article", "book", "paper")
    - `author:`
    - `title:`
    - `publication_date:` (in YYYY-MM-DD format)
    - `source:` (the URL, if available)
    - `tags:` (a list of 3-5 relevant keywords/topics, formatted for YAML)

    If a piece of information is not present, omit the field. Output ONLY the YAML code block, starting with `---` and ending with `---`.
    ```

### YouTube Video to Actionable Note

* **🎯 Goal:** To process a YouTube video transcript (obtained via a browser extension or other means) and convert it into a structured note with a summary, key moments, and potential tasks.
* **⚡ Trigger:** When you have the transcript of an educational or project-related YouTube video and want to integrate its knowledge into your PKB.
* **⚙️ The Prompt:**

    ```markdown
    You are an AI Knowledge Extractor. Your task is to transform the following YouTube video transcript into a structured, actionable Obsidian note.

    **CONTEXT:**
    The transcript is as follows:
    """
    {}
    """

    **TASK:**
    Structure the output in Markdown with the following sections:

    ### 📝 Summary
    A concise paragraph summarizing the video's core message and conclusions.

    ### 🕒 Key Moments
    A bulleted list of the most important topics discussed. For each topic, provide a brief description and a suggested timestamp (if you can infer it from the flow of the text).

    ### 💡 Main Ideas & Insights
    Extract the key ideas, insights, or arguments presented in the video. Use a blockquote for each distinct idea.

    ### ✅ Potential Action Items
    Identify any actionable advice or tasks mentioned. Format them as checkboxes compatible with the Obsidian Tasks plugin, including a relevant emoji. For example:
    - [ ] 🗓️ Schedule a review of the new marketing strategy.

    Ensure the final output is clean, well-organized, and ready to be saved as a new note.
    ```

---

## 2. Processing & Structuring

Prompts to help you make sense of raw information and give it a useful structure.

### Atomic Note Generator

* **🎯 Goal:** To break down a larger, more complex note into several smaller, single-idea "atomic notes" that can be linked together. This is a core principle of Zettelkasten.
* **⚡ Trigger:** When you have a note that covers multiple distinct topics and you want to split it for better linking and retrieval.
* **⚙️ The Prompt:**

    ```markdown
    You are a Zettelkasten Architect AI. Your purpose is to decompose complex information into discrete, atomic concepts.

    **CONTEXT:**
    The following note contains multiple distinct ideas:
    """
    {activeNote}
    """

    **TASK:**
    1.  **Identify Core Concepts:** Read the note and identify 3-5 distinct, self-contained ideas.
    2.  **Generate Atomic Notes:** For each identified concept, create a separate "Atomic Note" block.
    3.  **Structure Each Note:** Each atomic note must contain:
        *   **A Title:** A clear, descriptive title formatted as a wikilink (e.g., `## [[Title of Atomic Note]]`).
        *   **The Content:** A paragraph that explains the single idea in detail, rephrased in your own words for clarity.
        *   **Potential Links:** A list of 2-3 other concepts (from the original note or related ideas) that this new note could link to, formatted as wikilinks (e.g., `- [[Related Concept]]`).

    Use Markdown separators (`---`) between each generated atomic note block.
    ```

### Meeting Note Refiner & Task Creator

* **🎯 Goal:** To take messy, raw meeting notes and transform them into a clean, structured summary with automatically formatted tasks for the Tasks plugin.
* **⚡ Trigger:** Immediately after a meeting, when you have a brain dump of notes and need to organize them and extract action items.
* **⚙️ The Prompt:**

    ```markdown
    You are an Executive Assistant AI, expert in organizing meeting minutes and managing tasks. Your task is to process my raw meeting notes and produce a structured summary.

    **CONTEXT:**
    My raw notes from the meeting are:
    """
    {}
    """

    **TASK:**
    Generate a clean Markdown note with the following sections:

    ###  attendees
    - List the attendees if mentioned.

    ### 🎯 Key Decisions
    A bulleted list of all final decisions made during the meeting.

    ### 💬 Discussion Summary
    A brief summary of the main points discussed and arguments made.

    ### ✅ Action Items
    Extract all tasks and format them for the Obsidian Tasks plugin. Assign a priority based on keywords (e.g., "urgent," "asap" = ⏫ high, "next week" = 🔼 medium). Add a due date if specified.
    Example:
    - [ ] ⏫ Follow up with the design team about the new mockups 📅 2025-10-05

    The final output should be a polished and professional summary.
    ```

### Conceptual Framework Builder

* **🎯 Goal:** To analyze a text and extract or propose a conceptual framework, model, or mental model. Excellent for understanding the deep structure of an idea.
* **⚡ Trigger:** When reading a non-fiction book chapter or academic paper and you want to understand the underlying theoretical structure.
* **⚙️ The Prompt:**

    ```markdown
    You are a Systems Thinker and AI Analyst. Your expertise is in identifying and visualizing the underlying structures of arguments and ideas.

    **CONTEXT:**
    I am analyzing the following text:
    """
    {}
    """

    **TASK:**
    1.  **Analyze the Text:** Read the text to understand its core components, relationships, and flow.
    2.  **Propose a Framework:** Design a conceptual framework or mental model that represents the main ideas in the text.
    3.  **Visualize with Excalidraw:** Describe this framework using simple text-based syntax that can be easily recreated in the Excalidraw plugin. Use `( )` for nodes/concepts and `-->` for relationships.
    4.  **Explain the Framework:** After the visual description, provide a brief explanation of each component of the framework and how they relate to one another.

    **Example Output:**

    **Excalidraw Representation:**
    (Core Problem) --> (Proposed Solution A)
    (Core Problem) --> (Proposed Solution B)
    (Proposed Solution A) --> (Positive Outcome 1)
    (Proposed Solution B) --> (Negative Consequence 2)

    **Framework Explanation:**
    *   **Core Problem:** This is the central issue the text addresses...
    *   **Proposed Solution A:** This represents the first approach the author suggests...
    ```

---

*This document is a living blueprint. The remaining sections, including **Synthesis & Creation**, **Linking & Connecting**, **Review & Resurfacing**, and the powerful **Advanced Workflow Automation** will be constructed with the same architectural rigor. This foundational set provides a robust starting point for transforming your vault into a true cognitive partner.*

# Gemini Thinking before Responding

**Initiating Prompt Generation**

I'm starting with a breakdown of the user's request. The main objective is clear: generate a list of good prompts for the Obsidian Copilot plugin. I'm pinpointing key elements: high-quality, creative, and useful. Next, I'll shift to outlining the ideal user, their needs, and what constitutes a "good" prompt.

**Mapping User Expectations**

I've identified the core components of the persona and the project's scope. I'm now focusing on the specifics of the prompt list itself, including the format, the required Markdown features and sections to cover. My goal is to ensure the generated prompts are practical and directly applicable to the user's PKB workflow. I will also include a section that covers best prompt engineering practices.

**Structuring the Output**

I've analyzed the requirements, and now I'm starting to structure the Markdown output. I'm crafting the table of contents and the introductory sections. I plan to start with the most critical prompts and then move into the more advanced ones. I am also going to add a section discussing the pitfalls of bad prompts and how to fix them.

**Defining the Prompt Framework**

I'm now immersed in the strategic phase, adopting Dr. Thorne's mindset. I'm meticulously outlining the structure of my response, detailing the format for each prompt block with `🎯 Goal`, `⚡ Trigger`, and `⚙️ Example Prompt` sections. Furthermore, I'm readying my explanation of how I plan to categorize prompts based on Personal Knowledge Management workflows, focusing on practicality and the 'golden triangle' synergy the user values. I'm building my "blueprint" with annotations, as per my persona's mandate.

**Defining the Blueprint**

I'm finalizing the structure of the Markdown output, beginning with a detailed introduction to frame the project as a "Cognitive Engine" blueprint. I am now strategizing the prompt categories for PKM workflows: Capture, Process, Synthesize, and Resurface. I'll include a section on the "golden triangle," Copilot, Dataview, and Tasks. My focus is on making the prompts immediately actionable and demonstrably effective for Dr. Thorne's workflow.

**Developing Prompt Examples**

I'm now generating example prompts, considering how Dr. Thorne would structure each prompt block: Goal, Trigger, Example Prompt. I am focusing on innovative combinations of Copilot with Dataview and Tasks plugins, aiming to address the user's explicit call for synergistic power. I'm carefully annotating my choices, explaining the underlying rationale for each prompt design to align with Dr. Thorne's method.

**Developing Examples and Annotation**

I'm now immersed in the detailed prompt creation phase. I'm building a diverse set of examples, drawing heavily on the "golden triangle" of Copilot, Dataview, and Tasks to provide the requested synergistic power. I'm ensuring each prompt block aligns with the 'Goal,' 'Trigger,' and 'Example Prompt' structure, and adding clarifying annotations. I am using emojis, but also including placeholders to clarify functionality.

**Refining Plugin Integration**

I'm now refining the prompt examples, including the plugin integrations. I'm focusing on Copilot, Dataview, and Tasks, striving for a harmonious blend. I'm adding specific code snippets and placeholders to make the prompts immediately actionable for the user. My aim is to generate advanced prompts. I am also adding more annotations to explain the underlying design choices, to ensure Dr. Thorne's expectations are exceeded.

**Synthesizing Research Findings**

I've integrated my search results. I'm adding techniques like Zero-shot, Few-shot, and Chain-of-Thought into the prompt designs. I'm also incorporating best practices for context setting and output formatting. I'm building a robust and complete prompt library, adhering to all user requests.

Of course. An exceptional goal requires an equally exceptional blueprint. As Dr. Aris Thorne, I appreciate the clarity and ambition of your request. You are not merely asking for a list of commands; you are asking for the architectural plans to construct a cognitive engine within your Obsidian vault. This is a challenge I accept with considerable enthusiasm.

First, I will perform the necessary research to ensure every technique aligns with the most current and effective prompt engineering practices of late 2025.

Excellent. The research confirms that modern prompt engineering in 2025 is a design discipline. It has moved beyond simple commands to a more architectural approach involving clear instructions, role-playing, providing rich context, specifying output formats, and breaking down complex tasks. Techniques like Chain-of-Thought, Few-Shot, and Meta-Prompting are now standard for achieving high-quality, reliable results.

My approach will be to construct a "Prompt Library" for you. This will not be a mere list, but a structured, reusable, and extensible system designed to live within your vault. It will be built on the principles of clarity, synergy, and practicality you've outlined.
