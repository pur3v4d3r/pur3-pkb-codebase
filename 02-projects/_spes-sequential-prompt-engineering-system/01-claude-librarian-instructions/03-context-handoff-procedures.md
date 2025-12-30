---
tags: #spes #claude-instructions #context-management #multi-turn
aliases: [Context Handoff, Turn Management, Context Procedures]
status: evergreen
certainty: ^verified
created: 2025-12-16
---

# Context-Handoff Procedures

> [!abstract] Purpose
> Detailed procedures for managing context flow between turns in multi-turn sequential prompt workflows. Prevents context dilution, instruction drift, and attention degradation.

---

## 🎯 THE CONTEXT PROBLEM

### What is Context Dilution?

As conversations grow longer, the model's attention to earlier instructions weakens:

```
Turn 1 (1k tokens total):    Instruction adherence: 95%
Turn 5 (10k tokens total):   Instruction adherence: 80%
Turn 10 (25k tokens total):  Instruction adherence: 60%
Turn 15 (40k tokens total):  Instruction adherence: 40%
```

**Symptoms**:
- Format requirements forgotten
- Tone shifts unexpectedly
- Constraints violated
- Scope creep between turns
- Repetition of earlier content

**Root Causes**:
1. **Attention Distribution**: Model attention spreads across all tokens
2. **Recency Bias**: Recent instructions override distant ones
3. **Context Noise**: Irrelevant history dilutes signal

---

## 🧰 HANDOFF STRATEGIES

### Strategy 1: Semantic Anchoring (Anti-Drift)

**Purpose**: Refresh critical instructions at every turn

**Implementation**:
```markdown
[PRIMARY PROMPT CONTENT]

---
CONSTRAINTS (RE-INJECTED):
- Tone: [Tone requirement]
- Format: [Format requirement]
- Metadata: [Metadata requirement]
- Forbidden: [What not to do]
---
```

**When to Use**: ALL multi-turn workflows (default)

**Example**:
```
TURN 1:
"Generate Section 1 of technical guide.

---
CONSTRAINTS:
- Tone: Academic, rigorous
- Format: Markdown with wiki-links
- Metadata: Link all technical terms
- Forbidden: Do not summarize
---"

TURN 2:
"Generate Section 2 of technical guide.
Context: Section 1 covered [summary].

---
CONSTRAINTS:
- Tone: Academic, rigorous
- Format: Markdown with wiki-links
- Metadata: Link all technical terms
- Forbidden: Do not summarize
---"

[Constraints re-injected at EVERY turn]
```

**Component**: [[semantic-anchoring-footer]]

---

### Strategy 2: Context Windowing (Compression)

**Purpose**: Keep only relevant history in context

**Windowing Techniques**:

#### A. Sliding Window
Keep only last N turns in context:
```
Turn 5: Keep turns 3, 4, 5 (drop 1, 2)
Turn 6: Keep turns 4, 5, 6 (drop 1, 2, 3)
```
**Best for**: Independent sections, weak dependencies

#### B. Summary Window
Compress old turns into summary:
```
Turn 1-3: Full content (8k tokens)
Turn 4: "Turns 1-3 summary: [500 token summary]" + Turn 4 full content
```
**Best for**: Key points sufficient, details unneeded

#### C. Hierarchical Window
Keep turn outlines + full recent history:
```
Context at Turn 7:
- Turn 1: [Title + 1-sentence summary]
- Turn 2: [Title + 1-sentence summary]
- Turn 3: [Title + 1-sentence summary]
- Turn 4: [Title + 1-sentence summary]
- Turn 5: [Full content]
- Turn 6: [Full content]
- Turn 7: [Current]
```
**Best for**: Need awareness of all topics but not details

**Implementation Decision Tree**:
```
Context size <15k tokens?
└─ NO compression needed

Context 15k-30k tokens?
└─ Use Hierarchical Window

Context >30k tokens?
├─ Weak dependencies between turns?
│   └─ Use Sliding Window (keep last 3-5 turns)
└─ Strong dependencies between turns?
    └─ Use Summary Window (compress old, keep recent)
```

