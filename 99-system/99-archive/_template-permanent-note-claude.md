<%*
// Permanent Note Template with Alias Configuration
const title = await tp.system.prompt("Enter concept/theory/person name:");
const alias1 = await tp.system.prompt("Enter first alias (or press Enter to skip):");
const alias2 = await tp.system.prompt("Enter second alias (or press Enter to skip):");
const tag = await tp.system.suggester(
  ["Psychology", "Philosophy", "Education", "PKM", "Methodology", "Metacognition", "PKB"],
  ["psychology", "philosophy", "education", "pkm", "methodology", "metacognition", "pkb"],
  false,
  "Select primary domain:"
);

// Generate aliases array
let aliases = [title];
if (alias1) aliases.push(alias1);
if (alias2) aliases.push(alias2);
-%>
---
aliases: [<% aliases.map(a => `"${a}"`).join(", ") %>]
tags:
  - type/permanent
  - year/2025
  - <% tag %>
id: "<% tp.date.now("YYYYMMDDHHmmss") %>"
created: "<% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>"
week: "[[<% tp.date.now("gggg-[W]WW") %>]]"
month: "[[<% tp.date.now("YYYY-MM") %>]]"
quarter: "[[<% tp.date.now("YYYY-[Q]Q") %>]]"
year: "[[<% tp.date.now("YYYY") %>]]"
type: 🧬concept
link-up:
  - 
link-related:
  - "[[<% tp.date.now("YYYY-MM-DD") %>|Daily-Note]]"
  - "[[permeant-note_moc]]"
---

# <% title %>

> [!definition]
> - **Key-Term**:: [[<% tp.file.title %>]]
> - [**Definition**:: ]

## Foundational Understanding

[Your initial understanding of this concept]

## Key Principles

## Related Concepts

- [[Concept 1]]
- [[Concept 2]]

## Practical Applications

## Evolution Log

### <% tp.date.now("YYYY-MM-DD") %> - Initial Creation
[Context: Where you first encountered this concept]

---

## 📚 Sources

