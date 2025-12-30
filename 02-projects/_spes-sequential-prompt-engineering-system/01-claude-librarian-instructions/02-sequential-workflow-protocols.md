---
tags: #spes #claude-instructions #workflows #decomposition #sequential
aliases: [Workflow Protocols, Sequential Prompting SOP, Decomposition Procedures]
status: evergreen
certainty: ^verified
created: 2025-12-16
---

# Sequential Workflow Protocols

> [!abstract] Purpose
> Standard procedures for analyzing problems, recommending decomposition strategies, and orchestrating multi-turn sequential prompt workflows.

---

## 🎯 CORE PRINCIPLE

**Complex problems should be decomposed into sequential workflows, not forced into single prompts.**

One-shot prompts fail at:
- Long-form content (output token limits)
- Multi-faceted analysis (attention dilution)
- High-accuracy requirements (verification impossible)
- Context-heavy tasks (context window constraints)

Sequential workflows succeed by:
- Breaking problems into atomic sub-tasks
- Isolating context per turn (reducing noise)
- Enabling verification between steps
- Building progressively on validated outputs

---

## 📊 PROBLEM ANALYSIS FRAMEWORK

### Step 1: Classify the Problem Type

Use this taxonomy to identify the problem:

#### **Generation Problems** (Creating new content)
- **Long-Form Generation**: >2000 tokens output needed
  - Examples: Essays, reports, comprehensive guides
  - Recommended workflow: [[least-to-most-prompting]], [[recursive-expansion-loop]]
- **Technical Explanation**: High accuracy, examples, math
  - Examples: Algorithm explanations, scientific concepts
  - Recommended workflow: [[chain-of-verification]]
- **Creative Writing**: Style consistency, narrative flow
  - Examples: Stories, marketing copy, world-building
  - Recommended workflow: [[staged-generation]]

#### **Analysis Problems** (Understanding existing content)
- **Comparative Analysis**: Multiple items, structured comparison
  - Examples: Tool comparisons, research synthesis
  - Recommended workflow: [[parallel-convergence]]
- **Research Synthesis**: Multiple sources, coherent narrative
  - Examples: Literature reviews, meta-analysis
  - Recommended workflow: [[least-to-most-prompting]] + [[chain-of-verification]]
- **Critical Evaluation**: Deep analysis, evidence-based claims
  - Examples: Code review, argument analysis
  - Recommended workflow: [[chain-of-verification]]

#### **Transformation Problems** (Modifying existing content)
- **Format Conversion**: Restructure while preserving meaning
  - Examples: Article → slides, code → documentation
  - Recommended workflow: [[strict-isolation]] (each section independent)
- **Enhancement**: Improve quality without changing core content
  - Examples: Add examples, improve clarity, expand brevity
  - Recommended workflow: [[recursive-expansion-loop]]

#### **PKB Problems** (Vault-specific operations)
- **Note Atomization**: Break large note into concept atoms
  - Recommended workflow: [[strict-isolation]] per concept
- **MOC Creation**: Synthesize scattered notes into coherent map
  - Recommended workflow: [[parallel-convergence]]
- **Graph Enrichment**: Add links, metadata, connections
  - Recommended workflow: [[sequential-building]]

### Step 2: Identify Constraints

Check for these constraint types:

```markdown
OUTPUT CONSTRAINTS
├─ Token Limit: Will output exceed ~4000 tokens?
├─ Format Requirements: Specific structure, sections, template?
└─ Quality Bar: Accuracy critical? Examples required?

INPUT CONSTRAINTS
├─ Context Size: Multiple long documents as input?
├─ Context Type: Mixed types (code + text + data)?
└─ Context Complexity: Highly technical or specialized?

PROCESS CONSTRAINTS
├─ Verification Needed: Must catch errors/hallucinations?
├─ Iteration Required: Refine through multiple passes?
└─ Dependency Chain: Task B depends on quality of Task A?
```

### Step 3: Decomposition Decision

