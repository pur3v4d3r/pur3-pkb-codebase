---
aliases:
  - Dataview Inline Fields
  - Inline Metadata
tags:
  - type/permanent
  - year/2025
  - complexity/basic
  - context/applied
  - obsidian/plugins/dataview
  - obsidian
source: claude-sonnet-4.5
id: "20251123114909"
created: 2025-11-23T11:49:09
modified: 2025-11-23T11:49:09
week: "[[2025-W47]]"
month: "[[2025-11]]"
quarter: "[[2025-Q4]]"
year: "[[2025]]"
type: reference
maturity: needs-review
confidence: speculative
next-review: 2025-11-30
review-count: 0
link-count: 0
backlink-count: 0
link-up:
  - "[[pkb-&-pkm-moc]]"
link-related:
  - "[[2025-11-23|Daily-Note]]"
---

# Dataview Inline Fields: Complete Reference Guide



aliases: [Dataview Inline Fields, Inline Metadata, Dataview Inline Syntax]
---

# 🏷️ Dataview Inline Fields: Complete Reference Guide

> [!the-purpose]
> **Inline fields** are a core [[Dataview Plugin]] feature that allows you to embed queryable metadata directly within your note content using the `Key:: Value` syntax. Unlike [[YAML Frontmatter]] which sits at the top of a note, inline fields let you annotate specific paragraphs, sentences, list items, or tasks with structured data that can be queried, aggregated, and displayed through [[Dataview Query Language]] (DQL) queries.

## 📐 What Are Inline Fields?

> [!definition]
> An **inline field** is metadata written directly in your [[Markdown]] content using a double-colon separator (`::`) between a key and its value. Inline fields use a `Key:: Value` syntax that can be embedded anywhere in your file, including in the middle of sentences, on their own lines, within list items, or inside task checkboxes.

Inline fields offer several advantages over traditional frontmatter:

- **Contextual placement**: Add metadata exactly where it's relevant in your content
- **Mid-sentence annotation**: Embed fields seamlessly within prose
- **Task-specific metadata**: Annotate individual tasks and list items with unique data
- **Mixed workflows**: Use inline fields and YAML frontmatter together in the same note
- **Dynamic knowledge work**: Perfect for [[03-notes/01_permanent-notes/02_personal-knowledge-base/Personal Knowledge Management]] systems where context matters

> [!core-principle]
> Inline fields are the only way to explicitly add metadata to specific list items, while YAML frontmatter always applies to the entire page. This makes inline fields essential for granular data tracking in task management, project logging, and detailed annotation workflows.

---

## 🔧 Syntax Variations

[[Dataview Plugin]] supports three distinct syntax formats for inline fields, each designed for different use cases.

### Standard Line-Based Syntax

> [!methodology-and-sources]
> **Format:** `Key:: Value`
> 
> The most straightforward approach—place the field on its own line without any preceding content. If your inline field has its own line, without any content beforehand, you can write it like this:

```markdown
# Project Alpha

Status:: In Progress
Priority:: High
Due Date:: 2025-12-01
Project Lead:: [[John Smith]]
Budget:: $50,000
```

**Characteristics:**
- Fields are **visible** in both edit and reading mode
- Key names can include **spaces** and **capital letters**
- Multiple fields can stack vertically for organized metadata blocks
- Ideal for creating "metadata sections" within notes

> [!helpful-tip]
> When using spaces or capitalized letters in metadata key names, Dataview provides a sanitized version of the key—always lowercase with dashes instead of spaces. For example, `Project Lead:: John` becomes queryable as `project-lead`.

### Bracketed Inline Syntax

> [!methodology-and-sources]
> **Format:** `[Key:: Value]`
> 
> If you want to embed metadata inside sentences, or multiple fields on the same line, you can use the bracket syntax by wrapping your field in square brackets:

```markdown
I would rate this project a [rating:: 9] out of 10! The execution was [quality:: exceptional] and the timeline was [status:: on-track].

The meeting is scheduled for [date:: 2025-11-25] at [time:: 14:00] in [location:: Conference Room B].
```

**When to use bracketed syntax:**
- Embedding fields within paragraphs or sentences
- Placing multiple fields on the same line
- **Required** for annotating list items and tasks
- Maintaining natural prose flow while adding queryable data

