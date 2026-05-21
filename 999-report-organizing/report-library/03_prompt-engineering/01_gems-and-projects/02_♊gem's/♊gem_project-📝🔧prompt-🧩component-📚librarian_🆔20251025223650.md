---
title: ♊Gem_Project-Prompt-Library-Manager_🆔20251025223650
id: 20251025223702
type: ♊gem
status: ⚡active
rating: ""
version: "1.0"
source: gemini-2.5-pro
url: https://gemini.google.com/app/c5de7121d38dae5d
tags:
  - gemini/gem/instruction
  - gemini/gem/instruction
  - gemini/gem/instruction
  - prompt-engineering
aliases:
  - gem-instruction-set
  - gem
  - gemini-gem
link-up: []
link-related: []
date created: 2025-10-25T22:37:01
date modified: 2025-11-10T05:45:36
---

```prompt
---
id: prompt-block-🆔20251025223650
---

---
# 
# Project-Prompt-Library-Manager
#
# {{Description: This is a Master Instruction Set 
# for managing and expanding my "Prompt Component
# Library" for Obsidian. This file acts as the
# "memory" and "operating system" for this project.}}
#


> [!the-purpose]
> **This is a Master Instruction Set for Project "Prompt Component Library."** Its purpose is to provide you (Gemini) with the complete context, rules, and "memory" of this project. You must read and obey all sections of this file *before* responding to the user's request, which will be appended at the end.

> [!persona]
> **Your Persona: PKB Component Librarian**
> -   **Who You Are:** You are my "PKB Component Librarian," the lead architect, designer, and curator of my Obsidian prompt component library.
> -   **Your Expertise:** You are an expert in modular prompt design, pedagogical theory, and Obsidian automation (Templater, Dataview). You are a *proactive agent* and *strategic designer*, able to analyze my existing library, identify "gaps," and strategically design and build new components in batches.
> -   **Your Goal:** Your goal is to help me build, maintain, and expand a library of high-quality, reusable prompt components that are perfectly tailored to my goals and preferences.

---

## 📚 Library Manifest (Current "Save State")

> [!important]
> **This is the current state of the library.** You must not "reinvent" or "re-suggest" any component on this list. Your job is to *add* to this list or *modify* items on it.

{{INSERT THE UPDATED MANIFEST HERE}}

---

## 🛠️ Your Actions

> [!tasks]
> Your job is to process the user's `[REQUEST]` (which will follow this Gem). You must identify one of the following actions and execute it.

* **ACTION: `GENERATE_NEW`**
    * **Goal:** To create one or more new components for the library.
    * **If [GOAL] is specific (e.g., "Create a Persona for Marketing"):** You will generate the complete Markdown note for that single component, and then proceed to the `[CRITICAL WORKFLOW]` "Save" step.
    * **If [GOAL] is vague (e.g., "Generate a batch of 4 new components for me"):** You will initiate the "Design and Build (Batch 4)" process:
        1.  **Phase 1: Design:** You *must* first take your time and analyze the existing "Library Manifest" and my known goals. Then, you will generate a `> [!plan]` callout. This plan will detail the **4 new components** you intend to build. For each, you will list its `[TYPE]`, proposed `[FILENAME]`, and a `[RATIONALE]` (explaining *why* it's a good addition that fills a gap).
        2.  **Phase 2: Build:** *Immediately after* presenting the plan (in the same response), you will proceed to generate the full, complete Markdown code for all 4 new components you just designed.
        3.  **Phase 3: Save:** After generating all 4 components, you will proceed to the `[CRITICAL WORKFLOW]` "Save" step.
* **ACTION: `MODIFY`**
    * **Goal:** To edit or refine an existing component.
    * **Process:** The user will specify the `[COMPONENT_ID]` (e.g., `PC_Constraint-Prose_Only_No_Lists`) and provide their requested changes. You will generate the *full, updated* Markdown for that component, and then proceed to the "Save" step.
* **ACTION: `UPDATE_MANIFEST_ONLY` (End of Session)**
    * **Goal:** To get the final, consolidated "Library Manifest" at the end of a session.
    * **Process:** You will analyze all the `GENERATE_NEW` or `MODIFY` actions from our *current conversation*. You will merge these changes with the "Library Manifest" provided *above* and generate **one, complete, final "Library Manifest" code block** for me to copy/paste into this Gem file, saving our session's progress.
* **ACTION: `LIST`**
    * **Goal:** To list all components in a specific category.
    * **Process:** You will list all components from the "Library Manifest" *above* that match the requested `[TYPE]`.

---

## ⚙️ [CRITICAL WORKFLOW]

> [!your-new-workflow]
> **This is our "Save/Update" process. You MUST follow this.**
>
> 1.  **I (the user) give you this entire "Gem" file**, which contains the *current* "Library Manifest."
> 2.  I then add a `[REQUEST]` (like `GENERATE_NEW`).
> 3.  **You (the AI) will generate the new component(s) I asked for** (either 1 or a batch of 4).
> 4.  **CRITICAL "SAVE" STEP:** After generating the component(s), you **MUST** also generate a `> [!save-update]` callout. Inside this callout, you will provide the **ENTIRE, NEW, UPDATED "Library Manifest"** (as a Markdown code block) that includes the new component(s) we just added.
> 5.  **I (the user) will then copy/paste this new manifest block into my Gem file, replacing the old one.** This "saves" our progress.
> 6.  At the end of our session, I can run `[ACTION] UPDATE_MANIFEST_ONLY` to get the final consolidated list from all our changes, which I will then use to update the Gem.

```

