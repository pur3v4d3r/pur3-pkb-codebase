<%*
/* ═══════════════════════════════════════════════════════════════════════
   MASTER GENERAL-NOTE TEMPLATE v3.0.2 (REORGANIZED)
   COMPLETE TAXONOMY INTEGRATION (OPTIMIZED FOR SUGGESTER DISPLAY)
   CHANGELOG v3.0.0:
   - Split large arrays into manageable sub-groups (25-40 tags each)
   - Alphabetized ALL arrays for easier human scanning
   - Improved visual organization with clear section headers
   - Fixed suggester display limitations
   - Added hierarchical selection workflow
   ═══════════════════════════════════════════════════════════════════════
*/
/* ───────────────────────────────────────────────────────────────────────
   CONFIGURATION: PRE-DEFINED METADATA LISTS
   ─────────────────────────────────────────────────────────────────────── */
// 1. NOTE TYPES (For 'type' property - matches "type/" tags)
const typeList = [
    "analysis",
    "case-study",
    "claude-project",
    "cog-sci-report",
    "comparison",
    "concept",
    "cosmo-report",
    "dashboard",
    "definition",
    "edu-report",
    "experiment",
    "fleeting",
    "framework",
    "gemini-gem",
    "guide",
    "insight",
    "literature",
    "mental-model",
    "moc",
    "pattern",
    "permanent-note",
    "pkb-report",
    "practice-log",
    "principle",
    "prompt",
    "prompt-report",
    "reference",
    "reflection",
    "report",
    "review",
    "strategy",
    "technique",
    "theory",
    "tutorial"
];
// 2. SOURCE ORIGINS
const sourceList = [
    "article",
    "book",
    "claude-opus-4.1",
    "claude-sonnet-4.5",
    "community",
    "conversation",
    "course",
    "documentation",
    "experience",
    "gemini-flash-2.5",
    "gemini-flash-3.0",
    "gemini-pro-2.5",
    "gemini-pro-3.0",
    "literature-synthesis",
    "local-llm",
    "original-synthesis",
    "paper",
    "report",
    "video",
];
// 3. LINK-UP MOCs (Your Primary Domain Hubs)
const linkUpList = [
    "[[artificial-intelligence-moc]]",
    "[[99-archive/05-moc's/cognitive-science-moc]]",
    "[[cosmology-moc]]",
    "[[educational-psychology-moc]]",
    "[[learning-theory-moc]]",
    "[[neuroscience-moc]]",
    "[[pkb-&-pkm-moc]]",
    "[[prompt-engineering-moc]]"
];
// 4. STATUS & MATURITY LEVELS
const maturityLevels = [
    "needs-review",
    "seedling",
    "developing",
    "budding",
    "evergreen"
];
const confidenceLevels = [
    "speculative",
    "provisional",
    "moderate",
    "established",
    "high"
];
/* ═══════════════════════════════════════════════════════════════════════
   MASTER TAXONOMY: TAG ARRAYS
   ORGANIZATION STRATEGY:
   - GROUP A: Meta-Dimensions (Type, Status, Context, Mode, Nature)
   - GROUP B: Top-Level Domains & High-Level Systems (L1/L2)
   - GROUP C: Sub-Domains & Methodologies (L3 Parent Paths)
   - GROUP D-J: Granular Concepts & Mechanisms (L4 Leaves)
   Each group is split into sub-arrays of 25-40 tags for optimal display
   All arrays are ALPHABETICALLY SORTED
   ═══════════════════════════════════════════════════════════════════════ */
/* ───────────────────────────────────────────────────────────────────────
   GROUP A: META-DIMENSIONS (Type, Status, Context, Mode, Nature, Model)
   Split into: A1 (Type), A2 (Status), A3 (Context/Source), A4 (Mode/Nature/Model/Validation)
   ─────────────────────────────────────────────────────────────────────── */
