----
----
Create a reference note for these.
### 1. The "Project / Output" Skeleton

**Best for:** Managing active projects (like your "Prompt Component Library" or "Photography Series"), coding sprints, or goals.
**Key Feature:** It automatically calculates a "Target Finish Date" based on a prompt and sets status metadata.

`````
<%*
/* ---------------------------------------------------------------
   PROJECT / SPRINT SKELETON
   Use this for: Projects, Goals, Sprints, Deliverables
   ---------------------------------------------------------------
*/
// --- CONFIGURATION: DROPDOWNS ---
const statusList = [
    "1-Backlog", 
    "2-Planning", 
    "3-Active", 
    "4-Review", 
    "5-Completed", 
    "6-Archived"
];
const priorityList = [
    "High", 
    "Medium", 
    "Low"
];
const areaList = [
    "Development", 
    "Photography", 
    "Learning", 
    "Personal", 
    "Maintenance"
];
// --- INPUT PROMPTS ---
const title = await tp.system.prompt("Project Name:");
const selectedStatus = await tp.system.suggester(statusList, statusList, false, "Current Status:");
const selectedPriority = await tp.system.suggester(priorityList, priorityList, false, "Priority Level:");
const selectedArea = await tp.system.suggester(areaList, areaList, false, "Area of Responsibility:");
// --- LOGIC: DATE CALCULATIONS ---
// Ask for duration in weeks to estimate a due date
const durationWeeks = await tp.system.prompt("Estimated duration (weeks)?", "2");
const targetDate = moment().add(parseInt(durationWeeks), 'weeks').format("YYYY-MM-DD");
_%>
---
type: "project"
status: "<% selectedStatus %>"
priority: "<% selectedPriority %>"
area: "<% selectedArea %>"
started: "<% tp.date.now("YYYY-MM-DD") %>"
target-finish: "<% targetDate %>"
tags:
  - "project/<% selectedArea.toLowerCase() %>"
link-related:
  - 
---

# <% title %>

## 🎯 Objective
> [!goal]
> What is the definition of done?

## 📋 Key Deliverables
- [ ] Deliverable 1
- [ ] Deliverable 2

## 🛠 Resources & Tech Stack
* **Tools:** * **Dependencies:** ## 🗓 Log & Updates
* **<% tp.date.now("YYYY-MM-DD") %>**: Project initialized.

`````

-----

### 2. The "Source / Reference" Skeleton

**Best for:** Books, Articles, YouTube Videos, or Papers.
**Key Feature:** It handles "Author" generation (splitting multiple authors if needed) and categorizes the input type.

```
<%*
/* ---------------------------------------------------------------
   SOURCE / REFERENCE SKELETON
   Use this for: Books, Articles, Videos, Papers
   ---------------------------------------------------------------
*/
// --- CONFIGURATION: MEDIA TYPES ---
const mediaTypes = [
    "Book", 
    "Article", 
    "Video", 
    "Course", 
    "Whitepaper", 
    "Podcast"
];
const statusOptions = [
    "To-Consume", 
    "Reading", 
    "Processing", 
    "Finished", 
    "Abandoned"
];
// --- INPUT PROMPTS ---
const fullTitle = await tp.system.prompt("Title of Work:");
const authorName = await tp.system.prompt("Author / Creator Name:");
const urlLink = await tp.system.prompt("URL (Paste link or leave empty):");
const mediaType = await tp.system.suggester(mediaTypes, mediaTypes, false, "Select Media Type:");
const currentStatus = await tp.system.suggester(statusOptions, statusOptions, false, "Current Status:");
// --- LOGIC: TITLE CLEANING ---
// Removes illegal characters from filenames just in case
const fileName = fullTitle.replace(/[:\/\\|?*"]/g, "");
_%>
---
type: "reference"
subtype: "<% mediaType.toLowerCase() %>"
author: "[[<% authorName %>]]"
status: "<% currentStatus %>"
url: "<% urlLink %>"
rating: 
tags:
  - "input/<% mediaType.toLowerCase() %>"
created: "<% tp.date.now("YYYY-MM-DD") %>"
---

# <% fullTitle %>

> [!info] Metadata
> * **Author**:: [[<% authorName %>]]
> * **Link**:: <% urlLink %>
> * **Type**:: <% mediaType %>

## 🧠 Summary / Abstract
[Enter a high-level summary here]

## 📝 Notes & Highlights

## 🔗 Connected Concepts
- [[Related Topic A]]
- [[Related Topic B]]

```

