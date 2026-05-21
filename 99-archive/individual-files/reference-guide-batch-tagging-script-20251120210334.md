---
title: Tag Taxonomy Reference Guide
aliases:
  - Tag Taxonomy Selector
  - Batch Tag Suggester Reference
tags:
  - type/reference
  - obsidian
  - information-architecture
status: complete
created: 2025-11-21
---

# Tag Taxonomy Reference Guide

> [!info] Purpose
> This note serves as a master reference for the batch-tag-suggester script's taxonomy options. Use this to quickly determine which taxonomy preset to use for different folder types.

## Quick Selection Guide

| Folder Type | Recommended Taxonomy | Use Case |
|-------------|---------------------|----------|
| General PKM notes | `pkmGeneral` | Most comprehensive for knowledge management |
| Psychology notes | `psychologyCognitive` | Mental models, learning, cognitive science |
| AI/LLM prompts | `promptEngineering` | Prompt techniques, patterns, experiments |
| Book notes | `books` | Literature notes and book summaries |
| System notes | `obsidianSystem` | Obsidian configuration, templates, scripts |
| Project folders | `projects` | Active projects and project tracking |
| Research papers | `research` | Academic research and papers |
| Learning materials | `learning` | Courses, tutorials, practice logs |
| Inbox/captures | `minimal` | Quick captures needing processing |

---

## Taxonomy Definitions

### 1. PKM General (`pkmGeneral`)
**Best for:** General knowledge management notes, permanent notes, MOCs

**Dimensions:**
- **Domains:** `#pkm`, `#pkb`, `#note-taking`, `#knowledge-workflow`, `#obsidian`, `#information-architecture`, `#knowledge-graph`, `#digital-garden`, `#productivity`
- **Types:** `#type/fleeting`, `#type/literature`, `#type/permanent`, `#type/moc`, `#type/reference`, `#type/tutorial`, `#type/template`, `#type/dashboard`, `#type/framework`
- **Status:** `#status/seedling`, `#status/budding`, `#status/evergreen`, `#status/review`, `#status/archived`, `#status/in-progress`, `#status/complete`
- **Source:** `#source/book`, `#source/article`, `#source/blog`, `#source/video`, `#source/podcast`, `#source/course`, `#source/documentation`, `#source/community`, `#source/experience`, `#source/original`

---

### 2. Psychology/Cognitive (`psychologyCognitive`)
**Best for:** Mental models, learning theory, self-improvement, cognitive science notes

**Dimensions:**
- **Domains:** `#cognitive-science`, `#critical-thinking`, `#self-regulation`, `#learning-theory`, `#self-improvement`
- **Types:** `#type/fleeting`, `#type/literature`, `#type/permanent`, `#type/moc`, `#type/practice-log`, `#type/synthesis`, `#type/technique`, `#type/framework`
- **Status:** `#status/seedling`, `#status/budding`, `#status/evergreen`, `#status/review`, `#status/archived`
- **Source:** `#source/book`, `#source/article`, `#source/paper`, `#source/course`, `#source/podcast`, `#source/video`, `#source/experience`, `#source/original`

---

### 3. Prompt Engineering (`promptEngineering`)
**Best for:** AI prompts, LLM techniques, prompt experiments

**Dimensions:**
- **Domains:** `#prompt-engineering`, `#prompting-technique`, `#prompt-pattern`, `#llm-capability`, `#llm-limitation`, `#advanced-prompting`, `#prompt-safety`, `#context-management`
- **Types:** `#type/technique`, `#type/pattern`, `#type/template`, `#type/experiment`, `#type/analysis`, `#type/literature`, `#type/reference`, `#type/case-study`, `#type/tutorial`
- **Status:** `#status/experimental`, `#status/proven`, `#status/deprecated`, `#status/under-revision`, `#status/production`, `#status/archived`
- **Maturity:** `#maturity/emerging`, `#maturity/established`, `#maturity/standard`, `#maturity/deprecated`

---

### 4. Books (`books`)
**Best for:** Book notes, literature notes, reading summaries

**Dimensions:**
- **Domains:** `#cognitive-science`, `#learning-theory`, `#prompt-engineering`, `#pkm`, `#productivity`, `#self-improvement`
- **Types:** `#type/literature`, `#type/permanent`, `#type/moc`, `#type/synthesis`
- **Status:** `#status/to-read`, `#status/reading`, `#status/complete`, `#status/review`, `#status/archived`
- **Source:** `#source/book`