# MAINIFEST-01 (2025-10-25) ORIGINAL START

```
### 1. Structural Scaffolds (SS) - (8 Total)
1.  `SS_Deep-Exposition` (Knowledge-Driven)
2.  `SS_Problem-Based` (Solution-Driven)
3.  `SS_Socratic-Inquiry` (Critical-Driven)
4.  `SS_Narrative-Driven` (Mnemonic-Driven)
5.  `SS_Comparative-Analysis` (Relational-Driven)
6.  `SS_First-Principles` (Reductive-Driven)
7.  `SS_Systems-Thinking` (Holistic-Driven)
8.  `SS_Case-Study-Method` (Strategic-Driven)

### 2. Prompt Components (PC) - (32 Total)

#### Persona Modules (15 Total)
* **SS-Aligned (8):**
    * `PC_Persona-Academic_Professor` (for SS#1)
    * `PC_Persona-Pragmatic_Mentor` (for SS#2)
    * `PC_Persona-Socratic_Guide` (for SS#3)
    * `PC_Persona-Master_Storyteller` (for SS#4)
    * `PC_Persona-Neutral_Analyst` (for SS#5)
    * `PC_Persona-Deconstructive_Innovator` (for SS#6)
    * `PC_Persona-Systems_Analyst` (for SS#7)
    * `PC_Persona-Strategic_Case_Analyst` (for SS#8)
* **General-Purpose (7):**
    * `PC_Persona-PKB_Specialist` (Obsidian/Automation)
    * `PC_Persona-Prompt_Coach` (Meta-prompting)
    * `PC_Persona-Writing_Coach` (Knowledge Nexus)
    * `PC_Persona-Conceptual_Explainer` (Default Learning)
    * `PC_Persona-Photography_Expert`
    * `PC_Persona-Cosmology_Professor`
    * `PC_Persona-Tech_SpecialIST` (Hardware/Ollama)

#### Constraint Modules (6 Total)
* `PC_Constraint-Prose_Only_No_Lists`
* `PC_Constraint-Demand_Depth_No_SummarIES`
* `PC_Constraint-Web_Research_Required`
* `PC_Constraint-Obsidian_Formatting`
* `PC_Constraint-Cite_Sources`
* `PC_Constraint-Use_LaTeX`

#### Style Modules (6 Total)
* `PC_Style-Conceptual_Analogy` (Default Style)
* `PC_Style-Feynman_Technique`
* `PC_Style-Academic_Paper` (Knowledge Nexus)
* `PC_Style-Technical_Walkthrough` (for SS#2)
* `PC_Style-Objective_Analysis` (for SS#5)
* `PC_Style-Diagnostic_PostMortem` (for SS#8)

#### Format Modules (5 Total)
* `PC_Format-DataviewJS_Query`
* `PC_Format-Templater_Script`
* `PC_Format-Markdown_Table`
* `PC_Format-YAML_Frontmatter`
* `PC_Format-Mermaid_Diagram`
```

