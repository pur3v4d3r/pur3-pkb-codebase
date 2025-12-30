<%*
/* ---------------------------------------------------------------
  MASTER GENERAL-NOTE TEMPLATE v2.1 (CONDENSED)
  INTEGRATED TAXONOMY EDITION
  ---------------------------------------------------------------
*/
// --- CONFIGURATION: PRE-DEFINED LISTS ---
// 1. NOTE TYPES (Permanent Notes)
const typeList = [
    "reference",
    "concept",
    "principle",
    "mental-model",
    "framework",
    "theory",
    "insight",
    "strategy",
    "definition",
    "permanent-note",
    "literature",
    "practice-log",
    "technique",
    "case-study",
    "tutorial",
    "experiment"
];
// 2. SOURCE ORIGINS
const sourceList = [
    "original-synthesis",
    "literature-synthesis",
    "report",
    "book",
    "article",
    "paper",
    "conversation",
    "experience",
    "course",
    "video",
    "podcast",
    "gemini-pro-2.5",
    "gemini-flash-2.5",
    "gemini-pro-3.0",
    "gemini-flash-3.0",
    "claude-sonnet-4.5",
    "claude-opus-4.1",
    "gpt-4o",
    "open-source-local"
];
// 3. LINK-UP MOCs
const linkUpList = [
    "[[99-archive/05-moc's/cognitive-science-moc]]",
    "[[pkb-&-pkm-moc]]",
    "[[educational-psychology-moc]]",
    "[[prompt-engineering-moc]]",
    "[[cosmology-moc]]",
    "[[learning-theory-moc]]",
    "[[neuroscience-moc]]"
];
// 4. MATURITY LEVELS
const maturityLevels = [
    "seedling", // Initial capture
    "budding", // Basic structure established
    "developing", // Active refinement
    "evergreen", // Mature, stable
    "needs-review" // Flagged for revision
];
// 5. CONFIDENCE LEVELS
const confidenceLevels = [
    "speculative", // Hypothesis/early thinking
    "provisional", // Needs verification
    "moderate", // Reasonably confident
    "high", // Well-supported
    "established" // Academically verified
];
// --- TAXONOMY ARRAYS ---
// GROUP A: High-Level Domains, Dimensions (L1 & L2) & Meta-Tags
const groupA_Tags = [
    // --- DOMAINS (L1) ---
    "pkm", "pkb", "knowledge-work", "second-brain", "productivity-systems",
    "cognitive-science", "neuroscience", "behavioral-science", "learning-science",
    "prompt-engineering", "artificial-intelligence", "cosmology",
    // --- SUB-DISCIPLINES (L2 - PKM) ---
    "vault-architecture", "knowledge-workflow", "information-architecture",
    "digital-garden", "note-taking", "obsidian", "productivity",
    // --- SUB-DISCIPLINES (L2 - COG SCI) ---
    "cognitive-psychology", "cognitive-neuroscience", "cognitive-linguistics",
    "cognitive-development", "educational-psychology", "instructional-design",
    "human-factors", "decision-science", "experimental-psychology", "computational-modeling",
    // --- SUB-DISCIPLINES (L2 - PROMPT ENG) ---
    "prompt-engineering/theory", "prompt-engineering/principles", "prompt-engineering/optimization",
    "llm-capability", "llm-architecture", "prompt-safety", "advanced-prompting",
    // --- MULTI-DIMENSIONAL META TAGS ---
    // Note Type
    "type/fleeting", "type/literature", "type/permanent", "type/moc", "type/reference",
    "type/tutorial", "type/dashboard", "type/guide", "type/framework",
    "type/reflection", "type/review", "type/technique", "type/pattern",
    "type/experiment", "type/analysis", "type/case-study", "type/comparison",
    "type/prompt-library", "type/gemini-gem", "type/claude-project",
    // Development Status
    "status/seedling", "status/budding", "status/evergreen", "status/review", "status/archived",
    "status/in-progress", "status/complete", "status/read", "status/not-read",
    "status/experimental", "status/proven", "status/deprecated", "status/under-revision", "status/production",
    // Source
    "source/book", "source/article", "source/blog", "source/video", "source/podcast",
    "source/course", "source/documentation", "source/community", "source/conference",
    "source/workshop", "source/experience", "source/original", "source/paper", "source/conversation",
    // Context
    "context/theoretical", "context/practical", "context/tutorial", "context/reference", "context/meta",
    "context/experimental", "context/applied", "context/personal", "context/professional",
    "context/teaching", "context/research",
    // Maturity Level
    "maturity/beginner", "maturity/intermediate", "maturity/advanced", "maturity/expert",
    "maturity/emerging", "maturity/established", "maturity/standard", "maturity/deprecated",
    // Content Nature
    "nature/conceptual", "nature/procedural", "nature/declarative", "nature/reflective",
    // Cognitive Mode
    "mode/analytical", "mode/synthetic", "mode/reflective", "mode/practical",
    // Model (PE)
    "model/claude", "model/gemini", "model/gpt", "model/local", "model/agnostic",
    "model/open-source",
    // Complexity (PE)
    "complexity/basic", "complexity/intermediate", "complexity/advanced", "complexity/expert",
    // Validation (PE)
    "validation/tested", "validation/reported", "validation/theoretical", "validation/failed"
];
// GROUP B: Major Systems, Frameworks, & Methodologies (L3)
const groupB_Tags = [
    // --- PKM SYSTEMS & METHODS ---
    "capture-system", "processing-workflow", "organization-system", "synthesis-workflow",
    "retrieval-system", "review-system", "note-types", "note-organization", "knowledge-graph",
    "index-systems", "dashboard-design", "tag-taxonomy", "metadata-systems", "linking-strategy",
    "zettelkasten", "para-method", "gtd", "building-second-brain", "evergreen-notes",
    "cornell-method", "outline-method", "mind-mapping", "concept-mapping",
    "progressive-summarization", "atomic-notes", "moc-system", "structure-notes",
    // --- OBSIDIAN ECOSYSTEM ---
    "dataview", "templater", "quickadd", "tasks-plugin", "smart-connections",
    "meta-bind", "copilot-plugin", "excalidraw", "breadcrumbs", "automation",
    "javascript", "api-integration", "version-control",
    // --- COGNITIVE SYSTEMS ---
    "memory-systems", "attention", "perception", "executive-function",
    "language-processing", "reasoning", "problem-solving", "learning-processes",
    "metacognition", "self-regulation", "motivation", "emotion-regulation",
    "skill-acquisition", "conceptual-learning", "expertise-development",
    // --- PROMPT TECHNIQUES ---
    "prompting-technique/zero-shot", "prompting-technique/few-shot",
    "prompting-technique/chain-of-thought", "prompting-technique/reasoning",
    "prompting-technique/react", "prompting-technique/reflection",
    "prompting-technique/meta-prompting", "prompt-pattern/persona",
    "prompt-pattern/context-control", "prompt-pattern/output-format",
    "advanced-prompting/agents", "advanced-prompting/rag",
    "context-management/window", "context-management/memory"
];
// GROUP C: Granular Concepts, Mechanisms, & Leaf Nodes (L4)
const groupC_Tags = [
    // --- COGNITIVE MECHANISMS ---
    // Memory
    "working-memory", "long-term-memory", "episodic-memory", "semantic-memory",
    "procedural-memory", "encoding", "consolidation", "retrieval", "reconsolidation",
    "interference", "phonological-loop", "visuospatial-sketchpad", "central-executive",
    // Attention & Executive
    "selective-attention", "divided-attention", "sustained-attention", "inhibitory-control",
    "cognitive-flexibility", "planning", "task-switching", "error-monitoring",
    "response-inhibition", "conflict-monitoring",
    // Learning Phenomena
    "spacing-effect", "testing-effect", "generation-effect", "desirable-difficulties",
    "interleaving", "elaborative-encoding", "transfer-of-learning", "implicit-learning",
    "explicit-learning", "cognitive-load-theory", "intrinsic-load", "extraneous-load",
    "germane-load", "working-memory-capacity",
    // Metacognition
    "metamemory", "metacomprehension", "self-regulated-learning", "calibration",
    // --- CRITICAL THINKING & REASONING ---
    "deductive-reasoning", "inductive-reasoning", "abductive-reasoning", "analogical-reasoning",
    "critical-thinking/analysis", "critical-thinking/logic", "critical-thinking/evaluation",
    "critical-thinking/bias-detection", "cognitive-bias", "logical-fallacies",
    // --- PKM SPECIFICS ---
    "note-templates", "frontmatter-design", "template-automation", "quick-capture",
    "daily-notes", "meeting-notes", "wiki-links", "backlinks", "unlinked-mentions",
    "transclusion", "tag-strategy", "folder-strategy", "file-naming",
    "search-operators", "dataview-queries", "dataviewjs", "templater-scripts",
    "quickadd-macros", "spaced-repetition", "progressive-review", "orphan-notes",
    "active-recall", "elaborative-interrogation", "self-explanation",
    // --- PROMPT ENGINEERING GRANULAR ---
    "chain-of-thought/self-consistency", "tree-of-thoughts", "graph-of-thoughts",
    "step-by-step", "role-prompting", "system-message", "jailbreaking", "prompt-injection",
    "hallucination", "temperature-control", "top-p-sampling", "token-probability",
    "context-window/optimization", "function-calling", "structured-output",
    // --- CROSS-DOMAIN INTEGRATION ---
    "cognitive-pkm", "evidence-based-pkm", "learning-optimization",
    "memory-systems-design", "attention-architecture", "metacognitive-pkm"
];
// --- HELPER FUNCTION: PRETTY PRINT TAGS ---
function formatTagsForDisplay(tags) {
    return tags.map(tag => {
        let icon = "🔹"; // Default bullet
        // 1. Assign Icons based on Domain Keywords (Prioritize Specificity)
        // Meta / Structure
        if (tag.startsWith("type/")) icon = "📑";
        else if (tag.startsWith("status/")) icon = "🚦";
        else if (tag.startsWith("context/")) icon = "🌐";
        else if (tag.startsWith("source/")) icon = "📚";
        else if (tag.startsWith("maturity/")) icon = "🍷";
        else if (tag.startsWith("mode/")) icon = "⚙️";
        else if (tag.startsWith("validation/") || tag.startsWith("complexity/")) icon = "📏";
        // PKM & Obsidian
        else if (tag.includes("obsidian") || tag.includes("dataview") || tag.includes("plugin")) icon = "💎";
        else if (tag.includes("pkm") || tag.includes("pkb") || tag.includes("zettelkasten")) icon = "🧠";
        else if (tag.includes("workflow") || tag.includes("system")) icon = "🔄";
        // Cognitive Science
        else if (tag.includes("neuro") || tag.includes("brain")) icon = "🧬";
        else if (tag.includes("memory") || tag.includes("encoding") || tag.includes("recall")) icon = "💾";
        else if (tag.includes("learning") || tag.includes("education") || tag.includes("student")) icon = "🎓";
        else if (tag.includes("attention") || tag.includes("focus")) icon = "🎯";
        else if (tag.includes("reasoning") || tag.includes("logic") || tag.includes("thinking")) icon = "💡";
        else if (tag.includes("cognitive") || tag.includes("psychology")) icon = "🧩";
        // Prompt Engineering / AI
        else if (tag.includes("prompt") || tag.includes("chain-of-thought")) icon = "💬";
        else if (tag.includes("llm") || tag.includes("gpt") || tag.includes("claude") || tag.includes("gemini")) icon = "🤖";
        else if (tag.includes("agent") || tag.includes("rag")) icon = "🕵️";
        // Cosmology
        else if (tag.includes("cosmology") || tag.includes("universe")) icon = "🌌";
        // 2. Formatting: Replace slashes with visual arrows for cleaner reading
        let cleanText = tag.split("/").join(" › ");
        return `${icon} ${cleanText}`;
    });
}
// --- INPUT SYSTEM ---
// 1. Prepare Display Arrays (Alphabetical Sort for UI)
const sortedA = groupA_Tags.sort();
const sortedB = groupB_Tags.sort();
const sortedC = groupC_Tags.sort();
const groupA_Display = formatTagsForDisplay(sortedA);
const groupB_Display = formatTagsForDisplay(sortedB);
const groupC_Display = formatTagsForDisplay(sortedC);
// 2. Text Prompts
const title = await tp.system.prompt("Enter Note Title (Concept Name):");
// Exit early if title is cancelled to prevent creating empty files
if (title == null) { return; }
const alias1 = await tp.system.prompt("Enter Alias 1 (Press Enter to skip):");
const alias2 = await tp.system.prompt("Enter Alias 2 (Press Enter to skip):");
// 3. Metadata Suggesters
const type = await tp.system.suggester(typeList, typeList, false, "Select Note TYPE:");
const source = await tp.system.suggester(sourceList, sourceList, false, "Select SOURCE / ORIGIN:");
const linkUp = await tp.system.suggester(linkUpList, linkUpList, false, "Select LINK-UP MOC:");
// 4. Status Tracking Fields
const maturity = await tp.system.suggester(maturityLevels, maturityLevels, false, "Select Maturity Level:");
const confidence = await tp.system.suggester(confidenceLevels, confidenceLevels, false, "Select Confidence Level:");
// 5. Tag Suggesters (Hierarchical Selection)
// Group A: High Level Domains & Dimensions
const tag1 = await tp.system.suggester(groupA_Display, sortedA, false, "Select Tag 01 (Primary Domain/Type):");
const tag2 = await tp.system.suggester(groupA_Display, sortedA, false, "Select Tag 02 (Secondary Domain/Context):");
// Group B: Sub-disciplines & Methods
const tag3 = await tp.system.suggester(groupB_Display, sortedB, false, "Select Tag 03 (System/Methodology):");
const tag4 = await tp.system.suggester(groupB_Display, sortedB, false, "Select Tag 04 (System/Methodology):");
// Group C: Granular Concepts
const tag5 = await tp.system.suggester(groupC_Display, sortedC, false, "Select Tag 05 (Concept/Mechanism):");
const tag6 = await tp.system.suggester(groupC_Display, sortedC, false, "Select Tag 06 (Concept/Mechanism):");
const tag7 = await tp.system.suggester(groupC_Display, sortedC, false, "Select Tag 07 (Concept/Mechanism):");
const tag8 = await tp.system.suggester(groupC_Display, sortedC, false, "Select Tag 08 (Concept/Mechanism):");
// 6. Date Calculations
const dateNow = tp.date.now("YYYY-MM-DD");
const timeNow = tp.date.now("HH:mm:ss");
const year = tp.date.now("YYYY");
const id = tp.date.now("YYYYMMDDHHmmss");
// 7. Calculate Next Review Date (Spaced Repetition)
const nextReview = tp.date.now("YYYY-MM-DD", 7); // 1 week from now
_%>
---
aliases:
  - "<% alias1 %>"
  - "<% alias2 %>"
tags:
  - "type/permanent"
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
modified: "<% dateNow %>T<% timeNow %>"
week: "[[<% tp.date.now("gggg-[W]WW") %>]]"
month: "[[<% tp.date.now("YYYY-MM") %>]]"
quarter: "[[<% tp.date.now("YYYY-[Q]Q") %>]]"
year: "[[<% year %>]]"
type: "<% type %>"
maturity: "<% maturity %>"
confidence: "<% confidence %>"
next-review: "<% nextReview %>"
review-count: 0
link-count: 0
backlink-count: 0
link-up:
  - "<% linkUp %>"
link-related:
  - "[[<% dateNow %>|Daily-Note]]"
---
# <% title %>