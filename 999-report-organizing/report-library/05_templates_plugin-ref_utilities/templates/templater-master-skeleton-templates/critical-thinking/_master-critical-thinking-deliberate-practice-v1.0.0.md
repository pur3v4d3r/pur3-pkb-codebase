<%*
/* ═══════════════════════════════════════════════════════════════════════════
   CRITICAL THINKING — DELIBERATE PRACTICE TEMPLATE  v1.0.0
   ─────────────────────────────────────────────────────────────────────────
   PURPOSE  Force structured, framework-driven reasoning on any object of
            analysis (argument, decision, article, claim, belief) with
            integrated metacognitive scaffolding.

   FRAMEWORKS SUPPORTED
     1. Paul-Elder — 8 Elements + 9 Standards (the default, full)
     2. FRISCO     — Ennis 6-step rapid evaluation
     3. Delphi-6   — Facione's interpret/analyze/evaluate/infer/explain/self-regulate
     4. Toulmin    — Claim / Data / Warrant / Backing / Qualifier / Rebuttal
     5. SEE-I      — State / Elaborate / Exemplify / Illustrate
     6. Custom     — Free-form with metacognitive scaffolding only

   DEPENDENCIES  Templater (required) · Meta Bind (recommended) ·
                 Dataview (recommended for dashboard rollup)

   PLACEMENT  Output goes to:  03-notes/critical-thinking-practice/
              Filename:        YYYY-MM-DD_ct_<framework>_<slug>.md
   ═══════════════════════════════════════════════════════════════════════════ */

// ─── 1. Object of analysis ─────────────────────────────────────────────────
const subject = await tp.system.prompt(
  "What are you analyzing? (one-line subject)",
  ""
);
if (subject === null || subject.trim() === "") return;

// ─── 2. Object type ────────────────────────────────────────────────────────
const objectType = await tp.system.suggester(
  ["Argument",  "Claim / Belief", "Decision", "Article / Source",
   "Conversation / Debate", "Concept / Definition", "Policy proposal",
   "Personal reasoning", "Other"],
  ["argument",  "claim",          "decision", "article",
   "conversation",            "concept",              "policy",
   "personal",            "other"]
);
if (objectType === null) return;

// ─── 3. Framework selection ────────────────────────────────────────────────
const framework = await tp.system.suggester(
  ["Paul-Elder (full 8 elements + 9 standards) — depth",
   "FRISCO (Ennis 6-step) — fast triage",
   "Delphi-6 (Facione core skills)",
   "Toulmin (argument decomposition)",
   "SEE-I (concept elaboration)",
   "Custom / Free-form (metacognition only)"],
  ["paul-elder", "frisco", "delphi", "toulmin", "see-i", "custom"]
);
if (framework === null) return;

// ─── 4. Question type (Paul-Elder Element 2) ──────────────────────────────
const questionType = await tp.system.suggester(
  ["Factual (empirically settleable)",
   "Conceptual (definitional / logical)",
   "Evaluative (requires value judgment)",
   "Policy (action-oriented)",
   "Mixed / Unclear"],
  ["factual", "conceptual", "evaluative", "policy", "mixed"]
);
if (questionType === null) return;

// ─── 5. Stakes / Why does this matter? ─────────────────────────────────────
const stakes = await tp.system.suggester(
  ["Low — exploratory practice",
   "Medium — informs a real decision",
   "High — significant consequences",
   "Critical — high-stakes / irreversible"],
  ["low", "medium", "high", "critical"]
);
if (stakes === null) return;

// ─── 6. Filename + move ────────────────────────────────────────────────────
const slug = subject
  .toLowerCase()
  .replace(/[^a-z0-9\s-]/g, "")
  .replace(/\s+/g, "-")
  .substring(0, 50);
const date  = tp.date.now("YYYY-MM-DD");
const fname = `${date}_ct_${framework}_${slug}`;
await tp.file.rename(fname);
await tp.file.move(`/03-notes/critical-thinking-practice/${fname}`);

// Capture for body
tR += "";
%>---
title: "<% subject %>"
aliases: []
tags:
  - critical-thinking
  - deliberate-practice
  - <% framework %>
  - <% objectType %>-analysis
  - metacognition
created: <% tp.date.now("YYYY-MM-DD") %>
modified: <% tp.date.now("YYYY-MM-DD") %>
type: critical-thinking-session
framework: <% framework %>
object-type: <% objectType %>
question-type: <% questionType %>
stakes: <% stakes %>
status: in-progress
confidence-pre: 
confidence-post: 
# Intellectual Standards self-ratings (1-5) — filled at end of session
rating-clarity: 
rating-accuracy: 
rating-precision: 
rating-relevance: 
rating-depth: 
rating-breadth: 
rating-logic: 
rating-significance: 
rating-fairness: 
# Computed at session close
overall-rigor-score: 
duration-minutes: 
related: []
cssclasses:
  - critical-thinking
