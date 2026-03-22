---
# ═══════════════════════════════════════════════════════════════════════════
# CORE IDENTITY
# ═══════════════════════════════════════════════════════════════════════════
title: "Core DataviewJS Task Methods"
aliases:
  - "Core DataviewJS Task Methods"
  - "CDTM"
type: permanent-note
status: evergreen
confidence: medium

# ═══════════════════════════════════════════════════════════════════════════
# CLASSIFICATION
# ═══════════════════════════════════════════════════════════════════════════
tags:
  - permanent-note
  - evergreen
  - other
  - type/report
  - year/2025
  - type/tutorial
  - status/in-progress
  - pkb

domain: other
subdomains:
  - 

# ═══════════════════════════════════════════════════════════════════════════
# TEMPORAL
# ═══════════════════════════════════════════════════════════════════════════
created: 2026-03-22
updated: 2026-03-22

# ═══════════════════════════════════════════════════════════════════════════
# SOURCE TRACKING
# ═══════════════════════════════════════════════════════════════════════════
source-type: report-extraction
source-reports:
  - "reference-comprehensive-dataview-tasks-quieries-2025120204"
evidence-quality: medium
extraction-method: "pkb-extractor-v1 → permanent-notes-generator-v1"

# ═══════════════════════════════════════════════════════════════════════════
# CONTENT CHARACTERISTICS
# ═══════════════════════════════════════════════════════════════════════════
complexity-level: intermediate
depth-level: comprehensive

# ═══════════════════════════════════════════════════════════════════════════
# RELATIONSHIPS
# ═══════════════════════════════════════════════════════════════════════════
prerequisites:
  - "[[]]"

related:
  - "[[]]"

broader:
  - "[[]]"

narrower:
  - "[[]]"

see-also:
  - "[[Dataview-Task-Query-Reference|Dataview Task Query Reference]]"
  - "[[Dataview-Plugin|Dataview Plugin]]"
  - "[[Task-Management|Task Management]]"
  - "[[DQL]]"
  - "[[DataviewJS]]"
  - "[[Tasks-Plugin|Tasks Plugin]]"
  - "[[YAML-Frontmatter|YAML Frontmatter]]"
  - "[[Inline-Fields|Inline Fields]]"

# ═══════════════════════════════════════════════════════════════════════════
# LEARNING PATHWAYS
# ═══════════════════════════════════════════════════════════════════════════
builds-on:
  - "[[]]"

enables:
  - "[[]]"

expansion-topics:
  - topic: "[[]]"
    description: ""
    priority: medium

# ═══════════════════════════════════════════════════════════════════════════
# PERSONAL KNOWLEDGE MANAGEMENT
# ═══════════════════════════════════════════════════════════════════════════
review-frequency: quarterly
mastery-stage: seedling
importance: medium
---

# Core DataviewJS Task Methods

> [!definition] **Core DataviewJS Task Methods**
> - `dv.pages()` - Get pages as DataArray
> - `.file.tasks` - Access all tasks in a file (including subtasks)
> - `.where()` - Filter tasks (equivalent to WHERE in DQL)
> - `.groupBy()` - Group tasks by field
> - `dv.taskList()` - Render tasks as interactive checklist

## Core Explanation

<!-- Expand this section with deeper explanation -->

## Practical Implications

> [!example] **Application**
> *Describe how this concept applies in practice.*

> [!warning] **Key Distinction**
> **Avoid These Patterns:**
> 
> ❌ **Regex in tight loops:**
> ```dataview
> TASK
> WHERE regexmatch("\d{2}:\d{2}", text)  # Slow on large vaults
> ```
> ✅ **Better:**
> ```dataview
> TASK
> WHERE contains(text, ":")  # Pre-filter, then regex if needed
> ```
> 
> ❌ **Nested FLATTEN without limits:**
> ```dataview
> TABLE
> FROM #project
> FLATTEN file.tasks  # Could explode to thousands of rows
> ```
> ✅ **Better:**
> ```dataview
> TABLE
> FROM #project
> WHERE file.tasks
> LIMIT 100
> ```

## Connections & Context

**Cross-report connections:**
- [[Tasks-Plugin|Tasks Plugin]]
- [[Dataview-Plugin|Dataview Plugin]]

**Related concepts:**
[[Dataview-Task-Query-Reference|Dataview Task Query Reference]] · [[Dataview-Plugin|Dataview Plugin]] · [[Task-Management|Task Management]] · [[DQL]] · [[DataviewJS]] · [[Tasks-Plugin|Tasks Plugin]] · [[YAML-Frontmatter|YAML Frontmatter]] · [[Inline-Fields|Inline Fields]] · [[Daily-Notes|Daily Notes]] · [[WHERE-Clause|WHERE Clause]] · [[GROUP-BY|GROUP BY]] · [[Date-Functions|Date Functions]] · [[Priority-Management|Priority Management]] · [[03-notes01-permanent-notes02-personal-knowledge-baseTime-Blocking|03-notes/01_permanent-notes/02_personal-knowledge-base/Time Blocking]] · [[GTD-Workflow|GTD Workflow]]