---

### 5. Obsidian System (`obsidianSystem`)
**Best for:** Technical notes, templates, plugins, CSS, workflows

**Dimensions:**
- **Domains:** `#obsidian`, `#information-architecture`, `#pkb`
- **Types:** `#type/reference`, `#type/tutorial`, `#type/template`, `#type/dashboard`, `#type/guide`, `#type/framework`
- **Status:** `#status/in-progress`, `#status/complete`, `#status/review`, `#status/archived`

---

### 6. Projects (`projects`)
**Best for:** Active projects, project planning, project tracking

**Dimensions:**
- **Domains:** `#project`, `#productivity`
- **Types:** `#type/project`, `#type/moc`, `#type/dashboard`, `#type/practice-log`
- **Status:** `#status/planning`, `#status/active`, `#status/on-hold`, `#status/complete`, `#status/archived`
- **Priority:** `#priority/high`, `#priority/medium`, `#priority/low`

---

### 7. Research (`research`)
**Best for:** Academic research, papers, scholarly articles

**Dimensions:**
- **Domains:** `#cognitive-science`, `#learning-theory`, `#prompt-engineering`
- **Types:** `#type/literature`, `#type/synthesis`, `#type/analysis`, `#type/framework`, `#type/moc`
- **Status:** `#status/seedling`, `#status/budding`, `#status/evergreen`, `#status/review`
- **Source:** `#source/paper`, `#source/article`, `#source/book`, `#source/conference`, `#source/course`

---

### 8. Learning (`learning`)
**Best for:** Courses, tutorials, educational content, skill development

**Dimensions:**
- **Domains:** `#learning-theory`, `#cognitive-science`, `#self-improvement`
- **Types:** `#type/tutorial`, `#type/guide`, `#type/practice-log`, `#type/technique`, `#type/framework`
- **Status:** `#status/learning`, `#status/practicing`, `#status/mastered`, `#status/review`
- **Source:** `#source/course`, `#source/book`, `#source/video`, `#source/tutorial`, `#source/practice`

---

### 9. Minimal (`minimal`)
**Best for:** Quick captures, inbox items, unprocessed notes

**Dimensions:**
- **Types:** `#type/fleeting`, `#type/inbox`
- **Status:** `#status/unprocessed`, `#status/in-progress`, `#status/complete`
- **Priority:** `#priority/high`, `#priority/medium`, `#priority/low`

---

## Folder → Taxonomy Mapping Examples

### Suggested Mappings

```yaml
00_inbox: minimal
01_fleeting: minimal
02_literature: 
  - books (for book notes)
  - research (for papers)
  - pkmGeneral (for mixed content)
03_permanent: pkmGeneral
04_projects: projects
05_areas:
  - psychology: psychologyCognitive
  - prompt-engineering: promptEngineering
  - learning: learning
99_system: obsidianSystem
```

---

## Usage Instructions

### Running the Batch Tag Suggester

1. Activate QuickAdd command for batch-tag-suggester
2. Select taxonomy type from the list
3. Select folder to analyze
4. Review generated report in `99_system/reports/`

### Reading the Report

Reports include:
- Taxonomy used
- Folder analyzed
- Total files processed
- Files needing attention
- Specific tag suggestions per file

---

## Tag Dimension Explanations

### Domain Tags (`#domain`)
What the note is about - the subject matter or field of knowledge

### Type Tags (`#type/`)
The kind or format of note - how it functions in your system

### Status Tags (`#status/`)
The development or completion status - maturity level

### Source Tags (`#source/`)
Where the information came from - the origin

### Priority Tags (`#priority/`)
Urgency or importance level - for tasks and projects

### Maturity Tags (`#maturity/`)
How established or proven the content is - especially for techniques

---

## Related Notes

- [[reference-taxonomy-pur3v4d3r-tags_202511190109|Complete Tag Taxonomy]]
- [[tag-taxonomies.js|Tag Taxonomy Script]]
- [[batch-tag-suggester.js|Batch Tag Suggester Script]]

---

*Last Updated: 2025-11-21*
