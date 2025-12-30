---
title: "Dataview: Inline Queries Cheat Sheet"
id: "20251129194513"
type: "reference"
source: "pur3v4d3r/claude/gemini"
aliases:
  - "Dataview Inline Queries"
  - "Inline Quries"
  - "Dataview"
  - "Dataview Inline Reference"
  - "DQL Inline Taxonomy"
  - "Inline Query Library"
  - "Embedded Dataview Patterns"
  - "Dataview Cheat Sheet"
  - "Cheat Sheet"
tags:
  - obsidian
  - obsidian/plugins/dataview
  - obsidian/advanced/automation
  - reference-note
  - pkm
  - pkb/architecture
  - pkb/design/information-architecture
  - pkb/metadata
  - pkb/metadata/frontmatter
  - pkb/optimization
  - information-architecture
---
# Comprehensive Dataview Inline Query Cheat Sheet

> [!abstract] Reference Overview
> **Purpose:** Production-ready library of Dataview inline query patterns organized by use case category for rapid implementation in daily [[Personal Knowledge Management]] workflows.
> 
> **Scope:** Covers all major inline query syntaxes including simple field access, cross-note references, vault-wide aggregations, date calculations, conditional logic, and DataviewJS hybrid patterns.
> 
> **Usage Model:** Copy-paste templates with placeholder syntax for immediate deployment in [[Templater]] templates, [[MOC]] hubs, or individual notes.


## 🎯 Core Concept & Syntax Foundation

> [!definition] 
> **Dataview Inline Queries** are single-value expressions embedded directly in prose using the `` `= expression` `` syntax. Unlike block queries that render separate sections, inline queries integrate seamlessly within text to display dynamic, auto-updating metadata.

### Syntax Pattern Recognition

| Pattern Type          | Syntax                                    | Use Case              | Example                                              |
| --------------------- | ----------------------------------------- | --------------------- | ---------------------------------------------------- |
| **Direct Field**      | `` `= this.field` ``                      | Current note metadata | `` `= this.status` ``                                |
| **Link Reference**    | `` `= [[Note]].field` ``                  | Other note metadata   | `` `= [[Project]].budget` ``                         |
| **Vault Aggregation** | `` `= length(pages("#tag"))` ``           | Count matching pages  | `` `= length(pages("#task"))` ``                     |
| **Filtered Sum**      | `` `= sum(map(pages(), p => p.value))` `` | Aggregate values      | `` `= sum(map(pages("#expense"), e => e.amount))` `` |
| **Date Calculation**  | `` `= (date2 - date1).days` ``            | Time differences      | `` `= (this.due - date(today)).days` ``              |
| **Conditional Logic** | `` `= choice(condition, true, false)` ``  | If/else rendering     | `` `= choice(this.done, "✅", "⏳")` ``                |

---


## 📁 Category I: Metadata Display & Status Tracking

### 1.1 Current Note Metadata Display

> [!example] **Living Header Pattern**
> Surfaces critical note metadata without manual updates

```markdown
> [!info] Note Metadata
> **Status**:: `= this.status` | **Priority**:: `= this.priority`
> **Author**:: `= this.author` | **Last Review**:: `= this.reviewed`
> **Created**:: `= this.file.ctime` | **Modified**:: `= this.file.mtime`
```

**Variation: Inline Prose Integration**

```markdown
This project is currently **`= this.status`** with a `= this.priority` priority level. 
Last reviewed on `= this.reviewed` by `= this.author`.
```

### 1.2 File System Metadata

> [!example] **Automatic File Information**

```markdown
**File Details**
- Name: `= this.file.name`
- Location: `= this.file.folder`
- Size: `= round(this.file.size / 1024, 2)` KB
- Tags: `= join(this.file.tags, ", ")`
- Aliases: `= join(this.file.aliases, " | ")`
```

### 1.3 Link Analytics

> [!example] **Bi-Directional Link Counters**

```markdown
**Link Context**
- Incoming Links: `= length(this.file.inlinks)` backlinks
- Outgoing Links: `= length(this.file.outlinks)` references
- Total Connection Strength: `= length(this.file.inlinks) + length(this.file.outlinks)` links
```

### 1.4 Conditional Status Indicators

> [!example] **Dynamic Status Badges**

```markdown
**Project Health**: `= choice(this.status = "complete", "✅ Complete", choice(this.status = "active", "🔥 Active", choice(this.status = "paused", "⏸️ Paused", "❌ Blocked")))`

**Priority Flag**: `= choice(this.priority = "high", "🔴 HIGH", choice(this.priority = "medium", "🟡 MEDIUM", "🟢 LOW"))`

**Deadline Status**: `= choice(this.deadline < date(today), "⚠️ OVERDUE", choice(this.deadline = date(today), "📌 DUE TODAY", "✅ On Track"))`
```

