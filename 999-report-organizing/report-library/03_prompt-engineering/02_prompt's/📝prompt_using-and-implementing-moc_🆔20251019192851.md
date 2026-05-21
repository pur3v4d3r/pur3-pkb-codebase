---
title: 📝Prompt_Using-and-Implementing-Moc_🆔20251019192851
id: 20251019192902
aliases:
  - prompt-engineering
  - prompting
  - prompt
  - prompts
type: 📝prompt
status: ⚡active
priority: ⁉️
created: 2025-10-19T19:29:02
source: gemini-2.5-pro
url: ⁉️
tags:
  - prompt-engineering
  - prompt-engineering
  - type/prompt
  - type/prompt
description: This is an experiment to see how well this framework can be executed and to what degree. I chose to use this style of message (Multi-turn) in order to test out how well it works.
version: "1.0"
success-rating: 🔍⁉️needs-review
---
```prompt
---
id: prompt-block-🆔20251019192851
---

### **Phase I: Constraint & Task Definition**

**1. System Role (The Constraint Setter)**

You are to operate under the following global constraints for this entire operation:
- **Persona**: Act as an expert academic researcher specializing in Personal Knowledge Management (PKM) and advanced Obsidian methodologies.
- **Tone**: Maintain a formal, educational, and comprehensive tone. The output is a definitive guide intended for personal study.
- **Core Objective**: The user's goal is to generate a report that serves as a personal guide on how to build effective, useful, and highly professional MOCs within their Obsidian PKB.
- **Mandatory Output Formatting**:
    - The final deliverable must be a single, coherent report of approximately **3500 words**.
    - The report must be formatted in **Markdown**, structured with elements optimized for viewing inside Obsidian (e.g., headings, lists, blockquotes, callouts).   
    - The final output must begin with a **YAML front matter** block containing metadata such as `title`, `author`, `date`, `tags`, and `aliases`.

---

### **Phase II: Orchestration & Execution**

**2. Conductor LLM (The Architect/Orchestrator)**

Your first task is to architect the research and generation process.

- **Action**: Receive the grand task: "Generate a 3500-word comprehensive report on designing, building, and employing Maps of Content (MOCs) in an Obsidian-based PKB."
- **Decomposition Strategy**: Employ a **Tree-of-Thoughts (ToT)** approach.
    1. Generate a detailed, multi-level outline for the report. This outline is your reasoning path. It must logically progress from foundational concepts to advanced implementation.
    2. From this outline, generate a series of specific, targeted tasks to delegate to the Expert LLMs.
    3. Hold this master outline. You will use it in the final synthesis stage to assemble the report.

**3. Expert LLM (The Specialized Researcher) - RAG Enabled**

Execute the following singular research tasks delegated by the Conductor. For each task, perform a deep-dive search, critically analyze the findings for relevance and utility, and synthesize the information into a detailed summary.

- **Delegated Task 1: Foundational Principles**: Research the origin, core philosophy, and purpose of MOCs, particularly referencing foundational thinkers in the PKM space like Nick Milo.
- **Delegated Task 2: Structural Design**: Research and detail the primary methods for designing and structuring MOCs. Include analysis of top-down vs. bottom-up creation, hierarchical vs. non-hierarchical structures, and the concept of "MOCs of MOCs."
- **Delegated Task 3: Practical Implementation**: Research the technical steps for building MOCs in Obsidian. This must include Markdown syntax (linking, embedding), best practices for note transclusion, and the role of key community plugins like Dataview and Breadcrumbs in automating and enhancing MOCs.
- **Delegated Task 4: Use Cases & Examples**: Find and describe various types of MOCs and their specific use cases (e.g., Project MOCs, Thematic MOCs, Daily Note MOCs, Source MOCs). Provide illustrative examples where possible.

**4. Expert LLM (The Specialized Researcher) - Contradiction**

Your task is to inject critical nuance and challenge the primary narrative.

- **Delegated Task**: Research and draft a section addressing the potential pitfalls, limitations, and common criticisms of the MOC methodology. Compare and contrast MOCs with alternative organizational systems (e.g., the structure of a pure Zettelkasten, the Johnny.Decimal system) and argue for scenarios where these alternatives might be more suitable.

---

### **Phase III: Synthesis & Validation**

**5. Conductor LLM (Synthesis and Formatting)**

You will now re-assume the role of the Architect to finalize the report.

- **Action**:
    1. Collect the synthesized research from the RAG-Enabled Expert and the counter-argument from the Contradiction Expert.
    2. Using your master outline from Step 2, meticulously assemble these components into a single, cohesive report. Ensure smooth transitions between sections.
    3. Rigorously enforce all global constraints defined by the System Role in Step 1. Pay close attention to the **3500-word count** and **Obsidian-centric Markdown formatting**.
    4. Insert the YAML front matter block at the very beginning of the document.
    5. Perform a final validation check for logical flow, factual accuracy, and grammatical errors.
- **Goal**: Deliver the final, validated, and properly formatted academic report, ready for immediate use in the user's PKB.

```

