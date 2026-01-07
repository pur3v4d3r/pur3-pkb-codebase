# Production Monitoring System

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    PROMPT LIFECYCLE MANAGEMENT                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐      │
│  │   REGISTRY   │───▶│   RUNTIME    │───▶│   MONITOR    │      │
│  │              │    │              │    │              │      │
│  │ • Versions   │    │ • Execution  │    │ • Metrics    │      │
│  │ • Prompts    │    │ • Logging    │    │ • Alerts     │      │
│  │ • Metadata   │    │ • Tracking   │    │ • Reports    │      │
│  └──────────────┘    └──────────────┘    └──────────────┘      │
│         │                   │                   │               │
│         ▼                   ▼                   ▼               │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                    CALIBRATION LOOP                      │   │
│  │  predicted quality ←→ actual quality → heuristic update  │   │
│  └─────────────────────────────────────────────────────────┘   │
│                              │                                  │
│                              ▼                                  │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                    ROLLBACK SYSTEM                       │   │
│  │  trigger detection → version switch → notification       │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Prompt Registry

### Data Structure

```yaml
PromptVersion:
  version_id: string         # Semantic version (1.0.0)
  prompt_text: string        # Full prompt content
  prompt_hash: string        # Content hash for integrity
  created_at: datetime
  created_by: string         # System or user identifier
  
  deployment:
    status: draft | staged | active | deprecated
    deployed_at: datetime | null
    deployed_by: string | null
    
  exploration:
    path: string             # "root → A → A.1 → A.1.2"
    techniques: list[string]
    complexity: string
    
  performance:
    predicted_quality: float
    baseline_accuracy: float | null
    baseline_latency_p50: float | null
    baseline_latency_p95: float | null
    
  rollback:
    reference: string | null  # Previous version ID
    auto_rollback_enabled: boolean
```

### Operations

| Operation | Description | Triggers |
|-----------|-------------|----------|
| `register(prompt_id, version)` | Add new version to registry | Prompt creation |
| `deploy(prompt_id, version)` | Set version as active | Manual or pipeline |
| `get_active(prompt_id)` | Return active prompt text | Runtime |
| `rollback(prompt_id)` | Revert to rollback reference | Alert or manual |
| `deprecate(prompt_id, version)` | Mark as deprecated | Newer version deployed |

## Execution Tracking

### Record Structure

```yaml
ExecutionRecord:
  execution_id: string
  prompt_id: string
  prompt_version: string
  timestamp: datetime
  
  performance:
    latency_ms: integer
    input_tokens: integer
    output_tokens: integer
    total_tokens: integer
    
  outcome:
    success: boolean
    error_type: string | null
    error_message: string | null
    
  quality:
    user_feedback: integer | null    # 1-5 rating
    automated_score: float | null    # If auto-eval enabled
    
  context:
    input_hash: string               # Privacy: hash not raw
    output_hash: string
    model_used: string
    temperature: float
    conditional_path: string | null  # Which branch triggered
```

### Privacy Considerations

- **Never store raw inputs/outputs** - Use hashes for debugging
- **Aggregated metrics only** - Individual records for alerts only
- **Retention policy** - Define TTL for execution records
- **Access control** - Limit who can query execution data

## Metrics Aggregation

### Time Windows

| Window | Purpose | Retention |
|--------|---------|-----------|
| 1 minute | Immediate issues | 24 hours |
| 5 minutes | Trend detection | 7 days |
| 1 hour | Sustained issues | 30 days |
| 24 hours | Daily reporting | 90 days |
| 7 days | Weekly trends | 1 year |

### Computed Metrics (Per Window)