---

## 🔢 Category II: Dynamic Counters & Aggregations

### 2.1 Vault-Wide Counts

> [!example] **Global Statistics**

```markdown
**Vault Statistics**
- Total Notes: `= length(pages())`
- Notes with Tag #project: `= length(pages("#project"))`
- Notes in Current Folder: `= length(pages('"' + this.file.folder + '"'))`
- Incomplete Tasks: `= length(filter(pages().file.tasks, t => !t.completed))`
- Notes Modified Today: `= length(filter(pages(), p => p.file.mday = date(today)))`
```

### 2.2 Filtered Aggregations

> [!example] **Conditional Counting**

```markdown
**Project Metrics**
- Active Projects: `= length(filter(pages("#project"), p => p.status = "active"))`
- High Priority Items: `= length(filter(pages("#task"), t => t.priority = "high"))`
- Overdue Tasks: `= length(filter(pages("#task"), t => t.due < date(today) and !t.completed))`
- This Week's Notes: `= length(filter(pages(), p => p.file.cday >= date(today) - dur(7 days)))`
```

### 2.3 Numeric Aggregations

> [!example] **Sum, Average, Min, Max**

```markdown
**Financial Overview**
- Total Budget: $`= sum(map(pages("#project"), p => p.budget))`
- Total Spent: $`= sum(map(pages("#expense"), e => e.amount))`
- Budget Remaining: $`= sum(map(pages("#project"), p => p.budget)) - sum(map(pages("#expense"), e => e.amount))`

**Performance Metrics**
- Average Rating: `= round(sum(map(pages("#review"), r => r.rating)) / length(pages("#review")), 2)` / 10
- Highest Score: `= max(map(pages("#review"), r => r.rating))`
- Lowest Score: `= min(map(pages("#review"), r => r.rating))`
```

### 2.4 List Aggregations

> [!example] **Collecting Multi-Value Fields**

```markdown
**Team Distribution**
- All Team Members: `= join(flat(map(pages("#project"), p => p.team)), ", ")`
- All Tags Used: `= join(flat(map(pages(), p => p.file.tags)), ", ")`
- All Locations Mentioned: `= join(flat(map(pages("#meeting"), m => m.location)), " | ")`
```

---

## 📅 Category III: Date & Time Calculations

### 3.1 Time Differences

> [!example] **Duration Calculations**

```markdown
**Temporal Context**
- Days Since Created: `= (date(today) - this.file.cday).days` days
- Days Until Deadline: `= (this.deadline - date(today)).days` days
- Project Duration: `= (this.end-date - this.start-date).days` days
- Weeks Active: `= round((date(today) - this.start-date).days / 7, 1)` weeks
- Days Since Last Edit: `= (date(today) - this.file.mday).days` days
```

### 3.2 Age & Staleness Indicators

> [!example] **Bio-Rhythm Module (from exemplar)**

```markdown
> [!calendar] 🕰️ Temporal Context
> **Created**:: `= this.file.ctime` | **Age**:: `= (date(today) - this.file.cday).days` days
> **Last Touch**:: `= this.file.mtime` | **Staleness**:: `= choice((date(today) - this.file.mday).days > 180, "🕸️ Cobwebs", choice((date(today) - this.file.mday).days > 30, "🍂 Cold", "🔥 Fresh"))`
```

### 3.3 Date Component Extraction

> [!example] **Parsing Date Fields**

```markdown
**Date Analysis**
- Creation Year: `= this.file.ctime.year`
- Creation Month: `= this.file.ctime.month`
- Creation Day: `= this.file.ctime.day`
- Day of Week Created: `= this.file.ctime.weekday`
- Is Weekend Creation: `= choice(this.file.ctime.weekday > 5, "Yes", "No")`
```

### 3.4 Deadline & Review Scheduling

> [!example] **Automatic Review Calculations**

```markdown
**Review Schedule**
- Next Review Due: `= this.last-review + dur(30 days)`
- Days Until Review: `= ((this.last-review + dur(30 days)) - date(today)).days`
- Review Status: `= choice(date(today) > this.last-review + dur(30 days), "⚠️ OVERDUE", choice(date(today) = this.last-review + dur(30 days), "📌 DUE TODAY", "✅ Current"))`
```

---

## 🔗 Category IV: Cross-Note References

### 4.1 Pulling Metadata from Linked Notes

> [!example] **Relational Data Retrieval**

```markdown
**Project Context**
- Project Manager: `= [[Project Alpha]].manager`
- Project Status: `= [[Project Alpha]].status`
- Project Budget: $`= [[Project Alpha]].budget`
- Team Size: `= length([[Project Alpha]].team-members)`
- Completion: `= [[Project Alpha]].completion`%
```

### 4.2 Calculated Cross-Note Values

