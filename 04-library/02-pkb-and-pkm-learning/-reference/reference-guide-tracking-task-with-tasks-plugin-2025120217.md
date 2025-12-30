---
aliases:
  - "Task Tracking with Dataview"
  - "Tasks + Dataview Guide"
tags:
  - "type/report"
  - "year/2025"
  - "type/reference"
  - "status/in-progress"
  - "pkb"
  - "pkm"
  - "review-system"
  - "cognitive-science/cognitive-load"
  - "skill-acquisition"
  - "cognitive-resources"
  - "pkb/optimization"
  - "dataview-queries"
  - "cognitive-pkm"
source: "claude-sonnet-4.5"
id: "20251202174009"
created: "2025-12-02T17:40:09"
modified: "2025-12-02T17:40:09"
week: "[[2025-W49]]"
month: "[[2025-12]]"
quarter: "[[2025-Q4]]"
year: "[[2025]]"
type: "reference"
maturity: "needs-review"
confidence: "speculative"
next-review: "2025-12-09"
review-count: 0
link-up:
  - "[[pkb-&-pkm-moc]]"
link-related:
  - "[[2025-12-02|Daily-Note]]"
---
# Tracking Tasks with Tasks Plugin and Dataview

> [!overview]
> - **Title**:: [[Tracking Tasks with Tasks Plugin and Dataview]]
> - **Prompt/Topic Used**:: 
> - **Status**:: 🌱 `= this.maturity` | Confidence: `= this.confidence`

## 📊 Note Metadata Dashboard
> [!fail] 🛠️ Metadata Health Check
> **Missing Fields**:: `$= const fields = ["status", "type", "tags"]; const missing = fields.filter(f => !dv.current()[f]); missing.length > 0 ? "⚠️ Missing: " + missing.join(", ") : "✅ All Systems Go"`

> [!metadata]
> **Note-Type**: `= this.type`
> **Development Status**: `= this.maturity`  
> **Epistemic Confidence**: `= this.confidence`  
> **Next Review**: `= this.next-review`  
> **Review Count**: `= this.review-count`  
> **Created**: `= this.created`  
> **Last Modified**: `= this.modified`

> [!quote] 📝 Content Metrics
> **Word Count**:: `= this.file.size` B | **Est. Read Time**:: `= round(this.file.size / 1300) + " min"`
> **Depth Class**:: `= choice(this.file.size < 500, "🌱 Stub", choice(this.file.size < 2000, "📄 Note", "📜 Essay"))`

> [!calendar] 🕰️ Temporal Context
> **Created**:: `= this.file.ctime` | **Age**:: `= (date(today) - this.file.ctime).days + " days"`
> **Last Touch**:: `= this.file.mtime` | **Staleness**:: `= choice((date(today) - this.file.mtime).days > 180, "🕸️ Cobwebs", choice((date(today) - this.file.mtime).days > 30, "🍂 Cold", "🔥 Fresh"))`

> [!network] 🔗 Network Connectivity
> **In-Links**:: `= length(this.file.inlinks)` | **Out-Links**:: `= length(this.file.outlinks)`
> **Network Status**:: `= choice(length(this.file.inlinks) = 0, "🕸️ Orphan", choice(length(this.file.inlinks) > 5, "⚡ Hub", "🌱 Node"))`

