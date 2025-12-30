---
aliases:
  - Philosophy
  - philosophy
tags:
  - type/permanent
  - year/2025
  - status/budding
  - critical-thinking
  - decision-science
  - processing-workflow
  - critical-thinking/logic
  - conceptual-learning
  - dual-process-theory
  - perception
  - reasoning
  - concept/knowledge-synthesis
source: report
id: "20251213025433"
created: 2025-12-13T02:54:33
modified: 2025-12-13T02:54:33
week: "[[2025-W50]]"
month: "[[2025-12]]"
quarter: "[[2025-Q4]]"
year: "[[2025]]"
type: concept
maturity: seedling
confidence: speculative
next-review: 2025-12-20
link-up:
  - "[[99-archive/05-moc's/cognitive-science-moc]]"
link-related:
  - "[[2025-12-13|Daily-Note]]"
status: active

review-priority: medium
review-last-reviewed: null
review-next-review: 2025-12-17
review-count: 0
review-interval: 3

---

> [!overview] ### <span style='color: #7200ff;'>Overview</span>
> - **Title**: [[Philosophy]]
> - **MOC**: `=this.link-up`

```dataviewjs
// SYSTEM: Enhanced Semantic Bridge Engine v2.0
// PURPOSE: Find "Sibling" notes that share the same Outlinks (Contexts) with advanced analytics

const current = dv.current();
const myOutlinks = current.file.outlinks?.map(l => l.path) || [];

// Performance optimization: Create Set for faster lookups
const myOutlinkSet = new Set(myOutlinks);
const currentPath = current.file.path;

// Advanced sibling analysis with metadata
let siblings = [];

try {
  siblings = dv.pages()
    .where(p => {
      // Safety checks
      if (!p.file?.path || p.file.path === currentPath) return false;
      // Exclude already linked notes
      if (current.file.outlinks?.some(l => l.path === p.file.path)) return false;
      return true;
    })
    .map(p => {
      try {
        // Calculate shared connections
        const shared = p.file.outlinks?.filter(l => myOutlinkSet.has(l.path)) || [];
        const sharedCount = shared.length;
        
        // Calculate similarity score (0-100%)
        const totalConnections = myOutlinks.length + (p.file.outlinks?.length || 0);
        const similarityScore = totalConnections > 0 ? Math.round((sharedCount * 2 / totalConnections) * 100) : 0;
        
        return { 
          link: p.file.link, 
          sharedCount, 
          sharedLinks: shared,
          similarityScore,
          maturity: p.maturity || "unset",
          type: p.type || "unknown",
          lastModified: p.file.mtime
        };
      } catch (e) {
        console.warn("Error processing page:", p.file?.path, e);
        return null;
      }
    })
    .where(p => p && p.sharedCount > 0)
    .sort(p => p.similarityScore, "desc")
    .limit(8);
    
  // Ensure siblings is an array
  if (!Array.isArray(siblings)) {
    siblings = [];
  }
} catch (e) {
  console.error("Error building siblings:", e);
  siblings = [];
}

// Render enhanced semantic bridges
if (siblings.length > 0) {
  dv.header(3, "🔗 Semantic Bridges (Missing Connections)");
  
  // Add summary statistics with error handling
  try {
    const totalSharedConnections = siblings.reduce((sum, s) => sum + (s.sharedCount || 0), 0);
    const avgSimilarity = siblings.length > 0 ? 
      Math.round(siblings.reduce((sum, s) => sum + (s.similarityScore || 0), 0) / siblings.length) : 0;
    
    dv.paragraph(`**Found ${siblings.length} semantic siblings** • Total shared: ${totalSharedConnections} connections • Avg. similarity: ${avgSimilarity}%`);
  } catch (e) {
    console.warn("Error calculating sibling statistics:", e);
    dv.paragraph(`**Found ${siblings.length} semantic siblings**`);
  }
  
  dv.table(
    ["Note", "Similarity", "Strength", "Maturity", "Type", "Shared Context"], 
    siblings.map(s => [
      s.link, 
      `📊${s.similarityScore || 0}%`,
      "🔗" + (s.sharedCount || 0), 
      s.maturity === "evergreen" ? "🌳" + s.maturity : 
      s.maturity === "budding" ? "🌿" + s.maturity :
      s.maturity === "developing" ? "🌱" + s.maturity :
      s.maturity === "seedling" ? "大豆" + s.maturity : "❓unset",
      s.type || "unknown",
      s.sharedLinks?.slice(0, 2).map(l => l.displayName || l.path).join(", ") + ((s.sharedLinks?.length || 0) > 2 ? "…" : "") || ""
    ])
  );
} else {
  dv.paragraph("*No semantic siblings found. This note is unique in its connections.*");
}

// DOMAIN COVERAGE: Advanced domain analysis
const myTags = current.tags || [];
const primaryDomain = myTags.find(t => typeof t === "string" && t.includes("/"))?.split("/")[0] 
                   || myTags.find(t => typeof t === "string");

if (primaryDomain) {
  let domainNotes = [];
  try {
    domainNotes = dv.pages()
      .where(p => 
        p.tags && 
        Array.isArray(p.tags) && 
        p.tags.some(t => 
          typeof t === "string" && 
          (t.startsWith(primaryDomain) || t === primaryDomain)
        )
      );
  } catch (e) {
    console.warn("Error filtering domain notes:", e);
    domainNotes = [];
  }
   
  const maturityDistribution = {
    evergreen: domainNotes.filter(p => p.maturity === "evergreen").length,
    budding: domainNotes.filter(p => p.maturity === "budding").length,
    developing: domainNotes.filter(p => p.maturity === "developing").length,
    seedling: domainNotes.filter(p => p.maturity === "seedling").length,
    unset: domainNotes.filter(p => !p.maturity).length
  };

  // Advanced domain health metrics
  const totalNotes = domainNotes.length;
  const matureNotes = maturityDistribution.evergreen + maturityDistribution.budding;
  const coverage = totalNotes > 0 ? Math.round((matureNotes / totalNotes) * 100) : 0;
  
  // Domain activity score (based on recent modifications)
  const recentNotes = domainNotes.filter(p => {
    try {
      const daysOld = (new Date() - new Date(p.file.mtime)) / (1000 * 60 * 60 * 24);
      return daysOld < 30;
    } catch (e) {
      return false;
    }
  }).length;
  const activityScore = totalNotes > 0 ? Math.round((recentNotes / totalNotes) * 100) : 0;

  dv.header(3, `📂 Domain Analysis: ${primaryDomain}`);
  dv.paragraph(`**Total notes**: ${totalNotes} | **Recent activity**: ${activityScore}% (30d)`);
  dv.paragraph(`**Maturity breakdown**: 🌳${maturityDistribution.evergreen} | 🌿${maturityDistribution.budding} | 🌱${maturityDistribution.developing} | 🌰${maturityDistribution.seedling} | ❓${maturityDistribution.unset}`);
  dv.paragraph(`**Domain health**: ${coverage}% mature (evergreen + budding)`);
  
  // Domain health indicator
  const healthIndicator = coverage >= 80 ? "🟢 Excellent" : 
                         coverage >= 60 ? "🟡 Good" : 
                         coverage >= 40 ? "🟠 Fair" : "🔴 Poor";
  dv.paragraph(`**Health status**: ${healthIndicator}`);
}

// NETWORK INTELLIGENCE: Advanced connectivity analysis
const inlinks = current.file.inlinks || [];
const outlinks = current.file.outlinks || [];

dv.header(3, "🕸️ Network Intelligence");
const networkMetrics = [
  ["**Metric**", "**Value**", "**Insight**"],
  ["In-links", inlinks.length, inlinks.length > 10 ? "⚡ Hub" : inlinks.length > 0 ? "🌱 Node" : "🕸️ Orphan"],
  ["Out-links", outlinks.length, outlinks.length > 15 ? "🗺️ Explorer" : outlinks.length > 5 ? "🧭 Navigator" : "🎯 Focused"],
  ["Link Ratio", outlinks.length > 0 ? (inlinks.length / outlinks.length).toFixed(1) : "∞", 
   outlinks.length > 0 && inlinks.length / outlinks.length > 2 ? "📈 High authority" : "📊 Balanced"]
];

dv.table(networkMetrics[0], networkMetrics.slice(1));

// TEMPORAL ANALYSIS: Content aging and review patterns
dv.header(3, "⏰ Temporal Intelligence");
try {
  const created = current.file.ctime;
  const modified = current.file.mtime;
  const ageDays = Math.floor((new Date() - new Date(created)) / (1000 * 60 * 60 * 24));
  const stalenessDays = Math.floor((new Date() - new Date(modified)) / (1000 * 60 * 60 * 24));

  const reviewInsights = [];
  if (current["review-count"] > 5) reviewInsights.push("🔁 Well-reviewed");
  if (stalenessDays > 180) reviewInsights.push("⏰ Needs refresh");
  if (ageDays < 30) reviewInsights.push("🆕 New content");

  dv.paragraph(`**Age**: ${ageDays} days | **Staleness**: ${stalenessDays} days`);
  dv.paragraph(`**Review status**: ${current["review-count"] || 0} reviews | ${reviewInsights.join(" • ") || "📝 Standard"}`);
} catch (e) {
  console.warn("Error in temporal analysis:", e);
  dv.paragraph("*Temporal analysis unavailable*");
}
```
> [!abstract] ### 🏷️ Tag Intelligence
> **Tag Count**: `= length(this.tags)` | **Unique Domains**: `= length(filter(this.tags, (t) => contains(t, "/")))` hierarchical tags
> **Tag Density**: `= choice(length(this.tags) < 3, "⚠️Sparse", choice(length(this.tags) > 10, "📚Rich", "✅Balanced"))`
> > 
> > ---
> 
> ```dataviewjs
> // TAG CO-OCCURRENCE: Find notes sharing the most tags with this note
> const current = dv.current();
> 
> // Safely get tags from current note
> let myTags = [];
> if (current.tags) {
>     if (Array.isArray(current.tags)) {
>         myTags = current.tags;
>     } else if (typeof current.tags === 'string') {
>         myTags = [current.tags];
>     }
> }
> 
> if (myTags.length > 0) {
>     const tagSiblings = dv.pages()
>         .where(p => p.file.path !== current.file.path)
>         .where(p => {
>             // Safely check if page has tags
>             if (!p.tags) return false;
>             // Convert tags to array if needed
>             let pageTags = [];
>             if (Array.isArray(p.tags)) {
>                 pageTags = p.tags;
>             } else if (typeof p.tags === 'string') {
>                 pageTags = [p.tags];
>             }
>             return pageTags.length > 0;
>         })
>         .map(p => {
>             // Safely convert page tags to array
>             let pageTags = [];
>             if (p.tags) {
>                 if (Array.isArray(p.tags)) {
>                     pageTags = p.tags;
>                 } else if (typeof p.tags === 'string') {
>                     pageTags = [p.tags];
>                 }
>             }
>             
>             // Find shared tags
>             const sharedTags = pageTags.filter(t => {
>                 if (typeof t === 'string') {
>                     return myTags.includes(t);
>                 } else if (t && typeof t === 'object' && t.path) {
>                     // Handle tag objects
>                     return myTags.some(myTag => {
>                         if (typeof myTag === 'string') {
>                             return myTag === t.path;
>                         }
>                         return false;
>                     });
>                 }
>                 return false;
>             });
>             
>             return {
>                 link: p.file.link,
>                 sharedCount: sharedTags.length,
>                 sharedTags: sharedTags,
>                 totalTags: pageTags.length
>             };
>         })
>         .where(p => p.sharedCount >= 2) // At least 2 shared tags
>         .sort(p => p.sharedCount, "desc")
>         .limit(5);
> 
>     if (tagSiblings.length > 0) {
>         dv.header(5, "🏷️ Tag Siblings (Shared Taxonomy)");
>         dv.table(
>             ["Note", "Overlap", "Shared Tags"],
>             tagSiblings.map(s => {
>                 // Safely extract tag names for display
>                 let displayTags = s.sharedTags.map(t => {
>                     if (typeof t === 'string') {
>                         return t;
>                     } else if (t && typeof t === 'object' && t.path) {
>                         return t.path;
>                     }
>                     return String(t);
>                 });
>                 
>                 return [
>                     s.link,
>                     s.sharedCount + "/" + s.totalTags,
>                     displayTags.slice(0, 3).join(", ") + (s.sharedCount > 3 ? "…" : "")
>                 ];
>             })
>         );
>     } else {
>         dv.paragraph("*No tag siblings with 2+ shared tags found.*");
>     }
> } else {
>     dv.paragraph("*No tags on this note to analyze.*");
> }
> ```

