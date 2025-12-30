---
tags: #spes #claude-instructions #analytics #usage-tracking #learning
aliases: [Usage Analytics, Analytics Protocols, SPES Learning System]
status: reference
certainty: ^verified
created: 2025-12-16
instruction-type: protocols
read-priority: 5
applies-to: [analytics, learning, pattern-detection]
version: 1.0
---

# Usage Analytics Protocols

> [!abstract] Purpose
> Systematic procedures for tracking component usage, detecting patterns, measuring performance, and enabling SPES to learn from every interaction.

---

## 🎯 ANALYTICS PHILOSOPHY

**Core Principle**: SPES becomes **smarter through usage**, not just through explicit programming.

**The Learning Loop**:
```
1. Use component/workflow
     ↓
2. Track usage & outcome
     ↓
3. Detect patterns
     ↓
4. Generate insights
     ↓
5. Update recommendations
     ↓
[Loop back to 1 with improved system]
```

**Without Analytics**: Static library, no improvement
**With Analytics**: Self-improving system that learns what works

---

## 📊 TRACKED METRICS

### Component-Level Metrics

#### Usage Metrics
- **Usage Count**: How many times component used
- **Last Used**: Most recent usage date
- **Usage Frequency**: Times used / days since creation
- **Co-usage Patterns**: Which components used together

#### Performance Metrics
- **Success Rate**: % of successful uses (high/medium/low)
- **Quality Score**: Average quality rating (0.0-10.0)
- **Failure Modes**: Types of failures when they occur
- **User Satisfaction**: Subjective rating from user

#### Relationship Metrics
- **Synergy Strength**: How much better when combined
- **Conflict Frequency**: How often conflicts with others
- **Dependency Chain**: What components enable this one
- **Replacement Rate**: How often swapped for alternatives

### Workflow-Level Metrics

#### Execution Metrics
- **Workflow Usage Count**: Times this workflow executed
- **Average Turns**: Mean turn count for this workflow
- **Average Quality**: Mean output quality rating
- **Time Investment**: Estimated time to complete

#### Effectiveness Metrics
- **Success Rate**: % of workflows that achieve goals
- **One-Shot Comparison**: Sequential quality vs one-shot baseline
- **Reproducibility**: Consistency across multiple runs
- **User Preference**: Chosen over alternatives? Why?

#### Context Metrics
- **Average Context Size**: Mean tokens per turn
- **Context Strategy Used**: Which handoff strategy
- **Drift Incidents**: Times instruction drift occurred
- **Context Efficiency**: Useful context / total context ratio

### System-Level Metrics

#### Health Metrics
- **Component Count**: Total active components
- **Workflow Count**: Total documented workflows
- **Metadata Compliance**: % files fully compliant
- **Graph Health**: % well-connected nodes

#### Growth Metrics
- **New Components**: Components added over time
- **Retired Components**: Components removed over time
- **Net Growth**: New - retired
- **Knowledge Density**: Components per domain area

#### Learning Metrics
- **Pattern Count**: Unique patterns detected
- **Recommendation Accuracy**: % accurate suggestions
- **Gap Closure Rate**: Identified gaps → new components
- **System Improvement**: Quality trend over time

---

## 🔄 TRACKING PROTOCOLS

### Protocol 1: Component Usage Tracking

**When**: Every time a component is used in a workflow

**Procedure**:
```markdown
STEP 1: Identify Component Usage
- Note which component(s) used
- Note workflow context (problem type, turn number)

STEP 2: Update Component Metadata
- Increment usage-count by 1
- Update last-tested to today's date
- If quality rated, update avg-quality-score

STEP 3: Log Co-Usage
- Document which other components used in same workflow
- Update known-synergies if new combination discovered
- Update known-conflicts if incompatibility found

STEP 4: Note Outcome
- Success or failure?
- If failure: Document failure mode
- If success: Note quality level
```

**Automation Opportunities**:
- Dataview query to calculate usage-count from backlinks
- Script to auto-update last-tested dates
- Dashboard to visualize co-usage networks

### Protocol 2: Workflow Performance Tracking

**When**: After completing any multi-turn workflow

**Procedure**:
```markdown
STEP 1: Record Execution Data
Create log entry in [[05-testing-validation/test-results/]]

---
DATE: YYYY-MM-DD
WORKFLOW: [[workflow-name]]
PROBLEM: [Brief description]

EXECUTION:
- Turns Used: [Count]
- Context Strategy: [Strategy name]
- Components: [[comp-a]], [[comp-b]], [[comp-c]]
- Total Tokens: [Approximate]
- Time Investment: [Estimate]

OUTCOME:
- Success: YES / NO
- Quality Rating: [0.0-10.0]
- Success Criteria Met: [List]
- Issues Encountered: [List]

COMPARISON:
- One-Shot Baseline: [Quality rating]
- Sequential Quality: [Quality rating]
- Delta: [+/- points]

INSIGHTS:
- What worked well?
- What failed?
- Would you use this workflow again?
- Recommendations for improvement?
---

STEP 2: Update Workflow Metadata
- Increment usage-count
- Update success-rate if pattern changes
- Update last-used date
- Adjust complexity-level if misrated

STEP 3: Update Component Performance
- Update success-rate for each component used
- Note if component contributed to success/failure

STEP 4: Extract Patterns
- New synergies discovered?
- New conflicts discovered?
- New use cases identified?
```

