---
aliases:
  - "inline-queries"
  - "Inline Queries"
  - Dataview Inline DQL
  - Inline Dataview Syntax
  - DQL Inline Queries
  - Embedded Dataview
tags:
  - "type/permanent"
  - "year/2025"
  - "complexity/intermediate"
  - "context/applied"
  - "learning-processes"
  - "conceptual-learning"
  - "dataview"
  - "dataview-queries"
  - "dataviewjs"
  - "control-processes"
source: "claude-sonnet-4.5"
id: "20251123230106"
created: "2025-11-23T23:01:06"
modified: "2025-11-23T23:01:06"
week: "[[2025-W47]]"
month: "[[2025-11]]"
quarter: "[[2025-Q4]]"
year: "[[2025]]"
type: "reference"
maturity: "needs-review"
confidence: "speculative"
next-review: "2025-11-30"
review-count: 0
link-count: 0
backlink-count: 0
link-up:
  - "[[pkb-&-pkm-moc]]"
link-related:
  - "[[2025-11-23|Daily-Note]]"
---
# Dataview: Inline Queries


aliases: [Dataview Inline DQL, Inline Dataview Syntax, DQL Inline Queries, Embedded Dataview]
---

# ⚡ Dataview Inline Queries — Implementation Guide

> [!the-purpose]
> **Inline queries bring dynamic, computed information directly into your prose.** Unlike traditional [[Dataview Plugin]] code blocks that create separate query results sections, inline queries embed live data seamlessly within sentences and paragraphs, making your notes reactive to your vault's changing state.

---

## 🎯 Core Concept

> [!definition]
> **Dataview Inline Queries** are compact, single-line expressions that execute [[Dataview Query Language]] (DQL) computations and render results directly within text. They transform static notes into dynamic views of your [[Personal Knowledge Base]], displaying metadata, calculations, and aggregations that update automatically as your vault evolves.

> [!analogy]
> Think of inline queries as **embedded spreadsheet cells** in your text. Just as Excel formulas calculate values based on other cells, inline queries compute values based on your vault's metadata. The difference? They read naturally within prose rather than living in a separate calculation layer.

### Inline vs. Block Queries

| Aspect | Inline Queries | Block Queries |
|--------|----------------|---------------|
| **Syntax** | `` `= expression` `` | ````dataview … ```` |
| **Output Style** | Inline with text | Separate section |
| **Use Case** | Single values, counters | Lists, tables, complex views |
| **Readability** | Seamless prose integration | Structured data display |
| **Performance** | Lightweight | More resource-intensive |

---

## 📐 Syntax & Structure

> [!methodology-and-sources]
> ### Basic Inline Query Syntax
> 
> Dataview inline queries use a **backtick-equals pattern**:
> ```markdown
> `= <expression>`
> ```
> 
> The `=` symbol signals to Dataview: "evaluate what follows as DQL."

### Three Primary Access Patterns

#### 1️⃣ **Direct Field Access** (Current Page)
```markdown
`= this.field-name`
`= this.status`
`= this.due-date`
```

> [!what-this-does]
> Accesses [[YAML Frontmatter]] or [[Inline Fields]] from the **current page**. The `this` keyword references the active note's metadata.

#### 2️⃣ **Link Field Access** (Other Pages)
```markdown
`= [[Note Name]].field-name`
`= [[Project Alpha]].progress`
`= [[2024-11-20]].mood`
```

> [!what-this-does]
> Retrieves metadata from **other notes** via [[Wiki-Links]]. Essential for creating relational connections between notes.

#### 3️⃣ **Query Results** (Vault-Wide Aggregation)
```markdown
`= length(filter(pages(), (p) => p.status = "active"))`
`= sum(filter(pages("#project"), (p) => p.budget))`
```

> [!what-this-does]
> Performs **computed queries** across your entire vault using [[Dataview Functions]]. This is where the real power emerges.

---

## 🔧 Implementation Patterns for Daily Operations

### 🏷️ Status & Metadata Display

> [!example]
> **Use Case:** Display current note's metadata inline
> 
> ```markdown
> This project is currently **`= this.status`** with a priority of `= this.priority`.
> 
> Last reviewed on `= this.reviewed` by `= this.author`.
> ```
> 
> **Renders as:**  
> This project is currently **in-progress** with a priority of high.  
> Last reviewed on 2024-11-15 by Sarah Chen.

