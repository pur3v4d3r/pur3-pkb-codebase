---
title: Symbiotic Relationship Between Metadata Structure (Yaml Frontmatter vs. Inline Fields)
id: "20251120092538"
type: pkb/pkm/report
status: not-read
source: 👾Polymath_v3.2_♊Gem-ID_OQHJPSLYU0
created: undefined
year: "[[2025]]"
tags:
  - pkm
  - project/pur3v4d3r
  - year/2025
  - self-improvement
  - pkb/metadata/frontmatter
  - pkb/maintenance/refactoring
  - pkb/maintenance/cleanup
aliases:
  - Dataview Query Architecture,Obsidian Metadata Strategy,YAML vs Inline Fields for Dataview
link-up:
  - "[[project-pur3v4d3r-moc]]"
link-related:
  - "[[2025-11-20|Daily-Note]]"
---






# ✨ An Investigation into the Symbiotic Relationship Between Metadata Structure (YAML Frontmatter vs. Inline Fields) and the Efficacy of Dataview Queries, Analyzing Strategies for Designing a Scalable and Consistent Data Architecture within an Obsidian Vault

> [!abstract]
> This report provides a comprehensive analysis of the two primary metadata systems used within Obsidian, YAML frontmatter and Dataview inline fields, and their symbiotic relationship. We explore the fundamental differences in their nature, moving from a "file-level" versus "content-level" paradigm. The central thesis is that these two systems are not adversarial but are complementary components of a robust data architecture.
>
> We will dissect the "how" and "why" of each system, examining their syntax, their intended use cases, and, most critically, how the Dataview plugin ingests and "flattens" them into a single, queryable data object for each note. This analysis reveals critical nuances, such as the potential for data conflicts and the impact on query performance at scale.
>
> The ultimate goal of this document is to move beyond simple definitions and provide actionable strategies for designing a scalable, consistent, and low-friction data architecture. We will demonstrate how a "YAML-first" approach for a note's identity, enforced by templates, combined with the surgical use of inline fields for contextual, in-text data, creates a system that is both powerfully structured and organically flexible. This hybrid model leverages the strengths of both metadata types to build a "second brain" that is not just a repository of information, but a dynamic, queryable database for knowledge generation.

## 1. 🗺️ Introduction & Context

In the ecosystem of Personal Knowledge Management (PKM), Obsidian has emerged as a powerhouse, distinguished by its philosophy of local-first, plain-text files. On their own, Markdown files are simple, portable, and human-readable. They are digital notebooks. However, the true "magic" of Obsidian lies in its plugin community, and no plugin has so fundamentally transformed the user's relationship with their notes as **Dataview**.

Dataview performs a kind of digital alchemy. It transmutes a simple folder of text files into a dynamic, queryable database. Suddenly, your notes are not just static documents; they are "rows" in a database you can sort, filter, and display at will. You can create tables of unfinished projects, lists of books from a specific author, or dashboards of your daily habits, all of which update automatically.

But this magic has a prerequisite. Like any database, it requires a clear, consistent data structure. You must provide your notes with *metadata*—data about your data—for Dataview to read. In Obsidian, this metadata can be added in two primary ways: within the **YAML frontmatter** block at the very top of a file, or as **inline fields** scattered throughout the note's body.

> [!the-purpose]
> The purpose of this investigation is to provide a deep, first-principles understanding of these two metadata systems. We will not merely state what they are, but explore *why* they exist, *how* they function differently, and *how their relationship dictates the power, performance, and scalability* of your entire knowledge base. This report is a guide to making deliberate, architectural decisions that will prevent data chaos and unlock the full potential of a Dataview-driven vault.

This choice between YAML and inline fields is not a trivial matter of preference. It is the foundational architectural decision you will make. A poorly designed system will lead to inconsistent data, broken queries, slow performance, and high "friction"—the cognitive load required to maintain your system. A well-designed system, however, feels effortless. It becomes an extension of your own mind, allowing you to find, connect, and generate insights with fluid precision.

> [!pre-read-questions]
> Before we proceed, consider the following:
> - What is the conceptual difference between data *about* a note (e.g., its creation date) and data *within* a note (e.g., a decision made in a meeting)?
> - If you were to design a database, would you want your "column names" to be consistent? What happens if one note uses `status: complete` and another uses `state: done`?
> - How do you think a plugin like Dataview "finds" a piece of data hidden in the middle of a 5,000-word essay? What might be the "cost" of that search?

