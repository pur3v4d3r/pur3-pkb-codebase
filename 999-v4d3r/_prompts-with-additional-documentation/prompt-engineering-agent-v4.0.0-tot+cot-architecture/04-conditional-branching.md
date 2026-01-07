# Conditional Output Branching Patterns

## Overview

Conditional output branching enables prompts to produce adaptive output structures based on intermediate classifications or assessments. This prevents over-generation for simple cases while ensuring comprehensive coverage for complex ones.

## Pattern Taxonomy

| Pattern | Trigger | Token Impact | Best For |
|---------|---------|--------------|----------|
| **Fixed Structure** | None | Always full | Compliance, audit |
| **Classification-Gated** | Category value | Variable by class | Routing, triage |
| **Complexity-Adaptive** | Complexity score | Scales with input | Support, analysis |
| **Error-Triggered** | Success/failure | Minimal on success | Review, validation |

## Pattern 1: Classification-Gated Expansion

### Structure
```
STEP 1: CLASSIFY {input} into categories

CLASSIFICATION: [Category A | Category B | Category C]

IF CLASSIFICATION == Category A:
    [EXPANDED_SECTION_A]
    - Detailed element 1
    - Detailed element 2
    - Detailed element 3
    
ELIF CLASSIFICATION == Category B:
    [STANDARD_SECTION_B]
    - Key element 1
    - Key element 2
    
ELSE:  # Category C
    [MINIMAL_SECTION_C]
    - Brief note

ALWAYS:
    [SUMMARY_SECTION]
```

### Example: Email Triage

```
Analyze this email and provide appropriate response:

═══════════════════════════════════════════════════
CLASSIFICATION
═══════════════════════════════════════════════════

PRIORITY: [High | Medium | Low]
CATEGORY: [Meeting | Project | Customer | Internal | Urgent]
ACTION_REQUIRED: [Yes | No]
SENTIMENT: [Positive | Neutral | Negative | Urgent]

═══════════════════════════════════════════════════
RESPONSE (Conditional)
═══════════════════════════════════════════════════

IF ACTION_REQUIRED == Yes:
    SUGGESTED_ACTIONS:
    - [Specific action 1]
    - [Specific action 2]
    - [Specific action 3]
    
    RECOMMENDED_TIMELINE: [Immediate | 4 hours | 24 hours | Week]
    
    STAKEHOLDERS_TO_NOTIFY:
    - [Person/team if applicable]

IF PRIORITY == High AND SENTIMENT == Urgent:
    ESCALATION_RECOMMENDATION:
    - Escalate to: [Recipient]
    - Suggested message: [Draft]
    - Timeline: [When to escalate]

IF CATEGORY == Customer:
    CUSTOMER_CONTEXT:
    - Account status: [If available]
    - Previous interactions: [Summary]
    - Recommended tone: [Formal | Friendly | Apologetic]

ALWAYS:
    SUMMARY: [1-2 sentence overview]
```

### Evaluation Scoring

When scoring Classification-Gated prompts:

| Criterion | Consideration | Score Modifier |
|-----------|---------------|----------------|
| **Classification reliability** | Can categories be clearly distinguished? | Critical for success |
| **Branch coverage** | Do all categories have appropriate depth? | Each branch evaluated |
| **Token efficiency** | Ratio of minimal to maximal output | Higher = better efficiency score |
| **Edge case handling** | What happens at category boundaries? | Test thoroughly |

## Pattern 2: Complexity-Adaptive Depth

