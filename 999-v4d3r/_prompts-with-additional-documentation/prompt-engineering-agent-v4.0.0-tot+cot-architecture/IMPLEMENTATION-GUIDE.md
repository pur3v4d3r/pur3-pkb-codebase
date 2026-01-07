# Implementation Guide: Prompt Engineering Agent v4.0

## Deployment Options

### Option A: Full System Prompt (Recommended for Claude)

**Best for:** Claude with extended thinking, complex prompt engineering tasks

1. **Consolidate the files** using the provided script or manually
2. **Deploy as system prompt** in Claude Projects, API, or custom interface
3. **Token consideration:** Full v4.0 is ~25K tokens as system prompt

```python
# API deployment example
import anthropic

client = anthropic.Anthropic()

# Load consolidated system prompt
with open("prompt-engineering-agent-v4-consolidated.md", "r") as f:
    system_prompt = f.read()

response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=16000,
    system=system_prompt,
    messages=[
        {"role": "user", "content": "Create a prompt for sentiment analysis of customer reviews"}
    ]
)
```

### Option B: Modular Loading (Token-Efficient)

**Best for:** API usage where token costs matter, simpler tasks

Load only the sections you need based on task complexity:

```python
def load_agent_modules(task_complexity: str) -> str:
    """Load appropriate v4.0 modules based on task complexity."""
    
    base_modules = [
        "00-overview-architecture.md",  # Always include
        "08-execution-protocol.md",      # Always include
    ]
    
    if task_complexity == "simple":
        # Minimal: just core architecture
        modules = base_modules
        
    elif task_complexity == "moderate":
        # Add conditional branching
        modules = base_modules + [
            "04-conditional-branching.md",
        ]
        
    elif task_complexity == "complex":
        # Add hybrid orchestration and CoT templates
        modules = base_modules + [
            "02-hybrid-orchestration.md",
            "03-cot-domain-templates.md",
            "04-conditional-branching.md",
        ]
        
    elif task_complexity == "production":
        # Full stack including monitoring and calibration
        modules = base_modules + [
            "02-hybrid-orchestration.md",
            "03-cot-domain-templates.md",
            "04-conditional-branching.md",
            "05-production-monitoring.md",
            "06-calibration-system.md",
        ]
    
    combined = ""
    for module in modules:
        with open(f"prompt-agent-v4/{module}", "r") as f:
            combined += f.read() + "\n\n"
    
    return combined
```

### Option C: Claude Project Integration

**Best for:** Repeated prompt engineering work, PKB integration

1. Create a new Claude Project: "Prompt Engineering Lab"
2. Add v4.0 files to Project Knowledge
3. Set custom instructions referencing the methodology

**Project Instructions Example:**
```
You are operating as the Prompt Engineering Agent v4.0. 

For every prompt engineering request:
1. Follow the nine-phase pipeline from 08-execution-protocol.md
2. Use extended thinking for exploration phases
3. Apply the appropriate domain CoT template from 03-cot-domain-templates.md
4. Include deployment specifications for production prompts

Reference the v4.0 documentation in your project knowledge for detailed procedures.
```

---

## Practical Workflow

### Step 1: Invoke the Agent

Start your request with clear framing:

```
Create a prompt for [task description].

Context:
- Target model: [Claude/GPT-4/Gemini/Local LLM]
- Use case: [one-off/production/high-volume]
- Complexity: [simple/moderate/complex]
- Special requirements: [any constraints]
```

### Step 2: Agent Executes Nine Phases

The agent will work through:

```
Phase 0: Safety Gate ──────────────────────────────────────────
         [Constitutional check - usually passes quickly]

Phase 1: Discovery ────────────────────────────────────────────
         [Requirements extraction, constraint enumeration]
         [Complexity classification → determines search mode]

Phase 2-3: Exploration ────────────────────────────────────────
         [Branch generation with multi-dimensional alternatives]
         [DFS or Hybrid Orchestration based on complexity]

Phase 4: Construction ─────────────────────────────────────────
         [SPARK framework, constraint verification]
         [Predicted quality recorded for calibration]

Phase 5: Enhancement ──────────────────────────────────────────
         [Token optimization, temperature recommendations]

Phase 6: Testing ──────────────────────────────────────────────
         [Stratified test strategy, calibration data]

Phase 7: Calibration ──────────────────────────────────────────
         [Predicted vs actual analysis]

Phase 8: Deployment Spec ──────────────────────────────────────
         [Version, baselines, thresholds, rollback triggers]

Phase 9: Deliverable ──────────────────────────────────────────
         [Complete package with all documentation]
```

### Step 3: Receive Deliverable

You'll get a structured output including:

1. **Prompt Artifact** - The actual prompt ready to use
2. **Exploration Trace** - Tree visualization of paths explored
3. **Implementation Guide** - Parameters, variables, customization
4. **Testing Evidence** - Validation results
5. **Deployment Spec** - Production configuration
6. **Alternatives** - Other high-scoring approaches preserved

---

## Example Invocations

### Simple Task (Pure ToT, fast)

```
Create a prompt for classifying customer support tickets into categories:
Billing, Technical, General, Urgent.

Context:
- Target: Claude Haiku (cost-sensitive)
- Use case: Production, high-volume
- Keep it minimal for speed
```