-----

### 3. The "People / CRM" Skeleton

**Best for:** Tracking family, networking, or learning partners (e.g., tracking your "Teaching Parents AI" interactions).
**Key Feature:** It calculates a "Next Contact" date based on a frequency selection.

```
<%*
/* ---------------------------------------------------------------
   PEOPLE / ENTITY SKELETON
   Use this for: People, Organizations, Network
   ---------------------------------------------------------------
*/
// --- CONFIGURATION: RELATIONSHIPS ---
const relations = [
    "Family", 
    "Friend", 
    "Professional", 
    "Mentor", 
    "Mentee"
];
const contextTags = [
    "Photography", 
    "Tech/AI", 
    "Personal", 
    "Local/Jax"
];
// --- INPUT PROMPTS ---
const name = await tp.system.prompt("Person's Name:");
const relation = await tp.system.suggester(relations, relations, false, "Relationship Type:");
const context = await tp.system.suggester(contextTags, contextTags, false, "Primary Context:");
// --- LOGIC: FOLLOW UP REMINDER ---
// Suggest a follow-up date
const followUpInterval = await tp.system.prompt("Follow up in X days? (Enter number)", "30");
const followUpDate = moment().add(parseInt(followUpInterval), 'days').format("YYYY-MM-DD");
_%>
---
type: "person"
relation: "<% relation %>"
context: "<% context %>"
location: 
last-contact: "<% tp.date.now("YYYY-MM-DD") %>"
next-contact: "<% followUpDate %>"
tags:
  - "people/<% relation.toLowerCase() %>"
---

# <% name %>

> [!user] Profile
> * **Relation**:: <% relation %>
> * **Location**:: 
> * **Interest**:: <% context %>

## 🤝 Interaction Log

### <% tp.date.now("YYYY-MM-DD") %>
* [Note on latest interaction…]

## 🎁 Gift Ideas / Notes
* ## ⚡ Action Items
- [ ] Reach out regarding…

```

### Key Features for this Template:

1.  **Model Tracking:** Tracks whether you used Gemini, ChatGPT, or your Local LLMs (useful for comparing performance).
2.  **Technique Metadata:** Tracks if you used "Chain-of-Thought," "Tree-of-Thoughts," or standard prompting.
3.  **Prompt Archival:** Dedicated section to paste the exact prompt used, preserving context for future iteration.
4.  **Verification Status:** A metadata field to track if you have fact-checked the output (crucial for your cosmology/physics reports).

<!-- end list -->

````
<%*
/* ---------------------------------------------------------------
   LLM GENERATION REPORT SKELETON
   Use this for: Saving AI outputs, comparing models, testing prompts
   ---------------------------------------------------------------
*/
// --- CONFIGURATION: AI MODELS ---
// Update this list as you swap models (e.g., new Local LLMs)
const aiModels = [
    "Gemini 1.5 Pro",
    "GPT-4o", 
    "Claude 3.5 Sonnet",
    "Local: Llama-3-8B", 
    "Local: Mistral-Large", 
    "Local: Qwen-2.5-Coder"
];
// --- CONFIGURATION: PROMPT STRATEGIES ---
// Tracks the specific architecture used
const promptStrategies = [
    "Zero-Shot / Direct", 
    "Chain-of-Thought (CoT)", 
    "Tree-of-Thoughts (ToT)", 
    "Role-Based / Persona", 
    "Few-Shot (Examples)", 
    "Iterative Refinement"
];
// --- CONFIGURATION: DOMAINS ---
const domains = [
    "Coding / Scripting", 
    "Prompt Engineering", 
    "Photography / Optics", 
    "Cosmology / Science", 
    "Philosophy / Stoicism", 
    "PKM / Obsidian"
];
// --- INPUT PROMPTS ---
const title = await tp.system.prompt("Topic of Generation:");
const selectedModel = await tp.system.suggester(aiModels, aiModels, false, "Select Model Used:");
const selectedStrategy = await tp.system.suggester(promptStrategies, promptStrategies, false, "Prompt Strategy Used:");
const selectedDomain = await tp.system.suggester(domains, domains, false, "Knowledge Domain:");
// --- LOGIC: VERIFICATION STATUS ---
// Default to "Unverified" because LLMs hallucinate
const verificationStatus = "Unverified"; 
_%>
---
type: "ai-generation"
model: "<% selectedModel %>"
strategy: "<% selectedStrategy %>"
domain: "<% selectedDomain %>"
verified: "<% verificationStatus %>"
created: "<% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>"
tags:
  - "ai/output"
  - "ai/model/<% selectedModel.replace(/[: ]/g, "-").toLowerCase() %>"
  - "domain/<% selectedDomain.split(" / ")[0].toLowerCase() %>"
