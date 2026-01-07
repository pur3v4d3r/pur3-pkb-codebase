# Enhanced ToT Cognitive Architecture v4.0

## Overview

The Tree of Thoughts framework provides the cognitive structure for systematic prompt engineering exploration. v4.0 enhances the original architecture with constraint tracking, state classification, and calibration integration.

## Thought Node Structure

```yaml
ThoughtNode:
  # ═══════════════════════════════════════════════════════════════
  # IDENTITY
  # ═══════════════════════════════════════════════════════════════
  id: string                    # Unique identifier (e.g., "root", "A", "A.1", "A.1.2")
  depth: integer                # Level in tree (0 = root)
  parent_id: string | null      # Reference to parent node
  
  # ═══════════════════════════════════════════════════════════════
  # STATE (What this node represents)
  # ═══════════════════════════════════════════════════════════════
  state:
    approach_label: string      # Human-readable approach name
    selected_techniques: list   # Techniques committed at this node
    partial_prompt: string      # Prompt content constructed so far
    constraints: list           # Requirements satisfied
    open_questions: list        # Unresolved decisions
    
  # ═══════════════════════════════════════════════════════════════
  # NEW v4.0: CONSTRAINT ACCUMULATION
  # ═══════════════════════════════════════════════════════════════
  constraint_accumulation:
    from_root: list             # Constraints from requirements analysis
      # Format: ["C1: description | source: explicit/inferred"]
    from_depth_1: list          # Constraints from technique selection
    from_depth_2: list          # Constraints from structural choices
    from_depth_3: list          # Constraints from enhancements (if applicable)
    
    summary:
      total_constraints: integer
      satisfied: list           # Constraint IDs verified as met
      violated: list            # Constraint IDs that failed
      unknown: list             # Constraints not yet evaluable
    
  # ═══════════════════════════════════════════════════════════════
  # EVALUATION (Scoring this node)
  # ═══════════════════════════════════════════════════════════════
  evaluation:
    feasibility: float          # 0-10: Can this approach work?
    quality_estimate: float     # 0-10: Expected output quality
    novelty: float              # 0-10: Distinctiveness from siblings
    efficiency: float           # 0-10: Token/complexity efficiency
    composite: float            # Weighted average (primary search signal)
    
  # ═══════════════════════════════════════════════════════════════
  # NEW v4.0: DERIVED STATE CLASSIFICATION
  # ═══════════════════════════════════════════════════════════════
  derived_state:
    classification: ThoughtState  # Categorical state
    state_reason: string          # Why this classification
    
  # ═══════════════════════════════════════════════════════════════
  # NEW v4.0: CALIBRATION TRACKING
  # ═══════════════════════════════════════════════════════════════
  calibration:
    predicted_quality: float      # Quality estimate at construction
    actual_quality: float | null  # Measured after testing (null until tested)
    calibration_delta: float | null  # |predicted - actual|
    calibration_status: string    # well_calibrated | minor_drift | significant_drift
    
  # ═══════════════════════════════════════════════════════════════
  # METADATA
  # ═══════════════════════════════════════════════════════════════
  metadata:
    status: enum                # [active | exploring | complete | pruned | backtracked]
    creation_reason: string     # Why this branch was generated
    pruning_reason: string      # If pruned, why
    
  children: list[ThoughtNode]   # Child branches
```

## ThoughtState Classification

v4.0 introduces categorical state classification as a derived property:

```yaml
ThoughtState:
  enum:
    - PROMISING      # High score, continue exploring
    - DEAD_END       # Low score, prune immediately
    - COMPLETE       # Terminal node with acceptable score
    - NEEDS_EXPLORATION  # Moderate score, has unexplored children
    - BACKTRACKED    # Previously explored, abandoned
```

### State Derivation Rules

```
FUNCTION derive_state(node) -> ThoughtState:

  composite = node.evaluation.composite
  is_terminal = node.depth >= max_branching_depth
  has_unexplored = len(node.children.filter(unexplored)) > 0
  
  IF composite >= 8.0:
    IF is_terminal:
      RETURN COMPLETE
      reason = "High score at terminal depth"
    ELSE:
      RETURN PROMISING
      reason = "High score, continue descent"
      
  ELIF composite >= 6.0:
    IF has_unexplored:
      RETURN NEEDS_EXPLORATION
      reason = "Moderate score with unexplored alternatives"
    ELSE:
      RETURN PROMISING
      reason = "Moderate score, best available path"
      
  ELIF composite >= 4.0:
    IF has_unexplored:
      RETURN NEEDS_EXPLORATION
      reason = "Marginal score, explore alternatives first"
    ELSE:
      RETURN PROMISING  # Reluctantly continue
      reason = "Marginal but only option"
      
  ELSE:  # composite < 4.0
    RETURN DEAD_END
    reason = f"Score {composite} below pruning threshold"
```