Thinking through these questions will prime you for the core concepts we are about to explore: the fundamental dichotomy between file-level and content-level data, and the non-negotiable importance of consistency for scalability.

## 2. 📜 Historical Context & Intellectual Lineage

To understand *why* we have two competing systems, we must look at how they evolved. Their existence is not the product of a single, unified design, but rather a convergence of different technologies solving different problems.

**1. The Rise of YAML Frontmatter (The "File Header")**

The concept of a "frontmatter" block was not invented by Obsidian. It was popularized by static site generators (SSGs) like **Jekyll** and later **Hugo**. A website might be built from hundreds of blog post files in Markdown. The SSG needed a way to know the `title`, `author`, `publication_date`, and `tags` for each post to properly render the website, create archive pages, and sort content.

The solution was to place a small, machine-readable "header" at the very top of the text file, separated by `---` delimiters. The language chosen was **YAML** (an acronym for "YAML Ain't Markup Language") because it is exceptionally human-readable, clean, and powerful enough to handle lists and nested data.

When Obsidian was created, it adopted this existing, well-established convention. This was a brilliant move, as it made Obsidian compatible with a vast ecosystem of other text-based tools. From the very beginning, this data was understood to be *metadata about the file itself*. It was the note's digital identity card.

**2. The Dataview Innovation (The "Content Query")**

YAML frontmatter was excellent for note-level identity, but it was inflexible. What if you wanted to track data *within* the flow of your writing? What if a single meeting note contained *ten* separate decisions or action items, each with its own due date? Adding all of these to the YAML frontmatter would be clumsy, chaotic, and, most importantly, *divorced from their context*.

This is the problem the Dataview plugin set out to solve. It introduced its own, proprietary syntax: the **inline field**.

- `Key:: Value`
- `[Key:: Value]`
- `- [ ] (due:: 2025-10-20)`

This syntax allowed a user to "tag" a piece of data *at the exact point it appeared in the text*. That `(due:: ...)` date isn't *about the note*; it's about the *task* it's written next to. This was a revolutionary leap. It enabled a new, more granular, and contextual way of tracking information.

**3. The Present Day: The "Properties" Convergence**

For years, users had to manually type their YAML. This was prone to typos and inconsistency. Recently, the Obsidian developers introduced a core feature called **Properties**. This is, quite simply, a beautiful graphical user interface (GUI) built directly on top of the YAML frontmatter.

It provides a "Properties" view at the top of the note, allowing you to edit YAML fields with dropdown menus, date pickers, and checkboxes. This feature *does not replace YAML*; it *is* YAML. It is a powerful endorsement from the Obsidian team, signaling that YAML frontmatter is the "official," first-class-citizen method for structured, note-level metadata.

This evolution has left us with a clear, two-part system:

- **YAML (via Properties):** The "official" system for note-level data.
- **Dataview Inline Fields:** The "specialist" system for content-level, contextual data.

Understanding this history is key. They were built for different purposes, and a truly effective system must respect this original design intent.

---

### **Core Analysis: An In-Depth Exposition**

---

## 3. 📖 Foundational Principles: The "Why"

To build a scalable architecture, we cannot simply copy what others do. We must understand the underlying principles. The "symbiotic relationship" of our topic rests on three core ideas.

> [!principle-point]
> **Principle 1: The "File vs. Content" Dichotomy**
> This is the single most important concept to grasp. You must differentiate between data *about the file* (its identity) and data *contained within the file* (its content).

YAML frontmatter and inline fields are designed to serve these two distinct masters.

> [!analogy]
> **The Book Analogy**
>
> - Think of a single note (`.md` file) as a **physical book**.
> - **YAML Frontmatter is the book's cover and its copyright page.** It contains data *about the book as a whole*: its `Title`, its `Author`, its `ISBN`, its `Publication Date`, its `Genre`. This data is singular and definitive for the entire object. You would never list a *single character's name* on the cover.
> - **Inline Fields are the notes, highlights, and marginalia you write *inside* the book.** On page 42, you might highlight a sentence and write in the margin: `(Key-Takeaway:: This is the central thesis)`. On page 97, you might circle a character's name and write `[Character-Appearance:: Frodo Baggins]`.
> 
> This distinction is intuitive. The YAML describes *what the note is*. The inline fields describe *what the note contains*. A truly scalable system *never* confuses the two. You would not put `(Key-Takeaway:: ...)` in your YAML, and you would not put your note's `Author:: ...` in the middle of a paragraph.

