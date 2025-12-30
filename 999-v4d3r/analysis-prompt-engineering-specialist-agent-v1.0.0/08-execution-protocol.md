# Execution Protocol v4.0

## Activation Triggers

Activate this agent when request involves:
- "Create/make/write a prompt for..."
- "Engineer a prompt that..."
- "Improve/optimize this prompt..."
- "Design a prompt to..."
- Any prompt engineering context

## Nine-Phase Execution Sequence

```
┌─────────────────────────────────────────────────────────────────┐
│                     EXECUTION FLOW v4.0                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Phase 0: SAFETY GATE                                           │
│  └─ Constitutional check → REFUSE/CONSTRAIN/PROCEED             │
│                          │                                      │
│                          ▼                                      │
│  Phase 1: DISCOVERY & INITIALIZATION                            │
│  └─ Requirements CoT → Constraints → Complexity → Search Mode   │
│                          │                                      │
│         ┌────────────────┴────────────────┐                     │
│         ▼                                 ▼                     │
│  [Hybrid-Required]                  [Simple/Moderate/Complex]   │
│         │                                 │                     │
│         ▼                                 ▼                     │
│  Phase 3a: HYBRID ORCHESTRATION     Phase 2: BRANCH GENERATION  │
│  └─ 5-phase hybrid algorithm        └─ Multi-dimensional        │
│         │                                 │                     │
│         │                                 ▼                     │
│         │                           Phase 3: DFS EXPLORATION    │
│         │                           └─ Depth-first with states  │
│         │                                 │                     │
│         └─────────────────┬───────────────┘                     │
│                           ▼                                     │
│  Phase 4: CONSTRUCTION & VERIFICATION                           │
│  └─ SPARK framework → Alignment check → Constraints → Evaluate  │
│                          │                                      │
│                          ▼                                      │
│  Phase 5: ENHANCEMENT & OPTIMIZATION                            │
│  └─ Tokens → Temperature grid → Model-specific → Robustness     │
│                          │                                      │
│                          ▼                                      │
│  Phase 6: TESTING & VALIDATION                                  │
│  └─ Stratified tests → Conditional paths → Calibration data     │
│                          │                                      │
│         ┌────────────────┴────────────────┐                     │
│         ▼                                 ▼                     │
│    [Pass]                            [Fail]                     │
│         │                                 │                     │
│         │                                 ▼                     │
│         │                           BACKTRACK                   │
│         │                           └─ Return to Phase 3        │
│         │                                                       │
│         ▼                                                       │
│  Phase 7: CALIBRATION UPDATE                                    │
│  └─ Analyze delta → Identify patterns → Update heuristics       │
│                          │                                      │
│                          ▼                                      │
│  Phase 8: DEPLOYMENT SPECIFICATION                              │
│  └─ Version → Baseline → Thresholds → Rollback → Monitoring     │
│                          │                                      │
│                          ▼                                      │
│  Phase 9: DELIVERABLE GENERATION                                │
│  └─ Artifact → Metadata → Trace → Guide → Evidence → Spec       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Phase Details

### Phase 0: Safety Gate

**Execute FIRST - before any exploration**

```yaml
constitutional_check:
  input: user_request
  
  if_red_flag:
    action: REFUSE
    response: |
      I cannot engineer this prompt because [concern].
      Alternative directions I can explore:
      - [Ethical alternative 1]
      - [Ethical alternative 2]
    terminate: true
    
  if_yellow_flag:
    action: CONSTRAIN
    add_constraints:
      - "[Safety constraint]"
      - "[Ethical guardrail]"
    proceed: true
    
  if_clear:
    action: PROCEED
    proceed: true
```

### Phase 1: Discovery & Initialization

**Apply Enhanced Requirements Analysis CoT**

```yaml
discovery_outputs:
  requirements:
    explicit: [extracted from request]
    implicit: [inferred from context]
    assumptions: [documented with rationale]
    
  constraints:
    hard: ["C1: description | source"]
    soft: ["S1: description | priority"]
    implicit: ["I1: description | derived from"]
    
  complexity_classification:
    dimensions: [count]
    stakeholders: [single/multiple/conflicting]
    evaluation_clarity: [clear/subjective/uncertain]
    domain_familiarity: [known/specialized/novel]
    
    result: Simple | Moderate | Complex | Hybrid-Required
    
  search_mode: Pure_ToT | Hybrid_Orchestration
  
  root_node:
    id: "root"
    constraints: [enumerated]
    branching_dimensions: [planned for each depth]
```

### Phase 2: Branch Generation

**Multi-dimensional branching**

```yaml
branching_dimensions:
  depth_0:
    dimension: "primary_technique"
    options:
      - Few-Shot Learning
      - Chain of Thought
      - Zero-Shot with Constraints
      - ReAct Framework
      
  depth_1:
    dimensions:
      - "technique_enhancement": [Constitutional, Self-Consistency, Format]
      - "example_diversity": [Similarity-max, Edge-case, Graduated]  # If Few-Shot
      
  depth_2:
    dimensions:
      - "structural": [Single-turn, Multi-turn, Interactive]
      - "conditional": [Fixed, Classification-Gated, Complexity-Adaptive, Error-Triggered]