### State-Driven Search Decisions

| State | Action |
|-------|--------|
| PROMISING | Descend to children or construct if terminal |
| COMPLETE | Proceed to construction and testing |
| NEEDS_EXPLORATION | Explore children before committing |
| DEAD_END | Prune immediately, try sibling |
| BACKTRACKED | Skip, already abandoned |

---

## Search Configuration

```yaml
SearchConfiguration:
  # ═══════════════════════════════════════════════════════════════
  # PRIMARY STRATEGY
  # ═══════════════════════════════════════════════════════════════
  strategy: "depth_first"       # Primary search strategy
  
  # ═══════════════════════════════════════════════════════════════
  # BRANCHING PARAMETERS
  # ═══════════════════════════════════════════════════════════════
  branching:
    min_branches: 2             # Minimum alternatives to generate
    max_branches: 4             # Maximum to prevent explosion
    branch_at_depths: [0, 1, 2] # Where to generate alternatives
    
    # NEW v4.0: Multi-dimensional branching
    dimensions_by_depth:
      0: ["primary_technique"]
      1: ["technique_enhancement", "example_diversity"]  # Multiple dimensions
      2: ["structural_variation", "conditional_pattern"]  # Multiple dimensions
    
  # ═══════════════════════════════════════════════════════════════
  # PRUNING PARAMETERS
  # ═══════════════════════════════════════════════════════════════
  pruning:
    threshold: 4.0              # Prune if composite score below this
    relative_threshold: 0.6     # Prune if < 60% of sibling max score
    constraint_violation: true  # Prune if hard constraint violated
    
  # ═══════════════════════════════════════════════════════════════
  # BACKTRACKING PARAMETERS
  # ═══════════════════════════════════════════════════════════════
  backtracking:
    trigger_score: 5.0          # Backtrack if completed path scores below
    max_backtracks: 3           # Maximum backtracks before settling
    calibration_trigger: 1.5    # Backtrack if calibration delta exceeds
    
  # ═══════════════════════════════════════════════════════════════
  # CONVERGENCE PARAMETERS
  # ═══════════════════════════════════════════════════════════════
  convergence:
    success_threshold: 8.0      # Accept path if composite >= this
    early_termination: true     # Stop if excellent path found early
    
  # ═══════════════════════════════════════════════════════════════
  # EVALUATION WEIGHTS
  # ═══════════════════════════════════════════════════════════════
  evaluation_weights:
    feasibility: 0.25
    quality_estimate: 0.35
    novelty: 0.15
    efficiency: 0.25
```

---

## Evaluation Heuristics

### Composite Score Calculation

```
composite_score = (
    0.25 × feasibility +
    0.35 × quality_estimate +
    0.15 × novelty +
    0.25 × efficiency
)
```

### Feasibility Scoring (0-10)

| Score | Criteria |
|-------|----------|
| 9-10 | Technique perfectly matches task; all constraints satisfiable |
| 7-8 | Strong match with minor adaptations needed |
| 5-6 | Workable but requires significant modifications |
| 3-4 | Marginal fit; high risk of constraint violation |
| 0-2 | Fundamental mismatch; one or more hard constraints violated |

**Constraint Integration:**
```
feasibility_adjusted = base_feasibility - (violated_constraints × 2.0)
IF any_hard_constraint_violated:
    feasibility_adjusted = min(feasibility_adjusted, 3.0)
```

### Quality Estimate Scoring (0-10)

| Score | Criteria |
|-------|----------|
| 9-10 | Expected output exceeds requirements; production-ready |
| 7-8 | Meets all requirements with high reliability |
| 5-6 | Meets core requirements; edge cases uncertain |
| 3-4 | Partial requirements met; significant gaps |
| 0-2 | Unlikely to produce acceptable output |

**Calibration Adjustment (v4.0):**
```
IF technique in calibration_adjustments:
    quality_estimate -= calibration_adjustments[technique]
```

### Novelty Scoring (0-10)

| Score | Criteria |
|-------|----------|
| 9-10 | Fundamentally different approach from all siblings |
| 7-8 | Distinct technique combination; moderate differentiation |
| 5-6 | Some overlap with siblings but meaningfully different |
| 3-4 | Minor variation on existing path |
| 0-2 | Nearly identical to sibling; redundant exploration |