```dataviewjs
// 🧠 SYSTEM: Semantic Bridge Engine
// PURPOSE: Find "Sibling" notes that share the same Outlinks (Contexts)
const current = dv.current();
const myOutlinks = current.file.outlinks.map(l => l.path);

// 1. Filter the Vault
const siblings = dv.pages()
    .where(p => p.file.path !== current.file.path) // Exclude self
    .where(p => !current.file.outlinks.map(l => l.path).includes(p.file.path)) // Exclude existing direct links
    .map(p => {
        // Find overlap between this page's links and the current page's links
        const shared = p.file.outlinks.filter(l => myOutlinks.includes(l.path));
        return { 
            link: p.file.link, 
            sharedCount: shared.length, 
            sharedLinks: shared 
        };
    })
    .where(p => p.sharedCount > 0) // Must share at least 1 connection
    .sort(p => p.sharedCount, "desc") // Sort by strongest connection
    .limit(5); // Only show top 5

// 2. Render the Bridge
if (siblings.length > 0) {
    dv.header(4, "🌉 Semantic Bridges (Missing Connections)");
    dv.table(
        ["Sibling Note", "Strength", "Shared Context"], 
        siblings.map(s => [
            s.link, 
            "🔗 " + s.sharedCount, 
            s.sharedLinks.slice(0, 3).join(", ") + (s.sharedCount > 3 ? "…" : "")
        ])
    );
} else {
    dv.paragraph("*No semantic siblings found. This note is unique in its connections.*");
}
```
### Related Notes
```dataview
TABLE type, maturity, confidence
FROM  ""
WHERE  type = "reference"
SORT "maturity" DESC
LIMIT 15
```
### Sources & References
```dataview
TABLE 
    source AS "Source Type",
    created AS "Date Added"
FROM [[]]
WHERE "claude-sonnet-4.5"
SORT created DESC
```
### Backlinks & Connections
```dataview
TABLE 
    type AS "Type",
    maturity AS "Maturity",
    created AS "Created"
FROM [[#]]
SORT created DESC
LIMIT 15
```
### 2025-12-02 - Initial Creation
*Context*: `=this.alias1` *or* `=this.alias2` **by**: `=this.source`
*Maturity*: `= this.maturity`  
*Confidence*: `= this.confidence`

### Tags & Classification
*Primary Tags*: `= this.tags`  
*Type*: `= this.type`  
*Source*: `= this.source`

### Review System
> [!important] Review Schedule
> - **Next Review**: `= this.next-review`
> - **Review Frequency**: Based on maturity level
>   - Seedling: Weekly
>   - Budding: Bi-weekly
>   - Developing: Monthly
>   - Evergreen: Quarterly


---

> [! ] ### Claude Thinking
> ## REQUEST ANALYSIS
> **Request Classification:**
> - Type: comprehensive_note
> - Scope: reference
> - Research Required: YES - Need to verify current best practices for Tasks plugin + Dataview integration in Obsidian
> - Note Type: Reference Note (technical guide)
> **User Context:**
> - Advanced Obsidian user with sophisticated PKB
> - Extensive plugin knowledge (Dataview, Templater, Meta Bind, Tasks)
> - Values automation and metadata-driven workflows
> - Needs production-ready, immediately implementable content
> **Research Needs:**
> - Tasks plugin syntax and capabilities (current version)
> - Dataview query integration with Tasks
> - Best practices for task metadata
> - Common patterns and workflows
> - Integration opportunities with user's existing system
> **Structural Planning:**
> I. Foundation Layer
>    - Tasks plugin overview
>    - Dataview overview
>    - Why combine them
>    - Prerequisites and setup
> II. Tasks Plugin Deep Dive
>    - Core syntax and features
>    - Metadata fields
>    - Emoji support
>    - Date handling
>    - Recurrence patterns
>    - Priority systems
> III. Dataview Integration
>    - Query syntax for tasks
>    - TABLE queries
>    - LIST queries
>    - TASK queries
>    - Filtering strategies
>    - Sorting approaches
> IV. Practical Patterns
>    - Project-based tracking
>    - Priority matrices
>    - Due date dashboards
>    - Status workflows
>    - Context-based views
> V. Advanced Techniques
>    - Custom metadata fields
>    - Inline fields for enrichment
>    - Templater automation
>    - Dynamic dashboards
>    - Cross-note aggregation
> VI. Optimization & Troubleshooting
>    - Performance considerations
>    - Common pitfalls
>    - Debugging queries
>    - Best practices
> **Wiki-Link Opportunities:**
> - [[Tasks Plugin]]
> - [[Dataview Plugin]]
> - [[Obsidian]]
> - [[03-notes/01_permanent-notes/02_personal-knowledge-base/Personal Knowledge Management]]
> - [[Task Management]]
> - [[YAML Frontmatter]]
> - [[Metadata-Driven Workflows]]
> - [[Query Languages]]
> - [[Templater Plugin]]
> - [[GTD (Getting Things Done)]]
> - [[Project Management in Obsidian]]
> - [[Dashboard Design]]
> - [[Inline Fields]]
> - [[JavaScript in Dataview]]
> - [[Task Prioritization]]
> - [[Date Management]]
> - [[Recurrence Patterns]]
> - [[Context-Based Productivity]]
> **Callout Strategy:**
> - [!definition] for key concepts
> - [!methodology-and-sources] for syntax rules
> - [!example] for concrete implementations
> - [!helpful-tip] for best practices
> - [!warning] for common mistakes
> - [!what-this-does] for explaining queries
> - [!core-principle] for foundational concepts
> - [!quick-reference] for syntax cheatsheets
> **Metadata Planning:**
> - Tags: #obsidian #tasks-plugin #dataview #task-management #reference-note
> - Aliases: [Task Tracking with Dataview, Tasks + Dataview Guide, Task Query Reference]
> Now I'll execute web searches to ensure current accuracy.
> Now I have sufficient research on both Tasks plugin and Dataview integration. Let me construct the comprehensive reference note.