> [!principle-point]
> **Principle 2: The Axiom of Consistency**
> A database is only functional if its schema is consistent. In database terms, a "column" must have the same name and data type for every "row."

Dataview treats your notes as "rows" and your metadata keys as "columns." If you have 100 notes about projects, you *must* have a single, consistent key to track their status.

- **Good (Consistent):** `status: "in-progress"`
- **Bad (Inconsistent):** `status: "in-progress"`, `state: "running"`, `progress: "underway"`

If you use three different keys, you have created three different "columns" in your database. A query for "all notes *in progress*" would have to be `WHERE status = "in-progress" OR state = "running" OR progress = "underway"`. This is a brittle, unscalable mess.

> [!key-claim]
> **Scalability is a direct and non-negotiable function of consistency.**
>
> YAML frontmatter, especially when combined with templates, is inherently designed for consistency. You can create a "Project Template" that *forces* every new project note to have a `status:` field. Inline fields, by their very nature, are "wild." They are typed manually, in the flow of writing, and are highly susceptible to typos (`due::` vs `duee::`) and synonym-creep (`due::` vs `deadline::`).

> [!principle-point]
> **Principle 3: Query "Cost" and Performance**
> Not all queries are created equal. The "cost" of a query refers to the computational effort required to find the answer. At a small scale (a few hundred notes), this is irrelevant. At a large scale (tens of thousands of notes), it can be the difference between a table that loads instantly and one that chokes your device.

- **YAML (Properties):** This metadata is formally indexed by Obsidian itself. It's stored in a clean, structured way. When Dataview runs a query, it can often hook into this "master index" to find all notes with `type: "book"` very, very quickly. It's like looking at the `Genre` labels on the spines of the books in our library.
- **Inline Fields:** This metadata is *not* formally indexed by Obsidian. It is just text inside a file. For Dataview to find `(rating:: 5/5)`, it must *read the entire text content* of every single file within your query's scope. This is a *much* more "expensive" operation. It's like *opening every book in the library and reading every single page* just to find your marginalia.

This principle doesn't mean inline fields are "bad"; it means they must be used *surgically*. Use YAML to do the "heavy lifting" (e.g., `FROM #books`) and let inline fields pull specific data *after* the note list has been filtered.

## 4. 🛠️ Mechanisms & Processes: The "How"

To master these systems, we must understand their mechanics. How are they written, and more importantly, how does Dataview *read* them?

### 4.1 YAML Frontmatter: The Structured Header

This is the metadata block at the top of the file, enclosed by `---`.