### Protocol 3: Pattern Detection

**When**: Periodically (weekly) or after significant usage

**Procedure**:
```markdown
STEP 1: Query Usage Patterns
Run analytics queries:
- Most-used components
- Most-successful combinations
- Most-frequent failure modes
- Underutilized high-performers

STEP 2: Identify Trends
Look for:
- Components often used together (synergy candidates)
- Components never used together (conflict candidates)
- Components with declining success rates (need review)
- Components with rising usage (indicate demand)

STEP 3: Generate Insights
Create insight entries in [[06-analytics-dashboards/claude-learning-insights]]

Example:
---
INSIGHT: Persona-Format Synergy Pattern
DISCOVERED: YYYY-MM-DD

OBSERVATION:
[[persona-technical-accuracy]] + [[format-example-rich]]
used together in 8 workflows with 100% success rate.
When used separately: 70% success rate.

HYPOTHESIS:
Technical accuracy persona benefits from concrete examples
to ground precision requirements.

RECOMMENDATION:
1. Document synergy in both component files
2. Create composite component for this pair
3. Recommend this combo for technical content workflows

STATUS: Validated through 8 uses
---

STEP 4: System Updates
- Update component metadata (known-synergies)
- Create composite components if justified
- Update workflow recommendations
- Document in session-memory
```

### Protocol 4: Gap Identification

**When**: When user requests something that doesn't exist

**Procedure**:
```markdown
STEP 1: Document the Gap
Create entry in [[04-intelligence-layer/metadata-schema/knowledge-gaps]]

---
GAP: [Name of missing component/workflow]
IDENTIFIED: YYYY-MM-DD
REQUESTED BY: User / Claude observation

NEED:
[Description of what's needed and why]

USE CASE:
[Specific scenario where this would be used]

WORKAROUND (Current):
[How we handle this need today, if at all]

PRIORITY: High / Medium / Low
---

STEP 2: Assess Demand
- Is this a one-time need or recurring?
- How many use cases would this serve?
- Is there a workaround that's "good enough"?

STEP 3: Plan Creation
If demand justified:
- Add to project backlog
- Assign priority
- Estimate effort
- Schedule creation

STEP 4: Track Gap Closure
When gap filled:
- Update gap entry with FILLED: YYYY-MM-DD
- Link to created component/workflow
- Measure: Did it solve the problem?
```

---

## 📈 ANALYTICS DASHBOARDS

### Dashboard 1: Component Performance Overview

**Purpose**: See which components are most valuable

**Queries**:
```dataview
TABLE
  component-type,
  usage-count,
  success-rate,
  avg-quality-score,
  (usage-count * avg-quality-score) as value-score
FROM "02-component-library"
WHERE usage-count > 0
SORT value-score DESC
LIMIT 20
```

**Insights**:
- High value-score = Frequently used + High quality (core components)
- High usage + Low quality = Needs improvement or retirement
- Low usage + High quality = Underutilized gems (promote these)

### Dashboard 2: Synergy Network

**Purpose**: Visualize which components work best together

**Queries**:
```dataview
TABLE
  file.name as Component,
  known-synergies as "Best Partners",
  length(known-synergies) as "Partner Count"
FROM "02-component-library"
WHERE known-synergies
SORT length(known-synergies) DESC
```

**Insights**:
- High partner count = Versatile component (works with many)
- Low partner count = Specialized component (specific use case)
- No partners yet = Needs more testing

### Dashboard 3: Workflow Success Rates

**Purpose**: Identify most reliable workflows

**Queries**:
```dataview
TABLE
  workflow-pattern,
  problem-types,
  usage-count,
  success-rate,
  typical-turns
FROM "03-sequential-workflows"
SORT success-rate DESC, usage-count DESC
```

**Insights**:
- High success + High usage = Production-ready workflows
- High success + Low usage = Hidden gems
- Low success = Needs refinement or retirement

### Dashboard 4: System Health Monitor

**Purpose**: Track overall SPES health

**Metrics**:
```markdown
## System Vitals

**Component Library**:
- Total Components: [Count]
- Evergreen Components: [Count] ([%])
- Average Success Rate: [%]

**Workflow Library**:
- Total Workflows: [Count]
- Production-Ready: [Count] ([%])
- Average Success Rate: [%]

**Metadata Health**:
- Compliance Rate: [%]
- Orphan Rate: [%]
- Broken Link Rate: [%]

**Usage Trends**:
- Components Used (Last 7 Days): [Count]
- Workflows Executed (Last 7 Days): [Count]
- New Components Created: [Count]
```

**Insights**:
- Compliance <90% = Metadata debt accumulating
- Orphan rate >20% = Graph connectivity problem
- Zero usage = System not being used (investigate why)

