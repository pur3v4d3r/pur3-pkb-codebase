<%*
/* ---------------------------------------------------------------
SYSTEMS SYNTHESIS & COSMOLOGY REPORT TEMPLATE
For First Principles, Cross-Domain connections, and Cosmology
*/
// --- CONFIGURATION: DATA LISTS ---
// LIST A: High-Level Systems & Frameworks
const groupA_Tags = [
"concept",
"concept/emergence",
"concept/networked-thought",
"knowledge-graph/theory",
"critical-thinking/analysis",
"critical-thinking/synthesis",
"first-principles",
"cosmology",
"systems-thinking"
];
// LIST B: Cross-Cutting Concepts & Deep Theory
const groupB_Tags = [
"concept/emergence",
"concept/serendipity",
"concept/mental-representation",
"concept/knowledge-synthesis",
"concept/transfer",
"knowledge-graph/theory/emergence",
"knowledge-graph/theory/networks",
"critical-thinking/logic/formal",
"critical-thinking/problem-solving/problem-framing",
"critical-thinking/synthesis/pattern-recognition",
"cosmology/theoretical",
"cosmology/models"
];
// --- METADATA LISTS ---
const type_options = [
"cosmo/report",
"report",
"cog/psy-report",
"pkb/report",
"prompt/report"
];
const source_options = [
"first-principles-thinking", "first-principles-claude", "first-principles-gemini",
"systems-thinking", "conceptual genealogy", "comparative-analysis",
"foundational-Claude", "foundational-Gemini",
"socratic-inquiry"
];
const link_up_options = [
"cosmology-moc",
"cognitive-science-moc",
"pkb-knowledge-moc",
"prompt-engineering-moc"
];
// --- INPUT PROMPTS ---
const title = await tp.system.prompt("Enter Title for YAML:");
const alias1 = await tp.system.prompt("Enter first alias (or press Enter to skip):");
const alias2 = await tp.system.prompt("Enter second alias (or press Enter to skip):");
// --- SUGGESTERS ---
const selectedType = await tp.system.suggester(type_options, type_options, false, "Select Report Type:");
const selectedSource = await tp.system.suggester(source_options, source_options, false, "Select Source / Methodology:");
const selectedLinkUp = await tp.system.suggester(link_up_options, link_up_options, false, "Link Up to MOC:");
const tag1 = await tp.system.suggester(groupA_Tags, groupA_Tags, false, "Select Tag 01 (System):");
const tag2 = await tp.system.suggester(groupA_Tags, groupA_Tags, false, "Select Tag 02 (System):");
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