// GROUP A1: Meta - Type Tags
const groupA1_Tags = [
    "type/analysis",
    "type/case-study",
    "type/claude-project",
    "type/comparison",
    "type/dashboard",
    "type/experiment",
    "type/fleeting",
    "type/framework",
    "type/gemini-gem",
    "type/guide",
    "type/literature",
    "type/moc",
    "type/pattern",
    "type/permanent",
    "type/practice-log",
    "type/prompt-library",
    "type/reference",
    "type/reflection",
    "type/report",
    "type/review",
    "type/synthesis",
    "type/technique",
    "type/template",
    "type/tutorial"
];
// GROUP A2: Meta - Status Tags
const groupA2_Tags = [
    "status/archived",
    "status/budding",
    "status/complete",
    "status/deprecated",
    "status/evergreen",
    "status/experimental",
    "status/in-progress",
    "status/not-read",
    "status/production",
    "status/proven",
    "status/read",
    "status/review",
    "status/seedling",
    "status/under-revision"
];
// GROUP A3: Meta - Context & Source Tags
const groupA3_Tags = [
    "context/applied",
    "context/experimental",
    "context/meta",
    "context/personal",
    "context/practical",
    "context/professional",
    "context/reference",
    "context/research",
    "context/teaching",
    "context/theoretical",
    "context/tutorial",
    "source/article",
    "source/blog",
    "source/book",
    "source/community",
    "source/conference",
    "source/conversation",
    "source/course",
    "source/documentation",
    "source/experience",
    "source/original",
    "source/paper",
    "source/podcast",
    "source/video",
    "source/workshop"
];
// GROUP A4: Meta - Mode, Nature, Model, Complexity, Validation, Maturity
const groupA4_Tags = [
    "complexity/advanced",
    "complexity/basic",
    "complexity/expert",
    "complexity/intermediate",
    "maturity/advanced",
    "maturity/beginner",
    "maturity/deprecated",
    "maturity/emerging",
    "maturity/established",
    "maturity/expert",
    "maturity/intermediate",
    "maturity/standard",
    "mode/analytical",
    "mode/practical",
    "mode/reflective",
    "mode/synthetic",
    "model/agnostic",
    "model/claude",
    "model/gemini",
    "model/gpt",
    "model/local",
    "model/open-source",
    "nature/conceptual",
    "nature/declarative",
    "nature/procedural",
    "nature/reflective",
    "validation/failed",
    "validation/reported",
    "validation/tested",
    "validation/theoretical"
];
/* ───────────────────────────────────────────────────────────────────────
   GROUP B: TOP-LEVEL DOMAINS & HIGH-LEVEL SYSTEMS (L1/L2)
   Split into: B1 (Domains), B2 (Systems)
   ─────────────────────────────────────────────────────────────────────── */
// GROUP B1: Top-Level Domains (L1/L2)
const groupB1_Tags = [
    "artificial-intelligence",
    "behavioral-science",
    "cognitive-anthropology",
    "cognitive-development",
    "cognitive-ergonomics",
    "cognitive-linguistics",
    "cognitive-neuroscience",
    "cognitive-psychology",
    "cognitive-science",
    "computational-modeling",
    "cosmology",
    "critical-thinking",
    "decision-science",
    "digital-garden",
    "educational-psychology",
    "experimental-psychology",
    "human-factors",
    "information-architecture",
    "instructional-design",
    "knowledge-graph",
    "knowledge-work",
    "learning-science",
    "learning-theory",
    "neuroscience",
    "neuroimaging",
    "note-taking",
    "obsidian",
    "pkb",
    "pkm",
    "productivity",
    "productivity-systems",
    "prompt-engineering",
    "psychometrics",
    "psychology",
    "second-brain",
    "self-improvement",
    "self-regulation",
    "vault-architecture",
    "knowledge-workflow"
];
// GROUP B2: Systems & Methodologies (High-Level)
const groupB2_Tags = [
    "atomic-notes",
    "building-second-brain",
    "capture-system",
    "concept-mapping",
    "cornell-method",
    "dashboard-design",
    "evergreen-notes",
    "gtd",
    "hub-notes",
    "index-notes",
    "index-systems",
    "linking-strategy",
    "metadata-systems",
    "mind-mapping",
    "moc-system",
    "note-organization",
    "note-types",
    "organization-system",
    "outline-method",
    "para",
    "processing-workflow",
    "progressive-summarization",
    "retrieval-system",
    "review-system",
    "structure-notes",
    "synthesis-workflow",
    "tag-taxonomy",
    "zettelkasten"
];
/* ───────────────────────────────────────────────────────────────────────
   GROUP C: SUB-DOMAINS & PARENT PATHS (L3)
   Split into: C1 (PKM/PKB), C2 (Cognitive), C3 (Prompt Engineering)
   ─────────────────────────────────────────────────────────────────────── */
