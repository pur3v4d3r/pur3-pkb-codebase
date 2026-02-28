## Obsidian Notes & Note‑Taking — A Practical, Philosophical Walkthrough

Let us turn Obsidian from "shiny app" into a reliable instrument. You want a system you can actually live in: notes that are easy to start, easy to connect, and easy to grow. This walkthrough explains how Obsidian thinks, how links really work under the hood, and how to design sturdy note templates from first principles—then layers in just enough Templater to automate the boring bits without obscuring the "why."

I’ll keep prose front and center (no sprawling tables), add example templates you can paste straight into your vault, and call out the few settings that matter so your notes stay portable when you route text through Google Docs on the way back to Markdown.

## 1) The mental model: Obsidian is a graph of plain‑text files

Obsidian stores everything as local Markdown files; there’s no opaque database. Your “vault” is simply a folder of `.md` files (plus attachments) on your drive. Obsidian then layers live features—linking, backlinks, graph view, properties—on top. That is why it is both fast and resilient![](obsidian-notes-guide/raw.png)screenshot.

Two core ideas:

-   **Notes are nodes; links are edges.** A link `[[Like this]]` connects notes. Backlinks, outgoing links, and the graph visualize these relationships![](obsidian-notes-guide/raw.png)screenshot.
    
-   **Properties** (structured metadata at the top of a note) make your notes queryable and consistent. In 2025, Obsidian added a richer properties editor—and even “Bases,” a way to treat sets of notes like databases—while still storing all metadata in YAML so your files remain plain text![](obsidian-notes-guide/raw.png)screenshot.
    

Why this matters: when you design templates, you’re deciding what a “node” looks like in your universe, what metadata it carries, and how it will connect. You’re designing a language your vault will speak back to you.

## 2) Linking—every moving piece, plus when to use which

### 2.1 Internal links (the default)

Type `[[` and start a title; Obsidian autocompletes and creates an _internal link_. Rename the target file later and Obsidian can update links automatically (toggle: **Settings → Files & Links → Automatically update internal links**). You can customize how links are written:

-   **Wikilinks**: `[[Note Title]]` (Obsidian’s default; compact, excellent autocompletion).
    
-   **Markdown links**: `[Note Title](folder/file.md)` (more interoperable with external tools). Switch in **Files & Links → Use \[\[Wikilinks\]\]**. Even if you disable wikilinks, typing `[[` still autocompletes but inserts Markdown‑style links![](obsidian-notes-guide/raw.png)screenshot.
    

**Pragmatic advice for your Google Docs round‑trip:** Markdown links survive that journey more predictably than wikilinks. If you frequently export to Google Docs and back, consider authoring with Markdown links to reduce cleanup, then (optionally) convert to wikilinks inside Obsidian using the Format Converter or a community converter when needed![](obsidian-notes-guide/raw.png)screenshot.

### 2.2 Links to headings and blocks

-   **Heading links:** `[[Note#Section]]` jumps to a heading in the target note. If you change the heading text, you can right‑click the heading and use **Rename this heading** to update links pointing to it![](obsidian-notes-guide/raw.png)screenshot.
    
-   **Block links:** add an ID to the end of any paragraph like `^quote-of-the-day`, then link to it with `[[Note#^quote-of-the-day]]`. Helpful for quoting exact fragments without copy‑paste. **Caveat:** block references are Obsidian‑specific; they will not work outside Obsidian![](obsidian-notes-guide/raw.png)screenshot.
    

### 2.3 Embeds (transclusion)

Put an exclamation mark before a link to _embed_ content: `![[Note]]`, `![[Note#Heading]]`, or `![[Note#^blockID]]`. Embeds display the other note’s content inside the current note (read‑only where shown). Accepted embed formats include notes, images, audio, video, PDFs, and canvases![](obsidian-notes-guide/raw.png)screenshot.

### 2.4 Backlinks, outgoing links, and the graph

-   **Backlinks** show what _points to_ the current note (incoming edges). Enable the Backlinks core plugin; you’ll see a sidebar panel![](obsidian-notes-guide/raw.png)screenshot.
    
-   **Outgoing links** list what the current note _points to_, and even suggest potential links (unlinked mentions)![](obsidian-notes-guide/raw.png)screenshot.
    
-   **Graph view** gives a visual overview of notes (nodes) and their link lines (edges). It’s a compass, not a map—useful to spot hubs and islands![](obsidian-notes-guide/raw.png)screenshot.
    

### 2.5 Aliases and display text

If a person or concept goes by multiple names, add **Aliases** in Properties so `[[Alt Name]]` also targets the same note. For one‑off custom link text, use the pipe: `[[Note|custom text]]`![](obsidian-notes-guide/raw.png)screenshot.

## 3) Properties (structured metadata) without the hand‑wringing

