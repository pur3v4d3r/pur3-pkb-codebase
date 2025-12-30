<%*
/* ---------------------------------------------------------------
  MASTER GENERAL-NOTE TEMPLATE v2.2
  COMPLETE TAXONOMY INTEGRATION (HYBRID HIERARCHY)
  ---------------------------------------------------------------
*/
// --- CONFIGURATION: PRE-DEFINED LISTS ---
// 1. NOTE TYPES (Matches your "type/" tags but for the 'type' property)
const typeList = [  
    "permanent-note", "reference", "concept", "principle", "mental-model", 
    "framework", "theory", "insight", "strategy", "definition", "literature", 
    "practice-log", "technique", "case-study", "tutorial", "experiment", 
    "guide", "dashboard", "reflection", "review", "pattern", "analysis", 
    "comparison", "prompt-library", "gemini-gem", "claude-project", "fleeting", "moc"
];
// 2. SOURCE ORIGINS
const sourceList = [
    "original-synthesis", "literature-synthesis", "report", "book", "article", 
    "paper", "conversation", "experience", "course", "video", "podcast", 
    "blog", "documentation", "community", "conference", "workshop",
    "gemini-pro-2.5", "gemini-flash-2.5", "gemini-pro-3.0", "gemini-flash-3.0", 
    "claude-sonnet-4.5", "claude-opus-4.1", "gpt-4o", "local-llm"
];
// 3. LINK-UP MOCs
const linkUpList = [
    "[[99-archive/05-moc's/cognitive-science-moc]]", "[[pkb-&-pkm-moc]]", "[[educational-psychology-moc]]", 
    "[[prompt-engineering-moc]]", "[[cosmology-moc]]", "[[learning-theory-moc]]", 
    "[[neuroscience-moc]]", "[[artificial-intelligence-moc]]"
];
// 4. STATUS & MATURITY
const maturityLevels = ["seedling", "budding", "developing", "evergreen", "needs-review"];
const confidenceLevels = ["speculative", "provisional", "moderate", "high", "established"];
// --- MASTER TAXONOMY ARRAYS ---
// GROUP A: Meta-Dimensions, Contexts, Status, & Top-Level Domains (L1/L2)
const groupA_Tags = [
    // --- DOMAINS (L1) ---
    "pkm", "pkb", "knowledge-work", "second-brain", "productivity-systems", "productivity",
    "cognitive-science", "neuroscience", "behavioral-science", "learning-science",
    "prompt-engineering", "artificial-intelligence", "cosmology", "digital-garden",
    "information-architecture", "knowledge-graph", "note-taking", "obsidian",
    "psychology", "critical-thinking", "self-regulation", "learning-theory", "self-improvement",
    // --- SUB-DOMAINS (L2 High Level) ---
    "cognitive-psychology", "cognitive-neuroscience", "cognitive-linguistics", "cognitive-development",
    "cognitive-anthropology", "educational-psychology", "instructional-design", "human-factors",
    "decision-science", "cognitive-ergonomics", "experimental-psychology", "computational-modeling",
    "neuroimaging", "psychometrics", "vault-architecture", "knowledge-workflow", 
    // --- META: TYPE ---
    "type/fleeting", "type/literature", "type/permanent", "type/moc", "type/reference",
    "type/tutorial", "type/dashboard", "type/guide", "type/framework", "type/practice-log",
    "type/reflection", "type/review", "type/technique", "type/pattern", "type/synthesis",
    "type/experiment", "type/analysis", "type/case-study", "type/comparison", 
    "type/prompt-library", "type/gemini-gem", "type/claude-project", "type/template",
    // --- META: STATUS ---
    "status/seedling", "status/budding", "status/evergreen", "status/review", "status/archived",
    "status/in-progress", "status/complete", "status/read", "status/not-read", 
    "status/experimental", "status/proven", "status/deprecated", "status/under-revision", "status/production",
    // --- META: CONTEXT ---
    "context/theoretical", "context/practical", "context/tutorial", "context/reference", "context/meta",
    "context/experimental", "context/applied", "context/personal", "context/professional",
    "context/teaching", "context/research",
    // --- META: SOURCE ---
    "source/book", "source/article", "source/blog", "source/video", "source/podcast", 
    "source/course", "source/documentation", "source/community", "source/conference", 
    "source/workshop", "source/experience", "source/original", "source/paper", "source/conversation",
    // --- META: MODE & NATURE ---
    "mode/analytical", "mode/synthetic", "mode/reflective", "mode/practical",
    "nature/conceptual", "nature/procedural", "nature/declarative", "nature/reflective",
    // --- META: PROMPT ENG SPECIFIC ---
    "model/claude", "model/gemini", "model/gpt", "model/local", "model/agnostic", "model/open-source",
    "complexity/basic", "complexity/intermediate", "complexity/advanced", "complexity/expert",
    "validation/tested", "validation/reported", "validation/theoretical", "validation/failed",
    "maturity/beginner", "maturity/intermediate", "maturity/advanced", "maturity/expert",
    "maturity/emerging", "maturity/established", "maturity/standard", "maturity/deprecated"
];
// GROUP B: Systems, Methodologies, Categories (L3 & Parent Paths)
const groupB_Tags = [
    // --- PKM SYSTEMS & PARENT PATHS ---
    "pkm/theory", "pkm/methodology", "pkm/workflow", "pkm/principles", "pkm/research",
    "pkb/architecture", "pkb/design", "pkb/components", "pkb/metadata", "pkb/maintenance", "pkb/optimization",
    "note-taking/zettelkasten", "note-taking/types", "note-taking/practices", "note-taking/formats",
    "knowledge-workflow/capture", "knowledge-workflow/processing", "knowledge-workflow/synthesis", "knowledge-workflow/output", "knowledge-workflow/review",
    "obsidian/core-features", "obsidian/plugins", "obsidian/customization", "obsidian/configuration", "obsidian/advanced",
    "information-architecture/organization", "information-architecture/navigation", "information-architecture/taxonomy", "information-architecture/retrieval",
    "knowledge-graph/theory", "knowledge-graph/structure", "knowledge-graph/linking", "knowledge-graph/visualization",
    "knowledge-work/reading", "knowledge-work/research", "knowledge-work/writing", "knowledge-work/thinking", "knowledge-work/learning",
    "digital-garden/philosophy", "digital-garden/structure", "digital-garden/publishing", "digital-garden/maintenance",
    "productivity/gtd", "productivity/para", "productivity/time-management", "productivity/task-management",
    // --- COGNITIVE PARENT PATHS ---
    "cognitive-science/metacognition", "cognitive-science/memory", "cognitive-science/attention", 
    "cognitive-science/cognitive-load", "cognitive-science/executive-function", "cognitive-science/reasoning",
    "critical-thinking/analysis", "critical-thinking/logic", "critical-thinking/evaluation", 
    "critical-thinking/synthesis", "critical-thinking/problem-solving",
    "self-regulation/theory", "self-regulation/motivation", "self-regulation/goal-setting", 
    "self-regulation/self-control", "self-regulation/emotional", "self-regulation/behavioral",
    "learning-theory/andragogy", "learning-theory/pedagogy", "learning-theory/heutagogy", 
    "learning-theory/constructivism", "learning-theory/cognitive-apprenticeship",
    "self-improvement/skill-development", "self-improvement/mental-models", "self-improvement/productivity", 
    "self-improvement/reflective-practice", "self-improvement/growth-mindset",
    // --- PROMPT ENGINEERING PARENT PATHS ---
    "prompt-engineering/theory", "prompt-engineering/principles", "prompt-engineering/anatomy", 
    "prompt-engineering/evaluation", "prompt-engineering/optimization",
    "prompting-technique/zero-shot", "prompting-technique/few-shot", "prompting-technique/chain-of-thought", 
    "prompting-technique/reasoning", "prompting-technique/react", "prompting-technique/reflection", "prompting-technique/meta-prompting",
    "prompt-pattern/persona", "prompt-pattern/template", "prompt-pattern/context-control", 
    "prompt-pattern/output-format", "prompt-pattern/error-handling", "prompt-pattern/multi-turn",
    "llm-capability/reasoning", "llm-capability/knowledge", "llm-capability/generation", "llm-capability/understanding", "llm-limitation",
    "llm-architecture/transformer", "llm-architecture/model-family", "llm-architecture/model-size", 
    "llm-architecture/training", "llm-architecture/context-window",
    "advanced-prompting/agents", "advanced-prompting/rag", "advanced-prompting/function-calling", 
    "advanced-prompting/multi-modal", "advanced-prompting/programming", "advanced-prompting/chain-systems",
    "prompt-safety/adversarial", "prompt-safety/alignment", "prompt-safety/bias", 
    "prompt-safety/content-policy", "prompt-safety/information-security",
    "context-management/window", "context-management/memory", "context-management/compression", "context-management/injection",
    "prompt-workflow/ideation", "prompt-workflow/prototyping", "prompt-workflow/evaluation", 
    "prompt-workflow/version-control", "prompt-workflow/deployment",
    "prompt-application/writing", "prompt-application/analysis", "prompt-application/education", 
    "prompt-application/coding", "prompt-application/creative", "prompt-application/productivity",
    // --- FLAT CATEGORIES (L3) ---
    "capture-system", "processing-workflow", "organization-system", "synthesis-workflow", "retrieval-system", "review-system",
    "note-types", "note-organization", "index-systems", "dashboard-design", "tag-taxonomy", "metadata-systems", "linking-strategy",
    "zettelkasten", "para", "gtd", "building-second-brain", "evergreen-notes", "cornell-method", "outline-method", "mind-mapping", "concept-mapping",
    "progressive-summarization", "atomic-notes", "moc-system", "structure-notes", "hub-notes", "index-notes",
    "memory-systems", "attention", "perception", "executive-function", "language-processing", "reasoning", "problem-solving", 
    "learning-processes", "skill-acquisition", "conceptual-learning", "expertise-development",
    "obsidian-plugins", "automation", "api-integration", "version-control", "template-automation",
    "active-recall", "elaborative-interrogation", "self-explanation", "cognitive-load-management", "attention-management",
    "metacognitive-monitoring", "instructional-design-pkm", "andragogy-pkm", "self-directed-learning"
];
// GROUP C: Granular Concepts, Mechanisms, & Hierarchical Leaves (L4)
const groupC_Tags = [
    // --- COGNITIVE SCIENCE (Granular) ---
    "working-memory", "long-term-memory", "episodic-memory", "semantic-memory", "procedural-memory", 
    "prospective-memory", "autobiographical-memory", "encoding", "consolidation", "retrieval", "reconsolidation", 
    "interference", "phonological-loop", "visuospatial-sketchpad", "central-executive",
    "selective-attention", "divided-attention", "sustained-attention", "visual-perception", "auditory-perception", "multimodal-integration",
    "inhibitory-control", "cognitive-flexibility", "planning", "task-switching", "self-regulation", "error-monitoring", 
    "response-inhibition", "conflict-monitoring", "performance-monitoring", "cognitive-control",
    "deductive-reasoning", "inductive-reasoning", "abductive-reasoning", "analogical-reasoning", "creative-thinking", "critical-thinking",
    "implicit-learning", "explicit-learning", "transfer-of-learning", "spacing-effect", "testing-effect", "generation-effect", 
    "desirable-difficulties", "interleaving", "elaborative-encoding",
    "metamemory", "metacomprehension", "self-regulated-learning", "calibration", "monitoring", "control-processes",
    "cognitive-load-theory", "working-memory-capacity", "cognitive-resources", "mental-effort", "intrinsic-load", "extraneous-load", "germane-load",
    "embodied-cognition", "situated-cognition", "grounded-cognition", "extended-cognition", "distributed-cognition", "enactive-cognition",
    "information-processing-theory", "dual-process-theory", "levels-of-processing", "spreading-activation", 
    "parallel-distributed-processing", "symbolic-architecture", "ACT-R", "SOAR", "global-workspace-theory", "multiple-drafts-model",
    // --- PKM & OBSIDIAN (Granular) ---
    "folder-hierarchy", "naming-conventions", "metadata-systems", "linking-strategy", "tag-taxonomy",
    "note-templates", "frontmatter-design", "daily-notes", "meeting-notes", "quick-capture",
    "wiki-links", "backlinks", "unlinked-mentions", "link-density", "bidirectional-links", "transclusion",
    "tag-strategy", "folder-strategy", "file-naming", "metadata-schema", "status-tracking",
    "search-operators", "dataview-queries", "graph-analysis", "semantic-search", "filter-strategies",
    "spaced-repetition", "progressive-review", "link-maintenance", "tag-cleanup", "orphan-notes",
    "dataview", "templater", "quickadd", "tasks-plugin", "smart-connections", "excalidraw", "breadcrumbs", "meta-bind", 
    "javascript", "dataviewjs", "templater-scripts", "quickadd-macros", "export-import", "sync-systems", "backup-systems",
    // --- PROMPT ENGINEERING (Granular & Leaves) ---
    "prompting-technique/zero-shot/instruction", "prompting-technique/zero-shot/task-specification",
    "prompting-technique/few-shot/example-selection", "prompting-technique/few-shot/example-ordering", "prompting-technique/few-shot/diversity",
    "prompting-technique/chain-of-thought/basic", "prompting-technique/chain-of-thought/zero-shot", "prompting-technique/chain-of-thought/self-consistency",
    "prompting-technique/reasoning/step-by-step", "prompting-technique/reasoning/decomposition", "prompting-technique/reasoning/tree-of-thoughts", "prompting-technique/reasoning/graph-of-thoughts",
    "prompting-technique/react/reasoning-acting", "prompting-technique/react/tool-use", "prompting-technique/react/iteration",
    "prompting-technique/reflection/self-critique", "prompting-technique/reflection/refinement", "prompting-technique/reflection/verification",
    "prompting-technique/meta-prompting/prompt-generation", "prompting-technique/meta-prompting/self-improvement", "prompting-technique/meta-prompting/optimization",
    "prompt-pattern/persona/role-assignment", "prompt-pattern/persona/expertise", "prompt-pattern/persona/style",
    "prompt-pattern/template/fill-in-blank", "prompt-pattern/template/structured", "prompt-pattern/template/formulaic",
    "prompt-pattern/context-control/framing", "prompt-pattern/context-control/perspective", "prompt-pattern/context-control/constraints",
    "prompt-pattern/output-format/structured-data", "prompt-pattern/output-format/markdown", "prompt-pattern/output-format/code", "prompt-pattern/output-format/creative",
    "prompt-pattern/error-handling/clarification", "prompt-pattern/error-handling/fallback", "prompt-pattern/error-handling/validation",
    "prompt-pattern/multi-turn/conversation", "prompt-pattern/multi-turn/state-management", "prompt-pattern/multi-turn/context-threading",
    "advanced-prompting/agents/autonomous", "advanced-prompting/agents/tool-use", "advanced-prompting/agents/multi-agent", "advanced-prompting/agents/planning",
    "advanced-prompting/rag/retrieval", "advanced-prompting/rag/context-injection", "advanced-prompting/rag/hybrid-search",
    "prompt-safety/adversarial/jailbreaking", "prompt-safety/adversarial/prompt-injection", "prompt-safety/adversarial/defense",
    "llm-limitation/hallucination", "llm-limitation/reasoning-failures", "llm-limitation/bias",
    // --- CROSS-CUTTING CONCEPTS ---
    "concept/atomic-notes", "concept/linking-thinking", "concept/progressive-summarization", "concept/emergence", "concept/serendipity",
    "concept/networked-thought", "concept/evergreen-notes", "concept/bidirectional-linking", "concept/context-switching", "concept/information-overload",
    "concept/cognitive-overhead", "concept/discoverability", "concept/wayfinding", "concept/knowledge-synthesis", "concept/knowledge-transfer",
    "concept/second-brain", "concept/external-cognition", "concept/transfer", "concept/automaticity", "concept/flow-state", "concept/cognitive-bias",
    "concept/mental-representation", "concept/chunking", "concept/distributed-practice", "concept/retrieval-practice", "concept/interleaving",
    "concept/elaboration", "concept/dual-coding", "concept/testing-effect", "concept/generation-effect", "concept/spacing-effect",
    "concept/instruction-following", "concept/in-context-learning", "concept/token-probability", "concept/temperature-control", "concept/top-p-sampling",
    "concept/prompt-chaining", "concept/task-decomposition", "concept/output-validation", "concept/error-correction", "concept/few-shot-exemplars",
    "concept/semantic-similarity", "concept/attention-mechanism", "concept/transformer-architecture", "concept/prompt-template", "concept/system-message",
    // --- RESEARCH & INTEGRATION ---
    "empirical-research", "experimental-design", "cognitive-modeling", "neuroimaging-studies", "behavioral-experiments", 
    "longitudinal-research", "cross-sectional-research", "meta-analysis",
    "applied-cognition", "cognitive-training", "cognitive-enhancement", "cognitive-rehabilitation", 
    "educational-applications", "workplace-cognition", "technology-cognition", "clinical-cognition",
    "developmental-cognition", "aging-cognition", "cognitive-decline", "neurodevelopmental", "cognitive-disorders", "cross-cultural-cognition",
    "cognitive-pkm", "evidence-based-pkm", "learning-optimization", "memory-systems-design", "attention-architecture",
    "spaced-review-system", "retrieval-practice-pkm", "encoding-strategies", "consolidation-workflow",
    "extraneous-load-reduction", "germane-load-optimization", "working-memory-support",
    "metacognitive-pkm", "learning-analytics", "reflection-systems", "calibration-practices"
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
        else if (tag.startsWith("nature/")) icon = "🌿";
        // PKM & Obsidian
        else if (tag.includes("obsidian") || tag.includes("dataview") || tag.includes("plugin")) icon = "💎";
        else if (tag.includes("pkm") || tag.includes("pkb") || tag.includes("zettelkasten") || tag.includes("para")) icon = "🧠";
        else if (tag.includes("workflow") || tag.includes("system") || tag.includes("architecture")) icon = "🔄";
        else if (tag.includes("information-architecture") || tag.includes("taxonomy")) icon = "🗂️";
        // Cognitive Science
        else if (tag.includes("neuro") || tag.includes("brain")) icon = "🧬";
        else if (tag.includes("memory") || tag.includes("encoding") || tag.includes("recall")) icon = "💾";
        else if (tag.includes("learning") || tag.includes("education") || tag.includes("student") || tag.includes("andragogy")) icon = "🎓";
        else if (tag.includes("attention") || tag.includes("focus")) icon = "🎯";
        else if (tag.includes("reasoning") || tag.includes("logic") || tag.includes("thinking") || tag.includes("decision")) icon = "💡";
        else if (tag.includes("cognitive") || tag.includes("psychology") || tag.includes("behavior")) icon = "🧩";
        else if (tag.includes("regulation") || tag.includes("motivation") || tag.includes("self")) icon = "💪";
        // Prompt Engineering / AI
        else if (tag.includes("prompt") || tag.includes("chain-of-thought")) icon = "💬";
        else if (tag.includes("llm") || tag.includes("gpt") || tag.includes("claude") || tag.includes("gemini") || tag.includes("artificial")) icon = "🤖";
        else if (tag.includes("agent") || tag.includes("rag")) icon = "🕵️";
        else if (tag.includes("safety") || tag.includes("bias")) icon = "🛡️";
        // Cosmology
        else if (tag.includes("cosmology") || tag.includes("universe")) icon = "🌌";
        // Cross-Cutting / Research
        else if (tag.includes("concept/")) icon = "💡";
        else if (tag.includes("research") || tag.includes("analysis") || tag.includes("study")) icon = "🔬";
        // 2. Formatting: Replace slashes with visual arrows for cleaner reading
        let cleanText = tag.split("/").join("  ›  ");
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