---
tags: #obsidian #tasks-plugin #dataview #task-management #reference-note
aliases: [Task Tracking with Dataview, Tasks + Dataview Guide, Task Query Reference, Obsidian Task Management]
---

# 📋 Tracking Tasks with Tasks Plugin and Dataview

> [!the-purpose]
> **This comprehensive reference note explains how to track, query, and manage tasks in [[Obsidian]] using both the [[Tasks Plugin]] and [[Dataview Plugin]]**—two powerful tools that transform your vault into a sophisticated [[Task Management]] system. Whether you need simple task lists or complex project dashboards, this guide covers the complete integration between these essential plugins.

---

## 🎯 Why Combine Tasks Plugin with Dataview?

> [!core-principle]
> The [[Tasks Plugin]] provides **rich task metadata and interactive functionality**, while [[Dataview Plugin]] offers **powerful querying and aggregation capabilities**. Used together, they create a flexible, metadata-driven task management system that scales from simple to-do lists to enterprise-level [[Project Management in Obsidian]].

**The Synergy:**
- **Tasks Plugin**: Specialized task syntax, date handling, recurrence patterns, priority systems, and interactive task completion
- **Dataview**: Cross-vault querying, dynamic filtering, custom aggregations, and automated dashboard generation
- **Combined Power**: Create intelligent task views that adapt to your workflow, automatically surface relevant work, and maintain context within your [[03-notes/01_permanent-notes/02_personal-knowledge-base/Personal Knowledge Management]] system

> [!helpful-tip]
> **Start Simple, Scale Gradually**: Begin with Tasks plugin's native queries for project-specific views, then layer in Dataview when you need cross-vault aggregation or complex filtering logic. This prevents overwhelm while building toward sophistication.

---

## ⚙️ Foundation: Setting Up Both Plugins

### Installing and Configuring Tasks Plugin

The Tasks plugin can be installed from Obsidian's Community Plugins browser by searching for "Tasks" and enabling it in settings.

> [!methodology-and-sources]
> **Critical Initial Configuration:**
> 
> 1. **Global Task Filter** (Highly Recommended)
>    - Navigate to: `Settings → Tasks → Global Filter`
>    - Set a filter like `#task` to differentiate between regular checkboxes and actual tasks
>    - This prevents legacy checkboxes in older notes from appearing in task queries
>    - Format: Add the tag to any task you want tracked: `- [ ] Task description #task`
> 
> 2. **Recurrence Behavior**
>    - Enable "Next recurrence appears on the line below"
>    - This keeps completed recurring tasks visible as history while generating new instances below
>    - Alternative: Default places new recurrence above (useful for keeping active task at top)
> 
> 3. **Hotkey Optimization**
>    - Replace "Toggle checkbox status" with "Tasks: Toggle Done" and bind to `Ctrl+Enter` (Windows/Linux) or `Cmd+Enter` (Mac)
>    - This ensures task metadata (completion dates, etc.) is properly recorded

