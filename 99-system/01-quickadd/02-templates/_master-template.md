<%*
// 1. NOTE TYPES (For 'type' property - matches "type/" tags)
const typeList = [
 "analysis",
 "claude-project",
 "concept",
 "definition",
 "framework",
 "gemini-gem",
 "guide",
 "permanent-note",
 "prompt",
 "reference",
 "report",
 "review",
 "technique",
 "theory",
 "tutorial"
];
// 2. SOURCE ORIGINS
const sourceList = [
 "claude-opus",
 "claude-sonnet",
 "gemini-flash",
 "gemini-pro",
 "coder-llm",
 "gpt-oss",
 "local-llm",
 "original",
 "report",
 "documentation",
 "video",
 "GitHub-Repo"
];
// 3. LINK-UP MOCs (Your Primary Domain Hubs)
const linkUpList = [
 "[[artificial-intelligence-moc]]",
 "[[cognitive-science-moc]]",
 "[[cosmology-moc]]",
 "[[educational-psychology-moc]]",
 "[[learning-theory-moc]]",
 "[[neuroscience-moc]]",
 "[[pkb-&-pkm-moc]]",
 "[[practical-philosophy-moc]]",
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
const priorityList = [
 "low",
 "medium",
 "high",
 "urgent"
];
// GROUP-[B]-TAGS-[STATUS]
const groupB_Tags = [
 "status/archived",
 "status/complete",
 "status/deprecated",
 "status/experimental",
 "status/in-progress",
 "status/not-read",
 "status/proven",
 "status/read",
 "status/review",
 "status/under-revision"
];
// 5. STATUS LIST (Extracted from groupB_Tags)
const statusList = groupB_Tags.map(tag => tag.replace("status/", ""));
// GROUP-[A]-TAGS-[DOMAIN]
const groupA_Tags = [
 "advanced-prompting/agents",
 "advanced-prompting/chain-systems",
 "advanced-prompting/multi-modal",
 "advanced-prompting/rag",
 "artificial-intelligence",
 "attention",
 "automation",
 "behavioral-science",
 "cognitive-development",
 "cognitive-enhancement",
 "cognitive-load-management",
 "cognitive-neuroscience",
 "cognitive-psychology",
 "cognitive-science",
 "cognitive-training",
 "context-management/memory",
 "context-management/window",
 "cosmology",
 "creative-thinking",
 "critical-thinking",
 "dataview",
 "dataview-queries",
 "dataviewjs",
 "developmental-cognition",
 "educational-applications",
 "educational-psychology",
 "expertise-development",
 "information-architecture",
 "informational-design-pkm",
 "instructional-design",
 "javascript",
 "knowledge-work",
 "knowledge-workflow",
 "learning-optimization",
 "learning-processes",
 "learning-science",
 "learning-theory",
 "meta-bind",
 "metacognitive-pkm",
 "neuroscience",
 "obsidian",
 "obsidian/advanced",
 "obsidian/plugins",
 "pkb",
 "pkb/architecture",
 "pkb/design",
 "pkm",
 "pkm/principles",
 "pkm/research",
 "pkm/theory",
 "pkm/workflow",
 "planning",
 "productivity",
 "productivity/task-management",
 "productivity/time-management",
 "prompt-engineering",
 "prompt-engineering/theory",
 "prompt-pattern/constraint",
 "prompt-pattern/context",
 "prompt-pattern/exemplar",
 "prompt-pattern/format",
 "prompt-pattern/framework",
 "prompt-pattern/instruction",
 "prompt-pattern/persona",
 "prompt-pattern/scaffold",
 "prompt-pattern/template",
 "prompting-technique/chain-of-thought",
 "prompting-technique/few-shot",
 "prompting-technique/meta-prompting",
 "prompting-technique/react",
 "prompting-technique/reasoning",
 "prompting-technique/reflection",
 "prompting-technique/zero-shot",
 "psychology",
 "quick-capture",
 "quickadd",
 "quickadd-macros",
 "scripting",
 "self-directed-learning",
 "self-improvement",
 "self-regulated-learning",
 "self-regulation",
 "skill-acquisition",
 "smart-connections",
 "spaced-repetition",
 "tasks-plugin",
 "template-automation",
 "templater",
 "templater-scripts",
 "vault-architecture",
 "working-memory"
];
/* ═══════════════════════════════════════════════════════════════════════
 HELPER FUNCTION: PRETTY PRINT TAGS WITH ICONS
 ═══════════════════════════════════════════════════════════════════════ */
function formatTagsForDisplay(tags) {
 return tags.map(tag => {
  let icon = "🔹"; // Default bullet
  // Assign Icons based on Domain Keywords (Prioritize Specificity)
  if (tag.startsWith("type/")) icon = "📑";
  else if (tag.startsWith("status/")) icon = "🚦";
  else if (tag.startsWith("context/")) icon = "🌐";
  else if (tag.startsWith("source/")) icon = "📚";
  else if (tag.startsWith("maturity/")) icon = "🍷";
  else if (tag.startsWith("mode/")) icon = "⚙️";
  else if (tag.startsWith("validation/") || tag.startsWith("complexity/")) icon = "📏";
  else if (tag.startsWith("nature/")) icon = "🌿";
  else if (tag.startsWith("model/")) icon = "🤖";
  else if (tag.includes("obsidian") || tag.includes("dataview") || tag.includes("plugin")) icon = "💎";
  else if (tag.includes("pkm") || tag.includes("pkb") || tag.includes("zettelkasten") || tag.includes("para")) icon = "🧠";
  else if (tag.includes("workflow") || tag.includes("system") || tag.includes("architecture")) icon = "🔄";
  else if (tag.includes("information-architecture") || tag.includes("taxonomy")) icon = "🗂️";
  else if (tag.includes("neuro") || tag.includes("brain")) icon = "🧬";
  else if (tag.includes("memory") || tag.includes("encoding") || tag.includes("recall")) icon = "💾";
  else if (tag.includes("learning") || tag.includes("education") || tag.includes("student") || tag.includes("andragogy")) icon = "🎓";
  else if (tag.includes("attention") || tag.includes("focus")) icon = "🎯";
  else if (tag.includes("reasoning") || tag.includes("logic") || tag.includes("thinking") || tag.includes("decision")) icon = "💡";
  else if (tag.includes("cognitive") || tag.includes("psychology") || tag.includes("behavior")) icon = "🧩";
  else if (tag.includes("regulation") || tag.includes("motivation") || tag.includes("self")) icon = "💪";
  else if (tag.includes("prompt") || tag.includes("chain-of-thought")) icon = "💬";
  else if (tag.includes("llm") || tag.includes("gpt") || tag.includes("claude") || tag.includes("gemini") || tag.includes("artificial")) icon = "🤖";
  else if (tag.includes("agent") || tag.includes("rag")) icon = "🕵️";
  else if (tag.includes("safety") || tag.includes("bias")) icon = "🛡️";
  else if (tag.includes("cosmology") || tag.includes("universe")) icon = "🌌";
  else if (tag.includes("concept/")) icon = "💡";
  else if (tag.includes("research") || tag.includes("analysis") || tag.includes("study")) icon = "🔬";
  let cleanText = tag.split("/").join(" › ");
  return `${icon} ${cleanText}`;
 });
}
/* ═══════════════════════════════════════════════════════════════════════
 INPUT SYSTEM: USER PROMPTS & SUGGESTERS
 ═══════════════════════════════════════════════════════════════════════ */
const title = await tp.system.prompt("Enter Title for YAML:");
if (title == null) { return; }
const alias1 = await tp.system.prompt("Enter Alias 1 (Press Enter to skip):");
const alias2 = await tp.system.prompt("Enter Alias 2 (Press Enter to skip):");
const type = await tp.system.suggester(typeList, typeList, false, "Select Note TYPE:");
const source = await tp.system.suggester(sourceList, sourceList, false, "Select SOURCE / ORIGIN:");
const linkUp = await tp.system.suggester(linkUpList, linkUpList, false, "Select LINK-UP MOC:");
const maturity = await tp.system.suggester(maturityLevels, maturityLevels, false, "Select Maturity Level:");
const confidence = await tp.system.suggester(confidenceLevels, confidenceLevels, false, "Select Confidence Level:");
const status = await tp.system.suggester(statusList, statusList, false, "Select Status:");
const priority = await tp.system.suggester(priorityList, priorityList, false, "Select Priority:");
const groupA_Display = formatTagsForDisplay(groupA_Tags.sort());
const groupB_Display = formatTagsForDisplay(groupB_Tags.sort());
const tag1 = await tp.system.suggester(groupA_Display, groupA_Tags.sort(), false, "TAG 1");
const tag2 = await tp.system.suggester(groupA_Display, groupA_Tags.sort(), false, "TAG 2");
const tag3 = await tp.system.suggester(groupA_Display, groupA_Tags.sort(), false, "TAG 3");
const tag4 = await tp.system.suggester(groupA_Display, groupA_Tags.sort(), false, "TAG 4");
const tag5 = await tp.system.suggester(groupA_Display, groupA_Tags.sort(), false, "TAG 5");
const tag6 = await tp.system.suggester(groupA_Display, groupA_Tags.sort(), false, "TAG 6");
const dateNow = tp.date.now("YYYY-MM-DD");
const timeNow = tp.date.now("HH:mm:ss");
const year = tp.date.now("YYYY");
const id = tp.date.now("YYYYMMDDHHmmss");
let nextReview = tp.date.now("YYYY-MM-DD", 7);
_%>
---
id: "<% id %>"
type: "<% type %>"
source: "<% source %>"
status: "<% status %>"
confidence: "<% confidence %>"
maturity: "<% maturity %>"
priority: "<% priority %>"
next-review: "<% nextReview %>"
review-count: 0
last-reviewed:
review-interval: 7
created: "<% dateNow %>T<% timeNow %>"
modified: "<% dateNow %>T<% timeNow %>"
week: "[[<% tp.date.now("gggg-[W]WW") %>]]"
month: "<% tp.date.now("YYYY-MM") %>"
quarter: "<% tp.date.now("YYYY-[Q]Q") %>"
year: "<% year %>"
link-up:
 - "<% linkUp %>"
link-related:
 - "[[<% dateNow %>|Daily-Note]]"
tags:
 - "type/<% type %>"
 - "source/<% source %>"
 - "maturity/<% maturity %>"
 - "confidence/<% confidence %>"
 - "status/<% status %>"
 - "priority/<% priority %>"
 - "year/<% year %>"
 - "<% tag1 %>"
 - "<% tag2 %>"
 - "<% tag3 %>"
 - "<% tag4 %>"
 - "<% tag5 %>"
 - "<% tag6 %>"
aliases:
 - "<% alias1 %>"
 - "<% alias2 %>"
 - "<% title %>"
title: "<% title %>"
---
### 📖 Extracted Definitions From Cognitive Science
```dataviewjs
try {
 // Get the current file
 const currentPage = dv.current();
 // Load the content of the current file
 const content = await dv.io.load(currentPage.file.path);
 // Storage for definitions in current file
 let allDefinitions = [];
 // Extract bracketed inline fields from current file content
 const bracketedFieldRegex = /\[\*\*([^*]+?)\*\*::\s*([^\]]+?)\]/g;
 let match;
 while ((match = bracketedFieldRegex.exec(content)) !== null) {
  allDefinitions.push({
   key: match[1].trim(), // This is the clean term without ** markdown
   value: match[2].trim()
  });
 }
 // Display results
 if (allDefinitions.length > 0) {
  dv.header(3, `📚 Definitions in Current File (${allDefinitions.length} total)`);
  // Group by first letter (using the clean key)
  const grouped = {};
  allDefinitions.forEach(d => {
   const firstLetter = d.key[0].toUpperCase();
   if (!grouped[firstLetter]) grouped[firstLetter] = [];
   grouped[firstLetter].push(d);
  });
  // Sort letters alphabetically
  const sortedLetters = Object.keys(grouped).sort();
  // Display grouped results
  for (let letter of sortedLetters) {
   dv.header(4, `${letter} (${grouped[letter].length} terms)`);
   dv.table(
    ["🔑 Term", "📝 Definition"],
    grouped[letter].map(d => [
     `**${d.key}**`,
     d.value
    ])
   );
   dv.paragraph(""); // Add spacing between groups
  }
 } else {
  dv.paragraph(`*No bracketed inline fields found in current file.*`);
 }
} catch (error) {
 console.error("Error in definitions script:", error);
 dv.paragraph("*Error loading definitions. Check console for details.*");
}
```
---





# Foundational Understanding
> [!definition] # Definition
> [**Note Title**:: [[**<% title %>**]]]
> [**Prompt Used**:: ]
> ##### [✅`= dateformat(this.file.ctime, "MMMM dd, yyyy")` - Initial Creation]


**{{PASTE HERE}}**



> [!warning] ### 📅 Review Intelligence
> **Next Review**: `= this.next-review` | **Review Count**: `= this.review-count`
> **Review Status**: `= choice(this.next-review < date(today), "🔴 OVERDUE", choice(this.next-review = date(today), "🟡 Due Today", choice(dateformat(this.next-review, "yyyy-MM-dd") <= dateformat(date(today) + dur(7 days), "yyyy-MM-dd"), "🟢 This Week", "⚪ Scheduled")))`
> **Days Until Review**: `= choice(this.next-review, (this.next-review - date(today)).days + " days", "Not scheduled")`
> [!abstract] ### 🏷️ Tag Intelligence
> **Tag Count**: `= length(this.tags)` | **Unique Domains**: `= length(filter(this.tags, (t) => contains(t, "/")))` hierarchical tags
> **Tag Density**: `= choice(length(this.tags) < 3, "⚠️Sparse", choice(length(this.tags) > 10, "📚Rich", "✅Balanced"))`
>




### Review Information
<%*
let intervalDays = 7;
let intervalText = "1 week";
if (maturity === "seedling") {
 intervalDays = 7;
 intervalText = "1 week";
} else if (maturity === "budding") {
 intervalDays = 14;
 intervalText = "2 weeks";
} else if (maturity === "developing") {
 intervalDays = 30;
 intervalText = "1 month";
} else if (maturity === "evergreen") {
 intervalDays = 90;
 intervalText = "3 months";
}
if (confidence === "^speculative" || confidence === "^provisional") {
 intervalDays = Math.ceil(intervalDays / 2);
 intervalText = `${intervalDays} days`;
}
nextReview = tp.date.now("YYYY-MM-DD", intervalDays);
const prioritySymbol = (confidence === "^speculative" || confidence === "^provisional") ? "⏫" : "🔼";
_%>
## 📅 Review System
**Maturity Level**: `= this.maturity`  
**Confidence Level**: `= this.confidence`  
**Review Interval**: <% intervalText %>  
**Next Review**: <% nextReview %>
### Active Review Task
- [ ] Review [[<% title %>]] (<% maturity %> | <% confidence %>) 📅 <% nextReview %> <% prioritySymbol %> 🔁 every <% intervalText %> #review
```tasks
not done
description includes [[<% title %>]]
description includes Review
```

---
