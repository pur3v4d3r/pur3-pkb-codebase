<%*
/* ---------------------------------------------------------------
HYBRID WORKFLOW REPORT TEMPLATE
Synthesizes PKM workflows with Prompt Engineering automation
*/
// --- CONFIGURATION: DATA LISTS ---
// LIST A: Workflow & Application Domains
const groupA_Tags = [
"knowledge-workflow/processing",
"knowledge-workflow/output",
"prompt-application/productivity",
"prompt-application/writing",
"prompt-application/coding",
"advanced-prompting/agents",
"obsidian/advanced",
"pkm/workflow"
];
// LIST B: Automation & Integration Specifics
const groupB_Tags = [
"obsidian/advanced/templater-scripts",
"obsidian/advanced/dataviewjs",
"prompt-workflow/ideation",
"prompt-application/productivity/summarization",
"prompt-application/writing/content-creation",
"advanced-prompting/programming/code-generation",
"knowledge-workflow/capture/quick-capture",
"knowledge-workflow/synthesis/integration",
"concept/task-decomposition",
"concept/automation",
"concept/prompt-template",
"concept/system-message"
];
// --- METADATA LISTS ---
const type_options = [
"prompt/report",
"pkb/report",
"report",
"edu/report"
];
const source_options = [
"gemini-pro-2.5", "gemini-flash-2.5", "gemini-pro-3.0", "gemini-flash-3.0",
"claude-sonnet-4.5", "claude-opus-4.1",
"foundational-Claude", "foundational-Gemini",
"first-principles-thinking", "systems-thinking"
];
const link_up_options = [
"prompt-engineering-moc",
"pkb-knowledge-moc",
"cognitive-science-moc"
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