link-related:
  - "[[<% tp.date.now("YYYY-MM-DD") %>|Daily-Note]]"
---

# 🤖 Gen-Report: <% title %>

> [!ai] Generation Metadata
> * **Model**:: [[<% selectedModel %>]]
> * **Strategy**:: <% selectedStrategy %>
> * **Date**:: <% tp.date.now("YYYY-MM-DD") %>
> * **Verdict**:: #status/unverified

---

## 🗣️ The Prompt
> [!note]Input Context
> **System / Persona:**
> (Paste your system instructions or "Gem" reference here)
> 
> **User Prompt:**
> ```text
> (Paste the exact prompt you used here)
> ```

---

## 📝 The Output
*Below is the raw output from the LLM.*

(Paste Output Here)

---

## 🕵️ Analysis & Critique
*Critique the performance. Did it hallucinate? Did it follow the formatting rules?*

* **Accuracy:** (1-10)
* **Adherence to Instructions:** (1-10)
* **Key Insights:**
    * * ## 🔗 Related Prompt Components
*Link to the reusable prompt modules in your Prompt Component Library used to build this:*
- [[Prompt-Component-A]]
- [[Prompt-Component-B]]
````

### Recommended Implementation for You

Since you are building the **"Prompt Component Library,"** you should treat this template as the "Testing Ground" for those components.

1.  **The Flow:** You assemble a prompt using your components -\> You run it in Gemini -\> You paste the result into this template.
2.  **The Link:** In the "Related Prompt Components" section at the bottom, you strictly link back to the "Master Instruction Set" or specific components you used.
3.  **The Benefit:** Later, when you look at your "Master Instruction Set" note, the backlinks will show you every single "LLM Report" generated by that instruction set, allowing you to see how it performs over time.

**Would you like a Dataview query that creates a "Leaderboard" showing which of your AI Models is producing the most "Verified" content based on these notes?**
Given your specific focus on **Prompt Architecture**, **Scientific Deconstruction (First Principles)**, and **Stoic Philosophy**, I have designed three highly specialized templates.

These go beyond standard "note-taking" and act as **cognitive scaffolds**—they force you to think in specific patterns (Modular Design, Root Cause Analysis, and Dichotomy of Control) before you even start writing.

-----

### 1. The "Atomic Prompt Component" Skeleton

**Best for:** Your "Prompt Component Library."
**Why you need it:** You mentioned building a "Master Prompt Architecture." To do this effectively, you need to treat prompts like software code—modular, versioned, and reusable. This template isolates a specific instruction (e.g., a "Chain of Thought" module or a "Tone" module) so you can drag-and-drop it into larger prompts.

```
<%*
/* ---------------------------------------------------------------
   ATOMIC PROMPT COMPONENT
   Use this for: Building your "Prompt Component Library"
   ---------------------------------------------------------------
*/
// --- CONFIGURATION: COMPONENT TYPES ---
const componentTypes = [
    "Role / Persona", 
    "Task / Instruction", 
    "Constraint / Guardrail", 
    "Output Format", 
    "Context / Knowledge Base", 
    "Tone / Style"
];
const variableRequirements = [
    "Static (No variables)",
    "Dynamic {{INPUT}}",
    "Dynamic {{CONTEXT}}",
    "Multi-Variable"
];
// --- INPUT PROMPTS ---
const title = await tp.system.prompt("Component Name (e.g., CoT-Module-v1):");
const type = await tp.system.suggester(componentTypes, componentTypes, false, "Component Type:");
const vars = await tp.system.suggester(variableRequirements, variableRequirements, false, "Variable Requirement:");
_%>
---
type: "prompt-module"
module-type: "<% type %>"
variables: "<% vars %>"
version: "1.0"
status: "Active"
tags:
  - "prompt-engineering/component"
  - "prompt-engineering/type/<% type.split(" / ")[0].toLowerCase() %>"
created: "<% tp.date.now("YYYY-MM-DD") %>"
---

# 🧩 Component: <% title %>

> [!summary] usage
> **Purpose**:: [Briefly describe what this module achieves]
> **Best Used**:: [e.g., "When reasoning requires step-by-step logic"]

## 📋 The Syntax block
*Copy this block to insert into Master Prompts.*

[PASTE YOUR PROMPT INSTRUCTION HERE]

## ⚙️ Configuration

  * **Required Variables**:
      * `{{Variable_1}}`: Description…
  * **Token Cost Estimate**: \~ [Low/Med/High]

## 🧪 Version History

  * **v1.0** (\<% tp.date.now("YYYY-MM-DD") %\>): Initial commit. %>

## 🔗 Master Prompts Using This

  * [List the Master Instruction Sets that rely on this module]

<!-- end list -->
```