```
Is the problem SIMPLE?
├─ Output <1000 tokens
├─ Single aspect to address
├─ No verification needed
├─ Standard format
└─ → USE ONE-SHOT PROMPT
    └─ Select appropriate components
    └─ Execute single prompt
    └─ Done

Is the problem MODERATE?
├─ Output 1000-3000 tokens
├─ 2-3 distinct aspects
├─ Verification helpful
├─ Some format complexity
└─ → USE STAGED GENERATION (2-3 turns)
    └─ Break into logical sections
    └─ Generate section 1 → review → section 2 → review
    └─ User assembles final output

Is the problem COMPLEX?
├─ Output >3000 tokens
├─ 4+ distinct aspects
├─ Verification critical
├─ High quality bar
└─ → USE FULL SEQUENTIAL WORKFLOW (4-10 turns)
    └─ Select workflow pattern (see WORKFLOW PATTERNS section)
    └─ Define sub-problems
    └─ Define context-handoff strategy
    └─ Execute workflow with verification gates
```

---

## 🔄 WORKFLOW PATTERNS

### Pattern 1: Least-to-Most Prompting

**When to Use**:
- Problem has clear hierarchical structure
- Sub-problems build on each other
- Final output is synthesis of parts

**Protocol**:
```markdown
TURN 1: Decomposition
Prompt: "Break [PROBLEM] into 5-7 sequential sub-problems.
        List them in logical order."
Output: Ordered list of sub-problems

TURN 2-N: Sequential Solving
For each sub-problem:
  Prompt: "Solve sub-problem N: [SUB-PROBLEM].
          Context from previous: [SUMMARY OF PREVIOUS SOLUTIONS]
          Focus strictly on this sub-problem. 800-1000 words."
  Output: Detailed solution to sub-problem N

TURN N+1: Integration (Optional, user may do manually)
Prompt: "Review the N solutions above. Identify:
        1. Gaps between solutions
        2. Contradictions to resolve
        3. Connections to strengthen"
```

**Component Selections**:
- Use: [[decomposition-enforcer]], [[scope-limiter]], [[context-carryover]]
- Avoid: [[comprehensive-coverage]] (fights against decomposition)

**Example Usage**:
- Problem: "Create comprehensive guide to transformer architecture"
- Sub-problems: 1) Attention mechanism, 2) Multi-head attention, 3) Positional encoding, 4) Feed-forward layers, 5) Training objectives, 6) Applications

### Pattern 2: Chain-of-Verification (CoVe)

**When to Use**:
- Accuracy is critical
- Hallucinations likely (technical content, rare facts)
- User needs confidence in output

**Protocol**:
```markdown
TURN 1: Draft Generation
Prompt: "Generate [OUTPUT] with [CONSTRAINTS]."
Output: Initial draft (likely contains errors)

TURN 2: Verification Question Generation
Prompt: "Review the text above. Generate 5-7 verification questions
        that would expose errors, oversimplifications, or hallucinations.
        Focus on factual accuracy and technical precision."
Output: List of verification questions

TURN 3: Independent Verification
Prompt: "Answer each verification question independently,
        WITHOUT referring to the original text.
        Use your knowledge to provide accurate answers."
Output: Verified answers (may contradict original)

TURN 4: Corrected Generation
Prompt: "Compare the original text to the verified answers.
        Rewrite the text, correcting errors and incorporating
        verified details. Expand where original was oversimplified."
Output: Corrected, verified content
```

**Component Selections**:
- Use: [[skeptical-reviewer]], [[technical-precision]], [[evidence-based]]
- Avoid: [[confident-tone]] (conflicts with self-doubt in Turn 2)

**Example Usage**:
- Problem: "Explain quantum entanglement for technical audience"
- Risk: Easy to oversimplify or misstate Bell's theorem
- CoVe catches: "Can entanglement transmit information?" → Verification corrects

### Pattern 3: Recursive Expansion Loop

**When to Use**:
- Output is currently "tiny fraction" of needed depth
- Each paragraph could be its own section
- User wants maximum detail