### Structure
```
STEP 1: ASSESS complexity of {input}

COMPLEXITY_FACTORS:
- Factor A: [low | medium | high]
- Factor B: [low | medium | high]
- Factor C: [low | medium | high]

COMPLEXITY_SCORE: [1-5 scale]

═══════════════════════════════════════════════════

IF COMPLEXITY_SCORE <= 2 (Simple):
    [BRIEF_RESPONSE]
    Answer: [Direct response]
    Key point: [Single takeaway]

ELIF COMPLEXITY_SCORE <= 4 (Moderate):
    [STANDARD_RESPONSE]
    Answer: [Response with context]
    
    Explanation:
    - [How/why]
    - [Considerations]
    
    Example: [Illustrative]
    Caveat: [Main limitation]

ELSE (Complex):
    [COMPREHENSIVE_RESPONSE]
    Executive Summary: [2-3 sentences]
    
    Detailed Analysis:
    - [Component 1]
    - [Component 2]
    - [Component 3]
    
    Technical Deep-Dive:
    - [Mechanism]
    - [Architecture]
    - [Implications]
    
    Examples:
    - [Basic]
    - [Advanced]
    - [Edge case]
    
    Trade-offs:
    - [Alternative 1]: [pros/cons]
    - [Alternative 2]: [pros/cons]
    
    Recommendations: [Guidance]
    Further Reading: [Topics]
```

### Example: Technical Support

```
Technical Question Analysis

═══════════════════════════════════════════════════
COMPLEXITY ASSESSMENT
═══════════════════════════════════════════════════

Analyze the question complexity:

FACTORS:
- Concept count: [1-2: low | 3-4: medium | 5+: high]
- Interdependencies: [none: low | some: medium | many: high]
- Ambiguity level: [clear: low | some: medium | significant: high]
- Context required: [minimal: low | moderate: medium | extensive: high]

COMPLEXITY SCORE: [Calculate 1-5]

═══════════════════════════════════════════════════
RESPONSE
═══════════════════════════════════════════════════

IF COMPLEXITY_SCORE <= 2:
    ANSWER: [Direct, concise response in 1-2 sentences]
    
    KEY POINT: [Single most important takeaway]
    
    QUICK TIP: [Actionable suggestion if relevant]

ELIF COMPLEXITY_SCORE <= 4:
    ANSWER: [Clear response with necessary context]
    
    EXPLANATION:
    [2-3 paragraphs covering how/why this works]
    
    EXAMPLE:
    ```
    [Code or scenario illustration]
    ```
    
    COMMON PITFALLS:
    - [Issue 1]: [How to avoid]
    - [Issue 2]: [How to avoid]
    
    RELATED: [1-2 related concepts to explore]

ELSE:  # COMPLEXITY_SCORE == 5
    ## Executive Summary
    [3-4 sentences covering the complete answer]
    
    ## Detailed Explanation
    
    ### Core Concept
    [Thorough explanation of fundamentals]
    
    ### Technical Details
    [In-depth coverage of mechanisms]
    
    ### Implementation Considerations
    [Practical aspects]
    
    ## Examples
    
    ### Basic Example
    ```
    [Simple case]
    ```
    
    ### Advanced Example
    ```
    [Complex case with edge handling]
    ```
    
    ### Edge Case
    ```
    [Unusual scenario]
    ```
    
    ## Alternatives and Trade-offs
    | Approach | Pros | Cons | Best For |
    |----------|------|------|----------|
    | ... | ... | ... | ... |
    
    ## Recommendations
    [Context-specific guidance based on common scenarios]
    
    ## Further Learning
    - [Advanced topic 1]
    - [Advanced topic 2]
    - [Related domain]
```

### Complexity Scoring Guidelines

| Factor | Low (1) | Medium (2-3) | High (4-5) |
|--------|---------|--------------|------------|
| **Concepts** | 1-2 distinct concepts | 3-4 concepts | 5+ interrelated |
| **Dependencies** | Independent | Some relationships | Tightly coupled |
| **Ambiguity** | Single interpretation | Some clarification needed | Multiple valid interpretations |
| **Context** | Self-contained | Domain knowledge helps | Requires significant context |

## Pattern 3: Error-Triggered Elaboration