```yaml
window_metrics:
  volume:
    execution_count: count(*)
    unique_users: count(distinct user_id)  # If available
    
  success:
    success_count: count(success=true)
    failure_count: count(success=false)
    success_rate: success_count / execution_count
    error_rate: failure_count / execution_count
    
  latency:
    p50: percentile(latency_ms, 50)
    p95: percentile(latency_ms, 95)
    p99: percentile(latency_ms, 99)
    avg: mean(latency_ms)
    
  tokens:
    avg_input: mean(input_tokens)
    avg_output: mean(output_tokens)
    total: sum(total_tokens)
    
  quality:
    avg_user_feedback: mean(user_feedback) where not null
    avg_automated: mean(automated_score) where not null
    feedback_count: count(user_feedback not null)
    
  errors:
    by_type: group_by(error_type).count()
    top_5: order_by(count).limit(5)
```

## Alert Configuration

### Alert Rules

```yaml
alert_rules:
  - name: "Critical Error Rate"
    condition: "error_rate > 0.05"
    window: "5_minutes"
    severity: "critical"
    actions: ["alert", "auto_rollback"]
    
  - name: "Elevated Error Rate"
    condition: "error_rate > 0.03"
    window: "15_minutes"
    severity: "warning"
    actions: ["alert"]
    
  - name: "High Latency P95"
    condition: "latency_p95 > baseline * 2.0"
    window: "5_minutes"
    severity: "critical"
    actions: ["alert"]
    
  - name: "Elevated Latency"
    condition: "latency_p95 > baseline * 1.5"
    window: "15_minutes"
    severity: "warning"
    actions: ["alert"]
    
  - name: "Low Success Rate"
    condition: "success_rate < 0.95"
    window: "10_minutes"
    severity: "critical"
    actions: ["alert", "auto_rollback"]
    
  - name: "Calibration Drift"
    condition: "avg_calibration_delta > 2.0"
    window: "1_hour"
    severity: "warning"
    actions: ["alert", "flag_for_review"]
    
  - name: "User Satisfaction Drop"
    condition: "avg_user_feedback < 3.0"
    window: "24_hours"
    severity: "warning"
    actions: ["alert"]
```

### Escalation Policy

```yaml
escalation:
  warning:
    channels: ["slack"]
    repeat_after: "1_hour"
    escalate_after: null
    
  critical:
    channels: ["slack", "pagerduty"]
    repeat_after: "15_minutes"
    escalate_after: "30_minutes"
    escalate_to: "on_call_engineer"
```

## Rollback Protocol

### Automatic Rollback

```yaml
auto_rollback:
  triggers:
    - condition: "error_rate > 0.10 for 5 minutes"
      confidence: "high"
    - condition: "success_rate < 0.85 for 10 minutes"
      confidence: "high"
    - condition: "latency_p99 > 10000ms for 5 minutes"
      confidence: "medium"
      
  process:
    1. DETECT trigger condition met
    2. VERIFY rollback_reference exists and is valid
    3. SNAPSHOT current metrics for post-mortem
    4. SWITCH active_version to rollback_reference
    5. NOTIFY operations team immediately
    6. LOG rollback event with full context
    7. MONITOR recovery metrics
    
  safeguards:
    - Minimum time between rollbacks: 15 minutes
    - Maximum auto-rollbacks per day: 3
    - Require manual intervention after limit
```

### Manual Rollback

```yaml
manual_rollback:
  triggers:
    - Operator request
    - User feedback indicates issues
    - Calibration drift detected
    - Business logic changes required
    
  process:
    1. RECEIVE rollback request with reason
    2. VERIFY requestor authorization
    3. CONFIRM target version is valid
    4. EXECUTE version switch
    5. MONITOR for improvement (15 min window)
    6. DOCUMENT reason and outcome
```

### Post-Rollback Actions

1. **Continue monitoring** with previous version
2. **Analyze failed version** for root cause
3. **Connect to exploration trace** - which decisions led here?
4. **Update calibration heuristics** if applicable
5. **Plan fix and re-deployment** with testing

## Performance Reports

### Daily Report Template

