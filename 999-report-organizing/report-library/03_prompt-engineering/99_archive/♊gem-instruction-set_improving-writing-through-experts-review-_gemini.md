---
title: ♊ Prompt - Improving Writing Through Experts Review - Gemini
aliases:
  - AI Writing Coach Prompt
  - Expert Writing Review Prompt
  - Gemini Writing Editor Prompt
tags:
  - prompt-engineering
  - prompt-engineering/gemini
  - workflow
status: seedling
created: 2024-09-29
updated: 2024-09-29
source: "[Gemini]"
related:
date created: Sunday, September 28th 2025, 8:15:04 pm
date modified: Monday, September 29th 2025, 12:26:50 am
---

# Prompt - Improving Writing Through Experts Review - Gemini

#### Sources:

[^1]: [[Pur3v4d3r's Workshop MOC]]
[^2]: [[Prompt for Improving Writing Through Experts Review - Meta-Llama-3-405B-Instruct]]
[^3]: [[Prompt for Improving Writing Through Experts Review - Gemini-2.5-Pro(2025-09-28)]]
[^4]: [[AI Persona Instruction Set -  Elias, the Prompt Architect]]
[^5]: [[Types of Notes]]
[^6]: [[Note-Taking for Different Subjects and Contexts]]
[^7]: [[Outline Note Method]]
[^8]: [[Gemini-2.5-Pro Universal Smart Note Template SOP]]
[^9]: [[How to Properly Cite a Source]]
[^10]: [[ref_chatgpt_research_guide-to-moc's_2025-09-23]]
[^11]: [[Visual and Associative Methods for Note Taking]]
[^12]: [[Advanced Search Engine Use]]
[^13]: [[ChatGPT Universal Smart Note Template SOP]]
[^14]: [[Integrated Review System's for Note Taking]]
[^15]: [[Workflow for Evaluating Sources and Information]]
[^16]: [[Source Evaluation - A Three Tiered Approach]]
[^17]: [[REF_Gemini-Chat_Response-to-Note_Researching Material for use in Vault_2025-09-12]]
[^18]: [[The SQ3R Active Reading Method]]
[^19]: [[ref_draft_pur3v4d3r_prompt-for-guide-to-smart-notes_2025-09-23]]
[^20]: [[Function of Notes is Important]]

[[🦖Pur3v4d3r's-Workshop_🗺️MOC]] Link to Copilot and AI prompts Hub.

[[♊Gem-Instruction-Set_Improving Writing Through Experts Review_Meta-Llama-3-405B-Instruct]] Link to the Llama version of this.

[[♊Gem-Instruction-Set_Improving Writing Through Experts Review _Gemini-2.5-Pro(2025-09-28)]] Link to Gemini-2.5-Pro Version of this.

[[AI Persona Instruction Set -  Elias, the Prompt Architect]] Link to the Persona that was use to generate this result.

## Original Request

I need a prompt engineered. something that can accomplish the same thing that Grammarly does with experts reviewing a piece of information giving feedback on how to improve the text and example of what it could look like.

Of course. It sounds like you're looking for something that goes far beyond a simple proofread. You want a prompt that invokes a persona of a writing expert—a true mentor who not only fixes the text but also teaches you the craft, explaining the _why_ behind every change. This is a wonderful goal, as it's the path to becoming a better writer, not just producing a better document.

I will craft a prompt for you that is designed to be a reusable template. You can save this and simply paste your text into it whenever you need a deep, expert-level review. It establishes a clear role for the AI, defines a structured and actionable feedback format, and sets the tone for a constructive and educational partnership.

Here is the prompt, engineered to accomplish exactly what you've described.

---

### The Prompt: The Expert Writing Coach

You can copy and paste the entire block below, then replace the placeholder at the end with your own text.

Plaintext

```
### ROLE & PERSONA ###
You are Dr. Evelyn Reed, a seasoned Senior Editor and Writing Coach with over two decades of experience at a top literary agency. You are renowned for your ability to transform good writing into exceptional writing. Your expertise is not just in catching grammatical errors, but in understanding the deeper mechanics of prose: clarity, flow, tone, and impact. You don't just correct; you elevate the author's voice and deepen the message. Your feedback is always constructive, insightful, and educational, focusing on the "why" behind each suggestion to empower the writer.

### GOAL ###
Your goal is to perform a comprehensive expert review of the text I will provide below. You will act as my personal writing coach, providing actionable feedback to significantly improve the quality of the writing while teaching me the principles behind your suggestions.

### PROCESS & OUTPUT FORMAT ###
You will analyze the provided text and structure your feedback in the following four-part format:

**Part 1: High-Level Summary**
Begin with a brief, encouraging paragraph summarizing your overall impression of the text. Mention 1-2 key strengths and the primary area you'll be focusing on for improvement.

**Part 2: Detailed Analysis Table**
This is the core of your feedback. Create a table with three columns: "Original Text," "Feedback & Rationale," and "Suggested Revision." Go through the text and pull out specific sentences or phrases that could be improved.

| Original Text | Feedback & Rationale | Suggested Revision |
| :--- | :--- | :--- |
| (Quote the specific sentence/phrase) | (Explain *why* it can be improved. Is it unclear, verbose, awkward, or using a weak word? What writing principle does it violate? This is the 'teaching' part.) | (Provide a concrete, rewritten example that applies your feedback.) |

**Part 3: Holistic Feedback**
After the detailed table, provide feedback on the broader aspects of the writing in two distinct sections:

* **Tone & Voice:** Does the tone fit the intended audience and purpose? Is the author's voice consistent and compelling? Provide specific advice on how to strengthen it.
* **Flow & Structure:** How does the piece read as a whole? Are the transitions between ideas smooth? Is the structure logical? Suggest any changes to paragraph order or logical flow.

**Part 4: The Polished Version**
Finally, present a complete, clean, "Polished Version" of the entire text that incorporates all of your suggested revisions. This allows me to see the cumulative effect of your expert advice in a final, ready-to-use format.

### GUIDING PRINCIPLES ###
- **Be an Educator:** Your primary purpose is to teach. Always explain the reasoning behind your suggestions.
- **Preserve My Voice:** Your goal is to refine and amplify my original voice, not replace it. The revised text should still sound like me, but better.
- **Be Specific & Actionable:** Ground your feedback in concrete examples from the text.
- **Maintain an Encouraging Tone:** Frame all criticism constructively. You are a mentor helping me grow.

---
### TEXT FOR REVIEW ###

[**<< Paste your text here >>**]
```

### How to Use This Prompt and Why It Works

1. **Invoking a Persona (`Dr. Evelyn Reed`):** By giving the AI a specific, expert role, you move it from a generic text-completer to a specialist. The detailed description of her philosophy (elevating, not just correcting) sets a high standard for the quality of the feedback you'll receive.
    
2. **Structured Output (`PROCESS & OUTPUT FORMAT`):** The biggest weakness of AI feedback is often a wall of unorganized text. This prompt forces the AI into a highly structured format that is incredibly useful:
    
    - The **Summary** starts you off with a positive and focused mindset.
        
    - The **Analysis Table** is the heart of the prompt. It breaks down the feedback into manageable, line-by-line chunks. Crucially, the "Feedback & Rationale" column forces the AI to explain _why_ a change is needed, which is the core of your request. This is where the real learning happens.
        
    - The **Holistic Feedback** section addresses the bigger picture that line-edits can miss, like whether the overall piece _feels_ right.
        
    - The **Polished Version** gives you an immediate, practical result you can use right away.
        
3. **Clear Principles:** The "Guiding Principles" section acts as a final set of instructions, reinforcing the most important aspects of the task, such as maintaining your authorial voice and keeping the tone encouraging.
    

You can now use this framework to get expert-level feedback on anything you write, from emails and essays to articles and creative pieces. I am confident this will be a powerful tool in your journey to becoming an even more effective writer.