---

### 2. The "First Principles" Deconstruction

**Best for:** Your deep dives into **Cosmology**, **Photography Physics**, and **Optics**.
**Why you need it:** You mentioned the "First Principles Reconstruction Model" is your preferred learning scaffold. This template forces you to drill down recursively until you hit the fundamental truth (the axiom), and then rebuild the concept from there.

```
<%*
/* ---------------------------------------------------------------
   FIRST PRINCIPLES DECONSTRUCTION
   Use this for: Physics, Optics, Complex Systems
   ---------------------------------------------------------------
*/
// --- CONFIGURATION: DOMAINS ---
const domains = [
    "Physics / Astrophysics", 
    "Optics / Light", 
    "Cognitive Science", 
    "Philosophy", 
    "System Architecture"
];
// --- INPUT PROMPTS ---
const title = await tp.system.prompt("Concept to Deconstruct:");
const domain = await tp.system.suggester(domains, domains, false, "Primary Domain:");
_%>
---
type: "concept-deconstruction"
model: "first-principles"
domain: "<% domain %>"
status: "In-Progress"
tags:
  - "learning/first-principles"
  - "domain/<% domain.split(" / ")[0].toLowerCase() %>"
---
# ⚛️ <% title %>
## 1. The Surface Level (The "What")
*How is this concept generally understood or defined?*
> [!quote] Standard Definition
> 
## 2. The Recursive "Why" (Deconstruction)
*Ask "Why?" five times to break the assumption.*
1. **Why does X happen?** * *Because…*
2. **Why is that true?** * *Because…*
3. **Why?** * *Because…*
## 3. The Bedrock Truths (Axioms)
*What are the fundamental, irreducible facts remaining? (Use LaTeX for physics)*
* **Fact A**: $$ E = mc^2 $$
* **Fact B**: 
## 4. Reconstruction (The Build)
*Re-derive the concept from the axioms above without using analogies.*
## 5. The Feynman Test
> [!check] Simplify
> *Explain this concept to a 12-year-old using the reconstructed logic above.*
````

-----

### 3\. The "Stoic Control" Decision Journal

**Best for:** Your daily philosophy practice and major life decisions.

**Why you need it:** You mentioned Epictetus and the "Dichotomy of Control." This 
template operationalizes that philosophy. It helps you process anxiety or decisions by strictly separating internal vs. external factors.

```
<%*
/* ---------------------------------------------------------------
   STOIC DECISION JOURNAL
   Use this for: Anxiety processing, Decision making, Reflection
   ---------------------------------------------------------------
*/
// --- CONFIGURATION: STOIC LENS ---
const philosophers = [
    "Epictetus (Control)", 
    "Marcus Aurelius (Duty)", 
    "Seneca (Time/Anger)"
];
// --- INPUT PROMPTS ---
const situation = await tp.system.prompt("Situation / Event:");
const lens = await tp.system.suggester(philosophers, philosophers, false, "Philosophical Lens:");
_%>
---
type: "journal/stoic"
lens: "<% lens %>"
date: "<% tp.date.now("YYYY-MM-DD") %>"
tags:
  - "philosophy/stoicism"
  - "practice/journaling"
---

# 🏛️ Stoic Reflection: <% situation %>

> *"Some things are in our control and others not."* — Epictetus

## The Dichotomy of Control

