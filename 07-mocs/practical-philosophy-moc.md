---
aliases:
  - Philosophy MOC
  - Practical Philosophy Hub
  - Applied Philosophy Index
  - Philosophy Knowledge Map
tags:
  - type/moc
  - year/2025
  - philosophy
  - stoicism
  - epistemology
  - pragmatism
  - status/developing
  - context/personal
  - nature/conceptual
source: original-synthesis
id: 20251213-philosophy-moc
created: 2025-12-13T00:00:00
modified: 2025-12-13T00:00:00
week: "[[2025-W50]]"
month: "[[2025-12]]"
quarter: "[[2025-Q4]]"
year: "[[2025]]"
type: moc
maturity: developing
confidence: moderate
next-review: 2025-12-20
review-count: 0
cssclass: philosophy-moc
link-up:
  - "[[cognitive-science-moc]]"
  - "[[pkb-&-pkm-moc]]"
link-related:
  - "[[stoicism]]"
  - "[[epistemology]]"
  - "[[pragmatism]]"
philosophy-filter: all
---

# 🏛️ Practical Philosophy MOC

> [!abstract] Hub Overview
> This [[Map of Content]] serves as the central navigation hub for **practical philosophy**—philosophical traditions and frameworks designed for **application in daily life**. Unlike purely theoretical philosophy, practical philosophy emphasizes [[actionable wisdom]], [[self-regulation]], and [[epistemic accountability]].
> 
> [**MOC-Purpose**:: To organize, connect, and surface philosophical concepts that directly inform decision-making, emotional regulation, and knowledge validation in personal knowledge management practice.]

```meta-bind
INPUT[inlineSelect(
  option(all, 🌐 All Notes),
  option(stoicism, 🏺 Stoicism),
  option(epistemology, 🔬 Epistemology),
  option(pragmatism, 🔧 Pragmatism),
  option(mind, 🧠 Philosophy of Mind)
):philosophy-filter]
```

---

## 📊 Philosophy Knowledge Dashboard

> [!metadata] ### Hub Metrics & Health
> **Total Philosophy Notes:** `$= dv.pages('#philosophy OR #stoicism OR #epistemology OR #pragmatism').length`
> **Evergreen Notes:** `$= dv.pages('#philosophy OR #stoicism OR #epistemology').where(p => p.maturity === "evergreen").length`
> **Seedlings Needing Attention:** `$= dv.pages('#philosophy OR #stoicism OR #epistemology').where(p => p.maturity === "seedling").length`
> **Notes Due for Review:** `$= dv.pages('#philosophy OR #stoicism').where(p => p["next-review"] && dv.date(p["next-review"]) <= dv.date("today")).length`

```dataviewjs
// 🎯 PHILOSOPHY DOMAIN DISTRIBUTION CHART
// Shows breakdown of notes across philosophical branches

const pages = dv.pages('#philosophy OR #stoicism OR #epistemology OR #pragmatism OR #philosophy-of-mind');

// Count by primary domain
const domains = {
  "🏺 Stoicism": 0,
  "🔬 Epistemology": 0,
  "🔧 Pragmatism": 0,
  "🧠 Philosophy of Mind": 0,
  "📚 General": 0
};

for (let page of pages) {
  const tags = page.file.tags || [];
  const tagStr = tags.join(" ");
  
  if (tagStr.includes("stoicism") || tagStr.includes("stoic")) {
    domains["🏺 Stoicism"]++;
  } else if (tagStr.includes("epistemology") || tagStr.includes("epistemic")) {
    domains["🔬 Epistemology"]++;
  } else if (tagStr.includes("pragmatism") || tagStr.includes("pragmatic")) {
    domains["🔧 Pragmatism"]++;
  } else if (tagStr.includes("philosophy-of-mind") || tagStr.includes("cognitive")) {
    domains["🧠 Philosophy of Mind"]++;
  } else {
    domains["📚 General"]++;
  }
}

// Render as formatted list
dv.header(4, "Domain Distribution");
for (let [domain, count] of Object.entries(domains)) {
  if (count > 0) {
    const bar = "█".repeat(Math.min(count, 20)) + "░".repeat(Math.max(0, 20 - count));
    dv.paragraph(`${domain}: ${bar} (${count})`);
  }
}
```