> [!definition]
> **YAML (YAML Ain't Markup Language):** A human-readable data serialization standard. It uses `key: value` pairs. Indentation (with spaces, not tabs) is used to denote nested data (objects) and hyphens are used to denote lists (arrays).

> [!example]
> A YAML block for a literature note might look like this:
> ```yaml
> ---
> title: "The Structure of Scientific Revolutions"
> author: "Thomas S. Kuhn"
> type: "book"
> status: "read"
> rating: 5
> tags:
>   - "science/philosophy"
>   - "sociology"
> created: "2025-10-15T10:00:00"
> related:
>   - "[[Paradigm Shift]]"
>   - "[[Normal Science]]"
> ---
> ```
> - `title`, `author`, `type`, `status`, `rating`, `created` are all simple key-value pairs.
> - `tags` and `related` are *lists* (arrays).

**How Dataview Queries It:**
In a Dataview query, you access these fields directly.
- **DQL (Dataview Query Language):** `TABLE author, rating FROM #books WHERE status = "read"`
- **DataviewJS:** `dv.pages('#books').where(p => p.status === "read").table(...)`

Notice that `p.status` directly accesses the `status:` key. It's clean, 1-to-1, and highly predictable.

### 4.2 Inline Fields: The Contextual Annotations

These are Dataview-specific fields written anywhere in the body of the note.

> [!definition]
> **Inline Field:** A key-value pair formatted in one of three ways that the Dataview plugin is specifically programmed to find and parse from your note's text content.

**The Three Syntaxes:**
1. **`Key:: Value` (Double-Colon):** This is the most common form. It is visible in both editing and reading modes. `Project:: [[Project Phoenix]]`
1. **`[Key:: Value]` (Brackets):** This is also visible in both modes. Often used to feel more like a "tag." `[Mood:: 7/10]`
1. **`(Key:: Value)` (Parentheses):** This is the "hidden" syntax. In reading mode, the `(Key:: ...)` part is hidden, and only the `Value` is shown (if it's a link). This is excellent for "annotating" text without cluttering the final view.

> [!example]
> A meeting note's body:
>
> `### Agenda`
> `- Discuss marketing budget. (Owner:: [[Sarah P.]])`
>
> `### Notes`
> `- The team agrees to move forward. (decision:: Proceed with alpha test)`
> `- We must finalize the report by next Friday. - [ ] Finalize report (due:: 2025-10-25)`
>
> Here, `Owner`, `decision`, and `due` are all inline fields.

### 4.3 The "Flattening" Model: How Dataview Sees Your Vault

This is the most critical, and most misunderstood, mechanism. When Dataview initializes, it scans your vault and creates an *in-memory data object* for every single note. It "flattens" all metadata sources into one object.

> [!analogy]
> **The Data Collector**
>
> Imagine Dataview is a researcher building a profile for every note in your vault.
>
> 1.  **Step 1 (YAML):** The researcher first looks at the **cover (YAML)** of the note. They write down all the fields: `type: "book"`, `status: "read"`.
> 1.  **Step 2 (Inline):** Then, the researcher *opens the note* and **reads every single page (the content)**. They find your marginalia: `(Key-Takeaway:: Thesis is weak)`. They add this to their clipboard.
> 1.  **Step 3 (Implicit Fields):** Finally, the researcher adds the file's *own* properties: `file.name`, `file.path`, `file.tasks`, etc.
> 
> The final "profile" for that note is a *single, flat object* containing all of these fields:
> ```json
> {
>   "type": "book",
>   "status": "read",
>   "Key-Takeaway": "Thesis is weak",
>   "file": { ... }
> }
> ```
> This is why, in a query, you can access `p.status` (from YAML) and `p.Key-Takeaway` (inline) in the exact same way. Dataview *hides* this complexity from you.

> [!important]
> **The "Override" Rule: A Critical Pitfall**
>
> What happens if there is a conflict?
> - **YAML:** `status: "reading"`
> - **Inline:** `status:: "done"`
> 
> When Dataview builds its profile, **inline fields *override* frontmatter fields if they have the same key.**
>
> In the example above, Dataview will report the note's status as `"done"`. This is a massive source of confusion and "broken" queries. A user will look at their YAML, see `status: "reading"`, but the query will behave as if it's "done" because an inline field is hiding somewhere in the note's body.
>
> This mechanism *enforces* our architectural principle: **Never use the same key in YAML and inline.** The systems must be separate. YAML is for the "columns" of your database. Inline fields are for *new*, *different*, contextual data.

## 5. 🔬 Strategies for a Scalable Architecture: The "Symbiosis"

Now we move from theory to practice. A scalable and consistent architecture is a *symbiotic* one. It uses both systems for their intended purpose.

### 5.1 Strategy 1: The YAML-First "Note Schema" (The Architect)

Your primary data structure must be in YAML. This is the "Architect" part of your system—it is top-down, planned, and ruthlessly consistent.

1. **Define Your Note Types:** Decide on the major "types" of notes you have. Common examples: `person`, `project`, `meeting`, `book`, `article`, `daily-note`.
1. **Create a Schema:** For each type, define the *required* and *optional* metadata.
1. **Enforce with Templates:** Use the **Templater** plugin (or core templates) to create a template for each note type. When you create a "New Project Note," it should *automatically* insert the correct YAML block.

> [!example]
> **Template for `type: "project"`:**
> ```yaml
> ---
> type: "project"
> status: "planning"
> manager: ""
> due:
> tags: ["project"]
> ---
> ```
> This *solves* the consistency problem. You will *never* misspell `status` or forget to add it. Your queries for `TABLE ... FROM #project` will always be reliable. Use the core Properties UI to make filling in these fields even easier.

**YAML is for:** `type`, `status`, `created`, `due`, `author`, `source`, `rating`, `aliases`, `tags`... anything that defines *what the note is*.

### 5.2 Strategy 2: The "Contextual Data" Inline Model (The Gardener)

This is the "Gardener" part of your system—it is bottom-up, organic, and flexible. Use inline fields *only* for data that:

a) Is contextual to a specific line of text.

b) Appears multiple times in one note.