// GROUP C1: PKM/PKB/Obsidian Parent Paths
const groupC1_Tags = [
    "digital-garden/maintenance",
    "digital-garden/philosophy",
    "digital-garden/publishing",
    "digital-garden/structure",
    "information-architecture/navigation",
    "information-architecture/organization",
    "information-architecture/retrieval",
    "information-architecture/taxonomy",
    "knowledge-graph/linking",
    "knowledge-graph/structure",
    "knowledge-graph/theory",
    "knowledge-graph/visualization",
    "knowledge-work/learning",
    "knowledge-work/reading",
    "knowledge-work/research",
    "knowledge-work/thinking",
    "knowledge-work/writing",
    "knowledge-workflow/capture",
    "knowledge-workflow/output",
    "knowledge-workflow/processing",
    "knowledge-workflow/review",
    "knowledge-workflow/synthesis",
    "note-taking/formats",
    "note-taking/practices",
    "note-taking/types",
    "note-taking/zettelkasten",
    "obsidian/advanced",
    "obsidian/configuration",
    "obsidian/core-features",
    "obsidian/customization",
    "obsidian/plugins",
    "pkb/architecture",
    "pkb/components",
    "pkb/design",
    "pkb/maintenance",
    "pkb/metadata",
    "pkb/optimization",
    "pkm/methodology",
    "pkm/principles",
    "pkm/research",
    "pkm/theory",
    "pkm/workflow",
    "productivity/gtd",
    "productivity/para",
    "productivity/task-management",
    "productivity/time-management"
];
// GROUP C2: Cognitive Science Parent Paths
const groupC2_Tags = [
    "cognitive-science/attention",
    "cognitive-science/cognitive-load",
    "cognitive-science/executive-function",
    "cognitive-science/memory",
    "cognitive-science/metacognition",
    "cognitive-science/reasoning",
    "critical-thinking/analysis",
    "critical-thinking/evaluation",
    "critical-thinking/logic",
    "critical-thinking/problem-solving",
    "critical-thinking/synthesis",
    "learning-theory/andragogy",
    "learning-theory/cognitive-apprenticeship",
    "learning-theory/constructivism",
    "learning-theory/heutagogy",
    "learning-theory/pedagogy",
    "self-improvement/growth-mindset",
    "self-improvement/mental-models",
    "self-improvement/productivity",
    "self-improvement/reflective-practice",
    "self-improvement/skill-development",
    "self-regulation/behavioral",
    "self-regulation/emotional",
    "self-regulation/goal-setting",
    "self-regulation/motivation",
    "self-regulation/self-control",
    "self-regulation/theory"
];
// GROUP C3: Prompt Engineering Parent Paths
const groupC3_Tags = [
    "advanced-prompting/agents",
    "advanced-prompting/chain-systems",
    "advanced-prompting/function-calling",
    "advanced-prompting/multi-modal",
    "advanced-prompting/programming",
    "advanced-prompting/rag",
    "context-management/compression",
    "context-management/injection",
    "context-management/memory",
    "context-management/window",
    "llm-architecture/context-window",
    "llm-architecture/model-family",
    "llm-architecture/model-size",
    "llm-architecture/training",
    "llm-architecture/transformer",
    "llm-capability/generation",
    "llm-capability/knowledge",
    "llm-capability/reasoning",
    "llm-capability/understanding",
    "llm-limitation",
    "prompt-application/analysis",
    "prompt-application/coding",
    "prompt-application/creative",
    "prompt-application/education",
    "prompt-application/productivity",
    "prompt-application/writing",
    "prompt-engineering/anatomy",
    "prompt-engineering/evaluation",
    "prompt-engineering/optimization",
    "prompt-engineering/principles",
    "prompt-engineering/theory",
    "prompt-pattern/context-control",
    "prompt-pattern/error-handling",
    "prompt-pattern/multi-turn",
    "prompt-pattern/output-format",
    "prompt-pattern/persona",
    "prompt-pattern/template",
    "prompt-safety/adversarial",
    "prompt-safety/alignment",
    "prompt-safety/bias",
    "prompt-safety/content-policy",
    "prompt-safety/information-security",
    "prompt-workflow/deployment",
    "prompt-workflow/evaluation",
    "prompt-workflow/ideation",
    "prompt-workflow/prototyping",
    "prompt-workflow/version-control",
    "prompting-technique/chain-of-thought",
    "prompting-technique/few-shot",
    "prompting-technique/meta-prompting",
    "prompting-technique/react",
    "prompting-technique/reasoning",
    "prompting-technique/reflection",
    "prompting-technique/zero-shot"
];
/* ───────────────────────────────────────────────────────────────────────
   GROUPS D-J: GRANULAR CONCEPTS & MECHANISMS (L4 Leaves)
   Split by domain for manageable selection
   ─────────────────────────────────────────────────────────────────────── */