### Installing and Configuring Dataview

Dataview generates data from your vault by pulling information from Markdown frontmatter and inline fields.

> [!methodology-and-sources]
> **Essential Dataview Setup:**
> 
> 1. Install from Community Plugins (search "Dataview")
> 2. Enable in Settings under Community Plugins
> 3. **Important Settings to Configure:**
>    - `Enable JavaScript Queries`: Turn ON if you need advanced DataviewJS functionality
>    - `Enable Inline JavaScript Queries`: Turn ON for inline JS expressions
>    - `Date Format`: Set to match your preferred format (e.g., `yyyy-MM-dd`)
>    - `Task Completion Tracking`: Enable to auto-add completion dates when checking tasks in Dataview queries

---

## 📝 Tasks Plugin: Core Syntax and Features

### Basic Task Syntax

The [[Tasks Plugin]] extends standard Markdown checkboxes with rich metadata signifiers:

```markdown
- [ ] Basic task
- [x] Completed task
- [ ] Task with due date 📅 2024-12-15
- [ ] Task with scheduled date ⏳ 2024-12-10
- [ ] Task with start date 🛫 2024-12-01
- [ ] Recurring task 🔁 every week on Monday
- [ ] High priority task ⏫
- [ ] Low priority task 🔽
```

> [!definition]
> **Task Metadata Emojis:**
> - **📅 Due Date**: When the task must be completed
> - **⏳ Scheduled Date**: When you plan to work on the task
> - **🛫 Start Date**: When the task becomes actionable
> - **✅ Done Date**: Automatically added when task is completed
> - **🔁 Recurrence**: Pattern for repeating tasks
> - **⏫ High Priority** / **🔼 Medium Priority** / **🔽 Low Priority**
> - **🏁 Delete**: Automatically deletes task upon completion (useful for recurring checklists)

### Date Handling

> [!example]
> **Date Format Flexibility:**
> 
> Tasks plugin accepts multiple date formats:
> ```markdown
> - [ ] Task 📅 2024-12-15
> - [ ] Task 📅 2024-12-15
> - [ ] Task 📅 December 15, 2024
> - [ ] Task 📅 15 Dec 2024
> ```
> 
> **Relative Dates:**
> ```markdown
> - [ ] Task 📅 today
> - [ ] Task 📅 tomorrow
> - [ ] Task 📅 next Monday
> - [ ] Task 📅 in 2 weeks
> ```

### Recurrence Patterns

> [!methodology-and-sources]
> **Recurrence Syntax Structure:**
> 
> ```markdown
> 🔁 every [interval] [day/week/month/year] [on specific day/date]
> ```
> 
> **Examples:**
> ```markdown
> - [ ] Daily standup 🔁 every day
> - [ ] Weekly review 🔁 every week on Friday
> - [ ] Monthly report 🔁 every month on the 1st
> - [ ] Quarterly planning 🔁 every 3 months
> - [ ] Birthday reminder 🔁 every year on January 15th
> - [ ] Biweekly sprint review 🔁 every 2 weeks on Monday
> ```

> [!helpful-tip]
> **When to Use Which Date Type:**
> - Use **🛫 Start Date** for tasks with dependencies or that shouldn't appear until a specific time
> - Use **⏳ Scheduled Date** for time-blocking and planning when you'll work on something
> - Use **📅 Due Date** for hard deadlines and commitments
> - Combine all three for comprehensive task lifecycle tracking

### Priority System

> [!methodology-and-sources]
> **Priority Levels:**
> - `⏫` **Highest Priority**: Critical, urgent tasks
> - `🔼` **High Priority**: Important but not urgent
> - (no symbol) **Normal Priority**: Default state
> - `🔽` **Low Priority**: Nice-to-have, defer if needed
> - `➖` **Lowest Priority**: Someday/maybe tasks

---

## 🔍 Tasks Plugin: Native Query Syntax

### Basic Query Structure

Tasks plugin queries are written in code blocks with the `tasks` identifier:

````markdown
```tasks
# Query instructions here
```
````

