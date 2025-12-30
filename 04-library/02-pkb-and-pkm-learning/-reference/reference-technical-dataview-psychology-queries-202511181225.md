---
title:
aliases:
  - "Dataview Queries Cognitive Psychology "
  - Cognitive Psychology Dataview
tags:
  - year/2025
  - source/pur3v4d3r
  - pkb/plugin/dataview
id: "20251118122758"
created: 2025-11-18T12:27:58
week: "[[2025-W47]]"
month: "[[2025-11]]"
quarter: "[[2025-Q4]]"
year: "[[2025]]"
type: reference
link-up:
  - 
link-related:
  - "[[2025-11-18|Daily-Note]]"
  - "[[permeant-note_moc]]"
---

## 🔍 Essential Dataview Queries for This Domain

> [!what-this-does]
> **These queries transform your tags into dynamic views of your knowledge base.** Save these in your domain MOC or dashboard for quick access.

### Query 1: All Permanent Notes in Cognitive Abilities Domain

```dataview
TABLE status, file.mtime as "Last Modified"
FROM #topic/psychology
WHERE type = "🧬concept"
SORT status ASC, file.mtime DESC
```

**Use-case:** Identify your original thinking in this domain—the core intellectual contributions of your PKB.

---

### Query 2: Notes Needing Review by Subdomain

```
TABLE file.tags as "Tags", file.mtime as "Last Modified"
WHERE contains(file.tags, "cognitive-science") AND status = "review"
SORT file.mtime ASC
```

**Use-case:** During your weekly review, identify cognitive science notes that need attention.

---

### Query 3: Techniques and Practices Ready to Implement

```
LIST
FROM #type/technique
WHERE contains(file.tags, "self-improvement") AND status != "archived"
SORT file.name
```

**Use-case:** Generate a list of actionable techniques you've documented for personal practice.

---

### Query 4: Literature Notes by Theory

```
TABLE author, source, file.ctime as "Added"
FROM #type/literature
WHERE contains(file.tags, "theory")
SORT author ASC
```

**Use-case:** Create a reading bibliography organized by author/source.

---

### Query 5: Metacognition Knowledge Cluster

```
TABLE type, status, file.outlinks as "Links Out"
FROM #cognitive-science/metacognition
SORT type, status
```

**Use-case:** Visualize all your metacognition-related notes and their interconnections.

---



---




