---
# ═══════════════════════════════════════════════════════════════════════════
# CORE IDENTITY
# ═══════════════════════════════════════════════════════════════════════════
title: "TASK Query Type Fundamentals"
aliases:
  - "TASK Query Type Fundamentals"
  - "TQTF"
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
  - vault-architecture
  - dashboard-design
  - critical-thinking/problem-solving
  - instructional-design-pkm
  - cognitive-resources

domain: other
subdomains:
  - 

# ═══════════════════════════════════════════════════════════════════════════
# TEMPORAL
# ═══════════════════════════════════════════════════════════════════════════
created: 2026-04-01
updated: 2026-04-01

# ═══════════════════════════════════════════════════════════════════════════
# SOURCE TRACKING
# ═══════════════════════════════════════════════════════════════════════════
source-type: report-extraction
source-reports:
  - "reference-comprehensive-dataview-tasks-quieries-2025120204"
evidence-quality: medium
extraction-method: "pkb-extractor-v1 → permanent-notes-generator-v1"
pipeline-version: "2.1.0"
extraction-date: "2026-04-01"

# ═══════════════════════════════════════════════════════════════════════════
# CONTENT CHARACTERISTICS
# ═══════════════════════════════════════════════════════════════════════════
complexity-level: intermediate
depth-level: comprehensive

# ═══════════════════════════════════════════════════════════════════════════
# RELATIONSHIPS
# ═══════════════════════════════════════════════════════════════════════════
prerequisites:
  []

related:
  []

broader:
  []

narrower:
  []

see-also:
  - "[[Dataview-Task-Query-Reference|Dataview Task Query Reference]]"
  - "[[Dataview-Plugin|Dataview Plugin]]"
  - "[[Task-Management|Task Management]]"
  - "[[DQL]]"
  - "[[DataviewJS]]"
  - "[[Tasks-Plugin|Tasks Plugin]]"
  - "[[YAML-Frontmatter|YAML Frontmatter]]"
  - "[[Inline-Fields|Inline Fields]]"
  - "[[Daily-Notes|Daily Notes]]"
  - "[[WHERE-Clause|WHERE Clause]]"
  - "[[GROUP-BY|GROUP BY]]"
  - "[[Date-Functions|Date Functions]]"
  - "[[Priority-Management|Priority Management]]"
  - "[[03-notes01-permanent-notes02-personal-knowledge-baseTime-Blocking|03-notes/01_permanent-notes/02_personal-knowledge-base/Time Blocking]]"
  - "[[GTD-Workflow|GTD Workflow]]"
  - "[[Dashboard-Design|Dashboard Design]]"
  - "[[Query-Performance|Query Performance]]"
  - "[[Dataview-Plugin|Dataview Plugin]]"
  - "[[Task-Management|Task Management]]"
  - "[[Obsidian]]"

# ═══════════════════════════════════════════════════════════════════════════
# LEARNING PATHWAYS
# ═══════════════════════════════════════════════════════════════════════════
builds-on:
  []

enables:
  []

expansion-topics:
  []

# ═══════════════════════════════════════════════════════════════════════════
# PERSONAL KNOWLEDGE MANAGEMENT
# ═══════════════════════════════════════════════════════════════════════════
review-frequency: quarterly
mastery-stage: seedling
importance: medium
---

# TASK Query Type Fundamentals

> [!definition] **TASK Query Type Fundamentals** *(from [[reference-comprehensive-dataview-tasks-quieries-2025120204]])*
> The `TASK` query type is unique in [[Dataview-Plugin]] because it operates at **task level** rather than page level, enabling granular filtering of individual task items. It's the only Dataview query that can **modify your files**—checking a task in a Dataview view updates the original file.

## Core Explanation

<!-- Expand this section with deeper explanation -->

## Practical Implications

> [!example] **Application**
> *Describe how this concept applies in practice.*

> [!warning] **Key Distinction** *(from [[reference-comprehensive-dataview-tasks-quieries-2025120204]])*
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

## Concrete Examples