> [!example]
> **Essential Query Patterns:**
> 
> **1. All Incomplete Tasks:**
> ````markdown
> ```tasks
> not done
> ```
> ````
> 
> **2. Tasks Due Today:**
> ````markdown
> ```tasks
> not done
> due today
> ```
> ````
> 
> **3. High Priority Tasks:**
> ````markdown
> ```tasks
> not done
> priority is above none
> sort by priority
> ```
> ````
> 
> **4. Tasks from Specific Folder:**
> ````markdown
> ```tasks
> not done
> path includes Projects/Active
> ```
> ````

### Advanced Filtering

> [!methodology-and-sources]
> **Powerful Filter Combinations:**
> 
> ````markdown
> ```tasks
> not done
> (due before tomorrow) OR (priority is high)
> path includes Projects
> heading includes Action Items
> sort by due
> limit 10
> ```
> ````
> 
> **Filter Operators:**
> - `includes` / `does not include`: Text matching
> - `is` / `is not`: Exact matching
> - `before` / `after`: Date comparisons
> - `AND` / `OR` / `NOT`: Boolean logic
> - `(parentheses)`: Grouping logic

### Grouping and Sorting

> [!example]
> **Organization Strategies:**
> 
> ````markdown
> ```tasks
> not done
> group by folder
> sort by priority
> sort by due
> ```
> ````
> 
> **Grouping Options:**
> - `group by folder`: Organize by file location
> - `group by heading`: Organize by section header
> - `group by priority`: Organize by priority level
> - `group by due`: Organize by due date
> - `group by status`: Organize by completion status
> 
> **Sorting Options:**
> - `sort by priority`: Highest priority first
> - `sort by due`: Earliest due date first
> - `sort by path`: Alphabetical by file path
> - `sort by created`: Oldest tasks first
> - `sort by done`: Completed tasks handling

---

## 🗄️ Dataview Integration: Querying Tasks with DQL

### Understanding Dataview's Task Query Type

The TASK Query outputs an interactive list of all tasks in your vault that match the given data commands, and TASK queries are special because they operate on Task level rather than page level.

> [!core-principle]
> **Key Difference from Tasks Plugin Queries:**
> - **Tasks Plugin**: Task-centric, designed specifically for task management with rich date/priority syntax
> - **Dataview TASK**: Data-centric, leverages vault-wide metadata for dynamic aggregation
> - **Best Practice**: Use Tasks plugin for project-specific views, Dataview for cross-cutting dashboards

### Basic Dataview TASK Queries

````markdown
```dataview
TASK
WHERE !completed
```
````

> [!example]
> **Fundamental Patterns:**
> 
> **1. Incomplete Tasks with Tag Filter:**
> ````markdown
> ```dataview
> TASK
> WHERE !completed AND contains(tags, "#important")
> ```
> ````
> 
> **2. Tasks from Specific Folder:**
> ````markdown
> ```dataview
> TASK
> FROM "Projects/Active"
> WHERE !completed
> ```
> ````
> 
> **3. Tasks Completed Today:**
> ````markdown
> ```dataview
> TASK
> WHERE completed AND completion = date(today)
> ```
> ````

### Filtering by Task Metadata

> [!methodology-and-sources]
> **Accessing Task Properties in Dataview:**
> 
> Tasks in Dataview expose these implicit fields:
> - `completed`: Boolean (true/false)
> - `fullyCompleted`: Boolean (all subtasks also complete)
> - `text`: Task text content
> - `line`: Line number in file
> - `path`: File path
> - `status`: Task status character
> - `completion`: Completion date (if completed)
> - `tags`: Array of tags in the task line

````markdown
```dataview
TASK
WHERE !completed 
  AND contains(text, "review")
  AND file.folder = "Projects"
SORT file.name ASC
```
````

### Combining with Inline Fields

