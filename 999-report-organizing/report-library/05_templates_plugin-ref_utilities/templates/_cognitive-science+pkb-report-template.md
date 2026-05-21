<%*
/* ---------------------------------------------------------------
HYBRID LEARNING REPORT TEMPLATE
Synthesizes Cognitive Science with Knowledge Management
*/
// --- CONFIGURATION: DATA LISTS ---
// LIST A: Learning & Knowledge Domains
const groupA_Tags = [
"cognitive-science/memory",
"learning-theory/constructivism",
"pkm/theory",
"digital-garden/philosophy",
"knowledge-work/learning",
"knowledge-work/thinking",
"self-improvement/skill-development",
"critical-thinking/synthesis"
];
// LIST B: Cognitive Scaffolding & Methods
const groupB_Tags = [
"pkm/principles/progressive-summarization",
"pkm/principles/linking-thinking",
"cognitive-science/memory/retrieval",
"cognitive-science/metacognition/reflection",
"knowledge-work/learning/mastery",
"digital-garden/structure/evergreen-notes",
"self-improvement/mental-models/frameworks",
"learning-theory/constructivism/scaffolding",
"concept/knowledge-synthesis",
"concept/second-brain",
"concept/external-cognition",
"concept/elaboration"
];
// --- METADATA LISTS ---
const type_options = [
"edu/report",
"cog-psy/report",
"pkb/report",
"report"
];
const source_options = [
"first-principles-thinking", "conceptual genealogy",
"systems-thinking", "socratic-inquiry", "problem-based-learning",
"gemini-pro-2.5", "claude-sonnet-4.5"
];
const link_up_options = [
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
const tag1 = await tp.system.suggester(groupA_Tags, groupA_Tags, false, "Select Tag 01 (Domain):");
const tag2 = await tp.system.suggester(groupA_Tags, groupA_Tags, false, "Select Tag 02 (Domain):");
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