---

## 🏺 Stoicism

> [!principle-point] Core Doctrine
> [**Stoicism-Core-Principle**:: The distinction between what is "up to us" (ἐφ' ἡμῖν) and what is not—our judgments, impulses, desires, and aversions versus external circumstances, others' actions, and outcomes beyond our control.]

[[Stoicism]] represents the philosophical backbone of this practical philosophy collection. The [[Stoic Philosophy]] tradition offers systematic techniques for [[emotional regulation]], [[cognitive reframing]], and [[virtue cultivation]].

### 🔗 Stoic Concept Network

```dataviewjs
// 🧠 STOIC CONCEPTS SEMANTIC MAP
// Discovers and displays all Stoicism-related notes with maturity indicators

const stoicPages = dv.pages('#stoicism OR #stoic')
  .sort(p => p.maturity === "evergreen" ? 0 : p.maturity === "budding" ? 1 : p.maturity === "developing" ? 2 : 3);

if (stoicPages.length > 0) {
  dv.table(
    ["Note", "Maturity", "Confidence", "Connections", "Last Modified"],
    stoicPages.map(p => {
      const maturityEmoji = {
        "evergreen": "🌳",
        "budding": "🌿",
        "developing": "🌱",
        "seedling": "🫒",
        "needs-review": "⚠️"
      };
      const inlinks = p.file.inlinks?.length || 0;
      const outlinks = p.file.outlinks?.length || 0;
      const connections = inlinks + outlinks;
      
      return [
        p.file.link,
        (maturityEmoji[p.maturity] || "📄") + " " + (p.maturity || "unset"),
        p.confidence || "—",
        `↙${inlinks} ↗${outlinks}`,
        p.file.mtime ? p.file.mtime.toFormat("yyyy-MM-dd") : "—"
      ];
    })
  );
} else {
  dv.paragraph("*No Stoicism notes found. Create your first with the button below.*");
}
```

#### 📚 Core Stoic Concepts

> [!definition] Dichotomy of Control
> [**Dichotomy-of-Control**:: The foundational Stoic distinction (τὰ ἐφ' ἡμῖν / τὰ οὐκ ἐφ' ἡμῖν) between what depends on us—our judgments, intentions, and responses—and what does not—external events, others' actions, bodily conditions, and outcomes.]
> 
> - [[Dichotomy of Control]] — *The master key to Stoic practice*
> - Related: [[Locus of Control]] (psychological parallel)

> [!definition] Prosoche (Attention)
> [**Prosoche**:: The Stoic practice of continuous self-attention and vigilance over one's impressions, judgments, and impulses—the foundational discipline enabling all other Stoic practices.]

**Primary Notes:**
- [[Stoicism]] — *Foundational overview*
- [[Stoic Philosophy]] — *Theoretical framework*
- [[Dichotomy of Control]] — *Core practical technique*
- [[Locus of Control]] — *Psychological bridge concept*

**Stoic Techniques:**
- [[Negative Visualization]] — *Premeditatio malorum*
- [[View from Above]] — *Cosmic perspective*
- [[Memento Mori]] — *Death contemplation*
- [[Morning Preparation]] — *Prospective visualization*
- [[Evening Reflection]] — *Philosophical journaling*

**Stoic Virtues:**
- [[Wisdom (Sophia)]] — *Knowing what is truly good*
- [[Courage (Andreia)]] — *Endurance in difficulty*
- [[Justice (Dikaiosyne)]] — *Right action toward others*
- [[Temperance (Sophrosyne)]] — *Moderation and self-control*

---

## 🧠 Philosophy of Mind

> [!principle-point] Domain Focus
> [**Philosophy-of-Mind-Scope**:: The examination of mental phenomena—consciousness, intentionality, perception, and cognition—particularly as they relate to practical wisdom and self-understanding.]

This branch explores the intersection of [[Philosophy of Mind]] with practical application, emphasizing how understanding mental processes enables better [[self-regulation]] and [[metacognition]].

### 🔗 Mind Philosophy Network

```dataviewjs
// 🧠 PHILOSOPHY OF MIND CONCEPT EXPLORER
const mindPages = dv.pages('#philosophy-of-mind OR #cognitive-philosophy OR #consciousness')
  .sort(p => p.file.name);

if (mindPages.length > 0) {
  dv.table(
    ["Concept", "Type", "Connections"],
    mindPages.map(p => [
      p.file.link,
      p.type || "permanent-note",
      (p.file.inlinks?.length || 0) + (p.file.outlinks?.length || 0)
    ])
  );
} else {
  dv.paragraph("*Philosophy of Mind notes will appear here as you create them.*");
}
```

#### 📚 Core Mind Concepts

**Foundational:**
- [[Philosophy of Mind]] — *Domain overview*
- [[Stoic Philosophy]] — *Ancient mind theory*
- [[Socratic Method]] — *Dialectical inquiry*
- [[Socratic Thinking]] — *Applied questioning*

**Thinking Methods:**
> [!methodology-and-sources] Socratic Inquiry
> [**Socratic-Method**:: A form of cooperative argumentative dialogue using questioning to stimulate critical thinking, expose contradictions in one's beliefs, and arrive at well-examined conclusions.]
> 
> - [[Socratic Method]] — *The art of philosophical questioning*
> - [[Socratic Thinking]] — *Applying dialectic to daily reasoning*

---

## 🔬 Epistemology

> [!principle-point] Domain Focus  
> [**Epistemology-Practical-Focus**:: The study of knowledge, belief, and justification—particularly as applied to evaluating information sources, calibrating confidence levels, and maintaining intellectual honesty in personal knowledge work.]

[[Epistemology]] grounds our [[PKM]] practice in philosophical rigor, ensuring we approach knowledge with appropriate [[Epistemic-Humility]] and [[validation practices]].

### 🔗 Epistemology Network

```dataviewjs
// 🔬 EPISTEMOLOGY CONCEPT DISCOVERY
const epistemicPages = dv.pages('#epistemology OR #epistemic')
  .sort(p => p.maturity === "evergreen" ? 0 : 1);

if (epistemicPages.length > 0) {
  // Create hierarchical grouping
  const grouped = {};
  for (let p of epistemicPages) {
    const type = p.type || "concept";
    if (!grouped[type]) grouped[type] = [];
    grouped[type].push(p);
  }
  
  for (let [type, pages] of Object.entries(grouped)) {
    dv.header(5, `📁 ${type.charAt(0).toUpperCase() + type.slice(1)}`);
    dv.list(pages.map(p => p.file.link));
  }
} else {
  dv.paragraph("*Epistemology notes will appear here as you create them.*");
}
```

#### 📚 Core Epistemic Concepts

> [!definition] Epistemic Accountability
> [**Epistemic-Accountability**:: The intellectual virtue of taking responsibility for one's beliefs—actively seeking evidence, acknowledging uncertainty, correcting errors when discovered, and maintaining transparent reasoning processes.]

> [!definition] Epistemic Cognition
> [**Epistemic-Cognition**:: The cognitive processes involved in acquiring, evaluating, and using knowledge—including how individuals understand the nature of knowledge itself and calibrate their confidence appropriately.]

**Primary Notes:**
- [[Epistemology]] — *Domain foundation*
- [[Epistemic Accountability]] — *Intellectual responsibility*
- [[Epistemic Cognition]] — *Knowledge processing*
- [[Evolutionary Epistemology]] — *Naturalized knowledge theory*

**Applied Epistemology:**
- [[Source Evaluation]] — *Assessing information quality*
- [[Confidence Calibration]] — *Matching certainty to evidence*
- [[Epistemic-Humility]] — *Recognizing knowledge limits*

---

## 🔧 Pragmatism

> [!principle-point] Domain Focus
> [**Pragmatism-Core-Thesis**:: The philosophical tradition holding that the meaning and truth of ideas are determined by their practical consequences—"truth is what works" in guiding successful action and inquiry.]

[[Pragmatism]] provides the meta-philosophical framework for this entire MOC, emphasizing that philosophical concepts earn their place through **practical utility**.

### 🔗 Pragmatism Network

```dataviewjs
// 🔧 PRAGMATISM CONCEPT EXPLORER
const pragmaticPages = dv.pages('#pragmatism OR #pragmatic OR #practical-philosophy')
  .sort(p => p.file.name);

if (pragmaticPages.length > 0) {
  dv.table(
    ["Note", "Application Area", "Status"],
    pragmaticPages.map(p => [
      p.file.link,
      p.context || "general",
      p.maturity || "developing"
    ])
  );
} else {
  dv.paragraph("*Pragmatism notes will appear here as you create them.*");
}
```

#### 📚 Core Pragmatist Concepts

> [!definition] Pragmatic Maxim
> [**Pragmatic-Maxim**:: "Consider what effects, that might conceivably have practical bearings, we conceive the object of our conception to have. Then, our conception of these effects is the whole of our conception of the object." — Charles Sanders Peirce]

**Primary Notes:**
- [[Pragmatism]] — *Philosophical foundation*
- [[Practical Wisdom]] — *Phronesis*
- [[Instrumentalism]] — *Ideas as tools*

---

## 🌉 Cross-Domain Connections

> [!key-claim] Integration Thesis
> [**Philosophy-PKM-Integration**:: Practical philosophy and personal knowledge management share a common goal: transforming information into wisdom that guides action. Stoic practices map to PKM workflows; epistemic virtues underpin note quality; pragmatic criteria validate system design.]

```dataviewjs
// 🌉 SEMANTIC BRIDGE ENGINE - Philosophy Cross-Connections
// Discovers notes that connect multiple philosophical domains

const allPhilosophy = dv.pages('#philosophy OR #stoicism OR #epistemology OR #pragmatism OR #philosophy-of-mind');
const current = dv.current();

// Find notes that bridge domains
const bridges = allPhilosophy
  .filter(p => {
    const tags = (p.file.tags || []).join(" ");
    let domainCount = 0;
    if (tags.includes("stoicism") || tags.includes("stoic")) domainCount++;
    if (tags.includes("epistemology") || tags.includes("epistemic")) domainCount++;
    if (tags.includes("pragmatism")) domainCount++;
    if (tags.includes("philosophy-of-mind")) domainCount++;
    return domainCount >= 2; // Bridges at least 2 domains
  })
  .sort(p => p.file.inlinks?.length || 0, 'desc')
  .limit(10);

if (bridges.length > 0) {
  dv.header(4, "🔀 Multi-Domain Bridge Notes");
  dv.table(
    ["Bridge Note", "Domains Connected", "Hub Strength"],
    bridges.map(p => {
      const tags = (p.file.tags || []).join(" ");
      let domains = [];
      if (tags.includes("stoicism") || tags.includes("stoic")) domains.push("🏺");
      if (tags.includes("epistemology") || tags.includes("epistemic")) domains.push("🔬");
      if (tags.includes("pragmatism")) domains.push("🔧");
      if (tags.includes("philosophy-of-mind")) domains.push("🧠");
      
      return [
        p.file.link,
        domains.join(" ↔ "),
        "⭐".repeat(Math.min(5, Math.ceil((p.file.inlinks?.length || 0) / 2)))
      ];
    })
  );
} else {
  dv.paragraph("*Create notes with multiple philosophy domain tags to see cross-connections here.*");
}
```

### 🔗 Key Integration Points

| Stoicism Concept | Connects To | Integration Insight |
|------------------|-------------|---------------------|
| [[Dichotomy of Control]] | [[Locus of Control]] | Psychological research validates Stoic distinction |
| [[Prosoche]] (Attention) | [[Metacognition]] | Both emphasize awareness of mental processes |
| [[Stoic Journaling]] | [[Daily Note Reflection]] | Same practice, different frameworks |
| [[Epistemic Assent]] | [[Epistemic Accountability]] | Stoic cognitive theory meets modern epistemology |

| Epistemology Concept | Connects To | Integration Insight |
|----------------------|-------------|---------------------|
| [[Epistemic Cognition]] | [[Metacognition]] | Cognitive science operationalizes epistemology |
| [[Evolutionary Epistemology]] | [[Pragmatism]] | Both naturalize knowledge processes |
| [[Confidence Calibration]] | [[Stoic Reservation]] | Ancient and modern uncertainty management |

---

## 🔄 Recent Activity & Review Queue

```dataviewjs
// 📅 RECENTLY MODIFIED PHILOSOPHY NOTES
const recentPhilosophy = dv.pages('#philosophy OR #stoicism OR #epistemology OR #pragmatism')
  .sort(p => p.file.mtime, 'desc')
  .limit(7);

dv.header(4, "📝 Recently Modified");
dv.table(
  ["Note", "Modified", "Maturity"],
  recentPhilosophy.map(p => [
    p.file.link,
    p.file.mtime ? p.file.mtime.toFormat("yyyy-MM-dd HH:mm") : "—",
    p.maturity || "—"
  ])
);
```

```dataviewjs
// ⏰ REVIEW QUEUE - Notes due for review
const today = dv.date("today");
const reviewQueue = dv.pages('#philosophy OR #stoicism OR #epistemology OR #pragmatism')
  .filter(p => {
    if (!p["next-review"]) return false;
    const reviewDate = dv.date(p["next-review"]);
    return reviewDate && reviewDate <= today;
  })
  .sort(p => dv.date(p["next-review"]), 'asc')
  .limit(10);

if (reviewQueue.length > 0) {
  dv.header(4, "⚠️ Review Queue (Past Due)");
  dv.table(
    ["Note", "Review Date", "Days Overdue"],
    reviewQueue.map(p => {
      const reviewDate = dv.date(p["next-review"]);
      const daysOverdue = Math.floor((today - reviewDate) / (1000 * 60 * 60 * 24));
      return [
        p.file.link,
        reviewDate.toFormat("yyyy-MM-dd"),
        daysOverdue + " days"
      ];
    })
  );
} else {
  dv.paragraph("✅ *No philosophy notes currently due for review.*");
}
```

---

## 🌱 Seedlings & Development Queue

```dataviewjs
// 🌱 SEEDLING NOTES - Underdeveloped concepts needing attention
const seedlings = dv.pages('#philosophy OR #stoicism OR #epistemology OR #pragmatism')
  .filter(p => p.maturity === "seedling" || p.maturity === "needs-review")
  .sort(p => p.file.ctime, 'asc');

if (seedlings.length > 0) {
  dv.header(4, "🌱 Seedlings Awaiting Development");
  dv.table(
    ["Note", "Created", "Current Confidence", "Suggested Action"],
    seedlings.map(p => {
      const linkCount = (p.file.outlinks?.length || 0);
      let suggestion = "Add connections";
      if (linkCount < 3) suggestion = "🔗 Needs more links";
      else if (!p.source) suggestion = "📚 Add sources";
      else suggestion = "✍️ Expand content";
      
      return [
        p.file.link,
        p.file.ctime ? p.file.ctime.toFormat("yyyy-MM-dd") : "—",
        p.confidence || "speculative",
        suggestion
      ];
    })
  );
} else {
  dv.paragraph("🌳 *All philosophy notes are developing or evergreen!*");
}
```

---

## 🛠️ Quick Actions

> [!helpful-tip] Meta Bind Integration
> Use these buttons to quickly create new philosophy notes or navigate to related hubs.

```meta-bind-button
label: "🏺 New Stoic Note"
style: primary
action:
  type: templaterCreateNote
  templateFile: "_templates/philosophy-note-template"
  folderPath: "Philosophy/Stoicism"
  fileName: "stoic-{{date:YYYYMMDD}}"
```

```meta-bind-button
label: "🔬 New Epistemology Note"
style: default
action:
  type: templaterCreateNote
  templateFile: "_templates/philosophy-note-template"
  folderPath: "Philosophy/Epistemology"
  fileName: "epistemic-{{date:YYYYMMDD}}"
```

```meta-bind-button
label: "📊 Open Dashboard"
style: default
action:
  type: open
  link: "[[pkb-dashboard]]"
```

---

## 📚 Recommended Reading Path

> [!methodology-and-sources] Learning Progression
> For newcomers to practical philosophy, this sequence builds understanding systematically:

**Foundation Layer:**
1. [[Stoicism]] → [[Dichotomy of Control]] → [[Locus of Control]]
2. [[Epistemology]] → [[Epistemic Accountability]]
3. [[Pragmatism]] → Evaluate philosophy by practical results

**Application Layer:**
1. [[Stoic Philosophy]] → Daily practice techniques
2. [[Socratic Method]] → [[Socratic Thinking]]
3. [[Epistemic Cognition]] → PKB quality validation

**Integration Layer:**
1. Connect Stoic practices to [[daily notes|Daily Note]] routines
2. Apply epistemic principles to [[source evaluation|source quality]]
3. Use pragmatic criteria to [[system design|refine PKB architecture]]

---

## 🔗 Related MOCs & Hubs

> [!network] Knowledge Graph Position
> This MOC connects to broader knowledge domains:

- **Up:** [[Home]] → [[Knowledge MOC]]
- **Lateral:** 
  - [[cognitive-science-moc]] — *Psychology of philosophical practice*
  - [[pkb-&-pkm-moc]] — *System design philosophy*
  - [[learning-theory-moc]] — *Education philosophy*
- **Down:** 
  - [[stoicism|Stoicism Index]]
  - [[epistemology|Epistemology Index]]

```dataviewjs
// 🔗 ORPHAN DETECTION - Philosophy notes not linked from this MOC
const allPhilosophy = dv.pages('#philosophy OR #stoicism OR #epistemology OR #pragmatism');
const currentOutlinks = dv.current().file.outlinks.map(l => l.path);

const orphans = allPhilosophy.filter(p => {
  return !currentOutlinks.includes(p.file.path);
});

if (orphans.length > 0) {
  dv.header(4, "🔍 Discovered Notes Not Yet Linked");
  dv.paragraph("*These philosophy notes exist but aren't linked from this MOC:*");
  dv.list(orphans.limit(10).map(p => p.file.link));
  if (orphans.length > 10) {
    dv.paragraph(`*…and ${orphans.length - 10} more.*`);
  }
}
```

---

## 📈 Review System

> [!important] Review Schedule
> - **Next Review**: `= this.next-review`
> - **Review Frequency**: Monthly (MOC-level review)
> - **Review Focus**:
>   - Add newly created philosophy notes
>   - Update cross-domain connections
>   - Promote matured seedlings
>   - Archive deprecated concepts

**Review Checklist:**
- [ ] All philosophy notes linked appropriately?
- [ ] Cross-domain bridges identified?
- [ ] Seedlings reviewed for development?
- [ ] DataviewJS queries returning expected results?
- [ ] New concepts from reading added?

---

## 🏷️ Tags & Classification

**Primary Tags:** `= this.tags`
**Type:** `= this.type`
**Maturity:** `= this.maturity`
**Confidence:** `= this.confidence`

---

# 🔗 Related Topics for PKB Expansion

1. **[[Virtue Ethics]]**
   - *Connection*: The ethical framework underlying Stoic practice—arete as the goal of philosophical life
   - *Depth Potential*: Explore Aristotelian vs. Stoic virtue concepts
   - *Knowledge Graph Role*: Bridge between Stoicism and broader ethical theory

2. **[[Cognitive Behavioral Therapy]]**
   - *Connection*: Modern therapeutic approach heavily influenced by Stoic cognitive techniques
   - *Depth Potential*: Document specific Stoic-CBT technique parallels
   - *Knowledge Graph Role*: Connect ancient philosophy to contemporary psychology

3. **[[Phenomenology]]**
   - *Connection*: Philosophical examination of conscious experience relevant to both Stoicism and epistemology
   - *Depth Potential*: Husserl, Heidegger, and their relevance to self-knowledge
   - *Knowledge Graph Role*: Expand Philosophy of Mind branch

4. **[[Critical Thinking Frameworks]]**
   - *Connection*: Operationalized epistemology—practical methods for evaluating arguments and evidence
   - *Depth Potential*: Paul-Elder framework, argument mapping, fallacy identification
   - *Knowledge Graph Role*: Bridge epistemology to PKM practice

---

*Last updated: `= this.file.mtime`*
*Notes in domain: `$= dv.pages('#philosophy OR #stoicism OR #epistemology OR #pragmatism').length`*