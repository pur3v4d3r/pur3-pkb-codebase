<%*
/* ═══════════════════════════════════════════════════════════════════════
  🧠 INTELLIGENT PERMANENT NOTE TEMPLATE v3.0
  Advanced Context-Aware Knowledge Capture System
  ═══════════════════════════════════════════════════════════════════════ */
// ─────────────────────────────────────────────────────────────────────────
// 🛠 CONFIGURATION & SETUP
// ─────────────────────────────────────────────────────────────────────────
// Smart defaults based on common patterns
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
  "seedling": 3,    // 3 days
  "developing": 7,  // 1 week
  "budding": 14,    // 2 weeks
  "evergreen": 30   // 1 month
};
// Domain knowledge bases for intelligent suggestions
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
/**
 * Analyze title/content to suggest domains and tags
 */
function analyzeContext(title, content = "") {
  const text = (title + " " + content).toLowerCase();
  const suggestions = {
    domains: [],
    tags: [],
    mocSuggestions: []
  };
  // Domain detection
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
/**
 * Generate smart tag suggestions based on selections
 */
function generateSmartTags(selectedDomain, noteType, context) {
  const tags = [`type/${noteType}`, `domain/${selectedDomain}`, `context/${context}`];
  if (DOMAIN_KNOWLEDGE[selectedDomain]) {
    tags.push(...DOMAIN_KNOWLEDGE[selectedDomain].tags.slice(0, 2));
    tags.push(`year/${tp.date.now("YYYY")}`);
  }
  return [...new Set(tags)];
}
/**
 * Suggest related MOCs based on domain
 */
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
// Step 1: Get basic note info
const fileName = tp.file.title;
const title = await tp.system.prompt("📝 Note Title:", fileName.includes("Untitled") ? "" : fileName) || "Untitled Note";
if (!title) return;
// Step 2: Smart context analysis
const contextAnalysis = analyzeContext(title);
const suggestedDomains = contextAnalysis.domains.length > 0 ? 
  contextAnalysis.domains : 
  Object.keys(DOMAIN_KNOWLEDGE);
// Step 3: Core selections with smart defaults
const noteType = await tp.system.suggester(
  DEFAULT_TYPES.map(t => `📝 ${t.charAt(0).toUpperCase() + t.slice(1)}`),
  DEFAULT_TYPES,
  false,
  "📋 Note Type:",
  DEFAULT_TYPES[0]
);
const source = await tp.system.suggester(
  SOURCE_TYPES.map(s => `📚 ${s.charAt(0).toUpperCase() + s.slice(1)}`),
  SOURCE_TYPES,
  false,
  "📖 Source Origin (Optional):",
  ""
);
const primaryDomain = await tp.system.suggester(
  suggestedDomains.map(d => `🌐 ${d.charAt(0).toUpperCase() + d.slice(1).replace('-', ' ')}`),
  suggestedDomains,
  false,
  "🌍 Primary Domain:",
  suggestedDomains[0]
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
  "🎯 Context:",
  "reference"
);
// Step 4: Status tracking
const maturityObj = await tp.system.suggester(
  MATURITY_LEVELS.map(m => m.label),
  MATURITY_LEVELS,
  false,
  "🌿 Maturity Level:",
  MATURITY_LEVELS[0]
);
const maturity = maturityObj.value;
const confidenceObj = await tp.system.suggester(
  CONFIDENCE_LEVELS.map(c => c.label),
  CONFIDENCE_LEVELS,
  false,
  "📊 Confidence Level:",
  CONFIDENCE_LEVELS[1]
);
const confidence = confidenceObj.value;
// Step 5: Smart tag generation
const smartTags = generateSmartTags(primaryDomain, noteType, context);
const additionalTags = await tp.system.prompt(
  "🏷️ Additional Tags (comma-separated, optional):",
  ""
);
// Step 6: Relationship mapping
const suggestedMOCs = suggestMOCs([primaryDomain, ...contextAnalysis.domains]);
const linkUp = await tp.system.suggester(
  suggestedMOCs.length > 0 ? 
    [...suggestedMOCs.map(m => `🔗 ${m}`), "➕ Other MOC", "❌ None"] : 
    ["➕ Select MOC", "❌ None"],
  suggestedMOCs.length > 0 ? 
    [...suggestedMOCs, "other", "none"] : 
    ["other", "none"],
  false,
  "枢纽 Link to MOC:",
  suggestedMOCs[0] || "none"
);
let finalLinkUp = [];
if (linkUp === "other") {
  const customMOC = await tp.system.prompt("Enter MOC link (e.g., [[my-moc]]):");
  if (customMOC) finalLinkUp.push(customMOC);
} else if (linkUp !== "none") {
  finalLinkUp.push(`[[${linkUp}]]`);
}
// Step 7: Custom aliases
const alias1 = await tp.system.prompt("🔖 Alias 1 (Optional):", "");
const alias2 = await tp.system.prompt("🔖 Alias 2 (Optional):", "");
// ─────────────────────────────────────────────────────────────────────────
// 📊 METADATA CALCULATIONS
// ─────────────────────────────────────────────────────────────────────────
const dateNow = tp.date.now("YYYY-MM-DD");
const timeNow = tp.date.now("HH:mm:ss");
const year = tp.date.now("YYYY");
const id = tp.date.now("YYYYMMDDHHmmss");
const nextReviewDays = REVIEW_SCHEDULES[maturity] || 7;
const nextReview = tp.date.now("YYYY-MM-DD", nextReviewDays);
// Process tags
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
  - "<%= alias1 %>"
<%* } -%>
<%* if (alias2) { -%>
  - "<%= alias2 %>"
<%* } -%>
<%* } -%>
tags:
<% allTags.forEach(tag => { -%>
  - "<%= tag %>"
<% }); -%>
source: <%= source ? `"${source}"` : '""' %>
id: "<%= id %>"
created: "<%= dateNow %>T<%= timeNow %>"
modified: "<%= dateNow %>T<%= timeNow %>"
week: "[[<%= tp.date.now("gggg-[W]WW") %>]]"
month: "[[<%= tp.date.now("YYYY-MM") %>]]"
quarter: "[[<%= tp.date.now("YYYY-[Q]Q") %>]]"
year: "[[<%= year %>]]"
type: "<%= noteType %>"
maturity: "<%= maturity %>"
confidence: "<%= confidence %>"
next-review: "<%= nextReview %>"
review-count: 0
link-count: 0
backlink-count: 0
<%* if (finalLinkUp.length > 0) { -%>
link-up:
<% finalLinkUp.forEach(link => { -%>
  - "<%= link %>"
<% }); -%>
<%* } -%>
link-related:
  - "[[<%= dateNow %>|Daily-Note]]"