---
# Foundational Understanding
> [!definition] # Definition
> [**Philosophy**:: At its core, philosophy seeks to understand the deepest and most general aspects of reality, humanity's place within it, and the principles that govern thought and action. Unlike empirical sciences, philosophy often investigates questions that cannot be answered solely through observation or experimentation.]
> 
> ##### [✅`= dateformat(this.file.ctime, "MMMM dd, yyyy")` - Initial Creation]

>[! ] # Ouline
> - ## **Philosophy**
>     - **Etymology & Definition**
>         - Greek: *philosophia* ("love of wisdom")
>         - Study of fundamental questions about existence, knowledge, values, reason, mind, and language
>     - **Main Branches of Philosophy**
>         - **Metaphysics**
>             - Study of the nature of reality and existence
>             - Ontology (study of being)
>             - Cosmology (study of the universe)
>             - Mind-body problem
>             - Free will vs. Determinism
>         - **Epistemology**
>             - Study of the nature and scope of knowledge
>             - Sources of knowledge (perception, reason, intuition, testimony)
>             - Justification of belief
>             - Rationalism vs. Empiricism
>             - Skepticism
>         - **Ethics (Moral Philosophy)**
>             - Study of moral principles and values
>             - Meta-ethics (nature of moral judgment)
>             - Normative ethics (how one ought to act)
>                 - Deontology (duty-based ethics)
>                 - Consequentialism (outcome-based ethics)
>                 - Virtue Ethics (character-based ethics)
>             - Applied ethics (specific moral issues)
>         - **Logic**
>             - Study of valid reasoning and argumentation
>             - Deductive reasoning
>             - Inductive reasoning
>             - Fallacies
>         - **Aesthetics**
>             - Study of beauty, art, and taste
>             - Nature of art
>             - Experience of beauty
>         - **Political Philosophy**
>             - Study of government, justice, liberty, rights, and political obligation
>             - Theories of justice
>             - Forms of government
>             - Rights and duties of citizens
>     - **Key Concepts & Themes**
>         - Truth
>         - Reality
>         - Existence
>         - Knowledge
>         - Reason
>         - Morality
>         - Beauty
>         - Meaning of life
>     - **Historical Periods & Movements**
>         - **Ancient Philosophy**
>             - Pre-Socratics (Thales, Heraclitus, Parmenides)
>             - Classical Greek (Socrates, Plato, Aristotle)
>             - Hellenistic (Epicureanism, Stoicism, Skepticism)
>         - **Medieval Philosophy**
>             - Scholasticism (Augustine, Aquinas)
>             - Influence of Abrahamic religions
>         - **Modern Philosophy**
>             - Renaissance (Humanism)
>             - Rationalism (Descartes, Spinoza, Leibniz)
>             - Empiricism (Locke, Berkeley, Hume)
>             - Enlightenment (Kant, Rousseau)
>         - **19th Century Philosophy**
>             - German Idealism (Hegel)
>             - Romanticism
>             - Existentialism precursors (Kierkegaard, Nietzsche)
>             - Utilitarianism (Mill)
>         - **20th Century & Contemporary Philosophy**
>             - Analytic Philosophy (Russell, Wittgenstein)
>             - Continental Philosophy (Husserl, Heidegger, Sartre, Foucault, Derrida)
>             - Pragmatism (Peirce, James, Dewey)
>             - Postmodernism
>     - **Philosophical Methods**
>         - Socratic Method (dialogical inquiry)
>         - Dialectic
>         - Logical Analysis
>         - Thought Experiments
>         - Conceptual Analysis
>     - **Relationship to Other Disciplines**
>         - Science
>         - Religion
>         - Art
>         - Politics
>         - Psychology
>         - Linguistics

----

>[! ] # Philosophy: An Introduction
> 
> Philosophy, derived from the Greek "philosophia" meaning "love of wisdom," is a field of study that explores fundamental questions about existence, knowledge, values, reason, mind, and language. It is characterized by its critical, systematic approach and its reliance on rational argument.
> 
> ---
> ### What is Philosophy?
> 
> At its core, philosophy seeks to understand the deepest and most general aspects of reality, humanity's place within it, and the principles that govern thought and action. Unlike empirical sciences, philosophy often investigates questions that cannot be answered solely through observation or experimentation.
> 
> Key characteristics include:
> -   **Rational Inquiry**: Emphasizes logical reasoning and argumentation.
> -   **Critical Thinking**: Challenges assumptions and analyzes concepts.
> -   **Universality**: Addresses fundamental questions relevant to all human experience.
> -   **Systematic Approach**: Aims to build coherent frameworks of thought.

> [!phase-four] ## Major Branches of Philosophy
> 
> Philosophy is traditionally divided into several core branches, each focusing on a distinct set of questions:
> 
> ### 1. Metaphysics
> The study of the fundamental nature of reality, including the relationship between mind and matter, between substance and attribute, and between potentiality and actuality.
> -   **Key Questions**: What is reality? Does God exist? What is time? What is causality? Do we have free will?
> 
> ### 2. Epistemology
> The theory of knowledge. It investigates the nature, origin, and scope of knowledge.
> -   **Key Questions**: What is knowledge? How do we acquire knowledge? What are the limits of human knowledge? How can we distinguish belief from justified true belief?
> 
> ### 3. Ethics (Moral Philosophy)
> The study of moral principles that govern human behavior, the morality of human action, and the goodness or badness of human character.
> -   **Key Questions**: What is good? What is right action? How should we live? Is morality objective or subjective? What are our duties and obligations?
> 
> ### 4. Logic
> The study of reasoning and argumentation. It provides tools for analyzing the structure of arguments to determine their validity and soundness.
> -   **Key Questions**: What constitutes a valid argument? How can we distinguish good reasoning from bad reasoning? What are fallacies?
> 
> ### 5. Aesthetics
> The philosophy of art and beauty. It explores the nature of art, beauty, taste, creation, and appreciation.
> -   **Key Questions**: What is beauty? What is art? What makes something beautiful or artistic? What is the purpose of art?
> 
> ### Other Important Branches:
> -   **Political Philosophy**: The study of government, politics, liberty, justice, property, rights, law, and the enforcement of a legal code by authority.
> -   **Philosophy of Mind**: Explores the nature of the mind, mental events, mental functions, mental properties, consciousness, and their relationship to the physical body.
> -   **Philosophy of Science**: Examines the philosophical foundations, methods, and implications of science.
> -   **Philosophy of Language**: Investigates the nature of language, meaning, reference, truth, and interpretation.

> [!key] ### Why Study Philosophy?
> 
> Studying philosophy cultivates essential intellectual skills and offers profound insights:
> -   **Critical Thinking**: Sharpens analytical and evaluative skills.
> -   **Problem-Solving**: Teaches how to approach complex problems systematically.
> -   **Argumentation**: Develops the ability to construct and defend reasoned arguments.
> -   **Perspective-Taking**: Encourages understanding diverse viewpoints and challenging assumptions.
> -   **Self-Reflection**: Promotes introspection about one's own values, beliefs, and purpose.
> -   **Communication**: Enhances clarity and precision in thought and expression.
> >[! ] ##### Key Concepts and Themes
> > Throughout its history, philosophy has grappled with recurring concepts:
> > -   **Truth**: Correspondence to reality, coherence, pragmatic utility.
> > -   **Reality**: What exists independently of our minds.
> > -   **Knowledge**: Justified true belief, acquaintance, skill.
> > -   **Morality**: Principles distinguishing right from wrong.
> > -   **Reason**: The capacity for conscious thought, inference, and judgment.
> > -   **Existence**: The state of being real.
> > -   **Meaning**: The significance or purpose of something, particularly life.
> > -   **Consciousness**: The state of being aware of one's own existence and surroundings.


> [!plan] ## Historical Overview (Brief)
>
> Philosophy has a rich history, evolving through various periods and traditions:
> -   **Ancient Philosophy (c. 600 BCE - 600 CE)**: Dominated by Greek philosophers like **Socrates**, **Plato**, and **Aristotle**, laying foundations for Western thought.
> -   **Medieval Philosophy (c. 600 - 1600 CE)**: Heavily influenced by Christian, Islamic, and Jewish theology, with figures like **Augustine** and **Aquinas**.
> -   **Modern Philosophy (c. 1600 - 1900 CE)**: Characterized by the Enlightenment and debates between **Rationalism** (Descartes, Spinoza, Leibniz) and **Empiricism** (Locke, Berkeley, Hume), culminating in **Kant's** critical philosophy.
> -   **19th & 20th Century Philosophy**: Emergence of diverse movements including **Existentialism** (Kierkegaard, Nietzsche, Sartre), **Analytic Philosophy** (Russell, Wittgenstein), **Phenomenology** (Husserl, Heidegger), and **Postmodernism**.

> [!in-note-metadata] ## Conclusion
>  
> 
> Philosophy remains a vibrant and essential field that continually challenges us to think deeply about fundamental questions. By engaging with philosophical inquiry, individuals can develop a more nuanced understanding of themselves, others, and the world, fostering intellectual growth and a richer human experience. It is not just a collection of theories, but an ongoing method of critical inquiry that underpins all knowledge and informs our lives.
> 









>[! ] ### 🔗Backlinks & Connections
> ```dataview
> TABLE 
>     type AS "Type",
>     maturity AS "Maturity",
>     created AS "Created"
> FROM [[#]]
> SORT created DESC
> LIMIT 15
> ```

> [!warning] ### 📅 Review Intelligence
> **Next Review**: `= this.next-review` | **Review Count**: `= this.review-count`
> **Review Status**: `= choice(this.next-review < date(today), "🔴 OVERDUE", choice(this.next-review = date(today), "🟡 Due Today", choice(dateformat(this.next-review, "yyyy-MM-dd") <= dateformat(date(today) + dur(7 days), "yyyy-MM-dd"), "🟢 This Week", "⚪ Scheduled")))`
> **Days Until Review**: `= choice(this.next-review, (this.next-review - date(today)).days + " days", "Not scheduled")

> [!abstract] ### 🏷️ Tag Intelligence
> **Tag Count**: `= length(this.tags)` | **Unique Domains**: `= length(filter(this.tags, (t) => contains(t, "/")))` hierarchical tags
> **Tag Density**: `= choice(length(this.tags) < 3, "⚠️Sparse", choice(length(this.tags) > 10, "📚Rich", "✅Balanced"))`
> 
> ---
> 
> ```dataviewjs
> // TAG CO-OCCURRENCE: Find notes sharing the most tags with this note
> const current = dv.current();
> 
> // Safely get tags from current note
> let myTags = [];
> if (current.tags) {
>     if (Array.isArray(current.tags)) {
>         myTags = current.tags;
>     } else if (typeof current.tags === 'string') {
>         myTags = [current.tags];
>     }
> }
> 
> if (myTags.length > 0) {
>     const tagSiblings = dv.pages()
>         .where(p => p.file.path !== current.file.path)
>         .where(p => {
>             // Safely check if page has tags
>             if (!p.tags) return false;
>             // Convert tags to array if needed
>             let pageTags = [];
>             if (Array.isArray(p.tags)) {
>                 pageTags = p.tags;
>             } else if (typeof p.tags === 'string') {
>                 pageTags = [p.tags];
>             }
>             return pageTags.length > 0;
>         })
>         .map(p => {
>             // Safely convert page tags to array
>             let pageTags = [];
>             if (p.tags) {
>                 if (Array.isArray(p.tags)) {
>                     pageTags = p.tags;
>                 } else if (typeof p.tags === 'string') {
>                     pageTags = [p.tags];
>                 }
>             }
>             
>             // Find shared tags
>             const sharedTags = pageTags.filter(t => {
>                 if (typeof t === 'string') {
>                     return myTags.includes(t);
>                 } else if (t && typeof t === 'object' && t.path) {
>                     // Handle tag objects
>                     return myTags.some(myTag => {
>                         if (typeof myTag === 'string') {
>                             return myTag === t.path;
>                         }
>                         return false;
>                     });
>                 }
>                 return false;
>             });
>             
>             return {
>                 link: p.file.link,
>                 sharedCount: sharedTags.length,
>                 sharedTags: sharedTags,
>                 totalTags: pageTags.length
>             };
>         })
>         .where(p => p.sharedCount >= 2) // At least 2 shared tags
>         .sort(p => p.sharedCount, "desc")
>         .limit(5);
> 
>     if (tagSiblings.length > 0) {
>         dv.header(5, "🏷️ Tag Siblings (Shared Taxonomy)");
>         dv.table(
>             ["Note", "Overlap", "Shared Tags"],
>             tagSiblings.map(s => {
>                 // Safely extract tag names for display
>                 let displayTags = s.sharedTags.map(t => {
>                     if (typeof t === 'string') {
>                         return t;
>                     } else if (t && typeof t === 'object' && t.path) {
>                         return t.path;
>                     }
>                     return String(t);
>                 });
>                 
>                 return [
>                     s.link,
>                     s.sharedCount + "/" + s.totalTags,
>                     displayTags.slice(0, 3).join(", ") + (s.sharedCount > 3 ? "…" : "")
>                 ];
>             })
>         );
>     } else {
>         dv.paragraph("*No tag siblings with 2+ shared tags found.*");
>     }
> } else {
>     dv.paragraph("*No tags on this note to analyze.*");
> }
> ```
---

### 📖 Extracted Definitions From Cognitive Science
```dataviewjs
try {
  // Configuration
  const folderPath = "03-notes/01_permanent-notes/01_cognitive-development"; // Change this to your folder
  
  // Get all pages from the specified folder
  const pages = dv.pages(`"${folderPath}"`);
  
  // Storage for all definitions across files
  let allDefinitions = [];
  
  // Process each file
  for (let page of pages) {
    try {
      const content = await dv.io.load(page.file.path);
      const bracketedFieldRegex = /\[\*\*([^*]+?)\*\*::\s*([^\]]+?)\]/g;
       
      let match;
      while ((match = bracketedFieldRegex.exec(content)) !== null) {
        allDefinitions.push({
          source: page.file.link,
          key: match[1].trim(), // This is the clean term without ** markdown
          value: match[2].trim()
        });
      }
    } catch (e) {
      console.warn(`Error processing file ${page.file.path}:`, e);
      continue;
    }
  }
  
  // Display aggregated results
  if (allDefinitions.length > 0) {
    dv.header(3, `📚 All Definitions Across ${folderPath} (${allDefinitions.length} total)`);
    
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
        ["📄 Source", "🔑 Term", "📝 Definition"],
        grouped[letter].map(d => [
          d.source,
          `**${d.key}**`,
          d.value
        ])
      );
      dv.paragraph(""); // Add spacing between groups
    }
    
  } else {
    dv.paragraph(`*No bracketed inline fields found in "${folderPath}".*`);
  }
  
} catch (error) {
  console.error("Error in definitions aggregation script:", error);
  dv.paragraph("*Error loading definitions. Check console for details.*");
}
```


---