### Efficiency Scoring (0-10)

| Score | Criteria |
|-------|----------|
| 9-10 | Minimal tokens; simple structure; low latency expected |
| 7-8 | Reasonable token count; clean architecture |
| 5-6 | Moderate complexity; acceptable trade-offs |
| 3-4 | Complex structure; high token count |
| 0-2 | Excessive complexity; efficiency concerns |

**Conditional Branching Modifier (v4.0):**
```
IF conditional_pattern == "fixed":
    efficiency -= 1.0  # Always full output
ELIF conditional_pattern in ["classification_gated", "complexity_adaptive"]:
    efficiency += 0.5  # Average case savings
ELIF conditional_pattern == "error_triggered":
    efficiency += 1.0  # Minimal on success
```

---

## Depth-First Search Algorithm

```
ALGORITHM: DepthFirstPromptSearch

INPUT: root_node (initialized with requirements)
OUTPUT: best_path (sequence of nodes from root to solution)

1. INITIALIZE:
   - stack ← [root_node]
   - best_solution ← null
   - best_score ← 0
   - backtrack_count ← 0

2. WHILE stack is not empty AND backtrack_count < max_backtracks:
   
   2.1. current ← stack.pop()
   
   2.2. DERIVE state classification for current
        IF current.derived_state == DEAD_END:
            CONTINUE (skip to next in stack)
   
   2.3. IF current.depth in branch_at_depths:
        - children ← GENERATE_BRANCHES(current)
        - For each child:
            - EVALUATE(child)
            - DERIVE state classification
            - CHECK constraint satisfaction
        - PRUNE children where state == DEAD_END
        - SORT children by composite_score (descending)
        - stack.push(children)  # Best child explored first
   
   2.4. ELSE IF current is terminal (complete prompt):
        - CONSTRUCT prompt from path
        - final_score ← FULL_EVALUATION(current)
        - RECORD calibration prediction
        
        - IF final_score >= convergence.success_threshold:
            - RETURN current as best_solution  # Early termination
        - ELSE IF final_score > best_score:
            - best_solution ← current
            - best_score ← final_score
        - IF final_score < backtracking.trigger_score:
            - backtrack_count += 1
            - CONTINUE (try next in stack)
   
   2.5. ELSE:
        - ELABORATE current (add detail, resolve open questions)
        - EVALUATE updated current
        - UPDATE constraint satisfaction
        - IF current.derived_state != DEAD_END:
            - stack.push(current)

3. RETURN best_solution with exploration_trace
```

---

## Enhanced Branching Strategy

### Branching Dimensions by Depth

**Depth 0: Primary Technique**
```yaml
branches:
  - Few-Shot Learning
  - Chain of Thought
  - Zero-Shot with Constraints
  - ReAct Framework
  - Tree of Thoughts (for meta/complex)
  - Least-to-Most Decomposition
```

**Depth 1: Multiple Dimensions**
```yaml
dimensions:
  technique_enhancement:
    - Constitutional Safety
    - Self-Consistency
    - Format Enforcement
    - Confidence Calibration
    - Meta-Prompting
    
  example_diversity:  # Only if Few-Shot selected at depth 0
    - Similarity-Maximizing: "Examples cluster around expected inputs"
    - Edge-Case-Covering: "Examples include boundary conditions"
    - Difficulty-Graduated: "Examples progress from simple to complex"
```

**Depth 2: Multiple Dimensions**
```yaml
dimensions:
  structural_variation:
    - Single-turn, minimal format
    - Single-turn, structured output
    - Multi-turn, interactive
    - Multi-turn, guided workflow
    
  conditional_pattern:  # NEW v4.0
    - Fixed Structure
    - Classification-Gated
    - Complexity-Adaptive
    - Error-Triggered
```

### Branch Generation Process

```
FUNCTION GENERATE_BRANCHES(node, dimensions):

  1. IDENTIFY branching dimensions for current depth
     dimensions = config.dimensions_by_depth[node.depth]
  
  2. FOR each dimension in dimensions:
     
     2.1. GENERATE 2-4 distinct approaches for this dimension
     
     2.2. FOR each approach:
          - CREATE child node
          - INHERIT parent's constraint_accumulation
          - ADD dimension-specific constraints
          - SET approach-specific attributes
          - ESTIMATE evaluation scores
          - DERIVE state classification
     
     2.3. ENSURE novelty >= 5 between siblings
  
  3. COMBINE dimensions if multiple:
     - If depth has 2 dimensions with 3 options each → 9 combinations
     - PRUNE combinations that violate constraints
     - PRUNE redundant combinations (novelty < 5)
     - Keep top max_branches by composite score
  
  4. RETURN list of child nodes with derived states
```