**Protocol**:
```markdown
TURN 1: Seed Generation
Prompt: "Generate concise overview of [TOPIC].
        4-6 paragraphs, each covering distinct sub-topic."
Output: Overview (the "tiny fraction")

TURN 2-N: Paragraph Explosion
For each paragraph in overview:
  Prompt: "Take this paragraph:
          ---
          [PARAGRAPH TEXT]
          ---
          This paragraph is now the ABSTRACT for a new section.
          Expand it into 800-1000 words. Do not repeat the abstract.
          Instead, explode each concept within it.
          Include examples, edge cases, and technical depth."
  Output: Detailed expansion of single paragraph

TURN N+1: Cross-Reference Check
Prompt: "Review all N expanded sections. Identify:
        1. Concepts that appear in multiple sections (link them)
        2. Gaps between sections (what's missing?)
        3. Suggested order for final assembly"
```

**Component Selections**:
- Use: [[depth-enforcer]], [[example-rich]], [[no-summarization]]
- Avoid: [[conciseness]] (directly conflicts with expansion goal)

**Example Usage**:
- Problem: "LLM keeps giving 500-word summaries, need 5000-word guide"
- Solution: Generate 500-word overview → expand each of 5 paragraphs to 1000 words → 5000 total

### Pattern 4: Parallel Convergence

**When to Use**:
- Multiple independent analyses needed
- Results must be synthesized
- Analyses don't depend on each other

**Protocol**:
```markdown
TURN 1: Analysis Decomposition
Prompt: "Identify N independent dimensions to analyze [TOPIC].
        Example dimensions: Performance, Cost, Usability, Scalability."
Output: List of analysis dimensions

TURN 2-N: Parallel Analysis (can be done simultaneously in UI)
For each dimension:
  Prompt: "Analyze [TOPIC] solely on dimension: [DIMENSION].
          Ignore other dimensions. 600-800 words."
  Output: Focused analysis on single dimension

TURN N+1: Synthesis
Prompt: "Given the N analyses above, synthesize findings into:
        1. Overall assessment
        2. Trade-off matrix
        3. Recommendation based on context: [USER CONTEXT]"
Output: Integrated synthesis with recommendations
```

**Component Selections**:
- Use: [[dimensional-analysis]], [[synthesis-enforcer]], [[trade-off-matrix]]
- Avoid: [[holistic-view]] (conflicts with dimensional isolation)

**Example Usage**:
- Problem: "Compare tools A, B, C across multiple criteria"
- Dimensions: Performance, Ease-of-use, Ecosystem, Cost, Learning curve
- Result: Each dimension analyzed in isolation → synthesized comparison

### Pattern 5: Strict Isolation

**When to Use**:
- Tasks are completely independent
- Context carryover would cause confusion
- User will assemble pieces manually

**Protocol**:
```markdown
TURN 1-N: Independent Generation
For each independent task:
  Prompt: "[TASK N] ONLY. Do not reference other tasks.
          Do not assume context from previous turns."
  Output: Standalone content for task N

  [Start NEW conversation for next task, or clear context]
```

**Component Selections**:
- Use: [[strict-scope]], [[standalone-completeness]], [[no-assumptions]]
- Avoid: [[context-carryover]], [[sequential-reference]]

**Example Usage**:
- Problem: "Create 10 atomic notes from large document"
- Solution: Each note created in isolation, no cross-contamination

---

## 🔀 CONTEXT-HANDOFF STRATEGIES

### Strategy A: Full Context Carryover (Sequential Building)

**Mechanism**: Each turn receives full history from previous turns

**When to Use**:
- Narrative continuity required
- Later sections must reference earlier ones
- Synthesis is goal

**Risks**:
- Context dilution at high turn counts (>8 turns)
- Model attention spreads thin
- Earlier instructions fade

**Mitigation**:
- Use [[semantic-anchoring]] footer in every prompt
- Summarize previous turns if context >15k tokens
- Re-inject critical instructions every 3 turns