> [!example] **Today's Schedule (Time-Blocked Tasks)** *(from [[reference-comprehensive-dataview-tasks-quieries-2025120204]])*
> **Query:**
> 
> TASK
> WHERE scheduled = date(today)
>   AND contains(text, " - ")
> SORT regexreplace(text, "^.*?(\d{2}:\d{2}).*", "$1") ASC
> 
> 
> **What it does:** Shows only tasks scheduled for today that have time blocks (e.g., `10:00 - 11:00`), sorted chronologically by start time.
> 
> **Use case:** Morning planning dashboard—displays your day's timeline in order
> 
> **Required task format:**
> ```markdown
> - [ ] Team standup 09:00 - 09:30 ⏳ 2025-12-02
> - [ ] Code review session 10:00 - 11:30 ⏳ 2025-12-02
> - [ ] Lunch break 12:00 - 13:00 ⏳ 2025-12-02
> ```

> [!example] **All Today's Tasks (Simple View)** *(from [[reference-comprehensive-dataview-tasks-quieries-2025120204]])*
> **Query:**
> ```
> TASK
> WHERE scheduled = date(today)
>   AND !completed
> SORT priority DESC, due ASC
> ```
> 
> **What it does:** Lists all incomplete tasks scheduled for today, prioritizing high-priority items first, then sorting by deadline.
> 
> **Use case:** Clean daily task list without time constraints

> [!example] **Today's Completed Tasks (Work Log)** *(from [[reference-comprehensive-dataview-tasks-quieries-2025120204]])*
> **Query:**
> ```
> TASK
> WHERE completion = date(today)
> SORT file.ctime DESC
> ```
> 
> **What it does:** Shows all tasks marked complete today, reverse chronological order
> 
> **Use case:** End-of-day review / accomplishment tracking / time logging

