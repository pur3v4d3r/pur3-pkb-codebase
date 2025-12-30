<%*
/* ---------------------------------------------------------------
   MASTER MULTI-PURPOSE PERMANENT NOTE SKELETON
   Integrated with Pur3v4d3r Tag Taxonomy
   ---------------------------------------------------------------
*/
// --- CONFIGURATION: PRE-DEFINED LISTS ---
// 1. NOTE TYPES (Adapted for Permanent Notes)
const typeList = [
    "concept",
    "principle",
    "mental-model",
    "framework",
    "theory",
    "insight",
    "strategy",
    "definition",
    "permanent-note"
];
// 2. SOURCE ORIGINS (Extended for Synthesis)
const sourceList = [
    "original-synthesis",
    "literature-synthesis",
    "report",
    "book",
    "article",
    "other-note",
    "gemini-pro-2.5",
    "gemini-flash-2.5",
    "gemini-pro-3.0",
    "gemini-flash-3.0",
    "claude-sonnet-4.5",
    "claude-opus-4.1"
];
// 3. LINK-UP MOCs (Strict Selection)
const linkUpList = [
    "[[cognitive-science-perm-moc]]",
    "[[pkb-knowledge-perm-moc]]",
    "[[prompt-engineering-perm-moc]]",
    "[[cosmology-perm-moc]]"
];
// --- TAXONOMY ARRAYS (Derived from Tag Taxonomy File) ---
// GROUP A: High-Level Domains & Dimensions (For Tags 01 & 02)
const groupA_Tags = [
    // PKM & PKB
    "pkm", "pkb", "note-taking", "knowledge-workflow", "obsidian", 
    "information-architecture", "knowledge-graph", "knowledge-work", "digital-garden", "productivity",
    // Cross-Cutting Concepts (High Level)
    "concept/atomic-notes", "concept/emergence", "concept/serendipity", "concept/networked-thought", "concept/knowledge-synthesis",
    "concept/external-cognition", "concept/transfer", "concept/automaticity", "concept/flow-state", "concept/cognitive-bias",
    "concept/mental-representation", "concept/chunking", "concept/distributed-practice", "concept/retrieval-practice", "concept/elaboration",
    "concept/instruction-following", "concept/in-context-learning", "concept/prompt-chaining", "concept/task-decomposition",
    // Psychology & Cognitive
    "cognitive-science", "critical-thinking", "self-regulation", "learning-theory", "self-improvement",
    // Prompt Engineering
    "prompt-engineering", "prompting-technique", "prompt-pattern", "llm-capability", "llm-architecture",
    "advanced-prompting", "prompt-safety", "context-management", "prompt-workflow", "prompt-application",
    // --- MULTI-DIMENSIONAL TAGS ---
    // Note Type
    "type/fleeting", "type/literature", "type/permanent", "type/moc", "type/reference",
    "type/tutorial", "type/template", "type/dashboard", "type/guide", "type/framework",
    "type/practice-log", "type/reflection", "type/review", "type/technique", "type/pattern",
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
// GROUP B: Sub-Domains & Categories (For Tag 03)
const groupB_Tags = [
    // PKM & PKB
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
    // Psychology & Cognitive
    "cognitive-science/metacognition", "cognitive-science/memory", "cognitive-science/attention", 
    "cognitive-science/cognitive-load", "cognitive-science/executive-function", "cognitive-science/reasoning",
    "critical-thinking/analysis", "critical-thinking/logic", "critical-thinking/evaluation", "critical-thinking/synthesis", "critical-thinking/problem-solving",
    "self-regulation/theory", "self-regulation/motivation", "self-regulation/goal-setting", "self-regulation/self-control", "self-regulation/emotional", "self-regulation/behavioral",
    "learning-theory/andragogy", "learning-theory/pedagogy", "learning-theory/heutagogy", "learning-theory/constructivism", "learning-theory/cognitive-apprenticeship",
    "self-improvement/skill-development", "self-improvement/mental-models", "self-improvement/productivity", "self-improvement/reflective-practice", "self-improvement/growth-mindset",
    // Prompt Engineering
    "prompt-engineering/theory", "prompt-engineering/principles", "prompt-engineering/anatomy", "prompt-engineering/evaluation", "prompt-engineering/optimization",
    "prompting-technique/zero-shot", "prompting-technique/few-shot", "prompting-technique/chain-of-thought", "prompting-technique/reasoning", "prompting-technique/react", "prompting-technique/reflection", "prompting-technique/meta-prompting",
    "prompt-pattern/persona", "prompt-pattern/template", "prompt-pattern/context-control", "prompt-pattern/output-format", "prompt-pattern/error-handling", "prompt-pattern/multi-turn",
    "llm-capability/reasoning", "llm-capability/knowledge", "llm-capability/generation", "llm-capability/understanding", "llm-limitation",
    "llm-architecture/transformer", "llm-architecture/model-family", "llm-architecture/model-size", "llm-architecture/training", "llm-architecture/context-window",
    "advanced-prompting/agents", "advanced-prompting/rag", "advanced-prompting/function-calling", "advanced-prompting/multi-modal", "advanced-prompting/programming", "advanced-prompting/chain-systems",
    "prompt-safety/adversarial", "prompt-safety/alignment", "prompt-safety/bias", "prompt-safety/content-policy", "prompt-safety/information-security",
    "context-management/window", "context-management/memory", "context-management/compression", "context-management/injection",
    "prompt-workflow/ideation", "prompt-workflow/prototyping", "prompt-workflow/evaluation", "prompt-workflow/version-control", "prompt-workflow/deployment",
    "prompt-application/writing", "prompt-application/analysis", "prompt-application/education", "prompt-application/coding", "prompt-application/creative", "prompt-application/productivity"
];
// GROUP C: Granular Concepts & Leaf Nodes (For Tags 04, 05, 06)
const groupC_Tags = [
    // --- PKM: Theory & Methodology ---
    "pkm/theory/foundations", "pkm/theory/epistemology", "pkm/theory/cognitive-basis", "pkm/theory/philosophy",
    "pkm/methodology/zettelkasten", "pkm/methodology/para", "pkm/methodology/lyt", "pkm/methodology/evergreen-notes", "pkm/methodology/digital-garden", "pkm/methodology/commonplace-book",
    "pkm/workflow/capture", "pkm/workflow/process", "pkm/workflow/organize", "pkm/workflow/distill", "pkm/workflow/express", "pkm/workflow/review",
    "pkm/principles/progressive-summarization", "pkm/principles/atomic-notes", "pkm/principles/linking-thinking", "pkm/principles/emergence", "pkm/principles/networked-thought",
    "pkm/research/empirical", "pkm/research/case-studies", "pkm/research/comparative",
    // --- PKB: Architecture & Design ---
    "pkb/architecture/structure", "pkb/architecture/hierarchy", "pkb/architecture/folders", "pkb/architecture/taxonomy",
    "pkb/design/information-architecture", "pkb/design/navigation", "pkb/design/discoverability", "pkb/design/scalability",
    "pkb/components/moc", "pkb/components/hub-notes", "pkb/components/index-notes", "pkb/components/dashboards", "pkb/components/atomic-notes",
    "pkb/metadata/tags", "pkb/metadata/properties", "pkb/metadata/frontmatter", "pkb/metadata/yaml",
    "pkb/maintenance/refactoring", "pkb/maintenance/cleanup", "pkb/maintenance/consolidation", "pkb/maintenance/archiving",
    "pkb/optimization/search", "pkb/optimization/retrieval", "pkb/optimization/performance", "pkb/optimization/workflows",
    // --- Note Taking Systems ---
    "note-taking/zettelkasten/principles", "note-taking/zettelkasten/slip-box", "note-taking/zettelkasten/linking", "note-taking/zettelkasten/numbering", "note-taking/zettelkasten/keywords",
    "note-taking/types/fleeting", "note-taking/types/literature", "note-taking/types/permanent", "note-taking/types/reference", "note-taking/types/synthesis", "note-taking/types/project",
    "note-taking/practices/annotation", "note-taking/practices/summarization", "note-taking/practices/paraphrasing", "note-taking/practices/extraction",
    "note-taking/formats/markdown", "note-taking/formats/outlining", "note-taking/formats/mind-mapping", "note-taking/formats/visual",
    // --- Knowledge Workflows ---
    "knowledge-workflow/capture/inbox", "knowledge-workflow/capture/quick-capture", "knowledge-workflow/capture/voice-notes", "knowledge-workflow/capture/highlights",
    "knowledge-workflow/processing/triage", "knowledge-workflow/processing/elaboration", "knowledge-workflow/processing/linking", "knowledge-workflow/processing/tagging",
    "knowledge-workflow/synthesis/integration", "knowledge-workflow/synthesis/connection", "knowledge-workflow/synthesis/emergence",
    "knowledge-workflow/output/writing", "knowledge-workflow/output/publishing", "knowledge-workflow/output/sharing", "knowledge-workflow/output/teaching",
    "knowledge-workflow/review/daily-review", "knowledge-workflow/review/weekly-review", "knowledge-workflow/review/monthly-review", "knowledge-workflow/review/spaced-repetition",
    // --- Obsidian Ecosystem ---
    "obsidian/core-features/linking", "obsidian/core-features/graph-view", "obsidian/core-features/search", "obsidian/core-features/backlinks", "obsidian/core-features/canvas",
    "obsidian/plugins/dataview", "obsidian/plugins/templater", "obsidian/plugins/quickadd", "obsidian/plugins/advanced-tables", "obsidian/plugins/calendar", "obsidian/plugins/periodic-notes", "obsidian/plugins/tag-wrangler",
    "obsidian/customization/css", "obsidian/customization/themes", "obsidian/customization/snippets", "obsidian/customization/callouts",
    "obsidian/configuration/settings", "obsidian/configuration/hotkeys", "obsidian/configuration/workspace", "obsidian/configuration/sync",
    "obsidian/advanced/dataviewjs", "obsidian/advanced/templater-scripts", "obsidian/advanced/automation", "obsidian/advanced/api",
    // --- Information Architecture ---
    "information-architecture/organization/hierarchical", "information-architecture/organization/networked", "information-architecture/organization/faceted", "information-architecture/organization/hybrid",
    "information-architecture/navigation/wayfinding", "information-architecture/navigation/breadcrumbs", "information-architecture/navigation/indexes", "information-architecture/navigation/search",
    "information-architecture/taxonomy/classification", "information-architecture/taxonomy/ontology", "information-architecture/taxonomy/folksonomy", "information-architecture/taxonomy/controlled-vocabulary",
    "information-architecture/retrieval/findability", "information-architecture/retrieval/discoverability", "information-architecture/retrieval/serendipity",
    // --- Knowledge Graph ---
    "knowledge-graph/theory/networks", "knowledge-graph/theory/nodes-edges", "knowledge-graph/theory/semantics", "knowledge-graph/theory/emergence",
    "knowledge-graph/structure/clustering", "knowledge-graph/structure/hubs", "knowledge-graph/structure/bridges", "knowledge-graph/structure/density",
    "knowledge-graph/linking/bidirectional", "knowledge-graph/linking/contextual", "knowledge-graph/linking/semantic", "knowledge-graph/linking/typed-links",
    "knowledge-graph/visualization/graph-view", "knowledge-graph/visualization/network-analysis", "knowledge-graph/visualization/pathfinding",
    // --- Knowledge Work Practices ---
    "knowledge-work/reading/active-reading", "knowledge-work/reading/annotation", "knowledge-work/reading/speed-reading", "knowledge-work/reading/comprehension",
    "knowledge-work/research/literature-review", "knowledge-work/research/source-evaluation", "knowledge-work/research/synthesis", "knowledge-work/research/citation",
    "knowledge-work/writing/drafting", "knowledge-work/writing/editing", "knowledge-work/writing/argumentation", "knowledge-work/writing/publishing",
    "knowledge-work/thinking/analysis", "knowledge-work/thinking/synthesis", "knowledge-work/thinking/reflection", "knowledge-work/thinking/ideation",
    "knowledge-work/learning/study-methods", "knowledge-work/learning/retention", "knowledge-work/learning/transfer", "knowledge-work/learning/mastery",
    // --- Digital Garden ---
    "digital-garden/philosophy/learning-in-public", "digital-garden/philosophy/work-in-progress", "digital-garden/philosophy/imperfection",
    "digital-garden/structure/evergreen-notes", "digital-garden/structure/seedlings", "digital-garden/structure/trails",
    "digital-garden/publishing/obsidian-publish", "digital-garden/publishing/static-sites", "digital-garden/publishing/sharing",
    "digital-garden/maintenance/gardening", "digital-garden/maintenance/pruning", "digital-garden/maintenance/cultivating",
    // --- Productivity ---
    "productivity/gtd/capture", "productivity/gtd/clarify", "productivity/gtd/organize", "productivity/gtd/reflect", "productivity/gtd/engage",
    "productivity/para/projects", "productivity/para/areas", "productivity/para/resources", "productivity/para/archives",
    "productivity/time-management/scheduling", "productivity/time-management/batching", "productivity/time-management/blocking",
    "productivity/task-management/todos", "productivity/task-management/projects", "productivity/task-management/workflows",
    // --- Cognitive Science ---
    "cognitive-science/metacognition/awareness", "cognitive-science/metacognition/monitoring", "cognitive-science/metacognition/regulation", "cognitive-science/metacognition/reflection",
    "cognitive-science/memory/working-memory", "cognitive-science/memory/long-term", "cognitive-science/memory/encoding", "cognitive-science/memory/retrieval", "cognitive-science/memory/consolidation",
    "cognitive-science/attention/selective", "cognitive-science/attention/sustained", "cognitive-science/attention/divided", "cognitive-science/attention/executive",
    "cognitive-science/cognitive-load/intrinsic", "cognitive-science/cognitive-load/extraneous", "cognitive-science/cognitive-load/germane", "cognitive-science/cognitive-load/management",
    "cognitive-science/executive-function/inhibition", "cognitive-science/executive-function/working-memory", "cognitive-science/executive-function/cognitive-flexibility", "cognitive-science/executive-function/planning",
    "cognitive-science/reasoning/deductive", "cognitive-science/reasoning/inductive", "cognitive-science/reasoning/abductive", "cognitive-science/reasoning/analogical",
    // --- Critical Thinking ---
    "critical-thinking/analysis/argument-analysis", "critical-thinking/analysis/claim-evaluation", "critical-thinking/analysis/evidence-assessment",
    "critical-thinking/logic/formal", "critical-thinking/logic/informal", "critical-thinking/logic/fallacies", "critical-thinking/logic/validity",
    "critical-thinking/evaluation/source-credibility", "critical-thinking/evaluation/bias-detection", "critical-thinking/evaluation/quality-assessment",
    "critical-thinking/synthesis/integration", "critical-thinking/synthesis/pattern-recognition", "critical-thinking/synthesis/concept-building",
    "critical-thinking/problem-solving/problem-framing", "critical-thinking/problem-solving/solution-generation", "critical-thinking/problem-solving/decision-making",
    // --- Self-Regulation ---
    "self-regulation/theory/self-determination", "self-regulation/theory/social-cognitive", "self-regulation/theory/control-theory",
    "self-regulation/motivation/intrinsic", "self-regulation/motivation/extrinsic", "self-regulation/motivation/autonomous", "self-regulation/motivation/controlled",
    "self-regulation/goal-setting/goal-formation", "self-regulation/goal-setting/goal-pursuit", "self-regulation/goal-setting/goal-adjustment",
    "self-regulation/self-control/impulse-control", "self-regulation/self-control/delay-gratification", "self-regulation/self-control/willpower",
    "self-regulation/emotional/awareness", "self-regulation/emotional/regulation-strategies", "self-regulation/emotional/resilience",
    "self-regulation/behavioral/habit-formation", "self-regulation/behavioral/action-control", "self-regulation/behavioral/self-monitoring",
    // --- Learning Theory ---
    "learning-theory/andragogy/adult-learning", "learning-theory/andragogy/self-directed", "learning-theory/andragogy/experience-based",
    "learning-theory/pedagogy/instructional-design", "learning-theory/pedagogy/teaching-methods", "learning-theory/pedagogy/assessment",
    "learning-theory/heutagogy/self-determined", "learning-theory/heutagogy/capability-building",
    "learning-theory/constructivism/knowledge-construction", "learning-theory/constructivism/schema-theory", "learning-theory/constructivism/scaffolding",
    "learning-theory/cognitive-apprenticeship/modeling", "learning-theory/cognitive-apprenticeship/coaching", "learning-theory/cognitive-apprenticeship/fading",
    // --- Self-Improvement ---
    "self-improvement/skill-development/deliberate-practice", "self-improvement/skill-development/mastery", "self-improvement/skill-development/expertise",
    "self-improvement/mental-models/frameworks", "self-improvement/mental-models/heuristics", "self-improvement/mental-models/decision-frameworks",
    "self-improvement/productivity/focus-techniques", "self-improvement/productivity/time-management", "self-improvement/productivity/energy-management",
    "self-improvement/reflective-practice/journaling", "self-improvement/reflective-practice/review-systems", "self-improvement/reflective-practice/feedback-loops",
    "self-improvement/growth-mindset/beliefs", "self-improvement/growth-mindset/challenges", "self-improvement/growth-mindset/learning-orientation",
    // --- Prompt Engineering: Theory & Principles ---
    "prompt-engineering/theory/foundations", "prompt-engineering/theory/linguistics", "prompt-engineering/theory/cognitive-basis", "prompt-engineering/theory/information-theory",
    "prompt-engineering/principles/clarity", "prompt-engineering/principles/specificity", "prompt-engineering/principles/context", "prompt-engineering/principles/constraints", "prompt-engineering/principles/iteration",
    "prompt-engineering/anatomy/instruction", "prompt-engineering/anatomy/context", "prompt-engineering/anatomy/examples", "prompt-engineering/anatomy/output-format", "prompt-engineering/anatomy/constraints",
    "prompt-engineering/evaluation/testing", "prompt-engineering/evaluation/metrics", "prompt-engineering/evaluation/comparison", "prompt-engineering/evaluation/iteration",
    "prompt-engineering/optimization/refinement", "prompt-engineering/optimization/compression", "prompt-engineering/optimization/efficiency", "prompt-engineering/optimization/cost",
    // --- Prompt Techniques ---
    "prompting-technique/zero-shot/instruction", "prompting-technique/zero-shot/task-specification",
    "prompting-technique/few-shot/example-selection", "prompting-technique/few-shot/example-ordering", "prompting-technique/few-shot/diversity",
    "prompting-technique/chain-of-thought/basic", "prompting-technique/chain-of-thought/zero-shot", "prompting-technique/chain-of-thought/self-consistency",
    "prompting-technique/reasoning/step-by-step", "prompting-technique/reasoning/decomposition", "prompting-technique/reasoning/tree-of-thoughts", "prompting-technique/reasoning/graph-of-thoughts",
    "prompting-technique/react/reasoning-acting", "prompting-technique/react/tool-use", "prompting-technique/react/iteration",
    "prompting-technique/reflection/self-critique", "prompting-technique/reflection/refinement", "prompting-technique/reflection/verification",
    "prompting-technique/meta-prompting/prompt-generation", "prompting-technique/meta-prompting/self-improvement", "prompting-technique/meta-prompting/optimization",
    // --- Prompt Patterns ---
    "prompt-pattern/persona/role-assignment", "prompt-pattern/persona/expertise", "prompt-pattern/persona/style",
    "prompt-pattern/template/fill-in-blank", "prompt-pattern/template/structured", "prompt-pattern/template/formulaic",
    "prompt-pattern/context-control/framing", "prompt-pattern/context-control/perspective", "prompt-pattern/context-control/constraints",
    "prompt-pattern/output-format/structured-data", "prompt-pattern/output-format/markdown", "prompt-pattern/output-format/code", "prompt-pattern/output-format/creative",
    "prompt-pattern/error-handling/clarification", "prompt-pattern/error-handling/fallback", "prompt-pattern/error-handling/validation",
    "prompt-pattern/multi-turn/conversation", "prompt-pattern/multi-turn/state-management", "prompt-pattern/multi-turn/context-threading",
    // --- LLM Capabilities & Architecture ---
    "llm-capability/reasoning/logical", "llm-capability/reasoning/mathematical", "llm-capability/reasoning/causal", "llm-capability/reasoning/analogical",
    "llm-capability/knowledge/factual", "llm-capability/knowledge/procedural", "llm-capability/knowledge/domain-specific", "llm-capability/knowledge/cutoff-date",
    "llm-capability/generation/creative", "llm-capability/generation/technical", "llm-capability/generation/structured", "llm-capability/generation/code",
    "llm-capability/understanding/comprehension", "llm-capability/understanding/inference", "llm-capability/understanding/context", "llm-capability/understanding/ambiguity",
    "llm-limitation/hallucination", "llm-limitation/reasoning-failures", "llm-limitation/knowledge-gaps", "llm-limitation/instruction-following", "llm-limitation/consistency", "llm-limitation/bias",
    "llm-architecture/transformer/attention", "llm-architecture/transformer/decoder-only", "llm-architecture/transformer/encoder-decoder",
    "llm-architecture/model-family/gpt", "llm-architecture/model-family/claude", "llm-architecture/model-family/gemini", "llm-architecture/model-family/llama", "llm-architecture/model-family/mistral",
    "llm-architecture/model-size/small", "llm-architecture/model-size/medium", "llm-architecture/model-size/large", "llm-architecture/model-size/frontier",
    "llm-architecture/training/pretraining", "llm-architecture/training/fine-tuning", "llm-architecture/training/rlhf", "llm-architecture/training/constitutional-ai",
    "llm-architecture/context-window/length", "llm-architecture/context-window/management", "llm-architecture/context-window/optimization",
    // --- Advanced Prompting Systems ---
    "advanced-prompting/agents/autonomous", "advanced-prompting/agents/tool-use", "advanced-prompting/agents/multi-agent", "advanced-prompting/agents/planning",
    "advanced-prompting/rag/retrieval", "advanced-prompting/rag/context-injection", "advanced-prompting/rag/hybrid-search",
    "advanced-prompting/function-calling/tool-definition", "advanced-prompting/function-calling/parameter-extraction", "advanced-prompting/function-calling/orchestration",
    "advanced-prompting/multi-modal/vision", "advanced-prompting/multi-modal/audio", "advanced-prompting/multi-modal/code",
    "advanced-prompting/programming/code-generation", "advanced-prompting/programming/debugging", "advanced-prompting/programming/refactoring", "advanced-prompting/programming/documentation",
    "advanced-prompting/chain-systems/sequential", "advanced-prompting/chain-systems/parallel", "advanced-prompting/chain-systems/conditional", "advanced-prompting/chain-systems/recursive",
    // --- Safety, Context, & Workflow ---
    "prompt-safety/adversarial/jailbreaking", "prompt-safety/adversarial/prompt-injection", "prompt-safety/adversarial/defense",
    "prompt-safety/alignment/values", "prompt-safety/alignment/constitutional", "prompt-safety/alignment/harmlessness", "prompt-safety/alignment/honesty",
    "prompt-safety/bias/detection", "prompt-safety/bias/mitigation", "prompt-safety/bias/fairness",
    "prompt-safety/content-policy/restrictions", "prompt-safety/content-policy/boundaries", "prompt-safety/content-policy/compliance",
    "prompt-safety/information-security/pii", "prompt-safety/information-security/confidentiality", "prompt-safety/information-security/data-handling",
    "context-management/window/limits", "context-management/window/optimization", "context-management/window/chunking",
    "context-management/memory/short-term", "context-management/memory/long-term", "context-management/memory/retrieval", "context-management/memory/summarization",
    "context-management/compression/summarization", "context-management/compression/extraction", "context-management/compression/prioritization",
    "context-management/injection/document", "context-management/injection/knowledge-base", "context-management/injection/dynamic",
    "prompt-workflow/ideation/brainstorming", "prompt-workflow/ideation/requirements", "prompt-workflow/ideation/use-case",
    "prompt-workflow/prototyping/drafting", "prompt-workflow/prototyping/iteration", "prompt-workflow/prototyping/testing",
    "prompt-workflow/evaluation/manual", "prompt-workflow/evaluation/automated", "prompt-workflow/evaluation/ab-testing", "prompt-workflow/evaluation/benchmark",
    "prompt-workflow/version-control/tracking", "prompt-workflow/version-control/comparison", "prompt-workflow/version-control/rollback",
    "prompt-workflow/deployment/production", "prompt-workflow/deployment/monitoring", "prompt-workflow/deployment/maintenance",
    // --- Applications ---
    "prompt-application/writing/content-creation", "prompt-application/writing/editing", "prompt-application/writing/style",
    "prompt-application/analysis/data", "prompt-application/analysis/text", "prompt-application/analysis/research",
    "prompt-application/education/tutoring", "prompt-application/education/assessment", "prompt-application/education/curriculum",
    "prompt-application/coding/generation", "prompt-application/coding/review", "prompt-application/coding/debugging",
    "prompt-application/creative/storytelling", "prompt-application/creative/ideation", "prompt-application/creative/design",
    "prompt-application/productivity/summarization", "prompt-application/productivity/organization", "prompt-application/productivity/automation"
];
// --- HELPER FUNCTION: PRETTY PRINT TAGS ---
// This function adds icons and arrows for the UI, but keeps the original tag for the file.
function formatTagsForDisplay(tags) {
    return tags.map(tag => {
        let icon = "🔹"; // Default bullet
        
        // 1. Assign Icons based on Domain Keywords
        if (tag.startsWith("pkm") || tag.startsWith("pkb") || tag.startsWith("note-taking")) icon = "🧠";
        else if (tag.startsWith("cognitive") || tag.startsWith("critical") || tag.startsWith("learning") || tag.startsWith("self")) icon = "🎓";
        else if (tag.startsWith("prompt") || tag.startsWith("llm") || tag.startsWith("advanced-prompting")) icon = "🤖";
        else if (tag.startsWith("obsidian")) icon = "💎";
        else if (tag.startsWith("type/")) icon = "📑";
        else if (tag.startsWith("status/")) icon = "🚦";
        else if (tag.startsWith("context/")) icon = "🌐";
        else if (tag.startsWith("source/")) icon = "📚";
        else if (tag.startsWith("maturity/")) icon = "🍷";
        else if (tag.startsWith("mode/")) icon = "⚙️";
        
        // 2. Formatting: Replace slashes with visual arrows
        // Example: "pkm/theory/foundations" BECOMES "🧠 pkm › theory › foundations"
        let cleanText = tag.split("/").join("  ›  ");
        
        return `${icon} ${cleanText}`;
    });
}
// --- INPUT SYSTEM ---
// 1. Text Prompts
const title = await tp.system.prompt("Enter Note Title (Concept Name):");
const alias1 = await tp.system.prompt("Enter Alias 1 (Press Enter to skip):");
const alias2 = await tp.system.prompt("Enter Alias 2 (Press Enter to skip):");
// 2. Metadata Suggesters
const type = await tp.system.suggester(typeList, typeList, false, "Select Note TYPE:");
const source = await tp.system.suggester(sourceList, sourceList, false, "Select SOURCE / ORIGIN:");
const linkUp = await tp.system.suggester(linkUpList, linkUpList, false, "Select LINK-UP MOC:");
// 3. Tag Suggesters (Hierarchical Selection)
// Tag 01 & 02: High Level Domains or Dimensions (Group A)
const tag1 = await tp.system.suggester(groupA_Tags, groupA_Tags, false, "Select Tag 01 (Domain/Dimension - Group A):");
const tag2 = await tp.system.suggester(groupA_Tags, groupA_Tags, false, "Select Tag 02 (Domain/Dimension - Group A):");
// Tag 03: Sub-Domain / Category (Group B)
const tag3 = await tp.system.suggester(groupB_Tags, groupB_Tags, false, "Select Tag 03 (Sub-Domain - Group B):");
// Tag 04 - 08: Granular Concepts / Specifics (Group C)
const tag4 = await tp.system.suggester(groupC_Tags, groupC_Tags, false, "Select Tag 04 (Granular Concept - Group C):");
const tag5 = await tp.system.suggester(groupC_Tags, groupC_Tags, false, "Select Tag 05 (Granular Concept - Group C):");
const tag6 = await tp.system.suggester(groupC_Tags, groupC_Tags, false, "Select Tag 06 (Granular Concept - Group C):");
const tag7 = await tp.system.suggester(groupC_Tags, groupC_Tags, false, "Select Tag 07 (Granular Concept - Group C):");
const tag8 = await tp.system.suggester(groupC_Tags, groupC_Tags, false, "Select Tag 08 (Granular Concept - Group C):");
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

> [!definition]
> - **Key-Term**:: [[<% title %>]]
> - [**Definition**:: <% tp.file.cursor() %>

## Foundational Understanding

[Your initial understanding of this concept]

## Key Principles

## Related Concepts

- [[Concept 1]]
- [[Concept 2]]

## Practical Applications

## Evolution Log

### <% dateNow %> - Initial Creation
[Context: Where you first encountered this concept]

---

## 📚 Sources