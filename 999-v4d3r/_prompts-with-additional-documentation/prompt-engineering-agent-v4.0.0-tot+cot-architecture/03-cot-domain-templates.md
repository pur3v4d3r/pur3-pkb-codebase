# Domain-Specialized CoT Templates

## Overview

v4.0 introduces domain-specialized Chain of Thought templates that improve reasoning quality for specific problem types. Apply these during Hybrid Orchestration Phase 2 or whenever the task matches the domain.

## Template Selection Guide

| Task Characteristics | Template |
|---------------------|----------|
| Calculations, formulas, proofs | Mathematical CoT |
| Decisions, stakeholders, trade-offs | Analytical CoT |
| Code, architecture, technical | Technical CoT |
| General reasoning, requirements | Standard Requirements CoT |
| Multiple domains | Combine relevant templates |

---

## Mathematical CoT Template

### Purpose
Specialized reasoning for quantitative and mathematical problems with explicit verification steps.

### Template

```
<mathematical_cot>
MATHEMATICAL PROBLEM: {problem_statement}

═══════════════════════════════════════════════════════════════
PHASE 1: PROBLEM ANALYSIS
═══════════════════════════════════════════════════════════════

1.1 CLASSIFICATION
- Type: [algebraic | geometric | statistical | optimization | calculus | other]
- Complexity: [single-step | multi-step | proof-based]
- Domain: [pure math | applied | word problem]

1.2 GIVEN INFORMATION
- Known values: 
  • {value_1} = {amount} {units}
  • {value_2} = {amount} {units}
- Known relationships:
  • {equation_1}
  • {constraint_1}
- Implicit information:
  • {domain_knowledge_applicable}

1.3 GOAL
- Primary unknown: {what_we_need_to_find}
- Secondary unknowns: {intermediate_values_needed}
- Required form: [exact | approximate | range | proof]

═══════════════════════════════════════════════════════════════
PHASE 2: STRATEGY SELECTION
═══════════════════════════════════════════════════════════════

2.1 APPLICABLE CONCEPTS
- Framework: {mathematical_theory}
- Key formulas:
  • {formula_1}: {description}
  • {formula_2}: {description}
- Relevant theorems:
  • {theorem}: {applicability}

2.2 APPROACH OPTIONS
APPROACH A: {method_name}
├── Steps: {brief_description}
├── Pros: {advantages}
└── Cons: {disadvantages}

APPROACH B: {alternative_method}
├── Steps: {brief_description}
├── Pros: {advantages}
└── Cons: {disadvantages}

2.3 SELECTED APPROACH
Method: {chosen_method}
Rationale: {why_this_is_best}

═══════════════════════════════════════════════════════════════
PHASE 3: STEP-BY-STEP SOLUTION
═══════════════════════════════════════════════════════════════

STEP 1: {action_description}
┌─────────────────────────────────────────────────────────────┐
│ Calculation:                                                │
│ {show_work_line_1}                                         │
│ {show_work_line_2}                                         │
│ {show_work_line_3}                                         │
├─────────────────────────────────────────────────────────────┤
│ Result: {intermediate_value} {units}                       │
├─────────────────────────────────────────────────────────────┤
│ Sanity check: {quick_verification}                         │
└─────────────────────────────────────────────────────────────┘

STEP 2: {action_description}
[Same structure]

STEP N: {final_calculation}
┌─────────────────────────────────────────────────────────────┐
│ Final Calculation:                                          │
│ {show_work}                                                 │
├─────────────────────────────────────────────────────────────┤
│ RESULT: {FINAL_ANSWER} {units}                             │
└─────────────────────────────────────────────────────────────┘

═══════════════════════════════════════════════════════════════
PHASE 4: VERIFICATION
═══════════════════════════════════════════════════════════════

4.1 DIMENSIONAL ANALYSIS
- Units check: {verify_units_combine_correctly}
- Result: [✓ Units correct | ✗ Unit error detected]

4.2 MAGNITUDE CHECK
- Expected scale: {reasonable_range}
- Actual result: {result}
- Assessment: [✓ Reasonable | ⚠️ Investigate]

4.3 BOUNDARY CHECK
- At minimum: {what_happens}
- At maximum: {what_happens}
- Sign: [✓ Appropriate | ⚠️ Investigate]

4.4 ALTERNATIVE VERIFICATION
Method: {different_approach}
Result via alternative: {result}
Match: [✓ Confirmed | ✗ Discrepancy - investigate]

═══════════════════════════════════════════════════════════════
FINAL ANSWER
═══════════════════════════════════════════════════════════════

{ANSWER_WITH_APPROPRIATE_PRECISION_AND_UNITS}

Confidence: [High | Medium | Low]
Basis: {why_this_confidence_level}
</mathematical_cot>
```