### Dashboard 5: Learning Insights Log

**Purpose**: Track patterns Claude has discovered

**Format**:
```markdown
## Recent Discoveries

### YYYY-MM-DD: [Insight Name]
**Type**: Synergy / Conflict / Pattern / Gap
**Details**: [Description]
**Evidence**: [Usage data supporting this]
**Action Taken**: [What was updated]
**Status**: Validated / Needs More Data

[More entries chronologically...]
```

---

## 🧠 LEARNING MECHANISMS

### Mechanism 1: Synergy Detection

**How It Works**:
1. Track which components used together
2. Compare combined success rate vs individual rates
3. If combined > individual: Synergy detected
4. Validate over multiple uses
5. Document and recommend

**Example**:
```
Component A alone: 75% success
Component B alone: 70% success
A + B together: 95% success

Conclusion: Synergistic pair
Action: Document in both component files
```

### Mechanism 2: Conflict Detection

**How It Works**:
1. Track failed workflows
2. Analyze component combinations in failures
3. If specific pair frequently appears in failures: Conflict suspected
4. Test in isolation
5. Document and warn

**Example**:
```
[[conciseness-enforcer]] + [[example-rich-format]]

Workflows using both: 3 total, 3 failed (100% failure)
Hypothesis: Instructions contradict (be concise vs be detailed)
Action: Mark as conflicting components
```

### Mechanism 3: Success Pattern Recognition

**How It Works**:
1. Identify workflows with consistently high success
2. Extract common elements (components, strategies, problem types)
3. Formalize as "pattern"
4. Test pattern on new problems
5. If validates: Add to workflow library

**Example**:
```
Pattern Observed:
Technical content workflows succeed when using:
- [[technical-accuracy-persona]]
- [[chain-of-verification]]
- [[example-rich-format]]

Success Rate: 90% across 10 uses
Action: Create "Technical Content Workflow" template
```

### Mechanism 4: Failure Mode Analysis

**How It Works**:
1. Document all workflow failures
2. Categorize failure types
3. Identify root causes
4. Update components/workflows to address
5. Track if fixes reduce failure rate

**Common Failure Modes**:
- **Instruction Drift**: Constraints forgotten at later turns
  - Fix: Increase re-anchoring frequency
- **Scope Creep**: Turns bleeding into each other
  - Fix: Stricter scope definitions
- **Context Overload**: Too much history, attention degrades
  - Fix: Switch to summary window strategy
- **Component Incompatibility**: Conflicting instructions
  - Fix: Document conflicts, warn users

---

## 🔄 CONTINUOUS IMPROVEMENT LOOP

### Daily Activities
- [ ] Update component usage-count when used
- [ ] Rate output quality after workflows
- [ ] Log any new synergies/conflicts discovered
- [ ] Note any gaps encountered

### Weekly Activities
- [ ] Run all analytics dashboard queries
- [ ] Review learning insights log
- [ ] Identify trends in usage patterns
- [ ] Update component success-rates based on recent data
- [ ] Check for stale components (not tested in >30 days)

### Monthly Activities
- [ ] Comprehensive system health check
- [ ] Review and update SOPs based on learnings
- [ ] Analyze gap closure rate (are we filling needs?)
- [ ] Benchmark system improvement (quality trend)
- [ ] Archive inactive components (no use in 90 days)

### Quarterly Activities
- [ ] Major system review and retrospective
- [ ] User satisfaction survey (if applicable)
- [ ] Evaluate return on investment (is SPES worth it?)
- [ ] Plan next phase of system development
- [ ] Celebrate wins (what successes did SPES enable?)

---

## 📊 SUCCESS METRICS

### Component Library Metrics

| Metric | Target | Current | Trend |
|--------|--------|---------|-------|
| Evergreen Rate | >60% | TBD | TBD |
| Average Success Rate | >70% | TBD | TBD |
| Usage per Component | >5 | TBD | TBD |
| Synergies Documented | >20 | TBD | TBD |

### Workflow Performance Metrics

| Metric | Target | Current | Trend |
|--------|--------|---------|-------|
| Workflow Success Rate | >70% | TBD | TBD |
| Sequential > One-Shot | >80% cases | TBD | TBD |
| User Satisfaction | >8/10 | TBD | TBD |
| Reproducibility | >70% | TBD | TBD |

### System Learning Metrics

| Metric | Target | Current | Trend |
|--------|--------|---------|-------|
| Patterns Detected | >10 | TBD | TBD |
| Gaps Identified | >5 | TBD | TBD |
| Gaps Filled | >80% | TBD | TBD |
| Recommendation Accuracy | >75% | TBD | TBD |

---

## 🔗 Related Protocols

- [[00-librarian-core-identity]] → Learning as core capability
- [[01-component-management-sop]] → Usage tracking in component lifecycle
- [[04-quality-assurance-checklist]] → Performance measurement standards
- [[05-metadata-tagging-standards]] → Metadata enables analytics

---

*Usage Analytics Protocols Version: 1.0 | Last Updated: 2025-12-16*
