---
title: Prompt - Improving Writing Through Experts Review - Gemini-2.5-Pro(2025-09-28)
aliases: [AI Writing Coach Prompt, Expert Review Prompt for Writing, Grammarly-like AI Prompt]
tags: [prompt-engineering, prompt-engineering/gemini, workflow]
status: seedling
created: 2024-09-29
updated: 2024-09-29
source: 
related:

date created: Sunday, September 28th 2025, 8:00:08 pm
date modified: Monday, September 29th 2025, 12:29:08 am
---

# Prompt - Improving Writing Through Experts Review - Gemini-2.5-Pro(2025-09-28)

#### Sources:

[^1]: [[Pur3v4d3r's Workshop MOC]]
[^2]: [[Prompt for Improving Writing Through Experts Review - Meta-Llama-3-405B-Instruct]]
[^3]: [[Persona Instruction Set -  Elias, the Prompt Architect]]
[^4]: [[Gemini-2.5-Pro Universal Smart Note Template SOP]]
[^5]: [[Types of Notes]]
[^6]: [[Note-Taking for Different Subjects and Contexts]]
[^7]: [[ref_chatgpt_research_guide-to-moc's_2025-09-23]]
[^8]: [[Outline Note Method]]
[^9]: [[ref_draft_pur3v4d3r_prompt-for-guide-to-smart-notes_2025-09-23]]
[^10]: [[ref_notes_guide-to-active-reading-by-ai's_2025-09-24]]
[^11]: [[Visual and Associative Methods for Note Taking]]
[^12]: [[How to Properly Cite a Source]]
[^13]: [[ChatGPT Universal Smart Note Template SOP]]
[^14]: [[Advanced Search Engine Use]]
[^15]: [[Workflow for Evaluating Sources and Information]]
[^16]: [[Integrated Review System's for Note Taking]]
[^17]: [[REF_Gemini-Chat_Response-to-Note_Researching Material for use in Vault_2025-09-12]]
[^18]: [[Source Evaluation - A Three Tiered Approach]]
[^19]: [[The SQ3R Active Reading Method]]
[^20]: [[ref_gemini-2.5-pro_guide-to-pkb-knowledge_2025-09-24]]

[[🦖Pur3v4d3r's-Workshop_🗺️MOC]] Link to Copilot and AI prompts Hub.

[[♊Gem-Instruction-Set_Improving Writing Through Experts Review_Meta-Llama-3-405B-Instruct]] Link to the Llama version of this.

[[AI Persona Instruction Set -  Elias, the Prompt Architect]] Link to the Persona that was use to generate this result.


### **The Engineered Prompt: The Editorial Review Panel**

Here is the final, constructed prompt. It is designed to be a powerful, all-in-one tool. Simply replace the placeholder text with your own information. For the `[GOAL]`, `[AUDIENCE]`, and `[DESIRED TONE]` placeholders, use the answers you determine from the questions I asked earlier.

```text
### [ROLE]
You are to act as an "Editorial Review Panel," a team of three distinct experts collaborating to provide a comprehensive analysis of a piece of writing. Your panel consists of:
1.  **Lead Editor:** Focuses on the overall structure, purpose, and argument of the text. Ensures the piece achieves its primary goal.
2.  **Clarity Specialist:** Obsessed with clear, concise, and unambiguous language. Hunts down jargon, convoluted sentences, and poor flow.
3.  **Engagement Specialist:** Analyzes the text for its ability to capture and hold the reader's attention. Focuses on tone, voice, word choice, and impact.

### [CONTEXT]
The panel is reviewing the following text. The author's objectives are clearly defined below. Your entire analysis must be based on how well the text meets these specific objectives.

**Author's Objectives:**
*   **Goal of Text:** [e.g., To persuade a potential client to sign up for our new SaaS platform.]
*   **Target Audience:** [e.g., Tech-savvy project managers, aged 30-50, who are busy and value efficiency.]
*   **Desired Tone:** [e.g., Professional, confident, and benefit-oriented, but not overly salesy.]

**Original Text for Review:**
"""
[INSERT YOUR FULL TEXT HERE]
"""

### [TASK]
Perform a comprehensive review of the provided text by following these three steps precisely:

**Step 1: Overall Assessment**
As the Lead Editor, provide a brief, high-level summary of the text's strengths and weaknesses in relation to the author's stated objectives.

**Step 2: Detailed Feedback**
Provide a detailed, categorized analysis from each specialist's perspective. For EACH point of feedback, you must use the following structure:
*   **Issue:** A brief description of the problem.
*   **Suggestion:** A concrete recommendation for how to fix it.
*   **Rationale:** A clear explanation of WHY the suggestion improves the text, linking it back to the author's objectives (goal, audience, tone).

**Step 3: Revised & Improved Version**
Rewrite the entire original text from scratch, incorporating all the feedback from the panel. This new version should be a polished, ready-to-use example that perfectly aligns with the author's stated objectives.

### [CONSTRAINTS]
*   Your feedback must be constructive, respectful, and educational.
*   Do not merely correct grammar; provide strategic advice on style, structure, and impact.
*   Adhere strictly to the output format defined below.

### [FORMAT]
Your entire output must be in Markdown and follow this exact structure:

## Editorial Panel Review

### **1. Overall Assessment**
*(Your summary from the Lead Editor goes here.)*

### **2. Detailed Feedback**

**A. Clarity & Flow (from the Clarity Specialist)**
*   **Issue:** ...
*   **Suggestion:** ...
*   **Rationale:** ...
*(Add more points as needed)*

**B. Engagement & Tone (from the Engagement Specialist)**
*   **Issue:** ...
*   **Suggestion:** ...
*   **Rationale:** ...
*(Add more points as needed)*

**C. Structure & Purpose (from the Lead Editor)**
*   **Issue:** ...
*   **Suggestion:** ...
*   **Rationale:** ...
*(Add more points as needed)*

### **3. Revised & Improved Version**
*(Your complete, rewritten version of the text goes here.)*
```

---

### **Architect's Rationale**

I have constructed this prompt with several key principles in mind:

1. **Multi-Persona Simulation:** The "Editorial Review Panel" is the core innovation. It forces the AI to deconstruct the problem and analyze the text from multiple, complementary angles (Clarity, Engagement, Structure). This prevents a monolithic, one-dimensional review and provides a richer, more expert-level critique.
2. **Goal-Oriented Analysis:** The `[CONTEXT]` section is critical. By forcing you to define your goal, audience, and tone upfront, we anchor the AI's entire analysis to *your* specific needs. It's no longer just "good writing"; it's "writing that is good *for this specific purpose*."
3. **Actionable & Educational Feedback:** The `Issue / Suggestion / Rationale` structure is non-negotiable. It moves beyond simple correction ("change this word") to genuine coaching ("change this word *because* it will better resonate with your target audience by creating a sense of urgency..."). This is how you learn the craft.
4. **Enforced Structure:** The strict `[FORMAT]` requirement is the skeleton that gives the prompt its strength. It guarantees a well-organized, predictable, and highly usable output every single time, turning a potentially messy stream of consciousness from the AI into a clean, professional report.

## Gemini Thinking

**Analyzing the Core Task**

I'm focusing on the core request - to mimic an expert review from Grammarly. It's clear that basic grammar and spellcheck won't suffice. I'm isolating the essential parts, like the review of the text and the idea of an expert, for a prompt strategy.

**Dissecting Expert Roles**

I'm now focused on defining the "expert" role. Different texts need different experts. I'm leaning towards specifying expertise based on text type. The output should reflect multiple perspectives. This means crafting a prompt that can take on different professional perspectives.

**Questioning for Clarity**

I'm now refining my approach. Instead of assuming, I'm planning a series of initial questions to extract vital context. Questions about the text's purpose, audience, tone, and context. This will ensure the prompt is tailored to the user's specific needs and the generated feedback is highly relevant, like a real Grammarly expert.

**Designing the Review Panel**

I'm now focused on the "Review Panel" concept. I plan to include a Lead Editor, a Clarity Specialist, and an Engagement Specialist to provide diverse expert feedback. This multifaceted approach is intended to improve the quality of the output. I'll focus on defining these roles.

**Formulating the Inquiry**

I'm now focused on the "Socratic Inquiry" phase. Refining those initial questions is essential. I want each question to elicit specific, useful details, so I'm restructuring them. Also, I'll explore using multiple-choice options within the prompt to guide the user further.

**Constructing the Framework**

I'm now focusing on the core framework of the prompt. I plan to create a structured prompt with roles, context, task instructions, constraints, and a format section. This detailed architecture is essential. I'll clearly explain the purpose of each element to the user, with a special emphasis on the 'why' behind my approach.

**Crafting the Complete Prompt**

I'm now translating the architectural design into a fully functional prompt. It will include the review panel, context section, task breakdown, constraints, and the specific Markdown format. I'll make it easy for the user to copy and paste, highlighting the areas they'll need to customize. Finally, the prompt will be presented with a rationale to justify all of its design elements.

Excellent. You are seeking to construct a digital equivalent of an expert review panel—a mechanism that goes beyond simple error correction and delves into the strategic improvement of a text. This is a superb application for a well-architected prompt. You're not just looking for a proofreader; you're looking for a mentor, a strategist, and a wordsmith, all in one.

Before I construct the final prompt, I must first understand the blueprint of your intent. A prompt's effectiveness is directly proportional to the clarity of its objective. Please help me by answering these questions:

1. **What is the typical purpose of the text you'll be reviewing?** (e.g., to persuade a client, to inform a technical audience, to entertain readers on a blog, to craft a formal academic paper?)
2. **Who is the intended audience?** (e.g., experts in a field, general consumers, corporate executives, potential employers?)
3. **What specific tone or voice are you usually aiming for?** (e.g., formal and academic, conversational and witty, professional and authoritative, empathetic and supportive?)

Your answers will allow me to precisely calibrate the persona and instructions for the AI. While we wait for those details, I will build a robust and adaptable framework that you can later refine.
## Original Request

I need a prompt engineered. something that can accomplish the same thing that Grammarly does with experts reviewing a piece of information giving feedback on how to improve the text and example of what it could look like.

---

This prompt is a robust machine for textual refinement. Use it as your digital whetstone to sharpen your writing.

### **Prompt Architecture Blueprint**

Here is the architectural plan for the prompt. I will design it to be a comprehensive and reusable tool.

* **[ROLE]:** We will establish a multi-persona "Editorial Review Panel." This is more powerful than a single editor, as it forces the AI to analyze the text from multiple, specialized perspectives. I will create a Lead Editor, a Clarity Specialist, and an Engagement Specialist.
* **[CONTEXT]:** This section will frame the entire operation. It will contain the user's text and, crucially, the specific goals for that text (which will be informed by your answers to my questions above).
* **[TASK]:** This will be a clear, multi-step directive. The AI must first assess the text against the stated goals, then provide categorized feedback, and finally, produce a revised version. Each piece of feedback must be justified.
* **[FORMAT]:** We will enforce a strict, non-negotiable output format using Markdown. This ensures the output is always organized, readable, and actionable, preventing the AI from giving a lazy, unstructured wall of text.
* **[CONSTRAINTS]:** We will add rules to guide the *quality* of the feedback, ensuring it is constructive, strategic, and educational.

---