// GROUP D: Cognitive Science - Memory & Attention (Granular)
const groupD_Tags = [
    "attention",
    "auditory-perception",
    "autobiographical-memory",
    "consolidation",
    "divided-attention",
    "encoding",
    "episodic-memory",
    "interference",
    "long-term-memory",
    "multimodal-integration",
    "perception",
    "phonological-loop",
    "procedural-memory",
    "prospective-memory",
    "reconsolidation",
    "retrieval",
    "selective-attention",
    "semantic-memory",
    "sustained-attention",
    "visual-perception",
    "visuospatial-sketchpad",
    "working-memory"
];
// GROUP E: Cognitive Science - Executive Function & Reasoning (Granular)
const groupE_Tags = [
    "abductive-reasoning",
    "analogical-reasoning",
    "central-executive",
    "cognitive-control",
    "cognitive-flexibility",
    "conflict-monitoring",
    "creative-thinking",
    "critical-thinking",
    "deductive-reasoning",
    "error-monitoring",
    "executive-function",
    "inductive-reasoning",
    "inhibitory-control",
    "performance-monitoring",
    "planning",
    "problem-solving",
    "reasoning",
    "response-inhibition",
    "self-regulation",
    "task-switching"
];
// GROUP F: Cognitive Science - Learning & Metacognition (Granular)
const groupF_Tags = [
    "active-recall",
    "andragogy-pkm",
    "attention-management",
    "calibration",
    "calibration-practices",
    "cognitive-load-management",
    "cognitive-load-theory",
    "conceptual-learning",
    "control-processes",
    "desirable-difficulties",
    "elaborative-encoding",
    "elaborative-interrogation",
    "explicit-learning",
    "expertise-development",
    "generation-effect",
    "germane-load",
    "germane-load-optimization",
    "implicit-learning",
    "instructional-design-pkm",
    "interleaving",
    "intrinsic-load",
    "learning-processes",
    "metacognitive-monitoring",
    "metacognitive-pkm",
    "metacomprehension",
    "metamemory",
    "monitoring",
    "self-directed-learning",
    "self-explanation",
    "self-regulated-learning",
    "skill-acquisition",
    "spacing-effect",
    "testing-effect",
    "transfer-of-learning",
    "working-memory-capacity",
    "working-memory-support"
];
// GROUP G: Cognitive Science - Theories & Models (Granular)
const groupG_Tags = [
    "ACT-R",
    "cognitive-resources",
    "distributed-cognition",
    "dual-process-theory",
    "embodied-cognition",
    "enactive-cognition",
    "extraneous-load",
    "extraneous-load-reduction",
    "extended-cognition",
    "global-workspace-theory",
    "grounded-cognition",
    "information-processing-theory",
    "levels-of-processing",
    "memory-systems",
    "mental-effort",
    "multiple-drafts-model",
    "parallel-distributed-processing",
    "situated-cognition",
    "SOAR",
    "spreading-activation",
    "symbolic-architecture"
];
// GROUP H: PKM/Obsidian - Technical & Plugin Details (Granular)
const groupH_Tags = [
    "api-integration",
    "automation",
    "backlinks",
    "backup-systems",
    "bidirectional-links",
    "breadcrumbs",
    "daily-notes",
    "dataview",
    "dataview-queries",
    "dataviewjs",
    "excalidraw",
    "export-import",
    "file-naming",
    "filter-strategies",
    "folder-hierarchy",
    "folder-strategy",
    "frontmatter-design",
    "graph-analysis",
    "javascript",
    "language-processing",
    "link-density",
    "link-maintenance",
    "linking-strategy",
    "meeting-notes",
    "meta-bind",
    "metadata-schema",
    "metadata-systems",
    "naming-conventions",
    "note-templates",
    "obsidian-plugins",
    "orphan-notes",
    "progressive-review",
    "quick-capture",
    "quickadd",
    "quickadd-macros",
    "search-operators",
    "semantic-search",
    "smart-connections",
    "spaced-repetition",
    "status-tracking",
    "sync-systems",
    "tag-cleanup",
    "tag-strategy",
    "tag-taxonomy",
    "tasks-plugin",
    "template-automation",
    "templater",
    "templater-scripts",
    "transclusion",
    "unlinked-mentions",
    "version-control",
    "wiki-links"
];
// GROUP I: Prompt Engineering - Detailed Techniques (Granular)
const groupI_Tags = [
    "advanced-prompting/agents/autonomous",
    "advanced-prompting/agents/multi-agent",
    "advanced-prompting/agents/planning",
    "advanced-prompting/agents/tool-use",
    "advanced-prompting/rag/context-injection",
    "advanced-prompting/rag/hybrid-search",
    "advanced-prompting/rag/retrieval",
    "llm-limitation/bias",
    "llm-limitation/hallucination",
    "llm-limitation/reasoning-failures",
    "prompt-pattern/context-control/constraints",
    "prompt-pattern/context-control/framing",
    "prompt-pattern/context-control/perspective",
    "prompt-pattern/error-handling/clarification",
    "prompt-pattern/error-handling/fallback",
    "prompt-pattern/error-handling/validation",
    "prompt-pattern/multi-turn/context-threading",
    "prompt-pattern/multi-turn/conversation",
    "prompt-pattern/multi-turn/state-management",
    "prompt-pattern/output-format/code",
    "prompt-pattern/output-format/creative",
    "prompt-pattern/output-format/markdown",
    "prompt-pattern/output-format/structured-data",
    "prompt-pattern/persona/expertise",
    "prompt-pattern/persona/role-assignment",
    "prompt-pattern/persona/style",
    "prompt-pattern/template/fill-in-blank",
    "prompt-pattern/template/formulaic",
    "prompt-pattern/template/structured",
    "prompt-safety/adversarial/defense",
    "prompt-safety/adversarial/jailbreaking",
    "prompt-safety/adversarial/prompt-injection",
    "prompting-technique/chain-of-thought/basic",
    "prompting-technique/chain-of-thought/self-consistency",
    "prompting-technique/chain-of-thought/zero-shot",
    "prompting-technique/few-shot/diversity",
    "prompting-technique/few-shot/example-ordering",
    "prompting-technique/few-shot/example-selection",
    "prompting-technique/meta-prompting/optimization",
    "prompting-technique/meta-prompting/prompt-generation",
    "prompting-technique/meta-prompting/self-improvement",
    "prompting-technique/react/iteration",
    "prompting-technique/react/reasoning-acting",
    "prompting-technique/react/tool-use",
    "prompting-technique/reasoning/decomposition",
    "prompting-technique/reasoning/graph-of-thoughts",
    "prompting-technique/reasoning/step-by-step",
    "prompting-technique/reasoning/tree-of-thoughts",
    "prompting-technique/reflection/refinement",
    "prompting-technique/reflection/self-critique",
    "prompting-technique/reflection/verification",
    "prompting-technique/zero-shot/instruction",
    "prompting-technique/zero-shot/task-specification"
];
// GROUP J: Cross-Cutting Concepts & Research (Granular)
const groupJ_Tags = [
    "aging-cognition",
    "applied-cognition",
    "attention-architecture",
    "behavioral-experiments",
    "clinical-cognition",
    "cognitive-decline",
    "cognitive-disorders",
    "cognitive-enhancement",
    "cognitive-modeling",
    "cognitive-pkm",
    "cognitive-rehabilitation",
    "cognitive-training",
    "concept/attention-mechanism",
    "concept/atomic-notes",
    "concept/automaticity",
    "concept/bidirectional-linking",
    "concept/chunking",
    "concept/cognitive-bias",
    "concept/cognitive-overhead",
    "concept/context-switching",
    "concept/discoverability",
    "concept/distributed-practice",
    "concept/dual-coding",
    "concept/elaboration",
    "concept/emergence",
    "concept/error-correction",
    "concept/evergreen-notes",
    "concept/external-cognition",
    "concept/few-shot-exemplars",
    "concept/flow-state",
    "concept/generation-effect",
    "concept/in-context-learning",
    "concept/information-overload",
    "concept/instruction-following",
    "concept/interleaving",
    "concept/knowledge-synthesis",
    "concept/knowledge-transfer",
    "concept/linking-thinking",
    "concept/mental-representation",
    "concept/networked-thought",
    "concept/output-validation",
    "concept/progressive-summarization",
    "concept/prompt-chaining",
    "concept/prompt-template",
    "concept/retrieval-practice",
    "concept/second-brain",
    "concept/semantic-similarity",
    "concept/serendipity",
    "concept/spacing-effect",
    "concept/system-message",
    "concept/task-decomposition",
    "concept/temperature-control",
    "concept/testing-effect",
    "concept/token-probability",
    "concept/top-p-sampling",
    "concept/transfer",
    "concept/transformer-architecture",
    "concept/wayfinding",
    "consolidation-workflow",
    "cross-cultural-cognition",
    "cross-sectional-research",
    "developmental-cognition",
    "educational-applications",
    "empirical-research",
    "encoding-strategies",
    "evidence-based-pkm",
    "experimental-design",
    "learning-analytics",
    "learning-optimization",
    "longitudinal-research",
    "memory-systems-design",
    "meta-analysis",
    "neurodevelopmental",
    "neuroimaging-studies",
    "reflection-systems",
    "retrieval-practice-pkm",
    "spaced-review-system",
    "technology-cognition",
    "workplace-cognition"
];
/* ═══════════════════════════════════════════════════════════════════════
   HELPER FUNCTION: PRETTY PRINT TAGS WITH ICONS
   ═══════════════════════════════════════════════════════════════════════ */
