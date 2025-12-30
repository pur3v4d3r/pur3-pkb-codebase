---
title: "Dataview: Comprehensive Reference"
id: 20251114-020650
type: reference
status: seedling
rating: ""
source: ""
url: ""
tags:
  - year/2025
  - pkm/workflow
  - pkb/architecture
  - pkb/design/information-architecture
  - pkb/design/discoverability
  - pkb/design/scalability
  - pkb/maintenance/refactoring
  - pkb/optimization/search
  - pkb/optimization/workflows
  - knowledge-workflow
  - obsidian/plugins/dataview
  - information-architecture/navigation/indexes
aliases:
  - Dataview Plugin
  - DQL
  - Dataview Query Language
  - Obsidian Dataview
  - DataviewJS
link-up: []
link-related: []
---
> [!info] 🏷️ Context Badges
> **Type**:: `= "<span style='background-color: #4a6fa5; padding: 2px 6px; border-radius: 4px; color: white; font-size: 0.8em;'>" + choice(this.type, this.type, "Unclassified") + "</span>"`
> **Folder**:: `= "<span style='background-color: #333; padding: 2px 6px; border-radius: 4px; color: #aaa; font-size: 0.8em;'>" + this.file.folder + "</span>"`

---

aliases: [Dataview Plugin, DQL, Dataview Query Language, Obsidian Dataview, DataviewJS]
---

> [!comprehensive-reference] 📚 Comprehensive-Reference
> - **Generated**: 2024-11-14
> - **Version**: 1.0
> - **Type**: Reference Documentation

> [!abstract]
> **Executive Overview**
> Dataview is a live index and query engine over your personal knowledge base that allows you to add metadata to notes and query them with the Dataview Query Language to list, filter, sort or group data. This comprehensive reference covers all three query methods ([[dql]], [[Inline Queries]], and [[DataviewJS]]), metadata architecture design, systematic query construction processes, operator/function specifications, and an extensive pattern library for building sophisticated vault automation.

> [!how-to-use-this]
> **Navigation Guide**
> This reference note is organized into 9 major sections covering all aspects of Dataview query development. Use the table of contents below for quick navigation, or search for specific terms using wiki-links. Each section builds progressively from foundational concepts through advanced implementation patterns.

## 📑 Table of Contents

