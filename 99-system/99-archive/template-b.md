> [!important]
> This is the Template I want you to take the Note Body from (that has Dataview) this Template and use it as the foundation to the new template you will be creating.


`````
<%*
/* ---------------------------------------------------------------
   ENHANCED MASTER COGNITIVE-SCIENCE PERMANENT NOTE TEMPLATE
   Version: 2.0
   Enhancements: Status tracking, review system, query-ready fields
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
// 4. MATURITY LEVELS (NEW - For Progressive Development)
const maturityLevels = [
    "seedling",      // Initial capture
    "budding",       // Basic structure established
    "developing",    // Active refinement
    "evergreen",     // Mature, stable
    "needs-review"   // Flagged for revision
];
// 5. CONFIDENCE LEVELS (NEW - Epistemic Status)
const confidenceLevels = [
    "speculative",   // Hypothesis/early thinking
    "provisional",   // Needs verification
    "moderate",      // Reasonably confident
    "high",          // Well-supported
    "established"    // Academically verified
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
// GROUP B: Sub-Domains & Categories (For Tag 03)
const groupB_Tags = [
    // Psychology & Cognitive
    "cognitive-science/metacognition", "cognitive-science/memory", "cognitive-science/attention", 
    "cognitive-science/cognitive-load", "cognitive-science/executive-function", "cognitive-science/reasoning",
    "critical-thinking/analysis", "critical-thinking/logic", "critical-thinking/evaluation", "critical-thinking/synthesis", "critical-thinking/problem-solving",
    "self-regulation/theory", "self-regulation/motivation", "self-regulation/goal-setting", "self-regulation/self-control", "self-regulation/emotional", "self-regulation/behavioral",
    "learning-theory/andragogy", "learning-theory/pedagogy", "learning-theory/heutagogy", "learning-theory/constructivism", "learning-theory/cognitive-apprenticeship",
    "self-improvement/skill-development", "self-improvement/mental-models", "self-improvement/productivity", "self-improvement/reflective-practice", "self-improvement/growth-mindset",
];
// GROUP C: Granular Concepts & Leaf Nodes (For Tags 04, 05, 06)
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
    // --- Knowledge Workflow ---
    "knowledge-workflow/capture/note-taking", "knowledge-workflow/capture/bookmarking", "knowledge-workflow/capture/clipping", "knowledge-workflow/capture/dictation",
    "knowledge-workflow/process/organizing", "knowledge-workflow/process/tagging", "knowledge-workflow/process/linking", "knowledge-workflow/process/refining",
    "knowledge-workflow/output/writing", "knowledge-workflow/output/publishing", "knowledge-workflow/output/sharing", "knowledge-workflow/output/teaching",
    "knowledge-workflow/review/daily-review", "knowledge-workflow/review/weekly-review", "knowledge-workflow/review/monthly-review", "knowledge-workflow/review/spaced-repetition",
];
// --- HELPER FUNCTION: PRETTY PRINT TAGS ---
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
        let cleanText = tag.split("/").join("  ›  ");
        return `${icon} ${cleanText}`;
    });
}
// --- INPUT SYSTEM ---
// 1. Prepare Display Arrays
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
// 4. NEW: Status Tracking Fields
const maturity = await tp.system.suggester(maturityLevels, maturityLevels, false, "Select Maturity Level:");
const confidence = await tp.system.suggester(confidenceLevels, confidenceLevels, false, "Select Confidence Level:");
// 5. Tag Suggesters (Hierarchical Selection)
const tag1 = await tp.system.suggester(groupA_Display, sortedA, false, "Select Tag 01 (Domain - Group A):");
const tag2 = await tp.system.suggester(groupA_Display, sortedA, false, "Select Tag 02 (Domain - Group A):");
const tag3 = await tp.system.suggester(groupB_Display, sortedB, false, "Select Tag 03 (Sub-Domain - Group B):");
const tag4 = await tp.system.suggester(groupC_Display, sortedC, false, "Select Tag 04 (Granular - Group C):");
const tag5 = await tp.system.suggester(groupC_Display, sortedC, false, "Select Tag 05 (Granular - Group C):");
const tag6 = await tp.system.suggester(groupC_Display, sortedC, false, "Select Tag 06 (Granular - Group C):");
const tag7 = await tp.system.suggester(groupC_Display, sortedC, false, "Select Tag 07 (Granular - Group C):");
const tag8 = await tp.system.suggester(groupC_Display, sortedC, false, "Select Tag 08 (Granular - Group C):");
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

> [!definition]
> - **Key-Term**:: [[<% title %>]]
> - **Definition**:: <% tp.file.cursor(1) %>
> - **Status**:: 🌱 `= this.maturity` | Confidence: `= this.confidence`

## 📊 Note Metadata Dashboard

**Development Status**: `= this.maturity`  
**Epistemic Confidence**: `= this.confidence`  
**Next Review**: `= this.next-review`  
**Review Count**: `= this.review-count`  
**Created**: `= this.created`  
**Last Modified**: `= this.modified`

---

## Foundational Understanding

<% tp.file.cursor(2) %>

## Key Principles

1. 
2. 
3. 

## Related Concepts

```dataview
TABLE type, maturity, confidence
FROM [[]]
WHERE type = "concept" OR type = "principle"
SORT maturity DESC
LIMIT 10
```

### Direct Connections
- [[Concept 1]]
- [[Concept 2]]
- [[Concept 3]]

## Practical Applications

> [!example] Application 1
> Description: <% tp.file.cursor(3) %>

> [!example] Application 2
> Description: 

## Questions & Tensions

> [!question] Open Question 1
> 

> [!question] Open Question 2
> 

## Evolution Log

> [!timeline] Development History
> `= this.review-count` total reviews

### <% dateNow %> - Initial Creation
**Context**: <% tp.file.cursor(4) %>  
**Maturity**: `= this.maturity`  
**Confidence**: `= this.confidence`

---

## 📚 Sources & References

```dataview
TABLE 
    source AS "Source Type",
    created AS "Date Added"
FROM [[]]
WHERE source
SORT created DESC
```

### Primary Sources
- 

### Supporting Material
- 

### To Explore
- [ ] 

---

## 🔗 Backlinks & Connections

```dataview
TABLE 
    type AS "Type",
    maturity AS "Maturity",
    created AS "Created"
FROM [[#]]
SORT created DESC
LIMIT 15
```

---

## 📈 Review System

> [!important] Review Schedule
> - **Next Review**: `= this.next-review`
> - **Review Frequency**: Based on maturity level
>   - Seedling: Weekly
>   - Budding: Bi-weekly
>   - Developing: Monthly
>   - Evergreen: Quarterly

**Review Checklist**:
- [ ] Definition still accurate?
- [ ] New connections identified?
- [ ] Applications validated?
- [ ] Sources still relevant?
- [ ] Maturity level appropriate?

---

## 🏷️ Tags & Classification

Primary Tags: `= this.tags`  
Type: `= this.type`  
Source: `= this.source`

----
````