---

# <% subject %>

> [!abstract] Session Overview
> **Object type:** <% objectType %>  ·  **Framework:** <% framework %>  ·  **Question type:** <% questionType %>  ·  **Stakes:** <% stakes %>
> **Session start:** <% tp.date.now("YYYY-MM-DD HH:mm") %>
>
> This is a [[Deliberate Practice]] session in [[Critical Thinking]] following the [[<% framework === "paul-elder" ? "Paul-Elder Framework" : framework === "frisco" ? "FRISCO Model" : framework === "delphi" ? "Delphi Consensus" : framework === "toulmin" ? "Toulmin Argument Model" : framework === "see-i" ? "SEE-I Method" : "Critical Thinking" %>]]. Reason through each section deliberately. Do not skip. Productive friction is the point.

---

## 0 · Pre-Analysis Snapshot — Calibration

> [!attention] Capture your starting state *before* analysis begins.
> This is essential for measuring whether structured reasoning actually changed your view — the [[Confirmation Bias]] check.

**Initial position / gut answer (in one sentence):**
> 

**Confidence in initial position (1-5):**
`INPUT[number(minValue(1), maxValue(5)):confidence-pre]`

**Emotional charge around this topic (1-5, 1=neutral, 5=highly invested):**
> 

**What outcome am I motivated to reach? (Be honest — name it.)**
> 

**Time-box for this session (minutes):**
> 

---

