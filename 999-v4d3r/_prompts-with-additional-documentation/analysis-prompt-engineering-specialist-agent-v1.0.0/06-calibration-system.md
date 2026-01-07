# Evaluation Heuristic Calibration System

## Calibration Loop Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    CALIBRATION FEEDBACK LOOP                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  EXPLORATION PHASE                    VALIDATION PHASE          │
│  ┌──────────────────┐                ┌──────────────────┐       │
│  │ Evaluation CoT   │                │ Testing Phase    │       │
│  │                  │                │                  │       │
│  │ Generate:        │───predicted───▶│ Measure:         │       │
│  │ • feasibility    │                │ • actual quality │       │
│  │ • quality_est    │                │ • consistency    │       │
│  │ • novelty        │                │ • constraint sat │       │
│  │ • efficiency     │                │                  │       │
│  └──────────────────┘                └──────────────────┘       │
│           ▲                                   │                 │
│           │                                   │ actual          │
│           │ adjusted                          ▼                 │
│           │ heuristics               ┌──────────────────┐       │
│           │                          │ Calibration      │       │
│           │                          │ Analysis         │       │
│           │                          │                  │       │
│           │                          │ • Compare pred   │       │
│           │                          │   vs actual      │       │
│           │                          │ • Identify bias  │       │
│           │                          │ • Detect drift   │       │
│           │                          └──────────────────┘       │
│           │                                   │                 │
│           │                                   ▼                 │
│           │                          ┌──────────────────┐       │
│           └──────────────────────────│ Heuristic       │       │
│                                      │ Update          │       │
│                                      │                  │       │
│                                      │ • Scoring rules  │       │
│                                      │ • Weights        │       │
│                                      │ • Thresholds     │       │
│                                      └──────────────────┘       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Calibration Data Collection

### Data Point Structure

```yaml
CalibrationDataPoint:
  prompt_id: string
  timestamp: datetime
  
  task_characteristics:
    task_type: classification | generation | analysis | extraction
    complexity: simple | moderate | complex | hybrid
    domain: string
    techniques_used: list[string]
    conditional_branching: boolean
    constraint_count: integer
    example_count: integer  # If Few-Shot
  
  predictions:
    feasibility: float      # 0-10
    quality_estimate: float # 0-10
    novelty: float          # 0-10
    efficiency: float       # 0-10
    composite: float        # Weighted
  
  actuals:
    test_success_rate: float         # % of tests passed
    consistency_score: float         # Semantic similarity across runs
    constraint_satisfaction: float   # % constraints met
    user_feedback: float | null      # 1-5 if available
    semantic_similarity: float       # vs gold standard outputs
  
  computed:
    quality_delta: |predictions.quality_estimate - (semantic_similarity * 10)|
    composite_delta: |predictions.composite - (test_success_rate * 10)|
    
  classification:
    well_calibrated: quality_delta < 0.5
    minor_drift: 0.5 <= quality_delta < 1.5
    significant_drift: quality_delta >= 1.5
```

### Collection Points

| Phase | Data Collected | Purpose |
|-------|----------------|---------|
| Phase 4 (Construction) | `predicted_quality` | Record estimate |
| Phase 6 (Testing) | `actual_quality`, `consistency` | Measure reality |
| Phase 7 (Calibration) | `delta`, `classification` | Analyze gap |
| Production | `user_feedback`, ongoing metrics | Long-term validation |

## Semantic Similarity Validation

Ground truth comparison for quality predictions:

```yaml
SemanticSimilarityValidation:
  process:
    1. COLLECT gold standard outputs (expert-written ideal responses)
    2. GENERATE outputs using constructed prompt
    3. EMBED both outputs using sentence transformer
    4. COMPUTE cosine similarity
    5. CONVERT to 0-10 scale: similarity × 10
    6. COMPARE to predicted quality estimate
    
  example:
    gold_output: "Expert-written ideal response"
    generated_output: "Prompt-generated response"
    embedding_similarity: 0.87
    actual_quality: 8.7  # similarity × 10
    predicted_quality: 8.5
    delta: |8.5 - 8.7| = 0.2
    classification: "well_calibrated"
```

### Evaluator Options