> [!example]
> **Task annotation with bracketed fields:**
> 
> ```markdown
> - [ ] Send proposal to client [due:: 2025-11-30] [priority:: high] [client:: [[Acme Corp]]]
> - [ ] Review contract documents [due:: 2025-12-05] [assignee:: [[Sarah Jones]]]
> - [x] Complete initial research [completed:: 2025-11-20] [hours:: 8]
> ```

> [!warning]
> When annotating list items or tasks with metadata, you always need to use the bracket syntax because the field is not the only information in the line.

### Parenthesis (Hidden Key) Syntax

> [!methodology-and-sources]
> **Format:** `(Key:: Value)`
> 
> There is also the alternative parenthesis syntax, which hides the key when rendered in Reader mode:

```markdown
This analysis was completed by (author:: Dr. Emily Watson) on (date:: 2025-11-23).

The research methodology employed (methodology:: mixed-methods) across (sample-size:: 150) participants.
```

**Rendering behavior:**
- **Edit mode**: Both key and value visible: `(author:: Dr. Emily Watson)`
- **Reading mode**: Only value shown: `Dr. Emily Watson`
- **Dataview queries**: Key remains fully accessible for querying

**Use cases:**
- Creating cleaner reading experiences while preserving queryable metadata
- Embedding technical metadata that readers don't need to see
- Maintaining professional document appearance with hidden data infrastructure

---

## 📊 Supported Data Types

[[Dataview Plugin]] automatically interprets inline field values into appropriate data types for querying and manipulation.

> [!quick-reference]
> **Dataview Data Type Auto-Detection:**
> 
> | Syntax Example | Interpreted Type | Notes |
> |---------------|------------------|-------|
> | `count:: 42` | **Number** | Integer or decimal |
> | `title:: Project Alpha` | **Text** | Default string type |
> | `due:: 2025-12-01` | **Date** | ISO 8601 format preferred |
> | `time:: 14:30` | **Duration** | Time-based values |
> | `completed:: true` | **Boolean** | `true`/`false` values |
> | `tags:: #project #priority` | **Tags** | Hash-prefixed identifiers |
> | `related:: [[Note 1]], [[Note 2]]` | **Links** | Wiki-link format |
> | `items:: one, two, three` | **Array** | Comma-separated values |

### Working With Different Types

> [!example]
> **Numbers and calculations:**
> 
> ```markdown
> hours-worked:: 8.5
> hourly-rate:: 75
> revenue:: 637.50
> ```
> 
> Query these with mathematical operations:
> ```dataview
> TABLE hours-worked, hourly-rate, hours-worked * hourly-rate AS "Total Revenue"
> WHERE hours-worked
> ```

> [!example]
> **Dates and temporal queries:**
> 
> ```markdown
> project-start:: 2025-11-01
> project-end:: 2025-12-31
> milestone-1:: 2025-11-15
> milestone-2:: 2025-12-10
> ```
> 
> Filter by date ranges:
> ```dataview
> LIST WHERE project-end > date(today)
> SORT project-end ASC
> ```

> [!example]
> **Links and relationships:**
> 
> ```markdown
> team-members:: [[Alice Chen]], [[Bob Rodriguez]], [[Carol Kim]]
> related-projects:: [[Project Beta]], [[Initiative Gamma]]
> stakeholder:: [[VP of Engineering]]
> ```
> 
> Build relationship queries:
> ```dataview
> TABLE team-members, length(team-members) AS "Team Size"
> WHERE team-members
> ```

> [!example]
> **Multi-value fields (arrays):**
> 
> ```markdown
> skills:: Python, JavaScript, SQL, Docker
> technologies:: React, PostgreSQL, AWS, Kubernetes
> certifications:: AWS Certified, Scrum Master, PMP
> ```
> 
> Query contains operations:
> ```dataview
> LIST WHERE contains(skills, "Python")
> ```

---

## 🎯 Practical Use Cases

### 📝 Task Management with Metadata

> [!use-cases-and-examples]
> Inline fields transform simple task lists into queryable project management systems:

