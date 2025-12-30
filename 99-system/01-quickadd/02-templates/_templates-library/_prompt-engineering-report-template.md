<%*
/* ---------------------------------------------------------------
PROMPT ENGINEERING REPORT TEMPLATE
Domain: Prompt Engineering, LLMs, AI Architecture
*/
// --- CONFIGURATION: DATA LISTS ---
// LIST A: Primary Domains
const groupA_Tags = [
"prompt-engineering",
"prompt-engineering/theory",
"prompt-engineering/principles",
"prompting-technique",
"prompt-pattern",
"llm-capability",
"llm-architecture",
"advanced-prompting",
"prompt-safety",
"context-management",
"prompt-workflow"
];
// LIST B: Specific Techniques & Architectures
const groupB_Tags = [
"prompting-technique/chain-of-thought",
"prompting-technique/few-shot",
"prompting-technique/reasoning/tree-of-thoughts",
"prompting-technique/meta-prompting",
"prompt-pattern/persona/role-assignment",
"prompt-pattern/context-control/framing",
"llm-capability/reasoning/logical",
"llm-architecture/transformer/attention",
"advanced-prompting/agents/autonomous",
"advanced-prompting/rag",
"prompt-safety/adversarial/prompt-injection",
"context-management/window/optimization",
"concept/instruction-following",
"concept/in-context-learning",
"concept/token-probability",
"concept/temperature-control"
];
// --- METADATA LISTS ---
const type_options = [
"prompt/report",
"cog-psy/report",
"pkb/report",
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
"prompt-engineering-moc",
"cognitive-science-moc",
"pkb-knowledge-moc",
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