> [!example] **Overdue High-Priority Tasks (Triage View)** *(from [[reference-comprehensive-dataview-tasks-quieries-2025120204]])*
> **Query:**
> ```
> TASK
> WHERE due < date(today)
>   AND !completed
>   AND (contains(text, "⏫") OR contains(text, "🔼"))
> ```
> 
> **What it does:** Finds incomplete tasks with missed deadlines that are high or highest priority (using [[Tasks-Plugin]] emoji: ⏫ = highest, 🔼 = high)
> 
> **Use case:** Emergency attention queue—what needs immediate action
> 
> **Compatible task format:**
> ``
> - [ ] File quarterly taxes ⏫ 📅 2025-11-30
> - [ ] Review contract amendments 🔼 📅 2025-11-25
> ```

> [!example] **Tasks Grouped by Priority (All Levels)** *(from [[reference-comprehensive-dataview-tasks-quieries-2025120204]])*
> **Query:**
> ```
> TABLE WITHOUT ID
>   text as "Task",
>   scheduled as "When",
>   due as "Deadline"
> WHERE !completed
> GROUP BY
>   choice(contains(text, "⏫"), "⏫ Highest",
>   choice(contains(text, "🔼"), "🔼 High",
>   choice(contains(text, "🔽"), "🔽 Low",
>   choice(contains(text, "⬇"), "⬇ Lowest", "Normal"))))
> SORT choice(contains(text, "⏫"), 1,
>      choice(contains(text, "🔼"), 2,
>      choice(contains(text, "🔽"), 4,
>      choice(contains(text, "⬇"), 5, 3)))) ASC
> ```
> 
> **What it does:** Creates a TABLE view grouped by priority level (Highest → High → Normal → Low → Lowest) with intelligent sorting
> 
> **Use…

> [!example] **Weekly Task Timeline** *(from [[reference-comprehensive-dataview-tasks-quieries-2025120204]])*
> **Query:**
> ```
> TASK
> WHERE scheduled >= date(today)
>   AND scheduled <= date(today) + dur(7 days)
>   AND !completed
> SORT scheduled ASC
> ```
> 
> **What it does:** All incomplete tasks scheduled for the next 7 days
> 
> **Use case:** Week-ahead planning view / sprint planning

> [!example] **Unscheduled Tasks with Approaching Deadlines** *(from [[reference-comprehensive-dataview-tasks-quieries-2025120204]])*
> **Query:**
> ```
> TASK
> WHERE !scheduled
>   AND !completed
>   AND due <= date(today) + dur(3 days)
> SORT due ASC
> ```
> 
> **What it does:** Finds tasks with deadlines within 3 days that haven't been scheduled yet
> 
> **Use case:** "Tasks I forgot to plan" inbox—catches upcoming deadlines before they become emergencies

> [!example] **Monthly Review Queue** *(from [[reference-comprehensive-dataview-tasks-quieries-2025120204]])*
> ```
> TASK
> WHERE due >= date(today) 
>   AND due <= date(today) + dur(30 days)
>   AND !completed
> GROUP BY dateformat(due, "yyyy-MM (MMMM)") as "Month"
> SORT due ASC
> ```
> 
> **What it does:** Groups tasks by month for the next 30 days
> 
> **Use case:** Long-term planning / capacity assessment

> [!example] **Tasks Linked to Specific Project** *(from [[reference-comprehensive-dataview-tasks-quieries-2025120204]])*
> **Query:**
> ```
> TASK
> WHERE contains(text, "[[Project X]]")
>   AND !completed
> SORT priority DESC, due ASC
> ```
> 
> **What it does:** Finds all incomplete tasks mentioning a specific project note
> 
> **Use case:** Project-specific task list (replace "Project X" with your note name)
> 
> **Pattern variation for multiple projects:**
> ```dataview
> TASK
> WHERE (contains(text, "[[Project-Alpha]]") 
>    OR contains(text, "[[Project Beta]]"))
>   AND !completed
> GROUP BY regexreplace(text, ".*\[\[([^\]]+)\]\].*", "$1") as "Project"
> ```

> [!example] **Tasks by Source Daily Note (Recent Activity)** *(from [[reference-comprehensive-dataview-tasks-quieries-2025120204]])*
> **Query:**
> ```
> TABLE WITHOUT ID
>   rows.text as "Tasks"
> FROM #daily-note
> WHERE file.tasks
> GROUP BY file.link
> SORT file.ctime DESC
> LIMIT 10
> ```
> 
> **What it does:** Shows tasks from the 10 most recent [[Daily-Notes]], grouped by date
> 
> **Use case:** "What did I capture this week?" review / task audit

> [!example] **Tasks by Section Heading** *(from [[reference-comprehensive-dataview-tasks-quieries-2025120204]])*
> **Query:**
> ```
> TASK
> FROM "Projects"
> WHERE !completed
> GROUP BY section
> SORT section ASC
> ```
> 
> **What it does:** Groups tasks by the heading they appear under in source files
> 
> **Use case:** Organizing tasks by document structure (e.g., all tasks under "## Research" vs "## Implementation")

> [!example] **Tasks with Time Estimates** *(from [[reference-comprehensive-dataview-tasks-quieries-2025120204]])*
> **Query:**
> ```
> TASK
> WHERE estimated
>   AND !completed
> SORT estimated DESC
> ```
> 
> **What it does:** Finds tasks with `[estimated:: duration]` [[Inline-Fields]]
> 
> **Use case:** [[03-notes/01_permanent-notes/02_personal-knowledge-base/Time Blocking]] / capacity planning / velocity tracking
> 
> **Required task format:**
> ```markdown
> - [ ] Write documentation [estimated:: 4h] ⏳ 2025-12-02
> - [ ] Code review [estimated:: 1.5h] ⏳ 2025-12-02
> ```
> 
> **Calculate total estimated time:**
> ```dataview
> TABLE
>   sum(rows.estimated) as "Total Hours"
> WHERE estimated AND !completed
> GROUP BY file.folder
> ```

> [!example] **Tasks by Custom Status Field** *(from [[reference-comprehensive-dataview-tasks-quieries-2025120204]])*
> **Query:**
> ```
> TASK
> WHERE task-status
>   AND !completed
> GROUP BY task-status
> ```
> 
> **What it does:** Groups tasks by custom status inline field (e.g., `[task-status:: in-review]`)
> 
> **Use case:** Kanban-style workflow tracking
> 
> **Task format example:**
> ```markdown
> - [ ] Implement feature X [task-status:: in-progress] [assignee:: [[Alice]]]
> - [ ] Test feature Y [task-status:: in-review] [assignee:: [[Bob]]]
> - [ ] Deploy feature Z [task-status:: blocked] [assignee:: [[Carol]]]
> ```

> [!example] **Multi-Condition Task Filter (Complex Logic)** *(from [[reference-comprehensive-dataview-tasks-quieries-2025120204]])*
> **Query:**
> ```
> TASK
> WHERE !completed
>   AND (
>     (contains(text, "⏫") AND due < date(today) + dur(2 days))
>     OR
>     (contains(text, "🔼") AND due < date(today))
>   )
>   AND !contains(text, "[[Blocked]]")
> SORT due ASC
> ```
> 
> **What it does:** 
> - Highest priority tasks due within 2 days, OR
> - High priority tasks that are overdue
> - Excludes any task linked to a "Blocked" status note
> 
> **Use case:** Intelligent prioritization—surfaces what actually needs attention right now

> [!example] **Recurring Tasks Pattern** *(from [[reference-comprehensive-dataview-tasks-quieries-2025120204]])*
> **Query:**
> ```
> TASK
> WHERE contains(text, "🔁")
>   AND scheduled <= date(today)
> SORT scheduled ASC
> ```
> 
> **What it does:** Finds [[Tasks-Plugin]] recurring tasks (marked with 🔁) that are due today or earlier
> 
> **Use case:** Daily habit tracking / recurring maintenance tasks
> 
> **Recurring task format:**
> ```markdown
> - [ ] Review inbox 🔁 every day ⏳ 2025-12-02
> - [ ] Weekly planning 🔁 every Monday ⏳ 2025-12-02
> ```

> [!example] **Tasks WITHOUT Certain Tags** *(from [[reference-comprehensive-dataview-tasks-quieries-2025120204]])*
> **Query:**
> ```
> TASK
> WHERE !completed
>   AND !contains(tags, "#waiting")
>   AND !contains(tags, "#someday")
> SORT due ASC
> ```
> 
> **What it does:** Filters out tasks in "waiting" or "someday/maybe" categories
> 
> **Use case:** Actionable task list (excluding deferred items per [[GTD-Workflow]])

> [!example] **Show Tasks or Success Message** *(from [[reference-comprehensive-dataview-tasks-quieries-2025120204]])*
> **DataviewJS:**
> ```
> const dql = dv.tryQuery(`
> TASK
> WHERE due < date(today)
>   AND !completed
>   AND contains(text, "📅")
> SORT due asc
> `);
> 
> dql ? dv.taskList(dql) : dv.paragraph("✅ Well done! No overdue tasks.");
> ```
> 
> **What it does:** Shows overdue tasks if any exist; otherwise displays a congratulatory message
> 
> **Use case:** Motivation-friendly dashboard that celebrates when you're caught up

> [!example] **Tasks Grouped by Priority with Custom Headers** *(from [[reference-comprehensive-dataview-tasks-quieries-2025120204]])*
> **DataviewJS:**
> ```javascript
> const priorityMap = {
>   '⏫': 'Highest Priority',
>   '🔼': 'High Priority', 
>   'normal': 'Normal Priority',
>   '🔽': 'Low Priority'
> };
> 
> function getPriority(task) {
>   if (task.text.includes('⏫')) return '⏫';
>   if (task.text.includes('🔼')) return '🔼';
>   if (task.text.includes('🔽')) return '🔽';
>   return 'normal';
> }
> 
> const tasks = dv.pages()
>   .file.tasks
>   .where(t => !t.completed)
>   .groupBy(t => getPriority(t));
> 
> for (let group of tasks) {
>   dv.header(3, priorityMap[group.key]);
>   dv.taskList(group.rows);
> }
> ```
> 
> **What it does:** Creates custom section headers for…

> [!example] **Task Completion Statistics** *(from [[reference-comprehensive-dataview-tasks-quieries-2025120204]])*
> **DataviewJS:**
> ```javascript
> const allTasks = dv.pages().file.tasks;
> const completed = allTasks.where(t => t.completed).length;
> const incomplete = allTasks.where(t => !t.completed).length;
> const overdue = allTasks.where(t => !t.completed && t.due && t.due < dv.date('today')).length;
> 
> dv.header(3, "📊 Task Statistics");
> dv.table(
>   ["Metric", "Count", "Percentage"],
>   [
>     ["Total Tasks", allTasks.length, "100%"],
>     ["Completed", completed, `${Math.round(completed/allTasks.length*100)}%`],
>     ["Incomplete", incomplete, `${Math.round(incomplete/allTasks.length*100)}%`],
>     ["Overdue",…

> [!example] **Today's Schedule with Duration Extraction** *(from [[reference-comprehensive-dataview-tasks-quieries-2025120204]])*
> **DataviewJS:**
> ```javascript
> const today = dv.pages()
>   .file.tasks
>   .where(t => t.scheduled?.toString() === dv.date('today').toString())
>   .where(t => t.text.includes(' - '));
> 
> const schedule = today.map(t => {
>   const timeMatch = t.text.match(/(\d{2}:\d{2})\s*-\s*(\d{2}:\d{2})/);
>   const taskText = t.text.replace(/\d{2}:\d{2}\s*-\s*\d{2}:\d{2}/, '').trim();
>   
>   return {
>     time: timeMatch ? timeMatch[0] : 'No time',
>     task: taskText,
>     completed: t.completed
>   };
> }).sort(t => t.time);
> 
> dv.table(
>   ["Time", "Task", "Status"],
>   schedule.map(s => [s.time, s.task, s.completed ? "✅" :…

> [!example] **Project Tasks with Subtask Structure** *(from [[reference-comprehensive-dataview-tasks-quieries-2025120204]])*
> **DataviewJS:**
> ```javascript
> const projectTasks = dv.page('"Projects/Q4 Initiative"')
>   .file.tasks
>   .where(t => !t.parent); // Only root-level tasks
> 
> for (let task of projectTasks) {
>   dv.paragraph(`**${task.text}**`);
>   
>   if (task.children && task.children.length > 0) {
>     const childList = task.children.map(c => `  - ${c.text}`).join('\n');
>     dv.paragraph(childList);
>   }
>   
>   dv.paragraph("---");
> }
> ```
> 
> **What it does:** Displays tasks with their subtasks in a hierarchical view
> 
> **Use case:** Project breakdown visualization / work package structure

> [!example] **Automated Daily Note Task Summary** *(from [[reference-comprehensive-dataview-tasks-quieries-2025120204]])*
> **Add to Daily Note Template:**
> ````markdown
> ## 📋 Today's Tasks
> 
> ```dataview
> TASK
> WHERE scheduled = this.file.day
>   AND !completed
> SORT contains(text, "⏫") DESC, contains(text, "🔼") DESC, due ASC
> ```
> 
> ## ⏰ Time-Blocked Schedule
> 
> ```dataview
> TABLE WITHOUT ID
>   regexreplace(text, "^(.*?)(\d{2}:\d{2} - \d{2}:\d{2})(.*)$", "$1$3") as "Task",
>   regexreplace(text, "^.*?(\d{2}:\d{2} - \d{2}:\d{2}).*$", "$1") as "Time"
> WHERE scheduled = this.file.day
>   AND contains(text, " - ")
> SORT regexreplace(text, "^.*?(\d{2}:\d{2}).*", "$1") ASC
> ```
> 
> ## ✅ Completed Today
> 
> ```dataview
> TASK
> WHERE completion =…

> [!example] **Complete Weekly Task Dashboard** *(from [[reference-comprehensive-dataview-tasks-quieries-2025120204]])*
> ````markdown
> # 📅 Weekly Task Dashboard
> 
> ## 🚨 Overdue & Urgent
> 
> ```dataview
> TASK
> WHERE due < date(today)
>   AND !completed
>   AND (contains(text, "⏫") OR contains(text, "🔼"))
> SORT due ASC
> ```
> 
> ## 📆 This Week's Schedule
> 
> ```dataview
> TABLE WITHOUT ID
>   text as "Task",
>   dateformat(scheduled, "EEEE, MMM dd") as "Day",
>   due as "Due"
> WHERE scheduled >= date(today)
>   AND scheduled <= date(today) + dur(7 days)
>   AND !completed
> SORT scheduled ASC
> ```
> 
> ## 📊 Weekly Progress
> 
> ```dataviewjs
> const weekStart = dv.date('today').minus({days: dv.date('today').weekday});
> const weekEnd = weekStart.plus({days:…

> [!example] **Project-Specific Task Kanban** *(from [[reference-comprehensive-dataview-tasks-quieries-2025120204]])*
> ````markdown
> # 🎯 Project: [Project Name]
> 
> ## 📥 Backlog
> 
> ```dataview
> TASK
> WHERE contains(text, "[[Project-Name]]")
>   AND !scheduled
>   AND !completed
> SORT file.ctime DESC
> ```
> 
> ## 🏃 In Progress
> 
> ```dataview
> TASK
> WHERE contains(text, "[[Project-Name]]")
>   AND scheduled <= date(today)
>   AND !completed
> SORT priority DESC, due ASC
> ```
> 
> ## ⏸️ Blocked
> 
> ```dataview
> TASK
> WHERE contains(text, "[[Project-Name]]")
>   AND contains(text, "[[Blocked]]")
>   AND !completed
> ```
> 
> ## ✅ Completed (Last 7 Days)
> 
> ```dataview
> TASK
> WHERE contains(text, "[[Project-Name]]")
>   AND completion >= date(today) - dur(7…

## Connections & Context

**Cross-report connections** *(from [[reference-comprehensive-dataview-tasks-quieries-2025120204]])*:
- [[Tasks-Plugin|Tasks Plugin]]
- [[Dataview-Plugin|Dataview Plugin]]

**Related concepts:**
[[Dataview-Task-Query-Reference|Dataview Task Query Reference]] · [[Dataview-Plugin|Dataview Plugin]] · [[Task-Management|Task Management]] · [[DQL]] · [[DataviewJS]] · [[Tasks-Plugin|Tasks Plugin]] · [[YAML-Frontmatter|YAML Frontmatter]] · [[Inline-Fields|Inline Fields]] · [[Daily-Notes|Daily Notes]] · [[WHERE-Clause|WHERE Clause]] · [[GROUP-BY|GROUP BY]] · [[Date-Functions|Date Functions]] · [[Priority-Management|Priority Management]] · [[03-notes01-permanent-notes02-personal-knowledge-baseTime-Blocking|03-notes/01_permanent-notes/02_personal-knowledge-base/Time Blocking]] · [[GTD-Workflow|GTD Workflow]] · [[Dashboard-Design|Dashboard Design]] · [[Query-Performance|Query Performance]] · [[Dataview-Plugin|Dataview Plugin]] · [[Task-Management|Task Management]] · [[Obsidian]] · [[DQL]] · [[DataviewJS]] · [[Tasks-Plugin|Tasks Plugin]] · [[Inline-Fields|Inline Fields]] · [[03-notes01-permanent-notes02-personal-knowledge-baseTime-Blocking|03-notes/01_permanent-notes/02_personal-knowledge-base/Time Blocking]] · [[Dataview-Plugin|Dataview Plugin]] · [[Dataview-Plugin|Dataview Plugin]] · [[Note]] · [[Note]] · [[Inline-Fields|Inline Fields]]

## Methodology Notes

> [!methodology-and-sources] **Task Metadata Architecture** *(from [[reference-comprehensive-dataview-tasks-quieries-2025120204]])*
> Every task in your vault automatically inherits these implicit fields from [[Dataview-Plugin]]:

> [!methodology-and-sources] **DataviewJS for Tasks** *(from [[reference-comprehensive-dataview-tasks-quieries-2025120204]])*
> [[DataviewJS]] provides JavaScript-based query capabilities for complex task manipulation, custom rendering, and dynamic filtering that's difficult or impossible with [[DQL]] alone.

---

## Source Attribution

**Extracted from:** [[reference-comprehensive-dataview-tasks-quieries-2025120204]]