| Evaluator | Method | Best For |
|-----------|--------|----------|
| **Semantic Similarity** | Embedding cosine similarity | Content quality |
| **Exact Match** | String equality | Classification tasks |
| **Custom Criteria** | Weighted multiple criteria | Complex tasks |
| **LLM-as-Judge** | Another LLM evaluates | Nuanced quality |

## Calibration Status Classification

| Delta Range | Status | Action Required |
|-------------|--------|-----------------|
| < 0.5 | ✅ Well Calibrated | None - heuristics accurate |
| 0.5 - 1.5 | ⚠️ Minor Drift | Monitor trend; adjust if persistent |
| ≥ 1.5 | ❌ Significant Drift | Immediate heuristic adjustment |

### Direction Matters

- **Positive delta** (predicted > actual): Overestimation
  - Risk: Selecting suboptimal paths
  - Fix: Reduce scores or add penalties
  
- **Negative delta** (predicted < actual): Underestimation  
  - Risk: Missing good paths, excessive exploration
  - Fix: Increase scores or remove penalties

## Heuristic Adjustment Rules

### Trigger Conditions

```yaml
adjustment_triggers:
  systematic_overestimation:
    condition: "average quality_delta > +1.0 over 10+ prompts"
    adjustments:
      - "Reduce base quality scores by 0.5-1.0"
      - "Add stricter criteria for high scores (8+)"
      - "Increase required evidence for quality claims"
      
  systematic_underestimation:
    condition: "average quality_delta < -1.0 over 10+ prompts"
    adjustments:
      - "Increase base quality scores by 0.5-1.0"
      - "Relax criteria for moderate scores"
      - "Trust technique-task matches more"
      
  technique_specific_drift:
    condition: "technique X shows delta > 1.5 consistently"
    adjustments:
      - "Add technique-specific modifier to feasibility"
      - "Update technique selection guidance"
      - "Add warning note for technique X"
      
  complexity_miscalibration:
    condition: "complex prompts show larger deltas than simple"
    adjustments:
      - "Add complexity penalty to quality estimate"
      - "Require more testing for complex prompts"
      - "Increase exploration for complex tasks"
      
  conditional_branching_drift:
    condition: "conditional prompts show larger deltas"
    adjustments:
      - "Add branching complexity penalty"
      - "Increase testing coverage for each branch"
      - "Validate branch trigger conditions"
```

### Adjustment Process

```
FUNCTION ADJUST_HEURISTICS(calibration_data):

  1. DETECT trigger condition from calibration log
     - Check all trigger conditions
     - Identify which are met
     - Prioritize by impact
  
  2. ANALYZE root cause
     - Which dimension is miscalibrated?
     - What task/technique characteristics correlate?
     - Is this systematic or isolated?
     
     Example analysis:
     "Quality overestimation correlates with:
      - CoT technique (r=0.7)
      - Complex tasks (r=0.6)
      - >3 constraints (r=0.5)"
  
  3. PROPOSE adjustment
     Adjustment types:
     - Scoring criteria modification
     - Weight adjustment (composite formula)
     - Threshold change (pruning, success)
     - Pattern-specific modifier
     
     Example proposal:
     "For CoT + complex tasks:
      - Reduce quality_estimate by 0.5
      - OR add complexity modifier: -0.1 per dimension"
  
  4. VALIDATE adjustment (if historical data available)
     - Apply proposed change to historical data
     - Recompute calibration metrics
     - Check if delta improves
     - Ensure no over-correction (delta doesn't flip sign)
  
  5. DEPLOY adjustment
     - Update heuristic configuration
     - Document change with rationale
     - Set monitoring for improvement
     - Plan rollback if degradation
```

### Example Adjustments

```yaml
adjustment_examples:
  example_1:
    trigger: "CoT technique overestimates by avg 1.2"
    root_cause: "CoT reasoning quality varies more than expected"
    adjustment:
      type: "technique_modifier"
      rule: "For CoT: quality_estimate -= 0.5"
    validation: "Historical delta reduced from 1.2 to 0.6"
    
  example_2:
    trigger: "Complex tasks underestimate by avg 0.9"
    root_cause: "Penalizing complexity too heavily"
    adjustment:
      type: "complexity_penalty_reduction"
      rule: "For complexity >= complex: efficiency += 0.5"
    validation: "Historical delta reduced from -0.9 to -0.3"
    
  example_3:
    trigger: "Conditional branching shows 40% higher variance"
    root_cause: "Branch paths not equally tested"
    adjustment:
      type: "testing_requirement"
      rule: "For conditional: min_tests_per_branch = 3"
    validation: "Variance reduced by 30%"
```