---

### Strategy 3: Explicit State Management

**Purpose**: Track what the model "knows" at each turn

**State Document Template**:
```markdown
## WORKFLOW STATE (TURN N)

**Completed**:
- Turn 1: [Topic] → Key insight: [X]
- Turn 2: [Topic] → Key insight: [Y]
- Turn N-1: [Topic] → Key insight: [Z]

**Current Turn**: N
**Current Task**: [Specific task for this turn]
**Current Scope**: [What to include/exclude]

**Next Planned**:
- Turn N+1: [Upcoming task]
- Turn N+2: [Future task]

**Critical Carryover**:
- Terminology established: [List]
- Assumptions made: [List]
- Constraints active: [List]
```

**When to Use**: Complex workflows (>7 turns) with interdependencies

**Example**:
```
TURN 5 PROMPT:

## WORKFLOW STATE (TURN 5)

**Completed**:
- Turn 1: Attention Mechanism → Key insight: Query-key-value triplets
- Turn 2: Multi-head Attention → Key insight: Parallel attention pathways
- Turn 3: Positional Encoding → Key insight: Sin/cos frequency-based
- Turn 4: Feed-Forward Layers → Key insight: Position-wise transformation

**Current Turn**: 5
**Current Task**: Training Objectives
**Current Scope**: Loss functions, optimization, convergence ONLY

**Critical Carryover**:
- Terminology: Using "attention heads" not "attention layers"
- Assumptions: Targeting technical audience, math fluency assumed
- Constraints: Include mathematical notation, link technical terms

Generate Section 5: Training Objectives...
[Main prompt content]
```

**Components**: [[workflow-state-tracker]], [[context-state-header]]

---

### Strategy 4: Turn Isolation (Zero Handoff)

**Purpose**: Completely independent turns, no context carryover

**When to Use**:
- Atomic note creation (each note independent)
- Parallel analyses (no dependencies)
- Risk of context contamination

**Implementation**:
```markdown
OPTION A: Explicit Instruction
"Ignore all previous turns. This task is independent.
[Task details]"

OPTION B: New Conversation
[Actually start fresh conversation in UI]
[No context carryover possible]
```

**Example**:
```
TURN 1: Create atomic note for [[Attention Mechanism]]
[Model has no knowledge of other concepts]

[NEW CONVERSATION]

TURN 2: Create atomic note for [[Positional Encoding]]
[Model has no memory of Turn 1]
[No risk of cross-contamination]
```

**Trade-off**: Maximum isolation, but no synthesis possible

---

## 🔄 HANDOFF DECISION MATRIX

| Workflow Type | Context Strategy | Window Size | Re-anchoring Frequency |
|---------------|------------------|-------------|------------------------|
| **Least-to-Most** (5-7 turns) | Summary Window | Last 3 turns full | Every turn |
| **Chain-of-Verification** (4 turns) | Full Context | All turns | Turn 2, Turn 4 |
| **Recursive Expansion** (6-10 turns) | Sliding Window | Last 2 turns | Every turn |
| **Parallel Convergence** (3-5 turns) | Turn Isolation → Summary | Isolation, then all | At synthesis turn |
| **Staged Generation** (2-3 turns) | Full Context | All turns | Optional |

---

## 🛠️ HANDOFF EXECUTION CHECKLIST

### Before Starting Workflow

- [ ] **Estimate total turns**: How many turns will this workflow require?
- [ ] **Estimate context growth**: ~Tokens per turn × turn count = total context
- [ ] **Select handoff strategy**: Based on dependencies and context size
- [ ] **Prepare state template**: If using explicit state management
- [ ] **Prepare anchoring footer**: If using semantic anchoring

### At Each Turn

- [ ] **Check context size**: Running total of tokens
- [ ] **Apply handoff strategy**: Execute chosen compression/windowing
- [ ] **Re-inject constraints**: Use semantic anchoring footer
- [ ] **Update state**: If using explicit state management
- [ ] **Verify scope**: Is this turn staying within defined scope?