**Expected behavior:** 
- Skips hybrid orchestration
- Generates 2-3 technique branches at depth 0
- Selects Few-Shot (likely winner for classification)
- Adds Classification-Gated conditional branching
- Delivers with deployment spec

### Complex Task (Hybrid Orchestration)

```
Design a prompt system for an AI coding assistant that:
1. Reviews code for bugs, security, and style
2. Suggests improvements with explanations
3. Generates tests for the reviewed code
4. Adapts depth based on code complexity

Context:
- Target: Claude Sonnet with extended thinking
- Use case: Production, developer tool
- Must handle multiple languages
- Need comprehensive documentation
```

**Expected behavior:**
- Activates Hybrid Orchestration (multiple dimensions)
- Phase 1: Explores 4 strategic approaches
- Phase 2: Deep CoT analysis on primary (likely multi-stage CoT)
- Phase 3: Analyzes alternative (probably Few-Shot + Templates)
- Synthesizes best elements from both
- Uses Error-Triggered conditional branching
- Full deployment specification with monitoring thresholds

### Domain-Specific Task (Specialized CoT)

```
Create a prompt for financial risk assessment that:
- Analyzes loan applications
- Weighs multiple risk factors
- Produces structured risk scores
- Explains reasoning for compliance

Context:
- Target: Claude Opus (accuracy critical)
- Use case: Production, regulated industry
- Must be auditable
- Fixed output structure required (compliance)
```

**Expected behavior:**
- Uses Analytical CoT template (stakeholder analysis, decision framework)
- Applies Constitutional constraints (financial advice disclaimers)
- Selects Fixed Structure conditional pattern (audit requirement)
- Hybrid mode for explicit trade-off documentation
- Comprehensive calibration tracking

---

## Model-Specific Deployment

### Claude (Recommended)

```yaml
deployment:
  model: claude-sonnet-4-20250514
  features:
    - extended_thinking: true  # Enable for exploration phases
    - xml_tags: true           # Use for structure
  temperature: 0.3-0.5         # From grid search
  max_tokens: 8000-16000       # Allow comprehensive output
```

### GPT-4

```yaml
deployment:
  model: gpt-4-turbo
  adaptations:
    - Convert XML structure to markdown headers
    - Use system/user message separation
    - Simplify exploration trace format
  temperature: 0.3-0.7
  max_tokens: 4000-8000
```

### Local LLMs (Llama, Mistral)

```yaml
deployment:
  adaptations:
    - Reduce system prompt size (modular loading)
    - Simplify CoT templates
    - Skip production monitoring section
    - Focus on core exploration + construction
  considerations:
    - Token limits often lower
    - May need explicit "think step by step" triggers
    - Reduce branching (2 branches vs 4)
```

---

## Integration with PKB Workflow

### Storing Generated Prompts

Each deliverable can become a PKB note:

```yaml
---
tags: #prompt-engineering #production #domain/customer-support
aliases: [Support Ticket Classifier, Ticket Triage Prompt]
created: 2024-01-15
status: evergreen
type: reference
exploration_path: "root → A → A.1 → A.1.2"
techniques: [few-shot, constitutional, classification-gated]
calibration_status: well_calibrated
---

# Support Ticket Classification Prompt v1.0

## Prompt Artifact
[The actual prompt]

## Exploration Trace
[Tree visualization - collapsible in Obsidian]

## Implementation
[Parameters, variables]

## Connections
- [[Prompt Engineering Agent v4.0]] - Generation methodology
- [[Few-Shot Learning]] - Primary technique used
- [[Customer Support Automation]] - Application domain
```

### Tracking Calibration Over Time

Create a calibration log note:

```yaml
---
tags: #prompt-engineering #calibration #meta
type: log
---

# Prompt Calibration Log

## Entry: 2024-01-15

| Prompt | Predicted | Actual | Delta | Status |
|--------|-----------|--------|-------|--------|
| [[Ticket Classifier]] | 8.5 | 8.2 | 0.3 | ✓ |
| [[Code Reviewer]] | 8.8 | 7.9 | 0.9 | ⚠️ |

### Patterns Identified
- CoT + complex conditional: tends to overestimate by 0.5-1.0

### Adjustments Made
- For CoT + conditional: subtract 0.5 from quality estimate
```

---

## Quick Start Checklist

1. [ ] Choose deployment option (A, B, or C)
2. [ ] Consolidate or load appropriate modules
3. [ ] Deploy as system prompt or project knowledge
4. [ ] Test with simple task first
5. [ ] Verify exploration trace appears in output
6. [ ] Test with complex task to validate hybrid mode
7. [ ] Store first deliverable in PKB
8. [ ] Start calibration tracking

---

## Troubleshooting

### Agent skips exploration
**Cause:** Task classified as too simple
**Fix:** Add complexity indicators: "comprehensive", "production-grade", "explore alternatives"

### No deployment specification
**Cause:** Modular loading without `05-production-monitoring.md`
**Fix:** Include monitoring module or specify "include deployment spec"

### Hybrid mode not activating
**Cause:** Complexity threshold not met
**Fix:** Explicitly state multiple dimensions, stakeholders, or request "use hybrid orchestration"

### Calibration data missing
**Cause:** Testing phase skipped or simplified
**Fix:** Request "include calibration tracking" or include calibration module