---

## Backtracking Protocol

### Backtrack Triggers

1. **Low Score After Construction**: Completed prompt scores < 5.0
2. **Testing Failure**: Self-consistency or edge case tests fail
3. **Dead End**: No valid branches remain at current node
4. **Constraint Violation Discovered**: Late-discovered incompatibility
5. **Calibration Failure (v4.0)**: Predicted vs actual delta > 1.5

### Backtracking Process

```
FUNCTION BACKTRACK(current_node):

  1. MARK current_node.derived_state = BACKTRACKED
  
  2. RECORD backtrack_reason:
     - low_score: composite < trigger_score
     - test_failure: which tests failed
     - constraint_violation: which constraint
     - calibration_drift: delta value
  
  3. ASCEND to parent:
     parent_frame = stack.peek_parent()
  
  4. IF parent has unexplored children:
     - unexplored = parent.children.filter(state != BACKTRACKED)
     - SELECT next_child = max(unexplored, by=composite)
     - DESCEND to next_child
  
  5. ELSE:
     - RECURSIVELY backtrack to grandparent
  
  6. IF root reached with no unexplored paths:
     - RETURN best solution found so far
     - DOCUMENT exploration exhausted
     - NOTE: best may be suboptimal
  
  7. UPDATE calibration log:
     - Record this path as underperforming
     - Note technique combination for future adjustment
```

---

## Constraint Tracking System

### Constraint Structure

```yaml
Constraint:
  id: string              # "C1", "S2", etc.
  type: hard | soft       # Hard = must satisfy, Soft = prefer to satisfy
  description: string     # What the constraint requires
  source: string          # Where it came from (explicit, inferred, depth_N)
  priority: high | medium | low  # For soft constraints
  
  status: satisfied | violated | unknown
  evidence: string        # How we know the status
```

### Accumulation by Depth

```
DEPTH 0 (Root):
  Constraints from requirements analysis
  - Explicit from user request
  - Inferred from context
  - Constitutional (if yellow flag)

DEPTH 1 (Technique):
  Constraints from technique selection
  - Technique-specific requirements
  - Enhancement requirements
  - Example diversity requirements (if Few-Shot)

DEPTH 2 (Structure):
  Constraints from structural choices
  - Format constraints
  - Conditional pattern requirements
  - Output specification constraints

DEPTH 3+ (Enhancement):
  Additional constraints from refinement
  - Optimization constraints
  - Model-specific constraints
```

### Constraint Checking

```
FUNCTION check_constraints(node) -> (satisfied, violated, unknown):

  satisfied = []
  violated = []
  unknown = []
  
  FOR constraint in node.constraint_accumulation.all():
    
    IF can_evaluate(constraint, node.state):
      IF constraint_met(constraint, node.state):
        satisfied.append(constraint.id)
      ELSE:
        violated.append(constraint.id)
        IF constraint.type == hard:
          node.derived_state = DEAD_END
          node.metadata.pruning_reason = f"Violated: {constraint.id}"
    ELSE:
      unknown.append(constraint.id)
  
  RETURN (satisfied, violated, unknown)
```

---

## Exploration State Management

### State Structure

```yaml
exploration_state:
  # Core search state
  tree:
    root: ThoughtNode        # Full tree structure
    
  current:
    path: list[string]       # Node IDs from root to current
    node: ThoughtNode        # Current node being explored
    depth: integer           # Current depth in tree
    
  stack:                     # For DFS backtracking
    - node_id: string
      unexplored_children: list[string]
      
  # Solution tracking
  solutions:
    best: ThoughtNode | null
    best_score: float
    all_complete: list[ThoughtNode]  # All paths that reached completion
    
  # Search progress
  progress:
    nodes_created: integer
    nodes_evaluated: integer
    nodes_pruned: integer
    backtracks_used: integer
    max_backtracks: integer
    
  # NEW v4.0: Constraint tracking
  constraints:
    total: integer
    satisfied: list[string]
    violated: list[string]
    unknown: list[string]
    
  # NEW v4.0: Calibration tracking
  calibration:
    predictions: list[{node_id, predicted}]
    actuals: list[{node_id, actual}]
    deltas: list[float]
    average_delta: float
    status: well_calibrated | minor_drift | significant_drift
    
  # NEW v4.0: Hybrid mode tracking (if activated)
  hybrid:
    active: boolean
    current_phase: integer
    phase_outputs: dict
    approach_candidates: list
    synthesis_notes: string
```

