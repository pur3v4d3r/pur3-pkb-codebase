---
title: 🏗️Scaffolds_Socratic-Synthesis-Framework_🆔20251024221323
id: 20251024221348
aliases:
  - prompting
  - prompting/component
  - prompting/🧩prompting-materials-collection
  - 🧩pmc
  - pmc
  - prompting/component/🏗️scaffolds
  - 🏗️scaffolds
type: 🧩component
status: 🗄️archived
priority: ⁉️
created: 2025-10-24T22:13:48
source: 🦖pur3v4d3r
url: "[[gemini-prompt-components]]"
tags:
  - prompt-engineering
  - component
  - prompt-engineering
  - prompt-component-library
  - prompt-component-library
  - component/type/scaffold
  - cognitive-science
description: This is a Prompt-Component, its purpose is to serve as modular pieces that when combined with other component pieces. Will form a high quality prompt.
version: "1.0"
success-rating: ⁉️
---
```component
---
id: prompt-block-🆔20251024221323
---

---

### **THE SOCRATIC SYNTHESIS FRAMEWORK: EXECUTION PROTOCOL**

You will now execute the following phases in sequence. Do not proceed to the next phase until you have completed the current one.

#### **Phase 0: Scoping & Feasibility Analysis**

1.  **Initial Reconnaissance:** Conduct a broad but thorough search of the web for high-quality information (academic papers, reputable long-form articles, key books, expert interviews) related to the **{{TOPIC}}**.
2.  **Assess "Meatiness":** Based on your research, evaluate the topic's depth. Is the **{{WORD_COUNT_TARGET}}** appropriate?
    * If the topic is too niche or lacks sufficient high-quality source material to meet the target, state this clearly and suggest a more realistic word count (e.g., "I recommend a target of 3000-4000 words to maintain depth without resorting to filler.").
    * If the topic is vast, confirm that the target word count is achievable for the requested depth.
3.  **Report Back:** Present your findings from steps 1 and 2. **PAUSE AND WAIT FOR MY APPROVAL** before proceeding to Phase 1. This is our feasibility check.

#### **Phase 1: The Blueprint (Outline Generation)**

1.  **Construct a Detailed Outline:** Based on my approved scope, create a comprehensive, multi-level outline for the document. This outline MUST follow the Socratic Synthesis structure detailed below.
2.  **Structure Definition:**
    * **I. The Premise (Introduction & Foundational Knowledge):** What is this topic at its core?
    * **II. The Exposition (Historical Context & Key Concepts):** Where did this come from? What are the fundamental building blocks I need to know?
    * **III. The Dialectic (Core Tensions & Competing Views):** Where are the debates? What are the different schools of thought or opposing arguments? This is the heart of the paper.
    * **IV. The Application (Real-World Relevance & Case Studies):** Why does this matter? Where can I see this in action?
    * **V. The Synthesis (Broader Implications & Unanswered Questions):** What does this all mean when put together? What are the new questions that emerge from this understanding?
    * **VI. Appendix & Lexicon:** Key Terms, Further Reading.
3.  **Present the Blueprint:** Display the full outline to me. **PAUSE AND WAIT FOR MY APPROVAL** to begin writing. This allows me to suggest adjustments to the structure before you invest time in composition.

#### **Phase 2: The Composition (Drafting the Document)**

Once I approve the blueprint, begin writing the full document. Adhere strictly to these formatting and content guidelines to facilitate my active reading:

1.  **Obsidian-Native Formatting:**
    * Use Markdown for all formatting (`#` for titles, `##` for sections, `###` for sub-sections, `**bold**`, `*italics*`).
    * Identify key concepts and proper nouns that could become future notes and enclose them in `[[double brackets]]`.
    * At the end of the document, include a list of relevant `#tags`.

2.  **Active Reading Integration:** This is critical. You must embed the following elements throughout the document:
    * **Key Questions:** At the beginning of major sections, insert a Markdown callout with a probing question. Format:
        ```markdown
        > [!question] Key Question
        > How did the historical context of the Cold War influence the early formulations of the Fermi Paradox?
        ```
    * **Section Summaries:** At the end of each major section (I, II, III, IV, V), provide a concise summary in a callout. Format:
        ```markdown
        > [!summary] Section Summary
        > This section traced the origins of the concept, establishing the core conflict between the high probability of extraterrestrial life and the lack of observational evidence.
        ```
    * **Connections & Insights:** Where appropriate, create callouts that prompt me to think about connections to other fields or ideas. Format:
        ```markdown
        > [!quote] A Deeper Connection
        > The "Great Filter" hypothesis in the Fermi Paradox shares conceptual DNA with discussions of existential risk in fields like artificial intelligence and climate science. Both explore the idea of universal barriers to long-term survival.
        ```

#### **Phase 3: The Meta-Cognitive Review (Self-Correction)**

Before presenting the final document, you will perform a self-check. You don't need to write out the answers, but you must complete the process. Ask yourself:

1.  **Fidelity to Prompt:** Have I fully addressed every aspect of the user's **{{DESIRED_DEPTH}}** request?
2.  **Structural Integrity:** Does the document flow logically through the Socratic Synthesis phases? Is the balance between sections appropriate?
3.  **Depth over Breadth:** Have I avoided shallow lists of facts and instead focused on explaining relationships, tensions, and implications?
4.  **Active Reading Support:** Are the `[!question]`, `[!summary]`, and `[!quote]` callouts meaningfully placed and thoughtfully written?
5.  **Word Count Adherence:** Is the final document within the agreed-upon word count range?

#### **Phase 4: Final Rendering**

Present the complete, final document as a single, well-formatted Markdown response.

```

## My Original Prompt to Gemini

```prompt

#### Writing Framework Structure

Can you create a framework for a writing structure for a **long-form document that is rich in depth and understanding and goes beyond mere surface details**?

#### Some things I would like to see implemented:

- One that has the AI check for relevant information on the **web**.
    

- I would like the document to give me a **complete** understanding of the topic.
    
- Can you have it so the AI will design this into a markdown and Obsidian note-friendly format?
    
- If you can, can you design it so that it is flexible in that the AI can choose between a range of lengths according to the information available? (There's no sense sending it after a 7500-word paper on something with no real meat.)
    
- Also, can you have the AI design the document with the foresight that **I will be using the technique of active reading during the reading of these documents**?
    
- And I'm not sure about whether we should have the AI do some sort of self-check during the writing process to assess that it's stayed on topic and will meet the required word count(I'll leave the choice of whether to add this in or not up to you because I don't know).
    
- And one more thing, is there any way for the AI to successfully **replicate the results** in future papers with different topics?
    

And again, don't be afraid to dig deep and really put your effort into this; it needs to be something substantial and highly thought out.

```