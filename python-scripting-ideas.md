# Python PKB Scripting Ideas


<!-- TOC START -->

## Table of Contents

- [Python PKB Scripting Ideas](#python-pkb-scripting-ideas)
  - [📄 Existing (Original List)](#existing-original-list)
  - [🏗️ Vault Structure & Organisation](#vault-structure-organisation)
  - [🔗 Link Intelligence](#link-intelligence)
  - [🏷️ Frontmatter & Metadata](#frontmatter-metadata)
  - [🧠 Knowledge Analysis & Intelligence](#knowledge-analysis-intelligence)
  - [📤 Export & Publishing](#export-publishing)
  - [🔌 External Integrations](#external-integrations)
  - [🃏 Flashcards & Spaced Repetition](#flashcards-spaced-repetition)
  - [🔍 Search & Retrieval](#search-retrieval)
  - [🛠️ Content Quality Assurance](#content-quality-assurance)
  - [🗂️ Task & Project Management](#task-project-management)
  - [🔄 Git & Version Control](#git-version-control)
  - [📊 Visualisation & Reporting](#visualisation-reporting)
  - [⚙️ Workflow Automation](#workflow-automation)
  - [🔬 NLP & AI-Augmented](#nlp-ai-augmented)
  - [🧰 Developer & Toolchain Utilities](#developer-toolchain-utilities)

<!-- TOC END -->

A comprehensive backlog of Python automation scripts for Obsidian vault and PKB management.

---

## 📄 Existing (Original List)

- **Table of Contents Generator** — Automatically generate a table of contents for markdown files based on headers.
- **Markdown Link Checker** — Check for broken links in markdown files and report them.
- **Markdown Linter** — Analyze markdown files for style and formatting issues and provide suggestions for improvement.
- **Markdown Formatter** — Automatically format markdown files according to a specified style guide.
- **Markdown to HTML Converter** — Convert markdown files to HTML format.
- **YAML Front Matter Extractor** — Extract YAML front matter from markdown files for further processing.
- **Markdown Image Optimizer** — Optimize images in markdown files for better performance.
- **Markdown Spell Checker** — Check for spelling errors in markdown files and suggest corrections.
- **Markdown Word Count** — Count the number of words in markdown files.
- **Markdown Header Validator** — Validate headers in markdown files to ensure they follow a consistent structure.
- **Markdown Code Block Extractor** — Extract code blocks from markdown files for separate processing or analysis.
- **Markdown Table Formatter** — Format tables in markdown files for better readability.
- **Markdown Table Validator** — Validate the structure and content of tables in markdown files.
- **Markdown Link Extractor** — Extract all links from markdown files for analysis or validation.
- **Markdown TOC Updater** — Update the table of contents in markdown files when headers are added, removed, or changed.
- **Markdown Metadata Updater** — Update the metadata in markdown files, such as the title, author, or date.
- **File Renamer** — Rename files in a directory based on a specified pattern or criteria.

---

## 🏗️ Vault Structure & Organisation

- **Vault Folder Organiser** — Move notes into the correct folder based on their `doc_type` or tag frontmatter fields.
- **Note Archiver** — Move notes with `status: archived` or last-modified older than N days to an `_archive/` folder.
- **Duplicate Note Detector** — Find notes with near-identical titles or content using fuzzy string matching.
- **Note Splitter** — Split a large note at a specified heading level into multiple separate notes with correct frontmatter.
- **Note Merger** — Merge two or more notes into a single file, resolving duplicate headings.
- **Attachment Auditor** — Find images and attachments in your vault that are not referenced by any note.
- **Unused Attachment Cleaner** — Move (not delete) unreferenced attachments to a `_orphan-attachments/` folder.
- **Vault Size Analyser** — Report the largest notes, folders, and attachments by file size and word count.
- **Empty Note Detector** — Find notes that have frontmatter but no body content (stubs / placeholders).
- **Folder README Generator** — Auto-generate a `README.md` index for each folder listing all notes within it.
- **Note Stub Promoter** — Find all notes that only contain a title + frontmatter and flag them for development.
- **Vault Inventory Report** — Generate a full CSV export of every note: path, title, tags, status, word count, created, modified.

---

## 🔗 Link Intelligence

- **Auto-Linker** — Scan note body text and suggest (or auto-insert) wiki-links for terms that match existing note titles.
- **Backlink Report Generator** — For each note, produce a report of every note that links to it.
- **Link Density Analyser** — Score each note by its ratio of outgoing links to word count; flag under-linked notes.
- **Orphan Cluster Finder** — Identify groups of notes that only link to each other but not to the rest of the vault.
- **Alias Conflict Detector** — Find notes whose aliases overlap with another note's title or alias, causing ambiguous links.
- **Wiki-Link to File Validator** — Verify that every `[[wiki-link]]` resolves to an actual file on disk.
- **External URL Validator** — Check all `[text](https://...)` links in the vault for HTTP 404s or redirects.
- **Link Graph Exporter (JSON/CSV)** — Export the vault's link graph as a node-edge CSV or JSON for Gephi / D3.js.
- **Most-Linked Notes Report** — Rank notes by incoming link count — your vault's de-facto MOC candidates.
- **Cross-Folder Link Mapper** — Report all links that cross folder boundaries to visualise knowledge domains.
- **Dangling Alias Finder** — Find `[[links]]` that match an alias in frontmatter but point to the wrong file.

---

## 🏷️ Frontmatter & Metadata

- **Frontmatter Schema Validator** — Check all notes against a defined schema (required fields, valid values, correct types).
- **Date Field Normaliser** — Standardise all date fields to ISO 8601 (`YYYY-MM-DD`) across the vault.
- **Auto-Tag Suggester** — Analyse note body text with TF-IDF or keyword extraction to suggest relevant tags.
- **Tag Taxonomy Enforcer** — Flag or auto-correct tags that don't match your approved taxonomy list.
- **Tag Merger/Renamer (Bulk)** — Rename a tag across all notes in the vault in one operation.
- **Tag Co-occurrence Matrix** — Build a matrix showing which tags most frequently appear together.
- **Metadata Inheritance Injector** — Apply default frontmatter fields to all notes in a folder, inheriting from a folder-level config.
- **Status Progression Tracker** — Generate a timeline report of when notes moved from `draft` → `developing` → `evergreen`.
- **Missing Alias Generator** — For notes with no aliases, suggest aliases from the title (plural forms, abbreviations, acronyms).
- **Frontmatter Diff Reporter** — Compare frontmatter schemas between two vault snapshots to detect schema drift.
- **Created/Modified Date Fixer** — Set `doc_created` from the file's filesystem creation date if the field is missing.
- **Certainty & Status Heatmap** — Produce a report showing the distribution of `certainty` and `status` fields vault-wide.

---

## 🧠 Knowledge Analysis & Intelligence

- **Knowledge Gap Finder** — Identify concepts referenced in note bodies but with no corresponding note in the vault.
- **Note Maturity Scorer** — Score notes on a maturity scale (word count, link density, has callouts, has examples, etc.).
- **Reading Time Estimator** — Add a computed `reading_time_minutes` inline field to each note based on word count.
- **Note Complexity Analyser** — Score notes by heading depth, sentence length, and vocabulary diversity.
- **Concept Frequency Map** — Count how often key concepts (note titles) are mentioned across the vault.
- **Knowledge Domain Mapper** — Cluster notes into topic domains using tag analysis or TF-IDF similarity.
- **Evergreen Candidate Finder** — Identify notes that have high link density, word count, and age — prime candidates for `status: evergreen`.
- **Duplicate Concept Detector** — Find pairs of notes that are semantically similar (using sentence-transformers embeddings).
- **Note Evolution Tracker** — Use git history to show how a note's word count, link count, and status changed over time.
- **Reading Progress Tracker** — Track which literature notes have been processed into permanent notes.
- **Idea Decay Detector** — Flag notes that haven't been touched in over 90 days but are still marked `status: draft`.

---

## 📤 Export & Publishing

- **Markdown to PDF Exporter** — Convert selected notes or folders to styled PDFs using `weasyprint` or `pandoc`.
- **Markdown to EPUB Converter** — Package a collection of notes into a structured EPUB ebook.
- **Static Site Generator Bridge** — Export notes as clean HTML for Jekyll, Hugo, or Quartz static site generation.
- **Reveal.js Presentation Builder** — Convert a note with `---` separators into a Reveal.js slide deck HTML file.
- **Email Digest Generator** — Package the week's new and updated notes into a formatted HTML email digest.
- **Newsletter Formatter** — Convert a selected note into Substack/Mailchimp-compatible HTML.
- **Obsidian Publish Preparer** — Strip private frontmatter fields and internal-only callouts before publishing.
- **Zettlekasten Export (Plain Text)** — Export all permanent notes as plain-text files in The Archive / nvALT format.
- **Daily Note Aggregator** — Compile all daily notes within a date range into a single structured summary document.
- **Monthly Summary Report Generator** — Auto-generate a monthly review note summarising notes created, tags used, and tasks completed.
- **Changelog Generator** — Use git commit history to produce a CHANGELOG.md for your vault.

---

## 🔌 External Integrations

- **Zotero Importer** — Pull references from a Zotero library (via Zotero API) and create literature notes for each.
- **Readwise Highlights Importer** — Fetch highlights from Readwise API and create structured literature notes.
- **Hypothesis Annotations Importer** — Pull Hypothesis web annotations and create notes from them.
- **Pocket/Instapaper Importer** — Import your read-later queue as fleeting notes with URL, title, and excerpt.
- **YouTube Transcript Fetcher** — Download a YouTube transcript (via `youtube-transcript-api`) and create a literature note.
- **ArXiv Paper Fetcher** — Given an ArXiv ID, fetch the abstract and metadata and create a literature note.
- **Wikipedia Article Downloader** — Download a Wikipedia article's intro and key sections as a reference note scaffold.
- **OpenAI Auto-Summariser** — Call the OpenAI API to generate a one-paragraph summary and add it to the note's frontmatter.
- **OpenAI Auto-Tagger** — Use an LLM to suggest tags for notes that have none, writing suggestions to frontmatter.
- **Semantic Scholar Paper Fetcher** — Fetch citation data and abstract for academic papers by DOI or title.
- **Goodreads/OpenLibrary Book Importer** — Create structured literature notes for books from Goodreads shelf data.
- **RSS Feed to Fleeting Notes** — Subscribe to RSS feeds and auto-create fleeting notes from new items.
- **GitHub Issue to Note** — Convert a GitHub issue (via API) into a structured project note.
- **Obsidian URI Launcher** — Trigger Obsidian actions (open note, run template) from external Python scripts via `obsidian://` URIs.

---

## 🃏 Flashcards & Spaced Repetition

- **Anki Flashcard Exporter (CSV)** — Extract `Q:: / A::` pairs from notes and export as Anki-compatible CSV.
- **Anki Sync via AnkiConnect** — Push flashcards directly into an Anki deck via the AnkiConnect REST API.
- **Cloze Deletion Generator** — Identify bolded terms in notes and auto-generate cloze-deletion Anki cards.
- **Spaced Repetition Scheduler** — Track last-reviewed dates in frontmatter and surface notes due for review.
- **Flashcard Coverage Report** — Show which notes/topics have flashcard coverage and which have none.
- **Recall Score Tracker** — Update a `recall_score` frontmatter field based on Anki review history imported via CSV.

---

## 🔍 Search & Retrieval

- **Full-Text Search Indexer** — Build a local SQLite full-text index of your vault for sub-second searches.
- **Semantic Search Engine** — Use `sentence-transformers` to embed notes and answer natural-language queries.
- **Tag-Based Note Finder** — Return all notes matching a complex tag query (AND, OR, NOT logic).
- **Date-Range Query Tool** — Find all notes created or modified within a specified date range.
- **Regex Search Across Vault** — Run a regex pattern against all note bodies and return matching lines with context.
- **Concept Map Extractor** — Extract all wiki-links from a note and recursively map its knowledge neighbourhood.
- **Top N Notes by Criteria** — Return top N notes by word count, link count, age, or recency.

---

## 🛠️ Content Quality Assurance

- **Readability Scorer** — Compute Flesch-Kincaid, Gunning Fog, and SMOG readability scores for each note.
- **Heading Hierarchy Validator** — Detect H3 headings that appear without a parent H2, or H1s after H2s.
- **Empty Section Detector** — Find headings with no content between them and the next heading.
- **Placeholder Text Finder** — Scan for `TODO`, `TBD`, `FIXME`, `<!-- placeholder -->` and report them.
- **Consistency Checker** — Find the same concept spelled multiple ways (e.g. "wiki link" vs "wikilink") and suggest standardisation.
- **Callout Type Auditor** — Validate that all `> [!type]` callouts use approved types from your taxonomy.
- **Long Sentence Detector** — Flag sentences over N words as potential clarity issues.
- **Passive Voice Detector** — Identify heavy use of passive voice constructions in note bodies.
- **Jargon Density Analyser** — Flag notes that use specialised terms without linking to their definitions.

---

## 🗂️ Task & Project Management

- **Task Aggregator** — Collect all `- [ ]` checkboxes from across the vault into a single prioritised task list.
- **Overdue Task Finder** — Find tasks with `📅 YYYY-MM-DD` due dates (Tasks plugin format) that are past due.
- **Task Completion Stats** — Report completed vs open task counts per note, folder, and tag.
- **Project Status Dashboard Generator** — Scan all project notes for status fields and generate a markdown project dashboard.
- **Habit Tracker Parser** — Parse habit tracker tables from daily notes and generate streak / completion stats.
- **Meeting Notes Formatter** — Convert a structured meeting note template into a clean summary with action items extracted.
- **Deadline Reminder Generator** — Scan notes for deadline fields and produce an upcoming-deadlines report.

---

## 🔄 Git & Version Control

- **Vault Auto-Commit** — Watch the vault directory for changes and auto-commit with a timestamp message.
- **Daily Change Digest** — Generate a summary of which notes were created, modified, or deleted since yesterday.
- **Note History Viewer** — Show the git commit history for a specific note file with diff summaries.
- **Conflict Resolver Assistant** — Detect git merge conflicts in markdown files and apply heuristic auto-resolution.
- **Schema Drift Detector** — Compare frontmatter schemas across two git commits to identify structural changes.

---

## 📊 Visualisation & Reporting

- **Tag Cloud Generator** — Produce an SVG tag cloud from vault tag frequencies using `wordcloud` or `matplotlib`.
- **Activity Heatmap Generator** — Create a GitHub-style contribution heatmap showing daily note creation/modification.
- **Note Timeline Creator** — Generate a chronological timeline visualisation of note creation over time.
- **Folder Tree Visualiser** — Output a styled ASCII or HTML tree of your entire vault folder structure.
- **Knowledge Graph Exporter (Gephi)** — Export nodes and edges as `.gexf` or `.graphml` for Gephi network analysis.
- **Link Graph to D3.js HTML** — Generate a self-contained interactive D3.js force-directed graph of your vault links.
- **Stats Dashboard Report** — Produce a comprehensive weekly/monthly markdown stats report: total notes, words written, tags, new links.
- **Note Growth Chart** — Plot cumulative note count and word count over time as a matplotlib chart saved to PNG.

---

## ⚙️ Workflow Automation

- **New Note Template CLI** — Command-line tool to create a new note from a template with prompts for all frontmatter fields.
- **Batch Template Applier** — Apply a Templater-style template to all notes in a folder that are missing key frontmatter.
- **Weekly Review Note Generator** — Auto-generate a weekly review note pre-populated with the week's new notes, tasks due, and habit stats.
- **Literature-to-Permanent Pipeline** — Scan literature notes with `status: processed` and scaffold corresponding permanent notes.
- **Note Promotion Workflow** — Automate the `fleeting → literature → permanent` promotion by updating status, moving folders, and adding links.
- **Hotkey Script Runner** — Map vault management Python scripts to keyboard shortcuts via AutoHotkey or `keyboard` library.
- **Vault Watch Daemon** — Background process that watches for new files and auto-applies frontmatter defaults.
- **Scheduled Health Check** — Run the full suite of audit scripts on a schedule and write a summary report to a daily note.
- **Pre-Commit Hook Generator** — Generate a git pre-commit hook that runs the linter and metadata validator before each commit.

---

## 🔬 NLP & AI-Augmented

- **Topic Modeller (LDA/NMF)** — Run Latent Dirichlet Allocation on your vault to discover hidden topic clusters.
- **Named Entity Extractor** — Use `spaCy` to extract people, places, organisations, and dates from note bodies.
- **Keyword Frequency Analyser** — Build a TF-IDF ranked keyword list for the entire vault or a specific folder.
- **Auto-Categoriser** — Use a local or API-based classifier to suggest `doc_type` for uncategorised notes.
- **Note Similarity Graph** — Find and rank pairs of notes by semantic similarity using embeddings; flag potential merges.
- **Sentiment Analyser** — Score notes by sentiment polarity — useful for journal entries and reflective writing.
- **Auto-Definition Extractor** — Identify sentences of the form "X is Y" and extract them as potential Dataview inline fields.
- **Question Detector** — Find rhetorical and genuine questions in note bodies and surface them as open inquiry nodes.
- **Concept Relationship Extractor** — Use dependency parsing to identify "X → causes → Y" relationships and build a causal map.

---

## 🧰 Developer & Toolchain Utilities

- **Plugin Settings Auditor** — Parse `.obsidian/plugins/*/data.json` files to document current plugin configurations.
- **Snippet Exporter** — Export vault-specific VS Code snippets from note templates automatically.
- **cSpell Dictionary Builder** — Scan all note frontmatter aliases and proper nouns to auto-build a custom cSpell word list.
- **Repomix Config Generator** — Generate a `repomix.config.json` for any subfolder of the vault for LLM context packaging.
- **Script Dependency Checker** — Scan all Python scripts in `99-scripts/` and report their `pip` dependencies with versions.
- **Environment Setup Script** — Auto-create the `.venv`, install requirements, and verify all script dependencies in one command.
- **Vault Backup Manager** — Create timestamped zip archives of the vault, rotate old backups, and optionally push to cloud storage.
- **Path Sanitiser** — Find and fix file/folder names containing characters that break cross-platform compatibility.
- **JSON Schema Generator** — Introspect your vault's frontmatter and auto-generate a JSON Schema for validation tooling.