### State Update Operations

```yaml
on_node_creation:
  - exploration_state.progress.nodes_created += 1
  - exploration_state.tree.add(new_node)
  - inherit parent.constraint_accumulation
  
on_node_evaluation:
  - exploration_state.progress.nodes_evaluated += 1
  - node.evaluation = computed_scores
  - node.derived_state = derive_state(node)
  - IF node.derived_state == DEAD_END:
      PRUNE(node)
      
on_constraint_check:
  - Update node.constraint_accumulation.summary
  - Update exploration_state.constraints lists
  - IF hard_constraint_violated:
      node.derived_state = DEAD_END
      
on_pruning:
  - exploration_state.progress.nodes_pruned += 1
  - node.metadata.status = "pruned"
  - node.metadata.pruning_reason = reason
  
on_descent:
  - exploration_state.stack.push({
      node_id: current.id,
      unexplored_children: current.children.filter(not_selected)
    })
  - exploration_state.current.path.append(selected_child.id)
  - exploration_state.current.node = selected_child
  - exploration_state.current.depth += 1
  
on_backtrack:
  - exploration_state.progress.backtracks_used += 1
  - current.derived_state = BACKTRACKED
  - parent_frame = exploration_state.stack.pop()
  - Record calibration failure if applicable
  
on_completion:
  - exploration_state.solutions.all_complete.append(current)
  - IF current.evaluation.composite > exploration_state.solutions.best_score:
      exploration_state.solutions.best = current
      exploration_state.solutions.best_score = current.evaluation.composite
      
on_calibration_record:
  - exploration_state.calibration.predictions.append({node_id, predicted})
  - # After testing:
  - exploration_state.calibration.actuals.append({node_id, actual})
  - delta = |predicted - actual|
  - exploration_state.calibration.deltas.append(delta)
  - exploration_state.calibration.average_delta = mean(deltas)
  - exploration_state.calibration.status = classify_calibration(average_delta)
```

---

## Exploration Trace Output

```markdown
## 🌳 Exploration Trace

### Tree Visualization

```
[Problem: {description}]
         │
    ┌────┴────┬────────────┐
    ▼         ▼            ▼
 [A: Few-Shot] [B: CoT] ★  [C: ReAct]
   (7.3)       (7.9)       (6.5) ✗
   PROMISING   PROMISING   DEAD_END
               │
         ┌─────┼─────┐
         ▼     ▼     ▼
    [B.1: +Const] [B.2: +Self-Con] [B.3: +Few-Shot]
      (8.2) ★       (7.8)           (7.5)
      PROMISING     NEEDS_EXPL      NEEDS_EXPL
         │
    ┌────┴────┐
    ▼         ▼
[B.1.1: Fixed] [B.1.2: Adaptive] ★
   (7.6)         (8.5)
   COMPLETE      COMPLETE

★ = Path taken
✗ = Pruned (DEAD_END)
(n.n) = Composite score
```

### Selected Path

| Depth | Node | Approach | Score | State | Constraints |
|-------|------|----------|-------|-------|-------------|
| 0 | B | Chain of Thought | 7.9 | PROMISING | 3/3 ✓ |
| 1 | B.1 | + Constitutional | 8.2 | PROMISING | 5/5 ✓ |
| 2 | B.1.2 | Complexity-Adaptive | 8.5 | COMPLETE | 7/7 ✓ |

### Constraint Accumulation

**From Root (3):**
- C1: Must classify into 3 categories | source: explicit
- C2: Production reliability required | source: inferred
- C3: Handle ambiguous inputs gracefully | source: inferred

**From Depth 1 (2):**
- C4: Include step-by-step reasoning | source: CoT technique
- C5: Maintain constructive tone | source: Constitutional

**From Depth 2 (2):**
- C6: Adapt depth to input complexity | source: Adaptive pattern
- C7: Include complexity assessment step | source: Adaptive pattern

**Summary:** 7/7 satisfied, 0 violated, 0 unknown

### Pruned Branches

| Node | Score | State | Reason |
|------|-------|-------|--------|
| C | 6.5 | DEAD_END | Action-observation not needed for static classification |

### Calibration Summary

- Predicted quality: 8.5
- Status: Pending (will update after testing)
```
