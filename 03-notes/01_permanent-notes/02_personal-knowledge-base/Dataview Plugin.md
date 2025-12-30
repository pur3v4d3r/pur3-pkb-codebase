---
aliases:
  - "Dataview"
  - "dataview "
tags:
  - "type/permanent"
  - "year/2025"
  - "complexity/intermediate"
  - "context/applied"
  - "critical-thinking/analysis"
  - "knowledge-work/learning/mastery"
  - "learning-theory/andragogy/self-directed"
  - "learning-theory/heutagogy/capability-building"
  - "knowledge-work/reading/comprehension"
  - "critical-thinking/synthesis/concept-building"
source: "other-note"
id: "20251124052105"
created: "2025-11-24T05:21:05"
modified: "2025-11-24T05:21:05"
week: "[[2025-W48]]"
month: "[[2025-11]]"
quarter: "[[2025-Q4]]"
year: "[[2025]]"
type: "permanent-note"
maturity: seedling
confidence: speculative
next-review: "2025-12-01"
link-count: 0
backlink-count: 0
link-up:
  - "[[pkb-knowledge-perm-moc]]"
link-related:
  - "[[2025-11-24|Daily-Note]]"
status: active


review-last-reviewed: null
review-next-review: 2025-12-17
review-count: 0
review-interval: 3

review-priority: medium
---

# Dataview Plugin

> [!definition]
> - **Key-Term**:: [[Dataview Plugin]]
> - [**Definition**:: The Dataview plugin is a powerful tool for Obsidian that allows users to query and display data from their Markdown notes. It transforms Obsidian from a simple note-taking app into a dynamic personal knowledge management system by enabling users to extract and organize information programmatically.]
> - **Status**:: 🌱 `= this.maturity` | Confidence: `= this.confidence`

## 📊 Note Metadata Dashboard

**Development Status**: `= this.maturity`  
**Epistemic Confidence**: `= this.confidence`  
**Next Review**: `= this.next-review`  
**Review Count**: `= this.review-count`  
**Created**: `= this.created`  
**Last Modified**: `= this.modified`

---

## Foundational Understanding
### What is Dataview?

Dataview processes the metadata within your notes (like YAML frontmatter, inline fields, and tags) and allows you to create dynamic tables, lists, and task lists based on specific criteria. Instead of manually linking or organizing every piece of information, Dataview can automatically pull and present relevant data from across your vault.


## Key Principles

1. **Data Extraction**: Automatically pulls data from YAML frontmatter, inline fields, and tags.
2. **Query Language**: Uses a simple, SQL-like query language to define what data to retrieve and how to display it.
3. **Dynamic Views**: Creates live-updating lists, tables, and task lists that reflect changes in your notes instantly.
4. **Inter-note Relationships**: Helps visualize connections between notes based on shared metadata.
5. **Task Management**: Can aggregate and display tasks from across your vault, including due dates and completion status.

## Related Concepts

```dataview
TABLE type, maturity, confidence
FROM [[]]
WHERE type = "concept" OR type = "principle"
SORT maturity DESC
LIMIT 10
```

### Direct Connections
- [[Concept 1]]
- [[Concept 2]]
- [[Concept 3]]

## Practical Applications

> [!example] Application 1
> 
Dataview scans your Obsidian vault for notes containing specific metadata. This metadata can be:

-   **YAML Frontmatter**: Defined at the top of a note between `---` delimiters (e.g., `status: "in progress"`).
-   **Inline Fields**: Key-value pairs written directly in the body of a note (e.g., `status:: in progress` or `[status:: in progress]`).
-   **Tags**: Standard Obsidian tags (e.g., `#project`, `#status/in-progress`).

Dataview queries then specify which notes to include (e.g., all notes with a certain tag) and which fields to display from those notes.
## Questions & Tensions

> [!question] Open Question 1
> 

> [!question] Open Question 2
> 

## Evolution Log

> [!timeline] Development History
> `= this.review-count` total reviews

### 2025-11-24 - Initial Creation
[**Context**:: Needed to Learn about Inline Queries and wanted to test out the system for creating these permanent notes.] 
**Maturity**: `= this.maturity`  
**Confidence**: `= this.confidence`

---

## 📚 Sources & References

```dataview
TABLE 
    source AS "Source Type",
    created AS "Date Added"
FROM [[]]
WHERE source
SORT created DESC
```

### Primary Sources
- [[reference-comprehensive-dataview-202511140206 1]]

### Supporting Material
- [[reference-guide-dataview-inline-fields_202511231147]]
- [[reference-guide-dataview-inline-queries-202511232257]]


### To Explore
- [ ] [[self-documenting-dataview-implementation-guide]]
- [ ] [[self-documenting-dataview-system-reference]]

---

## 🔗 Backlinks & Connections

```dataview
TABLE 
    type AS "Type",
    maturity AS "Maturity",
    created AS "Created"
FROM [[#]]
SORT created DESC
LIMIT 15
```

```dataview
TABLE 
    type AS "Type",
    maturity AS "Maturity",
    length(file.inlinks) AS "Its Backlinks",
    dateformat(date(created), "MMM dd, yyyy") AS "Created"
FROM [[#]]
WHERE file.name != this.file.name
SORT length(file.inlinks) DESC
LIMIT 20
```
---

## 📈 Review System

> [!important] Review Schedule
> - **Next Review**: `= this.next-review`
> - **Review Frequency**: Based on maturity level
>   - Seedling: Weekly
>   - Budding: Bi-weekly
>   - Developing: Monthly
>   - Evergreen: Quarterly

**Review Checklist**:
- [ ] Definition still accurate?
- [ ] New connections identified?
- [ ] Applications validated?
- [ ] Sources still relevant?
- [ ] Maturity level appropriate?

---

## 🏷️ Tags & Classification

Primary Tags:: `= this.tags`  
Type:: `= this.type`  
Source:: `= this.source`

----