---
# 📚 <%= title %>
## 🎯 Overview
<% if (source) { %>
**Source:** <%= source.charAt(0).toUpperCase() + source.slice(1) %>
<% } %>
## 🧠 Key Insights
## 📖 Detailed Explanation
## 🔗 Related Concepts
## 🛠️ Applications
## 📚 References
<% if (source) { %>
- Source: <%= source %>
<% } %>
## 🔄 Connections
- **Link Up:** <% if (finalLinkUp.length > 0) { %><%= finalLinkUp.join(', ') %><% } else { %>None specified<% } %>
- **Related Notes:** [[<%= dateNow %>|Daily-Note]]
## 📅 Review Schedule
- **Maturity:** <%= maturity.charAt(0).toUpperCase() + maturity.slice(1) %> 
- **Confidence:** <%= confidence.charAt(0).toUpperCase() + confidence.slice(1) %>
- **Next Review:** [[<%= nextReview %>]]

---
**Metadata Tags:** <% allTags.forEach((tag, i) => { %><%= (i > 0 ? ', ' : '') + tag %><% }); %>
```
## Key Improvements:
### 🎯 **Intelligent Context Detection**
- Auto-analyzes title to suggest relevant domains
- Provides smart defaults based on content patterns
- Reduces cognitive load with contextual suggestions
### 🚀 **Streamlined User Flow**
- Fewer mandatory prompts (6 core questions instead of 10+)
- Batch selection with visual icons
- Smart defaults reduce decision fatigue
### 🧠 **Enhanced Intelligence**
- Domain-specific tag suggestions
- Automatic MOC linking based on content
- Adaptive review scheduling based on maturity
### 🎨 **Better User Experience**
- Visual icons for quick recognition
- Clear section organization
- Helpful placeholders and examples
### ⚙️ **Flexible Configuration**
- Easy to customize domain knowledge bases
- Configurable review schedules
- Extensible tag systems
### 📊 **Rich Metadata Tracking**
- Comprehensive status tracking
- Relationship mapping
- Automatic date/time management