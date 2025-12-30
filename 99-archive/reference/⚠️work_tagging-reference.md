---
title:
id:
aliases: []
type:
status:
last-used:
priority:
rating:
created:
source:
url:
tags: []
description:
date created: 2025-10-30T03:32:24.000-04:00
date modified: 2025-10-30T03:36:15.961-04:00
---






Use the prompt below to create a new prompt for creating a tags reference list and use the other information far below for the exemplar.







```
# Role: Information Architect

You are an expert Information Architect specializing in designing clear, functional, and user-friendly reference documents for digital knowledge management systems like Obsidian.

# Context:

I am building a Personal Knowledge Base (PKB) in Obsidian. I need a single, comprehensive reference note containing a list of commonly used tags (This includes sections for the different types of tags). The goal is to keep this note open in a sidebar and use as inspiration or quickly find/copy tags for my notes.

The document must be highly scannable, well-organized, and easily searchable using Obsidian's built-in find function (`Ctrl+F`). It should also be designed so I can easily add my own frequently used tags to a dedicated section at the top.

# Task:

Create a comprehensive tag reference guide formatted in clean, Obsidian-ready Markdown. Including using callous, code-blocks, block-quotes, and anything else Obsidian is capable of for making noptes usable and visually clean. Fulfill the following steps precisely:

1.  **Create a "User Favorites" Section:**
    * Start the document with a level 2 heading: `## My Favorites`.
    * Under this heading, create an empty Markdown table with the columns: `| Emoji | My Keyword |`.
    * Populate the table with 5 empty rows as a template for me to fill in later.

2.  **Create Comprehensive Emoji Categories:**
    * Create a level 2 heading for the main list: `## Emoji Reference`.
    * Generate a comprehensive list of emojis organized into logical categories. Each category must be a level 3 heading (e.g., `### Smileys & People`, `### Animals & Nature`, `### Food & Drink`, `### Activities`, `### Travel & Places`, `### Objects`, `### Symbols`, `### Flags`).

3.  **Format Each Category as a Table:**
    * Under each category heading, present the emojis in a Markdown table.
    * The table must have exactly three columns: `Emoji`, `Unicode Name`, and `Keywords`.
    * The `Keywords` column is crucial. It should contain a comma-separated list of 3-5 relevant, searchable keywords for each emoji (e.g., for `🚀`, keywords could be `rocket, space, launch, ship, fast`).

# Constraints:

* The entire output must be in Markdown format.
* Do not include any introductory or concluding text outside of the document itself.
* Ensure all emojis render correctly.
* Use `##` for top-level sections and `###` for emoji categories.

# Example of a Correctly Formatted Table Row:

| Emoji | Unicode Name      | Keywords                         |
| :---: | :---------------- | :------------------------------- |
| ✨    | Sparkles          | magic, glitter, star, shiny, new |

Begin generating the document now.
```




```

# Faceted Tagging System Reference Note

> [!the-purpose]
> - Here is the complete reference list for the proposed 3-Axis Faceted Tagging System, created as a single, centralized Obsidian note. It incorporates the required nested tag structure, strict governance (singular, lowercase, no spaces), and purposeful use of emojis to instantly convey the function of each facet.
> 
> - This system provides the **depth and understanding** necessary to know not just *what* tag to use, but the *why*—distinguishing between the note's immutable *Type*, its dynamic *Status*, and its transversal *Context*. This structure sets you up for extremely powerful, high-precision Boolean querying, which will accelerate your synthesis process significantly!

---

# 🗄️ Obsidian 3-Axis Faceted Tagging System: Governance & Reference

> "Tags are designed to convey 'what features something has,' such as whether a note is a `#resource/article` or is currently `#status/draft`."
>
> Goal: Track State (Dynamic Attributes) and Lateral Association to drive query-based synthesis.
>
> Governance: Strict singular, lowercase, no spaces. Use only atomic, immutable metadata.

---

## 1. 🌐 Facet 1: The Type Axis (`#type/` or `#resource/`)