### 🔴 Not In My Control (Externals)
*What elements here are dictated by fate, others, or nature?*
* [ ] The outcome of…
* [ ] Other people's opinions of…
* [ ] The past events…

### 🟢 In My Control (Internals)
*What are my reasoned choices?*
* [ ] My judgment of the event.
* [ ] My preparation.
* [ ] My integrity and character.

## Premeditatio Malorum (Negative Visualization)
*What is the worst-case scenario, and how will I endure it?*
> **Worst Case:** > **My Response:** I will accept it as nature's will and focus on…

## The View from Above
*Zoom out. How significant is this event in the context of the cosmos or a lifetime?*

---
**Actionable Virtue:** what is the *one* right thing to do right now?
```

### How these fit your PKB Overhaul

Since you are currently fixing metadata:

1.  **Prompt Component:** Gives you a standard `type: prompt-module` tag so you can query your entire library with Dataview.
2.  **First Principles:** Uses standard LaTeX formatting `$$…$$`, ensuring your scientific notes are clean.
3.  **Stoic Journal:** connects directly to your interest in **Self-Regulation** (from your first template request tags).

**Would you like me to create the "Master Instruction Set" template that ties these "Atomic Components" together into a full workflow?**

----
---
use to create apoeriodic review system for monthly and weekly reviews.
# Periodic Notes Creation (Daily, Weekly,Monthly, Yearly)

```
# Periodic Notes Settings:

Daily Notes:
├─ Folder: Periodic/Daily
├─ Format: YYYY-MM-DD
└─ Template: Templates/Daily-Note-Template.md

Weekly Notes:
├─ Folder: Periodic/Weekly  
├─ Format: gggg-[W]WW
└─ Template: Templates/Weekly-Note-Template.md

Monthly Notes:
├─ Folder: Periodic/Monthly
├─ Format: YYYY-MM
└─ Template: Templates/Monthly-Note-Template.md

Quarterly Notes:
├─ Folder: Periodic/Quarterly
├─ Format: YYYY-[Q]Q
└─ Template: Templates/Quarterly-Note-Template.md

Yearly Notes:
├─ Folder: Periodic/Yearly
├─ Format: YYYY
└─ Template: Templates/Yearly-Note-Template.md
```

**Comprehensive Daily Template**:

```markdown
---
date: <% tp.date.now("YYYY-MM-DD", 0, tp.file.title, "YYYY-MM-DD") %>
week: [[<% tp.date.now("gggg-[W]WW", 0, tp.file.title, "YYYY-MM-DD") %>]]
month: [[<% tp.date.now("YYYY-MM", 0, tp.file.title, "YYYY-MM-DD") %>]]
quarter: [[<% tp.date.now("YYYY-[Q]Q", 0, tp.file.title, "YYYY-MM-DD") %>]]
year: [[<% tp.date.now("YYYY", 0, tp.file.title, "YYYY-MM-DD") %>]]
energy: 
mood:
sleep_hours:
tags: [daily-note]
---

# <% tp.date.now("dddd, MMMM Do, YYYY", 0, tp.file.title, "YYYY-MM-DD") %>

## 📅 Temporal Context
- **Week**: [[<% tp.date.now("gggg-[W]WW", 0, tp.file.title, "YYYY-MM-DD") %>]]
- **This Week's Theme**: `= this.week.theme`
- **Monthly Goal**: `= this.month.primary_goal`

## 🎯 Today's Plan

### Big Rock 🎯
- [ ] [Primary outcome for today]

### Supporting Tasks 📝
- [ ] [Supporting task 1]
- [ ] [Supporting task 2]

### Routine Items 🔄
- [ ] Morning review
- [ ] Spaced repetition (20 min)
- [ ] Evening reflection

## ⏰ Time Blocks

| Time | Block | Type | Task |
|------|-------|------|------|
| 9:00-11:00 | Deep Work | 🧠 | [Big Rock work] |
| 11:00-12:00 | Buffer | ☕ | Break / Overflow |
| 12:00-1:00 | Lunch | 🍽️ | Meal + walk |
| 1:00-2:00 | Admin | 📧 | Email / Communications |
| 2:00-4:00 | Learning | 📚 | [Course/Reading] |
| 4:00-5:00 | Integration | 🔗 | Note-making / Linking |
| 5:00-5:30 | Review | 🔍 | Reflection + tomorrow's setup |