<%* if (framework === "paul-elder") { %>
## 1 · The Eight Elements of Thought — [[Paul-Elder Framework]]

> [!definition] Method
> Address each [[Elements of Thought|element]] in turn. Every act of reasoning has all eight — making them explicit is what distinguishes critical from automatic thinking.

---

### 1.1 · Purpose — *what is the reasoning for?*

[**Stated-Purpose**:: ]

- What am I trying to accomplish here?
- Is my stated purpose my *real* purpose, or is there a hidden agenda?
- Could the purpose be unrealistic or unethical?

> 

---

### 1.2 · Question at Issue — *what precise question am I answering?*

[**Central-Question**:: ]

- Is this the *right* question, or a substitute?
- Is the question loaded, ambiguous, or actually multiple questions?
- What would count as a satisfactory answer?
- Type: <% questionType %>

> 

---

### 1.3 · Information — *what data am I using?*

[**Key-Evidence**:: ]

- What is the *source* of each piece? Reliability?
- What information am I *not* using that I should be?
- Have I distinguished facts from interpretations?
- What evidence would *disconfirm* my view? Have I sought it?

**Supporting evidence:**
- 

**Disconfirming evidence I deliberately searched for:**
- 

**Information gaps I'm aware of:**
- 

---

### 1.4 · Interpretation & Inference — *what conclusions am I drawing?*

[**Primary-Inference**:: ]

- How exactly did I move from this information to this conclusion?
- Are there other reasonable inferences from the same data?
- Am I over-inferring (stronger claim than data warrants)?
- Am I confusing inference with observation?

**My inference chain (step → step → conclusion):**
1. 
2. 
3. 

**Alternative inferences I rejected (and why):**
- 

---

### 1.5 · Concepts — *what ideas/theories frame my thinking?*

[**Key-Concept**:: ]

- What key concepts am I using? Are they defined precisely?
- Am I using a concept in its technical sense or popular sense?
- What assumptions are *embedded* in these concepts?
- Am I [[Equivocation|equivocating]] — same word, shifting meaning?

**Concepts in play (with my working definitions):**
- **Concept A**: 
- **Concept B**: 

---

### 1.6 · Assumptions — *what am I taking for granted?*

> [!warning] Highest-leverage move
> Unexamined [[Assumptions]] are the most dangerous element. They drive conclusions invisibly.

[**Load-Bearing-Assumption**:: ]

**Assumptions I'm aware of:**
- 

**Assumptions that, if false, would collapse my conclusion:**
- 

**Assumptions of those who disagree with me:**
- 

---

### 1.7 · Implications & Consequences — *what follows from this?*

[**Key-Implication**:: ]

- If I accept this, what *else* must I accept?
- Short-term vs. long-term consequences?
- What happens if everyone reasoned/acted this way?
- Am I willing to accept the consequences?

**Logical implications (what is entailed):**
- 

**Practical consequences (what would result):**
- 

---

### 1.8 · Point of View — *from where am I reasoning?*

[**My-Standpoint**:: ]

- What experiences/values/training shape my perspective?
- What might I be missing *because* of this perspective?
- How would someone who strongly disagrees characterize this?
- Am I exhibiting [[Egocentrism]] or [[Sociocentrism]]?

**My standpoint and what it makes visible:**
> 

**Alternative standpoint #1 (steelmanned):**
> 

**Alternative standpoint #2 (steelmanned):**
> 

---

## 2 · The Nine Intellectual Standards — Self-Audit

> [!attention] Rate each standard 1-5 honestly using the Meta Bind sliders below.
> 1 = failed this standard · 3 = adequate · 5 = exemplary

| Standard | Rating | Brief justification |
|---|---|---|
| **Clarity** — is my meaning unambiguous? | `INPUT[slider(minValue(1), maxValue(5), addLabels):rating-clarity]` | |
| **Accuracy** — does it correspond to reality? | `INPUT[slider(minValue(1), maxValue(5), addLabels):rating-accuracy]` | |
| **Precision** — sufficient specificity & detail? | `INPUT[slider(minValue(1), maxValue(5), addLabels):rating-precision]` | |
| **Relevance** — bears on the question? | `INPUT[slider(minValue(1), maxValue(5), addLabels):rating-relevance]` | |
| **Depth** — addresses complexity? | `INPUT[slider(minValue(1), maxValue(5), addLabels):rating-depth]` | |
| **Breadth** — multiple perspectives considered? | `INPUT[slider(minValue(1), maxValue(5), addLabels):rating-breadth]` | |
| **Logic** — internally consistent / follows? | `INPUT[slider(minValue(1), maxValue(5), addLabels):rating-logic]` | |
| **Significance** — focused on what matters most? | `INPUT[slider(minValue(1), maxValue(5), addLabels):rating-significance]` | |
| **Fairness** — free from bias / self-interest? | `INPUT[slider(minValue(1), maxValue(5), addLabels):rating-fairness]` | |

**Weakest standard (focus area for next session):**
> 

<%* } else if (framework === "frisco") { %>
## 1 · FRISCO Analysis — [[Robert Ennis|Ennis]] 6-Step Model

### F · Focus — *what is the main question/issue/conclusion?*
[**Focus**:: ]
> 

### R · Reasons — *what reasons are offered in support?*
[**Reasons**:: ]
- 
- 
- 

### I · Inference — *is the reasoning from reasons to conclusion acceptable?*
[**Inference-Quality**:: ]
> 

### S · Situation — *physical/social/intellectual context?*
[**Situation**:: ]
> 

### C · Clarity — *are key terms clear?*
[**Clarity-Issues**:: ]
- Term 1: 
- Term 2: 

### O · Overview — *does the whole hold up under integrated review?*
[**Overall-Verdict**:: ]
> 

<%* } else if (framework === "delphi") { %>
## 1 · Delphi Six Core Skills — [[Facione]]

### Interpretation — *categorize, decode significance, clarify meaning*
> 

### Analysis — *examine ideas, identify arguments/reasons/claims*
> 

### Evaluation — *assess claims and arguments*
> 

### Inference — *query evidence, conjecture alternatives, draw conclusions*
> 

### Explanation — *state results, justify procedures, present arguments*
> 

### Self-Regulation — *self-examine and self-correct*
> 

<%* } else if (framework === "toulmin") { %>
## 1 · Toulmin Argument Map — [[Stephen Toulmin|Toulmin]]

### Claim — *what conclusion is being argued for?*
[**Claim**:: ]
> 

### Data / Grounds — *what evidence supports the claim?*
[**Data**:: ]
- 

### Warrant — *what principle authorizes moving from data to claim?*
[**Warrant**:: ]
> 

### Backing — *what supports the warrant itself?*
[**Backing**:: ]
> 

### Qualifier — *what hedges/limits the claim? (probably, usually, often)*
[**Qualifier**:: ]
> 

### Rebuttal — *under what conditions would the claim fail?*
[**Rebuttal**:: ]
> 

<%* } else if (framework === "see-i") { %>
## 1 · SEE-I Elaboration — [[Paul-Elder Framework|Paul-Elder]] Conceptual Tool

### S · State — *state the idea in one clear sentence*
[**Statement**:: ]
> 

### E · Elaborate — *explain it in your own words, in depth*
> 

### E · Exemplify — *provide a concrete example*
> 

### I · Illustrate — *use an analogy, metaphor, or diagram*
> 

<%* } else { %>
## 1 · Free-Form Analysis

> [!note] No fixed framework chosen — apply reasoning as the situation requires.
> Then complete the metacognitive sections (mandatory).

> 

<%* } %>

---

## 3 · Counter-Argument & Steelman

> [!important] Mandatory regardless of framework.
> Confront the strongest possible objection to your position. If you cannot articulate it, you do not yet understand the issue.

**Strongest opposing position (steelmanned — make it as strong as you can):**
> 

**Why this opposing position is harder to dismiss than I initially thought:**
> 

**How does this objection change (or fail to change) my conclusion?**
> 

