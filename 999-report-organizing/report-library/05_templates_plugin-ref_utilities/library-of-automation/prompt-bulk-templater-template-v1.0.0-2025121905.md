---
type: "prompt"
id: "20251219051659"
status: "active"
version: "1.0.0"
rating: "0.0"
source: "claude-sonnet-4.5"
title: "Bulk Templater Templates"
description: "Bulk Templater Template, this prompt is meant to be run repeatedly."
key-takeaway: "Tested -> Works Great [[2525-12-18]]"
last-used: "[[2025-12-19]]"
tags:
  - "year/2025"
  - "prompt-engineering"
  - "llm-capability/generation"
  - "prompt-workflow/deployment"
aliases:
  - "Prompt"
  - "Prompt-Engineering"
link-up: "[[moc-agentic-instruction-sets-2025117044009]]"
link-related:
  - "[[2025-12-19|Daily Note]]"
  - "[[2025-W51|Weekly Review]]"
---



[Initial Creation: [[2025-12-19|Friday, December 19th, 2025]]]

---

# prompt-bulk-templater-template-v1.0.0-2025121905

`````prompt
----
Prompt-ID: "2025121905"
Prompt-Version: 1.0.0
----

You are a world-class Obsidian PKB Architect and Templater plugin expert. You have a deep understanding of the Templater plugin's complete API, including all internal functions (tp.date, tp.file, tp.frontmatter, tp.system, tp.config, tp.web) and advanced features like user scripts, dynamic commands, and plugin integrations.
Your task is to generate a comprehensive collection of Templater templates to be used as inspiration and educational examples for a user building their own PKB. You must generate a wide variety of templates, ranging from simple to highly advanced.
The examples must be centered around the theme of: **[INSERT THEME HERE]**
**CRITICAL FORMATTING RULE:** All code blocks you generate MUST use plain Markdown backticks (```) with **NO language identifier** (do NOT use ```templater or ```javascript). This is to ensure the code is stored as inert text and does not auto-execute within an Obsidian note.
You must follow this structure precisely:

---
## Basic Templates
*Provide 3-4 examples of fundamental Templater templates. These should demonstrate:
- Simple variable insertion (`<% tp.file.title %>`)
- Date/time formatting (`<% tp.date.now("YYYY-MM-DD") %>`)
- Basic frontmatter generation
- File path/name operations
Enclose each template in a plain code block with a brief description above it.*

---
## Intermediate Templates
*Provide 3-4 examples of more complex Templater templates. These should include:
- Conditional logic (`<% if %>`, `<% else %>`)
- Loops and iteration (`<% for %>`)
- Dynamic content generation based on context
- User input prompts (`<% tp.system.prompt() %>`)
- File manipulation operations
- Multi-line template variables
For each template, provide a 1-2 sentence description. Enclose templates in plain code blocks.*

---
## Advanced Templates
*Provide 2-3 examples of sophisticated Templater templates demonstrating expert-level capabilities.*
**For each Advanced Template, you MUST provide:**
1. **Description** - Exactly what the template does and how it works
2. **Top Use Cases** - 2-3 specific scenarios where this template shines
3. **Implementation Tips** - Critical details for successful deployment
4. **Customization Options** - 2-3 ways users can adapt the template to their needs
*After the documentation, provide the complete, functional Templater code in a plain code block.*
These advanced templates should demonstrate:
- User script integration
- Complex automation workflows
- Multi-file operations (creation, modification, organization)
- Advanced string manipulation and parsing
- System command execution
- Web API integration (`tp.web.daily_quote()` or custom requests)

---
## Synergy Templates (Plugin Integration)
*Provide 2-3 examples of Templater templates that integrate with other Obsidian plugins (QuickAdd, Dataview, Meta Bind, Tasks, etc.) to create powerful combined workflows.*
**For each Synergy Template, you MUST provide:**
1. **Description** - What the template does and which plugins it integrates with
2. **Top Use Cases** - 2-3 specific scenarios for this integration pattern
3. **Implementation Tips** - Prerequisites, setup steps, and critical details
4. **Customization Options** - 2-3 ways to extend or modify the integration
*After the documentation, provide the complete, functional template code in a plain code block.*
These synergy templates should demonstrate integration patterns like:
- Templater + QuickAdd (capture workflows)
- Templater + Dataview (dynamic content generation from queries)
- Templater + Meta Bind (interactive button workflows)
- Templater + Tasks (automated task management)
- Templater + Custom user scripts (extending functionality)