function formatTagsForDisplay(tags) {
    return tags.map(tag => {
        let icon = "🔹"; // Default bullet
        // Assign Icons based on Domain Keywords (Prioritize Specificity)
        // --- META / STRUCTURE ---
        if (tag.startsWith("type/")) icon = "📑";
        else if (tag.startsWith("status/")) icon = "🚦";
        else if (tag.startsWith("context/")) icon = "🌐";
        else if (tag.startsWith("source/")) icon = "📚";
        else if (tag.startsWith("maturity/")) icon = "🍷";
        else if (tag.startsWith("mode/")) icon = "⚙️";
        else if (tag.startsWith("validation/") || tag.startsWith("complexity/")) icon = "📏";
        else if (tag.startsWith("nature/")) icon = "🌿";
        else if (tag.startsWith("model/")) icon = "🤖";
        // --- PKM & OBSIDIAN ---
        else if (tag.includes("obsidian") || tag.includes("dataview") || tag.includes("plugin")) icon = "💎";
        else if (tag.includes("pkm") || tag.includes("pkb") || tag.includes("zettelkasten") || tag.includes("para")) icon = "🧠";
        else if (tag.includes("workflow") || tag.includes("system") || tag.includes("architecture")) icon = "🔄";
        else if (tag.includes("information-architecture") || tag.includes("taxonomy")) icon = "🗂️";
        // --- COGNITIVE SCIENCE ---
        else if (tag.includes("neuro") || tag.includes("brain")) icon = "🧬";
        else if (tag.includes("memory") || tag.includes("encoding") || tag.includes("recall")) icon = "💾";
        else if (tag.includes("learning") || tag.includes("education") || tag.includes("student") || tag.includes("andragogy")) icon = "🎓";
        else if (tag.includes("attention") || tag.includes("focus")) icon = "🎯";
        else if (tag.includes("reasoning") || tag.includes("logic") || tag.includes("thinking") || tag.includes("decision")) icon = "💡";
        else if (tag.includes("cognitive") || tag.includes("psychology") || tag.includes("behavior")) icon = "🧩";
        else if (tag.includes("regulation") || tag.includes("motivation") || tag.includes("self")) icon = "💪";
        // --- PROMPT ENGINEERING / AI ---
        else if (tag.includes("prompt") || tag.includes("chain-of-thought")) icon = "💬";
        else if (tag.includes("llm") || tag.includes("gpt") || tag.includes("claude") || tag.includes("gemini") || tag.includes("artificial")) icon = "🤖";
        else if (tag.includes("agent") || tag.includes("rag")) icon = "🕵️";
        else if (tag.includes("safety") || tag.includes("bias")) icon = "🛡️";
        // --- COSMOLOGY ---
        else if (tag.includes("cosmology") || tag.includes("universe")) icon = "🌌";
        // --- CROSS-CUTTING / RESEARCH ---
        else if (tag.includes("concept/")) icon = "💡";
        else if (tag.includes("research") || tag.includes("analysis") || tag.includes("study")) icon = "🔬";
        // Format: Replace slashes with visual arrows for cleaner reading
        let cleanText = tag.split("/").join("  ›  ");
        return `${icon} ${cleanText}`;
    });
}
/* ═══════════════════════════════════════════════════════════════════════
   INPUT SYSTEM: USER PROMPTS & SUGGESTERS
   ═══════════════════════════════════════════════════════════════════════ */