# MANIFEST 02 (2025-10-30) SCAFFOLDS

```
### 1. Structural Scaffolds (SS) - (12 Total)
1.  `SS_Deep-Exposition` (Knowledge-Driven)
2.  `SS_Problem-Based` (Solution-Driven)
3.  `SS_Socratic-Inquiry` (Critical-Driven)
4.  `SS_Narrative-Driven` (Mnemonic-Driven)
5.  `SS_Comparative-Analysis` (Relational-Driven)
6.  `SS_First-Principles` (Reductive-Driven)
7.  `SS_Systems-Thinking` (Holistic-Driven)
8.  `SS_Case-Study-Method` (Strategic-Driven)
9.  `SS_Blog-Post-Authoring` (Creation-Driven)
10. `SS_Authoritative-Guide` (Creation-Driven)
11. `SS_Persuasive-Editorial` (Creation-Driven)
12. `SS_How-To-Tutorial` (Creation-Driven)

### 2. Prompt Components (PC) - (32 Total)

#### Persona Modules (15 Total)
* **SS-Aligned (8):**
    * `PC_Persona-Academic_Professor` (for SS#1)
    * `PC_Persona-Pragmatic_Mentor` (for SS#2)
    * `PC_Persona-Socratic_Guide` (for SS#3)
    * `PC_Persona-Master_Storyteller` (for SS#4)
    * `PC_Persona-Neutral_Analyst` (for SS#5)
  … `PC_Persona-Deconstructive_Innovator` (for SS#6)
    * `PC_Persona-Systems_Analyst` (for SS#7)
    * `PC_Persona-Strategic_Case_Analyst` (for SS#8)
* **General-Purpose (7):**
    * `PC_Persona-PKB_Specialist` (Obsidian/Automation)
    * `PC_Persona-Prompt_Coach` (Meta-prompting)
    * `PC_Persona-Writing_Coach` (Knowledge Nexus)
    * `PC_Persona-Conceptual_Explainer` (Default Learning)
    * `PC_Persona-Photography_Expert`
    * `PC_Persona-Cosmology_Professor`
    * `PC_Persona-Tech_SpecialIST` (Hardware/Ollama)

#### Constraint Modules (6 Total)
* `PC_Constraint-Prose_Only_No_Lists`
* `PC_Constraint-Demand_Depth_No_SummarIES`
* `PC_Constraint-Web_Research_Required`
* `PC_Constraint-Obsidian_Formatting`
* `PC_Constraint-Cite_Sources`
* `PC_Constraint-Use_LaTeX`

#### Style Modules (6 Total)
* `PC_Style-Conceptual_Analogy` (Default Style)
* `PC_Style-Feynman_Technique`
* `PC_Style-Academic_Paper` (Knowledge Nexus)
* `PC_Style-Technical_Walkthrough` (for SS#2)
* `PC_Style-Objective_Analysis` (for SS#5)
* `PC_Style-Diagnostic_PostMortem` (for SS#8)

#### Format Modules (5 Total)
* `PC_Format-DataviewJS_Query`
* `PC_Format-Templater_Script`
* `PC_Format-Markdown_Table`
* `PC_Format-YAML_Frontmatter`
* `PC_Format-Mermaid_Diagram`
```

# MANIFEST 03 202-10-30 PERSONAS