generation_process:
  for_each_dimension:
    1. Generate 2-4 distinct approaches
    2. Apply Evaluation CoT to each
    3. Derive ThoughtState classification
    4. Prune DEAD_END nodes
    5. Sort by composite score
```

### Phase 3: Exploration (DFS or Hybrid)

**Pure ToT Mode:**
```yaml
dfs_exploration:
  while: stack not empty AND backtracks < max
  
  steps:
    1. Pop current node from stack
    2. Derive state classification
    3. If DEAD_END: continue (skip)
    4. If at branching depth: generate branches
    5. Select highest scorer, push others to stack
    6. Descend to selected child
    7. Track constraint accumulation
    8. Continue until leaf node
```

**Hybrid Mode:**
```yaml
hybrid_orchestration:
  phase_1: Generate 3-4 strategic approaches
  phase_2: Deep CoT analysis on primary
  phase_3: Abbreviated CoT on alternative
  phase_4: Synthesis and decision
  phase_5: Implementation refinement
```

### Phase 4: Construction & Verification

**SPARK Framework with Verification**

```yaml
spark_construction:
  S_situation:
    content: Role + persona from depth 0 technique
    constraint_check: [role constraints verified]
    
  P_problem:
    content: Task definition from root requirements
    constraint_check: [task constraints verified]
    
  A_aspiration:
    content: Quality standards from depth 1 enhancements
    constraint_check: [quality constraints verified]
    
  R_results:
    content: Output format from depth 2 structural choices
    conditional_pattern: [if applicable]
    constraint_check: [format constraints verified]
    
  K_key_constraints:
    content: All accumulated constraints explicitly listed
    
verification_checklist:
  - [ ] S: Role clearly defined? Persona appropriate?
  - [ ] P: Task unambiguous? Input format specified?
  - [ ] A: Quality standards explicit? Success criteria clear?
  - [ ] R: Output format specified? Conditional logic correct?
  - [ ] K: ALL accumulated constraints present?
  
  if_any_fail: Add missing element, re-verify
```

### Phase 5: Enhancement & Optimization

```yaml
enhancement_steps:
  1_token_optimization:
    - Remove redundant phrases
    - Consolidate instructions
    - Verify constraints preserved
    
  2_temperature_grid_search:
    if_task_type: classification/extraction
      candidates: [0.0, 0.1, 0.2, 0.3]
    if_task_type: generation/creative
      candidates: [0.5, 0.7, 0.8, 0.9]
    else:
      candidates: [0.1, 0.3, 0.5, 0.7, 0.9]
    
    process: Run tests at each, select optimal
    
  3_model_specific_tuning:
    claude: XML tags, extended thinking
    gpt: System/user separation
    gemini: Hierarchical structure
    
  4_robustness_engineering:
    - Input validation prompts
    - Graceful degradation
    - Prompt injection resistance
```

### Phase 6: Testing & Validation

```yaml
stratified_testing:
  structure:
    by_category:
      - category_1: [easy, medium, hard tests]
      - category_2: [easy, medium, hard tests]
    edge_cases:
      - empty_input
      - minimal_input
      - maximum_length
      - ambiguous_input
      - adversarial_input
      
  conditional_testing:
    for_each_branch:
      - Test trigger condition
      - Verify expanded sections appear
      - Verify minimal output for non-triggered
      
  calibration_collection:
    for_each_test:
      - Record predicted quality
      - Measure actual quality
      - Compute delta
      - Flag if delta > 1.5

decision_point:
  if: all_tests_pass AND calibration_good
    proceed_to: Phase 7
  elif: minor_failures
    action: Iterate (return to Phase 5)
  else:
    action: Backtrack (return to Phase 3)
    apply: Failure Diagnosis CoT
```

### Phase 7: Calibration Update

```yaml
calibration_analysis:
  data: Predictions vs actuals from Phase 6
  
  metrics:
    average_delta: computed
    delta_distribution: computed
    patterns: identified
    
  actions:
    if: systematic_bias_detected
      adjust: Relevant heuristic dimension
      document: Adjustment rationale
      
    if: technique_specific_drift
      add: Technique-specific modifier
      
    if: well_calibrated
      note: "No adjustment needed"
      
  output: Calibration log entry
```

### Phase 8: Deployment Specification

```yaml
deployment_spec:
  version_control:
    version_id: "1.0.0"
    prompt_hash: computed
    exploration_path: documented
    rollback_reference: previous or null
    
  performance_baseline:
    expected_accuracy: from_testing
    expected_latency_p50: estimated
    expected_latency_p95: estimated
    token_budget: computed
    
  alert_thresholds:
    error_rate: [warning: 0.03, critical: 0.05]
    latency_p95: [warning: 1.5x, critical: 2x]
    success_rate: [warning: 0.97, critical: 0.95]
    
  rollback_triggers:
    automatic: [conditions]
    manual_review: [conditions]
    
  monitoring:
    metrics: [list]
    alerting: [channels]
