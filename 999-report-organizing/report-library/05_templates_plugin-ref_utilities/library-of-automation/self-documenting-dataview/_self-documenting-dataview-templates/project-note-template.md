---
aliases: []
tags: #project
status: planning
created: <% tp.date.now("YYYY-MM-DD") %>
concepts: []
tools: []
people: []
---

# <% tp.file.title %>

## 🎯 Project Overview

**Status**: `INPUT[select(planning,active,on-hold,completed):status]`

## 🧠 Concepts Applied

*Add concept links to frontmatter `concepts::` field to auto-register in concept notes*

**Primary Concepts**:
- concepts:: [[Concept Name 1]]
- concepts:: [[Concept Name 2]]

**Supporting Concepts**:
- concepts:: [[Supporting Concept]]

## 🛠️ Tools & Technologies

- tools:: [[Tool Name]]

## 👥 People Involved

- people:: [[Person Name]]

## 📋 Tasks

```tasks
not done
path includes {{TITLE}}
```

## 📝 Notes

*Main content here*

---

## 🔍 Auto-Discovery

### Related Concept Notes

```dataview
TABLE concept-type, status
FROM [[<% tp.file.title %>]]
WHERE concept-type
SORT file.name
```

### Related Projects

```dataview
TABLE status, created
WHERE contains(concepts, this.file.link) OR contains(file.outlinks, this.file.link)
WHERE contains(tags, "project")
WHERE file.name != this.file.name
SORT status ASC, file.mtime DESC
LIMIT 10
```