<%*
// --- CONFIGURATION: TAG LISTS ---
// Defining these once keeps the code clean and prevents copy-paste errors

const generalTags = [
	 "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
	
	
	
	
];
const specificTags = [
	 "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
	
	


	
];
// --- INPUT PROMPTS ---
const title = await tp.system.prompt("Enter Title for YAML:");
const alias1 = await tp.system.prompt("Enter first alias (or press Enter to skip):");
const alias2 = await tp.system.prompt("Enter second alias (or press Enter to skip):");
// Initialize empty strings for these to avoid "undefined" in YAML
// Alternatively, you can add prompts for these if you wish
const source = ""; 
const type = "report"; 
// Suggesters using the pre-defined arrays
const tag1 = await tp.system.suggester(generalTags, generalTags, false, "Select Tag 01:");
const tag2 = await tp.system.suggester(generalTags, generalTags, false, "Select Tag 02:");
const tag3 = await tp.system.suggester(specificTags, specificTags, false, "Select Tag 03:");
const tag4 = await tp.system.suggester(specificTags, specificTags, false, "Select Tag 04:");
const tag5 = await tp.system.suggester(specificTags, specificTags, false, "Select Tag 05:");
_%>
---
aliases:
  - "<% alias1 %>"
  - "<% alias2 %>"
tags:
  - "type/report"
  - "year/2025"
  - "<% tag1 %>"
  - "<% tag2 %>"
  - "<% tag3 %>"
  - "<% tag4 %>"
  - "<% tag5 %>"
source: "<% source %>"
id: "<% tp.date.now("YYYYMMDDHHmmss") %>"
created: "<% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>"
week: "[[<% tp.date.now("gggg-[W]WW") %>]]"
month: "[[<% tp.date.now("YYYY-MM") %>]]"
quarter: "[[<% tp.date.now("YYYY-[Q]Q") %>]]"
year: "[[<% tp.date.now("YYYY") %>]]"
type: "<% type %>"
link-up:
  - 
link-related:
  - "[[<% tp.date.now("YYYY-MM-DD") %>|Daily-Note]]"
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