## 📊 Tasks Overview

### Due Today

````
```dataview
TASK
FROM "Projects" OR "Areas"
WHERE !completed AND due = this.file.day
```
````

### Can Do Today  

````
```
TASK
FROM "Projects" OR "Areas"
WHERE !completed AND (due = null OR due > this.file.day)
SORT file.name DESC
LIMIT 10
```
````

### Completed Today

````
```
TASK
FROM "Projects" OR "Areas" OR ""
WHERE completed AND completion = this.file.day
```
````

## 📝 Notes & Captures

### Quick Captures
- 

### Ideas
- 

### Observations
- 

## 🔗 Notes Created/Modified Today

````
```
LIST
FROM ""
WHERE file.cday = this.file.day OR file.mday = this.file.day
SORT file.mtime DESC
```
````

## 🌙 Evening Reflection

### Wins 🎉
- 
- 

### Learned 💡
- 
- 

### Challenges ⚠️
- 
- 

### Tomorrow's Priority
- 

### Energy Patterns
**Morning**: 
**Afternoon**: 
**Evening**: 

---
**Previous Day**: [[<% tp.date.now("YYYY-MM-DD", -1, tp.file.title, "YYYY-MM-DD") %>]]
**Next Day**: [[<% tp.date.now("YYYY-MM-DD", 1, tp.file.title, "YYYY-MM-DD") %>]]
````

<% tp.file.cursor() %>

<% tp.system.prompt.(Description of Prompt:)%>
---
---

```
YAML to add to Templates

# Literature-Note Template

---
title: '"<% await tp.system.prompt("Title for YAML") %>"'
id: <% tp.date.now("YYYYMMDD-HHmmss") %>
created: <% tp.file.creation_date('YYYY-MM-DD HH:mm') %>
date: <% tp.date.now('YYYY-MM-DD (dddd)') %>
week: <% tp.date.now('GGGG-[W]WW') %>
type: literature
status: seedling
source: pur3v4d3r
tags:
  - "type/"
  - "#topic/"
  - "#project/"
  - "#source/"
  - "status/draft"
  - "status/seedling"
  - "source/pur3v4d3r"
  - "year/2025"
aliases:
  - Literature
  - Literature-Note
  - Literature Note
link-up: []
link-related:
---

# <% tp.date.now('(dddd) YYYY-MM-DD ') %>
```

```
YYYYMMDD          20251112.md          [[<% tp.date.now("YYYYMMDD") %>]]
YYYY-MM-DD        2025-11-12.md        [[<% tp.date.now("YYYY-MM-DD") %>]]
MM-DD-YYYY        11-12-2025.md        [[<% tp.date.now("MM-DD-YYYY") %>]]
Daily/YYYY-MM-DD  Daily/2025-11-12.md  [[<% tp.date.now("Daily/YYYY-MM-DD") %>]]

# Method 01: Linking to Yesterday's Daily Note
[[<% tp.date.now("YYYY-MM-DD", -1) %>]]
	- Result: [[2025-11-12]]
	  
# Method 02: Link to Tomorrow
[[<% tp.date.now("YYYY-MM-DD", 1) %>]]
	- Result: [[2025-11-11]]
	  
# Method 03: Dynamic Link Title with Pipe (Alias)
[[<% tp.date.now("YYYY-MM-DD") %>|Today's Log]]
	- Result: [[2025-11-12|Today's Log]]

# Method 04: Pretty Link
[[<% tp.date.now("YYYY-MM-DD") %>|<% tp.date.now("dddd, MMMM Do, YYYY") %>]]
	- Result: [[2025-11-22|Wednesday, November 5th, 2025]]
- Note: This link will be displayed as **Wednesday, November 12th, 2025** but links directly to the `2025-11-12.md` file.

# Method 05: Link to Yesterday

[[<% tp.date.now("YYYY-MM-DD", -1) %>|<% tp.date.now("dddd, MMMM Do, YYYY", -1) %>]]

Link to Todays Daily Note Daily Note

- "[[<% tp.date.now("YYYY-MM-DD") %>|Daily Note]]"

Link to Yesterdays Daily Note Daily Note

- "[[<% tp.date.now("YYYY-MM-DD", -1, tp.file.title, "YYYY-MM-DD") %>|Yesterday's Daily Note]]"

```