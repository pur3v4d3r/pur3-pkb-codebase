---
aliases: []
concept-type: concept
tags:
status: active
created: <% tp.date.now("YYYY-MM-DD") %>
---
## ⚙️ Concept Management





# <% tp.file.title %>

## 📊 Overview

**Status**: `VIEW[{status}]`
**Type**: `VIEW[{concept-type}]`
**References**: `$= dv.current().file.inlinks.length` inlinks

## 🔍 Where This Concept Appears

> [!info]How this works
> This query finds all notes that reference this concept in their `concepts::` metadata field

```dataview
TABLE 
  file.folder as "Location",
  concept-type as "Type",
  status as "Status"
WHERE concepts AND contains(concepts, this.file.link)
SORT file.mtime DESC
LIMIT 50
```

## 📝 Usage Examples

*Document how this concept is used in your PKB*

### Example 1: [Context]

- **Reference Note**: 
- **Usage Pattern**: 
- **Key Insight**: 

## 🔗 Related Concepts

```dataviewjs
const inlinks = dv.current().file.inlinks.limit(20)
const outlinks = dv.current().file.outlinks.filter(l => !l.path.includes("template")).limit(20)
const maxLen = Math.max(inlinks.length, outlinks.length)

dv.table(
  ["← References This (" + inlinks.length + ")", "This References → (" + outlinks.length + ")"],
  Array.from({length: maxLen}, (_, i) => [
    inlinks[i] || "",
    outlinks[i] || ""
  ])
)
```

## 📚 Resources

- **Documentation**: 
- **Related Notes**: 

---

## 🏷️ Metadata Registry

*For notes that reference this concept, add this to your frontmatter:*

```yaml
concepts: [[<% tp.file.title %>]]
```