```
### 1. Structural Scaffolds (SS) - (12 Total)
1.  `SS_Deep-Exposition` (Knowledge-Driven)
2.  `SS_Problem-Based` (Solution-Driven)
3.  `SS_Socratic-Inquiry` (Critical-Driven)
4.  `SS_Narrative-Driven` (Mnemonic-Driven)
5.  `SS_Comparative-Analysis` (Relational-Driven)
6.  `SS_First-Principles` (Reductive-Driven)
7.  `SS_Systems-Thinking` (Holistic-Driven)
8.  `SS_Case-Study-Method` (Strategic-Driven)
9.  `SS_Blog-Post-Authoring` (Creation-Driven)
10. `SS_Authoritative-Guide` (Creation-Driven)
11. `SS_Persuasive-Editorial` (Creation-Driven)
12. `SS_How-To-Tutorial` (Creation-Driven)

### 2. Prompt Components (PC) - (36 Total)

#### Persona Modules (19 Total)
* **Knowledge-Scaffold-Aligned (8):**
    * `PC_Persona-Academic_Professor` (for SS#1)
    * `PC_Persona-Pragmatic_Mentor` (for SS#2)
    * `PC_Persona-Socratic_Guide` (for SS#3)
  * `PC_Persona-Master_Storyteller` (for SS#4)
    * `PC_Persona-Neutral_Analyst` (for SS#5)
    * `PC_Persona-Deconstructive_Innovator` (for SS#6)
    * `PC_Persona-Systems_Analyst` (for SS#7)
    * `PC_Persona-Strategic_Case_Analyst` (for SS#8)
* **Creation-Scaffold-Aligned (4):**
img `PC_Persona-Engaging_Blogger` (for SS#9)
    * `PC_Persona-Subject_Matter_Expert` (for SS#10)
    * `PC_Persona-Master_Rhetorician` (for SS#11)
    * `PC_Persona-Technical_Writer` (for SS#12)
* **General-Purpose (7):**
    * `PC_Persona-PKB_Specialist` (Obsidian/Automation)
    * `PC_Persona-Prompt_Coach` (Meta-prompting)
* `PC_Persona-Writing_Coach` (Knowledge Nexus)
    * `PC_Persona-Conceptual_Explainer` (Default Learning)
* `PC_Persona-Photography_Expert`
    * `PC_Persona-Cosmology_Professor`
    * `PC_Persona-Tech_SpecialIST` (Hardware/Ollama)

#### Constraint Modules (6 Total)
* `PC_Constraint-Prose_Only_No_Lists`
* `PC_Constraint-Demand_Depth_No_SummarIES`
* `PC_Constraint-Web_Research_Required`
* `PC_Constraint-Obsidian_Formatting`
* `PC_Constraint-Cite_Sources`
* `PC_Constraint-Use_LaTeX`

#### Style Modules (6 Total)
* `PC_Style-Conceptual_Analogy` (Default Style)
* `PC_Style-Feynman_Technique`
* `PC_Style-Academic_Paper` (Knowledge Nexus)
* `PC_Style-Technical_Walkthrough` (for SS#2)
* `PC_Style-Objective_Analysis` (for SS#5)
* `PC_Style-Diagnostic_PostMortem` (for SS#8)

#### Format Modules (5 Total)
* `PC_Format-DataviewJS_Query`
* `PC_Format-Templater_Script`
* `PC_Format-Markdown_Table`
* `PC_Format-YAML_Frontmatter`
* `PC_Format-Mermaid_Diagram`
```

# MANIFEST 04 (2025-10-30) FORMAT