> [!example]
> **Enriching Tasks with Inline Metadata:**
> 
> **In your notes:**
> ```markdown
> - [ ] Finalize Q4 budget [priority:: high] [owner:: John] #finance
> - [ ] Review marketing deck [priority:: medium] [owner:: Sarah] #marketing
> ```
> 
> **Query them:**
> ````markdown
> ```dataview
> TASK
> WHERE !completed 
>   AND priority = "high"
> GROUP BY owner
> ```
> ````

---

## 🎨 Practical Dashboard Patterns

### Pattern 1: Project Task Dashboard

> [!example]
> **Comprehensive Project View:**
> 
> ````markdown
> ## 🎯 Active Tasks by Priority
> 
> ```tasks
> not done
> path includes {{PROJECT_FOLDER}}
> (priority is high) OR (due before in 3 days)
> group by priority
> sort by due
> ```
> 
> ## 📅 This Week's Schedule
> 
> ```dataview
> TASK
> FROM "{{PROJECT_FOLDER}}"
> WHERE !completed 
>   AND scheduled >= date(today) 
>   AND scheduled <= date(today) + dur(7 days)
> SORT scheduled ASC
> ```
> 
> ## ✅ Recently Completed
> 
> ```tasks
> done
> path includes {{PROJECT_FOLDER}}
> done after 1 week ago
> sort by done reverse
> limit 10
> ```
> ````

### Pattern 2: Daily Note Integration

Adding tasks to daily notes requires just a single line of code and provides automatic task aggregation.

> [!example]
> **Daily Note Task Section:**
> 
> ````markdown
> ---
> date: 2024-12-02
> ---
> 
> ## 📋 Today's Tasks
> 
> ```tasks
> not done
> (due today) OR (scheduled today)
> sort by priority
> ```
> 
> ## ⚠️ Overdue Items
> 
> ```tasks
> not done
> due before today
> sort by due
> ```
> 
> ## 🎯 This Week's Focus
> 
> ```dataview
> TASK
> WHERE !completed
>   AND (due >= date(today) AND due <= date(today) + dur(7 days))
> SORT due ASC
> ```
> ````

### Pattern 3: Context-Based Views

> [!example]
> **GTD-Style Context Filtering:**
> 
> ````markdown
> ## 💻 @computer Tasks
> 
> ```tasks
> not done
> description includes @computer
> sort by priority
> ```
> 
> ## 📞 @phone Tasks
> 
> ```tasks
> not done
> description includes @phone
> sort by due
> ```
> 
> ## 🏃 @errands
> 
> ```dataview
> TASK
> WHERE !completed
>   AND contains(text, "@errands")
> SORT file.name
> ```
> ````

### Pattern 4: Priority Matrix

> [!example]
> **Eisenhower Matrix Implementation:**
> 
> ````markdown
> ## 🔴 Urgent & Important
> 
> ```tasks
> not done
> priority is high
> due before in 3 days
> ```
> 
> ## 🟡 Important but Not Urgent
> 
> ```tasks
> not done
> priority is high
> due after in 3 days
> ```
> 
> ## 🟢 Urgent but Not Important
> 
> ```tasks
> not done
> priority is normal
> due before in 3 days
> ```
> 
> ## ⚪ Neither Urgent nor Important
> 
> ```tasks
> not done
> priority is low
> ```
> ````

---

## 🚀 Advanced Techniques

### Custom Metadata Fields

> [!methodology-and-sources]
> **Extending Task Metadata with Inline Fields:**
> 
> Tasks plugin respects Dataview inline fields, allowing custom enrichment:
> 
> ```markdown
> - [ ] Complete design mockups [client:: Acme Corp] [estimate:: 4h] [sprint:: 23] 📅 2024-12-20 ⏫
> ```
> 
> **Query with custom fields:**
> ````markdown
> ```dataview
> TABLE 
>   text AS "Task",
>   client,
>   estimate,
>   sprint
> FROM "Projects"
> WHERE !completed 
>   AND sprint = 23
> SORT estimate DESC
> ```
> ````

### DataviewJS for Complex Logic

