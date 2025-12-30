---
title: The IDEA Framework
id: 20251110-042855
type: 🧬concept
status: active
rating: ""
source: ""
url: ""
tags:
  - permanent-note
  - permanent-note/project-pur3v4d3r
  - permanent-note/pkb
  - prompt-engineering
  - prompt-engineering
  - prompt-engineering
aliases:
  - The IDEA Framework
link-up:
  - "[[self-learning-and-cognitive-development-moc]]"
link-related: []
maturity: seedling
confidence: speculative


review-last-reviewed: null
review-next-review: 2025-12-17
review-count: 0
review-interval: 3

review-priority: medium
---

> [!definition]
> - **Key-Term**:: [[The Idea Framework]]
> - [**Definition**:: IDEA (Identify, Design, Execute, Analyze) provides a systematic approach to developing complex prompts, particularly for multi-turn interactions or agent-like behaviors.]

> [!principle-point]
> **Chain-of-Thought Universality**
> CoT is not just for mathematical problems. It improves quality across domains: content analysis, strategic planning, code review, creative writing, ethical reasoning, and more. The visible reasoning also makes Claude's logic auditable and correctable.
# **I - Identify Requirements**

Begin by decomposing the task into its essential components and constraints.

## *Process Steps*:
1. **Task Decomposition**: Break the high-level goal into discrete cognitive operations
   - What must Claude *understand*?
   - What must Claude *analyze*?
   - What must Claude *generate*?
   - What must Claude *evaluate*?

2. **Success Criteria Definition**: Establish measurable outcomes
   - What does a perfect response look like?
   - What failure modes must be prevented?
   - What quality thresholds must be met?

3. **Constraint Mapping**: Identify all limitations and requirements
   - Length constraints
   - Format requirements
   - Tone/style specifications
   - Prohibited actions or content

### *Documentation Template*:
```markdown
## Requirements Analysis

**Primary Goal**: [Single sentence objective]

**Cognitive Operations Required**:
- [ ] Understanding: [What Claude needs to comprehend]
- [ ] Analysis: [What Claude needs to evaluate]
- [ ] Generation: [What Claude needs to create]
- [ ] Validation: [How Claude should self-check]

**Success Looks Like**:
1. [Measurable criterion 1]
2. [Measurable criterion 2]
3. [Measurable criterion 3]

**Critical Constraints**:
- [Constraint 1]
- [Constraint 2]

**Failure Modes to Prevent**:
- [Potential failure 1]
- [Potential failure 2]
```

# **D - Design Prompt Architecture**

Translate requirements into structured prompt components using XML architecture.

## *Design Principles*:
1. **Component Mapping**: Match each requirement to a prompt component
   - Understanding requirements → `<context>` + `<background>`
   - Analysis requirements → `<thinking_instructions>` + `<evaluation_criteria>`
   - Generation requirements → `<task>` + `<output_format>`
   - Validation requirements → `<success_criteria>` + `<constraints>`

2. **Structure Selection**: Choose appropriate XML hierarchy
   - Flat structure (2 levels) for simple tasks
   - Nested structure (3-4 levels) for complex tasks
   - Parallel structures for multiple similar items

3. **Example Integration**: Determine example strategy
   - Zero-shot if task is standard
   - One-shot for format matching
   - Few-shot (3-5 examples) for complex pattern matching

### *Design Document Template*:
```xml
<!-- PROMPT ARCHITECTURE DESIGN -->

<design_rationale>
  <structure_choice>
    [Why this XML structure was selected]
  </structure_choice>
  
  <component_map>
    <requirement>Understanding of technical context</requirement>
    <component>context</component>
    <rationale>Need domain-specific background</rationale>
  </component_map>
  
  <!-- Additional mappings -->
</design_rationale>

<!-- ACTUAL PROMPT FOLLOWS -->
<prompt>
  [Designed prompt structure]
</prompt>
```

# **E - Execute and Test**

Implement the prompt and evaluate against success criteria.

## *Testing Protocol*:
1. **Baseline Test**: Run prompt with representative input
2. **Edge Case Testing**: Test with unusual or boundary inputs
3. **Variation Testing**: Test with different phrasings of same request
4. **Stress Testing**: Test with maximum complexity inputs

## *Evaluation Dimensions*:
- **Correctness**: Does output match requirements?
- **Completeness**: Are all requested elements present?
- **Consistency**: Does repeated execution produce similar quality?
- **Clarity**: Is output understandable and well-structured?
- **Compliance**: Does output respect constraints?

# **A - Analyze and Refine**

Systematically improve the prompt based on test results.

## *Analysis Process*:
1. **Failure Mode Identification**: Categorize where prompt fails
   - Misunderstanding task
   - Incomplete output
   - Wrong format
   - Missing constraints
   - Poor quality reasoning

2. **Root Cause Analysis**: Determine why failures occur
   - Ambiguous instructions
   - Missing context
   - Insufficient examples
   - Unclear success criteria
   - Conflicting requirements

3. **Targeted Refinement**: Modify specific components
   - Add specificity where ambiguity exists
   - Add examples where format matching fails
   - Add constraints where boundary violations occur
   - Add reasoning instructions where logic is weak

### *Refinement Documentation*:
```markdown
## Iteration Log

### Iteration 1
**Test Result**: Output was correct but too verbose (1800 words vs 1000 target)

**Root Cause**: No explicit length constraint in prompt

**Refinement**: Added to `<output_format>`:
```xml
<length>
  Target: 1000 words
  Maximum: 1200 words
  If approaching maximum, prioritize key findings over supporting detail
</length>
```

# **Result**: Next iteration produced 1050-word output ✓

```

### The Chain-of-Thought Prompting Pattern

[[Chain-of-Thought prompting]] is particularly effective for Claude and should be incorporated whenever tasks involve reasoning, analysis, or multi-step problem-solving.

**Basic CoT Pattern**:

```xml
<instructions>
Before providing your final answer, think through this step-by-step:

1. [First reasoning step to show]
2. [Second reasoning step to show]
3. [Third reasoning step to show]

Show your complete reasoning, then present your final answer.
</instructions>
```

## **Enhanced CoT with Self-Evaluation**:

```xml
<thinking_process>
Follow this reasoning process:

## Step 1: Problem Analysis
[Analyze what the question is really asking]

## Step 2: Information Gathering
[Identify what information is relevant from context]

## Step 3: Reasoning
[Show your logical reasoning process]

## Step 4: Self-Check
[Evaluate your reasoning: What assumptions did you make? What could you be wrong about?]

## Step 5: Final Answer
[Provide your conclusion based on the above reasoning]
</thinking_process>
```

## **CoT with Multiple Paths (Tree-of-Thoughts)**:

```xml
<reasoning_instructions>
Explore multiple solution approaches:

**Approach 1: [Name]**
- Method: [How you'd solve it this way]
- Pros: [Advantages]
- Cons: [Disadvantages]
- Likely outcome: [What you'd expect]

**Approach 2: [Name]**
- Method: [How you'd solve it this way]
- Pros: [Advantages]
- Cons: [Disadvantages]
- Likely outcome: [What you'd expect]

**Approach 3: [Name]**
- Method: [How you'd solve it this way]
- Pros: [Advantages]
- Cons: [Disadvantages]
- Likely outcome: [What you'd expect]

**Selected Approach**: [Which one and why]

**Implementation**: [Execute the selected approach with detailed steps]
</reasoning_instructions>
```

> [!connections-and-links]
> - [[atomic-notes_moc]]: This is a link to the *Main Hub* for all **Atomic Notes**, from there you will find sections of each of the various *Subjects* I have been **working on**.