### Structure
```
STEP 1: ATTEMPT {primary_operation}

ASSESSMENT: [Success | Partial | Failure]

═══════════════════════════════════════════════════

IF ASSESSMENT == Success:
    [MINIMAL_OUTPUT]
    ✅ {confirmation}
    Optional notes: [Minor suggestions if any]

ELIF ASSESSMENT == Partial:
    [MODERATE_OUTPUT]
    ⚠️ Partial success
    
    What worked:
    - [Working element 1]
    - [Working element 2]
    
    Issues found:
    - [Issue 1]: [Severity] | [Fix]
    - [Issue 2]: [Severity] | [Fix]
    
    Suggested fixes: [Actionable steps]

ELSE:  # Failure
    [COMPREHENSIVE_OUTPUT]
    ❌ Significant issues detected
    
    Failure Analysis:
    - Primary failure: [What broke]
    - Root cause: [Why it broke]
    - Impact: [Consequences]
    
    Detailed Breakdown:
    [Issue-by-issue analysis]
    
    Corrected Implementation:
    [Full working solution]
    
    Prevention:
    - [How to avoid in future]
    - [Testing approach]
    - [Checklist items]
```

### Example: Code Review

```
Code Review: Error-Triggered Analysis

═══════════════════════════════════════════════════
INITIAL ASSESSMENT
═══════════════════════════════════════════════════

Reviewing code for: correctness, security, performance, style

OVERALL STATUS: [✅ Approved | ⚠️ Needs Changes | ❌ Requires Revision]
SCORE: [X]/10

═══════════════════════════════════════════════════
REVIEW (Depth based on status)
═══════════════════════════════════════════════════

IF STATUS == ✅ Approved:
    ✅ **Code approved for merge**
    
    Strengths noted:
    - [Positive aspect]
    
    Minor suggestions (optional):
    - [Style improvement if any]

ELIF STATUS == ⚠️ Needs Changes:
    ⚠️ **Changes required before merge**
    
    ## What Works Well
    - [Correctly implemented aspect 1]
    - [Correctly implemented aspect 2]
    
    ## Issues to Address
    
    ### Issue 1: [Title]
    - **Location**: Line X / Function Y
    - **Severity**: [High | Medium | Low]
    - **Type**: [Security | Performance | Logic | Style]
    - **Current**:
      ```language
      [problematic code]
      ```
    - **Suggested**:
      ```language
      [corrected code]
      ```
    - **Why**: [Explanation]
    
    [Repeat for each issue]
    
    ## Testing Recommendations
    - [Specific test to add]

ELSE:  # STATUS == ❌ Requires Revision
    ❌ **Significant revision required**
    
    ## Critical Failure Analysis
    
    ### Primary Failure
    - **What breaks**: [Specific behavior]
    - **Root cause**: [Underlying issue]
    - **Impact if deployed**: [Consequences]
    
    ### Issue Breakdown
    | # | Issue | Location | Severity | Type |
    |---|-------|----------|----------|------|
    | 1 | [Desc] | [Line] | Critical | [Type] |
    | 2 | [Desc] | [Line] | High | [Type] |
    
    ## Detailed Analysis
    
    ### Issue 1: [Title]
    [Full analysis with context, cause, fix]
    
    ### Issue 2: [Title]
    [Full analysis]
    
    ## Corrected Implementation
    ```language
    // Full working version with comments explaining changes
    [complete corrected code]
    ```
    
    ## Step-by-Step Fixes
    1. **[Change 1]**: [Why this is necessary]
    2. **[Change 2]**: [Why this is necessary]
    3. **[Change 3]**: [Why this is necessary]
    
    ## Prevention Strategies
    - **Code practice**: [What to do differently]
    - **Testing approach**: [What tests would catch this]
    - **Review checklist**: [Item to add to review process]
    
    ## Learning Resources
    - [Relevant concept to study]
    - [Best practice guide]
```

## Pattern 4: Fixed Structure

### When to Use
- Compliance/audit requirements
- Legal/regulatory content
- Consistent reporting formats
- Multi-system integration
- User expectation of completeness

### Structure
```
[All sections always present regardless of input]

## Section A: [Always included]
[Content - may be "N/A" or "None identified" if not applicable]

## Section B: [Always included]
[Content]

## Section C: [Always included]
[Content]

[No conditional logic - predictable structure]
```

### Example: Compliance Report