---

## 4 · Common Cognitive Biases — Active Check

> [!warning] Identify any bias you may have committed in this session.
> Honest self-detection is the first defense.

- [ ] [[Confirmation Bias]] — sought only confirming evidence
- [ ] [[Anchoring Bias]] — over-weighted first information
- [ ] [[Availability Heuristic]] — relied on what came to mind easily
- [ ] [[Motivated Reasoning]] — reasoned toward preferred conclusion
- [ ] [[Sunk Cost Fallacy]] — continued because of past investment
- [ ] [[Dunning-Kruger Effect]] — overestimated competence in this domain
- [ ] [[Bandwagon Effect]] — accepted because others do
- [ ] [[Halo Effect]] — let one positive trait color overall judgment
- [ ] [[Fundamental Attribution Error]] — over-attributed to disposition vs. situation
- [ ] [[Hindsight Bias]] — "I knew it all along"
- [ ] None detected (justify below)

**Bias detected? Brief description and corrective action:**
> 

---

## 5 · Metacognitive Reflection — [[Metacognition]]

> [!key-claim] The session is incomplete without this section.
> [[Metacognitive Monitoring]] is what converts practice into [[Deliberate Practice]].

### 5.1 · What was hardest about this analysis?
> 

### 5.2 · What did I notice about my *own thinking process*?
> 

### 5.3 · Where did I cut corners or rush?
> 

### 5.4 · Did the framework expose anything I would have missed without it?
> 

### 5.5 · What [[Intellectual Virtues|intellectual virtue]] was most tested?
- [ ] [[Intellectual Humility]]
- [ ] [[Intellectual Courage]]
- [ ] [[Intellectual Empathy]]
- [ ] [[Intellectual Autonomy]]
- [ ] [[Intellectual Integrity]]
- [ ] [[Intellectual Perseverance]]
- [ ] [[Confidence in Reason]]
- [ ] [[Fairmindedness]]

**Why:** 
> 

### 5.6 · What will I do *differently* in my next practice session?
> 

---

## 6 · Post-Analysis Calibration

**Updated position (in one sentence):**
> 

**Confidence in updated position (1-5):**
`INPUT[number(minValue(1), maxValue(5)):confidence-post]`

**Did my position change? If so, what specifically moved me?**
> 

**If position did NOT change, can I articulate *why* the analysis failed to move me — and is that reason itself sound?**
> 

---

## 7 · Session Close

**Session end:** <% tp.date.now("YYYY-MM-DD HH:mm") %>
**Duration (minutes):** `INPUT[number:duration-minutes]`

```meta-bind-button
label: "Mark Session Complete"
style: primary
actions:
  - type: updateMetadata
    bindTarget: status
    evaluate: "'complete'"
  - type: updateMetadata
    bindTarget: modified
    evaluate: "moment().format('YYYY-MM-DD')"
```

```meta-bind-button
label: "Flag for Re-Review"
style: destructive
actions:
  - type: updateMetadata
    bindTarget: status
    evaluate: "'needs-re-review'"
```

---

## 8 · Computed Rigor Score (auto-updates from ratings)

```dataviewjs
const p = dv.current();
const r = ["rating-clarity","rating-accuracy","rating-precision","rating-relevance",
           "rating-depth","rating-breadth","rating-logic","rating-significance","rating-fairness"]
  .map(k => Number(p[k])).filter(v => !isNaN(v) && v > 0);
if (r.length === 0) { dv.paragraph("*Rate the standards above to see your rigor score.*"); }
else {
  const avg = (r.reduce((a,b)=>a+b,0) / r.length).toFixed(2);
  const band = avg >= 4.5 ? "🟢 Exemplary" : avg >= 3.5 ? "🟡 Strong" : avg >= 2.5 ? "🟠 Adequate" : "🔴 Needs work";
  dv.paragraph(`**Overall rigor:** ${avg} / 5 — ${band}  (n=${r.length} standards rated)`);
}
```

---

# 🔗 Related Topics for PKB Expansion

## 🎯 Core Extensions
1. **[[Paul-Elder Framework]]** — full reference for elements, standards, and intellectual virtues used in this session.
2. **[[Metacognition]]** — the monitoring discipline that converts practice into deliberate practice.

## 🌐 Cross-Domain Connections
3. **[[Dual-Process Theory]]** — System 1 vs. System 2 framing for *why* structured analysis is necessary.
4. **[[Cognitive Biases]]** — catalog of failure modes this template guards against.

## 📚 Foundational Prerequisites
- **[[Deliberate Practice]]** — Ericsson's framework underwriting why structured friction produces growth.
- **[[Critical Thinking]]** — umbrella construct.

## 🔄 Related MOCs
- **[[Critical Thinking Practice MOC]]**
- **[[Metacognition MOC]]**
