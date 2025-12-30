---
title: Building Your Personal Command Library with Custom Prompts
aliases: [AI Functions Workflow, Custom AI Prompts, Personal Command Library]
tags: [prompt-engineering, type/report/psychology, workflow]
status: seedling
created: 2024-09-29
updated: 2024-09-29
source: 
related:

date created: Sunday, September 28th 2025, 6:20:10 pm
date modified: Monday, September 29th 2025, 12:30:44 am
---

#### Sources:

[^1]: [[Note-Taking for Different Subjects and Contexts]]
[^2]: [[Types of Notes]]
[^3]: [[Outline Note Method]]
[^4]: [[Visual and Associative Methods for Note Taking]]
[^5]: [[Advanced Search Engine Use]]
[^6]: [[How to Properly Cite a Source]]
[^7]: [[ref_chatgpt_research_guide-to-moc's_2025-09-23]]
[^8]: [[ChatGPT Universal Smart Note Template SOP]]
[^9]: [[Workflow for Evaluating Sources and Information]]
[^10]: [[Source Evaluation - A Three Tiered Approach]]
[^11]: [[Common Logical Fallacies]]
[^12]: [[ref_notes_guide-to-active-reading-by-ai's_2025-09-24]]
[^13]: [[Function of Notes is Important]]
[^14]: [[S I F T - Lateral Reading for Source Verification]]
[^15]: [[The Toulmin Model]]
[^16]: [[ref_gemini-prompt_guide-to-creating-smart-notes_2025-09-23]]
[^17]: [[Document Your Searches during Research]]
[^18]: [[ref_gemini-prompt_guide-to-obsidian-plug-in-quickadd_2025-09-24]]
[^19]: [[00 Inbox/00_File/REF_Gemini-Deep-Research_Obsidian-Knowledge-Research-Guide_2025-09-12]]

> [!the-purpose]
> This is a complete workflow for building out a AI integrated workflow in your Obsidian [[PKB]]. Its from an article that Gemini generated for using a custom prompt. Both of which have been left at the bottom of this section for reference.
> 
> - [[REF_Gemini-Deep-Research_AI-Augmented-Vault_Strategic-Prompting-Guide-for-Copilot-&-Plugin Synergy_2025-09-28]]
> 	- This is the link to the original article written by [[Gemini]].
> - [[Draft_Copilot-Prompt-Aquisition_Pur3v4d3r]]
> 	- This is the link to the prompt that was used to create this material.
> - [[The AI-Augmented Vault Guide for Obsidian Copilot and Plugin Synergy]]
> 	- This is a link to a related Note, it used the same prompt as this Note but I did so through many various AI channels. 
> 		- This is a great high level overview comparison of the different AIs functionality.

# Building Your Personal Command Library with Custom Prompts

*The principles of prompt engineering and the power of contextual placeholders are fully operationalized through the creation of custom prompts. This feature allows users to save complex, multi-step instructions as reusable commands, effectively transforming the AI assistant into a bespoke toolkit tailored to their specific workflows.1 Building a personal library of custom prompts elevates the user from a passive question-asker to an active tool-builder, encapsulating their most common cognitive tasks into efficient, one-click operations.*

*This process can be conceptualized as creating a set of "AI Functions." In programming, a function is a named block of code that performs a specific task; it accepts inputs, processes them, and returns an output. A custom prompt in Obsidian Copilot functions identically: it accepts vault content as input (via placeholders), directs the LLM to perform a complex cognitive operation (via the prompt's instructions), and returns structured text as output. Adopting this developer-like mindset—identifying repetitive cognitive workflows and encapsulating them into functions—is the key to building a truly augmented knowledge system.*

*The workflow for creating and using these AI Functions is straightforward and seamlessly integrated into the Obsidian environment.*

1. **Creation:** A new custom prompt is created by invoking the "**Copilot: Add custom prompt**" command from the Command Palette (**Ctrl + P**). This opens a modal with two fields: `Title` and `Prompt`. **The `Title` should be a short**, **memorable name that will be used to invoke the command** (e.g., "Summarize to Bullets," "Brainstorm Counterarguments"). The `Prompt` field is where the full instruction is written, incorporating the [[The G.C.S.E. Framework (Goal, Context, Source, Expectations)|G.C.S.E.]] framework and any necessary placeholders.
    
2. **Execution:** Once saved, a custom prompt can be triggered in two primary ways. The first is by selecting text, opening the Command Palette, and choosing "**Copilot: Apply custom prompt**," which presents a list of all saved prompts. **A more fluid and efficient method is to type a forward slash (`/`) in the Copilot chat input box. This action brings up a searchable modal of all existing custom prompts, allowing for rapid selection and execution.**
    
3. **Management:** Custom prompts are stored as individual Markdown files within the `.obsidian/plugins/copilot-custom-prompts/` folder in the vault. This aligns with Obsidian's core philosophy of open, text-based formats. **Prompts can be edited, duplicated, or deleted either through the Copilot settings interface or by directly manipulating these `.md` files in a text editor, offering maximum flexibility and control to the user.**
    

*By systematically building out a library of custom prompts—such as a `/summarize` function, a `/critique` function, a `/generate-tasks` function, or a `/find-connections` function—the user* **creates a personalized and powerful extension of their own cognitive capabilities**, *ready to be deployed at a moment's notice.*