### Warning Signs (Adjust Strategy)

- ⚠️ **Instruction drift detected**: Model forgetting constraints
  - **Action**: Increase re-anchoring frequency or switch to explicit state
- ⚠️ **Context >25k tokens**: Risk of attention degradation
  - **Action**: Switch to Summary Window or Sliding Window
- ⚠️ **Repetition across turns**: Model re-stating earlier content
  - **Action**: More aggressive compression or turn isolation
- ⚠️ **Scope creep**: Turns bleeding into each other
  - **Action**: Stricter scope definitions, consider turn isolation

---

## 🧪 ADVANCED TECHNIQUES

### Technique 1: Context Forking

**Use Case**: Explore multiple paths from same starting point

```
TURN 1: Generate base content
         ↓
    [Fork context]
    ↙           ↘
TURN 2a:        TURN 2b:
Path A          Path B
(context       (context
from T1)       from T1)
```

**Implementation**: User maintains two conversation threads

**Example**:
- Turn 1: Overview of algorithm
- Turn 2a: Optimize for speed (fork)
- Turn 2b: Optimize for accuracy (fork)
- Later: Compare outcomes

### Technique 2: Context Checkpointing

**Use Case**: Save state before risky operations

```
TURN 3: Verified good state ← CHECKPOINT
TURN 4: Risky generation (might fail)
  ↓
  Failure detected
  ↓
TURN 5: Restore from Turn 3, try alternative approach
```

**Implementation**: User manually tracks "good" state, references in recovery turn

### Technique 3: Differential Context (Delta Encoding)

**Use Case**: Long workflows where only changes matter

```
TURN 1: Full context (5k tokens)
TURN 2: "Changes from Turn 1: [200 tokens delta]" + new content
TURN 3: "Changes from Turn 2: [150 tokens delta]" + new content
```

**Implementation**: User summarizes what changed, not full state

**Example**:
```
TURN 5 PROMPT:
"Changes from Turn 4:
- New terminology introduced: 'gradient clipping'
- Assumption added: Batch size >32
- Constraint modified: Now require 2 examples per concept

Generate Turn 5 content with above changes applied..."
```

---

## 📊 HANDOFF QUALITY METRICS

### How to Measure Handoff Effectiveness

**Metric 1: Instruction Adherence Rate**
- Check: Does output follow all constraints?
- Calculate: (Constraints met / Total constraints) × 100%
- Target: >90% through entire workflow

**Metric 2: Context Efficiency**
- Check: Tokens in context vs tokens actually used
- Calculate: (Useful context / Total context) × 100%
- Target: >60% (low ratio = wasted context)

**Metric 3: Drift Distance**
- Check: How much does later output differ from early constraints?
- Measure: Qualitative assessment of tone/format/scope consistency
- Target: No detectable drift

**Metric 4: Turn Independence (when appropriate)**
- Check: Could this turn stand alone?
- Measure: Remove context, re-read turn output
- Target: Turn is coherent without context (if isolation strategy used)

---

## 🔗 Related Procedures

- [[00-librarian-core-identity]] → Context as memory system
- [[02-sequential-workflow-protocols]] → When to use which handoff strategy
- [[04-quality-assurance-checklist]] → Validating handoff quality

---

## 📚 QUICK REFERENCE: Handoff Strategies

| Strategy | Context Size | Turns | Best For |
|----------|-------------|-------|----------|
| **Semantic Anchoring** | Any | Any | Default, always use |
| **Full Context** | <15k | <6 | Simple workflows |
| **Sliding Window** | 15-30k | 6-10 | Weak dependencies |
| **Summary Window** | >30k | >10 | Strong dependencies |
| **Hierarchical Window** | 20-40k | 8-15 | Awareness of all topics |
| **Turn Isolation** | Any | Any | Independent tasks |
| **Explicit State** | >20k | >7 | Complex workflows |

---

*Context Handoff Procedures Version: 1.0 | Last Updated: 2025-12-16*
