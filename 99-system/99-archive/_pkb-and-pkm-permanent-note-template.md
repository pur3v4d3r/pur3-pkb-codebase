<%*
// --- CONFIGURATION: TAG LISTS ---
// Defining these once keeps the code clean and prevents copy-paste errors

const generalTags = [
	 "pkm", "pkm/theory", "pkm/methodology", "pkm/workflow", "pkm/principles", "pkm/research", "pkb", "pkb/architecture", "pkb/design", "pkb/components", "pkb/metadata", "pkb/maintenance", "pkb/optimization", "note-taking", "knowledge-workflow", "knowledge-workflow/review", "obsidian", "obsidian/plugins", "obsidian/plugins/dataview", "obsidian/plugins/templater", "obsidian/plugins/quickadd", "obsidian/customization", "obsidian/customization/css", "obsidian/customization/snippets", "obsidian/customization/callouts", "obsidian/configuration", "obsidian/advanced", "information-architecture", "information-architecture/organization", "information-architecture/taxonomy", "information-architecture/navigation", "knowledge-work", "knowledge-work/reading", "knowledge-work/research", "knowledge-work/writing", "knowledge-work/thinking", "knowledge-work/learning", "digital-garden", "digital-garden/philosophy", "productivity", "productivity/time-management", "productivity/task-management", "productivity/task-management/todos", "productivity/task-management/projects", "productivity/task-management/workflows", "concept/atomic-notes", "concept/progressive-summarization", "concept/emergence", "concept/information-overload", "concept/cognitive-overhead", "concept/discoverability", "concept/external-cognition"
	
	
	
	
];
const specificTags = [
	 "pkm/theory/foundations", "pkm/theory/epistemology", "pkm/theory/cognitive-basis", "pkm/theory/philosophy", "pkm/workflow/capture", "pkm/workflow/process", "pkm/workflow/organize", "pkm/workflow/review", "pkb/architecture/structure", "pkb/architecture/hierarchy", "pkb/architecture/folders", "pkb/architecture/taxonomy", "pkb/design/information-architecture", "pkb/components/moc", "pkb/components/hub-notes", "pkb/components/index-notes", "pkb/components/dashboards", "pkb/components/atomic-notes", "pkb/metadata/tags", "pkb/metadata/properties", "pkb/metadata/frontmatter", "pkb/metadata/yaml", "pkb/maintenance/refactoring", "pkb/maintenance/cleanup", "pkb/optimization/workflows", "note-taking/practices/summarization", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
	
	

	
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