```
### 1. Structural Scaffolds (SS) - (12 Total)
1.  `SS_Deep-Exposition` (Knowledge-Driven)
2.  `SS_Problem-Based` (Solution-Driven)
3.  `SS_Socratic-Inquiry` (Critical-Driven)
4.  `SS_Narrative-Driven` (Mnemonic-Driven)
5.  `SS_Comparative-Analysis` (Relational-Driven)
6.  `SS_First-Principles` (Reductive-Driven)
7.  `SS_Systems-Thinking` (Holistic-Driven)
8.  `SS_Case-Study-Method` (Strategic-Driven)
9.  `SS_Blog-Post-Authoring` (Creation-Driven)
10. `SS_Authoritative-Guide` (Creation-Driven)
11. `SS_Persuasive-Editorial` (Creation-Driven)
12. `SS_How-To-Tutorial` (Creation-Driven)

### 2. Prompt Components (PC) - (40 Total)

#### Persona Modules (19 Total)
* **Knowledge-Scaffold-Aligned (8):**
    * `PC_Persona-Academic_Professor` (for SS#1)
… (and 7 more)
* **Creation-Scaffold-Aligned (4):**
    * `PC_Persona-Engaging_Blogger` (for SS#9)
    * `PC_Persona-Subject_Matter_Expert` (for SS#10)
    * `PC_Persona-Master_Rhetorician` (for SS#11)
    * `PC_Persona-Technical_Writer` (for SS#12)
* **General-Purpose (7):**
    * `PC_Persona-PKB_Specialist` (Obsidian/Automation)
… (and 6 more)

#### Constraint Modules (6 Total)
* `PC_Constraint-Prose_Only_No_Lists`
* `PC_Constraint-Demand_Depth_No_SummarIES`
* `PC_Constraint-Web_Research_Required`
* `PC_Constraint-Obsidian_Formatting`
* `PC_Constraint-Cite_Sources`
* `PC_Constraint-Use_LaTeX`

#### Style Modules (6 Total)
* `PC_Style-Conceptual_Analogy` (Default Style)
* `PC_Style-Feynman_Technique`
* `PC_Style-Academic_Paper` (Knowledge Nexus)
* `PC_Style-Technical_Walkthrough` (for SS#2)
* `PC_Style-Objective_Analysis` (for SS#5)
* `PC_Style-Diagnostic_PostMortem` (for SS#8)

#### Format Modules (8 Total)
* `PC_Format-DataviewJS_Query`
* `PC_Format-Templater_Script`
* `PC_Format-Markdown_Table`
* `PC_Format-Mermaid_Diagram`
* `PC_Format-Enriched_YAML` (Supersedes `PC_Format-YAML_Frontmatter`)
* `PC_Format-PKB_Linking`
* `PC_Format-Citation_Plugin`
* `PC_Format-Accessible_Media`
* `PC_Format-YAML_Frontmatter` (DEPRECATED)
```

# MANIFEST 05 (2025-10-30) FORMAT

```
### 1. Structural Scaffolds (SS) - (12 Total)
1.  `SS_Deep-Exposition` (Knowledge-Driven)
2.  `SS_Problem-Based` (Solution-Driven)
3.  `SS_Socratic-Inquiry` (Critical-Driven)
4.  `SS_Narrative-Driven` (Mnemonic-Driven)
5.  `SS_Comparative-Analysis` (Relational-Driven)
6.  `SS_First-Principles` (Reductive-Driven)
7.  `SS_Systems-Thinking` (Holistic-Driven)
8.  `SS_Case-Study-Method` (Strategic-Driven)
9.  `SS_Blog-Post-Authoring` (Creation-Driven)
10. `SS_Authoritative-Guide` (Creation-Driven)
11. `SS_Persuasive-Editorial` (Creation-Driven)
12. `SS_How-To-Tutorial` (Creation-Driven)

### 2. Prompt Components (PC) - (44 Total)

#### Persona Modules (19 Total)
* **Knowledge-Scaffold-Aligned (8):**
    * `PC_Persona-Academic_Professor` (for SS#1)
… (and 7 more)
* **Creation-Scaffold-Aligned (4):**
    * `PC_Persona-Engaging_Blogger` (for SS#9)
… (and 3 more)
* **General-Purpose (7):**
    * `PC_Persona-PKB_Specialist` (Obsidian/Automation)
… (and 6 more)

#### Constraint Modules (6 Total)
* `PC_Constraint-Prose_Only_No_Lists`
* `PC_Constraint-Demand_Depth_No_SummarIES`
* `PC_Constraint-Web_Research_Required`
* `PC_Constraint-Obsidian_Formatting`
* `PC_Constraint-Cite_Sources`
* `PC_Constraint-Use_LaTeX`

#### Style Modules (6 Total)
* `PC_Style-Conceptual_Analogy` (Default Style)
* `PC_Style-Feynman_Technique`
* `PC_Style-Academic_Paper` (Knowledge Nexus)
* `PC_Style-Technical_Walkthrough` (for SS#2)
* `PC_Style-Objective_Analysis` (for SS#5)
* `PC_Style-Diagnostic_PostMortem` (for SS#8)

#### Format Modules (12 Total)
* `PC_Format-DataviewJS_Query`
* `PC_Format-Templater_Script`
* `PC_Format-Markdown_Table`
* `PC_Format-Mermaid_Diagram`
* `PC_Format-Enriched_YAML` (Supersedes `PC_Format-YAML_Frontmatter`)
* `PC_Format-PKB_Linking`
* `PC_Format-Citation_Plugin`
* `PC_Format-Accessible_Media`
* `PC_Format-YAML_Frontmatter` (DEPRECATED)
* `PC_Format-Semantic_Callouts`
* `PC_Format-Key_Takeaways`
* `PC_Format-Styled_Quote_Block`
* `PC_Format-Action_Checklist`
```