### Example Application

```
MATHEMATICAL PROBLEM: A tank initially contains 100 liters of water with 
5 kg of salt dissolved. Brine with 0.1 kg/L concentration enters at 
3 L/min, and the well-mixed solution leaves at 3 L/min. Find the 
amount of salt after 30 minutes.

PHASE 1: PROBLEM ANALYSIS
1.1 CLASSIFICATION
- Type: differential equations (first-order linear)
- Complexity: multi-step
- Domain: applied math (mixing problem)

1.2 GIVEN INFORMATION
- Known values:
  • Volume = 100 L (constant, since in = out)
  • Initial salt = 5 kg
  • Concentration in = 0.1 kg/L
  • Flow rate = 3 L/min
  • Time = 30 min
- Known relationships:
  • dS/dt = rate_in - rate_out
  • Well-mixed: uniform concentration

1.3 GOAL
- Primary unknown: S(30) = amount of salt at t=30
- Secondary unknowns: S(t) general solution
- Required form: exact numerical answer in kg

[Continue with remaining phases...]
```

---

## Analytical CoT Template

### Purpose
Decision-making and stakeholder analysis for complex business/strategic scenarios.

### Template

```
<analytical_cot>
SCENARIO: {scenario_description}
DOMAIN: {domain}
DECISION CONTEXT: {what_decision_is_needed}

═══════════════════════════════════════════════════════════════
PHASE 1: SITUATION ANALYSIS
═══════════════════════════════════════════════════════════════

1.1 KEY FACTS (Objective observations only)
• {fact_1}
• {fact_2}
• {fact_3}
• {fact_4}

1.2 ASSUMPTIONS
| Assumption | Confidence | Impact if Wrong |
|------------|------------|-----------------|
| {assumption_1} | High/Med/Low | {impact} |
| {assumption_2} | High/Med/Low | {impact} |
| {assumption_3} | High/Med/Low | {impact} |

1.3 CRITICAL CONTEXT
- Time constraints: {deadlines_pressures}
- Resource constraints: {budget_capacity_limits}
- External factors: {market_regulatory_competitive}
- Historical context: {relevant_precedents}

═══════════════════════════════════════════════════════════════
PHASE 2: STAKEHOLDER ANALYSIS
═══════════════════════════════════════════════════════════════

2.1 STAKEHOLDER MAP
| Stakeholder | Primary Interest | Influence | Position | Strategy |
|-------------|------------------|-----------|----------|----------|
| {stakeholder_1} | {goal} | H/M/L | Support/Oppose/Neutral | {approach} |
| {stakeholder_2} | {goal} | H/M/L | Support/Oppose/Neutral | {approach} |
| {stakeholder_3} | {goal} | H/M/L | Support/Oppose/Neutral | {approach} |

2.2 CONFLICT ANALYSIS
CONFLICT 1: {stakeholder_A} vs {stakeholder_B}
├── Nature: {what_they_disagree_on}
├── Root cause: {underlying_reason}
└── Resolution approach: {how_to_address}

CONFLICT 2: {description}
[Same structure]

2.3 COALITION POSSIBILITIES
- Natural allies: {stakeholders_with_aligned_interests}
- Potential converts: {neutral_stakeholders_to_persuade}
- Likely opposition: {stakeholders_to_manage}

═══════════════════════════════════════════════════════════════
PHASE 3: OPTION DEVELOPMENT
═══════════════════════════════════════════════════════════════

OPTION A: {name}
┌─────────────────────────────────────────────────────────────┐
│ Description: {detailed_description}                         │
├─────────────────────────────────────────────────────────────┤
│ Implementation:                                             │
│ 1. {step_1}                                                │
│ 2. {step_2}                                                │
│ 3. {step_3}                                                │
├─────────────────────────────────────────────────────────────┤
│ Resources: {requirements}                                   │
│ Timeline: {duration}                                        │
├─────────────────────────────────────────────────────────────┤
│ Stakeholder Impact:                                         │
│ • Benefits: {who_gains}                                     │
│ • Risks: {who_loses_or_concerns}                           │
├─────────────────────────────────────────────────────────────┤
│ Trade-offs: {what_we_give_up}                              │
└─────────────────────────────────────────────────────────────┘

OPTION B: {name}
[Same structure]

OPTION C: {name} (Creative/Hybrid Alternative)
[Same structure with emphasis on novel insight]

═══════════════════════════════════════════════════════════════
PHASE 4: RISK ASSESSMENT
═══════════════════════════════════════════════════════════════

4.1 RISK MATRIX
| Risk | Probability | Impact | Option | Mitigation | Residual |
|------|-------------|--------|--------|------------|----------|
| {R1} | H/M/L | H/M/L | A,B | {strategy} | H/M/L |
| {R2} | H/M/L | H/M/L | A | {strategy} | H/M/L |
| {R3} | H/M/L | H/M/L | B,C | {strategy} | H/M/L |

4.2 RISK TOLERANCE ASSESSMENT
- Organization appetite: [Risk-averse | Moderate | Risk-tolerant]
- Context factors: {what_influences_tolerance_here}
- Acceptable failure probability: {threshold}

4.3 WORST-CASE SCENARIOS
Option A worst case: {scenario} → Impact: {severity}
Option B worst case: {scenario} → Impact: {severity}
Option C worst case: {scenario} → Impact: {severity}

═══════════════════════════════════════════════════════════════
PHASE 5: DECISION FRAMEWORK
═══════════════════════════════════════════════════════════════

5.1 WEIGHTED CRITERIA ANALYSIS
| Criterion | Weight | Opt A | Opt B | Opt C |
|-----------|--------|-------|-------|-------|
| {criterion_1} | {%} | {1-5} | {1-5} | {1-5} |
| {criterion_2} | {%} | {1-5} | {1-5} | {1-5} |
| {criterion_3} | {%} | {1-5} | {1-5} | {1-5} |
| {criterion_4} | {%} | {1-5} | {1-5} | {1-5} |
| **WEIGHTED TOTAL** | 100% | {sum} | {sum} | {sum} |

5.2 SENSITIVITY ANALYSIS
- If {assumption_1} is wrong: Winner changes to {option}
- If {assumption_2} is wrong: Scores shift by {amount}
- Robustness assessment: [Highly robust | Moderately robust | Sensitive]

5.3 INFORMATION GAPS
- Would change analysis: {what_information}
- How to obtain: {method}
- Timeline: {when_available}
- Proceed without?: [Yes, with caveat | No, must wait]

═══════════════════════════════════════════════════════════════
PHASE 6: RECOMMENDATION
═══════════════════════════════════════════════════════════════

6.1 SELECTED OPTION
Choice: {option}

Primary rationale:
1. {most_important_reason}
2. {second_reason}
3. {third_reason}

6.2 KEY ASSUMPTIONS FOR SUCCESS
• {assumption_1_must_hold}
• {assumption_2_must_hold}
• {external_condition}

6.3 CONTINGENCY PLAN
Trigger: {when_to_reconsider}
Alternative: {backup_option}
Pivot timeline: {how_quickly_can_switch}

═══════════════════════════════════════════════════════════════
PHASE 7: IMPLEMENTATION ROADMAP
═══════════════════════════════════════════════════════════════

IMMEDIATE (0-30 days):
□ {action_1} | Owner: {who} | Deadline: {when}
□ {action_2} | Owner: {who} | Deadline: {when}
□ {action_3} | Owner: {who} | Deadline: {when}

SHORT-TERM (1-3 months):
□ {milestone_1}
□ {milestone_2}

LONG-TERM (3-12 months):
□ {strategic_objective_1}
□ {strategic_objective_2}

SUCCESS METRICS:
| Metric | Current | Target | Timeline | Review |
|--------|---------|--------|----------|--------|
| {KPI_1} | {now} | {goal} | {when} | {frequency} |
| {KPI_2} | {now} | {goal} | {when} | {frequency} |

COMMUNICATION PLAN:
- Stakeholder {X}: {message} via {channel} by {when}
- Stakeholder {Y}: {message} via {channel} by {when}

REVIEW SCHEDULE:
- Progress check: {frequency}
- Decision review trigger: {conditions_to_reconsider}
</analytical_cot>
```

