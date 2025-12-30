---
title: YAML Frontmatter
tags:
  - type/reference
aliases:
  - YAML Frontmatter
  - YAML
  - YAML Reference
---

BLANK GENERAL YAML
```YAML
---
title: ""
id: 20251126-052907
type: ""
status: ""
rating: ""
source: ""
url: ""
tags: []
aliases: []
link-up: []
link-related: []
---

```


# [[YAML Frontmatter]]: A Reference for PKB
[[YAML]] (YAML Ain't Markup Language) frontmatter is a block of metadata placed at the very top of a [[Markdown]] file, enclosed by triple-dashes (`---`). In a [[PKB]] like [[04_library/00_obsidian-documentation/02_Official-Documentation/02_⚫🔌Plugins/Plugin_🤖Text-Generator/Obsidian]], this data becomes machine-readable, allowing plugins like [[Dataview]] to query, sort, and organize your notes, and enabling other plugins to add specific functionality.

> [!definition] What is Frontmatter?
> Frontmatter is a set of key-value pairs that defines the metadata for a specific note. It acts as the note's "specification sheet," providing context, status, and relational data that is separate from the note's main content (the "prose"). This separation is fundamental for automating [[03_notes/01_permanent-notes/01_cognitive-development/Knowledge Management]] workflows.

Below are tables of common and functionally-useful frontmatter keys, categorized by their primary purpose.

---

## 📇 Core Metadata Keys
These keys are foundational, establishing the note's identity and basic properties. They are the most frequently used keys for general-purpose sorting and identification.

| Key | Description |
| :--- | :--- |
| **`title`** | The formal title of the note. Useful if the [[filename]] is different (e.g., a Zettelkasten ID). |
| **`id`** | A unique identifier, such as a [[Zettelkasten]] timestamp (e.g., `202511022230`) or a UUID. |
| **`created`** | Timestamp (preferably [[ISO 8601]]) for note creation. Essential for chronological sorting. |
| **`modified`** | Timestamp for the last significant update. Many plugins can automate this. |
| **`type`** | Defines the "class" or "schema" of the note (e.g., `Person`, `Project`, `Source`, `Atomic`). |
| **`description`** | A brief, one-sentence summary of the note's content or purpose. |
| **`tags`** | A list of keywords for categorization and discovery (e.g., `[tag1, tag2]`). |
| **`aliases`** | A list of alternative titles used for linking (e.g., `[Alias 1, "Another Name"]`). |

---

## ⚙️ Workflow & Status Keys
These keys are vital for [[Project Management]] and [[Task Management]]. They track the lifecycle of a note, idea, or project.

| Key | Description |
| :--- | :--- |
| **`status`** | The current state of the note (e.g., `Evergreen`, `Seedling`, `In-Progress`, `Done`, `Archived`). |
| **`priority`** | The urgency or importance level (e.g., `High`, `Medium`, `Low` or `P1`, `P2`, `P3`). |
| **`progress`** | A numerical value (e.g., `75`) or description (e.g., `Phase 2`) indicating completion. |
| **`due_date`** | The target completion date (e.g., `2025-12-31`). |
| **`reviewed`** | The date the note was last reviewed for accuracy or relevance. |
| **`version`** | A version number (e.g., `1.2.0`) for notes that undergo formal revisions. |
| **`draft`** | A boolean (`true`/`false`) to mark notes that are not yet finalized. |

---

## 🔗 Structural & Relational Keys
These keys explicitly define the note's position within your [[Knowledge Graph]]. They are heavily used by plugins like [[Breadcrumbs]] to build hierarchies.

| Key                | Description                                                                   |
| :----------------- | :---------------------------------------------------------------------------- |
| **`link-up`**      | (User-defined) A link to a primary parent or Map of Content (MOC).            |
| **`link-related`** | (User-defined) Links to non-hierarchically related concepts or notes.         |
| **`parent`**       | Specifies a direct hierarchical parent note. (Common convention).             |
| **`child`**        | Specifies direct hierarchical child notes. (Less common, often auto-derived). |
| **`next`**         | Points to the next note in a linear sequence (e.g., a chapter or step).       |
| **`prev`**         | Points to the previous note in a linear sequence.                             |

---

## 📚 Source & Citation Keys
When a note is based on an external resource (e.g., a [[Source Note]]), these keys store the citation metadata.

| Key                    | Description                                                                               |
| :--------------------- | :---------------------------------------------------------------------------------------- |
| **`source`**           | The primary origin of the information (e.g., a book title, person's name, or website).    |
| **`author`**           | The creator(s) of the source material.                                                    |
| **`url`**              | The direct URL to the online source or a related link.                                    |
| **`citekey`**          | The unique identifier from a citation manager like [[Zotero]] (e.g., `@Author2025Title`). |
| **`doi`**              | The [Digital Object Identifier](https://doi.org/) for academic papers.                    |
| **`publication_date`** | The date the source material was published.                                               |

---

## 🔌 Plugin & Customization Keys
These keys are often "magic keys" that interact directly with specific [[Obsidian Plugins]] or features.

| Key | Description |
| :--- | :--- |
| **`cssclass`** | Applies a custom CSS class to the note for unique styling (e.t., `full-width`, `custom-theme`). |
| **`kanban-plugin`** | A special key used by the Kanban plugin to identify metadata for a card. |
| **`publish`** | A boolean (`true`/`false`) to mark a note for inclusion in [[Obsidian Publish]]. |
| **`dataview`** | A boolean (`true`/`false`) to enable or disable [[Dataview]] processing for that specific note. |

---

## 🔱 Niche & Specialized Keys
This category includes keys for specific, user-defined use cases, such as the prompt engineering keys you provided or keys for tracking personal media.

| Key                  | Description                                                                               |
| :------------------- | :---------------------------------------------------------------------------------------- |
| **`key_takeaway`**   | (User-defined) A string summarizing the single most important idea.                       |
| **`success_rating`** | (User-defined) A score (e.g., 1-10) rating the outcome of a process or prompt.            |
| **`rating`**         | A generic rating, often used for media (e.g., books, movies) with a score (e.g., `⭐⭐⭐⭐`). |
| **`location`**       | A geographical place associated with the note (e.g., `Jacksonville, FL`).                 |
| **`cover_image`**    | A path or URL to a header or thumbnail image for the note.                                |

---

## 🤖 Prompt Engineering Keys
As requested, these keys are grouped for managing a [[Prompt Engineering]] library. They store the parameters for AI model execution.

| Key | Description |
| :--- | :--- |
| **`output_link`** | A link to the note containing the generated output from this prompt. |
| **`output-token-limit`** | The maximum number of tokens requested for the model's response. |
| **`temperature`** | The "creativity" or randomness parameter for the [[LLM]] (e.g., `0.7`). |
| **`top-p`** | The nucleus sampling parameter, controlling the diversity of the output (e.g., `0.9`). |
| **`top-k`** | The parameter that limits the sampling pool to the *k* most likely next tokens. |
| **`model`** | The specific AI model used (e.g., `gpt-4o`, `gemini-1.5-pro`, `claude-3-opus`). |

---