> [!example]
> **Advanced Aggregation with JavaScript:**
> 
> ````markdown
> ```dataviewjs
> // Calculate total estimated hours for incomplete tasks
> const tasks = dv.pages()
>   .file.tasks
>   .where(t => !t.completed && t.estimate);
> 
> const totalHours = tasks
>   .map(t => {
>     const match = t.text.match(/\[estimate:: (\d+)h\]/);
>     return match ? parseInt(match[1]) : 0;
>   })
>   .reduce((sum, hours) => sum + hours, 0);
> 
> dv.header(3, `📊 Total Estimated Hours: ${totalHours}h`);
> dv.taskList(tasks);
> ```
> ````

> [!warning]
> **JavaScript Security Considerations:**
> JavaScript queries run at the same access level as any Obsidian plugin and can potentially rewrite, create, or delete files, as well as make network calls. Only use scripts you've written or that come from reputable sources.

### Templater Integration

> [!example]
> **Automated Task Creation with [[Templater Plugin]]:**
> 
> ```markdown
> ---
> project: <% tp.file.title %>
> created: <% tp.date.now("YYYY-MM-DD") %>
> ---
> 
> ## Project Tasks
> 
> ```tasks
> not done
> path includes <% tp.file.folder(true) %>
> group by heading
> ```
> 
> ## Quick Add Task
> 
> - [ ] <% tp.system.prompt("Task description") %> 📅 <% tp.date.now("YYYY-MM-DD") %> #task
> ```

### Query Presets for Reusability

Presets allow you to save commonly used task query instructions and reuse them across multiple queries, so instead of repeatedly typing the same complex filters you can define them once in settings and reference them by name.

> [!methodology-and-sources]
> **Setting Up Query Presets (Tasks Plugin v7.0+):**
> 
> 1. Navigate to `Settings → Tasks → Presets`
> 2. Create a preset with your common filters:
>    - Name: `high-priority-this-week`
>    - Content:
>      ```
>      not done
>      priority is high
>      due before in 7 days
>      sort by due
>      ```
> 3. Use in queries:
>    ````markdown
>    ```tasks
>    preset: high-priority-this-week
>    path includes Projects/Active
>    ```
>    ````

---

## ⚠️ Common Pitfalls and Solutions

> [!warning]
> **Frequent Issues and Fixes:**

### Issue 1: Dataview Can't Find Tasks Plugin Tasks

**Problem**: Dataview doesn't index note contents the same way Tasks plugin does, leading to missing tasks in queries.

**Solution**: 
- Ensure tasks have your global filter tag (e.g., `#task`)
- Verify Dataview is enabled and up to date
- Use `FROM` clause to explicitly target folders containing tasks
- Remember Dataview's `TASK` query type operates on all checkboxes, not just Tasks plugin tasks

### Issue 2: Date Comparisons Not Working

**Problem**: Date queries return unexpected results or errors.

**Solution**:
````markdown
# ❌ WRONG
WHERE due < "2024-12-15"

# ✅ CORRECT
WHERE due < date("2024-12-15")

# ✅ ALSO CORRECT (Dataview)
WHERE due < date(today)
````

### Issue 3: Tags in Tasks Not Matching

When accessing Obsidian from mobile devices, the initial letter of a tag often gets capitalized automatically.

**Solution**:
````markdown
```dataview
TASK
WHERE !completed 
  AND contains(upper(text), "#TODO")
SORT text ASC
```
````

### Issue 4: Performance Degradation

**Problem**: Queries become slow with large vaults (thousands of tasks).

> [!helpful-tip]
> **Optimization Strategies:**
> - Use `FROM` clause to limit search scope
> - Add `LIMIT` to cap results
> - Avoid complex regex in DataviewJS when simple filters suffice
> - Tasks searches now only run when visible, not on inactive tabs (v7.0+)
> - Consider archiving completed tasks to separate folders

---

## 🎓 Best Practices and Workflow Design

### Principle 1: Semantic Consistency

> [!core-principle]
> **Establish and document your task metadata conventions** early. Inconsistent use of tags, dates, and priority markers undermines query reliability.
> 
> **Example Convention:**
> - `#task` = Required on all tracked tasks
> - `#project/[name]` = Project categorization
> - `#context/[location]` = GTD-style context tags
> - `[sprint:: N]` = Agile sprint number
> - `[estimate:: Xh]` = Time estimation

