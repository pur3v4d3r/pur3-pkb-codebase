<%*
/* ═══════════════════════════════════════════════════════════════════════
   _permanent-note-template-v2.0.0-contextual
   INTELLIGENT CONTEXTUAL TAG SELECTION SYSTEM
   Dynamically adapts tag suggestions based on domain context
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
    "methodology",
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
    "gemini-flash-3.0",
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
   MASTER TAXONOMY: TAG ARRAYS ORGANIZED BY DOMAIN
   ═══════════════════════════════════════════════════════════════════════ */
/* ───────────────────────────────────────────────────────────────────────
   META-DIMENSION TAGS (Always Available)
   ─────────────────────────────────────────────────────────────────────── */
const metaTypeTags = [
    "type/analysis",
    "type/case-study",
    "type/claude-project",
    "type/comparison",
    "type/concept",
    "type/dashboard",
    "type/definition",
    "type/experiment",
    "type/fleeting",
    "type/framework",
    "type/gemini-gem",
    "type/guide",
    "type/literature",
    "type/mental-model",
    "type/methodology",
    "type/moc",
    "type/pattern",
    "type/permanent",
    "type/practice-log",
    "type/principle",
    "type/prompt-library",
    "type/reference",
    "type/reflection",
    "type/report",
    "type/review",
    "type/strategy",
    "type/synthesis",
    "type/technique",
    "type/template",
    "type/theory",
    "type/tutorial"
];
const metaStatusTags = [
    "status/archived",
    "status/budding",
    "status/complete",
    "status/deprecated",
    "status/evergreen",
    "status/experimental",
    "status/in-progress",
    "status/needs-review",
    "status/not-read",
    "status/production",
    "status/proven",
    "status/read",
    "status/seedling",
    "status/under-revision"
];
const metaContextTags = [
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
    "context/tutorial"
];
const metaSourceTags = [
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
/* ───────────────────────────────────────────────────────────────────────
   PKM/PKB DOMAIN TAGS
   ─────────────────────────────────────────────────────────────────────── */
const pkmDomainTags = [
    "pkm",
    "pkb",
    "note-taking",
    "knowledge-workflow",
    "obsidian",
    "information-architecture",
    "knowledge-graph",
    "knowledge-work"
];
const pkmSubdomainTags = [
    // PKM Theory & Methodology
    "pkm/theory",
    "pkm/theory/foundations",
    "pkm/theory/epistemology",
    "pkm/theory/cognitive-basis",
    "pkm/methodology",
    "pkm/methodology/zettelkasten",
    "pkm/methodology/para",
    "pkm/methodology/lyt",
    "pkm/methodology/evergreen-notes",
    "pkm/methodology/digital-garden",
    // PKB Architecture
    "pkb/architecture",
    "pkb/architecture/structure",
    "pkb/architecture/hierarchy",
    "pkb/architecture/taxonomy",
    "pkb/design",
    "pkb/design/information-architecture",
    "pkb/design/navigation",
    "pkb/design/discoverability",
    // PKB Components
    "pkb/components",
    "pkb/components/moc",
    "pkb/components/hub-notes",
    "pkb/components/dashboards",
    "pkb/components/atomic-notes",
    // Metadata & Maintenance
    "pkb/metadata",
    "pkb/metadata/tags",
    "pkb/metadata/properties",
    "pkb/metadata/frontmatter",
    "pkb/maintenance",
    "pkb/optimization",
    // Obsidian Specific
    "obsidian/core-features",
    "obsidian/plugins",
    "obsidian/plugins/dataview",
    "obsidian/plugins/templater",
    "obsidian/plugins/quickadd",
    "obsidian/plugins/tasks",
    "obsidian/plugins/meta-bind",
    "obsidian/plugins/commander",
    "obsidian/customization",
    "obsidian/advanced",
    "obsidian/advanced/dataviewjs",
    "obsidian/advanced/automation",
    // Knowledge Graph
    "knowledge-graph/theory",
    "knowledge-graph/structure",
    "knowledge-graph/linking",
    "knowledge-graph/visualization"
];
const pkmGranularTags = [
    // Note Types & Templates
    "note-templates",
    "frontmatter-design",
    "template-automation",
    "quick-capture",
    "daily-notes",
    "atomic-concept",
    "reference-note",
    "literature-note",
    "permanent-note",
    "fleeting-note",
    // Linking & Connection
    "wiki-links",
    "backlinks",
    "bidirectional-links",
    "link-density",
    "transclusion",
    // Organization
    "tag-strategy",
    "folder-strategy",
    "file-naming",
    "metadata-schema",
    // Search & Retrieval
    "dataview-queries",
    "graph-analysis",
    "semantic-search",
    // Review & Maintenance
    "spaced-repetition",
    "progressive-review",
    "link-maintenance",
    "tag-cleanup"
];
/* ───────────────────────────────────────────────────────────────────────
   COGNITIVE SCIENCE DOMAIN TAGS
   ─────────────────────────────────────────────────────────────────────── */
const cogSciDomainTags = [
    "cognitive-science",
    "cognitive-psychology",
    "cognitive-neuroscience",
    "cognitive-development",
    "cognitive-linguistics",
    "behavioral-science",
    "neuroscience",
    "psychology",
    "educational-psychology",
    "learning-theory"
];
const cogSciSubdomainTags = [
    // Memory Systems
    "memory",
    "memory/working-memory",
    "memory/long-term-memory",
    "memory/episodic-memory",
    "memory/semantic-memory",
    "memory/procedural-memory",
    "memory/encoding",
    "memory/consolidation",
    "memory/retrieval",
    // Attention Systems
    "attention",
    "attention/selective-attention",
    "attention/divided-attention",
    "attention/sustained-attention",
    "attention/executive-attention",
    // Executive Function
    "executive-function",
    "executive-function/cognitive-control",
    "executive-function/inhibition",
    "executive-function/working-memory",
    "executive-function/cognitive-flexibility",
    // Learning & Development
    "learning",
    "learning/implicit-learning",
    "learning/explicit-learning",
    "learning/skill-acquisition",
    "learning/transfer",
    "learning/metacognition",
    // Reasoning & Problem-Solving
    "reasoning",
    "reasoning/deductive",
    "reasoning/inductive",
    "reasoning/analogical",
    "problem-solving",
    "decision-making",
    // Language & Communication
    "language",
    "language/comprehension",
    "language/production",
    "language/acquisition",
    // Perception & Cognition
    "perception",
    "visual-processing",
    "auditory-processing",
    "pattern-recognition"
];
const cogSciTheoriesTags = [
    // Major Theories
    "cognitive-load-theory",
    "information-processing-theory",
    "dual-coding-theory",
    "schema-theory",
    "situated-cognition",
    "embodied-cognition",
    "distributed-cognition",
    // Memory Models
    "multi-store-model",
    "working-memory-model",
    "levels-of-processing",
    "encoding-specificity",
    // Learning Theories
    "constructivism",
    "social-cognitive-theory",
    "self-regulated-learning",
    "expertise-development",
    // Educational Models
    "cognitive-apprenticeship",
    "scaffolding",
    "zone-of-proximal-development",
    "deliberate-practice"
];
const cogSciGranularTags = [
    // Memory Mechanisms
    "phonological-loop",
    "visuospatial-sketchpad",
    "episodic-buffer",
    "central-executive",
    "consolidation-processes",
    "retrieval-cues",
    // Attention Mechanisms
    "attentional-control",
    "attentional-capture",
    "inattentional-blindness",
    "change-blindness",
    // Learning Mechanisms
    "spacing-effect",
    "testing-effect",
    "generation-effect",
    "desirable-difficulties",
    "interleaving",
    "elaboration",
    // Cognitive Processes
    "automaticity",
    "chunking",
    "cognitive-schemas",
    "mental-models",
    "heuristics",
    "biases"
];
/* ───────────────────────────────────────────────────────────────────────
   PROMPT ENGINEERING DOMAIN TAGS
   ─────────────────────────────────────────────────────────────────────── */
const promptEngDomainTags = [
    "prompt-engineering",
    "artificial-intelligence",
    "llm",
    "ai-interaction",
    "conversational-ai"
];
const promptEngSubdomainTags = [
    // Core Techniques
    "prompt-engineering/techniques",
    "prompt-engineering/patterns",
    "prompt-engineering/optimization",
    "prompt-engineering/evaluation",
    // Prompting Methods
    "chain-of-thought",
    "few-shot-learning",
    "zero-shot-learning",
    "role-prompting",
    "system-prompting",
    "constitutional-ai",
    // Advanced Patterns
    "tree-of-thoughts",
    "react-prompting",
    "self-consistency",
    "chain-of-density",
    "meta-prompting",
    // AI Architectures
    "rag",
    "rag/retrieval",
    "rag/generation",
    "rag/context-management",
    "agent-systems",
    "multi-agent-systems",
    // Model Interaction
    "llm/claude",
    "llm/gpt",
    "llm/gemini",
    "llm/local-models",
    // Safety & Ethics
    "ai-safety",
    "ai-alignment",
    "bias-mitigation",
    "hallucination-prevention"
];
const promptEngGranularTags = [
    // Specific Techniques
    "instruction-following",
    "context-window-management",
    "token-optimization",
    "prompt-chaining",
    "prompt-templates",
    "dynamic-prompting",
    // Evaluation & Testing
    "prompt-testing",
    "output-validation",
    "quality-assessment",
    "benchmarking",
    // Integration
    "api-integration",
    "workflow-automation",
    "tool-use",
    "function-calling",
    // Advanced Concepts
    "emergent-abilities",
    "in-context-learning",
    "prompt-injection",
    "jailbreaking",
    "adversarial-prompting"
];
/* ───────────────────────────────────────────────────────────────────────
   CROSS-DOMAIN INTEGRATION TAGS
   ─────────────────────────────────────────────────────────────────────── */
const crossDomainTags = [
    // PKM + Cognitive Science
    "cognitive-pkm",
    "evidence-based-pkm",
    "learning-optimization",
    "memory-systems-design",
    "attention-architecture",
    "spaced-review-system",
    "retrieval-practice-pkm",
    "encoding-strategies",
    "cognitive-load-management",
    "metacognitive-pkm",
    // Educational Psychology Applications
    "instructional-design-pkm",
    "andragogy-pkm",
    "self-directed-learning",
    "expertise-development",
    // AI + PKM
    "ai-assisted-pkm",
    "llm-knowledge-work",
    "semantic-search-ai",
    // Research Methods
    "empirical-research",
    "experimental-design",
    "qualitative-research",
    "quantitative-research",
    "mixed-methods"
];
/* ═══════════════════════════════════════════════════════════════════════
   HELPER FUNCTIONS
   ═══════════════════════════════════════════════════════════════════════ */
/**
 * Format tags with icons for better visual scanning
 */
function formatTagsForDisplay(tags) {
    return tags.map(tag => {
        let icon = "🏷️"; // Default
        // META DIMENSIONS
        if (tag.startsWith("type/")) icon = "📝";
        else if (tag.startsWith("status/")) icon = "📊";
        else if (tag.startsWith("context/")) icon = "🎯";
        else if (tag.startsWith("source/")) icon = "📚";
        else if (tag.startsWith("mode/")) icon = "⚙️";
        else if (tag.startsWith("complexity/")) icon = "📈";
        else if (tag.startsWith("maturity/")) icon = "🌱";
        // PKM/PKB
        else if (tag.includes("pkm") || tag.includes("pkb")) icon = "🧠";
        else if (tag.includes("obsidian") || tag.includes("plugin")) icon = "💎";
        else if (tag.includes("note") || tag.includes("template")) icon = "📄";
        else if (tag.includes("graph") || tag.includes("link")) icon = "🔗";
        else if (tag.includes("workflow") || tag.includes("automation")) icon = "⚡";
        else if (tag.includes("dataview") || tag.includes("query")) icon = "🔍";
        // COGNITIVE SCIENCE
        else if (tag.includes("memory") || tag.includes("encoding") || tag.includes("retrieval")) icon = "🧩";
        else if (tag.includes("attention") || tag.includes("focus")) icon = "👁️";
        else if (tag.includes("executive") || tag.includes("control")) icon = "🎛️";
        else if (tag.includes("learning") || tag.includes("acquisition")) icon = "📖";
        else if (tag.includes("reasoning") || tag.includes("problem-solving")) icon = "💭";
        else if (tag.includes("language") || tag.includes("linguistic")) icon = "💬";
        else if (tag.includes("neuroscience") || tag.includes("brain")) icon = "🧠";
        else if (tag.includes("perception") || tag.includes("visual") || tag.includes("auditory")) icon = "👀";
        // THEORIES & MODELS
        else if (tag.includes("theory") || tag.includes("model")) icon = "🔬";
        else if (tag.includes("schema") || tag.includes("mental-model")) icon = "🗺️";
        // PROMPT ENGINEERING
        else if (tag.includes("prompt")) icon = "💬";
        else if (tag.includes("llm") || tag.includes("ai") || tag.includes("claude") || tag.includes("gpt")) icon = "🤖";
        else if (tag.includes("rag") || tag.includes("agent")) icon = "🕵️";
        else if (tag.includes("chain-of-thought") || tag.includes("reasoning")) icon = "🔗";
        else if (tag.includes("safety") || tag.includes("alignment")) icon = "🛡️";
        // CROSS-DOMAIN
        else if (tag.includes("cognitive-pkm") || tag.includes("evidence-based")) icon = "🎓";
        else if (tag.includes("research") || tag.includes("empirical")) icon = "🔬";
        // Format: Clean display with arrows for hierarchy
        let cleanText = tag.split("/").join("  ›  ");
        return `${icon} ${cleanText}`;
    });
}
/**
 * Determine relevant tag pools based on domain context
 */
function getContextualTagPool(primaryDomain, secondaryDomain = null) {
    let pool = [];
    // Always include cross-domain tags
    pool = pool.concat(crossDomainTags);
    // Add domain-specific tags based on primary domain
    if (primaryDomain.includes("pkm") || primaryDomain.includes("pkb") || 
        primaryDomain.includes("obsidian") || primaryDomain.includes("note-taking") ||
        primaryDomain.includes("knowledge-workflow") || primaryDomain.includes("information-architecture") ||
        primaryDomain.includes("knowledge-graph") || primaryDomain.includes("knowledge-work")) {
        pool = pool.concat(pkmSubdomainTags, pkmGranularTags);
    }
    if (primaryDomain.includes("cognitive") || primaryDomain.includes("neuroscience") ||
        primaryDomain.includes("psychology") || primaryDomain.includes("learning") ||
        primaryDomain.includes("memory") || primaryDomain.includes("attention")) {
        pool = pool.concat(cogSciSubdomainTags, cogSciTheoriesTags, cogSciGranularTags);
    }
    if (primaryDomain.includes("prompt") || primaryDomain.includes("ai") ||
        primaryDomain.includes("llm") || primaryDomain.includes("artificial")) {
        pool = pool.concat(promptEngSubdomainTags, promptEngGranularTags);
    }
    // Add secondary domain tags if specified
    if (secondaryDomain) {
        if (secondaryDomain.includes("pkm") || secondaryDomain.includes("pkb") ||
            secondaryDomain.includes("obsidian")) {
            pool = pool.concat(pkmSubdomainTags.filter(tag => !pool.includes(tag)));
        }
        if (secondaryDomain.includes("cognitive") || secondaryDomain.includes("psychology") ||
            secondaryDomain.includes("learning")) {
            pool = pool.concat(cogSciSubdomainTags.filter(tag => !pool.includes(tag)));
        }
        if (secondaryDomain.includes("prompt") || secondaryDomain.includes("ai")) {
            pool = pool.concat(promptEngSubdomainTags.filter(tag => !pool.includes(tag)));
        }
    }
    // Remove duplicates and sort
    pool = […new Set(pool)].sort();
    return pool;
}
/**
 * Smart tag suggestions based on already-selected tags
 */
function getAdaptiveTagSuggestions(selectedTags) {
    // Extract domains from already selected tags
    const hasPKM = selectedTags.some(tag => 
        tag.includes("pkm") || tag.includes("pkb") || tag.includes("obsidian") || 
        tag.includes("note") || tag.includes("knowledge-workflow")
    );
    const hasCogSci = selectedTags.some(tag => 
        tag.includes("cognitive") || tag.includes("psychology") || 
        tag.includes("neuroscience") || tag.includes("learning") || 
        tag.includes("memory") || tag.includes("attention")
    );
    const hasPromptEng = selectedTags.some(tag => 
        tag.includes("prompt") || tag.includes("ai") || 
        tag.includes("llm") || tag.includes("rag")
    );
    let suggestions = [];
    // Build contextual suggestions
    if (hasPKM && hasCogSci) {
        suggestions = suggestions.concat([
            "cognitive-pkm",
            "evidence-based-pkm",
            "memory-systems-design",
            "spaced-review-system",
            "metacognitive-pkm"
        ]);
    }
    if (hasPKM && hasPromptEng) {
        suggestions = suggestions.concat([
            "ai-assisted-pkm",
            "llm-knowledge-work",
            "semantic-search-ai",
            "automation"
        ]);
    }
    if (hasCogSci && hasPromptEng) {
        suggestions = suggestions.concat([
            "ai-alignment",
            "cognitive-modeling",
            "learning-optimization"
        ]);
    }
    if (hasPKM) {
        suggestions = suggestions.concat(pkmGranularTags.slice(0, 15));
    }
    if (hasCogSci) {
        suggestions = suggestions.concat(cogSciGranularTags.slice(0, 15));
    }
    if (hasPromptEng) {
        suggestions = suggestions.concat(promptEngGranularTags.slice(0, 15));
    }
    // Remove duplicates and already-selected tags
    suggestions = […new Set(suggestions)]
        .filter(tag => !selectedTags.includes(tag))
        .sort();
    return suggestions;
}
/* ═══════════════════════════════════════════════════════════════════════
   INPUT SYSTEM: USER PROMPTS & INTELLIGENT SUGGESTERS
   ═══════════════════════════════════════════════════════════════════════ */
// ─────────────────────────────────────────────────────────────────────────
// STEP 1: BASIC METADATA COLLECTION
// ─────────────────────────────────────────────────────────────────────────
const title = await tp.system.prompt("Enter Note Title (Concept Name):");
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
// STEP 4: INTELLIGENT TAG SELECTION (CONTEXTUAL & ADAPTIVE)
// ─────────────────────────────────────────────────────────────────────────
/* INTELLIGENT TAG SELECTION STRATEGY:
   1. Start with meta-dimensions (type, status, context)
   2. Select primary domain - this determines subsequent options
   3. Optionally select secondary domain
   4. Subdomain and granular tags are filtered based on domain context
   5. Cross-domain tags appear when multiple domains are selected
*/
// Track selected tags for adaptive suggestions
let selectedTags = [];
// TAG 1: Meta - Type
const metaTypeDisplay = formatTagsForDisplay(metaTypeTags.sort());
const tag1 = await tp.system.suggester(metaTypeDisplay, metaTypeTags.sort(), false, "TAG 1 - Meta: Type");
selectedTags.push(tag1);
// TAG 2: Meta - Status
const metaStatusDisplay = formatTagsForDisplay(metaStatusTags.sort());
const tag2 = await tp.system.suggester(metaStatusDisplay, metaStatusTags.sort(), false, "TAG 2 - Meta: Status");
selectedTags.push(tag2);
// TAG 3: PRIMARY DOMAIN (L1) - This determines contextual filtering
const allDomainTags = […new Set([…pkmDomainTags, …cogSciDomainTags, …promptEngDomainTags])].sort();
const allDomainDisplay = formatTagsForDisplay(allDomainTags);
const tag3 = await tp.system.suggester(allDomainDisplay, allDomainTags, false, "TAG 3 - Primary Domain (L1)");
selectedTags.push(tag3);
// TAG 4: SECONDARY DOMAIN (Optional) or Context
// Offer remaining domains + context tags
const remainingDomains = allDomainTags.filter(d => d !== tag3);
const secondaryOptions = […remainingDomains, …metaContextTags].sort();
const secondaryDisplay = formatTagsForDisplay(secondaryOptions);
const tag4 = await tp.system.suggester(secondaryDisplay, secondaryOptions, false, "TAG 4 - Secondary Domain or Context (Optional)");
selectedTags.push(tag4);
// GENERATE CONTEXTUAL TAG POOL based on selected domains
const contextualPool = getContextualTagPool(tag3, tag4);
const contextualDisplay = formatTagsForDisplay(contextualPool);
// TAG 5: SUBDOMAIN (Contextual to primary/secondary domain)
const tag5 = await tp.system.suggester(
    contextualDisplay, 
    contextualPool, 
    false, 
    "TAG 5 - Subdomain (Filtered by your domain selection)"
);
selectedTags.push(tag5);
// TAG 6: SUBDOMAIN or Methodology (Contextual)
// Remove already selected tag from options
const contextualPool2 = contextualPool.filter(t => !selectedTags.includes(t));
const contextualDisplay2 = formatTagsForDisplay(contextualPool2);
const tag6 = await tp.system.suggester(
    contextualDisplay2, 
    contextualPool2, 
    false, 
    "TAG 6 - Subdomain/Methodology (Filtered)"
);
selectedTags.push(tag6);
// TAG 7-10: ADAPTIVE SUGGESTIONS based on tag combinations
const adaptiveSuggestions = getAdaptiveTagSuggestions(selectedTags);
const adaptiveDisplay = formatTagsForDisplay(adaptiveSuggestions);
const tag7 = await tp.system.suggester(
    adaptiveDisplay, 
    adaptiveSuggestions, 
    false, 
    "TAG 7 - Granular Concept (Smart Suggestions)"
);
selectedTags.push(tag7);
// Update adaptive pool for remaining selections
const adaptiveSuggestions2 = adaptiveSuggestions.filter(t => !selectedTags.includes(t));
const adaptiveDisplay2 = formatTagsForDisplay(adaptiveSuggestions2);
const tag8 = await tp.system.suggester(
    adaptiveDisplay2, 
    adaptiveSuggestions2, 
    false, 
    "TAG 8 - Granular Concept (Smart Suggestions)"
);
selectedTags.push(tag8);
const adaptiveSuggestions3 = adaptiveSuggestions2.filter(t => !selectedTags.includes(t));
const adaptiveDisplay3 = formatTagsForDisplay(adaptiveSuggestions3);
const tag9 = await tp.system.suggester(
    adaptiveDisplay3, 
    adaptiveSuggestions3, 
    false, 
    "TAG 9 - Granular Concept (Smart Suggestions)"
);
selectedTags.push(tag9);
const adaptiveSuggestions4 = adaptiveSuggestions3.filter(t => !selectedTags.includes(t));
const adaptiveDisplay4 = formatTagsForDisplay(adaptiveSuggestions4);
const tag10 = await tp.system.suggester(
    adaptiveDisplay4, 
    adaptiveSuggestions4, 
    false, 
    "TAG 10 - Granular Concept (Optional)"
);
if (tag10) selectedTags.push(tag10);
// ═══════════════════════════════════════════════════════════════════════
// VALIDATION: Ensure critical tags were selected
// ═══════════════════════════════════════════════════════════════════════
if (!tag1 || !tag2 || !tag3) {
    new Notice("⚠️ Template Error: Required tags (Type, Status, Domain) not selected.");
    return;
}
// Clean any undefined/null entries from selectedTags array
selectedTags = selectedTags.filter(tag => tag !== undefined && tag !== null && tag !== "");
// Handle empty optional tags for YAML output
const safeTag4 = tag4 || "";
const safeTag5 = tag5 || "";
const safeTag6 = tag6 || "";
const safeTag7 = tag7 || "";
const safeTag8 = tag8 || "";
const safeTag9 = tag9 || "";
const safeTag10 = tag10 || "";
// ─────────────────────────────────────────────────────────────────────────
// STEP 5: DATE CALCULATIONS
// ─────────────────────────────────────────────────────────────────────────
const dateNow = tp.date.now("YYYY-MM-DD");
const timeNow = tp.date.now("HH:mm:ss");
const year = tp.date.now("YYYY");
const id = tp.date.now("YYYYMMDDHHmmss");
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
<%* if (safeTag4) { -%>
  - "<% safeTag4 %>"
<%* } -%>
<%* if (safeTag5) { -%>
  - "<% safeTag5 %>"
<%* } -%>
<%* if (safeTag6) { -%>
  - "<% safeTag6 %>"
<%* } -%>
<%* if (safeTag7) { -%>
  - "<% safeTag7 %>"
<%* } -%>
<%* if (safeTag8) { -%>
  - "<% safeTag8 %>"
<%* } -%>
<%* if (safeTag9) { -%>
  - "<% safeTag9 %>"
<%* } -%>
<%* if (safeTag10) { -%>
  - "<% safeTag10 %>"
<%* } -%>
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