---

## Technical CoT Template

### Purpose
Code review, architecture analysis, and technical implementation decisions.

### Template

```
<technical_cot>
TECHNICAL CONTEXT: {what_is_being_analyzed}
DOMAIN: {technology_area}
OBJECTIVE: {goal_of_analysis}

═══════════════════════════════════════════════════════════════
PHASE 1: CONTEXT UNDERSTANDING
═══════════════════════════════════════════════════════════════

1.1 SCOPE
- Component/System: {what_specifically}
- Boundaries: {what_is_in_scope}
- Exclusions: {what_is_out_of_scope}

1.2 REQUIREMENTS
- Functional: {what_it_must_do}
- Non-functional:
  • Performance: {requirements}
  • Security: {requirements}
  • Scalability: {requirements}
  • Maintainability: {requirements}

1.3 CONSTRAINTS
- Technical: {technology_limitations}
- Resource: {time_budget_team}
- Integration: {external_dependencies}

═══════════════════════════════════════════════════════════════
PHASE 2: ANALYSIS
═══════════════════════════════════════════════════════════════

2.1 CURRENT STATE ASSESSMENT
Strengths:
+ {positive_aspect_1}
+ {positive_aspect_2}

Weaknesses:
- {issue_1}: Impact [{High/Med/Low}]
- {issue_2}: Impact [{High/Med/Low}]

2.2 DETAILED FINDINGS
FINDING 1: {title}
├── Location: {where_in_code/system}
├── Category: [Security | Performance | Logic | Architecture | Style]
├── Severity: [Critical | High | Medium | Low]
├── Evidence: {specific_observation}
├── Impact: {consequence_if_unaddressed}
└── Root cause: {underlying_reason}

FINDING 2: {title}
[Same structure]

2.3 PATTERN ANALYSIS
- Anti-patterns detected: {list}
- Best practices followed: {list}
- Opportunities for improvement: {list}

═══════════════════════════════════════════════════════════════
PHASE 3: SOLUTION DESIGN
═══════════════════════════════════════════════════════════════

3.1 APPROACH OPTIONS
APPROACH A: {name}
├── Description: {how_it_works}
├── Addresses: {which_findings}
├── Trade-offs: {pros_cons}
└── Effort: [Low | Medium | High]

APPROACH B: {name}
[Same structure]

3.2 RECOMMENDED SOLUTION
Selected: {approach}

Implementation:
```{language}
// Before
{problematic_code_or_design}

