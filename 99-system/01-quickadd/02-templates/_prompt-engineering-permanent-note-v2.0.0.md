<%*
// 1. DATA DEFINITIONS
// -------------------
const maturityLevels = [
  "needs-review", "seedling", "developing", "budding", "evergreen"
];

const confidenceLevels = [
  "speculative", "provisional", "moderate", "established", "high"
];

const groupC3_Tags = [
  "advanced-prompting/agents", "advanced-prompting/chain-systems", "advanced-prompting/function-calling",
  "advanced-prompting/multi-modal", "advanced-prompting/programming", "advanced-prompting/rag",
  "context-management/compression", "context-management/injection", "context-management/memory",
  "context-management/window", "llm-architecture/context-window", "llm-architecture/model-family",
  "llm-architecture/model-size", "llm-architecture/training", "llm-architecture/transformer",
  "llm-capability/generation", "llm-capability/knowledge", "llm-capability/reasoning",
  "llm-capability/understanding", "llm-limitation", "prompt-application/analysis",
  "prompt-application/coding", "prompt-application/creative", "prompt-application/education",
  "prompt-application/productivity", "prompt-application/writing", "prompt-engineering/anatomy",
  "prompt-engineering/evaluation", "prompt-engineering/optimization", "prompt-engineering/principles",
  "prompt-engineering/theory", "prompt-pattern/context-control", "prompt-pattern/error-handling",
  "prompt-pattern/multi-turn", "prompt-pattern/output-format", "prompt-pattern/persona",
  "prompt-pattern/template", "prompt-safety/adversarial", "prompt-safety/alignment",
  "prompt-safety/bias", "prompt-safety/content-policy", "prompt-safety/information-security",
  "prompt-workflow/deployment", "prompt-workflow/evaluation", "prompt-workflow/ideation",
  "prompt-workflow/prototyping", "prompt-workflow/version-control", "prompting-technique/chain-of-thought",
  "prompting-technique/few-shot", "prompting-technique/meta-prompting", "prompting-technique/react",
  "prompting-technique/reasoning", "prompting-technique/reflection", "prompting-technique/zero-shot"
];

const groupD_Tags = [
  "attention", "creative-thinking", "critical-thinking", "error-monitoring", "planning",
  "problem-solving", "reasoning", "self-regulation", "attention-management",
  "cognitive-load-management", "cognitive-load-theory", "expertise-development",
  "instructional-design-pkm", "learning-processes", "metacognitive-monitoring",
  "metacognitive-pkm", "skill-acquisition"
];

const groupI_Tags = [
  "advanced-prompting/agents/autonomous", "advanced-prompting/agents/multi-agent", "advanced-prompting/agents/planning",
  "advanced-prompting/agents/tool-use", "advanced-prompting/rag/context-injection", "advanced-prompting/rag/hybrid-search",
  "advanced-prompting/rag/retrieval", "llm-limitation/bias", "llm-limitation/hallucination",
  "llm-limitation/reasoning-failures", "prompt-pattern/context-control/constraints", "prompt-pattern/context-control/framing",
  "prompt-pattern/context-control/perspective", "prompt-pattern/error-handling/clarification",
  "prompt-pattern/error-handling/fallback", "prompt-pattern/error-handling/validation",
  "prompt-pattern/multi-turn/context-threading", "prompt-pattern/multi-turn/conversation",
  "prompt-pattern/multi-turn/state-management", "prompt-pattern/output-format/code",
  "prompt-pattern/output-format/creative", "prompt-pattern/output-format/markdown",
  "prompt-pattern/output-format/structured-data", "prompt-pattern/persona/expertise",
  "prompt-pattern/persona/role-assignment", "prompt-pattern/persona/style",
  "prompt-pattern/template/fill-in-blank", "prompt-pattern/template/formulaic",
  "prompt-pattern/template/structured", "prompt-safety/adversarial/defense",
  "prompt-safety/adversarial/jailbreaking", "prompt-safety/adversarial/prompt-injection",
  "prompting-technique/chain-of-thought/basic", "prompting-technique/chain-of-thought/self-consistency",
  "prompting-technique/chain-of-thought/zero-shot", "prompting-technique/few-shot/diversity",
  "prompting-technique/few-shot/example-ordering", "prompting-technique/few-shot/example-selection",
  "prompting-technique/meta-prompting/optimization", "prompting-technique/meta-prompting/prompt-generation",
  "prompting-technique/meta-prompting/self-improvement", "prompting-technique/react/iteration",
  "prompting-technique/react/reasoning-acting", "prompting-technique/react/tool-use",
  "prompting-technique/reasoning/decomposition", "prompting-technique/reasoning/graph-of-thoughts",
  "prompting-technique/reasoning/step-by-step", "prompting-technique/reasoning/tree-of-thoughts",
  "prompting-technique/reflection/refinement", "prompting-technique/reflection/self-critique",
  "prompting-technique/reflection/verification", "prompting-technique/zero-shot/instruction",
  "prompting-technique/zero-shot/task-specification"
];

// 2. HELPER FUNCTIONS
// -------------------