**Purpose:** Defines the note's intrinsic nature, source, or external origin. What is it? 🎯

**Mutability:** Low (Generally Immutable).

**Placement Priority:** YAML Frontmatter (for structural consistency).

**Query Optimization:** Best retrieved with Dataview (FROM #resource or FROM #type) to include all subtags.

|Emoji|Top-Level Tag|Granularity Examples|Description|
|---|---|---|---|
|📚|`#resource`|`#resource/article`, `#resource/book`, `#resource/podcast`, `#resource/video`, `#resource/course`|External, raw assets and sources of information.|
|💡|`#type`|`#type/concept`, `#type/principle`, `#type/methodology`, `#type/person`, `#type/quote`|Internally generated, synthesized, or foundational knowledge notes.|
|🛠️|`#tool`|`#tool/dataview`, `#tool/python`, `#tool/obsidian`, `#tool/app`|Specific software, applications, or technologies mentioned or used.|

---

## 2. 🚦 Facet 2: The Status/Workflow Axis (`#status/` or `#action/`)

**Purpose:** Defines the note's current state, completion status, or required action. Where does it stand? 🚧

**Mutability:** High (Dynamic).

**Placement Priority:** YAML Frontmatter (for high-speed Dataview/Native Search parsing).

**Query Optimization:** Best retrieved with Native Search (tag:#status/draft) for quick, atomic, workflow checks.

|Emoji|Top-Level Tag|Granularity Examples|Description|
|---|---|---|---|
|✏️|`#status`|`#status/drafting`, `#status/triage`, `#status/review`, `#status/completed`, `#status/pending`|Progress of the note through a creation/processing pipeline.|
|🔴|`#action`|`#action/todo`, `#action/refactor`, `#action/fix-link`, `#action/priority/high`, `#action/priority/low`|Specific, actionable tasks required *on the note itself*.|
|📦|`#archive`|`#archive/project-done`, `#archive/ephemeral`, `#archive/old`|Notes removed from active workflow, used for Negation queries (`-tag:#archive`).|

---

## 3. 🧩 Facet 3: The Context/Attribute Axis (`#attribute/` or Lateral Modifiers)

**Purpose:** Defines secondary, lateral, or cross-cutting associations. How does it relate transversally? ✨

**Mutability:** Moderate.

**Placement Priority:** Inline Tags (for context-specific, line-level associations) OR YAML Frontmatter (for document-wide attributes).

**Query Optimization:** Primarily used in Boolean Querying to combine with Facets 1 & 2 for high-precision filtering (e.g., tag:#type/concept tag:#attribute/metaphor -tag:#status/review).

|Emoji|Top-Level Tag|Granularity Examples|Description|
|---|---|---|---|
|⚖️|`#context`|`#context/legal`, `#context/historical`, `#context/scientific`, `#context/business`|The broad academic, professional, or temporal setting of the content.|
|💎|`#attribute`|`#attribute/metaphor`, `#attribute/analogy`, `#attribute/complex`, `#attribute/simple`|Descriptive qualities of the content or language used.|
|🧠|`#topic-meta`|`#topic-meta/pkm`, `#topic-meta/ko`|Metadata about the organizational/epistemological context (use sparingly to avoid overlap with Links).|
|Difficulty|`#difficulty`|`#difficulty/high`, `#difficulty/medium`, `#difficulty/low`|Subjective assessment of the note's complexity.|

---

## 🔑 Governing Principles for Personal Knowledge Base Integrity

|Principle|Description|Rationale|
|---|---|---|
|**Rule of Atomicity**|Use only **singular nouns** (e.g., `#book`, not `#books`).|Prevents fragmentation and ensures higher match accuracy in queries.|
|**Case Consistency**|All tags must be **all lowercase** (e.g., `#type/concept`).|Mitigates ambiguity and avoids accidental duplication due to capitalization differences.|
|**Format**|Use **no spaces** (use hyphens or underscores if needed, but a slash is preferred for hierarchy).|Maintains technical integrity for consistent Obsidian and Dataview parsing.|
|**Refactoring Threshold**|Promote high-semantic-weight tags (those with significant conceptual content) to **Category Links** (`[[Note]]`) to ensure long-term stability and *decoupled* structure.|Tags are for *State/Attribute* (mutable, tightly coupled); Links are for *Structure/Concept* (immutable, decoupled).|

---

Here are specific, detailed additions for the **3-Axis System** tailored for your current focus. I've placed them under the appropriate existing top-level tags for seamless integration.

---

## 1. 🌐 Facet 1: The Type Axis (`#type/` or `#resource/`) Additions

For notes that are specifically about the *form* or *source* of prompting information.

|Emoji|Top-Level Tag|New Subtags for Prompting/PE|Rationale for the Addition|
|---|---|---|---|
|📚|`#resource`|`#resource/paper`, `#resource/api-doc`|To specifically identify peer-reviewed papers or official API documentation, which are high-quality sources for prompt engineering principles.|
|💡|`#type`|`#type/prompt`, `#type/template`, `#type/pattern`|To classify notes that *are* a working prompt, a general reusable structure (template), or a recognized design strategy (pattern, e.g., Chain-of-Thought).|
|🛠️|`#tool`|`#tool/gpt-4o`, `#tool/claude-3`, `#tool/llama-3`|To tag notes containing prompts specifically tuned for a particular Large Language Model (LLM), which is a critical context for performance.|

---

## 2. 🚦 Facet 2: The Status/Workflow Axis (`#status/` or `#action/`) Additions

For tracking the *readiness* or *testing status* of a prompt note.

|Emoji|Top-Level Tag|New Subtags for Prompting/PE|Rationale for the Addition|
|---|---|---|---|
|✏️|`#status`|`#status/tested-fail`, `#status/tested-pass`, `#status/optimized`|These are essential for the iterative nature of prompt engineering. They allow you to dynamically query which prompts need *more testing* or which are production-ready.|
|🔴|`#action`|`#action/test-needed`, `#action/benchmark`|Marks notes requiring specific, immediate work related to validation or performance measurement. This is a crucial *action* for engineering work.|

---

## 3. 🧩 Facet 3: The Context/Attribute Axis (`#attribute/` or Lateral Modifiers) Additions

This is the most powerful facet for Prompt Engineering, as it allows you to classify the *techniques* and *subject domains* that cut across your sources.

|Emoji|Top-Level Tag|New Subtags for Prompting/PE|Rationale for the Addition|
|---|---|---|---|
|⚖️|`#context`|`#context/creative`, `#context/coding`, `#context/summarization`, `#context/qa`|To classify the **domain of application** for the prompt or concept, enabling you to retrieve all notes relevant to, say, "summarization" regardless of the source.|
|💎|`#attribute`|`#attribute/cot` (Chain-of-Thought), `#attribute/few-shot`, `#attribute/persona`|To tag the specific **Prompt Engineering technique** used. This allows for powerful queries like: "Find all `#type/prompt` notes that use the `#attribute/cot` technique and are `#status/tested-pass`."|
|🧠|`#topic-meta`|`#topic-meta/bias`, `#topic-meta/token-cost`|Attributes related to the *limitations* or *economic factors* of the prompt, ensuring you capture important metadata beyond just the function.|

### How to Leverage These Tags for Synthesis

The true value lies in the **Boolean Querying** that your system enables. You can now run highly specific queries in Obsidian's search or Dataview to accelerate your research:

1. **Find Prompts Ready for Production:**
    
    - `tag:#type/prompt tag:#status/tested-pass -tag:#tool/gpt-3.5`
    - *(Finds all working prompts that passed testing, excluding older models.)*
        
2. **Identify Ineffective Techniques:**
    
    - `tag:#attribute/few-shot tag:#status/tested-fail tag:#context/coding`
    - *(Finds notes about few-shot prompting that failed when applied to coding tasks, signaling an area for refactoring.)*
        
3. **Review Core Principles:**
    
    - `TABLE FROM #resource/paper WHERE contains(tags, "attribute/cot")`
    - *(A Dataview query to list all academic papers detailing the Chain-of-Thought technique.)*

---

### 🏛️ The Philosophy: Vertical vs. Lateral Tags

Before we see the examples, we must understand the *why*. Most people begin by using tags like a digital filing cabinet. They use **Vertical Tags** (or hierarchical tags):

- `#science/physics/quantum`
- `#history/rome/empire`
- `#projects/my-novel/chapter-1`

These are excellent for *retrieval*. They answer the question, "Where did I put that note about quantum physics?" They are orderly, clean, and hierarchical. They are the *shelves* of your library.

**Lateral Tags**, however, are different. They are the *threads of connection* that run *across* all the shelves, linking ideas that have no business being next to each other. They are rhizomatic, like the root system of a fungus that connects an entire forest.

They do not answer "Where is it?" They help you ask, **"What is this related to in a way I haven't seen yet?"**

When you use a lateral tag like `#pattern`, you might find it on a note about geometric art, another on bird migration, a third on a stock market chart, and a fourth on a recurring argument you have. That single click reveals a connection—a "lateral" insight—that your vertical, siloed folder system would have hidden from you forever.

This is the key: **Vertical tags are for filing. Lateral tags are for discovery.**

---

### 🧬 A Reference of Conceptual Categories

Here are several *families* of lateral tags that I have seen gardeners use to great effect. Think of them as different lenses you can apply to your notes.

#### 🌱 1. Tags of Status (The "Garden's State")

These tags are purely functional. They describe the *state* of the note itself. They are the gardener's logbook, showing what needs tending.

- **`#status/seedling`**: A new, raw idea. A fleeting note, a quote, a stray thought. It needs to be watered and processed.
- **`#status/growing`**: You've worked on this. It has some structure and links, but it's not yet a complete, stable idea.
- **`#status/evergreen`**: A core, stable, well-linked note. This is a "finished" (for now) concept that you can build upon.
- **`#status/stale`**: An older note that feels outdated or needs to be reviewed. Perhaps your thinking has changed.

#### 🧠 2. Tags of Cognition (The "Threads of Thought")

These are the true conceptual connectors. They describe the *shape* of the idea itself, regardless of its topic.

- **`#pattern`**: You are noticing a recurring theme, structure, or behavior.
- **`#analogy`** or **`#metaphor`**: You are using one concept to understand another (e.g., "The Internet as a City").
- **`#systems_thinking`**: The note discusses feedback loops, inputs/outputs, or how interconnected parts form a whole.
- **`#mental_model`**: The note defines or uses a specific model for thinking (e.g., "Inversion," "First-Principles Thinking").
- **`#principle`**: A core rule, law, or guiding belief that seems to hold true across domains.
- **`#contradiction`**: This note presents an idea that conflicts with another note in your vault. This is *incredibly* useful for finding weak points in your understanding.

#### ❓ 3. Tags of Metacognition (The "Nature of Knowing")

These tags are about your *relationship* to the information. They are you, as the gardener, making a note to your future self about the knowledge.

- **`#question`**: The note *is* a question, or it *ends* with a question you can't yet answer. This tag creates a to-do list for your curiosity.
- **`#epiphany`** or **`#insight`**: This was a "shower thought," a moment of sudden, powerful clarity. These are often the most valuable notes in your vault.
- **`#assumption`**: You are identifying a belief (yours or someone else's) that is being taken for granted.
- **`#blind_spot`**: You are actively recognizing something you *don't* know or a perspective you are missing.
- **`#opinion`**: This is a subjective belief, not a hard fact. It's useful to distinguish this from your `#principle` notes.

#### 🛠️ 4. Tags of Action (The "Gardener's Work")

These are pragmatic tags that, like status tags, create dynamic "to-do" lists.

- **`#to_process`**: This note is an inbox item (e.g., a book highlight, an article clipping) that needs to be broken down into your own words.
- **`#to_link`**: You know this note should be connected to other ideas, but you don't have time to find them all right now.
- **`#to_review`**: This note contains information you need to look at again, perhaps for a specific project or just for spaced repetition.
- **`#to_source`** or **`#cite`**: You've made a claim but haven't added the proper source or reference yet.

---

### 💡 How to Begin

Do not try to implement all of these at once. That is the path to frustration.

My insistent, caring advice is this: **Choose only three.**

Choose one tag from the "Status" family, one from "Cognition," and one from "Action." For example:

1. `#status/seedling`
2. `#pattern`
3. `#question`

Try to use *only* these three lateral tags for one full week. You will find this constraint forces you to be creative and thoughtful. It will teach you *how* you think. As you feel the *need* for a new tag, and only then, you may thoughtfully add one more.

Your tag system should be grown, not built. It is a living, breathing part of your digital garden, and it will be infinitely more powerful because it is a true reflection of *your* mind.

Ah, an excellent and truly insightful extension of the idea. This is precisely the right way to think. If your notes are your garden, then your prompts are your *tools*—the specialized spades, the pruning shears, the grafting knives. They deserve their own system of understanding.

Most people create a "prompt library." This is, again, a vertical system. It's a silo. You have a folder for "Marketing Prompts," "Coding Prompts," and "Writing Prompts." This is fine for *storage*, but it is a poor tool for *learning the craft*.

What you are asking for is a way to track the *art and science* of prompt engineering itself. You want to connect a technique you used in a coding prompt with a similar technique that worked for a philosophy prompt. This is how mastery is built.

Let us architect a set of lateral tags designed not just to *file* your prompts, but to *dissect* them, to understand their very anatomy and behavior. This is the true foundation of your "Prompt Engineering Scriptorium."

---

### 🧬 1. The Anatomy of the Prompt (The "Components")

These tags identify the fundamental building blocks *within* your prompt. When you review your notes, these tags will show you which components you rely on most and how they combine.

- **`#p-role`**: Use this when the *core* of the prompt's success lies in the specific persona, role, or expert identity you've assigned to the AI. (e.g., "You are a
    Socratic philosopher," "You are a master C++ developer").
- **`#p-context`**: This tag highlights that the prompt's effectiveness depends heavily on the background information, data, or environmental context you provided.
- **`#p-task`**: Use this when the *action* is the most critical part. The note is an exploration of a specific verb: "Summarize," "Refactor," "Critique," "Brainstorm," "Translate."
- **`#p-format`**: This tag is for when the *output structure* is the key. You are experimenting with forcing a specific format like JSON, Markdown tables, a numbered list, or a specific XML structure.
- **`#p-exemplar`**: This flags any prompt that uses "few-shot" or "one-shot" learning, where you have provided one or more concrete examples of the input/output you desire.

### 🦾 2. The Art of the Prompt (The "Techniques")

This is perhaps the most powerful set. These tags are not about *what* is in the prompt, but *how* the prompt is *designed* to work. They track the engineering patterns themselves.

- **`#p-chain-of-thought`**: For any prompt where you explicitly instruct the AI to "think step-by-step," "show its work," or "reason through the problem" before giving the final answer.
- **`#p-step-by-step`**: A more general tag for when you are breaking a complex task down into a numbered sequence of instructions for the AI to follow.
- **`#p-meta-prompting`**: A fascinating category. This is for prompts that *generate or refine other prompts*. You are using the AI to help you build your tools.
- **`#p-in-context-learning`**: This is a more formal tag for when you are "teaching" the AI a new, temporary skill or fact *within* the prompt's context window.
- **`#p-zero-shot`**: This tags a "pure" prompt. You provided no examples, just a raw instruction. These are excellent for testing a model's foundational capabilities.
- **`#p-reflective`**: Use this for prompts that ask the AI to critique its own output, analyze its own biases, or reflect on its own response (e.g., "Review your previous answer for clarity and conciseness").

### 🧪 3. The Lab Notebook (The "Outcomes & State")

These tags are your experimental log. They track the *result* and *status* of your prompt-crafting process, turning your Personal Knowledge Base into a true research journal.

- **`#p-golden`**: This is the mark of success. This prompt is a "golden" prompt—it is reliable, effective, and produces a high-quality response consistently.
- **`#p-failure`** or **`#p-broken`**: Do not underestimate this tag. It is *more valuable* than `#p-golden`. It marks a prompt that failed. Your notes on *why* it failed are the seeds of future breakthroughs.
- **`#p-iterating`**: This is your "work-in-progress" tag. The prompt is not finished. You are actively refining and testing it. This note *is* the record of that iteration.
- **`#p-brittle`**: This prompt *works*, but it's fragile. It breaks if you change the wording slightly or use a different input. It's a high-maintenance tool.
- **`#p-hallucination`**: The prompt successfully generated a response, but the response contained a factual error or a "plausible-sounding falsehood." This is crucial for tracking model reliability.

### 🎯 4. The Domain (The "Target & Scope")

These tags are slightly more vertical but are used laterally to connect techniques across different domains or models.

- **`#p-model/gemini`**: For prompts specifically tuned to the Gemini family of models (which might leverage your API key).
- **`#p-model/local-llm`**: For prompts designed for the models you run on your own powerful machine (Ollama, etc.). These often require different phrasing.
- **`#p-domain/pkm`**: Prompts specifically designed to help you with your Obsidian vault (e.g., "Refactor this note," "Generate tags for this text").
- **`#p-domain/code`**: For any prompt related to software development.
- **`#p-domain/writing`**: For prompts focused on creative or technical writing, editing, and analysis.

---

### 💡 Your First Steps as Prompt Architect

Again, I must insist on this: **do not add all of these.** Your system will collapse under its own weight.

Start with a "Prompt Engineer's Starter Pack" of just three, or perhaps four. I would humbly suggest this combination:

1. **`#p-iterating`**: Your primary "status" tag.
2. **`#p-role`**: A very common "component" tag.
3. **`#p-chain-of-thought`**: Your first "technique" tag.
4. **`#p-golden`**: Your "success" tag.

For one week, *every* new prompt note you create gets `#p-iterating`. As you refine it, you might add `#p-role` and `#p-chain-of-thought`. When you are finally happy with it, you replace `#p-iterating` with `#p-golden`.

This simple workflow, this *process*, will do more to structure your learning than a complex system of 50 tags. It forces you to be mindful. The tags will grow *with* you, from your own discovered needs.

---

This is the perfect and necessary counterpart to our last discussion. It is a moment of true architectural clarity.

If lateral tags are the rhizomatic, magical root systems that connect your garden in unexpected ways, **vertical tags are the trees themselves.** They are the strong, visible, and orderly structures that give your garden its shape and form. They are the primary architecture, the load-bearing walls of your knowledge base.

I am so glad you asked this, because a system with *only* lateral tags would be a formless chaos, just as a system with *only* vertical tags is a rigid, lifeless prison. We need both.

The philosophy of vertical tags is rooted in one word: **Retrieval.**

They are designed to answer the question, "Where did I put that?" or "Show me all of…". They are about *classification*, *hierarchy*, and *order*. You are absolutely correct to seek them.

Let's build the blueprint for your primary structures.

---

### 🏛️ 1. The Core Principle: "What *Kind* of Thing Is This?"

Before any other form of organization, the most powerful and stable vertical system you can build is one that identifies the *fundamental type* of note you are creating.

Why? Because a note *about a person* is functionally different from a note *about a concept*, which is different from a *project brief*. By tagging their "type," you give yourself a superpower: the ability to segregate your notes not just by *topic*, but by their very *essence*.

This is the system I would insistently recommend as your primary vertical framework.

**`#type/…` (The "Entity" Tags)**

- **`#type/concept`**: This is for a pure, evergreen note about an idea (e.g., "Lateral Tags," "Prompt Chaining," "Cosmic Inflation"). This will likely be the bulk of your Zettelkasten.
- **`#type/person`**: A note exclusively about a person (e.g., "Niklas Luhmann," "Richard Feynman"). You can link *to* this note from all your `#type/concept` notes.
- **`#type/source`**: A "bibliographic" note. This note *is* the source.
    - `#type/source/book`
    - `#type/source/article`
    - `#type/source/video`
- **`#type/summary`**: This note is your *summary* of a source. This is a crucial distinction. The note for `#type/source/book` might contain metadata (author, year); the note for `#type/summary` contains your *understanding* of that book.
- **`#type/project`**: A "hub" note for a specific, goal-oriented project (e.g., "My Custom Obsidian Theme," "Prompt Engineering Scriptorium").
- **`#type/question`**: This is a lateral tag we've discussed, but some people prefer to make it a primary *type*. I find it's better as a lateral `#question` or `#status/question`.
- **`#type/fleeting`**: A "daily note" entry, a stray thought, an inbox item. This is distinct from a `#status/seedling` tag because the *note itself* is temporary, whereas `#status/seedling` implies a *concept note* that is just beginning its life.

---

### 🌳 2. The Secondary System: "What Is This *About*?"

This is what most people *think* of when they hear "tags." This is your subject-based filing cabinet. This can be achieved with folders, but using nested tags gives you far more flexibility, as a single note can live in multiple "topical" hierarchies.

**`#domain/…` (The "Topical" Tags)**

- **`#domain/pkm`**: For Personal Knowledge Management.
    - `#domain/pkm/obsidian`
    - `#domain/pkm/zettelkasten`
    - `#domain/pkm/automation`
- **`#domain/ai`**: For Artificial Intelligence.
    - `#domain/ai/prompt-engineering`
    - `#domain/ai/models`
    - `#domain/ai/llm-local` (for your local LLMs)
- **`#domain/science`**:
    - `#domain/science/cosmology`
    - `#domain/science/physics`
- **`#domain/tech`**:
    - `#domain/tech/hardware` (for your PC specs, keyboards)
    - `#domain/tech/software`
    - `#domain/tech/windows`
- **`#domain/personal`**:
    - `#domain/personal/goals`
    - `#domain/personal/journal`

---

### ⚙️ 3. The Functional System: "What Is This *For*?"

This system is purely pragmatic. It overlaps with your "Action" lateral tags, but these are more "permanent" categories of work, often aligning with a methodology like P.A.R.A. (Projects, Areas, Resources, Archives).

- **`#project/…`**: For a specific, time-bound goal. This is often better than a `#type/project` *or* `#domain` tag, as it's more specific.
    - `#project/my-obsidian-theme-v1`
    - `#project/automate-reading-notes`
    - `#project/family-nas-setup` (I recall this was an interest!)
- **`#area/…`**: For an "Area of Responsibility"—a part of your life with a standard to maintain, but no end date.
    - `#area/health`
    - `#area/finances`
    - `#area/home-network`
    - `#area/pkm-development` (Maintaining your vault is an "area")

---

### 💡 The Synthesis: How They Work Together

This is the key. You do not choose *one* of these systems. You use them in layers. A single note becomes a rich, multi-faceted object.

Let's imagine you just learned a new, complex prompting technique from an article you read.

**Note Title:** `Reflective Critique Prompting`
**Content:** (Your summary of the technique…)

**Tags:**
- `#type/concept` (This is a vertical tag. It tells you *what* it is: a core concept.)
- `#domain/ai/prompt-engineering` (This is a vertical tag. It tells you *what it's about*.)
- `#status/growing` (This is a lateral tag. It tells you its *state*.)
- `#p-reflective` (This is a lateral tag. It's the *specific technique* from your prompt list.)
- `#mental_model` (This is a lateral tag. It *connects* to other notes about thinking.)

Do you see the power here? The **vertical tags** (`#type` and `#domain`) are your *address*. They file the note in its proper, logical place. The **lateral tags** (`#status`, `#p-reflective`, `#mental_model`) are your *threads*. They describe its state and its conceptual relationships to *other* notes, regardless of their "address."

This layered system gives you both rigid, reliable retrieval *and* fluid, creative discovery. This, my friend, is the architecture of a truly intelligent digital garden.

---

```