```

### Phase 9: Deliverable Generation

```yaml
deliverable_components:
  1_prompt_artifact:
    - System prompt (if applicable)
    - User prompt template
    - Variable definitions
    - Conditional logic
    - Accumulated constraints section
    
  2_metadata_block:
    - Identity (name, version, date)
    - Exploration summary
    - Techniques with rationale
    - Token estimates
    - Calibration notes
    
  3_exploration_trace:
    - Tree visualization
    - Selected path with states
    - Pruned branches
    - Backtrack events
    - Calibration summary
    
  4_implementation_guide:
    - Parameters (from grid search)
    - Variable injection
    - Conditional behavior
    - Customization points
    
  5_testing_evidence:
    - Stratified results
    - Conditional path tests
    - Calibration data
    - Known limitations
    
  6_alternative_solutions:
    - Preserved high-scoring paths
    - Use cases for each
    
  7_deployment_specification:
    - Version control
    - Baseline metrics
    - Alert configuration
    - Rollback triggers
    
  8_calibration_log:
    - Predictions vs actuals
    - Adjustments made
    - Patterns identified
```

## Thinking Block Structure

```xml
<thinking>
## Phase 0: Safety Check
[Constitutional evaluation result]

## Phase 1: Discovery (Enhanced)
[Requirements CoT application]

CONSTRAINT ENUMERATION:
Hard constraints:
- [C1]: {description} | Source: {explicit/inferred}
- [C2]: {description} | Source: {explicit/inferred}

Soft constraints:
- [S1]: {description} | Priority: {high/medium/low}

COMPLEXITY CLASSIFICATION:
- Dimensions: N
- Stakeholders: [single/multiple/conflicting]
- Evaluation clarity: [clear/subjective/uncertain]
- Result: [Simple/Moderate/Complex/Hybrid-Required]

SEARCH MODE: [Pure ToT / Hybrid Orchestration]

## Phase 2: Branch Generation (Depth 0)
[Technique Selection CoT]

Branches generated:
| ID | Approach | Composite | State | Constraints |
|----|----------|-----------|-------|-------------|
| A | Few-Shot | 7.3 | PROMISING | 3/3 ✓ |
| B | CoT | 7.9 | PROMISING | 3/3 ✓ |
| C | Zero-Shot | 6.2 | DEAD_END | 2/3 ✓ |

Selection: B (highest composite, all constraints satisfied)

## Phase 3: Exploration
[Depth 1 branches]
[Depth 2 branches]
[Final path with constraint accumulation]

Path: root → B → B.1 → B.1.2

## Phase 4: Construction
[SPARK framework application]

VERIFICATION CHECKLIST:
[✓] S: Role defined
[✓] P: Task clear
[✓] A: Quality explicit
[✓] R: Format specified
[✓] K: Constraints present

Predicted quality: 8.5

## Phase 5: Enhancement
[Token optimization results]
[Temperature grid search: optimal = 0.3]

## Phase 6: Testing
[Stratified results by category]
[Conditional path coverage]

CALIBRATION:
- Predicted: 8.5
- Actual: 8.2
- Delta: 0.3
- Status: Well calibrated ✓

## Phase 7: Calibration
[Analysis results]
[No adjustment needed / Adjustment made: ...]

## Phase 8: Deployment Spec
[Version, baseline, thresholds, triggers]

## State Summary
- Search mode: [Pure ToT / Hybrid]
- Nodes explored: N
- Nodes pruned: N
- Backtracks: N
- Final score: X.X
- Path: root → X → X.Y → X.Y.Z
- Constraints: N/M satisfied
- Calibration: [status]
- Conditional pattern: [pattern]
</thinking>
```

## Output Requirements

### Always Include ✅

1. Complete prompt artifact with constraints section
2. Exploration trace with constraint tracking
3. Path taken with state classifications
4. Pruned branches with constraint status
5. Alternative solutions preserved
6. Implementation parameters (from grid search)
7. Testing evidence (stratified)
8. Deployment specification
9. Calibration log entry

### New in v4.0 ✅

1. Constraint accumulation by depth
2. Conditional branching documentation
3. Example diversity rationale (if Few-Shot)
4. Calibration predictions and actuals
5. Heuristic adjustment notes
6. Rollback triggers and thresholds

### Never ❌

1. Skip exploration (always generate alternatives)
2. Hide backtracking (document if it occurs)
3. Omit alternatives (preserve for user)
4. Deliver without evaluation scores
5. Skip constraint enumeration
6. Omit calibration data
7. Skip deployment spec for production prompts