// After
{improved_code_or_design}
```

Explanation: {why_this_is_better}

═══════════════════════════════════════════════════════════════
PHASE 4: VALIDATION STRATEGY
═══════════════════════════════════════════════════════════════

4.1 TESTING REQUIREMENTS
- Unit tests needed: {specific_tests}
- Integration tests: {scenarios}
- Performance tests: {benchmarks}

4.2 VERIFICATION STEPS
□ {verification_1}
□ {verification_2}
□ {verification_3}

4.3 ROLLBACK PLAN
- Trigger: {when_to_rollback}
- Process: {how_to_rollback}
- Impact: {what_users_experience}

═══════════════════════════════════════════════════════════════
PHASE 5: RECOMMENDATIONS
═══════════════════════════════════════════════════════════════

CRITICAL (Must do):
1. {recommendation_1}
2. {recommendation_2}

IMPORTANT (Should do):
1. {recommendation_1}
2. {recommendation_2}

ENHANCEMENT (Could do):
1. {recommendation_1}
2. {recommendation_2}

DOCUMENTATION UPDATES:
- {doc_update_1}
- {doc_update_2}
</technical_cot>
```

---

## Applying Domain Templates in Hybrid Orchestration

During Hybrid Orchestration Phase 2 (CoT Deep Dive), select the appropriate domain template:

```yaml
domain_template_selection:
  if: task involves calculations, formulas, quantitative analysis
    use: Mathematical CoT Template
    
  elif: task involves decisions, stakeholders, trade-offs, strategy
    use: Analytical CoT Template
    
  elif: task involves code, architecture, technical implementation
    use: Technical CoT Template
    
  elif: task is general or cross-domain
    use: Standard Requirements Analysis CoT
    combine_with: Relevant domain template sections
```

The domain-specialized templates ensure that the deep-dive phase produces thoroughly reasoned analysis appropriate to the problem type, improving both the quality of the primary path analysis and the final prompt construction.