# Expirement-001_Prompting-Gemini-to-use-the_AMP-F_to create-a-new-prompt

> [!the-mission]
> 
## Message 01

```
This is going to be the start of a multi-turn based operation.
You will need to remember this information/conversations for this chat window.```
```

## Message 02

```
I'm going to be giving you a series of information.
Your end goal is to generate an engineered prompt using the specifications I will give you.
- Keep this in mind when you are review everything.
	- Start to formulate ideas for its conception while review the information.
	  
- **Note:**The framework isnt meant for this type of assignment. However, I want you to try and do your best. Just fill in and fix the parts that dont fit, with the relevant information.

*My next message will be the framework you are to use for this engineered prompt.*
```

## Message 03

```
I want you to take this, The Agentic Meta-Prompting Framework (AMP-F), and use it to re-engineer the rough-draft I'm will give to you.

**This is the AMP-F (The Framework)**
## The Agentic Meta-Prompting Framework (AMP-F)

1. **System Role (The Constraint Setter)**
    - **Action:** Establishes non-negotiable global constraints (Persona, Tone, Citation Style, Mandatory Output Formatting).
    - **Goal:** Define the operating environment and scholarly non-negotiables.
2. **Conductor LLM (The Architect/Orchestrator)**
    - **Action:** Receives the complex task, decomposes it, and employs the **Tree-of-Thoughts (ToT)** strategy.
    - **Goal:** Plan the reasoning path, oversee the process, and maintain the final coherent structure.
3. **Expert LLM (The Specialized Researcher) - RAG Enabled**
    - **Action:** Executes highly specific, singular tasks delegated by the Conductor, primarily **Retrieval Augmented Generation (RAG)** lookups.
    - **Goal:** Access the external, verified knowledge base to ensure factual grounding and mitigate hallucination.
4. **Expert LLM (The Specialized Researcher) - Contradiction**
    - **Action:** Executes singular tasks like drafting an opposing viewpoint or counter-argument.
    - **Goal:** Proactively inject conceptual nuance and challenge the primary narrative.
5. **Conductor LLM (Synthesis and Formatting)**
    - **Action:** Synthesizes the outputs from the Expert Agents and applies the mandated final structure (Markdown + YAML Front Matter).
    - **Goal:** Ensure the output is immediately ready for Phase III Validation.
```

## Message 2

```
*This is the rough-draft prompt I want you to use the framework to engineer.*
*Go over this information carefully.*

### GOAL
Generate a report that reviews **MOCs (Maps of Content)** for Obsidian.
*Its purpose is to be used as guidance, to educate myself, on How to build effective, useful, and highly professional MOCs.*
This will be used in my PKB (Personal Knowledge Base) in Obsidian, so the report needs to be **created with visual and structures that are becoming to Obsidian based PKBs.**

### Grand Task

1. Read over and review this prompt, **carefully.**
2. **Immediately** re-read this prompt again. This time thinking of ways to accomplish the task.
3. Upon completion of your second read through of the prompt, implement your online search function/research function.
4. Conduct a deep dive, researching this topic, on How to design, build, and employ the use of **MOCs** inside a PKB in Obsidian.
5. **Critically analyze** all the information you find for its usefulness.
	- Anything that can aid you in the generation of this report.
6. After researching enough material for a **3500 word report**, stop.
7. Take all the information you collected during your research phase, and compile it together, construct an **outline** of the report you will generate.
8. Review this outline for any errors in **reasoning, useless information, Etc.**
9. After completion of the review, take the time to fix anything you need to with the report's outline.
	-  *Be rigorous, in making sure it's ready to be used to generate the final report.*
10. Using the information collected during your research, my prompt, and your outline, generate a comprehensive academic report educating me on the uses and implementation of **MOCs** inside Obsidian based PKBs.
11. Finalize the report and check it for any errors.
12. Deliver the finalized report.
```

# Chat Log

*Message 01: Is entered into the chatbot.*
> [!gemini-pro-response]
> "Okay, I will keep track of our conversation in this chat window. I'm ready when you are."

*Message 02: Is entered into the chatbot.*

> [!gemini-pro-response]
> "Got it. I will keep all the information you provide in this chat session in mind to build the engineered prompt. I'm ready for the framework. I'll start thinking about how to structure the prompt as you provide the details."

*Message 03: Is entered into the chatbot.*

> [!gemini-pro-response]
> "Framework received. I understand the structure of the Agentic Meta-Prompting Framework (AMP-F) and the roles of the System Role, Conductor LLM, and the two Expert LLMs."
> 
> "I will use this five-step process to re-engineer the rough draft you provide. I am ready for the draft."
> 

*Message 04: Is entered into the chatbot.*

> [!gemini-pro-response]
> "Of course. I have analyzed your rough draft and the Agentic Meta-Prompting Framework (AMP-F). Here is the re-engineered prompt designed to produce your report on Maps of Content (MOCs) for Obsidian."
>