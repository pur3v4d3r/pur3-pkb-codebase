
```
Accessible-Media

This component instructs the AI to enhance content with placeholders for embedded media (images, diagrams) and to provide accessibility features like alt-text and plain-language summaries.

**Format: Accessible Media**
You must enrich the content for accessibility and visual engagement.
**1. Plain-Language Summary:**
* At the *beginning* of the document (immediately after the YAML), you MUST includea `[!summary]` callout.
* This callout will contain a 1-2 sentence, jargon-free summary of the entire note.
* *Example:*
    ```markdown
     > [!summary] Plain-Language Summary
    > This note explains what "dark energy" is and why scientists believe it iscausing the universe to expand at an accelerating rate.
    ```
**2. Embedded Media Placeholders:**
* When you describe a complex visual concept, diagram, graph, or object, you MUSTinsert a placeholder for an embedded image.
* The format MUST be an Obsidian `[[wikilink]]` embed: `![[Figure_Name.png]]`
* *Example:* "The process flow is shown below: `![[process_flow_diagram.png]]`"
**3. Accessibility (Alt-Text):**
* Immediately *after* the media placeholder, you MUST provide a `[!note]` calloutcontaining the descriptive alt-text for that image.
- *Example:*
    ```markdown
    ![[process_flow_diagram.png]]
    > [!note] Alt-Text
    > A diagram showing three boxes labeled A, B, and C, with an arrow pointing from A to B, and arrows from B to both A and C, indicating a feedback loop.
      ```
```

```
**Citations Plugin**

**1. Inline Citations:**

* The format is displayed as an exemplar for you to use.
* Just fill out the sections.
* *Example:* "The theory was first proposed in 1965 `[feynman1965]`."
**2. Page-Specific Citations:**
* To cite a specific page, use the format `[p. XX]`.
* *Example:* "This is explicitly stated on page 42 `[feynman1965, p. 42]`."
**3. References Block:**
* At the *very end* of the document, you MUST include a "References" section.
 * Inside this section, provide the full BibTeX entry for each `citekey` used, formatted inside a "bib" code block.

 > [!cite]
> **Bibliographic Information**
> - **Source Type**:: 
> - **Title**:: 
> - **Author(s)**:: 
> - **Year**:: 
> - **Publisher / Journal**:: 
> - **Volume / Issue**:: 
> - **Page(s)**:: 
> - **URL / DOI**:: 
> - **Date Accessed**::
```

```
[OUTPUT FORMAT RULES]
1.  **CRITICAL FORMAT:** Your *entire* response must be structured in two parts:
    1.  A single, complete, copy-paste-ready `dataviewjs` code block.
    2.  A `> [!the-purpose]` callout *after* the code block, explaining the query's logic, functions, and flow in detail (as if I am a learner).
2.  **REQUIREMENTS:**
    * The code must be **DataviewJS**, not DQL (Dataview Query Language), unless I explicitly ask for DQL.
    * The code must be heavily **commented** with `//` comments to explain the "why" of each logical step *inside* the code.
    * You must not include *any* other prose (e.g., "Here is the query you asked for…"). Your response must *start* with the ` ```dataviewjs ` line.
```

```
**Format: Enriched YAML Frontmatter**

You MUST generate a YAML frontmatter block at the very top of the note. This block must be comprehensive and optimized for a Personal Knowledge Base.

**1. Core Metadata:**
* `id:` (Use the note's filename)
* `alias:` (Provide 1-3 human-readable aliases)
* `created:` {{Current Datetime: YYYY-MM-DDTHH:mm:ss}}
* `updated:` {{Current Datetime: YYYY-MM-DDTHH:mm:ss}}
 **2. PKB Metadata:**
* `status:` (e.g., `#seed`, `#evergreen`, `#in-progress`)
* `type:` (e.g., `#concept`, `#person`, `#tutorial`, `#source`)
* `version:` 1.0 (Set initial version to 1.0)