### Principle 2: Progressive Disclosure

> [!the-philosophy]
> **Start with simple queries and add complexity as needs emerge.** A task system should reduce cognitive load, not increase it. Begin with basic "due today" and "high priority" views, then layer in sophistication as your workflow stabilizes.

### Principle 3: Context Over Collection

Visiting the library becomes a new note with a task section, creating a visit log; the same applies to doctor's appointments, restaurants, car maintenance.

> [!insight]
> **Embed tasks within relevant notes** rather than maintaining separate task repositories. This preserves context and makes your vault more useful as a [[03-notes/01_permanent-notes/02_personal-knowledge-base/Personal Knowledge Management]] system. A task about "Review Q3 financials" belongs in your Q3 project note, not just a master task list.

### Principle 4: Regular Maintenance

> [!helpful-tip]
> **Schedule Weekly Reviews:**
> - Archive or delete completed tasks
> - Update due dates and priorities
> - Verify recurring tasks are functioning correctly
> - Refactor queries that have become cluttered
> - This maintains system hygiene and prevents query bloat

---

## 🔗 Integration with Other Plugins

### QuickAdd for Rapid Task Capture

> [!example]
> **QuickAdd Macro for Task Creation:**
> 
> Create a QuickAdd choice that:
> 1. Prompts for task description
> 2. Prompts for due date
> 3. Prompts for priority
> 4. Prompts for project tag
> 5. Inserts formatted task at cursor or to designated inbox note
> 
> This reduces friction in task capture, ensuring more tasks get recorded.

### Day Planner for Time Blocking

The [[Day Planner]] plugin can integrate with Tasks plugin for visual time management:

> [!example]
> **Time-Blocked Task Schedule:**
> 
> ```markdown
> ## 📅 Today's Schedule
> 
> - 09:00 - [ ] Morning standup #task ⏳ 2024-12-02
> - 10:00 - [ ] Code review session #task ⏳ 2024-12-02
> - 14:00 - [ ] Client presentation #task ⏳ 2024-12-02 ⏫
> ```

### Calendar for Visual Timeline

Dataview's `CALENDAR` query type combined with Tasks plugin metadata:

````markdown
```dataview
CALENDAR file.tasks.due
FROM "Projects"
WHERE file.tasks
```
````

This creates a visual calendar view where dots represent tasks due on specific dates.

---

## 🧭 Further Exploration

### 1. **[[Tasks Plugin Query Language]]**
   - *Connection*: Deep dive into Tasks plugin's full query syntax, including regex filters, boolean expressions, and custom sorting
   - *Depth Potential*: Tasks plugin has extensive query capabilities beyond basic filtering that enable sophisticated task views
   - *Knowledge Graph Role*: Serves as specialized technical reference for advanced query construction

### 2. **[[Dataview Query Optimization Strategies]]**
   - *Connection*: Performance tuning for large vaults with thousands of tasks and notes
   - *Depth Potential*: Indexing mechanics, query execution order, caching strategies, and computational complexity considerations
   - *Knowledge Graph Role*: Critical for scaling task management systems in professional contexts

### 3. **[[GTD (Getting Things Done) Implementation in Obsidian]]**
   - *Connection*: Applying David Allen's GTD methodology using Tasks plugin and Dataview for context-based productivity
   - *Depth Potential*: Comprehensive workflow design including capture, clarification, organization, reflection, and engagement phases
   - *Knowledge Graph Role*: Bridges productivity methodology with technical implementation

### 4. **[[Metadata-Driven Workflows in PKM]]**
   - *Connection*: Broader architectural patterns for using metadata (YAML frontmatter, inline fields) to create reactive, queryable knowledge systems
   - *Depth Potential*: Extends beyond task management to holistic vault design using metadata as infrastructure
   - *Knowledge Graph Role*: Foundational architectural principle for advanced [[Obsidian]] usage

---

**Last Updated**: 2024-12-02  
**Status**: 🌲 Evergreen Reference  
**Version**: 1.0

