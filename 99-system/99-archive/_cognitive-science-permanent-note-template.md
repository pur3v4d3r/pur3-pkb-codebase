<%*
/* ---------------------------------------------------------------
   MASTER COGNITIVE-SCIENCE PERMANENT NOTE TEMPLATE
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
    "[[educational-psychology-perm-moc]]",
];
	  // --- TAXONOMY ARRAYS (Derived from Tag Taxonomy File) ---
	  // GROUP A: High-Level Domains & Dimensions (For Tags 01 & 02)
const groupA_Tags = [
	  // Cross-Cutting Concepts (High Level)
    "concept/atomic-notes", "concept/emergence", "concept/serendipity", "concept/networked-thought", "concept/knowledge-synthesis",
    "concept/external-cognition", "concept/transfer", "concept/automaticity", "concept/flow-state", "concept/cognitive-bias",
    "concept/mental-representation", "concept/chunking", "concept/distributed-practice", "concept/retrieval-practice", "concept/elaboration",
    "concept/instruction-following", "concept/in-context-learning", "concept/prompt-chaining", "concept/task-decomposition",
	  // Psychology & Cognitive
    "cognitive-science", "critical-thinking", "self-regulation", "learning-theory", "self-improvement",
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
	  // GROUP B: Sub-Domains & Categories 
const groupB_Tags = [
	  // Psychology & Cognitive
    "cognitive-science/metacognition", "cognitive-science/memory", "cognitive-science/attention", 
    "cognitive-science/cognitive-load", "cognitive-science/executive-function", "cognitive-science/reasoning",
    "critical-thinking/analysis", "critical-thinking/logic", "critical-thinking/evaluation", "critical-thinking/synthesis", "critical-thinking/problem-solving",
    "self-regulation/theory", "self-regulation/motivation", "self-regulation/goal-setting", "self-regulation/self-control", "self-regulation/emotional", "self-regulation/behavioral",
    "learning-theory/andragogy", "learning-theory/pedagogy", "learning-theory/heutagogy", "learning-theory/constructivism", "learning-theory/cognitive-apprenticeship",
    "self-improvement/skill-development", "self-improvement/mental-models", "self-improvement/productivity", "self-improvement/reflective-practice", "self-improvement/growth-mindset",
];
	  // GROUP C: Granular Concepts & Leaf Nodes 
const groupC_Tags = [
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
	  // --- Productivity ---
    "productivity/gtd/capture", "productivity/gtd/clarify", "productivity/gtd/organize", "productivity/gtd/reflect", "productivity/gtd/engage",
    "productivity/para/projects", "productivity/para/areas", "productivity/para/resources", "productivity/para/archives",
    "productivity/time-management/scheduling", "productivity/time-management/batching", "productivity/time-management/blocking",
    "productivity/task-management/todos", "productivity/task-management/projects", "productivity/task-management/workflows",
	  // --- Knowledge Work Practices ---
    "knowledge-work/reading/active-reading", "knowledge-work/reading/annotation", "knowledge-work/reading/speed-reading", "knowledge-work/reading/comprehension",
    "knowledge-work/research/literature-review", "knowledge-work/research/source-evaluation", "knowledge-work/research/synthesis", "knowledge-work/research/citation",
    "knowledge-work/writing/drafting", "knowledge-work/writing/editing", "knowledge-work/writing/argumentation", "knowledge-work/writing/publishing",
    "knowledge-work/thinking/analysis", "knowledge-work/thinking/synthesis", "knowledge-work/thinking/reflection", "knowledge-work/thinking/ideation",
    "knowledge-work/learning/study-methods", "knowledge-work/learning/retention", "knowledge-work/learning/transfer", "knowledge-work/learning/mastery",
	  // --- Knowledge Workflows ---
    "knowledge-workflow/capture/inbox", "knowledge-workflow/capture/quick-capture", "knowledge-workflow/capture/voice-notes", "knowledge-workflow/capture/highlights",
    "knowledge-workflow/processing/triage", "knowledge-workflow/processing/elaboration", "knowledge-workflow/processing/linking", "knowledge-workflow/processing/tagging",
    "knowledge-workflow/synthesis/integration", "knowledge-workflow/synthesis/connection", "knowledge-workflow/synthesis/emergence",
    "knowledge-workflow/output/writing", "knowledge-workflow/output/publishing", "knowledge-workflow/output/sharing", "knowledge-workflow/output/teaching",
    "knowledge-workflow/review/daily-review", "knowledge-workflow/review/weekly-review", "knowledge-workflow/review/monthly-review", "knowledge-workflow/review/spaced-repetition",
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
// 1. Prepare Display Arrays (What you SEE vs What you GET)
// We sort the tags alphabetically first so related items group together in the UI
const sortedA = groupA_Tags.sort();
const sortedB = groupB_Tags.sort();
const sortedC = groupC_Tags.sort();
const groupA_Display = formatTagsForDisplay(sortedA);
const groupB_Display = formatTagsForDisplay(sortedB);
const groupC_Display = formatTagsForDisplay(sortedC);
// 2. Text Prompts
const title = await tp.system.prompt("Enter Note Title (Concept Name):");
const alias1 = await tp.system.prompt("Enter Alias 1 (Press Enter to skip):");
const alias2 = await tp.system.prompt("Enter Alias 2 (Press Enter to skip):");
// 3. Metadata Suggesters
const type = await tp.system.suggester(typeList, typeList, false, "Select Note TYPE:");
const source = await tp.system.suggester(sourceList, sourceList, false, "Select SOURCE / ORIGIN:");
const linkUp = await tp.system.suggester(linkUpList, linkUpList, false, "Select LINK-UP MOC:");
// 5. Tag Suggesters (Hierarchical Selection)
// Syntax: await tp.system.suggester(DISPLAY_LIST, REAL_VALUE_LIST, throw_on_cancel, placeholder)
// Tag Set-01: High Level Domains (Group A)
const tag1 = await tp.system.suggester(groupA_Display, sortedA, false, "Select Tag 01:");
const tag2 = await tp.system.suggester(groupA_Display, sortedA, false, "Select Tag 02:");
const tag3 = await tp.system.suggester(groupA_Display, sortedA, false, "Select Tag 03:");
// Tag Set-02: Sub-Domain (Group B)
const tag4 = await tp.system.suggester(groupB_Display, sortedB, false, "Select Tag 04:");
const tag5 = await tp.system.suggester(groupB_Display, sortedB, false, "Select Tag 05:");
const tag6 = await tp.system.suggester(groupB_Display, sortedB, false, "Select Tag 06:");
const tag7 = await tp.system.suggester(groupC_Display, sortedC, false, "Select Tag 07:");
// Tag Set-03: Granular Concepts (Group C)
// We use the Display list for the UI, but the code returns the Original Tag from the sorted list
const tag8 = await tp.system.suggester(groupC_Display, sortedC, false, "Select Tag 08:");
// 6. Date Calculations
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
  - "[[Cognitive Processes]]"
  - "[[Cognitive Psychology]]"
  - "[[Cognitive Science]]"
  - "[[Cognitive Theory]]"
  - "[[Epistemic Cognition]]"
  - "[[Extended Mind]]"
  - "[[Long-Term Memory]]"
  - "[[Metacognition]]"
  - "[[Neuroplasticity]]"
  - "[[Schemas]]"
  - "[[Self Directed Learning]]"
  - "[[Self-Regulation-Theory]]"
  - "[[Self-Determination Theory]]"
  - "[[Socratic Method]]"

---

# <% title %>

> [!definition]
> - **Key-Term**:: [[<% title %>]]
> - [**Definition**:: ]

## Foundational Understanding
[Your initial understanding of this concept]

## Key Principles

## Related Concepts

- `[[Concept 1]]`
- `[[Concept 2]]`

## Practical Applications
> -

## Evolution Log
> 1. 
### <% dateNow %> - Initial Creation
[Context: Where you first encountered this concept]

---

## 📚 Sources
	
- 
	
- 
	
- 
	
- 
	
- 
	
- 
	
----
---

----