```markdown
## Sprint Backlog

- [ ] Implement user authentication [priority:: high] [estimate:: 5h] [assignee:: [[Dev Team]]] [due:: 2025-11-28]
- [ ] Design dashboard mockups [priority:: medium] [estimate:: 3h] [assignee:: [[Design Team]]] [due:: 2025-11-29]
- [ ] Write API documentation [priority:: low] [estimate:: 2h] [assignee:: [[Tech Writer]]] [due:: 2025-12-02]
- [x] Set up development environment [completed:: 2025-11-22] [actual-time:: 4h]
```

**Query high-priority incomplete tasks:**
```
TASK
WHERE !completed AND priority = "high"
SORT due ASC
```

**Calculate sprint velocity:**
```
TABLE 
  sum(rows.estimate) AS "Estimated Hours",
  sum(rows.actual-time) AS "Actual Hours"
WHERE completed
GROUP BY file.link
```

### 📚 Reading Notes & Book Tracking

> [!use-cases-and-examples]
> Create a comprehensive reading database:

```markdown
---
title: "Atomic Habits"
author: James Clear
type: #book
---

# Atomic Habits

author:: [[James Clear]]
published:: 2018
pages:: 320
rating:: 9/10
status:: Read Complete
date-started:: 2025-10-15
date-finished:: 2025-11-10
genre:: Self-Help, Psychology
themes:: habit formation, behavior change, identity

## Key Insights

The aggregation of marginal gains is powerful [insight-rating:: 5/5] [page:: 15].

Habit stacking creates automatic behaviors [insight-rating:: 5/5] [page:: 78] [implementation:: Applied to morning routine].
```

**Query all books by rating:**
```
TABLE author, rating, status, date-finished
FROM #book
WHERE rating >= 8
SORT rating DESC
```

### 🔬 Research & Knowledge Synthesis

> [!use-cases-and-examples]
> Annotate research materials with extractable metadata:

```markdown
# Climate Change Mitigation Strategies

study:: [[IPCC 2023 Report]]
topic:: climate-science
methodology:: meta-analysis
sample-size:: 1,200 studies
confidence-level:: high

## Carbon Capture Technologies

Direct air capture is promising [effectiveness:: moderate] [cost:: high] [trl:: 6] [source:: [[Nature 2024]]].

Reforestation programs show measurable impact [effectiveness:: high] [cost:: low] [scalability:: excellent] [timeline:: 10-20 years].
```

**Aggregate research findings:**
```
TABLE effectiveness, cost, scalability
WHERE topic = "climate-science"
GROUP BY source
```

### 💼 Project & Client Management

> [!use-cases-and-examples]
> Track business relationships and project details:

```markdown
# Project: Website Redesign - Acme Corp

client:: [[Acme Corp]]
project-type:: web-design
contract-value:: $45,000
start-date:: 2025-11-01
end-date:: 2025-12-20
status:: In Progress
completion:: 65%

## Deliverables

- [x] Wireframes [delivered:: 2025-11-08] [approved:: yes] [hours:: 12]
- [x] Design mockups [delivered:: 2025-11-15] [approved:: yes] [hours:: 20]
- [ ] Frontend development [due:: 2025-12-10] [estimate:: 40h]
- [ ] Backend integration [due:: 2025-12-18] [estimate:: 25h]
```

**Client revenue dashboard:**
```
TABLE 
  contract-value, 
  completion + "%" AS "Progress",
  end-date AS "Deadline"
WHERE client = [[Acme Corp]]
SORT end-date ASC
```

---

## ⚙️ Integration with Dataview Queries

Inline fields become powerful when combined with [[Dataview Query Language]] capabilities.

### Basic Field Access

> [!what-this-does]
> Access inline field values in queries using their sanitized names:

```
LIST priority
WHERE priority = "high"
```

```
TABLE project-lead, budget, due-date
FROM "Projects"
WHERE budget > 10000
SORT due-date ASC
```

### Field Operations & Calculations

> [!example]
> **Mathematical operations:**
> 
> ```
> TABLE 
>   hours-worked, 
>   hourly-rate,
>   hours-worked * hourly-rate AS "Total Cost"
> WHERE hours-worked
> ```

> [!example]
> **Date calculations:**
> 
> ```
> TABLE 
>   due-date,
>   due-date - date(today) AS "Days Remaining"
> WHERE due-date > date(today)
> SORT due-date ASC
> ```