> [!example] **Computed Relational Metrics**

```markdown
**Derived Metrics**
- Budget Remaining: $`= [[Project Alpha]].budget - [[Project Alpha]].spent`
- Budget Utilization: `= round(([[Project Alpha]].spent / [[Project Alpha]].budget) * 100, 1)`%
- Days Since Project Start: `= (date(today) - [[Project Alpha]].start-date).days`
- Estimated Days Remaining: `= ([[Project Alpha]].deadline - date(today)).days`
```

### 4.3 Multi-Note Aggregation

> [!example] **Collecting from Multiple Sources**

```markdown
**Sprint Summary**
- Total Story Points: `= [[Sprint 1]].points + [[Sprint 2]].points + [[Sprint 3]].points`
- Combined Team Size: `= length([[Sprint 1]].team) + length([[Sprint 2]].team) + length([[Sprint 3]].team)`
- Overall Completion: `= round((([[Sprint 1]].completed + [[Sprint 2]].completed + [[Sprint 3]].completed) / ([[Sprint 1]].points + [[Sprint 2]].points + [[Sprint 3]].points)) * 100, 1)`%
```

---

## ✅ Category V: Task & Progress Tracking

### 5.1 Task Completion Metrics

> [!example] **Progress Indicators**

```markdown
**Task Status**
- Completed Tasks: `= length(filter(this.file.tasks, t => t.completed))` / `= length(this.file.tasks)`
- Completion Rate: `= round((length(filter(this.file.tasks, t => t.completed)) / length(this.file.tasks)) * 100, 1)`%
- Remaining Tasks: `= length(filter(this.file.tasks, t => !t.completed))`
```

### 5.2 Task Filtering by Properties

> [!example] **Conditional Task Counts**

```markdown
**Task Breakdown**
- High Priority Tasks: `= length(filter(this.file.tasks, t => contains(string(t), "priority:: high")))`
- Overdue Tasks: `= length(filter(this.file.tasks, t => contains(string(t), "due::") and !t.completed))`
- Tasks Due Today: `= length(filter(this.file.tasks, t => contains(string(t), string(date(today)))))`
```

### 5.3 Project-Wide Task Aggregation

> [!example] **Vault-Level Task Analytics**

```markdown
**Global Task Metrics**
- All Open Tasks: `= length(filter(pages().file.tasks, t => !t.completed))`
- Project Tasks Remaining: `= length(filter(pages("#project").file.tasks, t => !t.completed))`
- Total Completed: `= length(filter(pages().file.tasks, t => t.completed))`
- Overall Completion: `= round((length(filter(pages().file.tasks, t => t.completed)) / length(pages().file.tasks)) * 100, 1)`%
```

---

## 🌐 Category VI: Folder & Hierarchy Context

### 6.1 Sibling Awareness Module (from exemplar)

> [!example] **Folder Context**

```markdown
> [!folder] 📂 Folder Context
> **Location**:: `= this.file.folder`
> **Neighbors**:: `= length(pages('"' + this.file.folder + '"')) - 1` other notes here
```

### 6.2 Hierarchical Navigation

> [!example] **Parent/Child Relationships**

```markdown
**Folder Structure**
- Current Folder: `= this.file.folder`
- Notes in Folder: `= length(pages('"' + this.file.folder + '"'))`
- Subfolders: `= length(filter(pages(), p => startswith(p.file.folder, this.file.folder + "/")))`
- Parent Folder: `= split(this.file.folder, "/")[length(split(this.file.folder, "/")) - 2]`
```

### 6.3 Folder-Scoped Queries

> [!example] **Localized Aggregations**

```markdown
**Local Statistics**
- Tags in This Folder: `= join(flat(map(pages('"' + this.file.folder + '"'), p => p.file.tags)), ", ")`
- Average File Size: `= round(sum(map(pages('"' + this.file.folder + '"'), p => p.file.size)) / length(pages('"' + this.file.folder + '"')) / 1024, 2)` KB
- Newest Note: `= max(map(pages('"' + this.file.folder + '"'), p => p.file.ctime))`
```

---

## 🎨 Category VII: Advanced Patterns & Hybrid Techniques

### 7.1 Multi-Level Conditional Logic

> [!example] **Nested Conditionals**

```markdown
**Status Classification**: `= choice(this.status = "complete", "✅ Complete", choice(this.status = "in-progress", choice(this.priority = "high", "🔥 Active (High)", "⚡ Active (Normal)"), choice(this.status = "paused", "⏸️ Paused", choice(this.status = "blocked", "🚫 Blocked", "📝 Planning"))))`

**Health Score**: `= choice(this.completion > 80, "🟢 Excellent", choice(this.completion > 60, "🟡 Good", choice(this.completion > 40, "🟠 Concerning", "🔴 Critical")))`
```

