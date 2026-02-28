---
title: Dataview-Queries-for-Taks-Log_🆔20251101181433
id: 20251101181446
type: ⚙️reference
status: 🌱seedling
rating: ""
source: gemini-2.5-flash
url: https://gemini.google.com/app/7ebcf09b8e6ba222
tags:
  - type/reference
  - type/reference
  - type/reference
  - pkb/plugin/dataview
  - pkb/plugin/dataview
aliases:
  - dataview queries/task-log
  - Task Log Dataview
  - Dataview Tasks
link-up:
  - "[[Dataview_Cheat-Sheet]]"
link-related:
  - "[[Dataview_Cheat-Sheet]]"
  - "[[🧠Report_How-to-write-Dataview-Queries]]"
  - "[[🧠Report_The Dataview Query Language (DQL) Explained]]"
  - "[[🧠Report_The-Obsidian-Dataview-Plugin]]"
  - "[[Ref_Gemini_Obsidian-Dataview-Plugin_Search-Queries_2025-09-12]]"
  - "[[REF_Gemini-Deep-Research_Guide-to-Plugin-Dataview_2025-09-11]]"
  - "[[Ref_Gemini-Dr_Dataview-Walkthrough_2025-09-11]]"
date created: 2025-11-01T18:14:46
date modified: 2025-11-11T06:27:05
---

# PROMPT

Use this information to construct dataview queries:

1. This is the location of my daily note, where I want the query to pull from.

```
01 📅Daily-Notes
```

1. This is the QuickAdd Capture format. (Considered a Task)

```
- [ ] {{VALUE:Task description?}} ➕ {{DATE:YYYY-MM-DD}} {{VALUE:Priority?|⏫,🔼,🔽}} 🔗 [[{{LINKCURRENT}}]]`
```

---

# RESPONSE

## QUERY FOR TASKS CREATED TODAY

- The following query targets your Daily Notes folder, filters specifically for tasks created on the current day using the ➕ created date, and sorts them by priority and time.

---

```
TASK
FROM "01 📅Daily-Notes"
WHERE created = date(today)
  AND !completed
SORT priority DESC, created ASC
```

### BREAKDOWN OF THE QUERY

1. TASK	Defines the query type.	Essential for querying checklist items and their task-level metadata.
2. FROM "01 📅Daily-Notes"	Defines the scope.	Restricts the search to your dedicated Daily Notes folder.
3. WHERE created = date(today)	Filters by creation date.	Targets the ➕ YYYY-MM-DD field (which Dataview interprets as task.created) and ensures it matches the current date.
4. AND !completed	Filters by status.	Ensures only incomplete (open) tasks are displayed, as indicated by the empty box (- [ ]).
5. SORT priority DESC, created ASC	Orders the results.	Sorts tasks by High Priority (DESC) first, then by Creation Time (ASC), so the oldest tasks you created this morning appear before newer ones of the same priority.

## QUERY FOR REVIEWING ALL CAPTURED TASKS

- Here is a helpful query to view the details of all tasks created today in a more structured **Table** format:

```
TABLE 
  text AS "Task Description",
  priority AS Priority,
  created AS "Captured On",
  link AS Source
FROM "01 📅Daily-Notes"
WHERE created = date(today)
  AND !completed
SORT priority DESC
```