---
## Context: Your PKB Metadata & Structure
This is my metadata quick reference and folder structure for you to use when populating the templates.
### Available Options for Metadata Fields
#### type
- analysis
- claude-project
- cog-sci-report
- concept
- cosmo-report
- dashboard
- definition
- edu-report
- experiment
- framework
- gemini-gem
- guide
- literature
- mental-model
- moc
- pattern
- permanent-note
- pkb-report
- principle
- prompt
- prompt-report
- reference
- report
- review
- theory
- tutorial
#### source
- claude-opus-4.1
- claude-sonnet-4.5
- gemini-flash-2.5
- gemini-flash-3.0
- gemini-pro-2.5
- gemini-pro-3.0
#### maturity
- needs-review
- seedling
- developing
- budding
- evergreen
#### confidence
- speculative
- provisional
- moderate
- established
- high
#### status
- active
- archived
- deprecated
#### priority
- low
- medium
- high
- urgent
#### link-up (MOCs)
- `[[artificial-intelligence-moc]]`
- `[[cognitive-science-moc]]`
- `[[cosmology-moc]]`
- `[[educational-psychology-moc]]`
- `[[learning-theory-moc]]`
- `[[neuroscience-moc]]`
- `[[pkb-&-pkm-moc]]`
- `[[practical-philosophy-moc]]`
- `[[prompt-engineering-moc]]`
#### Tags
#pkm
#pkb 
#prompt-engineering
#cognitive-science
#cosmology
#type/report
#type/reference
#type/permanent
#status/complete
#status/in-progress
#status/not-read
#status/read
#status/seedling
#status/budding
#status/developing
#status/evergreen
#status/needs-review
#year/2025
#cognitive-pkm
#cognitive-enhancement
#cognitive-training
#dataview
#templater
#automation
### Folder Hierarchy
#### Level 0: Core Infrastructure
- 00-inbox/ → Ingestion & triage zone
- 00-meta/ → System memory & configuration
- 000_database/ → [Database storage]
#### Level 1: Temporal Organization
- 01-daily-notes/ → Atomic daily entries (time-indexed)
#### Level 2-7: Content Layers
- 02-projects/ → Active project documentation
- 03-notes/ → Core knowledge atoms
- 04-library/ → Reference materials & resources
- 05-tasks-&-reviews/ → GTD & reflection systems
- 06-dashboards/ → Overview & summary pages
- 07-mocs/ → Maps of Content (graph hubs)
#### Level 99: System Management
- 99-archive/ → Deprecated/completed content
- 99-system/ → System configuration files

---
## Template Generation Guidelines
**When generating templates, ensure:**
1. All Templater syntax uses correct delimiters: `<%` and `%>`
2. Multi-line template commands use `<%*` and `%>` for proper execution
3. Variables are properly accessed (e.g., `tp.file.title`, `tp.date.now()`)
4. User prompts provide clear guidance on expected input
5. Error handling is included for complex operations
6. Comments explain non-obvious logic
7. Templates are immediately usable (no placeholders requiring additional setup unless noted)
**For themes involving:**
- **Capture workflows** → Focus on inbox processing, quick entry, metadata automation
- **Project management** → Emphasize project initialization, status tracking, file organization
- **Knowledge management** → Highlight note creation, linking automation, MOC generation
- **Review systems** → Feature periodic review templates, progress tracking, reflection prompts
- **Content generation** → Showcase dynamic content creation, AI integration, multi-file workflows

---
## Output Format Reminder
Each template code block should:
- Use plain backticks (```) with NO language identifier
- Be complete and functional (ready to copy into Obsidian)
- Include inline comments for complex logic
- Follow best practices for Templater syntax
- Be tested conceptually for logical correctness
Provide comprehensive, production-ready templates that demonstrate the full power of Templater while remaining accessible and well-documented.


`````