> [!example]
> **String manipulation:**
> 
> ```
> TABLE 
>   upper(status) AS "STATUS",
>   lower(project-type) AS "type"
> WHERE status
> ```

### Aggregation Functions

> [!methodology-and-sources]
> **Aggregate inline field data across multiple notes:**

```datavie
TABLE 
  count(rows) AS "Total Tasks",
  sum(rows.estimate) AS "Total Hours",
  average(rows.priority-score) AS "Avg Priority"
GROUP BY project
```

**Common aggregation patterns:**
- `sum(rows.field-name)` - Total numeric values
- `average(rows.field-name)` - Mean value
- `min(rows.field-name)` - Minimum value
- `max(rows.field-name)` - Maximum value
- `count(rows)` - Count of items

### Filtering with Multiple Conditions

> [!example]
> **Complex queries combining multiple inline fields:**
> 
> ```
> LIST
> WHERE priority = "high" 
>   AND status != "completed"
>   AND due-date <= date(today) + dur(7 days)
>   AND assignee = [[Current User]]
> SORT due-date ASC
> ```

### Task-Specific Queries

> [!what-this-does]
> Query tasks with their inline field metadata:

```datavie
TASK
WHERE !completed 
  AND contains(tags, "#work")
  AND priority = "high"
SORT due ASC
```

**Access task metadata in TABLE views:**
```datavie
TABLE 
  text AS "Task",
  due,
  priority,
  estimate
FROM "Projects"
FLATTEN file.tasks AS task
WHERE !task.completed
```

---

## 🔑 Key Syntax Rules & Best Practices

> [!core-principle]
> **The Double-Colon Requirement:**
> 
> You need to use a double colon `::` between key and value when using inline fields, contrary to YAML Frontmatter fields where one colon is enough. This distinguishes inline fields from standard Markdown and prevents parsing conflicts.

### Naming Conventions

> [!helpful-tip]
> **Choose field names strategically:**
> 
> - **Use lowercase with hyphens** for consistency: `project-status`, `due-date`, `team-lead`
> - **Avoid spaces** unless you're comfortable with sanitized names
> - **Be descriptive but concise**: `est-hours` rather than `estimated-hours-to-complete`
> - **Establish naming patterns** across your [[Personal Knowledge Base]]

**Handling spaces and capitals:**
```markdown
Project Status:: In Progress  ← Becomes: project-status
DueDate:: 2025-12-01         ← Becomes: duedate
team_lead:: [[Alice]]        ← Queryable as: team_lead
```

> [!quick-reference]
> **Access options for fields with spaces:**
> 
> 1. Use the sanitized name: `WHERE project-status = "active"`
> 2. Use row variable syntax: `WHERE row["Project Status"] = "active"`

### Emoji Field Keys

> [!methodology-and-sources]
> Using emojis as metadata keys is possible, but comes with limitations. When using emojis in field names, you need to put them into square brackets so that Dataview recognizes them correctly.

```markdown
[💰:: $5,000]
[🎯:: High Priority]
[📅:: 2025-12-01]
[✅:: Complete]
```

> [!warning]
> **Cross-platform emoji considerations:**
> 
> When switching operating systems (e.g., from Windows to Android), the same emoji could use another character code and you might not find your metadata when querying it. For maximum portability, prefer alphanumeric field names.

### Value Formatting Guidelines

> [!helpful-tip]
> **Format values for optimal Dataview interpretation:**

**Dates:**
```markdown
✅ due:: 2025-12-01           (ISO 8601 - best)
✅ due:: 2025-12-01T14:30:00  (with time)
⚠️ due:: December 1, 2025    (may not parse correctly)
```

**Numbers:**
```markdown
✅ cost:: 1250.50
✅ percentage:: 0.85
❌ cost:: $1,250.50           (includes currency symbol)
```

**Booleans:**
```markdown
✅ completed:: true
✅ published:: false
❌ completed:: yes            (interpreted as text)
```

**Lists/Arrays:**
```markdown
✅ tags:: tag1, tag2, tag3
✅ links:: [[Note A]], [[Note B]], [[Note C]]
✅ values:: one, two, three
```

### Mixing with YAML Frontmatter

> [!core-principle]
> You can use YAML Frontmatter and Inline fields with all syntax variants together in one file. You do not need to decide for one and can mix them to fit your workflow.

