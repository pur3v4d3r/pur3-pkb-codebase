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
// GROUP-[B]-TAGS-[STATUS] - MOVED ABOVE WHERE IT'S USED
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
// 5. STATUS LIST (Extracted from groupB_Tags) - NOW WORKS BECAUSE groupB_Tags IS DECLARED ABOVE
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
let nextReview = tp.date.now("YYYY-MM-DD", 7); // CHANGED FROM const TO let
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

---

# Foundational Understanding
> [!definition] # Definition
> [**<% title %>**: ]
>
> ##### [✅`= dateformat(this.file.ctime, "MMMM dd, yyyy")` - Initial Creation]


**{{PASTE HERE}}**


>[! ] ### 🔗Backlinks & Connections


 ```dataview
 TABLE
  type AS "Type",
  maturity AS "Maturity",
  created AS "Created"
 FROM [[#]]
 SORT created DESC
 LIMIT 15
```


> [!warning] ### 📅 Review Intelligence
> **Next Review**: `= this.next-review` | **Review Count**: `= this.review-count`
> **Review Status**: `= choice(this.next-review < date(today), "🔴 OVERDUE", choice(this.next-review = date(today), "🟡 Due Today", choice(dateformat(this.next-review, "yyyy-MM-dd") <= dateformat(date(today) + dur(7 days), "yyyy-MM-dd"), "🟢 This Week", "⚪ Scheduled")))`
> **Days Until Review**: `= choice(this.next-review, (this.next-review - date(today)).days + " days", "Not scheduled")`
> [!abstract] ### 🏷️ Tag Intelligence
> **Tag Count**: `= length(this.tags)` | **Unique Domains**: `= length(filter(this.tags, (t) => contains(t, "/")))` hierarchical tags
> **Tag Density**: `= choice(length(this.tags) < 3, "⚠️Sparse", choice(length(this.tags) > 10, "📚Rich", "✅Balanced"))`
>


### 📖 Extracted Definitions From Cognitive Science
```dataviewjs
try {
 const folderPath = "03-notes/01_permanent-notes/01_cognitive-development";
 const pages = dv.pages(`"$"`);
 let allDefinitions = [];
 for (let page of pages) {
 try {
  const content = await dv.io.load(page.file.path);
  const bracketedFieldRegex = /\[\*\*([^*]+?)\*\*::\s*([^\]]+?)\]/g;
  let match;
  while ((match = bracketedFieldRegex.exec(content)) !== null) {
  allDefinitions.push({
   source: page.file.link,
   key: match[1].trim(),
   value: match[2].trim()
  });
  }
 } catch (e) {
  console.warn(`Error processing file ${page.file.path}:`, e);
  continue;
 }
 }
 if (allDefinitions.length > 0) {
 dv.header(3, `📚 All Definitions Across $ (${allDefinitions.length} total)`);
 const grouped = {};
 allDefinitions.forEach(d => {
  const firstLetter = d.key[0].toUpperCase();
  if (!grouped[firstLetter]) grouped[firstLetter] = [];
  grouped[firstLetter].push(d);
 });
 const sortedLetters = Object.keys(grouped).sort();
 for (let letter of sortedLetters) {
  dv.header(4, `${letter} (${grouped[letter].length} terms)`);
  dv.table(
  ["📄 Source", "🔑 Term", "📝 Definition"],
  grouped[letter].map(d => [
   d.source,
   `**${d.key}**`,
   d.value
  ])
  );
  dv.paragraph("");
 }
 } else {
 dv.paragraph(`*No bracketed inline fields found in "$".*`);
 }
} catch (error) {
 console.error("Error in definitions aggregation script:", error);
 dv.paragraph("*Error loading definitions. Check console for details.*");
}
```