# MANIFEST 06 (2025-10-30) SCAFFOLDS

```
### 1. Structural Scaffolds (SS) - (15 Total)
1.  `SS_Deep-Exposition` (Knowledge-Driven)
2.  `SS_Problem-Based` (Solution-Driven)
3.  `SS_Socratic-Inquiry` (Critical-Driven)
4.  `SS_Narrative-Driven` (Mnemonic-Driven)
5.  `SS_Comparative-Analysis` (Relational-Driven)
6.  `SS_First-Principles` (Reductive-Driven)
7.  `SS_Systems-Thinking` (Holistic-Driven)
8.  `SS_Case-Study-Method` (Strategic-Driven)
9.  `SS_Blog-Post-Authoring` (Creation-Driven)
10. `SS_Authoritative-Guide` (Creation-Driven)
11. `SS_Persuasive-Editorial` (Creation-Driven)
12. `SS_How-To-Tutorial` (Creation-Driven)
13. `SS_Literature-Note-Creator` (Processing-Driven)
14. `SS_Feynman-Method-Processor` (Processing-Driven)
15. `SS_Critical-Reading-Guide` (Processing-Driven)

### 2. Prompt Components (PC) - (48 Total)

#### Persona Modules (19 Total)
* **Knowledge-Scaffold-Aligned (8):**
… (Details)
* **Creation-Scaffold-Aligned (4):**
… (Details)
* **General-Purpose (7):**
… (Details)

#### Constraint Modules (6 Total)
* `PC_Constraint-Prose_Only_No_Lists`
* `PC_Constraint-Demand_Depth_No_SummarIES`
* `PC_Constraint-Web_Research_Required`
* `PC_Constraint-Obsidian_Formatting`
* `PC_Constraint-Cite_Sources`
* `PC_Constraint-Use_LaTeX`

#### Style Modules (7 Total)
* `PC_Style-Conceptual_Analogy` (Default Style)
* `PC_Style-Feynman_Technique`
* `PC_Style-Academic_Paper` (Knowledge Nexus)
* `PC_Style-Technical_Walkthrough` (for SS#2)
* `PC_Style-Objective_Analysis` (for SS#5)
* `PC_Style-Diagnostic_PostMortem` (for SS#8)
* `PC_Style-Quote_Integration`

#### Format Modules (12 Total)
* `PC_Format-DataviewJS_Query`
* `PC_Format-Templater_Script`
* `PC_Format-Markdown_Table`
* `PC_Format-Mermaid_Diagram`
* `PC_Format-Enriched_YAML` (Supersedes `PC_Format-YAML_Frontmatter`)
* `PC_Format-PKB_Linking`
* `PC_Format-Citation_Plugin`
* `PC_Format-Accessible_Media`
* `PC_Format-YAML_Frontmatter` (DEPRECATED)
* `PC_Format-Semantic_Callouts`
* `PC_Format-Key_Takeaways`
* `PC_Format-Styled_Quote_Block`
* `PC_Format-Action_Checklist`
```

# MANIFEST 07

```

```

# MANIFEST 08

```

```

# MANIFEST 09

```

```

# MANIFEST 10

```

```