**Inline Fields are for:** `decision::`, `action-item::`, `quote-rating::`, `argument::`, `(mood:: 7/10)`, `(energy:: high)`.

> [!example]
> **A Literature Note on a book:**
> - **YAML** contains: `author: "Thomas S. Kuhn"`, `status: "read"`.
> - **Body of the note** contains:
>     - "...he calls this 'normal science,' which is the puzzle-solving that happens within an established framework. [key-concept:: normal science]"
>     - "...the shift from one to another is a 'paradigm shift.' [key-concept:: paradigm shift]"
>     - "...Kuhn argues that competing paradigms are 'incommensurable.' (critique:: This is his weakest point, seems to deny objective comparison.)"
> 
> This is a perfect symbiosis. The YAML identifies the note as a book. The inline fields tag specific concepts and critiques *where they appear*.

### 5.3 Strategy 3: The Hybrid Query (The Symbiosis in Action)

The true power is unleashed when your queries use *both* systems at once. You use the fast, reliable YAML fields to *filter* your list of notes, and then use the contextual inline fields to *extract* the specific data you want.

> [!example]
> **Goal:** "Show me all *key concepts* I identified in *philosophy books* I've *read*."
>
> **Query (DQL):**
> ```dataview
> TABLE key-concept
> FROM #books 
> WHERE status = "read" AND contains(tags, "philosophy")
> FLATTEN key-concept
> ```
>
> **Let's break this down:**
> 1.  `FROM #books`: This first filter uses the `tags` field in **YAML**. It's fast and reliable.
> 1.  `WHERE status = "read" AND contains(tags, "philosophy")`: This further filters the list using two more **YAML** fields. Dataview now has a small, accurate list of notes to work with.
> 1.  `TABLE key-concept`: Now, and *only* now, Dataview "opens" those few matched notes and searches their content for the **inline field** `key-concept::`.
> 
> This is the symbiotic architecture. The YAML is the "database" that does the heavy lifting (filtering 10,000 notes down to 50). The inline fields provide the "marginalia" that you extract from just those 50 notes.

## 6. 🌍 Broader Implications & Significance: The "So What"

This discussion is not merely a technical debate for plugin-tinkerers. The data architecture you choose fundamentally defines the nature and power of your "second brain."

- **Low Friction, High Signal:** A well-designed system (YAML-first, enforced by templates) *reduces cognitive load*. You don't waste time remembering "What did I call my status field?" You just create a new note, fill in the blanks, and trust that Dataview will find it. You spend your time *thinking*, not *organizing*.
- **Future-Proofing Your Vault:** YAML is an open, universal standard used by hundreds of tools. If you build your core metadata on YAML, your vault is portable. You could move to a different tool in 10 years and your `author:`, `status:`, and `tags:` fields will be instantly understood. Dataview's `Key:: Value` syntax is proprietary. If the plugin were to be abandoned, those fields would just be inert text. This is a strong argument for a YAML-first architecture.
- **The "Designed Garden":** This resolves the "Architect vs. Gardener" debate in PKM. You should not be one or the other; you must be both. Your vault should be a "designed garden."
    - **The Architect (YAML):** Lays down the stone paths, defines the flower beds, and installs the irrigation. This is the top-down structure that gives the garden its form and function.
    - **The Gardener (Inline):** Walks the paths and plants individual flowers, herbs, and bushes where they make the most sense. This is the bottom-up, organic growth that fills the garden with life and context.

Your YAML schema is the architecture. Your inline fields are the organic plantings. Together, they create a system that is both structured and alive.

---

## 7. ⏳ Current Landscape & Unanswered Questions

The landscape of metadata in Obsidian is currently being defined by one, massive change: the **core "Properties" feature**.

As mentioned, this feature is a GUI for YAML frontmatter. Its impact is profound:

1. **Validation of YAML:** It confirms that the Obsidian team views YAML as the primary, enduring, and "correct" place for structured metadata.
1. **Lowering the Barrier:** It removes the "scary" text-based nature of YAML. New users can now add consistent metadata from day one using visual menus.
1. **Enforcing Consistency:** It introduces "property types" (Text, List, Number, Checkbox, Date). This is a game-changer. You can define `rating` as a Number type, and the UI will prevent you from accidentally entering "Good" instead of `5`.

