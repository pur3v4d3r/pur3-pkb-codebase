<%*
/* ---------------------------------------------------------------
   MASTER REPORT SKELETON TEMPLATE
   Integrated with Pur3v4d3r Tag Taxonomy & Metadata Requirements
   ---------------------------------------------------------------
*/
// --- CONFIGURATION: PRE-DEFINED LISTS ---
// 1. REPORT TYPES (Strict Selection)
const typeList = [
    "cog-psy/report",
    "prompt/report",
    "pkb/report",
    "cosmo/report",
    "edu/report",
    "report"
];
// 2. SOURCE ORIGINS (Strict Selection)
const sourceList = [
    "gemini-pro-2.5",
    "gemini-flash-2.5",
    "gemini-pro-3.0",
    "gemini-flash-3.0",
    "claude-sonnet-4.5",
    "claude-opus-4.1",
    "foundational-Claude",
    "foundational-Gemini",
    "first-principles-thinking",
    "first-principles-claude",
    "first-principles-gemini",
    "conceptual genealogy",
    "systems-thinking",
    "narrative-driven",
    "case-study-method",
    "comparative-analysis",
    "problem-based-learning",
    "socratic-inquiry"
];
// 3. LINK-UP MOCs (Strict Selection)
const linkUpList = [
    "[[99-archive/05-moc's/cognitive-science-moc]]",
    "[[pkb-knowledge-moc]]",
    "[[prompt-engineering-moc]]",
    "[[cosmology-moc]]"
];
// --- TAXONOMY ARRAYS (Derived from Tag Taxonomy File) ---
// GROUP A: High-Level Domains (For Tags 01 & 02)
// Used to establish the broad context of the note.
const groupA_Tags = [
    "pkm", "pkb", "note-taking", "knowledge-workflow", "obsidian", 
    "information-architecture", "knowledge-graph", "digital-garden", 
    "productivity", "cognitive-science", "critical-thinking", 
    "self-regulation", "learning-theory", "self-improvement", 
    "prompt-engineering", "prompting-technique", "prompt-pattern", 
    "llm-capability", "llm-architecture", "advanced-prompting", 
    "prompt-safety", "context-management", "prompt-workflow", "cosmology"
];
// GROUP B: Granular Concepts (For Tags 03, 04, & 05)
// Specific sub-concepts derived from your taxonomy hierarchy.
const groupB_Tags = [
    // PKM & PKB
    "pkm/theory", "pkm/methodology", "pkm/workflow", "pkb/architecture", 
    "pkb/design", "pkb/components", "note-taking/zettelkasten", 
    "obsidian/plugins", "obsidian/advanced", "knowledge-graph/theory",
    
    // Psychology & Cognitive
    "cognitive-science/metacognition", "cognitive-science/memory", 
    "cognitive-science/attention", "cognitive-science/mental-models",
    "critical-thinking/analysis", "critical-thinking/logic", 
    "self-regulation/goal-setting", "learning-theory/constructivism",
    "self-improvement/deliberate-practice", "self-improvement/mental-models",
    
    // Prompt Engineering
    "prompt-engineering/principles", "prompt-engineering/optimization",
    "prompting-technique/chain-of-thought", "prompting-technique/reasoning", 
    "prompting-technique/few-shot", "prompting-technique/meta-prompting",
    "prompt-pattern/persona", "prompt-pattern/context-control",
    "llm-capability/reasoning", "llm-architecture/transformer",
    "advanced-prompting/agents", "advanced-prompting/rag",
    "prompt-safety/alignment", "context-management/window",
    
    // Cross-Cutting Concepts
    "concept/emergence", "concept/atomic-notes", "concept/transfer",
    "concept/first-principles", "concept/synthesis"
];
// --- INPUT SYSTEM ---
// 1. Text Prompts
const title = await tp.system.prompt("Enter YAML Title (Filename handled by QuickAdd):");
const alias1 = await tp.system.prompt("Enter Alias 1 (Press Enter to skip):");
const alias2 = await tp.system.prompt("Enter Alias 2 (Press Enter to skip):");
// 2. Metadata Suggesters
const type = await tp.system.suggester(typeList, typeList, false, "Select Report TYPE:");
const source = await tp.system.suggester(sourceList, sourceList, false, "Select SOURCE:");
const linkUp = await tp.system.suggester(linkUpList, linkUpList, false, "Select LINK-UP MOC:");
// 3. Tag Suggesters (Hierarchical Selection)
// Group A (Domains)
const tag1 = await tp.system.suggester(groupA_Tags, groupA_Tags, false, "Select Tag 01 (Domain):");
const tag2 = await tp.system.suggester(groupA_Tags, groupA_Tags, false, "Select Tag 02 (Domain):");
const tag3 = await tp.system.suggester(groupB_Tags, groupB_Tags, false, "Select Tag 03 (Domain):");
// Group B (Concepts)
const tag4 = await tp.system.suggester(groupB_Tags, groupB_Tags, false, "Select Tag 04 (Concept):");
const tag5 = await tp.system.suggester(groupB_Tags, groupB_Tags, false, "Select Tag 05 (Concept):");
const tag6 = await tp.system.suggester(groupB_Tags, groupB_Tags, false, "Select Tag 06 (Concept):");
const tag7 = await tp.system.suggester(groupB_Tags, groupB_Tags, false, "Select Tag 07 (Concept):");
const tag8 = await tp.system.suggester(groupB_Tags, groupB_Tags, false, "Select Tag 08 (Concept):");
// 4. Date Calculations
const dateNow = tp.date.now("YYYY-MM-DD");
const timeNow = tp.date.now("HH:mm:ss");
const year = tp.date.now("YYYY");
const id = tp.date.now("YYYYMMDDHHmmss");
_%>
---
aliases:
  - "<% alias1 %>"
  - "<% alias2 %>"
tags:
  - "type/report"
  - "year/<% year %>"
  - "<% tag1 %>"
  - "<% tag2 %>"
  - "<% tag3 %>"
  - "<% tag4 %>"
  - "<% tag5 %>"
  - "<% tag6 %>"
  - "<% tag7 %>"
  - "<% tag8 %>"
source: "<% source %>"
id: "<% id %>"
created: "<% dateNow %>T<% timeNow %>"
week: "[[<% tp.date.now("gggg-[W]WW") %>]]"
month: "[[<% tp.date.now("YYYY-MM") %>]]"
quarter: "[[<% tp.date.now("YYYY-[Q]Q") %>]]"
year: "[[<% year %>]]"
type: "<% type %>"
link-up:
  - "<% linkUp %>"
link-related:
  - "[[<% dateNow %>|Daily-Note]]"
---
# <% title %>

<% tp.file.cursor() %>