### 7.2 String Manipulation

> [!example] **Text Operations**

```markdown
**Text Processing**
- Uppercase Title: `= upper(this.title)`
- First Word: `= split(this.title, " ")[0]`
- Word Count: `= length(split(this.content, " "))`
- Initials: `= join(map(split(this.author, " "), w => string(w)[0]), "")`
```

### 7.3 Regex Pattern Matching

> [!example] **Pattern Extraction**

```markdown
**Pattern Detection**
- Contains Email: `= choice(regexmatch("[\w.-]+@[\w.-]+\.\w+", this.contact), "Yes", "No")`
- Has Phone Number: `= choice(regexmatch("\d{3}-\d{3}-\d{4}", string(this)), "Yes", "No")`
- URL Present: `= choice(regexmatch("https?://[^\s]+", string(this)), "Found", "None")`
```

### 7.4 DataviewJS Hybrid Pattern

> [!example] **Switching to JavaScript for Complex Logic**

````markdown
**Complex Calculation (DataviewJS)**

```dataviewjs
const incomplete = dv.pages("#task")
  .where(t => !t.completed && t.priority === "high")
  .length;

const overdue = dv.pages("#task")
  .where(t => !t.completed && t.due < dv.date("today"))
  .length;

dv.span(`**Critical Tasks:** ${incomplete} high-priority | ${overdue} overdue`);
```
````

**When to use DataviewJS:**
- Complex string manipulation
- Custom formatting requirements
- External data integration
- Advanced array operations
- Rendering custom HTML/CSS

---

## 📊 Category VIII: Visual Analytics Integration

### 8.1 Progress Bars (Semantic Display)

> [!example] **Text-Based Progress Indicators**

```markdown
**Project Progress**
`= this.completion`% `= choice(this.completion >= 100, "▓▓▓▓▓▓▓▓▓▓", choice(this.completion >= 90, "▓▓▓▓▓▓▓▓▓░", choice(this.completion >= 80, "▓▓▓▓▓▓▓▓░░", choice(this.completion >= 70, "▓▓▓▓▓▓▓░░░", choice(this.completion >= 60, "▓▓▓▓▓▓░░░░", choice(this.completion >= 50, "▓▓▓▓▓░░░░░", choice(this.completion >= 40, "▓▓▓▓░░░░░░", choice(this.completion >= 30, "▓▓▓░░░░░░░", choice(this.completion >= 20, "▓▓░░░░░░░░", choice(this.completion >= 10, "▓░░░░░░░░░", "░░░░░░░░░░"))))))))))`
```

### 8.2 Emoji-Based Status Arrays

> [!example] **Visual Health Dashboard**

```markdown
**System Health Checks**
- Database: `= choice(this.db-status = "healthy", "✅", "❌")`
- API: `= choice(this.api-status = "healthy", "✅", "❌")`
- Cache: `= choice(this.cache-status = "healthy", "✅", "❌")`
- Overall: `= choice(this.db-status = "healthy" and this.api-status = "healthy" and this.cache-status = "healthy", "🟢 All Systems Operational", "🔴 Issues Detected")`
```

---

## ⚙️ Category IX: Template Integration Patterns

### 9.1 Templater + Dataview Combination

> [!example] **Dynamic Template Generation**

``````markdown
```
---
created: <% tp.date.now("YYYY-MM-DD") %>
type: project-note
status: planning
---

# <% tp.file.title %>

**Project Metrics**
- Created: `= this.created`
- Age: `= (date(today) - this.created).days` days
- Status: `= this.status`
- Notes in Project: `= length(pages('"' + this.file.folder + '"'))`
```
``````

### 9.2 Self-Updating Headers

> [!example] **Living Document Metadata**

```markdown
---
last-updated: <% tp.date.now("YYYY-MM-DD") %>
review-count: <% tp.frontmatter.review-count ? tp.frontmatter.review-count + 1 : 1 %>
---

> [!info] Document Status
> Last Updated: `= this.last-updated` | Times Reviewed: `= this.review-count`
> Days Since Review: `= (date(today) - this.last-updated).days`
> Review Status: `= choice((date(today) - this.last-updated).days > 30, "⚠️ Needs Review", "✅ Current")`
```

---

## 🔧 Category X: Performance Optimization Patterns

### 10.1 Scoped Queries (Recommended)

> [!helpful-tip] **Performance Best Practices**

```markdown
❌ **SLOW** (queries entire vault):
`= length(pages())`
`= sum(map(pages(), p => p.value))`

✅ **FAST** (scoped to folder/tag):
`= length(pages('"10 Projects"'))`
`= sum(map(pages("#active-project"), p => p.value))`
```

### 10.2 Cached Calculations

> [!example] **Frontmatter Caching Strategy**