**Strategic combination:**
```markdown
---
title: Project Documentation
type: project-note
created: 2025-11-20
tags: [project, documentation]
---

# Project Alpha

Status:: In Progress
Phase:: Development
Lead:: [[Engineering Team]]

## Tasks

- [ ] Complete API integration [due:: 2025-12-01] [priority:: high]
- [ ] Write user documentation [due:: 2025-12-05] [priority:: medium]
```

**Best practice approach:**
- **Frontmatter**: Static, note-level metadata (title, creation date, broad categorization)
- **Inline fields**: Dynamic, contextual metadata (task details, in-text annotations, section-specific data)

---

## 🧰 Advanced Techniques

### Inline DataviewJS Queries as Field Values

> [!what-this-does]
> Assign dynamic calculations to inline fields for reuse in other queries:

```markdown
total-cost:: `$= dv.current().hours * dv.current().rate`
days-remaining:: `$= Math.ceil((dv.current()["due-date"] - Date.now()) / (1000 * 60 * 60 * 24))`
```

**Using computed fields in queries:**
```dataview
TABLE total-cost, days-remaining
WHERE days-remaining < 7
SORT days-remaining ASC
```

### Nested and Complex Values

> [!example]
> **Storing structured data:**
> 
> ```markdown
> team:: {lead: "Alice", members: 5, budget: 50000}
> coordinates:: {lat: 37.7749, lon: -122.4194}
> metrics:: {accuracy: 0.95, precision: 0.89, recall: 0.92}
> ```
> 
> Access nested properties:
> ```
> TABLE team.lead, team.budget
> WHERE team.budget > 30000
> ```

### Template Integration

> [!helpful-tip]
> Create [[Templater]] templates with inline field structures:

```markdown
<%* 
// Templater template for project notes
%>
---
title: <% tp.file.title %>
created: <% tp.date.now("YYYY-MM-DD") %>
type: project
---

# <% tp.file.title %>

status:: Not Started
priority:: <% tp.system.prompt("Priority (low/medium/high)") %>
due-date:: <% tp.system.prompt("Due date (YYYY-MM-DD)") %>
assigned-to:: [[<% tp.system.prompt("Assign to") %>]]
estimated-hours:: <% tp.system.prompt("Estimated hours") %>

## Objectives

- [ ] [milestone-1:: ] [due:: ]
- [ ] [milestone-2:: ] [due:: ]
- [ ] [milestone-3:: ] [due:: ]
```

### Bulk Field Operations with DataviewJS

> [!methodology-and-sources]
> **List all inline fields in current note:**

```dataviewjs
const page = dv.current()
delete page.file
dv.list(Object.keys(page))
```

**Find all unique field names across vault:**
```dataviewjs
let pages = dv.pages();
let fields = new Set();
for (let page of pages) {
    for (let key of Object.keys(page)) {
        if (key !== "file") fields.add(key);
    }
}
dv.list(Array.from(fields).sort());
```

---

## ⚠️ Common Pitfalls & Solutions

> [!constraints-and-pitfalls]
> **Issue #1: Fields not appearing in queries**
> 
> **Causes:**
> - Using single colon `:` instead of double colon `::`
> - Typos in field names (inconsistent spelling)
> - Incorrect bracket syntax for list items
> - Field placed inside code blocks or comments
> 
> **Solution:**
> - Always use `::` separator
> - Establish field name conventions and stick to them
> - Use brackets `[key:: value]` for tasks/lists
> - Keep fields outside fenced code blocks

> [!constraints-and-pitfalls]
> **Issue #2: Unexpected data types**
> 
> **Causes:**
> - Date format not recognized (e.g., "Nov 23, 2025")
> - Numbers with currency symbols ($50)
> - Boolean values as text ("yes" instead of `true`)
> 
> **Solution:**
> - Use ISO 8601 dates: `2025-11-23`
> - Store pure numbers without symbols
> - Use explicit `true`/`false` for booleans
> - Test with DataviewJS: `dv.span(typeof dv.current().fieldname)`