1. [[#⚙️ Dataview Plugin Overview & Core Architecture]]
2. [[#🗣️ Query Language Taxonomy Three Paradigms]]
3. [[#📐 DQL Query Syntax & Structure]]
4. [[#🏗️ Metadata Architecture & Field Design]]
5. [[#🔨 Systematic Query Construction Process]]
6. [[#🧮 Operator Function & Expression Reference]]
7. [[#📚 Query Pattern Library Comprehensive Examples]]
8. [[#🚀 Advanced Techniques & Optimization]]
9. [[#🔧 Troubleshooting & Best Practices]]

---

## ⚙️ Dataview Plugin Overview & Core Architecture

> [!definition]
> - **Dataview**: A [[Community Plugin]] for [[obsidian]] that treats your vault as a queryable database
> - **Core Function**: Live index and query engine that keeps queries always up to date and makes data aggregation a breeze
> - **Primary Use Case**: Automated views, dashboards, and data aggregation without manual maintenance

### Foundational Understanding

Dataview operates on metadata in your Markdown files through data indexing and data querying. The plugin creates a real-time index of specific types of information in your vault, making that data available for sophisticated queries. Unlike traditional search functionality, Dataview enables structured data extraction, transformation, and presentation through three distinct query paradigms.

The plugin's architecture centers on two building blocks: **Data Indexing** (what information Dataview can "see") and **Data Querying** (how you retrieve and manipulate that information). Understanding this distinction is critical—Dataview cannot query arbitrary text content within your notes, but only specifically indexed data types.

Dataview indexes certain information like tags and list items and the data you add via fields. This includes [[YAML Frontmatter]], [[Inline Fields]], [[04_library/02_pkb-and-pkm-learning/_reference/_official-documentation/_plugin-tasks/_getting started/Tags]], [[project-pur3v4d3r-20251121013128]], [[Bullet Lists]], and implicit [[File Metadata]]. The indexing happens automatically and continuously as you work, ensuring query results remain current without manual intervention.

> [!key-claim]
> **Central Principle**
> Dataview transforms your Obsidian vault from a collection of notes into a queryable knowledge database by indexing structured metadata and providing three progressively powerful query interfaces: [[dql]] for SQL-like queries, [[Inline Queries]] for embedded values, and [[DataviewJS]] for full JavaScript control.

### Plugin Capabilities & Limitations

**What Dataview Can Do:**
- Query pages by folder, tag, link relationships, or metadata fields
- Create dynamic tables, lists, task collections, and calendar views
- Perform calculations and data transformations
- Sort, filter, group, and flatten multi-value fields
- Generate always-updated dashboards and [[MOC]]s
- Scale to hundreds of thousands of annotated notes without issue

**What Dataview Cannot Do:**
- Search the actual contents of your notes—only indexed metadata is queryable
- Modify note content (except task completion status in TASK queries)
- Query unstructured narrative text
- Access data that hasn't been explicitly added as metadata

> [!warning]
> **Critical Constraint**
> Dataview only operates on **indexed data**. If information isn't stored as frontmatter, inline fields, tags, tasks, or implicit file metadata, it cannot be queried. This requires intentional metadata design as part of your [[PKM]] workflow.

### Use Case Categories

| Use Case Category | Example Applications | Query Type |
|------------------|---------------------|------------|
| **Task Management** | Aggregate incomplete tasks across vault, filter by due date, create project-specific task views | [[TASK Query]] |
| **Content Dashboards** | Book libraries with ratings, research paper collections, recipe databases | [[TABLE Query]] |
| **Temporal Views** | Daily note creation trackers, [[Calendar Views]], deadline monitoring | [[CALENDAR Query]] |
| **Relationship Mapping** | Pages linking to/from specific notes, [[Backlink]] analysis, [[Knowledge Graph]] exploration | [[from]] sources with [[Link Queries]] |
| **Progress Tracking** | Reading lists, habit tracking, project completion percentages | [[TABLE Query]] with calculations |
| **Dynamic MOCs** | Auto-generating [[Map of Content]] pages based on tags or folder structure | [[LIST Query]] with [[GROUP BY]] |

---

## 🗣️ Query Language Taxonomy: Three Paradigms

> [!principle-point]
> **Fundamental Design Philosophy**
>   provides three query methods with escalating power and complexity: [[dql]] for declarative SQL-like queries, [[Inline Queries]] for embedded single values, and [[DataviewJS]] for programmatic JavaScript control. Choose based on your technical proficiency and query complexity requirements.

### 1. Dataview Query Language (DQL)

> [!definition]
> - **DQL**: A SQL-like language and Dataview's core functionality supporting four Query Types, data commands to refine/resort/group results, and plentiful functions
> - **Syntax Pattern**: Query Type + optional data commands (FROM, WHERE, SORT, etc.)
> - **Technical Level**: Beginner to intermediate—requires no programming knowledge

**DQL Query Structure:**
``` 
<QUERY-TYPE> [fields]
FROM <source>
WHERE <condition>
SORT <field> [ASC|DESC]
GROUP BY <field>
FLATTEN <field>
LIMIT <number>
```

The Query Type is the only mandatory command in a query—everything else is optional. DQL excels at straightforward data aggregation tasks and is the recommended starting point for Dataview users.

**Key Characteristics:**
- Declarative syntax (describe *what* you want, not *how* to get it)
- Four output formats: TABLE, LIST, TASK, CALENDAR
- Cannot be confused with SQL—DQL differs significantly despite superficial similarities
- Executes at page level (except TASK queries which operate at task level)
- Limited to built-in functions and operators

> [!example]
> **Basic DQL Query**
> ``` 
> TABLE rating AS "Rating", summary AS "Summary"
> FROM #games
> WHERE rating >= 7
> SORT rating DESC
> ```
> This creates a table of game notes with ratings ≥7, sorted by rating descending.

### 2. Inline DQL Queries

> [!definition]
> - **Inline Query**: Uses inline block format with configurable prefix to mark inline code blocks as DQL blocks
> - **Default Syntax**: `` `= expression` ``
> - **Output**: Always displays exactly **one value** (not lists or tables)

**Inline Query Architecture:**

Inline DQL queries display exactly one value somewhere in the middle of your note, seamlessly blending into content. These are ideal for dynamically embedding computed values within narrative text, headers, or metadata fields.

**Syntax Examples:**
```markdown
Today is `= date(today)`
Days until exam: `= [[Exam Date]].deadline - date(today)`
This note was created: `= this.file.ctime`
Page count: `= length(file.inlinks)` backlinks
```

**Access Patterns:**
- Current page: `this.field` or `this.file.property`
- Linked pages: `[[Page Name]].field`
- All expressions and functions available
- Configurable prefix in settings (default `=``)
`
> [!helpful-tip]
> **When to Use Inline Queries**
> Use inline queries for single-value embeddings like counters, date calculations, or property references. For multi-item displays (lists, tables), use standard DQL code blocks instead.

### 3. DataviewJS

> [!definition]
> - **DataviewJS**: A high-powered JavaScript API giving full access to the Dataview index and rendering utilities
> - **Syntax**: ` ``` js ` code block with access to `dv` variable
> - **Technical Level**: Advanced—requires JavaScript programming knowledge

**DataviewJS Architecture:**

DataviewJS provides the full power of [[JavaScript]] combined with Dataview's indexing system. JavaScript queries run at the same level of access as any other Obsidian plugin, meaning they can potentially rewrite, create, or delete files and make network calls.

**Core API Methods:**

| Method | Purpose | Example |
|--------|---------|---------|
| `dv.pages(source)` | Query pages matching source | `dv.pages("#book")` |
| `dv.table(headers, rows)` | Render table | `dv.table(["Name", "Rating"], data)` |
| `dv.list(items)` | Render bullet list | `dv.list(pages.file.link)` |
| `dv.taskList(tasks)` | Render task list | `dv.taskList(pages.file.tasks)` |
| `dv.current()` | Get current page metadata | `dv.current().file.name` |
| `dv.page(path)` | Get specific page metadata | `dv.page("Notes/Example")` |

**When to Use DataviewJS:**
- Complex data transformations requiring loops or conditionals
- Custom formatting beyond DQL capabilities
- Dynamic heading generation with `dv.header()`
- Integration with other JavaScript-based functionality
- Multi-stage data processing pipelines

> [!example]
> **DataviewJS with Grouping**
> ``` js
> for (let group of dv.pages("#book").groupBy(p => p.genre)) {
>     dv.header(3, group.key);
>     dv.table(["Title", "Rating"], 
>         group.rows.sort(k => k.rating, 'desc')
>         .map(k => [k.file.link, k.rating])
>     );
> }
> ```
> Creates a heading for each book genre with a sorted table of books beneath it.

### Comparison Matrix

| Feature | DQL | Inline DQL | DataviewJS |
|---------|-----|------------|------------|
| **Learning Curve** | Low | Low | High |
| **Power/Flexibility** | Medium | Low | Very High |
| **Output Types** | 4 types (TABLE, LIST, TASK, CALENDAR) | Single value only | Unlimited |
| **Requires Programming** | No | No | Yes (JavaScript) |
| **Can Modify Files** | Only task completion | No | Yes (full access) |
| **Best For** | Standard queries, dashboards | Embedded calculations | Complex logic, custom views |
| **Performance** | Fast | Fastest | Moderate |

---

## 📐 DQL Query Syntax & Structure

> [!methodology-and-sources]
> **Query Construction Framework**
> Every DQL query follows a consistent structure with Query Type as the only mandatory component, followed by optional data commands that refine results. This section provides systematic specification of each query component.

### Query Type Specifications

#### TABLE Query

> [!definition]
> - **Function**: Outputs page data as tabular view with zero to multiple metadata fields as columns
> - **Syntax**: `TABLE field1, field2, … FROM source`
> - **Column Headers**: Use `AS "Header Name"` to rename columns

**TABLE Syntax Patterns:**
``` 
TABLE                           # Just file links (minimal)
TABLE field1, field2            # Multiple columns
TABLE field AS "Custom Name"   # Renamed column
TABLE WITHOUT ID field1, field2 # Hide first column
```

**Behavior Notes:**
- Default first column is "File" (or "Group" when using GROUP BY)
- First column name can be changed in Dataview Settings under Table Settings
- Calculations supported: `TABLE (field1 + field2) AS "Total"`
- Multiple rows per page possible with [[flatten]]

> [!example]
> **TABLE with Calculations**
> ``` 
> TABLE 
>     pagesRead, 
>     totalPages, 
>     round((pagesRead/totalPages)*100) AS "Progress %"
> FROM #reading
> WHERE status = "in-progress"
> SORT "Progress %" DESC
> ```

#### LIST Query

> [!definition]
> - **Function**: Outputs bullet point list consisting of file links or group names
> - **Syntax**: `LIST [additional_info] FROM source`
> - **Output**: Bullet list with optional additional information per item

**LIST Syntax Patterns:**
``` 
LIST                                    # Just file links
LIST field                              # Link + one field value
LIST "Text: " + field + " (" + f2 + ")" # Computed expression
LIST WITHOUT ID expression             # Hide file link entirely
```

LIST WITHOUT ID can be handy for outputting computed values, for example when showing aggregated group statistics.

> [!example]
> **LIST with Computed Output**
> ``` 
> LIST "Created: " + file.cday + " | Links: " + length(file.inlinks)
> FROM "Projects"
> WHERE status = "active"
> ```

#### TASK Query

> [!definition]
> - **Function**: Outputs interactive list of tasks that match given data commands
> - **Unique Property**: TASK Queries are the only command in dataview that modifies original files if interacted with
> - **Execution Level**: Task level (not page level)

**TASK Behavioral Characteristics:**

Child tasks belong to their parent, meaning if you're querying for tasks, you'll get child tasks as part of their parent back. This means child tasks appear in results if their parent matches the query, even if the child itself doesn't match.

**TASK Syntax:**
``` 
TASK
FROM source
WHERE condition
GROUP BY field
SORT field
```

**Task-Specific Filtering:**
``` 
TASK WHERE !completed                    # Incomplete tasks
TASK WHERE !completed AND due < date(today)  # Overdue tasks
TASK WHERE contains(tags, "#priority")   # Tasks with specific tag
TASK WHERE text                          # Tasks with any text
```

> [!warning]
> **Task Modification Behavior**
> If you check a task through a dataview query, it'll get checked in its original file too. In Dataview Settings under "Task Settings", you can enable automatic completion date metadata when checking tasks.

#### CALENDAR Query

> [!definition]
> - **Function**: Outputs monthly-based calendar where every result is depicted as a dot on its referred date
> - **Required Field**: Must specify a date field to display
> - **Syntax**: `CALENDAR date_field`

**CALENDAR Syntax:**
``` 
CALENDAR file.cday        # Creation date
CALENDAR file.mday        # Modification date
CALENDAR due              # Custom date field
CALENDAR published        # Publication date
```

The calendar view automatically groups by month and shows dots on days where matching pages exist.

---

### Data Commands Deep Dive

#### FROM Command

> [!definition]
> - **Purpose**: Determines what pages will initially be collected and passed to other commands for further filtering
> - **Position**: Must come immediately after Query Type (if used)
> - **Composability**: Can combine sources with AND, OR, and negation (-)

**FROM Source Types:**

| Source Type | Syntax | Description |
|------------|--------|-------------|
| **Tag** | `FROM #tag` | All pages with tag (and its subtags) |
| **Folder** | `FROM "folder"` | All pages in folder (and subfolders) |
| **Single File** | `FROM "path/to/file"` | One specific file |
| **Incoming Links** | `FROM [[note]]` | All pages which link TO the note |
| **Outgoing Links** | `FROM outgoing([[note]])` | All pages which link FROM the note |

**Source Composition:**

You can compose these filters using AND and OR operators. Parentheses control logical order:

``` 
FROM #tag AND "folder"                           # Both conditions
FROM [[Food]] OR [[Exercise]]                    # Either link
FROM (#project AND "Work") OR "Archive/Projects" # Complex logic
FROM #active AND -"Archive"                      # Negation
FROM #assignment AND -#completed                 # Tag negation
```

> [!example]
> **Complex FROM Patterns**
> ``` 
> LIST
> FROM (#development AND "Projects") 
>      OR ("Archive" AND outgoing([[Current Sprint]]))
> WHERE status != "cancelled"
> ```
> Finds development projects OR archived items linked from Current Sprint page.

#### WHERE Command

> [!definition]
> - **Purpose**: Filter pages on fields—only pages where clause evaluates to true will be yielded
> - **Multiple Use**: Can use WHERE multiple times in single query
> - **Execution**: Filters applied in written order

**WHERE Operators:**

| Operator | Purpose | Example |
|----------|---------|---------|
| `=` | Equality | `WHERE rating = 5` |
| `!=` | Inequality | `WHERE status != "done"` |
| `>`, `>=` | Greater than (or equal) | `WHERE price > 100` |
| `<`, `<=` | Less than (or equal) | `WHERE due <= date(today)` |
| `AND` | Logical conjunction | `WHERE tag AND active` |
| `OR` | Logical disjunction | `WHERE #urgent OR #important` |
| `!` | Negation | `WHERE !completed` |
| `contains()` | Substring/list membership | `WHERE contains(title, "Data")` |

**WHERE Best Practices:**

``` 
# Type checking to avoid null comparison issues
WHERE typeof(due) = "date" AND due < date(today)

# Field existence check
WHERE due AND due < date(today)

# Array membership
WHERE contains(tags, "#project")

# String operations
WHERE contains(file.name, "2024")

# Complex boolean logic
WHERE (status = "active" OR status = "pending") 
      AND priority >= 3
```

> [!warning]
> **Null Comparison Gotcha**
> If a field is not set, it is null and null <= date(today) returns true. Always check field existence with `WHERE field AND condition` or use typeof() for type safety.

#### SORT Command

> [!definition]
> - **Purpose**: Sorts all results by one or more fields
> - **Direction**: ASC (ascending) or DESC (descending)
> - **Tie-Breaking**: Multiple sort fields resolve ties in order

**SORT Syntax:**
``` 
SORT field [ASC|DESC]
SORT field1 ASC, field2 DESC, field3 ASC
```

**Common Sort Patterns:**

``` 
SORT file.ctime DESC           # Newest files first
SORT rating DESC, title ASC    # By rating, then alphabetically
SORT file.mtime                # Modified date (ASC implicit)
SORT length(file.inlinks) DESC # Most linked pages first
```

**Sort Order Notes:**
- Commands are processed in order they are written, so sorting after LIMIT affects different results than before
- Default sort is ASC if direction unspecified
- Can sort by calculated values: `SORT (end - start) DESC`

> [!example]
> **Multi-Level Sorting**
> ``` 
> TABLE status, priority, due
> FROM "Projects"
> SORT status ASC, priority DESC, due ASC
> ```
> Orders by status alphabetically, then priority high-to-low within each status, then by due date within each priority.

#### GROUP BY Command

> [!definition]
> - **Purpose**: Group all results on a field, yielding one row per unique field value with a rows array containing all matched pages
> - **Result Structure**: `{key: grouped_value, rows: [matching_pages]}`
> - **Field Swizzling**: rows.field automatically fetches field from every object in rows

**GROUP BY Fundamentals:**

After grouping, your result structure changes fundamentally. Before GROUP BY, each page is a result row. After GROUP BY, each unique group value becomes a row, with original pages nested in the `rows` array.

**GROUP BY Syntax:**
``` 
GROUP BY field
GROUP BY (calculated_field) AS name
```

**Accessing Grouped Data:**

``` 
# Display group key and count
LIST length(rows) + " items"
GROUP BY status

# Access fields from grouped pages
TABLE rows.file.link, rows.rating
GROUP BY genre

# Aggregate calculations
TABLE sum(rows.pages) AS "Total Pages"
FROM #books
GROUP BY author
```

**Field Swizzling Example:**

If you want the field test from every object in the rows array, rows.test will automatically fetch test from every object in rows, yielding a new array. You can then apply aggregation operators like `sum()`, `average()`, or `length()`.

> [!example]
> **GROUP BY with Calculations**
> ``` 
> TABLE WITHOUT ID
>     key AS "Genre",
>     length(rows) AS "Count",
>     average(rows.rating) AS "Avg Rating",
>     rows.file.link AS "Books"
> FROM #book
> GROUP BY genre
> SORT average(rows.rating) DESC
> ```

**GROUP BY with Multi-Value Fields:**

If a page matches multiple groups, dataview will duplicate the page to put it in every matching group. To properly group by multi-value fields (like lists of tags), first [[flatten]] the field:

``` 
TABLE rows.file.link
FROM "Books"
FLATTEN genres
GROUP BY genres
```

#### FLATTEN Command

> [!definition]
> - **Purpose**: Flatten an array in every row, yielding one result row per entry in the array
> - **Effect**: Splits multi-value fields into individual rows
> - **Naming**: Can assign flattened values to new field names

**FLATTEN Fundamentals:**

FLATTEN is the opposite of GROUP BY—instead of putting multiple notes into one row, it potentially splits one note into multiple rows. If querying 7 notes and flattening a field with 3 values per note, you get 21 result rows.

**FLATTEN Syntax:**
``` 
FLATTEN field
FLATTEN (calculated_field) AS name
FLATTEN field AS alias
```

**FLATTEN Use Cases:**

``` 
# Make list elements individually filterable
TABLE L.text AS "Task"
FROM "Daily Notes"
FLATTEN file.lists AS L
WHERE contains(L.text, "urgent")

# Create computed temporary fields
TABLE progress AS "Completion %"
FROM #projects
FLATTEN round((completed/total)*100) AS progress
WHERE progress >= 50

# Group by flattened multi-value field
TABLE rows.file.link
FROM #media
FLATTEN genres
GROUP BY genres
```

**FLATTEN Behavioral Notes:**

- FLATTEN works only correctly on lists or single values
- Order matters—a flattened field is only available after the FLATTEN command
- Can FLATTEN multiple times: results multiply (file count × field1 values × field2 values)
- Functions requiring single values need FLATTEN first

> [!example]
> **FLATTEN for Function Access**
> ``` 
> TABLE L.text
> FROM "Meeting Notes"
> FLATTEN file.lists AS L
> WHERE meta(L.section).subpath = "Action Items"
>       AND !contains(L.text, "DONE")
> ```
> FLATTEN makes it easier to operate on nested lists with simpler WHERE conditions versus using filter() functions.

#### LIMIT Command

> [!definition]
> - **Purpose**: Restrict results to at most N values
> - **Execution Order**: Applied when encountered in command sequence
> - **Common Pattern**: SORT then LIMIT for "top N" queries

**LIMIT Syntax:**
``` 
LIMIT number
```

**LIMIT Timing Examples:**

``` 
# Get 10 newest files
LIST FROM #notes
SORT file.ctime DESC
LIMIT 10

# WRONG: This limits first, THEN sorts the 10 results
LIST FROM #notes
LIMIT 10
SORT file.ctime DESC
```

Commands are processed in order written, so SORT after LIMIT affects already-limited results.

> [!helpful-tip]
> **Performance Optimization**
> Use LIMIT with large vaults to prevent slow queries. Example: `LIMIT 100` on TABLE queries returns results faster when you don't need every matching page.

---

## 🏗️ Metadata Architecture & Field Design

> [!principle-point]
> **Metadata Design Philosophy**
>   cannot query all content of your vault—content needs to be indexed through metadata fields to be searchable. Effective Dataview usage requires intentional metadata architecture designed into your [[PKM]] workflow.

### Metadata Addition Methods

#### YAML Frontmatter

> [!definition]
> - **Format**: Common Markdown extension allowing YAML metadata at top of page, natively supported by Obsidian
> - **Scope**: Page-level metadata only (not task/list-specific)
> - **Syntax**: Enclosed by `---` markers at document start

**Frontmatter Structure:**
```yaml
---
title: "Document Title"
status: active
priority: 3
tags: [project, development]
created: 2024-11-14
author: "[[Person Name]]"
metadata:
  nested: value
  properties: work
---
```

**Frontmatter Field Types:**

| YAML Type | Dataview Interpretation | Example |
|-----------|------------------------|---------|
| String | Text | `title: "My Note"` |
| Number | Number | `priority: 5` |
| Boolean | Boolean | `completed: true` |
| Date (ISO8601) | Date | `due: 2024-11-20` |
| Array/List | List | `tags: [a, b, c]` |
| Object | Object (nested fields) | `meta: {key: value}` |
| Link | Link | `parent: "[[Note]]"` |

**Frontmatter Best Practices:**

If you reference a link in frontmatter, you need to quote it as "[[link]]"—unquoted links lead to invalid YAML. Additionally, quoted links are only recognized by Dataview, not Obsidian (won't show in graph or update on rename).

```yaml
# ✅ GOOD - Quoted link
parent: "[[Parent Page]]"

# ❌ BAD - Unquoted (breaks YAML parsing)
parent: [[Parent Page]]

# Date formats (auto-recognized as dates)
created: 2024-11-14
due: 2024-11-20T15:30:00
published: 2024-11

# Lists - two formats
tags: [tag1, tag2, tag3]
topics:
  - topic1
  - topic2
  - topic3
```

#### Inline Fields

> [!definition]
> - **Format**: Key:: Value syntax usable everywhere in file for natural-looking annotation
> - **Scope**: Page-level by default; task/list-specific with bracket syntax
> - **Visibility**: Displayed in Reading mode (can be hidden with parenthesis syntax)

**Inline Field Syntax Patterns:**

```markdown
# Standalone line format
Basic Field:: Some Value
**Bold Field**:: Emphasized Value
Rating:: 8

# Embedded in sentences (bracket syntax)
I would rate this [rating:: 9]! It was [mood:: acceptable].

# Hidden key (parenthesis syntax)
This will not show the (hidden_key:: key) in Reading mode.

# Multiple fields on same line
Published [date:: 2024-11-14] by [author:: John Smith]

# Task/list-specific metadata (MUST use brackets)
- [ ] Send email to David [due:: 2024-04-05] [priority:: high]
- Read chapter 3 [pages:: 45-67] [time:: 30min]
```

**Inline Field Processing:**

If using spaces or capitalized letters in metadata key names, dataview provides a sanitized version that is always lowercase with dashes instead of spaces:

| Original Key | Sanitized Key | Query Usage |
|-------------|---------------|-------------|
| `Some Metadata` | `some-metadata` | `WHERE some-metadata` |
| `ComplexKey` | `complexkey` | `WHERE complexkey` |
| `my_field` | `my_field` | `WHERE my_field` |

For keys with spaces, either use sanitized name or the `row` syntax:
```
WHERE row["Some Metadata"] = value
# OR
WHERE some-metadata = value
```

> [!warning]
> **Inline Field Syntax Requirements**
> Note you need double colon `::` between key and value when using inline fields, contrary to YAML Frontmatter fields where one colon is enough.

#### Implicit Fields (Automatic Metadata)

> [!definition]
> - **Source**: Dataview automatically adds large amount of metadata to each page collected under the file field
> - **Scope**: Always available without manual addition
> - **Access Pattern**: `file.property` or just `property` in queries

**File Metadata Reference:**

| Field | Type | Description |
|-------|------|-------------|
| `file.name` | Text | File name without extension |
| `file.folder` | Text | Folder path containing file |
| `file.path` | Text | Full file path including extension |
| `file.link` | Link | Link object to the file |
| `file.size` | Number | File size in bytes |
| `file.ctime` | Date | File creation time |
| `file.cday` | Date | File creation date (time stripped) |
| `file.mtime` | Date | File last modification time |
| `file.mday` | Date | File last modification date |
| `file.tags` | List | All tags in file (including nested) |
| `file.etags` | List | Explicit tags only |
| `file.inlinks` | List | Pages linking TO this file |
| `file.outlinks` | List | Pages linked FROM this file |
| `file.aliases` | List | All aliases defined |
| `file.tasks` | List | All tasks in file |
| `file.lists` | List | All list items |
| `file.frontmatter` | Object | Raw frontmatter object |

**Date Property Access:**

For date fields, you can access properties that give you a certain portion of your date back:

```
# Date component access
WHERE file.ctime.year = 2024
WHERE file.ctime.month = 11
WHERE file.ctime.day = 14
WHERE birthday.month = date(now).month  # Birthday this month
```

---

### Data Types Deep Dive

#### Text (String)

```markdown
# Frontmatter
title: "Simple text"
description: 'Also text'

# Inline
Author:: John Smith
Notes:: This is a longer text field
```

**Text Operations:**
- `contains(text, substring)` - Check for substring
- `lower(text)` / `upper(text)` - Case conversion
- `split(text, delimiter)` - Split into array
- `regexmatch(pattern, text)` - Pattern matching

#### Number

```markdown
# Frontmatter
rating: 8
pages: 342
price: 29.99

# Inline
Priority:: 5
Score:: 87.5
```

**Numeric Operations:**
- Standard math: `+`, `-`, `*`, `/`, `%`
- `round(number, decimals)` - Rounding
- Comparisons: `>`, `<`, `>=`, `<=`, `=`, `!=`

#### Boolean

```markdown
# Frontmatter
completed: true
published: false
active: true

# Inline
Done:: true
Archived:: false
```

**Boolean Usage:**
```
WHERE completed = true   # Explicit comparison
WHERE completed          # Truthy check
WHERE !completed         # Negation
```

#### Date and Duration

> [!definition]
> - **Date Format**: Text matching ISO8601 notation (YYYY-MM[-DDTHH:mm:ss.nnn+ZZ]) automatically transformed into date object
> - **Duration Format**: `dur(quantity unit)` - e.g., `dur(1 day)`, `dur(3 hours)`

**Date Examples:**
```markdown
# Frontmatter - various precision levels
date: 2024-11              # Month precision
date: 2024-11-14           # Day precision
date: 2024-11-14T15:30:00  # Full timestamp
date: 2024-11-14T15:30:00.000+00:00  # With timezone

# Inline
Deadline:: 2024-12-01
Published:: 2024-11-14T10:00:00
```

**Date Functions:**
```
date(today)              # Today's date
date(now)                # Current timestamp
date(2024-11-14)         # Specific date
dateformat(date, format) # Format date string
striptime(datetime)      # Remove time component
```

**Duration Examples:**
```markdown
Duration:: 2 hours 30 minutes
Time:: 45 min
Length:: 3 days
```

**Duration Functions:**
```
dur(2 hours)                    # Create duration
due - date(today)               # Days until due
end - start - dur(8 hours)      # Calculate overtime
```

#### Link

> [!definition]
> - **Format**: `[[Page Name]]` or `[[Page Name|Display Text]]`
> - **Indexing**: Index through a link to get values on corresponding page via [[link]].field syntax

**Link Usage Patterns:**
```
# Link in frontmatter (MUST be quoted)
parent: "[[Parent Page]]"

# Inline field
Related:: [[Related Note]]

# Query with link indexing
WHERE [[Assignment Math]].due < date(today)
TABLE parent.status, [[Project]].priority
```

**Link Functions:**
```
link(path)                  # Create link object
link(path, display)         # Link with custom text
meta(link)                  # Get metadata about linked page
```

#### List (Array)

> [!definition]
> - **Frontmatter**: Defined as normal YAML lists
> - **Inline**: Comma-separated values (text must be quoted)
> - **Duplicate Keys**: Duplicated metadata keys in same file lead to lists

**List Syntax:**
```yaml
# Frontmatter - array notation
tags: [fiction, scifi, award-winning]

# Frontmatter - list notation
authors:
  - Author One
  - Author Two
  - Author Three
```

```markdown
# Inline (text values MUST be quoted)
Tags:: "fiction", "scifi", "award-winning"
Numbers:: 1, 2, 3, 5, 8, 13

# Duplicate keys create list
grocery:: flour
grocery:: eggs
grocery:: milk
# Results in grocery = [flour, eggs, milk]
```

**List Operations:**
```
length(list)              # Count elements
contains(list, item)      # Check membership
filter(list, predicate)   # Filter elements
map(list, function)       # Transform elements
sort(list)                # Sort list
flat(list)                # Flatten nested lists
```

#### Object

> [!definition]
> - **Format**: Only definable in YAML frontmatter using YAML object syntax
> - **Access**: `object.field` or `object.nested.field`

**Object Syntax:**
```yaml
---
metadata:
  status: active
  priority: high
  owner: "John Smith"
  
appointment:
  date: 2024-11-20
  time: "14:00"
  location: "Conference Room B"
  attendees:
    - Alice
    - Bob
    - Charlie
---
```

**Object Access in Queries:**
```
TABLE 
    metadata.status,
    metadata.priority,
    appointment.date,
    appointment.location
WHERE metadata.status = "active"
```

---

### Metadata Schema Design Patterns

> [!methodology-and-sources]
> **Schema Design Framework**
> Effective Dataview usage requires consistent metadata schemas across note types. Design schemas based on note categories (e.g., books, projects, people) with standardized field names and data types.

#### Project Note Schema Example

```yaml
---
type: project
status: active           # active | planning | complete | archived
priority: 2              # 1-5 scale
start_date: 2024-10-01
due_date: 2024-12-15
owner: "[[John Smith]]"
team:
  - "[[Alice]]"
  - "[[Bob]]"
tags: [development, web]
progress: 65             # 0-100 percentage
---

# Inline fields in body
Last Updated:: 2024-11-14
Budget:: $50000
Risk Level:: medium
```

**Query Patterns for Projects:**
```
# Active projects by priority
TABLE status, priority, due_date, owner
FROM #project
WHERE status = "active"
SORT priority ASC, due_date ASC

# Projects by team member
TABLE rows.file.link, rows.status
FROM #project
FLATTEN team AS member
GROUP BY member

# Overdue projects
LIST progress + "% complete"
FROM #project
WHERE due_date < date(today) AND status != "complete"
```

#### Book Note Schema Example

```yaml
---
type: book
title: "Book Title"
author: "[[Author Name]]"
genre: [fiction, scifi]
rating: 8                # 1-10 scale
status: reading          # reading | completed | want-to-read
started: 2024-11-01
finished: 2024-11-14
pages: 342
tags: [books, fiction]
---

Thoughts:: Engaging plot with strong characters
Recommended By:: [[Friend Name]]
```

---

## 🔨 Systematic Query Construction Process

> [!methodology-and-sources]
> **IDEA Framework for Query Development**
> Follow this systematic four-phase approach: **I**dentify requirements, **D**esign query structure, **E**xecute and test, **A**nalyze and refine.

### Phase 1: Identify Requirements

> [!question]
> **Define Query Objectives**
> - What information do I need to display?
> - Which notes contain this information?
> - What filtering/sorting/grouping is required?
> - What output format best suits this data?

**Requirement Analysis Checklist:**
- [ ] Target note set identified (folder, tag, link pattern)
- [ ] Required metadata fields catalogued
- [ ] Filter conditions defined
- [ ] Sort order determined
- [ ] Grouping requirements specified
- [ ] Output format selected (TABLE, LIST, TASK, CALENDAR)

### Phase 2: Design Query Structure

> [!methodology-and-sources]
> **Progressive Query Building**
> Start minimal, add complexity incrementally, test at each stage.

**Query Construction Sequence:**

```
# Step 1: Query Type + Source
LIST FROM #projects

# Step 2: Add filtering
LIST FROM #projects
WHERE status = "active"

# Step 3: Add sorting
LIST FROM #projects
WHERE status = "active"
SORT priority ASC

# Step 4: Add field display
TABLE status, priority, due_date
FROM #projects
WHERE status = "active"
SORT priority ASC

# Step 5: Add calculations/transformations
TABLE 
    status, 
    priority, 
    due_date,
    due_date - date(today) AS "Days Remaining"
FROM #projects
WHERE status = "active"
SORT priority ASC
```

### Phase 3: Execute and Test

**Testing Methodology:**

1. **Syntax Validation**: Verify query runs without errors
2. **Result Verification**: Confirm expected notes appear
3. **Edge Case Testing**: Check behavior with missing fields, empty lists
4. **Performance Check**: Ensure acceptable execution time

**Common Testing Scenarios:**
```
# Test with no results
LIST FROM #nonexistent-tag

# Test with missing fields
TABLE field1, field2
WHERE field1  # Ensures field exists before display

# Test with null values
WHERE typeof(due) = "date" AND due < date(today)
```

### Phase 4: Analyze and Refine

**Optimization Considerations:**

- Can FROM be more specific to reduce search space?
- Are WHERE conditions ordered efficiently (most restrictive first)?
- Is LIMIT needed to improve performance?
- Can complex calculations be simplified?
- Would GROUP BY reduce result size?

**Refinement Example:**
```
# Initial query (slow with large vault)
TABLE file.inlinks
FROM ""

# Refined query (much faster)
TABLE length(file.inlinks) AS "Link Count"
FROM "Active Projects"
WHERE length(file.inlinks) > 5
SORT length(file.inlinks) DESC
LIMIT 20
```

---

## 🧮 Operator, Function & Expression Reference

> [!quick-reference]
> **Expression Categories**
> - **Literals**: Direct values (numbers, strings, dates, lists, objects)
> - **Operators**: Arithmetic, comparison, logical
> - **Functions**: Built-in data manipulation functions
> - **Lambdas**: Anonymous functions for advanced transformations

### Arithmetic Operators

| Operator | Operation | Example | Result |
|----------|-----------|---------|--------|
| `+` | Addition / Concatenation | `5 + 3` | `8` |
| `-` | Subtraction | `10 - 4` | `6` |
| `*` | Multiplication | `7 * 6` | `42` |
| `/` | Division | `15 / 3` | `5` |
| `%` | Modulo | `17 % 5` | `2` |

**Arithmetic Usage:**
```
TABLE 
    pages,
    hours,
    pages / hours AS "Pages per Hour",
    (end - start) - dur(8 hours) AS "Overtime"
FROM #work
```

### Comparison Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `=` | Equal to | `status = "active"` |
| `!=` | Not equal to | `rating != 0` |
| `>` | Greater than | `price > 100` |
| `>=` | Greater than or equal | `progress >= 50` |
| `<` | Less than | `age < 18` |
| `<=` | Less than or equal | `due <= date(today)` |

**Comparison Best Practices:**

Comparing different data types can lead to unexpected results. Always ensure type compatibility:

```
# ❌ WRONG - May include null values
WHERE due <= date(today)

# ✅ CORRECT - Type-safe comparison
WHERE typeof(due) = "date" AND due <= date(today)

# ✅ ALSO CORRECT - Existence check
WHERE due AND due <= date(today)
```

### Logical Operators

| Operator | Purpose | Example |
|----------|---------|---------|
| `AND` | Both conditions true | `active AND priority > 3` |
| `OR` | Either condition true | `#urgent OR #important` |
| `!` | Negation | `!completed` |

**Logical Combinations:**
```
WHERE (status = "active" OR status = "pending") 
      AND priority >= 3
      AND !archived
```

### Essential Functions

#### String Functions

```
contains(string, substring)      # Check if contains
lower(string)                    # Convert to lowercase
upper(string)                    # Convert to uppercase
split(string, delimiter)         # Split into array
replace(string, pattern, replacement)  # Replace text
regexmatch(pattern, string)      # Match regex pattern
```

#### List Functions

```
length(list)                     # Count elements
contains(list, element)          # Check membership
filter(list, (x) => condition)   # Filter by condition
map(list, (x) => transform)      # Transform elements
flat(list)                       # Flatten nested lists
sort(list)                       # Sort list
reverse(list)                    # Reverse order
slice(list, start, end)          # Extract subset
```

#### Aggregation Functions

```
sum(list)                        # Sum numeric values
average(list) / avg(list)        # Calculate average
min(list)                        # Find minimum
max(list)                        # Find maximum
```

**Aggregation Usage:**
```
TABLE 
    length(rows) AS "Count",
    sum(rows.pages) AS "Total Pages",
    average(rows.rating) AS "Avg Rating"
FROM #books
GROUP BY author
```

#### Date Functions

```
date(text)                       # Parse date
date(today)                      # Today's date
date(now)                        # Current timestamp
dateformat(date, format)         # Format date
striptime(datetime)              # Remove time component
dur(duration_text)               # Create duration
```

**Date Usage Examples:**
```
WHERE due <= date(today) + dur(1 week)
TABLE dateformat(file.ctime, "yyyy-MM-dd") AS "Created"
WHERE file.mtime >= date(today) - dur(30 days)
```

#### Meta Functions

```
typeof(value)                    # Get type
meta(link)                       # Get link metadata
meta(section)                    # Get section metadata
```

**Meta Function Usage:**
```
# Type checking
WHERE typeof(rating) = "number"

# Section filtering
WHERE meta(section).subpath = "Action Items"

# Link properties
WHERE meta(file.link).type = "header"
```

#### Utility Functions

```
choice(condition, if_true, if_false)  # Ternary operator
default(value, default)               # Default if null
round(number, decimals)               # Round number
truncate(text, length)                # Truncate string
hash(value)                           # Generate hash
```

---

## 📚 Query Pattern Library: Comprehensive Examples

> [!principle-point]
> **Pattern Library Philosophy**
> This section provides battle-tested query patterns organized by use case. Each pattern includes context, implementation, and extension opportunities.

### Task Management Patterns

#### All Incomplete Tasks by Project

```
TASK
WHERE !completed
GROUP BY file.link
SORT rows.file.ctime ASC
```

**Variations:**
```
# Tasks due this week
TASK
WHERE !completed 
      AND typeof(due) = "date"
      AND due >= date(today)
      AND due <= date(today) + dur(1 week)

# Overdue tasks
TASK
WHERE !completed 
      AND typeof(due) = "date"
      AND due < date(today)
SORT due ASC
```

#### Task Dashboard with Priorities

```
TABLE 
    T.text AS "Task",
    T.due AS "Due",
    T.priority AS "Priority"
FROM "Projects"
FLATTEN file.tasks AS T
WHERE !T.completed AND T.priority
SORT T.priority DESC, T.due ASC
```

### Content Aggregation Patterns

#### Book Library with Ratings

```
TABLE
    author,
    rating AS "⭐ Rating",
    status,
    dateformat(finished, "yyyy-MM-dd") AS "Finished"
FROM #book
WHERE rating >= 7
SORT rating DESC, finished DESC
```

#### Reading Progress Tracker

```
TABLE
    pagesRead AS "Read",
    totalPages AS "Total",
    round((pagesRead/totalPages)*100) AS "Progress %",
    totalPages - pagesRead AS "Remaining"
FROM #book
WHERE status = "reading"
SORT round((pagesRead/totalPages)*100) DESC
```

### Temporal Query Patterns

#### Recently Modified Notes

```
TABLE 
    file.mtime AS "Modified",
    file.folder AS "Folder"
WHERE file.mtime >= date(today) - dur(7 days)
SORT file.mtime DESC
LIMIT 20
```

#### Content Created This Month

```
LIST
WHERE file.cday.year = date(today).year
      AND file.cday.month = date(today).month
SORT file.cday DESC
```

#### Calendar View of Deadlines

```
CALENDAR due
FROM #project OR #task
WHERE typeof(due) = "date"
```

### Relationship Query Patterns

#### Backlink Analysis

```
TABLE
    length(file.inlinks) AS "Incoming Links",
    length(file.outlinks) AS "Outgoing Links",
    length(file.inlinks) - length(file.outlinks) AS "Net Links"
WHERE length(file.inlinks) > 0
SORT length(file.inlinks) DESC
LIMIT 50
```

#### Notes Linking to Current Page

```
LIST
WHERE contains(file.outlinks, this.file.link)
SORT file.mtime DESC
```

#### Orphaned Pages (No Links)

```
LIST
WHERE length(file.inlinks) = 0 
      AND length(file.outlinks) = 0
      AND !contains(file.folder, "Archive")
SORT file.name
```

### Grouping Patterns

#### Projects by Status with Counts

```
TABLE WITHOUT ID
    key AS "Status",
    length(rows) AS "Count",
    rows.file.link AS "Projects"
FROM #project
GROUP BY status
SORT length(rows) DESC
```

#### Books by Genre and Author

```
TABLE rows.file.link AS "Books"
FROM #book
FLATTEN genres AS genre
GROUP BY genre
SORT genre ASC
```

#### Tasks by Due Date Ranges

```
LIST rows.T.text
FROM "Projects"
FLATTEN file.tasks AS T
WHERE !T.completed AND typeof(T.due) = "date"
GROUP BY choice(
    T.due < date(today), "Overdue",
    T.due = date(today), "Today",
    T.due <= date(today) + dur(1 week), "This Week",
    "Later"
) AS timeframe
SORT timeframe
```

### Advanced Calculation Patterns

#### Project Completion Percentage

```
TABLE
    status,
    completedTasks + "/" + totalTasks AS "Tasks",
    round((completedTasks/totalTasks)*100) AS "% Done"
FROM #project
WHERE totalTasks > 0
SORT round((completedTasks/totalTasks)*100) DESC
```

#### Average Rating by Category

```
TABLE WITHOUT ID
    key AS "Category",
    length(rows) AS "Items",
    round(average(rows.rating), 1) AS "Avg Rating",
    round(sum(rows.rating), 0) AS "Total Points"
FROM #media
WHERE rating
GROUP BY category
SORT average(rows.rating) DESC
```

### List Processing Patterns

#### Extract Specific List Items

```
TABLE L.text AS "Action Items"
FROM "Meeting Notes"
FLATTEN file.lists AS L
WHERE meta(L.section).subpath = "Action Items"
      AND !contains(L.text, "DONE")
```

#### Tasks with Specific Tags

```
TASK
WHERE contains(tags, "#priority") 
      OR contains(text, "#urgent")
SORT due ASC
```

### Multi-Value Field Patterns

#### Tags Frequency Analysis

```
TABLE WITHOUT ID
    tag AS "Tag",
    length(rows) AS "Usage Count",
    rows.file.link AS "Pages"
FLATTEN file.etags AS tag
GROUP BY tag
SORT length(rows) DESC
LIMIT 30
```

#### Contributors Per Project

```
TABLE 
    rows.file.link AS "Projects",
    length(rows) AS "Count"
FROM #project
FLATTEN contributors AS contributor
GROUP BY contributor
SORT length(rows) DESC
```

### Complex Filtering Patterns

#### Multi-Condition Project Filter

```
TABLE status, priority, owner, due_date
FROM #project
WHERE (status = "active" OR status = "pending")
      AND priority >= 3
      AND typeof(due_date) = "date"
      AND due_date <= date(today) + dur(2 months)
      AND !archived
SORT priority ASC, due_date ASC
```

#### Content Age Categorization

```
LIST "Created: " + dateformat(file.cday, "yyyy-MM-dd")
WHERE choice(
    date(today) - file.cday < dur(7 days), true,
    false
) = true  # Recent notes (last week)
SORT file.cday DESC
```

### JS Patterns

#### Custom Grouped Tables

```js
for (let group of dv.pages("#book").groupBy(p => p.genre)) {
    dv.header(3, group.key);
    dv.table(
        ["Title", "Author", "Rating"],
        group.rows
            .sort(k => k.rating, 'desc')
            .map(k => [k.file.link, k.author, k.rating])
    );
}
```

#### Conditional Task Lists

```js
let projects = dv.pages("#project");

dv.header(2, "High Priority Tasks");
dv.taskList(
    projects.file.tasks
        .where(t => !t.completed && t.priority === "high")
);

dv.header(2, "Overdue Tasks");
dv.taskList(
    projects.file.tasks
        .where(t => !t.completed && t.due && t.due < dv.date("today"))
);
```

#### Dynamic Content Aggregation

```js
let pages = dv.pages('"Daily Notes"')
    .where(p => p.file.cday.year === 2024);

dv.header(2, "2024 Statistics");
dv.paragraph(`Total Notes: ${pages.length}`);
dv.paragraph(`Total Tasks: ${pages.file.tasks.length}`);
dv.paragraph(`Completed: ${pages.file.tasks.where(t => t.completed).length}`);
```

#### Advanced Link Analysis

```js
let page = dv.current().file.path;
let pages = new Set();
let stack = [page];

while (stack.length > 0) {
    let elem = stack.pop();
    let meta = dv.page(elem);
    if (!meta) continue;
    
    for (let inlink of meta.file.inlinks.concat(meta.file.outlinks).array()) {
        if (pages.has(inlink.path)) continue;
        pages.add(inlink.path);
        stack.push(inlink.path);
    }
}

dv.header(2, "Connected Notes");
dv.paragraph(`Found ${pages.size} directly or indirectly connected notes`);
```

---

## 🚀 Advanced Techniques & Optimization

### Performance Optimization

> [!principle-point]
> **Performance Hierarchy**
> Optimize queries through: specific FROM sources → early WHERE filtering → LIMIT clauses → avoiding complex calculations in display

**Optimization Strategies:**

1. **Narrow FROM Source**
```
# ❌ Slow - searches entire vault
TABLE rating FROM ""

# ✅ Fast - specific folder
TABLE rating FROM "Books"
```

2. **Early Filtering**
```
# ❌ Processes all then filters
TABLE field1, field2
FROM #large-tag
SORT field1
WHERE condition
LIMIT 10

# ✅ Filters first
TABLE field1, field2
FROM #large-tag
WHERE condition
LIMIT 10
SORT field1
```

3. **Strategic LIMIT Usage**
```
TABLE expensive_calculation
FROM large_source
WHERE cheap_filter
LIMIT 50  # Process only top 50
```

### Query Composition Patterns

#### Reusable Query Components

Create note templates with parameterized queries:

```markdown
# Project Status Dashboard

**Status: active**
```
TABLE priority, due_date, owner
FROM #project
WHERE status = "active"
SORT priority ASC
```

**Status: pending**
```
TABLE priority, due_date, owner  
FROM #project
WHERE status = "pending"
SORT due_date ASC
```
```

#### Dynamic MOC Generation

```
# Development Topics MOC
LIST
FROM #development AND #permanent
GROUP BY file.folder
SORT file.name
```

### Custom View Patterns (DataviewJS)

#### Reusable Custom Views

Create `/views/custom-table.js`:
```javascript
// Custom view for formatted project tables
const projects = dv.pages(input.source);

dv.table(
    ["Project", "Status", "Progress"],
    projects
        .sort(p => p.priority)
        .map(p => [
            p.file.link,
            p.status,
            `${p.progress}% ` + "█".repeat(p.progress/10)
        ])
);
```

Use in queries:
```js
await dv.view("views/custom-table", {
    source: "#project"
});
```

### Complex Transformations

#### Multi-Stage Data Processing

```js
let books = dv.pages("#book")
    .where(b => b.rating >= 7)
    .sort(b => b.rating, 'desc');

// Group by rating tiers
let tiers = {
    "Excellent (9-10)": books.where(b => b.rating >= 9),
    "Great (7-8)": books.where(b => b.rating >= 7 && b.rating < 9)
};

for (let [tier, items] of Object.entries(tiers)) {
    dv.header(3, tier + ` (${items.length} books)`);
    dv.table(
        ["Title", "Author", "Rating"],
        items.map(b => [b.file.link, b.author, b.rating])
    );
}
```

### Error Handling Patterns

```js
try {
    let pages = dv.pages("#nonexistent");
    if (pages.length === 0) {
        dv.paragraph("*No matching pages found*");
    } else {
        dv.list(pages.file.link);
    }
} catch (error) {
    dv.paragraph("**Error:** " + error.message);
}
```

---

## 🔧 Troubleshooting & Best Practices

### Common Issues & Solutions

#### Issue: Query Returns No Results

**Diagnostic Steps:**
1. Verify FROM source is correct
2. Check metadata field existence
3. Test without WHERE conditions
4. Verify data type compatibility

```
# Debug query - show all fields
TABLE file.frontmatter
FROM "suspect-folder"
WHERE file.name = "specific-note"
```

#### Issue: Unexpected Null Values

Null comparisons can produce unexpected results—null <= date(today) returns true.

**Solution Pattern:**
```
# Always check field existence
WHERE field AND condition

# Or use type checking
WHERE typeof(field) = "expected-type" AND condition
```

#### Issue: Multi-Value Field Grouping Problems

Pages can appear multiple times in grouped results when matching multiple groups.

**Solution:**
```
# FLATTEN multi-value field before grouping
TABLE rows.file.link
FROM #media
FLATTEN genres
GROUP BY genres
```

### Best Practices Checklist

> [!quick-reference]
> **Query Development Best Practices**
> - [ ] Use specific FROM sources over vault-wide searches
> - [ ] Check field existence before comparison
> - [ ] Apply type-checking for null safety
> - [ ] FLATTEN multi-value fields before GROUP BY
> - [ ] Order commands logically (filter → sort → limit)
> - [ ] Use LIMIT with large result sets
> - [ ] Test queries incrementally
> - [ ] Document complex query logic

### Metadata Management Guidelines

**Field Naming Conventions:**
- Use lowercase with hyphens or underscores
- Avoid spaces (requires sanitization/row syntax)
- Be consistent across note types
- Prefix related fields: `project_status`, `project_priority`

**Date Field Standards:**
- Always use ISO8601 format (YYYY-MM-DD)
- Include time only when necessary
- Use consistent field names: `created`, `modified`, `due`, `completed`

**Link Field Requirements:**
- Always quote links in frontmatter
- Use [[Wiki-Link]] syntax for Dataview recognition
- Consider Obsidian's lack of tracking for quoted frontmatter links

### Query Organization Strategies

**Dashboard Pattern:**
```markdown
# Dashboard Title

## Section 1: Overview
```
[summary query]
```

## Section 2: Details
```
[detailed query]
```

## Section 3: Analytics
```
[analytical query]
```
```

**Query Note Template:**
```markdown
---
type: query-collection
category: projects
tags: [, dashboard]
---

# Project Queries

## Active Projects
``` 
[query]
```

**Purpose**: Shows all active projects sorted by priority

## Overdue Items  
``` 
[query]
```

**Purpose**: Identifies overdue project tasks
```

---

## 📊 Metadata & Attribution

> [!methodology-and-sources]
> **Research Methodology**
> - **Primary Sources**: Official Dataview documentation at blacksmithgu.github.io
> - **Research Queries**: "Dataview Obsidian query syntax", "Dataview metadata fields", "Dataview functions operations", "DataviewJS API examples", "Dataview query patterns library"
> - **Synthesis Approach**: Systematic extraction from official documentation, community examples, and implementation guides
> - **Confidence Level**: 
>   - High for DQL syntax and core functionality
>   - High for metadata architecture  
>   - High for official API methods
>   - Medium for performance optimization (implementation-dependent)

## 🔄 Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2024-11-14 | Initial comprehensive compilation |

---

# 🔗 Related Topics for PKB Expansion

1. **[[Advanced Dataview Optimization Techniques]]**
   - *Connection*: Builds on performance optimization section with vault-specific tuning
   - *Depth Potential*: Deep dive into indexing behavior, query planning, caching strategies
   - *Knowledge Graph Role*: Technical implementation details for power users

2. **[[Metadata Schema Design Patterns for PKM]]**
   - *Connection*: Expands metadata architecture section into systematic schema design
   - *Depth Potential*: Cross-note-type schemas, inheritance patterns, validation strategies
   - *Knowledge Graph Role*: Bridges Dataview with broader [[03_notes/01_permanent-notes/01_cognitive development/Knowledge management]] methodology

3. **[[DataviewJS Advanced Patterns & Custom Views]]**
   - *Connection*: Extends DataviewJS section with sophisticated JavaScript techniques
   - *Depth Potential*: Custom rendering, external API integration, complex data pipelines
   - *Knowledge Graph Role*: Programming interface between Dataview and advanced automation

4. **[[Dataview Integration with Templater & Other Plugins]]**
   - *Connection*: Explores cross-plugin workflows combining Dataview with [[Templater]], [[component-exemplar-quickadd-plugin-documentation-v1.0.0-20251119225738]], etc.
   - *Depth Potential*: Automated note generation, dynamic template population, workflow automation
   - *Knowledge Graph Role*: Positions Dataview within broader Obsidian automation ecosystem
     
```
<thinking>
**PHASE 1: REQUEST ANALYSIS**

Request Classification:
- Type: comprehensive_note (Reference Note)
- Scope: reference (exhaustive documentation)
- Topic: Dataview plugin for Obsidian
- Research Required: YES - Need to verify current syntax, latest features, best practices, and comprehensive query examples

User Requirements Breakdown:
1. Comprehensive Reference Note on Dataview plugin
2. Complete coverage of query development methods
3. Detailed explanation of query construction process
4. Information architecture for queryable fields (tags, status, type, etc.)
5. Extensive repository of example queries
6. Inspiration/pattern library for query design

**RESEARCH STRATEGY:**
I need to execute multiple searches to gather:
1. Dataview plugin fundamentals and current syntax
2. Query language specifications (DQL, Inline, DataviewJS)
3. Metadata field types and conventions
4. Advanced query techniques and operators
5. Real-world query examples and patterns

Let me conduct systematic research to ensure accuracy and comprehensiveness.

SEARCH 1 - FOUNDATIONAL UNDERSTANDING:
Query Rationale: "Dataview Obsidian plugin documentation query syntax"
Expected Insight: Current syntax specification, query types, basic structure

SEARCH 2 - QUERY LANGUAGE DEPTH:
Query Rationale: "Dataview DQL DataviewJS inline queries difference"
Expected Insight: Distinctions between query methods, use cases for each

SEARCH 3 - METADATA CONVENTIONS:
Query Rationale: "Obsidian Dataview metadata fields YAML frontmatter properties"
Expected Insight: Standard field naming, data types, organization patterns

SEARCH 4 - ADVANCED TECHNIQUES:
Query Rationale: "Dataview advanced queries functions operations"
Expected Insight: Complex operations, data manipulation, filtering techniques

SEARCH 5 - PRACTICAL EXAMPLES:
Query Rationale: "Dataview query examples library patterns"
Expected Insight: Real-world implementations, common patterns, query templates

**PHASE 2: STRUCTURAL PLANNING**

STRUCTURAL REASONING:
├── Core Concept Architecture
│   ├── Why this structure? 
│   │   └── Progression from fundamentals → query construction → implementation → examples
│   └── Information flow logic: 
│       └── Build understanding layer by layer: plugin overview → query types → syntax → 
│           metadata architecture → query building process → comprehensive examples
│
├── Hierarchy Decisions
│   ├── Primary sections: 
│   │   1. Plugin Overview & Capabilities (context)
│   │   2. Query Language Taxonomy (three types explained)
│   │   3. Query Syntax & Structure (DQL deep dive)
│   │   4. Metadata Architecture (field design & conventions)
│   │   5. Query Construction Process (systematic approach)
│   │   6. Operator & Function Reference (technical specifications)
│   │   7. Query Pattern Library (extensive examples)
│   │   8. Advanced Techniques (optimization, complex operations)
│   │   9. Troubleshooting & Best Practices (practical wisdom)
│   └── Subsection depth: 
│       └── 3-4 levels deep for technical sections, extensive examples in pattern library
│
└── Cross-referencing Strategy
    └── Internal link opportunities:
        - [[Obsidian]] ecosystem
        - [[YAML Frontmatter]] conventions
        - [[Metadata Schema Design]]
        - [[Regular Expressions]]
        - [[JavaScript]] for DataviewJS
        - [[SQL]] parallels for mental model
        - [[Knowledge Graph]] building
        - [[MOC]] creation with Dataview
        - [[Personal Knowledge Management]]
        - [[Zettelkasten]] integration

**WIKI-LINK TARGETS:**
Technical concepts: YAML, Frontmatter, Metadata, Query Language, DQL, JavaScript, Boolean Logic, Regular Expressions, Data Types
Obsidian concepts: Properties, Tags, Links, Backlinks, Canvas, Daily Notes, Templates, Folder Structure
PKM concepts: Knowledge Graph, MOC, Index, Dashboard, Zettelkasten, Progressive Summarization
Adjacent tools/concepts: SQL, Database Queries, Filter Operations, Data Manipulation

**CALLOUT STRATEGY:**
- [!abstract] - Overview sections
- [!definition] - Technical term definitions
- [!principle-point] - Core concepts
- [!methodology-and-sources] - Query construction process
- [!example] - Extensive use for query examples
- [!helpful-tip] - Best practices
- [!warning] - Common pitfalls
- [!quick-reference] - Syntax tables
- [!use-cases-and-examples] - Pattern library sections

**METADATA PLANNING:**
Tags: #obsidian #dataview #plugin #query-language #reference-note #pkm-tools
Aliases: [Dataview Plugin, DQL, Dataview Query Language, Obsidian Dataview]

Now I'll execute the web searches before constructing the document.
</thinking>
```

```
I'll create a comprehensive Reference Note on the Dataview plugin for Obsidian. Let me first conduct systematic research to ensure I provide the most current and accurate information.Perfect! I've gathered comprehensive information about the Dataview plugin. Now I'll create the exhaustive Reference Note as requested.
```