```markdown
---
# Calculate once, reference multiple times
total-budget: 50000
total-spent: 32500
# Derived value cached in frontmatter (updated by DataviewJS automation)
budget-remaining: 17500
utilization-rate: 65
---

**Financial Summary**
- Budget: $`= this.total-budget`
- Spent: $`= this.total-spent`
- Remaining: $`= this.budget-remaining` (cached)
- Utilization: `= this.utilization-rate`% (cached)
```

---

## 🚨 Category XI: Error Handling & Validation

### 11.1 Null/Undefined Checks

> [!example] **Defensive Queries**

```markdown
**Safe Field Access**
- Priority: `= choice(this.priority, this.priority, "Not Set")`
- Due Date: `= choice(this.due, this.due, "No Deadline")`
- Budget: `= choice(this.budget, "$" + this.budget, "TBD")`
```

### 11.2 Type Validation

> [!example] **Data Type Checking**

```markdown
**Type-Safe Calculations**
- Is Valid Date: `= choice(typeof(this.deadline) = "date", "✅", "❌ Invalid")`
- Is Number: `= choice(typeof(this.budget) = "number", "✅", "❌ Not Numeric")`
- Has Value: `= choice(this.status, "✅ Set", "⚠️ Missing")`
```

### 11.3 Fallback Values

> [!example] **Default Value Pattern**

```markdown
**With Fallbacks**
- Status: `= default(this.status, "unknown")`
- Priority: `= default(this.priority, "medium")`
- Owner: `= default(this.owner, "Unassigned")`
- Completion: `= default(this.completion, 0)`%
```

---

## 🎓 Category XII: Educational & Learning Patterns

### 12.1 Spaced Repetition Tracking

> [!example] **Review Scheduling**

```markdown
**Learning Progress**
- Times Reviewed: `= this.review-count`
- Last Review: `= this.last-review`
- Next Review: `= this.last-review + dur(this.interval days)`
- Days Until Next: `= ((this.last-review + dur(this.interval days)) - date(today)).days`
- Current Interval: `= this.interval` days
```

### 12.2 Knowledge Maturity Indicators

> [!example] **Zettelkasten Maturity**

```markdown
**Note Maturity**
- Incoming References: `= length(this.file.inlinks)`
- Outgoing References: `= length(this.file.outlinks)`
- Link Density: `= length(this.file.inlinks) + length(this.file.outlinks)` total
- Maturity Level: `= choice(length(this.file.inlinks) > 5, "🌳 Evergreen", choice(length(this.file.inlinks) > 2, "🌱 Growing", "🌾 Seedling"))`
```


























## *title*: In-Note Metadata *ver*: 1.0.0 *id*: 20251129214101
````
## 📊 Note Metadata Dashboard
> [!fail] 🛠️ Metadata Health Check
> **Missing Fields**:: `$= const fields = ["status", "type", "tags"]; const missing = fields.filter(f => !dv.current()[f]); missing.length > 0 ? "⚠️ Missing: " + missing.join(", ") : "✅ All Systems Go"`

> [!metadata]
> **Note-Type**: `= this.type`
> **Information-Source**: `=this.source`
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
````

## *title*: In-Note Metadata *ver*: 2.0.0 *id*: 20251129213805
````
<% title %>

> [!overview]
> - **Title**:: [[<% title %>]]
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
WHERE  type = "<% type %>"
SORT "maturity" DESC
LIMIT 15
```
### Sources & References
```dataview
TABLE 
    source AS "Source Type",
    created AS "Date Added"
FROM [[]]
WHERE "<% source %>"
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
### <% dateNow %> - Initial Creation
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
#### Review Checklist:
- [ ] Definition still accurate?
- [ ] New connections identified?
- [ ] Applications validated?
- [ ] Sources still relevant?
- [ ] Maturity level appropriate?

---

*{{PASTE REPORT HERE}}*
````

### The Template Component

Create a new file in your templates folder named `Component - Neuro-Link Header.md`. Paste the code block below into it exactly as it appears.

> [!danger] **Crucial Syntax Note**
> Do not remove the backticks inside the query expressions. The syntax `` `= … ` `` tells Dataview to render the value locally. The syntax `key::` tells Dataview to save that value as metadata for the page.

```markdown
> [!network] 🔗 Network Connectivity
> **In-Links**:: `= length(this.file.inlinks)` | **Out-Links**:: `= length(this.file.outlinks)`
> **Network Status**:: `= choice(length(this.file.inlinks) = 0, "🕸️ Orphan", choice(length(this.file.inlinks) > 5, "⚡ Hub", "🌱 Node"))`
```

#### ⚙️ How It Works (The Logic)