> [!constraints-and-pitfalls]
> **Issue #3: Spaces in field names causing query errors**
> 
> **Causes:**
> - Field name contains spaces: `Project Status:: Active`
> - Query uses spaced name directly: `WHERE Project Status = "Active"`
> 
> **Solution:**
> - Use sanitized name: `WHERE project-status = "Active"`
> - Or row syntax: `WHERE row["Project Status"] = "Active"`
> - Prefer hyphenated names from the start

> [!warning]
> **Performance considerations:**
> 
> - Dataview indexes inline fields automatically, but in vaults with hundreds of thousands of notes, excessive inline field usage can impact indexing speed
> - Balance inline field density with query performance needs
> - Consider using frontmatter for static, note-level metadata
> - Reserve inline fields for contextual, dynamic data

> [!constraints-and-pitfalls]
> **Issue #4: Task inline fields not accessible**
> 
> **Cause:**
> Task metadata exists within `file.tasks` object, not at page level
> 
> **Solution:**
> ```dataview
> TABLE text, due, priority
> FROM "Projects"
> FLATTEN file.tasks AS task
> WHERE !task.completed AND task.priority = "high"
> ```

---

## 🎓 Learning Path & Resources

> [!helpful-tip]
> **Master inline fields progressively:**
> 
> **Level 1: Fundamentals**
> 1. Practice basic `Key:: Value` syntax in standalone notes
> 2. Experiment with all three syntax variations (standard, bracketed, parenthesis)
> 3. Create simple LIST queries accessing single fields
> 
> **Level 2: Integration**
> 4. Mix inline fields with [[YAML Frontmatter]]
> 5. Add fields to tasks and query with TASK command
> 6. Build TABLE queries with multiple field columns
> 
> **Level 3: Advanced Applications**
> 7. Use aggregation functions (sum, average, count)
> 8. Combine multiple conditions in WHERE clauses
> 9. Create DataviewJS queries for complex field operations
> 
> **Level 4: System Design**
> 10. Establish vault-wide field naming conventions
> 11. Create [[Templater]] templates with field structures
> 12. Build dashboard notes aggregating data across vault

> [!important-links]
> **Official Dataview Documentation:**
> - [Adding Metadata - Dataview](https://blacksmithgu.github.io/obsidian-dataview/annotation/add-metadata/)
> - [Dataview Query Language Reference](https://blacksmithgu.github.io/obsidian-dataview/queries/structure/)
> - [Dataview Example Vault](https://s-blu.github.io/obsidian_dataview_example_vault/)

---

# 🔗 Related Topics for PKB Expansion

1. **[[YAML Frontmatter in Obsidian]]**
   - *Connection*: Complementary metadata system to inline fields; understanding both enables optimal metadata architecture
   - *Depth Potential*: Covers frontmatter syntax, advanced YAML features, nesting, and when to choose frontmatter vs inline fields
   - *Knowledge Graph Role*: Foundation for [[Metadata Management]] strategy; prerequisite for comprehensive [[Dataview Plugin]] mastery

2. **[[Dataview Query Language (DQL)]]**
   - *Connection*: The query system that makes inline fields useful; without DQL knowledge, inline fields remain dormant data
   - *Depth Potential*: Complete coverage of query types (TABLE, LIST, TASK, CALENDAR), data commands (FROM, WHERE, SORT, GROUP BY), functions, and operators
   - *Knowledge Graph Role*: Core skill in [[03-notes/01_permanent-notes/02_personal-knowledge-base/Personal Knowledge Management]] automation; enables creation of dynamic dashboards and knowledge aggregation systems

3. **[[DataviewJS for Advanced Queries]]**
   - *Connection*: Unlocks programmatic access to inline field data for complex operations beyond DQL capabilities
   - *Depth Potential*: JavaScript API reference, custom rendering, advanced filtering algorithms, bulk operations, and integration with other plugins
   - *Knowledge Graph Role*: Advanced tier in [[Obsidian Automation]]; enables custom PKB features and sophisticated data transformations

4. **[[Metadata Architecture for Personal Knowledge Bases]]**
   - *Connection*: Strategic framework for designing consistent, scalable metadata systems using inline fields and frontmatter
   - *Depth Potential*: Field taxonomy design, naming conventions, standardization protocols, version control, and migration strategies for evolving systems
   - *Knowledge Graph Role*: Meta-level knowledge work; essential for [[PKB System Design]] and long-term maintainability of knowledge infrastructure