Properties live at the top of the file as YAML and can be edited with the new properties editor (`Ctrl/Cmd+;` opens the add‑property dialog). Supported types include text, links, dates, checkboxes, and numbers. Obsidian stores them in plain YAML; many community plugins can read them![](obsidian-notes-guide/raw.png)screenshot.

Guidelines that keep things sane:

-   Prefer _fewer, clearer_ properties with consistent names over sprawling schemas.
    
-   Use **Aliases** for alternate titles; avoid inventing a parallel “title” field that fights the filename![](obsidian-notes-guide/raw.png)screenshot.
    
-   When in doubt, start with: `type`, `status`, `source`, `created`, `updated`, `aliases`, and a small set of domain‑specific fields (for you, photography and writing).
    

## 4) Designing a note template from the ground up

A template is not just boilerplate—it’s a set of promises. Each section exists for a reason. Here’s a design process you can use for _any_ template:

### Step A — Define the job

-   **What decision or action will this note help you make later?**
    
-   **Who** is the note for? (Future‑you with two minutes of patience.)
    
-   **When** will you reach for it? (Creation, review, or synthesis?)
    

### Step B — Decide the minimal, durable properties

Choose the fewest fields that make the note queryable and linkable. For example, a Literature Note benefits from `source`, `author`, `year`, `topics`, and a unique citation key; a Permanent Note benefits from `claims`, `tags`, and `links`.

### Step C — Write the anatomy in plain words

Sketch the note sections in the order you’ll naturally think through them. For example: **Context → Claim → Evidence → Links → Next actions**. Resist the urge to add everything.

### Step D — Add linking scaffolds

Pre‑write `See also:` with empty `[[ ]]` stubs to prompt linking while the idea is fresh. Add one property for `moc` (your “map of content” hub) if this note belongs in a curated hub.

### Step E — Make one gold example

Fill one instance fully. That completed note becomes your _style guide_ for that type.

### Step F — Automate gently with Templater

Use Templater for dates, titles, IDs, and little conveniences (examples below), not to bury the template under code. You should be able to read the template as prose.

## 5) Six copy‑ready templates (with “why,” “how,” and light Templater)

> **Using the examples:** The parts between `<% %>` are Templater. If you have not installed Templater yet, paste the templates anyway—the non‑Templater text will still work. When you do add Templater, those expressions will auto‑fill.

### 5.1 Fleeting Note (capture inbox)

**Why:** Fast capture with just enough context to process later; designed to be thrown away or refactored.

### 5.2 Literature Note (from books, articles, videos)

**Why:** A single page that ties a source to your own words. It keeps _ideas_ separate from _bibliography_ so you can later promote insights into Permanent Notes.

> Why this structure: it forces separation between the author’s words and your interpretation—a core Zettelkasten habit![](obsidian-notes-guide/raw.png)screenshot.

### 5.3 Permanent Note (atomic claim)

**Why:** One idea per note, written as a standalone claim in your voice, richly linked.

> Why this works: linking claims forces synthesis; it is how a web of thought emerges instead of a pile of summaries![](obsidian-notes-guide/raw.png)screenshot.

### 5.4 Project Note (deliverable‑driven)

**Why:** Keeps scope, decisions, and links to working material in one place.

### 5.5 Daily Note (journal + router)

Turn on the **Daily notes** core plugin, then set your template in **Core plugins → Templates**![](obsidian-notes-guide/raw.png)screenshot.

### 5.6 MOC (Map of Content) / Hub Note

**Why:** A curated “hub” for a topic; not a dumping ground. It is both navigation and active thinking![](obsidian-notes-guide/raw.png)screenshot.

## 6) Linking in practice: a rhythm you can follow

1.  **Capture** fast (Fleeting). Add just enough context to find it later (a topic, a source, and one sentence of why it mattered).
    
2.  **Process** into Literature or Permanent Notes. In Literature Notes, separate quotes from commentary. In Permanent Notes, state one claim and link it to neighbors![](obsidian-notes-guide/raw.png)screenshot.
    
3.  **Curate** into MOCs. When a cluster grows, make or update a hub note that explains the shape of the topic _in your words_. This is sense‑making, not filing![](obsidian-notes-guide/raw.png)screenshot.
    
4.  **Review** hubs and projects weekly; follow the links that still tingle.
    

Backlinks and outgoing links help you _notice_ connections you might otherwise miss; the graph can reveal hubs and orphans that deserve attention![](obsidian-notes-guide/raw.png)screenshot.

## 7) Core settings that actually matter (and why)

Open **Settings → Files & Links** and decide:

-   **Use \[\[Wikilinks\]\]**: On = compact, Obsidian‑native. Off = Markdown links, better outside Obsidian. For your Google Docs detour, Markdown links reduce friction. You can still type `[[` to autocomplete; Obsidian will insert Markdown links when wikilinks are disabled![](obsidian-notes-guide/raw.png)screenshot.
    