1.  **`In-Links::`**: Defines a new metadata field named "In-Links".
2.  **`= length(this.file.inlinks)`**: A dynamic DQL query that counts incoming links *live*.
3.  **`Network Status::`**: A calculated field that auto-classifies the note:
      * **Orphan**: 0 incoming links. (Needs integration).
      * **Hub**: More than 5 incoming links. (High value).
      * **Node**: 1-5 incoming links. (Standard).


-----


### Implementation Strategy

You have two ways to deploy this system depending on your workflow.

#### Option A: The "New Note" Automation (Recommended)

Integrate this component into your primary **Permanent Note** or **Project** templates so every new note is born with this header.

**Action**: Open your existing templates and insert the following Templater code immediately after the `---` YAML block:

```javascript
<% tp.file.include("Component - Neuro-Link Header") %>
```

*(Replace `"Component - Neuro-Link Header"` with the exact path to the file you created in Step 1 if it's in a subfolder, e.g., `Templates/Components/Component…`)*

#### Option B: The Retroactive Injection (For Old Notes)

Use **QuickAdd** to instantly stamp this header into your existing notes without messing up their content.

1.  Open **QuickAdd Settings** \> **Macros**.
2.  Create a new Macro named `Inject Connectivity Header`.
3.  Add a **Templater** step.
4.  Select the `Component - Neuro-Link Header.md` file.
5.  **Go to "Capture" Choices**:
      * Create a new Capture named "Add Header".
      * Enable **Capture to Active File**.
      * In the format box, enter: `{{MACRO:Inject Connectivity Header}}`.
      * Set "Insert After" to `---` (or simply place it at the top of the content).


-----

### Querying Your New Data

Because we used the `Key::` syntax, you can now query this "fake frontmatter" exactly like real YAML.

**Example Dashboard Query**: Find all "Orphan" notes that need connection.

```
TABLE file.folder, file.mtime as "Last Edited"
FROM "03 Notes"
WHERE Network-Status = "🕸️ Orphan"
SORT file.mtime DESC
```

> [!check] **System Synergy Achieved**
>
>   * **Dataview**: Handles the live counting and querying.
>   * **Templater**: Standardizes the injection of the component.
>   * **User Goal**: Achieved "YAML-like" data visibility without the maintenance burden of static YAML scripts.


#### 1. The "Project Pulse" Module (Task Intelligence)

**Best For:** Project Notes, Weekly Reviews, Todo Lists.
This module scans the *current note* for checkboxes and calculates real-time completion percentages. It instantly tells you if a project is stalled or nearing the finish line.

**The Code:**

```markdown
> [!todo] 🏗️ Project Status
> **Tasks Open**:: `= length(filter(this.file.tasks, (t) => !t.completed))` | **Tasks Done**:: `= length(filter(this.file.tasks, (t) => t.completed))`
> **Progress**:: `= round((length(filter(this.file.tasks, (t) => t.completed)) / max(list(1, length(this.file.tasks)))) * 100) + "%"`
```

**What it does:**

  * **Tasks Open/Done**: Live counters of your checkboxes.
  * **Progress**: Calculates a percentage (e.g., "67%").
  * *Note: The `max(list(1, …))` trick prevents "Division by Zero" errors on empty notes.*


-----


#### 2. The "Bio-Rhythm" Module (Temporal Health)

**Best For:** Permanent Notes, Zettelkasten, Gardening.
Notes decay over time. This module calculates "Staleness" relative to today, helping you identify notes that haven't been touched in months (Archives) vs. active thoughts.

**The Code:**

```markdown
> [!calendar] 🕰️ Temporal Context
> **Created**:: `= this.file.ctime` | **Age**:: `= (date(today) - this.file.ctime).days + " days"`
> **Last Touch**:: `= this.file.mtime` | **Staleness**:: `= choice((date(today) - this.file.mtime).days > 180, "🕸️ Cobwebs", choice((date(today) - this.file.mtime).days > 30, "🍂 Cold", "🔥 Fresh"))`
```

**What it does:**

  * **Age**: How long has this idea existed?
  * **Staleness**: Auto-classifies the note as "Fresh", "Cold", or "Cobwebs" based on the last edit date. Excellent for "Gardening" queries (e.g., "Show me all 'Cold' notes").


-----


### The "Content Auditor" Module (Quality Metrics)

**Best For:** Writing drafts, Essays, Long-form content.
This uses file metadata to estimate the depth and consumption time of a note. It helps you distinguish between "Stubs" (empty placeholders) and "Deep Dives."

**The Code:**

```markdown
> [!quote] 📝 Content Metrics
> **Word Count**:: `= this.file.size` B | **Est. Read Time**:: `= round(this.file.size / 1300) + " min"`
> **Depth Class**:: `= choice(this.file.size < 500, "🌱 Stub", choice(this.file.size < 2000, "📄 Note", "📜 Essay"))`
```

**What it does:**

  * **Est. Read Time**: Approximates reading time based on file size (bytes).
  * **Depth Class**: Auto-tags the note as a "Stub", "Note", or "Essay" without you having to manually update a status field.

-----


### The "Sibling Awareness" Module (Contextual Navigation)

**Best For:** MOCs, Johnny.Decimal folders, Structure notes.
This allows a note to know "Where am I?" and "Who else is here?". It counts other notes in the exact same folder.

**The Code:**

```markdown
> [!folder] 📂 Folder Context
> > **Location**:: `= this.file.folder`
> > **Neighbors**:: `$= dv.pages('"' + dv.current().file.folder + '"').length - 1` other notes here.
```

**What it does:**

  * **Neighbors**: Counts how many *other* files exist in the same folder (subtracting 1 to exclude itself). Useful for spotting over-stuffed folders that need refactoring.


-----

### Implementation Recommendation: The "Master Header"

You probably don't want *all* of these on *every* note. I recommend creating **two distinct header templates**:

1.  **`Component - Header (Project)`**:
      * Combines **Neuro-Link** (Links) + **Project Pulse** (Tasks).
      * *Why*: Projects are about *doing* and *connecting*.
2.  **`Component - Header (Idea)`**:
      * Combines **Neuro-Link** (Links) + **Bio-Rhythm** (Time) + **Content Auditor** (Depth).
      * *Why*: Ideas are about *growing*, *aging*, and *refining*.

**Pro Tip:** Since these use `Key:: Value` syntax, you can now run global queries like:

  * *"Show me all Projects that are \< 50% complete but have \> 10 outgoing links."*
  * *"Show me all 'Stub' notes that are 'Cobwebs' (old and empty) -\> Candidates for deletion."*
----


1. The "Semantic Bridge" (Discovery Engine)

**The Problem:** You know what you have explicitly linked. You *don't* know what is implicitly related.
**The Solution:** A DataviewJS algorithm that finds **"Sibling Notes"**—notes that link to the same things this note links to, but aren't directly connected to each other.
**The "Architect" Value:** This automates serendipity. It tells you, *"Hey, this note and that note both talk about 'Cognitive Science' and 'Habits', but they don't link to each other yet. You should fix that."*

### The Component

Create a template file named `Component - Semantic Bridge.md` and paste this **DataviewJS** block.

````javascript
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

> [!tip] **Usage**
> Place this at the **bottom** of your "Permanent Note" template. It serves as a dynamic "Recommended Reading" footer that updates as you add links to other notes.
``````

-----


2. The "Vault Pulse" (Visual Analytics)

**The Problem:** Dataview tables are great for data, but terrible for trends.
**The Solution:** Since you have the **Charts** plugin, we can pipe DataviewJS data directly into a visual graph to see your "Creation Velocity" over time.
**The "Architect" Value:** Visual feedback loop. Seeing a "flatline" in your creation graph motivates you to write.

### The Component

Create a new note called `Dashboard - Vault Pulse` and paste this code.

````javascript
```dataviewjs
/** * 📊 SYSTEM: Vault Pulse Visualizer
 * REQUIRES: 'Charts' Plugin
 */

// 1. Gather Data (Last 30 Days)
const pages = dv.pages('"03 Notes"'); // ⚠️ UPDATE folder path to your main notes folder
const today = moment();
const daysBack = 30;
let labels = [];
let data = [];

// 2. Build the Dataset
for (let i = daysBack; i >= 0; i--) {
    const date = moment().subtract(i, 'days').format('YYYY-MM-DD');
    const count = pages.where(p => moment(p.file.ctime).format('YYYY-MM-DD') == date).length;
    labels.push(moment(date).format('MM-DD'));
    data.push(count);
}

// 3. Render Chart
const chartData = {
    type: 'line',
    data: {
        labels: labels,
        datasets: [{
            label: '📝 New Notes Created',
            data: data,
            backgroundColor: ['rgba(54, 162, 235, 0.2)'],
            borderColor: ['rgba(54, 162, 235, 1)'],
            borderWidth: 2,
            tension: 0.4, // Curvy lines
            fill: true
        }]
    }
};

window.renderChart(chartData, this.container);
```
`````


-----

3. The "Action Bar" (Interactive Header)

**The Problem:** The "Live Header" we built is read-only. To change status, you have to go into the YAML.
**The Solution:** Use **Meta-Bind** to inject *buttons* directly into the header that trigger QuickAdd macros or modify fields.
**The "Architect" Value:** Transforms the note from a "Document" into an "App Interface."

### The Upgrade

Update your **Neuro-Link Header** (from the previous step) to include this Meta-Bind button row:

```markdown
> [!controls] 🎛️ Control Deck
> `INPUT[inlineSelect(option(seedling), option(incubating), option(evergreen)):status]`
> `BUTTON[promote-note]` 

```

**Requires:**

1.  **Meta-Bind** installed.
2.  A **QuickAdd Macro** named "Promote Note" that performs your specific status logic (e.g., changes tag `#status/seedling` to `#status/incubating`).
3.  **Button Definition**: You must define the button in the note or a global file:
    ````markdown
    ```meta-bind-button
    label: 🚀 Promote Status
    icon: upload
    id: promote-note
    action:
      type: command
      command: quickadd:choice:PromoteNote 
    ```
    ````

### Systemic Summary

You now have three layers of synergy:

1.  **The Live Header** (Dataview + Templater): *Monitoring* the immediate state.
2.  **The Semantic Bridge** (DataviewJS): *Discovering* hidden connections.
3.  **The Vault Pulse** (Charts + DataviewJS): *Visualizing* the macro-system.

> [!abstract] **System Evolution: From "Text" to "Interface"**
> We have moved past simple *counting*. The next frontier is **Visualization** and **Validation**.
>
> Using Dataview's ability to render **HTML** on the fly, we can turn your notes into graphical dashboards. We can also create "Quality Assurance" systems that validate your metadata integrity in real-time.

Here are **3 Advanced Display Modules** that transform raw metadata into visual interfaces.

-----

### The "Holographic" Progress Bar (Visual Task Tracking)

**Concept**: Text percentages (e.g., "50%") are hard to scan. A visual bar is instant.
**Mechanism**: We inject standard HTML `<progress>` tags into the note, calculating the `value` dynamically based on your checkboxes.

**The Code:**

```markdown
> [!abstract] 📊 Project Velocity
> **Completion**:: `= "<progress value='" + round((length(filter(this.file.tasks, (t) => t.completed)) / max(list(1, length(this.file.tasks)))) * 100) + "' max='100'></progress>"` 
> **Status**:: `= choice(length(filter(this.file.tasks, (t) => t.completed)) = length(this.file.tasks), "✅ Complete", "🚧 In Progress")`
```

**What it looks like**:
Instead of text, you get a native operating-system style progress bar that fills up as you check off boxes in the note.

-----

### The "Data Integrity" Scanner (Quality Assurance)

**Concept**: A PKB rots when metadata is missing. This module acts as a "Check Engine Light." It scans your YAML frontmatter to ensure required fields (like `status`, `type`, `tags`) actually exist.
**Mechanism**: It checks for null values and outputs a warning if your "Permanent Note" is missing its critical taxonomy.

**The Code:**

```markdown
> [!fail] 🛠️ Metadata Health Check
> **Missing Fields**:: `$= const fields = ["status", "type", "tags"]; const missing = fields.filter(f => !dv.current()[f]); missing.length > 0 ? "⚠️ Missing: " + missing.join(", ") : "✅ All Systems Go"`
```

**How to use**:
Put this in your templates. If you forget to add a status, the header will scream **"⚠️ Missing: status"** at you. When you fix it, it auto-updates to **"✅ All Systems Go"**.

-----

### The "Smart Badge" Array (Visual Classification)

**Concept**: Text tags (`#type/project`) are functional but ugly. This module converts your file path or specific frontmatter properties into "Pill Badges" (like GitHub labels) for a cleaner aesthetic.
**Mechanism**: Uses HTML `<span>` with inline CSS styling based on logic.

**The Code:**

```markdown
> [!info] 🏷️ Context Badges
> **Type**:: `= "<span style='background-color: #4a6fa5; padding: 2px 6px; border-radius: 4px; color: white; font-size: 0.8em;'>" + choice(this.type, this.type, "Unclassified") + "</span>"`
> **Folder**:: `= "<span style='background-color: #333; padding: 2px 6px; border-radius: 4px; color: #aaa; font-size: 0.8em;'>" + this.file.folder + "</span>"`
```

**What it does**:
It renders your `type` metadata (e.g., "project") inside a styled blue badge, and your folder path inside a subtle grey badge. This makes the header look like a professional application UI rather than a markdown file.

-----

### Architect's Recommendation

Combine these into a **"Master Control"** Callout for your Projects:

```markdown
> [!stack] 🎛️ Project Control Center
> **Velocity**:: `= "<progress value='" + round((length(filter(this.file.tasks, (t) => t.completed)) / max(list(1, length(this.file.tasks)))) * 100) + "' max='100'></progress>"`
> **Health**:: `$= const fields = ["priority", "due-date"]; const missing = fields.filter(f => !dv.current()[f]); missing.length > 0 ? "⚠️ Missing: " + missing.join(", ") : "✅ Valid"`
> **Context**:: `= "<span style='background-color: #2d7a46; padding: 2px 8px; border-radius: 10px; color: white;'>" + this.status + "</span>"`
```