---
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
nextReview = tp.date.now("YYYY-MM-DD", intervalDays); // CHANGED FROM const TO assignment
const prioritySymbol = (confidence === "^speculative" || confidence === "^provisional") ? "⏫" : "🔼";
// Auto-generate Tasks integration
const taskDate = nextReview;
const taskPriority = prioritySymbol;
const taskInterval = intervalText;
_%>
## 📅 Review System
**Maturity Level**: `= this.maturity`  
**Confidence Level**: `= this.confidence`  
**Review Interval**: <% intervalText %>  
**Next Review**: <% nextReview %>
### 🎯 Automated Review Task
- [ ] 📚 Review [[<% title %>]] (<% maturity %> | <% confidence %>) 📅 <% taskDate %> <% taskPriority %> 🔁 every <% taskInterval %> #review/<% maturity %> #confidence/<% confidence %>
### 📊 Review Dashboard
```dataview
TASK
FROM [[<% title %>]]
WHERE contains(text, "Review")
SORT due ASC
```
### 🔄 Related Reviews
```dataview
TABLE 
 maturity AS "Maturity",
 confidence AS "Confidence",
 next-review AS "Next Review"
FROM #review
WHERE maturity = "<% maturity %>"
SORT next-review ASC
```
### 📈 Review History
```dataviewjs
// This will show review completion history when tracked
dv.paragraph("📊 Review completion history will appear here once tasks are completed");
```
### ⚙️ Auto-Update Script
```javascript
// Add this to your daily note template or run manually
// Updates review dates based on completion and maturity
/*
const note = app.workspace.getActiveFile();
const metadata = app.metadataCache.getFileCache(note);
if (metadata.frontmatter && metadata.frontmatter["review-count"] !== undefined) {
  const currentCount = metadata.frontmatter["review-count"];
  const newCount = currentCount + 1;
  // Update review count and last reviewed date
  // This requires a plugin like MetaEdit or custom script
}
*/
```


---

## 🤖 Smart Review Automation
### 📋 Tasks Plugin Integration
**Auto-generated task for Tasks plugin:**

```tasks
not done
description includes [[<% title %>]]
description includes Review
group by due
```

### 📅 Calendar Integration

**Next review date:** `<% taskDate %>`  
**Calendar tag:** `#review/<% maturity %>`  
**Priority indicator:** `<% taskPriority %>`

### 🔄 Recurring Task Setup

To make this a recurring task automatically:
1. Complete the review task
2. The task will automatically reschedule for `<% taskInterval %>` later
3. Review count will increment automatically (requires MetaEdit plugin)

### 📊 Dataview Queries for Review Management
#### All Notes Due This Week
```dataview
TABLE 
 maturity AS "Maturity",
 confidence AS "Confidence",
 next-review AS "Due Date"
FROM #review 
WHERE next-review <= date(today) + dur(7 days)
SORT next-review ASC
```

#### Overdue Reviews
```dataview
TABLE 
 maturity AS "Maturity",
 confidence AS "Confidence",
 next-review AS "Overdue Since"
FROM #review 
WHERE next-review < date(today)
SORT next-review ASC
```

#### Review Statistics
```dataviewjs
const allReviews = dv.pages("#review");
const maturityStats = {};
const confidenceStats = {};
allReviews.forEach(page => {
  const maturity = page.maturity || "unknown";
  const confidence = page.confidence || "unknown";
  maturityStats[maturity] = (maturityStats[maturity] || 0) + 1;
  confidenceStats[confidence] = (confidenceStats[confidence] || 0) + 1;
});
dv.header(3, "📊 Review Statistics");
dv.paragraph(`**Total Reviews:** ${allReviews.length}`);
dv.header(4, "Maturity Distribution");
dv.table(["Maturity Level", "Count"], 
  Object.entries(maturityStats).map(([level, count]) => [level, count])
);
dv.header(4, "Confidence Distribution");
dv.table(["Confidence Level", "Count"], 
  Object.entries(confidenceStats).map(([level, count]) => [level, count])
);
```




----