```
Compliance Assessment Report

═══════════════════════════════════════════════════
EXECUTIVE SUMMARY
═══════════════════════════════════════════════════
[Always present - overview of findings]

═══════════════════════════════════════════════════
ASSESSMENT DETAILS
═══════════════════════════════════════════════════

## 1. Scope
[Always present - what was assessed]

## 2. Methodology  
[Always present - how assessment was conducted]

## 3. Findings

### 3.1 Critical Issues
[Always present - "None identified" if clean]

### 3.2 High Priority Issues
[Always present - "None identified" if clean]

### 3.3 Medium Priority Issues
[Always present - "None identified" if clean]

### 3.4 Low Priority Issues
[Always present - "None identified" if clean]

## 4. Recommendations
[Always present - may be "Continue current practices"]

## 5. Timeline
[Always present - remediation schedule or "N/A"]

═══════════════════════════════════════════════════
APPENDICES
═══════════════════════════════════════════════════

## A. Evidence Reviewed
[Always present]

## B. Personnel Interviewed
[Always present]

## C. Standards Applied
[Always present]

[Signature/approval section - always present]
```

## Integration with ToT Branching

Conditional patterns become a **branching dimension at Depth 2**:

```yaml
depth_2_conditional_branches:
  - id: "X.Y.1"
    pattern: "Fixed Structure"
    trade_off: "Consistent but may over-generate"
    evaluation_modifier: "efficiency -1, consistency +2"
    
  - id: "X.Y.2"
    pattern: "Classification-Gated"
    trade_off: "Efficient but requires reliable classification"
    evaluation_modifier: "efficiency +1, risk if classification fails"
    
  - id: "X.Y.3"
    pattern: "Complexity-Adaptive"
    trade_off: "Natural but complexity assessment may vary"
    evaluation_modifier: "user_satisfaction +1, consistency -1"
    
  - id: "X.Y.4"
    pattern: "Error-Triggered"
    trade_off: "Minimal on success, comprehensive on failure"
    evaluation_modifier: "efficiency +2 for success cases"
```

## Testing Conditional Prompts

### Test Coverage Requirements

Each conditional branch needs independent testing:

```yaml
test_plan_conditional:
  pattern: "Classification-Gated"
  
  branch_tests:
    - branch: "Category A (expanded)"
      test_cases: 5
      coverage: [normal, boundary, edge]
      
    - branch: "Category B (standard)"
      test_cases: 3
      coverage: [normal, boundary]
      
    - branch: "Category C (minimal)"
      test_cases: 3
      coverage: [normal, boundary]
      
  boundary_tests:
    - "Input at boundary between A and B"
    - "Ambiguous classification scenarios"
    
  consistency_tests:
    - "Same input → same branch selection"
    - "Branch output matches expected depth"
```

### Calibration for Conditional Prompts

Track calibration separately per branch:

```yaml
calibration_conditional:
  overall_delta: 0.8
  
  per_branch:
    expanded_branch:
      predicted: 8.5
      actual: 8.2
      delta: 0.3
      status: "well_calibrated"
      
    standard_branch:
      predicted: 7.8
      actual: 7.0
      delta: 0.8
      status: "minor_drift"
      
    minimal_branch:
      predicted: 7.5
      actual: 8.1
      delta: 0.6
      status: "minor_drift (underestimate)"
      
  insight: "Standard branch underperforms - consider expanding"
```

## Selection Decision Framework

| Factor | Fixed | Classification | Complexity | Error |
|--------|-------|----------------|------------|-------|
| **Predictability need** | ✅ Best | Good | Variable | Variable |
| **Token efficiency** | ❌ Worst | Good | ✅ Best | ✅ Best |
| **User satisfaction** | Medium | High | High | High |
| **Implementation complexity** | ✅ Simple | Medium | Medium | Simple |
| **Testing burden** | Simple | Multi-branch | Multi-level | Two-path |
| **Classification required** | No | ✅ Yes | ✅ Yes | ✅ Yes |

### Quick Selection Guide

```
IF audit/compliance required → Fixed Structure
ELIF distinct categories with different needs → Classification-Gated
ELIF input complexity varies significantly → Complexity-Adaptive
ELIF task is validation/review → Error-Triggered
ELSE → Start with Classification-Gated (most versatile)
```