**Example**:
```
Turn 1: Generate Section 1
Turn 2: "Given Section 1 above, generate Section 2..."
Turn 3: "Given Sections 1 and 2, generate Section 3..."
[Full context maintained throughout]
```

### Strategy B: Summary-Only Carryover (Compressed Context)

**Mechanism**: Summarize previous turn(s) before next turn

**When to Use**:
- Full context unnecessary
- Key points sufficient for continuity
- Long conversations (>10 turns)

**Risks**:
- Information loss in summarization
- Nuance stripped away

**Mitigation**:
- User manually summarizes (don't let model self-summarize)
- Or: Use model to generate "key points" explicitly

**Example**:
```
Turn 1: Generate Section 1 (2000 words)
[User extracts: "Key insight: X solves Y through Z mechanism"]
Turn 2: "Key context: X solves Y through Z.
         Now, generate Section 2..."
```

### Strategy C: Zero Context Carryover (Strict Isolation)

**Mechanism**: No context from previous turns

**When to Use**:
- Tasks completely independent
- Context would confuse or bias
- Atomic note creation

**Risks**:
- Redundancy (model doesn't know what was said before)
- No synthesis possible

**Mitigation**:
- Explicitly state: "Ignore all previous turns"
- Or: Start fresh conversation for each task

**Example**:
```
Turn 1: Create atomic note for Concept A
[Start new conversation]
Turn 2: Create atomic note for Concept B
[Concepts don't reference each other]
```

---

## 🎛️ WORKFLOW EXECUTION CHECKLIST

Before executing any workflow:

- [ ] Problem type classified (use taxonomy above)
- [ ] Constraints identified (output/input/process)
- [ ] Workflow pattern selected with justification
- [ ] Context-handoff strategy chosen
- [ ] Components selected for each turn
- [ ] Success criteria defined (how do we know it worked?)
- [ ] Verification gates planned (when to check quality?)

During execution:

- [ ] Monitor for context dilution (re-anchor if needed)
- [ ] Check adherence to format constraints each turn
- [ ] Verify scope isolation (turns staying focused?)
- [ ] Log deviations from plan (why did we adjust?)

After execution:

- [ ] Evaluate: Did workflow outperform one-shot?
- [ ] Document: What worked? What failed?
- [ ] Update: Component performance notes
- [ ] Log: Usage analytics for this workflow pattern

---

## 🚨 ANTI-PATTERNS (What NOT to Do)

### ❌ Anti-Pattern 1: Premature Optimization
**Symptom**: Choosing complex workflow for simple problem
**Example**: Using 7-turn CoVe for casual blog post
**Fix**: Always check if one-shot sufficient first

### ❌ Anti-Pattern 2: Context Overload
**Symptom**: Carrying 20k+ tokens through 15 turns
**Example**: Full history from Turn 1 to Turn 15
**Fix**: Switch to summary-only carryover at Turn 8-10

### ❌ Anti-Pattern 3: Vague Decomposition
**Symptom**: Sub-problems overlap or are poorly defined
**Example**: "Section 1: Introduction" + "Section 2: Overview" (what's the difference?)
**Fix**: Explicit scope definitions, mutual exclusivity

### ❌ Anti-Pattern 4: No Verification Gates
**Symptom**: Running full 10-turn workflow, finding error at end
**Example**: Generating 7 sections before realizing Section 1 was wrong
**Fix**: Verify critical turns before proceeding

### ❌ Anti-Pattern 5: Workflow Rigidity
**Symptom**: Following pattern exactly when adaptation needed
**Example**: Insisting on 7 sub-problems when 4 makes more sense
**Fix**: Patterns are guidelines, not laws

---

## 🔗 Related Protocols

- [[00-librarian-core-identity]] → Core mission: decomposition by default
- [[01-component-management-sop]] → Components used within workflows
- [[03-context-handoff-procedures]] → Detailed handoff mechanics
- [[04-quality-assurance-checklist]] → Workflow validation standards

---

*Workflow Protocols Version: 1.0 | Last Updated: 2025-12-16*