// Determine icon based on tag string (Optimized Lookup)
function getIconForTag(tag) {
  // Exact prefix matches first (high priority)
  if (tag.startsWith("type/")) return "📑";
  if (tag.startsWith("status/")) return "🚦";
  if (tag.startsWith("context/")) return "🌐";
  if (tag.startsWith("source/")) return "📚";
  if (tag.startsWith("maturity/")) return "🍷";
  if (tag.startsWith("mode/")) return "⚙️";
  if (tag.startsWith("validation/")) return "📏";
  if (tag.startsWith("complexity/")) return "📏";
  if (tag.startsWith("nature/")) return "🌿";
  if (tag.startsWith("model/")) return "🤖";
  if (tag.startsWith("concept/")) return "💡";

  // Keyword includes (Category matches)
  if (tag.includes("obsidian") || tag.includes("dataview") || tag.includes("plugin")) return "💎";
  if (tag.includes("pkm") || tag.includes("pkb") || tag.includes("zettelkasten") || tag.includes("para")) return "🧠";
  if (tag.includes("workflow") || tag.includes("system") || tag.includes("architecture")) return "🔄";
  if (tag.includes("information-architecture") || tag.includes("taxonomy")) return "🗂️";
  if (tag.includes("neuro") || tag.includes("brain")) return "🧬";
  if (tag.includes("memory") || tag.includes("encoding") || tag.includes("recall")) return "💾";
  if (tag.includes("learning") || tag.includes("education") || tag.includes("student") || tag.includes("andragogy")) return "🎓";
  if (tag.includes("attention") || tag.includes("focus")) return "🎯";
  if (tag.includes("reasoning") || tag.includes("logic") || tag.includes("thinking") || tag.includes("decision")) return "💡";
  if (tag.includes("cognitive") || tag.includes("psychology") || tag.includes("behavior")) return "🧩";
  if (tag.includes("regulation") || tag.includes("motivation") || tag.includes("self")) return "💪";
  if (tag.includes("prompt") || tag.includes("chain-of-thought")) return "💬";
  if (tag.includes("llm") || tag.includes("gpt") || tag.includes("claude") || tag.includes("gemini") || tag.includes("artificial")) return "🤖";
  if (tag.includes("agent") || tag.includes("rag")) return "🕵️";
  if (tag.includes("safety") || tag.includes("bias")) return "🛡️";
  if (tag.includes("cosmology") || tag.includes("universe")) return "🌌";
  if (tag.includes("research") || tag.includes("analysis") || tag.includes("study")) return "🔬";

  // Default
  return "🔹";
}

function formatTagsForDisplay(tags) {
  return tags.map(tag => {
    const icon = getIconForTag(tag);
    const cleanText = tag.split("/").join(" › ");
    // FIX: Variables inserted into template literal
    return `${icon} ${cleanText}`;
  });
}

// 3. EXECUTION & PROMPTS
// ----------------------

// Prompt for Title
let title = await tp.system.prompt("Enter Note Title (Concept Name):");
if (title == null) { return; } // Exit if canceled

// Rename the file to match the title (Best Practice)
await tp.file.rename(title);

// Prompt for Aliases
const alias1 = await tp.system.prompt("Enter Alias 1 (Press Enter to skip):");
const alias2 = await tp.system.prompt("Enter Alias 2 (Press Enter to skip):");

// Construct Alias Array for YAML
let aliases = [];
if (alias1) aliases.push(alias1);
if (alias2) aliases.push(alias2);

// Metadata Prompts
const maturity = await tp.system.suggester(maturityLevels, maturityLevels, false, "Select Maturity Level:");
const confidence = await tp.system.suggester(confidenceLevels, confidenceLevels, false, "Select Confidence Level:");

// Sort arrays ONCE to ensure display and values match index-for-index
groupC3_Tags.sort();
groupD_Tags.sort();
groupI_Tags.sort();

const groupC3_Display = formatTagsForDisplay(groupC3_Tags);
const groupD_Display = formatTagsForDisplay(groupD_Tags);
const groupI_Display = formatTagsForDisplay(groupI_Tags);

// Tag Prompts (Using safe defaults if user escapes)
const tag1 = await tp.system.suggester(groupC3_Display, groupC3_Tags, false, "TAG 1 (Core)") || "unassigned";
const tag2 = await tp.system.suggester(groupC3_Display, groupC3_Tags, false, "TAG 2 (Secondary)") || "unassigned";
const tag3 = await tp.system.suggester(groupD_Display, groupD_Tags, false, "TAG 3 (Cognitive)") || "unassigned";
const tag4 = await tp.system.suggester(groupI_Display, groupI_Tags, false, "TAG 4 (Implementation)") || "unassigned";
const tag5 = await tp.system.suggester(groupI_Display, groupI_Tags, false, "TAG 5 (Extra)") || "unassigned";

// Date calculations
const dateNow = tp.date.now("YYYY-MM-DD");
const timeNow = tp.date.now("HH:mm:ss");
const year = tp.date.now("YYYY");
const id = tp.date.now("YYYYMMDDHHmmss");

// 4. OUTPUT
// ---------
_%>
- --
aliases: [<% aliases.map(a => `"${a}"`).join(", ") %>]
tags:
  - "type/permanent"
  - "year/<% year %>"
  - "<% tag1 %>"
  - "<% tag2 %>"
  - "<% tag3 %>"
  - "<% tag4 %>"
  - "<% tag5 %>"
source: "report"
id: "<% id %>"
created: "<% dateNow %>T<% timeNow %>"
modified: "<% dateNow %>T<% timeNow %>"
week: "<% tp.date.now("gggg-[W]WW") %>"
month: "<% tp.date.now("YYYY-MM") %>"
quarter: "<% tp.date.now("YYYY-[Q]Q") %>"
year: "<% year %>"
type: "permanent-note"
maturity: "<% maturity || 'needs-review' %>"
confidence: "<% confidence || 'speculative' %>"
link-up:
  - "[[prompt-engineering-moc]]"
link-related:
  - "[[<% dateNow %>|Daily-Note]]"
- --

# <% title %>