// ─────────────────────────────────────────────────────────────────────────
// STEP 1: BASIC METADATA COLLECTION
// ─────────────────────────────────────────────────────────────────────────
const title = await tp.system.prompt("Enter Note Title (Concept Name):");
// Exit early if title is cancelled to prevent creating empty files
if (title == null) { return; } 
const alias1 = await tp.system.prompt("Enter Alias 1 (Press Enter to skip):");
const alias2 = await tp.system.prompt("Enter Alias 2 (Press Enter to skip):");
// ─────────────────────────────────────────────────────────────────────────
// STEP 2: METADATA SUGGESTERS (Type, Source, Link-Up)
// ─────────────────────────────────────────────────────────────────────────
const type = await tp.system.suggester(typeList, typeList, false, "Select Note TYPE:");
const source = await tp.system.suggester(sourceList, sourceList, false, "Select SOURCE / ORIGIN:");
const linkUp = await tp.system.suggester(linkUpList, linkUpList, false, "Select LINK-UP MOC:");
// ─────────────────────────────────────────────────────────────────────────
// STEP 3: STATUS TRACKING FIELDS
// ─────────────────────────────────────────────────────────────────────────
const maturity = await tp.system.suggester(maturityLevels, maturityLevels, false, "Select Maturity Level:");
const confidence = await tp.system.suggester(confidenceLevels, confidenceLevels, false, "Select Confidence Level:");
// ─────────────────────────────────────────────────────────────────────────
// STEP 4: TAG SELECTION (8 TAGS ACROSS HIERARCHICAL GROUPS)
// ─────────────────────────────────────────────────────────────────────────
/* TAG SELECTION STRATEGY:
   - Tags 1-2: Meta-dimensions (Type, Status, Context, Mode, etc.)
   - Tags 3-4: Top-level domains & systems
   - Tags 5-6: Sub-domains & methodologies
   - Tags 7-8: Granular concepts & mechanisms
*/
// Prepare Display Arrays (Alphabetically Sorted with Icons)
const groupA1_Display = formatTagsForDisplay(groupA1_Tags.sort());
const groupA2_Display = formatTagsForDisplay(groupA2_Tags.sort());
const groupA3_Display = formatTagsForDisplay(groupA3_Tags.sort());
const groupA4_Display = formatTagsForDisplay(groupA4_Tags.sort());
const groupB1_Display = formatTagsForDisplay(groupB1_Tags.sort());
const groupB2_Display = formatTagsForDisplay(groupB2_Tags.sort());
const groupC1_Display = formatTagsForDisplay(groupC1_Tags.sort());
const groupC2_Display = formatTagsForDisplay(groupC2_Tags.sort());
const groupC3_Display = formatTagsForDisplay(groupC3_Tags.sort());
const groupD_Display = formatTagsForDisplay(groupD_Tags.sort());
const groupE_Display = formatTagsForDisplay(groupE_Tags.sort());
const groupF_Display = formatTagsForDisplay(groupF_Tags.sort());
const groupG_Display = formatTagsForDisplay(groupG_Tags.sort());
const groupH_Display = formatTagsForDisplay(groupH_Tags.sort());
const groupI_Display = formatTagsForDisplay(groupI_Tags.sort());
const groupJ_Display = formatTagsForDisplay(groupJ_Tags.sort());
// Meta-Dimension Tags (Select from Group A sub-arrays)
const tag1 = await tp.system.suggester(groupA1_Display, groupA1_Tags.sort(), false, "TAG 1 - Meta: Type");
const tag2 = await tp.system.suggester(groupA2_Display, groupA2_Tags.sort(), false, "TAG 2 - Meta: Status");
// Top-Level Domain & System Tags (Select from Group B)
const tag3 = await tp.system.suggester(groupB1_Display, groupB1_Tags.sort(), false, "TAG 3 - Domain (L1/L2)");
const tag4 = await tp.system.suggester(groupB2_Display, groupB2_Tags.sort(), false, "TAG 4 - System/Methodology");
// Sub-Domain & Parent Path Tags (Select from Group C - Choose relevant sub-group)
const tag5 = await tp.system.suggester(groupC1_Display, groupC1_Tags.sort(), false, "TAG 5 - Sub-Domain: PKM/PKB");
const tag6 = await tp.system.suggester(groupC2_Display, groupC2_Tags.sort(), false, "TAG 6 - Sub-Domain: Cognitive");
// Granular Concept Tags (Select from Groups D-J - Choose relevant sub-groups)
const tag7 = await tp.system.suggester(groupD_Display, groupD_Tags.sort(), false, "TAG 7 - Concept: Memory/Attention");
const tag8 = await tp.system.suggester(groupE_Display, groupE_Tags.sort(), false, "TAG 8 - Concept: Executive/Reasoning");
// ─────────────────────────────────────────────────────────────────────────
// STEP 5: DATE CALCULATIONS
// ─────────────────────────────────────────────────────────────────────────
const dateNow = tp.date.now("YYYY-MM-DD");
const timeNow = tp.date.now("HH:mm:ss");
const year = tp.date.now("YYYY");
const id = tp.date.now("YYYYMMDDHHmmss");
// Calculate Next Review Date (Spaced Repetition - 7 days from now)
const nextReview = tp.date.now("YYYY-MM-DD", 7);
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

> [!abstract] Overview
> Brief summary of the concept/topic.



**{{PASTE REPORT/REFERENCE HERE}}**



## 🔗 Related Concepts

- [[Related Concept 1]] - [Brief connection explanation]
- [[Related Concept 2]] - [Brief connection explanation]
- [[Related Concept 3]] - [Brief connection explanation]

## 📚 References & Sources

1. [Source citation or internal reference]
2. [Source citation or internal reference]

## 💭 Personal Insights

> [!note] Reflection
> [Your thoughts, connections, or questions about this concept]

---

**Last Modified:** <% dateNow %>  
**Next Review:** <% nextReview %>