> [!helpful-tip]
> **Best Practice:** Use inline queries to surface critical metadata at the top of notes, creating a "living header" that reflects current state without manual updating.

---

### 📊 Dynamic Counters & Aggregations

> [!example]
> **Use Case:** Count related items across your vault
> 
> ```markdown
> I have `= length(filter(pages(#task), (t) => !t.completed))` open tasks.
> 
> Total project budget: $`= sum(filter(pages("#project"), (p) => p.budget))`
> 
> Research notes in this area: `= length(filter(pages(), (p) => contains(p.tags, "research") and contains(p.file.folder, this.file.folder)))`
> ```
> 
> **Renders as:**  
> I have 23 open tasks.  
> Total project budget: $45,000  
> Research notes in this area: 12

> [!warning]
> **Performance Consideration:** Vault-wide queries (`pages()`) can be slow in large vaults (10,000+ notes). Consider narrowing scope with folder paths or specific tags: `pages(""10 Projects"")` or `pages("#active-project")`.

---

### 📅 Date Calculations & Time Tracking

> [!example]
> **Use Case:** Calculate time differences and deadlines
> 
> ```markdown
> Days until deadline: `= (this.deadline - date(today)).days`
> 
> Days since project start: `= (date(today) - this.start-date).days`
> 
> Project duration: `= (this.end-date - this.start-date).days` days
> 
> Overdue by: `= choice(this.deadline < date(today), (date(today) - this.deadline).days + " days", "Not overdue")`
> ```

> [!helpful-tip]
> **Date Function Reference:**
> - `date(today)` - Current date
> - `date("2024-11-23")` - Specific date
> - `.days` / `.months` / `.years` - Extract duration components
> - `choice(condition, true-value, false-value)` - Conditional logic

---

### 🔗 Relational Metadata (Cross-Note References)

> [!example]
> **Use Case:** Pull information from linked notes
> 
> ```markdown
> Project Manager: `= [[Project Alpha]].manager`
> 
> Team Size: `= length([[Project Alpha]].team-members)`
> 
> Budget Remaining: $`= [[Project Alpha]].budget - [[Project Alpha]].spent`
> 
> Parent Project Status: `= [[Project Alpha]].status`
> ```

> [!connections-and-links]
> This pattern enables **bi-directional information flow**. A change to `[[Project Alpha]]`'s frontmatter instantly updates all notes that query it. This is foundational for [[MOC]] (Maps of Content) architectures and [[Dashboard Design]].

---

### 📋 Task & Progress Tracking

> [!example]
> **Use Case:** Real-time progress indicators
> 
> ```markdown
> Tasks completed: `= length(filter(this.file.tasks, (t) => t.completed))` / `= length(this.file.tasks)` (`= round((length(filter(this.file.tasks, (t) => t.completed)) / length(this.file.tasks)) * 100)`%)
> 
> Completion rate: `= round((length(filter(pages("#project"), (p) => p.status = "complete")) / length(pages("#project"))) * 100)`% of all projects
> ```

> [!what-this-does]
> The `this.file.tasks` property accesses **all tasks in the current note**, enabling progress calculations without manual counting. Combine with [[Task Management]] plugins like Tasks for even more powerful workflows.

---

### 🧮 Mathematical Expressions & Calculations

> [!example]
> **Use Case:** Embedded calculations for quantitative notes
> 
> ```markdown
> Average study time: `= round(sum(this.study-sessions) / length(this.study-sessions), 1)` hours
> 
> ROI: `= round(((this.revenue - this.cost) / this.cost) * 100, 2)`%
> 
> Compound interest: $`= round(this.principal * (1 + this.rate)^this.years, 2)`
> ```

> [!helpful-tip]
> **Mathematical Functions:**
> - `sum(list)` - Total of all values
> - `round(value, decimals)` - Round to specified precision
> - `min(list)` / `max(list)` - Find extremes
> - Standard operators: `+`, `-`, `*`, `/`, `^` (exponent)

---

## 🎨 Advanced Implementation Techniques

### 🔄 Conditional Display with `choice()`

> [!example]
> ```markdown
> Status: `= choice(this.deadline < date(today), "⚠️ OVERDUE", choice(this.status = "complete", "✅ Done", "🔄 In Progress"))`
> 
> Priority: `= choice(this.priority > 7, "🔴 Critical", choice(this.priority > 4, "🟡 Medium", "🟢 Low"))`
> ```

> [!methodology-and-sources]
> **Nested `choice()` Pattern:**
> ```javascript
> choice(
>   condition1, "result if true",
>   choice(
>     condition2, "result if condition2 true",
>     "fallback result"
>   )
> )
> ```

---

### 📦 List Manipulation & Filtering

> [!example]
> ```markdown
> Active tags: `= join(filter(this.tags, (t) => t != "archived"), ", ")`
> 
> Team members present: `= join(filter(this.team, (m) => contains(this.attendees, m)), ", ")`
> 
> First three authors: `= join(slice(this.authors, 0, 3), ", ")`
> ```

> [!helpful-tip]
> **Common List Functions:**
> - `filter(list, predicate)` - Keep matching items
> - `map(list, transform)` - Transform each item
> - `slice(list, start, end)` - Extract subset
> - `join(list, separator)` - Convert to string
> - `contains(list, item)` - Check membership

---

### 🧩 Template Integration

> [!example]
> **Use Case:** [[Template Integration]] with [[Templater]] plugin
> 
> ```markdown
> ---
> created: 2025-11-24 05:19
> status: active
> priority: 5
> ---
> 
> # Dataview Plugin
> 
> **Created:** `= this.created`  
> **Status:** `= this.status`  
> **Priority:** `= choice(this.priority > 7, "🔴 High", "🟢 Normal")`  
> **Days active:** `= (date(today) - this.created).days`
> ```

> [!connections-and-links]
> This pattern creates **dynamic note headers** that update automatically. Pair with [[Daily Notes]] templates for powerful daily dashboard functionality.

---

### 🖥️ Dashboard Construction

> [!example]
> **Use Case:** Create a personal productivity dashboard
> 
> ```markdown
> # 📊 Productivity Dashboard
> 
> ## 📈 Current Metrics
> - **Active Projects:** `= length(filter(pages("#project"), (p) => p.status = "active"))`
> - **Completed This Week:** `= length(filter(pages("#project"), (p) => p.completed >= date(today) - dur(7 days)))`
> - **Overdue Items:** `= length(filter(pages(), (p) => p.deadline and p.deadline < date(today) and p.status != "complete"))`
> - **Total Notes:** `= length(pages())`
> - **Notes Created Today:** `= length(filter(pages(), (p) => p.file.cday = date(today)))`
> 
> ## 💰 Financial Overview
> - **Total Budget:** $`= sum(filter(pages("#project"), (p) => p.budget))`
> - **Total Spent:** $`= sum(filter(pages("#project"), (p) => p.spent))`
> - **Remaining:** $`= sum(filter(pages("#project"), (p) => p.budget - p.spent))`
> 
> ## ⏰ Time Analysis
> - **Average Project Duration:** `= round(average(map(filter(pages("#project"), (p) => p.end-date), (p) => (p.end-date - p.start-date).days)), 1)` days
> ```

> [!what-this-does]
> This dashboard becomes a **living nerve center** for your [[Personal Knowledge Base]]. Every time you open it, the numbers reflect your vault's current state with zero manual updates.

---

## 🚀 Day-to-Day Workflow Patterns

### 🔍 Note Review Systems

> [!example]
> **Pattern:** Add to note templates for [[03-notes/01_permanent-notes/01_cognitive-development/Spaced Repetition]] tracking
> 
> ```markdown
> **Last Reviewed:** `= this.last-reviewed`  
> **Days Since Review:** `= (date(today) - this.last-reviewed).days`  
> **Next Review:** `= this.last-reviewed + dur(30 days)`  
> **Review Status:** `= choice((date(today) - this.last-reviewed).days > 30, "⚠️ Needs Review", "✅ Current")`
> ```

---

### 📝 Writing Progress Tracking

> [!example]
> **Pattern:** Embed in long-form content notes
> 
> ```markdown
> **Word Count:** `= this.word-count` / `= this.target-words` (`= round((this.word-count / this.target-words) * 100)`%)
> 
> **Completion:** `= choice(this.word-count >= this.target-words, "✅ Complete", "🔄 " + string(this.target-words - this.word-count) + " words remaining")`
> ```

> [!helpful-tip]
> Combine with a [[quickadd]] macro that updates `word-count` frontmatter field on save for fully automated progress tracking.

---

### 🔬 Research Organization

> [!example]
> **Pattern:** For [[Zettelkasten]] literature notes
> 
> ```markdown
> **Source Type:** `= this.type`  
> **Publication Year:** `= this.year`  
> **Citations in Vault:** `= length(filter(pages(), (p) => contains(p.file.outlinks, this.file.link)))`  
> **Connected Notes:** `= length(this.file.outlinks)`  
> **Research Cluster:** `= this.cluster`
> ```

---

## ⚠️ Common Pitfalls & Solutions

> [!warning]
> ### Issue: Null/Undefined Errors
> 
> **Problem:** Query returns `null` when field doesn't exist
> 
> **Solution:** Use `default()` function or conditional checks
> ```markdown
> `= default(this.status, "Not Set")`
> `= choice(this.priority, this.priority, "No priority assigned")`
> ```

> [!warning]
> ### Issue: Type Mismatches
> 
> **Problem:** Trying to perform math on text fields
> 
> **Solution:** Use `number()` conversion or validate data types
> ```markdown
> `= number(this.budget) + number(this.additional-costs)`
> ```

> [!warning]
> ### Issue: Performance Degradation
> 
> **Problem:** Too many inline queries on one page slow rendering
> 
> **Solution:** 
> 1. Limit queries to essential information
> 2. Use folder-scoped queries: `pages(""20 Projects"")` instead of `pages()`
> 3. Cache complex calculations in frontmatter fields updated via [[DataviewJS]]

---

## 🧪 Advanced: Combining with JavaScript

> [!example]
> **Pattern:** Switch to [[JavaScript Dataview]] for complex logic
> 
> ````markdown
> ```dataviewjs
> const incomplete = dv.pages("#task")
>   .where(t => !t.completed)
>   .length;
> 
> dv.span(`**Open Tasks:** ${incomplete}`);
> ```
> ````
> 
> **Why:** DataviewJS offers full JavaScript capabilities when inline DQL hits limitations. Use for:
> - Complex string manipulation
> - Custom formatting
> - External data integration
> - Advanced array operations

---

## 📚 Quick Reference

> [!quick-reference]
> ### Syntax Cheat Sheet
> 
> | Pattern | Purpose | Example |
> |---------|---------|---------|
> | `` `= this.field` `` | Current page field | `` `= this.status` `` |
> | `` `= [[Note]].field` `` | Other page field | `` `= [[Projects]].budget` `` |
> | `` `= length(pages())` `` | Count pages | `` `= length(pages("#task"))` `` |
> | `` `= sum(map(pages(), (p) => p.value))` `` | Sum across pages | `` `= sum(map(pages("#expense"), (e) => e.amount))` `` |
> | `` `= choice(condition, true, false)` `` | Conditional | `` `= choice(this.done, "✅", "⏳")` `` |
> | `` `= date(today)` `` | Today's date | `` `= date(today)` `` |
> | `` `= (date2 - date1).days` `` | Date difference | `` `= (this.due - date(today)).days` `` |
> 
> ### Essential Functions
> - **Aggregation:** `sum()`, `average()`, `min()`, `max()`, `length()`
> - **Filtering:** `filter()`, `where()`, `contains()`
> - **Transformation:** `map()`, `flat()`, `slice()`
> - **Logic:** `choice()`, `default()`, `any()`, `all()`
> - **Text:** `join()`, `split()`, `replace()`, `string()`
> - **Math:** `round()`, `floor()`, `ceil()`, `number()`

---

## 🎯 Best Practices Summary

> [!core-principle]
> **The Three Principles of Effective Inline Query Usage:**
> 
> 1. **Semantic Integration** — Inline queries should read naturally within prose. If it feels forced, consider a block query instead.
> 
> 2. **Strategic Scoping** — Narrow queries to specific folders or tags rather than querying entire vault when possible. This maintains performance at scale.
> 
> 3. **Metadata First** — Establish robust [[YAML Frontmatter]] conventions before implementing complex queries. Consistent metadata architecture is foundational to reliable inline query results.

> [!helpful-tip]
> **Implementation Strategy for New Users:**
> 4. Start with simple `this.field` queries in note headers
> 5. Progress to cross-note queries (`[[Note]].field`)
> 6. Build confidence with counters and basic aggregations
> 7. Advance to complex filtering and conditional logic
> 8. Finally, integrate into [[Template Integration]] systems and [[Dashboard Design]]

---

# 🔗 Related Topics for PKB Expansion

1. **[[Dataview Query Language (DQL)]]**
   - *Connection*: Inline queries are a subset of DQL; full query blocks offer expanded capabilities including table and list views
   - *Depth Potential*: Comprehensive DQL mastery enables building complex knowledge management automation and dynamic MOCs
   - *Knowledge Graph Role*: Foundational skill for creating reactive [[Personal Knowledge Base]] architectures

2. **[[DataviewJS — JavaScript API]]**
   - *Connection*: When inline DQL hits limitations, DataviewJS provides full programmatic control over query rendering and computation
   - *Depth Potential*: Enables custom visualizations, external API integration, and complex data transformations beyond declarative DQL
   - *Knowledge Graph Role*: Advanced automation layer for power users building sophisticated [[Dashboard Design]] systems

3. **[[YAML Frontmatter Architecture]]**
   - *Connection*: Inline queries are only as powerful as the metadata they query; systematic frontmatter design is prerequisite knowledge
   - *Depth Potential*: Establishing vault-wide metadata schemas, controlled vocabularies, and taxonomies for reliable automated queries
   - *Knowledge Graph Role*: Foundational infrastructure enabling all query-based workflows and [[MOC]] automation

4. **[[Templater Plugin Integration]]**
   - *Connection*: Combining Templater's template logic with Dataview inline queries creates dynamic, self-updating note templates
   - *Depth Potential*: Building advanced note generation systems that inject both static (Templater) and reactive (Dataview) content
   - *Knowledge Graph Role*: Automation bridge between note creation and knowledge graph maintenance, critical for scalable [[Zettelkasten]] workflows

---
```
<thinking>
**REQUEST CLASSIFICATION:**
- Type: comprehensive_note (reference note)
- Scope: reference (technical guide)
- Research Required: NO (Dataview inline queries are a well-established Obsidian plugin feature from my training data)
- Note Type: Reference Note (technical/practical guide)

**STRUCTURAL PLANNING:**

This request is for a reference note about Dataview inline queries - a specific feature of the Obsidian Dataview plugin. The user wants practical implementation guidance for "day to day operations," which signals they need:
1. Clear explanation of what inline queries are
2. Syntax reference
3. Practical examples for common use cases
4. Best practices for daily workflows
5. Troubleshooting and optimization tips

**Information Architecture:**
```
1. Core Concept Definition
   - What inline queries are
   - How they differ from dataview blocks
   - When to use them

2. Syntax & Structure
   - Basic syntax patterns
   - Query types (LIST, TABLE, TASK, CALENDAR)
   - Field access methods

3. Practical Implementation Categories
   - Status tracking
   - Metadata display
   - Dynamic calculations
   - Link aggregation
   - Date operations

4. Day-to-Day Workflow Integration
   - Template integration
   - Dashboard applications
   - Note review systems
   - Project management

5. Advanced Techniques
   - Complex expressions
   - Combining with JS
   - Performance considerations

6. Troubleshooting & Best Practices
```

**Wiki-Link Opportunities Identified:**
- [[Dataview Plugin]]
- [[Dataview Query Language]] (DQL)
- [[Obsidian Metadata]]
- [[YAML Frontmatter]]
- [[Inline Fields]]
- [[Dataview Functions]]
- [[JavaScript Dataview]] (DataviewJS)
- [[Template Integration]]
- [[MOC]] (Maps of Content)
- [[Dashboard Design]]
- [[Task Management]]
- [[Daily Notes]]
- [[Zettelkasten]]
- [[Progressive Summarization]]
- [[Regular Expressions]]

**Callout Strategy:**
- [!definition] - Core concept explanation
- [!the-purpose] - Why inline queries matter
- [!methodology-and-sources] - Syntax patterns
- [!example] - Concrete implementations (multiple)
- [!helpful-tip] - Best practices
- [!warning] - Common pitfalls
- [!what-this-does] - Feature explanations
- [!analogy] - Conceptual understanding
- [!connections-and-links] - Related features
- [!quick-reference] - Syntax cheat sheet

**Metadata Planning:**
Tags: #obsidian #dataview #inline-queries #technical-guide #reference-note
Aliases: [Dataview Inline DQL, Inline Dataview Syntax, DQL Inline Queries, Embedded Dataview]

**Chain-of-Density Layers:**
1. Foundation: What inline queries are and basic syntax
2. Enrichment: All query types with detailed syntax
3. Connection: Integration with workflows, templates, metadata systems
4. Application: Practical examples for daily operations across multiple use cases
</thinking>
```