-   **Automatically update internal links**: On, so renaming a file updates links pointing to it. (Note: header links update when you explicitly “Rename this heading.”)![](obsidian-notes-guide/raw.png)screenshot
    
-   **Default location for attachments**: Keep it predictable (e.g., an `attachments/` subfolder) so exported Markdown from Google Docs can be reconciled easily![](obsidian-notes-guide/raw.png)screenshot.
    

When importing Markdown exported from Google Docs, use **Format converter** (Core plugin) to normalize to Obsidian‑flavored Markdown, then skim for any links that need touch‑up![](obsidian-notes-guide/raw.png)screenshot.

## 8) Gentle Templater on‑ramp (for later, as you planned)

Install **Templater** (community plugin), point Obsidian’s **Templates** folder to where these `.md` templates live, and you’re off. The Templater docs show functions like `tp.file.title`, `tp.date.now()`, and `tp.frontmatter` for auto‑filling titles, dates, and properties![](obsidian-notes-guide/raw.png)screenshot.

A few tiny examples you can paste into any template:

-   **Human‑friendly date:** `Created: <% tp.date.now("YYYY-MM-DD HH:mm") %>`
    
-   **Use the note’s title in a heading:** `# <% tp.file.title %>`
    
-   **Include another template (reusable checklists, etc.):** `<%* tR += await tp.file.include("[[Template—Checklist]]") %>`![](obsidian-notes-guide/raw.png)screenshot
    

> Tip: keep Templater servicing _clarity_—dates, titles, a few links—rather than turning templates into code puzzles. You should be able to read and edit your templates without thinking about JavaScript.

## 9) Everything you need to know about Canvas and Graph (optional but handy)

-   **Graph view** helps you spot emerging hubs. Use it to find orphans to link or prune![](obsidian-notes-guide/raw.png)screenshot.
    
-   **Canvas** gives you an infinite board that can display notes, images, PDFs, and even web pages side‑by‑side; great for storyboarding or laying out research![](obsidian-notes-guide/raw.png)screenshot.
    

## 10) Common pitfalls and how to dodge them

-   **Copying quotes instead of writing ideas.** Literature Notes are for _understanding_, not transcription. Promote only the ideas you can express as claims![](obsidian-notes-guide/raw.png)screenshot.
    
-   **Letting MOCs become dumping grounds.** Curate and narrate; a good MOC explains why links belong together![](obsidian-notes-guide/raw.png)screenshot.
    
-   **Over‑engineering properties.** Start small; YAML remains plain text, but complexity invites drift. Use the new properties editor for consistency, not maximalism![](obsidian-notes-guide/raw.png)screenshot.
    
-   **Forgetting that block links are Obsidian‑only.** They are powerful inside your vault but will not resolve in external tools. Prefer heading links when you need broader compatibility![](obsidian-notes-guide/raw.png)screenshot.
    

## 11) A starter practice routine

1.  Create one **Fleeting** capture each day.
    
2.  Process one item into a **Literature** note; spin out one **Permanent** claim.
    
3.  Once per week, update a **MOC**: add two links, remove one, write one sentence summarizing what changed.
    
4.  Every project gets a **Project** note; every Project note links to at least three claims and one MOC.
    

This rhythm keeps your vault alive—ideas do not just accumulate; they connect, argue, and mature.

## 12) Appendix: where to look things up, fast

-   **Internal links, headings, blocks, and formatting basics.** Clear, up‑to‑date official docs![](obsidian-notes-guide/raw.png)screenshot.
    
-   **Backlinks, outgoing links, graph view.** What they show and how to use them![](obsidian-notes-guide/raw.png)screenshot.
    
-   **Properties and the editor.** How to add/edit, supported types, shortcuts![](obsidian-notes-guide/raw.png)screenshot.
    
-   **Templates (core) and Daily notes.** Where to put templates; how to insert them![](obsidian-notes-guide/raw.png)screenshot.
    
-   **Templater docs.** Precise references for `tp.file`, `tp.date`, `tp.frontmatter`![](obsidian-notes-guide/raw.png)screenshot.
    
-   **Accepted file formats.** What you can embed and preview![](obsidian-notes-guide/raw.png)screenshot.
    
-   **Format Converter and Importer.** Normalize Markdown from other apps; migrate content if needed![](obsidian-notes-guide/raw.png)screenshot.
    
-   **Roadmap (2025).** Properties improvements and Bases![](obsidian-notes-guide/raw.png)screenshot.
    

## Where to go next

If you want, I can tailor these templates to your exact use cases—photography projects, SOPs, or research papers—and wire up Templater so new notes auto‑link to their MOCs and stamp the right properties. Or we can build a “Note Design Checklist” you keep pinned in your vault so every new template turns into a repeatable craft.