```markdown
# Prompt Performance Report: {prompt_id}
Date: {date}
Version: {active_version}

## Executive Summary
- Total Executions: {count}
- Success Rate: {rate}%
- Average Latency: {ms}ms
- User Satisfaction: {score}/5

## Key Metrics
| Metric | Today | vs Yesterday | vs Baseline |
|--------|-------|--------------|-------------|
| Success Rate | X% | +/-Y% | +/-Z% |
| Latency P50 | Xms | +/-Yms | +/-Zms |
| Latency P95 | Xms | +/-Yms | +/-Zms |
| Avg Tokens | X | +/-Y | +/-Z |

## Error Analysis
| Error Type | Count | % of Errors | Trend |
|------------|-------|-------------|-------|
| {type_1} | N | X% | ↑/↓/→ |
| {type_2} | N | X% | ↑/↓/→ |

## Calibration Status
- Average Delta: {value}
- Status: {well_calibrated/minor_drift/significant_drift}
- Adjustment Recommended: {yes/no}

## Alerts Triggered
- Warning: {count}
- Critical: {count}
- Rollbacks: {count}

## Recommendations
- {recommendation_1}
- {recommendation_2}
```

## Deployment Specification Block

Include in every production prompt deliverable:

```yaml
deployment_specification:
  version_control:
    version_id: "1.0.0"
    prompt_hash: "{hash}"
    created_at: "YYYY-MM-DD HH:MM:SS"
    exploration_path: "root → X → X.Y → X.Y.Z"
    rollback_reference: null
    
  performance_baseline:
    expected_accuracy: 0.95
    expected_latency_p50: 800
    expected_latency_p95: 1500
    token_budget_average: 500
    token_budget_max: 1200
    consistency_target: 0.90
    
  alert_thresholds:
    error_rate:
      warning: 0.03
      critical: 0.05
    latency_p95:
      warning: 2250      # 1.5x baseline
      critical: 3000     # 2x baseline
    success_rate:
      warning: 0.97
      critical: 0.95
      
  rollback_triggers:
    automatic:
      - "error_rate > 0.10 for 5 minutes"
      - "success_rate < 0.85 for 10 minutes"
    manual_review:
      - "calibration_drift > 2.0"
      - "user_feedback_negative_rate > 0.20"
      - "latency_p95 > 3000 for 30 minutes"
      
  monitoring:
    metrics_to_track:
      - execution_count
      - latency_distribution
      - success_rate
      - error_type_breakdown
      - token_usage
      - user_feedback_scores
      - conditional_branch_distribution
    alerting_channels:
      - slack
      - email
    report_schedule: daily
```

## Integration with Exploration Trace

When performance degrades, trace back to construction decisions:

```yaml
performance_to_exploration_mapping:
  degradation_detected:
    affected_metric: "accuracy"
    current_value: 0.85
    baseline_value: 0.95
    delta: -0.10
    
  exploration_analysis:
    exploration_path: "root → B → B.1 → B.1.2"
    
    depth_0_decision:
      selected: "Chain of Thought"
      alternatives: ["Few-Shot (7.3)", "Zero-Shot (6.8)"]
      rationale: "Task requires multi-step reasoning"
      potential_issue: "CoT may struggle with ambiguous inputs"
      
    depth_1_decision:
      selected: "Constitutional Safety"
      alternatives: ["Self-Consistency (7.8)"]
      rationale: "Tone constraints important"
      potential_issue: "May be over-constraining"
      
    depth_2_decision:
      selected: "Complexity-Adaptive"
      alternatives: ["Fixed Structure (7.6)"]
      rationale: "Input complexity varies"
      potential_issue: "Complexity assessment may be unreliable"
      
  failure_correlation:
    - "Failures cluster around complex inputs"
    - "Complexity-adaptive is triggering full expansion too often"
    - "Constitutional constraints conflicting with technical accuracy"
    
  recommendations:
    - "Try alternative path B → B.2 (Self-Consistency)"
    - "Adjust complexity threshold for adaptive branching"
    - "Add calibration entry for CoT + Constitutional combo"
```