> [!question]
> **Does the new "Properties" feature make inline fields obsolete?**
>
> [!counter-argument]
> **No, it simply clarifies their role.**
>
> The Properties feature makes YAML *even better* at being the "database of record." It reinforces that any singular, note-level data (like `due:` or `rating:`) should absolutely be in the YAML.
>
> But this does not solve the "marginalia" problem. It does not help you tag 10 different `(decision:: ...)` items next to the 10 paragraphs where those decisions were recorded. The role of inline fields is not *removed*; it is *focused*. They are now, more than ever, purely for **contextual, in-text, repeating data points**, while YAML handles everything else.

The future of Dataview will likely involve deeper integration with this core Properties index, making YAML-based queries even faster and more powerful.

## 8. 🗝️ Conclusion & Key Takeaways

The relationship between YAML frontmatter and inline fields is not a rivalry, but a **symbiosis of specialization**. To build a scalable, consistent, and powerful Obsidian vault, you must embrace this "designed garden" philosophy.

> [!summary]
> **Key Takeaways for Your Data Architecture:**
>
> - **Principle 1: Differentiate Your Data.** YAML (Properties) is for *structured, note-level* metadata (data *about* the note; the "book cover"). Inline fields are for *contextual, in-text* data (data *within* the note; the "marginalia").
> - **Principle 2: Consistency is King.** Scalability is impossible without consistency. Your most important keys (e.g., `status`, `type`, `due`) must be consistent across your entire vault.
> - **Strategy: Be a YAML-First Architect.** Define your core note types and their metadata fields. Use **Templates** to enforce this schema rigorously. This is the non-negotiable foundation of your vault.
> - **Strategy: Be a Contextual Gardener.** Use **inline fields** *surgically* for data that is either deeply contextual (e.g., `(critique:: ...)` next to a quote) or appears multiple times in a single note (e.g., `(action-item:: ...)`).
> - **Critical Pitfall: Avoid Key Conflicts.** *Never* use the same metadata key in your YAML and inline. Dataview's override rule (inline wins) will cause unpredictable bugs. Use YAML for `status`, and if you need an inline status, call it `task-status` or something unique.
> - **The Hybrid Query is the Goal.** The most powerful queries use YAML to *filter* the notes (fast, efficient) and inline fields to *extract* the data (contextual, specific).
> - **Embrace "Properties."** Obsidian's new core feature is a powerful endorsement of the YAML-first model. Use it to manage your note's identity with ease and consistency.

By respecting this symbiotic relationship, you move from being a simple "note-taker" to a "knowledge-architect." You create a system that scales with you, reducing friction and amplifying your ability to connect ideas and generate new insights.

## 9. 🦖 Active Reading & Reflection (The Feynman Technique)

> [!ask-yourself-this]
> - **Explain It Simply:** How would you explain the difference between YAML (Properties) and inline fields to a brand-new Obsidian user using an analogy *other* than the "book" one? (Perhaps a "person" and their "thoughts"?)
> - **Identify Core Concepts:** What are the three most important *risks* of a poorly designed metadata system? (e.g., data conflict, query failure, inconsistency). Define each in your own words.
> - **Challenge & Connect:** Look at your current vault. Find one example of metadata you are using in a "sub-optimal" way based on this report. (e.g., are you using an inline field like `type:: book` when it should be in YAML?). What is your plan to fix it?
> - **The Next Step:** Design a "Note Schema" for one of your most common note types (e.g., `person` or `project`). What 5 YAML fields are *essential* for that note type? Create a template for it.

## 10. 📚 References

> [!cite]
> Dataview. (2024). *Dataview Documentation - Data Fields*. Obsidian Dataview. Retrieved from <https://blacksmithgu.github.io/obsidian-dataview/data-queries/data-fields/>
> [!cite]
> Obsidian MD. (2024). *Obsidian Help - Properties*. Obsidian. Retrieved from <https://help.obsidian.md/Editing+and+formatting/Properties>
> [!cite]
> Various Authors. (2023). *"Best Practices for Dataview Metadata"*. Obsidian Forums (Community Discussion). Retrieved from various threads on forum.obsidian.md
> [!cite]
> Jekyll. (2024). *Front Matter*. Jekyllrb.com. Retrieved from <https://jekyllrb.com/docs/front-matter/>

---
