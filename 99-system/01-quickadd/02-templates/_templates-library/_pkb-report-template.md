<%*
/* ---------------------------------------------------------------
PKB & PKM REPORT TEMPLATE
Domain: Personal Knowledge Management, Obsidian, Info Arch
*/
// --- CONFIGURATION: DATA LISTS ---
// LIST A: Primary Domains (PKM, PKB, Obsidian, IA)
const groupA_Tags = [
"pkm",
"pkm/theory",
"pkm/methodology",
"pkm/workflow",
"pkb",
"pkb/architecture",
"pkb/design",
"pkb/maintenance",
"note-taking",
"knowledge-workflow",
"obsidian",
"obsidian/plugins",
"information-architecture",
"digital-garden",
"productivity"
];
// LIST B: Specific Concepts & Methodologies
const groupB_Tags = [
"pkm/methodology/zettelkasten",
"pkm/methodology/para",
"pkm/methodology/lyt",
"pkm/methodology/evergreen-notes",
"pkm/workflow/capture",
"pkm/workflow/process",
"pkm/principles/atomic-notes",
"pkm/principles/linking-thinking",
"pkm/principles/emergence",
"pkb/components/moc",
"pkb/components/hub-notes",
"pkb/components/dashboards",
"note-taking/types/permanent",
"note-taking/types/literature",
"obsidian/core-features/graph-view",
"obsidian/core-features/canvas",
"obsidian/plugins/dataview",
"obsidian/plugins/templater",
"information-architecture/taxonomy",
"information-architecture/ontology",
"knowledge-graph/linking/bidirectional",
"digital-garden/philosophy/learning-in-public",
"productivity/gtd",
"concept/atomic-notes",
"concept/linking-thinking",
"concept/networked-thought"
];
// --- METADATA LISTS ---
const type_options = [
"pkb/report",
"cog-psy/report",
"prompt/report",
"cosmo/report",
"edu/report",
"report"
];
const source_options = [
"gemini-pro-2.5", "gemini-flash-2.5", "gemini-pro-3.0", "gemini-flash-3.0",
"claude-sonnet-4.5", "claude-opus-4.1",
"foundational-Claude", "foundational-Gemini",
"first-principles-thinking", "first-principles-claude", "first-principles-gemini",
"conceptual genealogy", "systems-thinking", "narrative-driven",
"case-study-method", "comparative-analysis", "problem-based-learning", "socratic-inquiry"
];
const link_up_options = [
"pkb-knowledge-moc",
"cognitive-science-moc",
"prompt-engineering-moc",
"cosmology-moc"
];
// --- INPUT PROMPTS ---
const title = await tp.system.prompt("Enter Title for YAML:");
const alias1 = await tp.system.prompt("Enter first alias (or press Enter to skip):");
const alias2 = await tp.system.prompt("Enter second alias (or press Enter to skip):");
// --- SUGGESTERS ---
const selectedType = await tp.system.suggester(type_options, type_options, false, "Select Report Type:");
const selectedSource = await tp.system.suggester(source_options, source_options, false, "Select Source / Methodology:");
const selectedLinkUp = await tp.system.suggester(link_up_options, link_up_options, false, "Link Up to MOC:");
// Tags 1 & 2 from Group A (Domains)
const tag1 = await tp.system.suggester(groupA_Tags, groupA_Tags, false, "Select Tag 01 (Domain):");
const tag2 = await tp.system.suggester(groupA_Tags, groupA_Tags, false, "Select Tag 02 (Domain):");
// Tags 3-6 from Group B (Specifics)
const tag3 = await tp.system.suggester(groupB_Tags, groupB_Tags, false, "Select Tag 03 (Concept):");
const tag4 = await tp.system.suggester(groupB_Tags, groupB_Tags, false, "Select Tag 04 (Concept):");
const tag5 = await tp.system.suggester(groupB_Tags, groupB_Tags, false, "Select Tag 05 (Concept):");
const tag6 = await tp.system.suggester(groupB_Tags, groupB_Tags, false, "Select Tag 06 (Concept):");
_%>
---
aliases:
  - "<% alias1 %>"
  - "<% alias2 %>"
tags:
  - "type/report"
  - "year/<% tp.date.now("YYYY") %>"
  - "<% tag1 %>"
  - "<% tag2 %>"
  - "<% tag3 %>"
  - "<% tag4 %>"
  - "<% tag5 %>"
  - "<% tag6 %>"
source: "<% selectedSource %>"
id: "<% tp.date.now("YYYYMMDDHHmmss") %>"
created: "<% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>"
week: "[[<% tp.date.now("gggg-[W]WW") %>]]"
month: "[[<% tp.date.now("YYYY-MM") %>]]"
quarter: "[[<% tp.date.now("YYYY-[Q]Q") %>]]"
year: "[[<% tp.date.now("YYYY") %>]]"
type: "<% selectedType %>"
link-up:
  - "[[<% selectedLinkUp %>]]"
link-related:
  - "[[<% tp.date.now("YYYY-MM-DD") %>|Daily-Note]]"
---
# <% title %>

<% tp.file.cursor() %>