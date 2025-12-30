<%*
/* ═══════════════════════════════════════════════════════════════════════
 🧠 intelligent-permanent-note-template-v3.0
 Advanced Context-Aware Knowledge Capture System
 ═══════════════════════════════════════════════════════════════════════ */
// ─────────────────────────────────────────────────────────────────────────
// 🛠 CONFIGURATION & SETUP
// ─────────────────────────────────────────────────────────────────────────
const DEFAULT_TYPES = [
 "concept", "framework", "methodology", "principle", 
 "mental-model", "theory", "technique", "strategy",
 "analysis", "case-study", "comparison", "definition"
];
const SOURCE_TYPES = [
 "book", "article", "paper", "video", "course", 
 "conversation", "experience", "original-synthesis",
 "community", "documentation", "report"
];
const MATURITY_LEVELS = [
 { value: "seedling", label: "🌱 Seedling - New idea, minimal development" },
 { value: "developing", label: "🌿 Developing - Taking shape, needs refinement" },
 { value: "budding", label: "🪴 Budding - Well-formed, some connections" },
 { value: "evergreen", label: "🌳 Evergreen - Mature, stable, well-connected" }
];
const CONFIDENCE_LEVELS = [
 { value: "speculative", label: "🔮 Speculative - Hypothesis, untested" },
 { value: "provisional", label: "🧪 Provisional - Some evidence, needs validation" },
 { value: "moderate", label: "📊 Moderate - Good evidence, some limitations" },
 { value: "established", label: "✅ Established - Strong evidence, widely accepted" },
 { value: "high", label: "🏆 High - Definitive, foundational knowledge" }
];
const CONTEXT_TYPES = [
 "research", "professional", "personal", "teaching", 
 "reference", "meta", "applied", "theoretical"
];
const REVIEW_SCHEDULES = {
 "seedling": 3,
 "developing": 7,
 "budding": 14,
 "evergreen": 30
};
const DOMAIN_KNOWLEDGE = {
 "pkm": {
  tags: ["pkm", "pkb", "obsidian", "note-taking", "knowledge-management"],
  subdomains: ["zettelkasten", "digital-garden", "moc", "atomic-notes"],
  mocPatterns: ["pkb-&-pkm-moc", "learning-theory-moc"]
 },
 "cognitive-science": {
  tags: ["cognitive-science", "psychology", "neuroscience", "learning-theory"],
  subdomains: ["memory", "attention", "executive-function", "learning"],
  mocPatterns: ["cognitive-science-moc", "learning-theory-moc"]
 },
 "ai-ml": {
  tags: ["artificial-intelligence", "machine-learning", "llm", "prompt-engineering"],
  subdomains: ["transformers", "neural-networks", "nlp", "computer-vision"],
  mocPatterns: ["artificial-intelligence-moc", "prompt-engineering-moc"]
 },
 "education": {
  tags: ["education", "instructional-design", "pedagogy", "andragogy"],
  subdomains: ["curriculum", "assessment", "learning-objectives", "didactics"],
  mocPatterns: ["educational-psychology-moc"]
 }
};
// ─────────────────────────────────────────────────────────────────────────
// 🤖 INTELLIGENCE ENGINE
// ─────────────────────────────────────────────────────────────────────────
function analyzeContext(title, content = "") {
 const text = (title + " " + content).toLowerCase();
 const suggestions = {
  domains: [],
  tags: [],
  mocSuggestions: []
 };
 Object.entries(DOMAIN_KNOWLEDGE).forEach(([domain, config]) => {
  const keywords = [...config.tags, ...config.subdomains];
  if (keywords.some(keyword => text.includes(keyword))) {
   suggestions.domains.push(domain);
   suggestions.tags.push(...config.tags.slice(0, 3));
   suggestions.mocSuggestions.push(...config.mocPatterns);
  }
 });
 return suggestions;
}
function generateSmartTags(selectedDomain, noteType, context) {
 const tags = [`type/${noteType}`, `domain/${selectedDomain}`, `context/${context}`];
 if (DOMAIN_KNOWLEDGE[selectedDomain]) {
  tags.push(...DOMAIN_KNOWLEDGE[selectedDomain].tags.slice(0, 2));
  tags.push(`year/${tp.date.now("YYYY")}`);
 }
 return [...new Set(tags)];
}
function suggestMOCs(domains) {
 const mocSet = new Set();
 domains.forEach(domain => {
  if (DOMAIN_KNOWLEDGE[domain] && DOMAIN_KNOWLEDGE[domain].mocPatterns) {
   DOMAIN_KNOWLEDGE[domain].mocPatterns.forEach(moc => mocSet.add(moc));
  }
 });
 return Array.from(mocSet);
}
// ─────────────────────────────────────────────────────────────────────────
// 🎯 USER INTERACTION FLOW
// ─────────────────────────────────────────────────────────────────────────
const fileName = tp.file.title;
const title = await tp.system.prompt("📝 Note Title:", fileName.includes("Untitled") ? "" : fileName) || "Untitled Note";
if (!title) return;
const contextAnalysis = analyzeContext(title);
const suggestedDomains = contextAnalysis.domains.length > 0 ? contextAnalysis.domains : Object.keys(DOMAIN_KNOWLEDGE);
const noteType = await tp.system.suggester(
 DEFAULT_TYPES.map(t => `📝 ${t.charAt(0).toUpperCase() + t.slice(1)}`),
 DEFAULT_TYPES,
 false,
 "📋 Note Type:"
);
const source = await tp.system.suggester(
 SOURCE_TYPES.map(s => `📚 ${s.charAt(0).toUpperCase() + s.slice(1)}`),
 SOURCE_TYPES,
 false,
 "📖 Source Origin (Optional):"
);
const primaryDomain = await tp.system.suggester(
 suggestedDomains.map(d => `🌐 ${d.charAt(0).toUpperCase() + d.slice(1).replace('-', ' ')}`),
 suggestedDomains,
 false,
 "🌍 Primary Domain:"
);
const context = await tp.system.suggester(
 CONTEXT_TYPES.map(c => {
  const icons = {
   "research": "🔬", "professional": "💼", "personal": "👤",
   "teaching": "chalkboard", "reference": "📚", "meta": "⚙️",
   "applied": "⚡", "theoretical": "💭"
  };
  return `${icons[c] || "🏷️"} ${c.charAt(0).toUpperCase() + c.slice(1)}`;
 }),
 CONTEXT_TYPES,
 false,
 "🎯 Context:"
);
const maturityObj = await tp.system.suggester(
 MATURITY_LEVELS.map(m => m.label),
 MATURITY_LEVELS.map(m => m.value),
 false,
 "🌿 Maturity Level:"
);
const confidenceObj = await tp.system.suggester(
 CONFIDENCE_LEVELS.map(c => c.label),
 CONFIDENCE_LEVELS.map(c => c.value),
 false,
 "📊 Confidence Level:"
);
const smartTags = generateSmartTags(primaryDomain, noteType, context);
const additionalTags = await tp.system.prompt("🏷️ Additional Tags (comma-separated, optional):", "");
const suggestedMOCs = suggestMOCs([primaryDomain, ...contextAnalysis.domains]);
const linkUpChoice = await tp.system.suggester(
 suggestedMOCs.length > 0 ? 
  [...suggestedMOCs.map(m => `🔗 ${m}`), "➕ Other MOC", "❌ None"] : 
  ["➕ Select MOC", "❌ None"],
 suggestedMOCs.length > 0 ? 
  [...suggestedMOCs, "other", "none"] : 
  ["other", "none"],
 false,
 "枢纽 Link to MOC:"
);
let finalLinkUp = [];
if (linkUpChoice === "other") {
 const customMOC = await tp.system.prompt("Enter MOC link (e.g., [[my-moc]]):");
 if (customMOC) finalLinkUp.push(customMOC);
} else if (linkUpChoice !== "none") {
 finalLinkUp.push(`[[${linkUpChoice}]]`);
}
const alias1 = await tp.system.prompt("🔖 Alias 1 (Optional):", "");
const alias2 = await tp.system.prompt("🔖 Alias 2 (Optional):", "");
// ─────────────────────────────────────────────────────────────────────────
// 📊 METADATA CALCULATIONS
// ─────────────────────────────────────────────────────────────────────────
const dateNow = tp.date.now("YYYY-MM-DD");
const timeNow = tp.date.now("HH:mm:ss");
const year = tp.date.now("YYYY");
const id = tp.date.now("YYYYMMDDHHmmss");
const nextReviewDays = REVIEW_SCHEDULES[maturityObj] || 7;
const nextReview = tp.date.now("YYYY-MM-DD", nextReviewDays);
let allTags = [...smartTags];
if (additionalTags) {
 allTags = [...allTags, ...additionalTags.split(',').map(t => t.trim()).filter(t => t)];
}
// ─────────────────────────────────────────────────────────────────────────
// 📄 TEMPLATE RENDERING
// ─────────────────────────────────────────────────────────────────────────
_%>
---
<%* if (alias1 || alias2) { -%>
aliases:
<%* if (alias1) { -%>
 - "<% alias1 %>"
<%* } -%>
<%* if (alias2) { -%>
 - "<% alias2 %>"
<%* } -%>
<%* } -%>
tags:
<% allTags.forEach(tag => { -%>
 - "<% tag %>"
<% }); -%>
source: <% source ? `"${source}"` : '""' %>
id: "<% id %>"
created: "<% dateNow %>T<% timeNow %>"
modified: "<% dateNow %>T<% timeNow %>"
week: "[[<% tp.date.now("gggg-[W]WW") %>]]"
month: "[[<% tp.date.now("YYYY-MM") %>]]"
quarter: "[[<% tp.date.now("YYYY-[Q]Q") %>]]"
year: "[[<% year %>]]"
type: "<% noteType %>"
maturity: "<% maturityObj %>"
confidence: "<% confidenceObj %>"
next-review: "<% nextReview %>"
review-count: 0
link-count: 0
backlink-count: 0
<%* if (finalLinkUp.length > 0) { -%>
link-up:
<% finalLinkUp.forEach(link => { -%>
 - "<% link %>"
<% }); -%>
<%* } -%>
link-related:
 - "[[<% dateNow %>|Daily-Note]]"
---
# 📚 <% title %>
## 🎯 Overview
<%* if (source) { -%>
**Source:** <% source.charAt(0).toUpperCase() + source.slice(1) %>
<%* } -%>
## 🧠 Key Insights
## 📖 Detailed Explanation
## 🔗 Related Concepts
## 🛠️ Applications
## 📚 References
<%* if (source) { -%>
- Source: <% source %>
<%* } -%>
## 🔄 Connections
- **Link Up:** <% finalLinkUp.length > 0 ? finalLinkUp.join(', ') : 'None specified' %>
- **Related Notes:** [[<% dateNow %>|Daily-Note]]
## 📅 Review Schedule
- **Maturity:** <% maturityObj.charAt(0).toUpperCase() + maturityObj.slice(1) %> 
- **Confidence:** <% confidenceObj.charAt(0).toUpperCase() + confidenceObj.slice(1) %>
- **Next Review:** [[<% nextReview %>]]

---