## Calibration Log Structure

### Entry Format

```yaml
calibration_log_entry:
  entry_id: "CAL-2024-001"
  timestamp: "2024-01-15T14:30:00Z"
  
  data_summary:
    prompts_analyzed: 15
    date_range: "2024-01-08 to 2024-01-15"
    task_types: ["classification", "generation", "analysis"]
    techniques_covered: ["Few-Shot", "CoT", "Zero-Shot"]
    
  metrics:
    average_quality_delta: +0.8
    average_composite_delta: +0.6
    well_calibrated_count: 8 (53%)
    minor_drift_count: 5 (33%)
    significant_drift_count: 2 (14%)
    
  patterns_identified:
    - pattern_type: "technique"
      description: "CoT consistently overestimates by 1.0+"
      affected_count: 5
      average_delta: +1.2
      
    - pattern_type: "complexity"
      description: "Complex tasks show 2x variance"
      affected_count: 4
      average_delta: varies
      
  adjustments_made:
    - dimension: "quality_estimate"
      scope: "CoT technique"
      before: "Base scoring criteria"
      after: "Base scoring - 0.5 for CoT"
      rationale: "Consistent overestimation observed"
      expected_improvement: "Reduce delta from 1.2 to <0.7"
      
  recommendations:
    - category: "testing"
      recommendation: "Increase test coverage for CoT prompts"
      priority: "medium"
      
    - category: "monitoring"
      recommendation: "Add CoT-specific calibration tracking"
      priority: "high"
      
  follow_up:
    review_date: "2024-01-22"
    success_criteria: "Average CoT delta < 0.7"
```

### Log Retention

| Data Type | Retention | Purpose |
|-----------|-----------|---------|
| Individual data points | 90 days | Detailed analysis |
| Weekly summaries | 1 year | Trend analysis |
| Adjustment records | Indefinite | Audit trail |
| Pattern discoveries | Indefinite | Knowledge base |

## Integration Points

### Phase 4 (Construction)
```python
# Record prediction for calibration
calibration_system.record_prediction(
    node_id=current_node.id,
    predicted_quality=current_node.evaluation.quality_estimate,
    techniques=current_node.state.selected_techniques,
    complexity=task_complexity
)
```

### Phase 6 (Testing)
```python
# Measure actual quality
actual_quality = semantic_similarity_evaluator.evaluate(
    expected=gold_standard,
    actual=generated_output
) * 10

# Record for calibration
calibration_system.record_actual(
    node_id=current_node.id,
    actual_quality=actual_quality,
    consistency=self_consistency_score,
    test_success_rate=test_results.success_rate
)
```

### Phase 7 (Calibration)
```python
# Analyze and adjust
calibration_analysis = calibration_system.analyze_recent(
    window_days=7,
    min_data_points=10
)

if calibration_analysis.adjustment_needed:
    new_heuristics = calibration_system.propose_adjustment(
        analysis=calibration_analysis
    )
    
    if calibration_system.validate_adjustment(new_heuristics):
        calibration_system.deploy_adjustment(new_heuristics)
        calibration_system.log_entry(calibration_analysis, new_heuristics)
```

### Production Monitoring
```python
# Continuous calibration from production
production_monitor.on_execution(
    callback=calibration_system.record_production_feedback
)

# Periodic recalibration
scheduler.weekly(
    calibration_system.analyze_production_data
)
```

## Best Practices

### Data Collection
- Collect at least 10 data points before adjustments
- Stratify by task type and complexity
- Include diverse domains to avoid overfitting
- Track over time, not just point-in-time

### Adjustment Caution
- Make small adjustments (±0.5) to avoid oscillation
- Validate on held-out data before deploying
- Monitor for over-correction
- Maintain history for rollback

### Pattern Recognition
- Look for correlations with characteristics
- Identify technique-specific biases
- Watch for interaction effects
- Consider temporal drift (model updates)

### Continuous Improvement
- Review calibration log weekly
- Update heuristics incrementally
- Document all changes
- Share learnings across team