**3. Search & Discovery:**
 * `keywords:` (Generate a YAML list of 5-8 specific, searchable keywords andtechnical terms from the content.)
* `tags:` (Generate a YAML list of 1-3 high-level nested tags, e.g., `cosmology/darkenergy`, `programming/python`)

**4. Source-Specific Metadata (If applicable):**
* If the content is based on a source, add:
* `source_author:`
* `source_title:`
* `source_type:` (e.g., "Academic Paper," "Blog Post," "Book")
* `doi:`
* `url:`
* `pdf_path:` (e.g., `_inbox/papers/author2023.pdf`)
```

```
**Markdown Generation Rules:**

 * You MUST generate pure, standards-compliant Markdown.
 * You are **explicitly forbidden** from using the backslash (`\`) to escape special characters, especially `>` for blockquotes/callouts, `#` for headers, or `*` for lists.
 * The output MUST be "clean" and ready for direct use in a Markdown editor like Obsidian without any post-processing or cleanup.
 * When generating a callout, the syntax MUST always start *exactly* with `> [!type]` on its own line, with no preceding characters (especially not `\`).
```

```
[OUTPUT FORMAT RULES]
1.  **CRITICAL FORMAT:** Your response *must* be a single, complete, copy-paste-ready `yaml` code block, formatted as Obsidian frontmatter.
2.  **REQUIREMENTS:**
    * The `yaml` block must *start* with `---` and *end* with `---`.
    * You must not include *any* other prose (e.g., "Here is the YAML…"). Your response must *start* with the `---` line.
    * You must adhere to correct YAML syntax (indentation, keys, lists).
```

```
[OUTPUT FORMAT RULES]
    1.  A single, complete, copy-paste-ready `mermaid` code block.
    2.  A `> [!the-purpose]` callout *after* the code block, explaining the diagram's logic and structure.
2.  **REQUIREMENTS:**
    * You must choose the *correct* Mermaid diagram type for my request (e.g., `graph TD` for a flowchart, `mindmap` for brainstorming, `timeline` for history).
    * The code must be functional and renderable in Obsidian.
    * You must not include *any* other prose. Your response must *start* with the ` ```mermaid ` line.
```

```
**Format: PKB Linking**

As you generate the main content (the prose), you must adhere to the following linking and tagging protocols:

**1. Bidirectional Linking (Wikilinks):**
* When you encounter a core concept, a person's name, a theory, or a technical term that is likely to be (or *should* be) its own note in the PKB, you MUST format it as a `[[wikilink]]`.
* *Example:* "This is related to the… `[[Feynman Technique]]`."
* *Example:* "The primary proponent was `[[Richard Feynman]]`."
* Do not over-link; focus on high-value nouns and concepts.
**2. Nested Tagging (Inline):**
* Where appropriate, use inline nested tags for granular, context-specific filtering.
* This is especially useful for opinions, questions, or specific data types.
* *Example:* "I think this is a flawed assumption. `#opinion/disagree`"
* *Example:* "What is the primary evidence for this? `#question/to-research`"
**3. "Connection Ideas" Callout:**
* At the end of the main content, you MUST add a "Connection Ideas" callout.
* This callout will contain a list of 3-5 `[[wikilinks]]` to *broader, related concepts* that the user should explore next.

> [!connect] Connection Ideas
> * [[Concept A]]
> * [[Theory B]]
> * [[Related Field C]]
```

```
[OUTPUT FORMAT RULES]
1.  **CRITICAL FORMAT:** Your *entire* response must be structured in two parts:
    1.  A single, complete, copy-paste-ready `javascript` code block, written to be compatible with the Obsidian **Templater** plugin.
    2.  A `> [!the-purpose]` callout *after* the code block, explaining the script's logic, the Templater functions used (e.g., `tp.file.create_new`), and the overall workflow.
2.  **REQUIREMENTS:**
    * The code must be heavily **commented** with `//` comments.
    * You must assume I have access to the Templater `tp` object.
    * You must not include *any* other prose. Your response must *start* with the ` ```javascript ` line.
```