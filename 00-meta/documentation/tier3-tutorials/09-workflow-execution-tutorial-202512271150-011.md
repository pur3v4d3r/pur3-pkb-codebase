---
title: SPES Workflow Execution Tutorial
document_type: tutorial
tier: 2
priority: critical
version: 2.0.0
status: published
prerequisites: ["Quick Start Guide", "Component Library Reference"]
estimated_time: 120-180 minutes
last_updated: 2025-12-25
---

# SPES Workflow Execution Tutorial

**Version**: 2.0.0  
**Document Type**: Progressive Tutorial  
**Audience**: Workflow designers, advanced users  
**Time Required**: 120-180 minutes  
**Goal**: Master multi-step workflow design and execution

---

## Table of Contents

1. [Learning Objectives](#1-learning-objectives)
2. [Workflow Fundamentals](#2-workflow-fundamentals)
3. [Tutorial 1: Simple Sequential Workflow](#3-tutorial-1-simple-sequential-workflow)
4. [Tutorial 2: Context Handoff Patterns](#4-tutorial-2-context-handoff-patterns)
5. [Tutorial 3: Multi-LLM Workflows](#5-tutorial-3-multi-llm-workflows)
6. [Tutorial 4: Conditional Workflows](#6-tutorial-4-conditional-workflows)
7. [Tutorial 5: Error Handling & Recovery](#7-tutorial-5-error-handling--recovery)
8. [Tutorial 6: Production Workflows](#8-tutorial-6-production-workflows)
9. [Advanced Patterns](#9-advanced-patterns)
10. [Best Practices](#10-best-practices)

---

## 1. Learning Objectives

By completing this tutorial, you will:

✅ **Understand Workflow Architecture**
- Workflow definition and structure
- Step dependencies and data flow
- State management across steps
- Context accumulation strategies

✅ **Master Sequential Workflows**
- Chain multiple LLM calls
- Pass context between steps
- Validate intermediate outputs
- Handle step failures

✅ **Implement Multi-LLM Patterns**
- Select optimal LLM per step
- Fallback to alternative LLMs
- Mix cloud and local LLMs
- Optimize for cost/speed/quality

✅ **Build Production-Ready Workflows**
- Comprehensive error handling
- Retry logic with backoff
- Validation at each step
- Logging and monitoring

✅ **Apply Advanced Techniques**
- Conditional branching
- Parallel execution
- Dynamic component selection
- Workflow templates

---

## 2. Workflow Fundamentals

### 2.1 What is a Workflow?

**Definition**: A workflow is a sequence of steps where each step:
1. Receives input (from user or previous step)
2. Composes a prompt from components
3. Executes with an LLM
4. Validates output
5. Passes result to next step

**Simple Workflow Diagram**:
```
┌─────────────┐
│   Input     │
└──────┬──────┘
       │
       ▼
┌─────────────────────────────────┐
│  Step 1: Generate Outline       │
│  Components: instruction-outline │
│  LLM: Claude Sonnet             │
└──────┬──────────────────────────┘
       │ (outline)
       ▼
┌─────────────────────────────────┐
│  Step 2: Write Content          │
│  Components: instruction-write   │
│  LLM: Claude Sonnet             │
│  Input: Step 1 output           │
└──────┬──────────────────────────┘
       │ (draft)
       ▼
┌─────────────────────────────────┐
│  Step 3: Review & Edit          │
│  Components: instruction-review  │
│  LLM: Claude Sonnet             │
│  Input: Step 2 output           │
└──────┬──────────────────────────┘
       │ (final)
       ▼
┌─────────────┐
│   Output    │
└─────────────┘
```

### 2.2 Workflow Specification Format

**YAML Workflow Definition**:
```yaml
workflow:
  name: "Content Generation Pipeline"
  version: "1.0.0"
  description: "Generate structured content from outline to final draft"
  
  steps:
    - id: step_1
      name: "Generate Outline"
      components:
        - instruction-create-outline-v1.0.0
        - format-bullet-list-v1.0.0
      llm:
        provider: claude
        model: sonnet-4
      context_strategy: fresh
      
    - id: step_2
      name: "Write Content"
      components:
        - instruction-write-content-v1.0.0
        - persona-technical-writer-v1.0.0
      llm:
        provider: claude
        model: sonnet-4
      context_strategy: full_accumulation
      depends_on: step_1
      
    - id: step_3
      name: "Review and Polish"
      components:
        - instruction-review-content-v1.0.0
        - constraint-clear-writing-v1.0.0
      llm:
        provider: claude
        model: sonnet-4
      context_strategy: selective_handoff
      depends_on: step_2
```

### 2.3 Context Handoff Strategies

**Four Primary Strategies**:

```python
class ContextStrategy(Enum):
    """Context handoff strategies for workflow steps."""
    
    FRESH = "fresh"
    # No previous context, only current step input
    # Use: When step is independent
    
    FULL_ACCUMULATION = "full_accumulation"
    # All previous outputs appended
    # Use: When context builds progressively
    
    SELECTIVE_HANDOFF = "selective_handoff"
    # Only specific previous outputs included
    # Use: When only certain context needed
    
    SUMMARIZED_CONTEXT = "summarized_context"
    # Previous context summarized before passing
    # Use: When context would exceed token limits
```

**When to Use Each**:

| Strategy | Use Case | Token Usage | Example |
|----------|----------|-------------|---------|
| **Fresh** | Independent steps | Low | Parallel tasks |
| **Full Accumulation** | Building narrative | High | Story writing |
| **Selective Handoff** | Specific dependencies | Medium | Code review |
| **Summarized** | Long workflows | Controlled | Multi-stage analysis |

---

## 3. Tutorial 1: Simple Sequential Workflow

### 3.1 Goal

Build a 3-step workflow that:
1. Analyzes requirements
2. Generates code
3. Creates tests

**Time**: 30 minutes

### 3.2 Create Required Components

**Step 1: Analyze Requirements Component**:

```bash
cd ~/PKB-System/spes/components/core/instructions

cat > instruction-analyze-requirements-v1.0.0.md << 'EOF'
---
title: Instruction - Analyze Code Requirements
type: instruction
version: 1.0.0
status: published
tags: [instruction, analysis, requirements]
context_budget: 400
---

# Requirements Analysis Task

You will analyze the user's code requirements and create a structured specification.

# Analysis Process

1. **Identify Core Functionality**: What must the code do?
2. **Determine Inputs/Outputs**: What data flows in and out?
3. **List Constraints**: Performance, security, compatibility requirements
4. **Note Edge Cases**: Unusual scenarios to handle
5. **Suggest Approach**: High-level implementation strategy

# Output Format

Provide a structured analysis:

## Core Functionality
- [Primary function 1]
- [Primary function 2]

## Inputs/Outputs
- **Inputs**: [data types and sources]
- **Outputs**: [data types and destinations]

## Constraints
- [Constraint 1]
- [Constraint 2]

## Edge Cases
- [Edge case 1]
- [Edge case 2]

## Recommended Approach
[Brief implementation strategy]
EOF
```

**Step 2: Generate Code Component** (already exists from Quick Start):
```bash
# Verify it exists
ls instruction-code-generation-v1.0.0.md
```

**Step 3: Create Tests Component**:

```bash
cat > instruction-create-tests-v1.0.0.md << 'EOF'
---
title: Instruction - Create Unit Tests
type: instruction
version: 1.0.0
status: published
tags: [instruction, testing, pytest]
context_budget: 450
---

# Test Creation Task

You will create comprehensive unit tests for the provided code using pytest.

# Test Requirements

Your tests must:
- Cover all major functions/methods
- Test normal cases and edge cases
- Test error handling
- Use descriptive test names
- Include docstrings explaining what's tested
- Use pytest conventions and fixtures

# Test Structure

```python
import pytest

def test_function_name_normal_case():
    """Test normal operation of function_name."""
    # Arrange
    input_data = ...
    
    # Act
    result = function_name(input_data)
    
    # Assert
    assert result == expected_value

def test_function_name_edge_case():
    """Test edge case handling."""
    ...

def test_function_name_error_handling():
    """Test that appropriate errors are raised."""
    with pytest.raises(ValueError):
        function_name(invalid_input)
```

# Coverage Goals

Aim for:
- 80%+ code coverage
- All public functions tested
- All error paths tested
EOF
```

### 3.3 Create Workflow Script

```bash
cd ~/PKB-System/spes

cat > workflow_tutorial_1.py << 'EOF'
#!/usr/bin/env python3
"""
Tutorial 1: Simple Sequential Workflow
Three steps: Analyze → Generate → Test
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from anthropic import Anthropic
from dataclasses import dataclass
from typing import List, Optional

load_dotenv()

@dataclass
class WorkflowStep:
    """Represents a single workflow step."""
    id: str
    name: str
    components: List[str]
    llm_provider: str = "claude"
    llm_model: str = "claude-sonnet-4-20250514"

@dataclass
class StepResult:
    """Result from executing a workflow step."""
    step_id: str
    success: bool
    output: str
    error: Optional[str] = None

class SimpleWorkflowEngine:
    """Minimal workflow execution engine."""
    
    def __init__(self):
        self.client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        self.base_path = Path(__file__).parent
    
    def load_component(self, component_name: str) -> str:
        """Load component content."""
        component_path = self.base_path / "components/core" / component_name
        
        # Try different subdirectories
        for subdir in ["instructions", "personas", "formats", "constraints"]:
            full_path = self.base_path / f"components/core/{subdir}/{component_name}"
            if full_path.exists():
                content = full_path.read_text()
                # Skip YAML frontmatter
                if content.startswith('---'):
                    parts = content.split('---', 2)
                    if len(parts) >= 3:
                        return parts[2].strip()
                return content
        
        raise FileNotFoundError(f"Component not found: {component_name}")
    
    def compose_prompt(self, components: List[str], context: str) -> str:
        """Compose components and context into prompt."""
        sections = []
        
        # Load all components
        for component in components:
            sections.append(self.load_component(component))
        
        # Add context
        sections.append(f"\n\n# Input\n\n{context}")
        
        return "\n\n".join(sections)
    
    def execute_step(self, step: WorkflowStep, context: str) -> StepResult:
        """Execute a single workflow step."""
        try:
            print(f"\n{'='*60}")
            print(f"Executing: {step.name}")
            print(f"{'='*60}")
            
            # Compose prompt
            prompt = self.compose_prompt(step.components, context)
            
            # Execute with LLM
            response = self.client.messages.create(
                model=step.llm_model,
                max_tokens=4096,
                messages=[{"role": "user", "content": prompt}]
            )
            
            output = response.content[0].text
            
            print(f"\n✓ Step completed successfully")
            print(f"Output length: {len(output)} characters")
            
            return StepResult(
                step_id=step.id,
                success=True,
                output=output
            )
            
        except Exception as e:
            print(f"\n✗ Step failed: {e}")
            return StepResult(
                step_id=step.id,
                success=False,
                output="",
                error=str(e)
            )
    
    def execute_workflow(self, steps: List[WorkflowStep], initial_input: str):
        """Execute complete workflow with context accumulation."""
        
        print("\n" + "="*60)
        print("WORKFLOW EXECUTION STARTED")
        print("="*60)
        
        results = []
        accumulated_context = initial_input
        
        for i, step in enumerate(steps, 1):
            print(f"\n--- Step {i}/{len(steps)} ---")
            
            # Execute step
            result = self.execute_step(step, accumulated_context)
            results.append(result)
            
            # Check if step failed
            if not result.success:
                print(f"\n✗ Workflow failed at step: {step.name}")
                break
            
            # Accumulate context for next step
            accumulated_context = (
                f"Previous step ({step.name}) output:\n\n"
                f"{result.output}\n\n"
                f"---\n\n"
                f"Original request: {initial_input}"
            )
        
        # Display final results
        self.display_results(results)
        
        return results
    
    def display_results(self, results: List[StepResult]):
        """Display workflow results."""
        print("\n\n" + "="*60)
        print("WORKFLOW RESULTS")
        print("="*60)
        
        for i, result in enumerate(results, 1):
            print(f"\n--- Step {i}: {result.step_id} ---")
            if result.success:
                print("✓ Success")
                print(f"\nOutput:\n{result.output[:500]}...")
                if len(result.output) > 500:
                    print(f"\n[Output truncated. Full length: {len(result.output)} chars]")
            else:
                print(f"✗ Failed: {result.error}")
        
        print("\n" + "="*60)

def main():
    """Run Tutorial 1 workflow."""
    
    # Define workflow steps
    steps = [
        WorkflowStep(
            id="analyze",
            name="Analyze Requirements",
            components=[
                "instruction-analyze-requirements-v1.0.0.md",
            ]
        ),
        WorkflowStep(
            id="generate",
            name="Generate Code",
            components=[
                "persona-python-expert-v1.0.0.md",
                "instruction-code-generation-v1.0.0.md",
            ]
        ),
        WorkflowStep(
            id="test",
            name="Create Unit Tests",
            components=[
                "instruction-create-tests-v1.0.0.md",
            ]
        ),
    ]
    
    # User request
    user_request = """
    Create a Python function that validates email addresses.
    It should check for proper format and optionally verify the domain exists.
    """
    
    # Execute workflow
    engine = SimpleWorkflowEngine()
    results = engine.execute_workflow(steps, user_request)
    
    # Check if all succeeded
    all_success = all(r.success for r in results)
    
    if all_success:
        print("\n✓ Workflow completed successfully!")
    else:
        print("\n✗ Workflow completed with errors")

if __name__ == "__main__":
    main()
EOF

chmod +x workflow_tutorial_1.py
```

### 3.4 Execute the Workflow

```bash
cd ~/PKB-System/spes
source ../spes-env/bin/activate

python workflow_tutorial_1.py
```

**Expected Output**:
```
============================================================
WORKFLOW EXECUTION STARTED
============================================================

--- Step 1/3 ---
============================================================
Executing: Analyze Requirements
============================================================

✓ Step completed successfully
Output length: 847 characters

--- Step 2/3 ---
============================================================
Executing: Generate Code
============================================================

✓ Step completed successfully
Output length: 1543 characters

--- Step 3/3 ---
============================================================
Executing: Create Unit Tests
============================================================

✓ Step completed successfully
Output length: 2134 characters


============================================================
WORKFLOW RESULTS
============================================================

--- Step 1: analyze ---
✓ Success

Output:
## Core Functionality
- Validate email address format using regex
- Optionally verify domain exists via DNS lookup

[... full output ...]
```

### 3.5 ✅ Checkpoint

You should now have:
- [x] Three workflow steps executed sequentially
- [x] Context passed between steps
- [x] Complete code + tests generated
- [x] Understanding of basic workflow structure

---

## 4. Tutorial 2: Context Handoff Patterns

### 4.1 Goal

Learn the four context handoff strategies by building examples of each.

**Time**: 30 minutes

### 4.2 Strategy 1: Fresh Context

**Use Case**: Independent parallel tasks

```python
# workflow_tutorial_2a_fresh.py
cat > workflow_tutorial_2a_fresh.py << 'EOF'
#!/usr/bin/env python3
"""
Tutorial 2a: Fresh Context Strategy
Each step gets only its own input, no previous context
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

def execute_with_fresh_context(prompt: str) -> str:
    """Execute step with fresh context only."""
    client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.content[0].text

def main():
    """Run parallel independent tasks."""
    
    print("Fresh Context Strategy: Parallel Independent Tasks\n")
    
    base_input = "Python programming"
    
    # Task 1: Generate tutorial outline
    task1_prompt = f"Create a tutorial outline for learning {base_input}"
    print("Task 1: Tutorial Outline")
    result1 = execute_with_fresh_context(task1_prompt)
    print(f"✓ Completed ({len(result1)} chars)\n")
    
    # Task 2: Generate practice exercises (independent of Task 1)
    task2_prompt = f"Create 5 practice exercises for learning {base_input}"
    print("Task 2: Practice Exercises")
    result2 = execute_with_fresh_context(task2_prompt)
    print(f"✓ Completed ({len(result2)} chars)\n")
    
    # Task 3: Generate quiz questions (independent of Task 1 & 2)
    task3_prompt = f"Create 10 quiz questions about {base_input}"
    print("Task 3: Quiz Questions")
    result3 = execute_with_fresh_context(task3_prompt)
    print(f"✓ Completed ({len(result3)} chars)\n")
    
    print("All tasks completed independently!")

if __name__ == "__main__":
    main()
EOF

python workflow_tutorial_2a_fresh.py
```

### 4.3 Strategy 2: Full Accumulation

**Use Case**: Building progressive narrative

```python
cat > workflow_tutorial_2b_accumulation.py << 'EOF'
#!/usr/bin/env python3
"""
Tutorial 2b: Full Accumulation Strategy
Each step receives all previous context
"""

import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

def execute_step_with_accumulation(prompt: str, accumulated_context: str) -> str:
    """Execute step with all previous context."""
    client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    
    # Combine accumulated context with new prompt
    full_prompt = f"{accumulated_context}\n\n---\n\n{prompt}"
    
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=2048,
        messages=[{"role": "user", "content": full_prompt}]
    )
    
    return response.content[0].text

def main():
    """Build a story with full context accumulation."""
    
    print("Full Accumulation Strategy: Progressive Story Building\n")
    
    # Start with initial context
    accumulated = ""
    
    # Step 1: Create character
    print("Step 1: Create Character")
    prompt1 = "Create a detailed character: name, background, personality, motivation"
    result1 = execute_step_with_accumulation(prompt1, accumulated)
    accumulated = f"Character:\n{result1}"
    print(f"✓ Character created\n")
    
    # Step 2: Create setting (uses character context)
    print("Step 2: Create Setting")
    prompt2 = (
        "Based on the character above, create an appropriate setting "
        "where this character's story will take place"
    )
    result2 = execute_step_with_accumulation(prompt2, accumulated)
    accumulated += f"\n\nSetting:\n{result2}"
    print(f"✓ Setting created\n")
    
    # Step 3: Create conflict (uses character + setting)
    print("Step 3: Create Conflict")
    prompt3 = (
        "Based on the character and setting above, create a compelling conflict "
        "that this character must face"
    )
    result3 = execute_step_with_accumulation(prompt3, accumulated)
    accumulated += f"\n\nConflict:\n{result3}"
    print(f"✓ Conflict created\n")
    
    # Step 4: Write opening scene (uses all previous context)
    print("Step 4: Write Opening Scene")
    prompt4 = (
        "Based on all the elements above (character, setting, conflict), "
        "write the opening scene of the story (300-400 words)"
    )
    result4 = execute_step_with_accumulation(prompt4, accumulated)
    print(f"✓ Opening scene written\n")
    
    print("="*60)
    print("FINAL STORY OPENING")
    print("="*60)
    print(result4)

if __name__ == "__main__":
    main()
EOF

python workflow_tutorial_2b_accumulation.py
```

### 4.4 Strategy 3: Selective Handoff

**Use Case**: Only specific previous outputs needed

```python
cat > workflow_tutorial_2c_selective.py << 'EOF'
#!/usr/bin/env python3
"""
Tutorial 2c: Selective Handoff Strategy
Each step receives only specific previous outputs
"""

import os
from dotenv import load_dotenv
from anthropic import Anthropic
from typing import Dict

load_dotenv()

class SelectiveWorkflowEngine:
    """Workflow engine with selective context handoff."""
    
    def __init__(self):
        self.client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        self.outputs = {}  # Store all step outputs
    
    def execute_step(self, step_id: str, prompt: str, 
                     required_context: list = None) -> str:
        """Execute step with selective context."""
        
        # Build context from only required previous outputs
        context_parts = []
        if required_context:
            for req_id in required_context:
                if req_id in self.outputs:
                    context_parts.append(
                        f"Output from {req_id}:\n{self.outputs[req_id]}"
                    )
        
        # Combine selected context with new prompt
        if context_parts:
            full_prompt = "\n\n---\n\n".join(context_parts)
            full_prompt += f"\n\n---\n\n{prompt}"
        else:
            full_prompt = prompt
        
        # Execute
        response = self.client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=2048,
            messages=[{"role": "user", "content": full_prompt}]
        )
        
        output = response.content[0].text
        self.outputs[step_id] = output
        
        return output

def main():
    """Code review workflow with selective context."""
    
    print("Selective Handoff Strategy: Code Review Workflow\n")
    
    engine = SelectiveWorkflowEngine()
    
    # Step 1: Generate code
    print("Step 1: Generate Code")
    code = engine.execute_step(
        step_id="code",
        prompt="Create a Python function to calculate prime numbers up to n"
    )
    print("✓ Code generated\n")
    
    # Step 2: Analyze performance (needs only code)
    print("Step 2: Analyze Performance")
    perf = engine.execute_step(
        step_id="performance",
        prompt="Analyze the performance characteristics and suggest optimizations",
        required_context=["code"]  # Only needs the code
    )
    print("✓ Performance analysis done\n")
    
    # Step 3: Analyze security (needs only code)
    print("Step 3: Analyze Security")
    security = engine.execute_step(
        step_id="security",
        prompt="Review for security issues and suggest improvements",
        required_context=["code"]  # Only needs the code, not performance
    )
    print("✓ Security analysis done\n")
    
    # Step 4: Create final report (needs all analyses, not original code)
    print("Step 4: Create Summary Report")
    report = engine.execute_step(
        step_id="report",
        prompt=(
            "Create a summary report combining the performance and security "
            "analyses. List key findings and recommendations."
        ),
        required_context=["performance", "security"]  # Not code, just analyses
    )
    print("✓ Report created\n")
    
    print("="*60)
    print("FINAL REPORT")
    print("="*60)
    print(report)

if __name__ == "__main__":
    main()
EOF

python workflow_tutorial_2c_selective.py
```

### 4.5 Strategy 4: Summarized Context

**Use Case**: Long workflows exceeding token limits

```python
cat > workflow_tutorial_2d_summarized.py << 'EOF'
#!/usr/bin/env python3
"""
Tutorial 2d: Summarized Context Strategy
Summarize accumulated context to stay within token limits
"""

import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

def summarize_context(context: str, max_length: int = 1000) -> str:
    """Summarize context if it exceeds max_length."""
    
    if len(context) <= max_length:
        return context
    
    client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    
    summary_prompt = f"""
Summarize this context concisely, preserving key information:

{context}

Provide a summary in about {max_length // 4} words that captures the essential points.
"""
    
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=512,
        messages=[{"role": "user", "content": summary_prompt}]
    )
    
    return response.content[0].text

def execute_with_summarization(prompt: str, context: str, 
                               max_context_length: int = 1000) -> str:
    """Execute step with summarized context if needed."""
    
    client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    
    # Summarize if context too long
    if len(context) > max_context_length:
        print(f"  [Context too long ({len(context)} chars), summarizing...]")
        context = summarize_context(context, max_context_length)
        print(f"  [Summarized to {len(context)} chars]")
    
    full_prompt = f"Context:\n{context}\n\n---\n\n{prompt}"
    
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=2048,
        messages=[{"role": "user", "content": full_prompt}]
    )
    
    return response.content[0].text

def main():
    """Multi-stage document analysis with summarization."""
    
    print("Summarized Context Strategy: Long Document Analysis\n")
    
    # Simulate a long document by concatenating multiple sections
    accumulated = ""
    
    # Stage 1-5: Analyze different aspects (builds up context)
    aspects = [
        "technical accuracy",
        "clarity and readability", 
        "structure and organization",
        "completeness",
        "consistency"
    ]
    
    doc_to_analyze = "Python is a high-level programming language..." * 50
    
    for i, aspect in enumerate(aspects, 1):
        print(f"Stage {i}: Analyze {aspect}")
        
        prompt = f"Analyze this document for {aspect}. Provide 2-3 key findings."
        result = execute_with_summarization(
            prompt,
            f"Document:\n{doc_to_analyze}\n\nPrevious analyses:\n{accumulated}",
            max_context_length=2000
        )
        
        accumulated += f"\n\n{aspect.title()}: {result}"
        print(f"✓ Analysis completed ({len(accumulated)} total context)\n")
    
    # Final stage: Overall recommendation
    print("Stage 6: Create Overall Recommendation")
    final_prompt = "Based on all analyses above, provide overall recommendations."
    final = execute_with_summarization(final_prompt, accumulated, 2000)
    
    print("\n" + "="*60)
    print("FINAL RECOMMENDATIONS")
    print("="*60)
    print(final)

if __name__ == "__main__":
    main()
EOF

python workflow_tutorial_2d_summarized.py
```

### 4.6 ✅ Checkpoint

You should now understand:
- [x] When to use each context strategy
- [x] How to implement each pattern
- [x] Trade-offs (token usage vs context richness)
- [x] Practical examples of each

---

## 5. Tutorial 3: Multi-LLM Workflows

### 5.1 Goal

Learn to select optimal LLMs for different steps and implement fallback strategies.

**Time**: 30 minutes

### 5.2 LLM Selection Matrix

**Quick Reference**:

| Task Type | Primary LLM | Fallback | Reasoning |
|-----------|-------------|----------|-----------|
| **Code Generation** | Claude Code | Claude API | Agentic coding tools |
| **Fast Analysis** | Gemini Flash | Claude | Speed + cost |
| **Deep Reasoning** | Claude Opus | Claude Sonnet | Maximum capability |
| **Local/Private** | Ollama CodeLlama | LM Studio | Privacy |
| **Bulk Processing** | Gemini | Claude | Cost efficiency |

### 5.3 Multi-LLM Workflow Example

```python
cat > workflow_tutorial_3_multi_llm.py << 'EOF'
#!/usr/bin/env python3
"""
Tutorial 3: Multi-LLM Workflow
Use optimal LLM for each step with fallback support
"""

import os
from dotenv import load_dotenv
from anthropic import Anthropic
import google.generativeai as genai
from enum import Enum
from typing import Optional

load_dotenv()

class LLMProvider(Enum):
    """Available LLM providers."""
    CLAUDE = "claude"
    GEMINI = "gemini"
    OLLAMA = "ollama"

class MultiLLMEngine:
    """Workflow engine with multi-LLM support."""
    
    def __init__(self):
        # Initialize clients
        self.claude_client = Anthropic(
            api_key=os.getenv("ANTHROPIC_API_KEY")
        )
        
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        self.gemini_model = genai.GenerativeModel('gemini-2.0-flash-exp')
    
    def execute_with_llm(
        self, 
        prompt: str, 
        provider: LLMProvider,
        fallback: Optional[LLMProvider] = None
    ) -> str:
        """Execute prompt with specified LLM, fallback if fails."""
        
        try:
            if provider == LLMProvider.CLAUDE:
                return self._execute_claude(prompt)
            elif provider == LLMProvider.GEMINI:
                return self._execute_gemini(prompt)
            elif provider == LLMProvider.OLLAMA:
                return self._execute_ollama(prompt)
        
        except Exception as e:
            print(f"  ⚠ {provider.value} failed: {e}")
            
            if fallback:
                print(f"  ↻ Falling back to {fallback.value}")
                return self.execute_with_llm(prompt, fallback, fallback=None)
            else:
                raise
    
    def _execute_claude(self, prompt: str) -> str:
        """Execute with Claude."""
        response = self.claude_client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text
    
    def _execute_gemini(self, prompt: str) -> str:
        """Execute with Gemini."""
        response = self.gemini_model.generate_content(prompt)
        return response.text
    
    def _execute_ollama(self, prompt: str) -> str:
        """Execute with Ollama (simplified)."""
        import requests
        
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3:8b",
                "prompt": prompt,
                "stream": False
            }
        )
        
        if response.status_code == 200:
            return response.json()["response"]
        else:
            raise Exception(f"Ollama API error: {response.status_code}")

def main():
    """Run multi-LLM workflow optimized for each task."""
    
    print("Multi-LLM Workflow: Optimized Task Assignment\n")
    
    engine = MultiLLMEngine()
    
    # Step 1: Fast initial analysis with Gemini
    print("Step 1: Quick Analysis (Gemini + fallback to Claude)")
    prompt1 = """
Analyze this business requirement in 3 bullet points:
"Build a customer dashboard showing sales metrics, user activity, and support tickets."
"""
    
    result1 = engine.execute_with_llm(
        prompt1,
        provider=LLMProvider.GEMINI,
        fallback=LLMProvider.CLAUDE
    )
    print(f"✓ Quick analysis completed\n")
    
    # Step 2: Deep reasoning for architecture with Claude
    print("Step 2: Architecture Design (Claude)")
    prompt2 = f"""
Based on this analysis:
{result1}

Design a detailed technical architecture including:
- Frontend components
- Backend services
- Database schema
- API endpoints
"""
    
    result2 = engine.execute_with_llm(
        prompt2,
        provider=LLMProvider.CLAUDE
    )
    print(f"✓ Architecture designed\n")
    
    # Step 3: Generate code with Claude (best for code)
    print("Step 3: Generate Sample Code (Claude)")
    prompt3 = f"""
Based on this architecture:
{result2}

Generate a Python FastAPI endpoint for fetching sales metrics.
Include proper error handling and documentation.
"""
    
    result3 = engine.execute_with_llm(
        prompt3,
        provider=LLMProvider.CLAUDE
    )
    print(f"✓ Code generated\n")
    
    # Step 4: Quick documentation with Gemini (cost-effective)
    print("Step 4: Generate README (Gemini + fallback to Claude)")
    prompt4 = f"""
Create a brief README.md for this API endpoint.
Include installation, usage, and examples.

{result3}
"""
    
    result4 = engine.execute_with_llm(
        prompt4,
        provider=LLMProvider.GEMINI,
        fallback=LLMProvider.CLAUDE
    )
    print(f"✓ Documentation created\n")
    
    print("="*60)
    print("FINAL README")
    print("="*60)
    print(result4)
    
    print("\n" + "="*60)
    print("LLM Usage Summary:")
    print("  Gemini: 2 steps (fast analysis, documentation)")
    print("  Claude: 2 steps (architecture, code generation)")
    print("  Benefit: Optimized for speed/cost/quality")
    print("="*60)

if __name__ == "__main__":
    main()
EOF

python workflow_tutorial_3_multi_llm.py
```

### 5.4 LLM Selection Best Practices

**Decision Framework**:

```python
def select_optimal_llm(task_characteristics: dict) -> LLMProvider:
    """Select best LLM based on task characteristics."""
    
    # Code generation/modification
    if task_characteristics.get("involves_code"):
        if task_characteristics.get("requires_agentic_tools"):
            return LLMProvider.CLAUDE_CODE
        else:
            return LLMProvider.CLAUDE
    
    # Privacy-sensitive
    if task_characteristics.get("privacy_sensitive"):
        return LLMProvider.OLLAMA
    
    # Speed-critical
    if task_characteristics.get("latency_critical"):
        return LLMProvider.GEMINI
    
    # Deep reasoning required
    if task_characteristics.get("complex_reasoning"):
        return LLMProvider.CLAUDE_OPUS
    
    # Bulk processing (cost-sensitive)
    if task_characteristics.get("high_volume"):
        return LLMProvider.GEMINI
    
    # Default
    return LLMProvider.CLAUDE
```

### 5.5 ✅ Checkpoint

You should now be able to:
- [x] Select appropriate LLM for different task types
- [x] Implement multi-LLM workflows
- [x] Add fallback strategies
- [x] Optimize for speed/cost/quality trade-offs

---

## 6. Tutorial 4: Conditional Workflows

### 6.1 Goal

Build workflows with conditional branching based on intermediate results.

**Time**: 20 minutes

### 6.2 Conditional Workflow Pattern

```python
cat > workflow_tutorial_4_conditional.py << 'EOF'
#!/usr/bin/env python3
"""
Tutorial 4: Conditional Workflows
Branch execution based on intermediate results
"""

import os
from dotenv import load_dotenv
from anthropic import Anthropic
from enum import Enum

load_dotenv()

class AnalysisResult(Enum):
    """Possible analysis outcomes."""
    SIMPLE = "simple"
    MODERATE = "moderate"
    COMPLEX = "complex"

class ConditionalWorkflowEngine:
    """Workflow engine with conditional branching."""
    
    def __init__(self):
        self.client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    
    def execute(self, prompt: str) -> str:
        """Execute LLM call."""
        response = self.client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=2048,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text
    
    def assess_complexity(self, requirements: str) -> AnalysisResult:
        """Assess complexity of requirements."""
        
        assessment_prompt = f"""
Analyze these requirements and classify complexity:

{requirements}

Respond with ONLY ONE WORD:
- SIMPLE: Basic CRUD, single table, no special logic
- MODERATE: Multiple tables, some business logic
- COMPLEX: Advanced algorithms, integrations, scalability needs

Classification:"""
        
        result = self.execute(assessment_prompt).strip().upper()
        
        if "SIMPLE" in result:
            return AnalysisResult.SIMPLE
        elif "COMPLEX" in result:
            return AnalysisResult.COMPLEX
        else:
            return AnalysisResult.MODERATE
    
    def execute_simple_path(self, requirements: str) -> str:
        """Simple path: Direct code generation."""
        print("→ Taking SIMPLE path: Direct generation")
        
        prompt = f"""
Generate code for these simple requirements:
{requirements}

Provide complete, working code with basic error handling.
"""
        return self.execute(prompt)
    
    def execute_moderate_path(self, requirements: str) -> str:
        """Moderate path: Design then code."""
        print("→ Taking MODERATE path: Design + Code")
        
        # Step 1: Design
        design_prompt = f"""
Create a design for these requirements:
{requirements}

Provide:
1. Component breakdown
2. Data structures
3. Key algorithms
"""
        design = self.execute(design_prompt)
        print("  ✓ Design completed")
        
        # Step 2: Implement based on design
        impl_prompt = f"""
Based on this design:
{design}

Generate the implementation with:
- Well-structured code
- Error handling
- Documentation
"""
        code = self.execute(impl_prompt)
        print("  ✓ Implementation completed")
        
        return code
    
    def execute_complex_path(self, requirements: str) -> str:
        """Complex path: Analysis → Design → Code → Review."""
        print("→ Taking COMPLEX path: Full workflow")
        
        # Step 1: Detailed analysis
        analysis_prompt = f"""
Perform detailed analysis of requirements:
{requirements}

Provide:
1. Use cases
2. Non-functional requirements
3. Potential challenges
4. Recommended approach
"""
        analysis = self.execute(analysis_prompt)
        print("  ✓ Analysis completed")
        
        # Step 2: Architecture design
        arch_prompt = f"""
Based on this analysis:
{analysis}

Design system architecture including:
- Components and their responsibilities
- Data flow
- Integration points
- Scalability considerations
"""
        architecture = self.execute(arch_prompt)
        print("  ✓ Architecture designed")
        
        # Step 3: Implementation
        impl_prompt = f"""
Based on this architecture:
{architecture}

Generate implementation with:
- Clean code structure
- Comprehensive error handling
- Performance optimization
- Full documentation
"""
        code = self.execute(impl_prompt)
        print("  ✓ Implementation completed")
        
        # Step 4: Code review
        review_prompt = f"""
Review this implementation:
{code}

Check for:
- Code quality issues
- Security vulnerabilities
- Performance problems
- Missing edge cases

Provide findings and suggested improvements.
"""
        review = self.execute(review_prompt)
        print("  ✓ Review completed")
        
        return f"{code}\n\n---\n\nCode Review:\n{review}"

def main():
    """Run conditional workflow."""
    
    print("Conditional Workflow: Complexity-Based Branching\n")
    
    engine = ConditionalWorkflowEngine()
    
    # Test with different complexity levels
    test_cases = [
        ("Create a function to check if a number is even", "SIMPLE"),
        ("Build a REST API for a todo list with user auth", "MODERATE"),
        ("Design a distributed task queue with retry logic, "
         "monitoring, and auto-scaling", "COMPLEX"),
    ]
    
    for requirements, expected_complexity in test_cases:
        print("\n" + "="*60)
        print(f"Requirements: {requirements[:50]}...")
        print("="*60)
        
        # Assess complexity
        complexity = engine.assess_complexity(requirements)
        print(f"\nAssessed as: {complexity.value.upper()}")
        
        # Branch based on complexity
        if complexity == AnalysisResult.SIMPLE:
            result = engine.execute_simple_path(requirements)
        elif complexity == AnalysisResult.MODERATE:
            result = engine.execute_moderate_path(requirements)
        else:  # COMPLEX
            result = engine.execute_complex_path(requirements)
        
        print(f"\n✓ Workflow completed")
        print(f"Output length: {len(result)} characters")

if __name__ == "__main__":
    main()
EOF

python workflow_tutorial_4_conditional.py
```

### 6.3 ✅ Checkpoint

You should now understand:
- [x] How to assess intermediate results
- [x] Implement conditional branching
- [x] Optimize workflow based on input characteristics

---

## 7. Tutorial 5: Error Handling & Recovery

### 7.1 Goal

Build robust workflows with comprehensive error handling and retry logic.

**Time**: 25 minutes

### 7.2 Error Taxonomy

```python
from enum import Enum

class ErrorType(Enum):
    """Types of errors in workflows."""
    
    TRANSIENT = "transient"
    # Temporary issues: rate limits, network timeouts
    # Recovery: Retry with exponential backoff
    
    RECOVERABLE = "recoverable"
    # Fixable issues: invalid format, context too long
    # Recovery: Adjust and retry
    
    PERMANENT = "permanent"
    # Cannot be fixed: invalid API key, unsupported operation
    # Recovery: Abort workflow
    
    USER_ERROR = "user_error"
    # User input issues: missing data, invalid request
    # Recovery: Request clarification
```

### 7.3 Robust Workflow Implementation

```python
cat > workflow_tutorial_5_error_handling.py << 'EOF'
#!/usr/bin/env python3
"""
Tutorial 5: Error Handling & Recovery
Robust workflows with retry logic and fallback strategies
"""

import os
import time
from dotenv import load_dotenv
from anthropic import Anthropic, APIError, RateLimitError
from typing import Optional, Callable
from dataclasses import dataclass

load_dotenv()

@dataclass
class RetryConfig:
    """Configuration for retry behavior."""
    max_attempts: int = 3
    base_delay: float = 1.0
    max_delay: float = 60.0
    exponential_base: float = 2.0

class RobustWorkflowEngine:
    """Workflow engine with comprehensive error handling."""
    
    def __init__(self, retry_config: RetryConfig = RetryConfig()):
        self.client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        self.retry_config = retry_config
    
    def execute_with_retry(
        self, 
        prompt: str,
        validator: Optional[Callable[[str], bool]] = None
    ) -> str:
        """Execute with retry logic and validation."""
        
        for attempt in range(1, self.retry_config.max_attempts + 1):
            try:
                print(f"  Attempt {attempt}/{self.retry_config.max_attempts}")
                
                # Execute
                response = self.client.messages.create(
                    model="claude-sonnet-4-20250514",
                    max_tokens=4096,
                    messages=[{"role": "user", "content": prompt}]
                )
                
                output = response.content[0].text
                
                # Validate if validator provided
                if validator and not validator(output):
                    print(f"  ✗ Validation failed")
                    if attempt < self.retry_config.max_attempts:
                        print(f"  ↻ Retrying with validation feedback")
                        prompt += "\n\nPrevious attempt failed validation. Please try again."
                        continue
                    else:
                        raise ValueError("Output failed validation after all retries")
                
                print(f"  ✓ Success")
                return output
            
            except RateLimitError as e:
                print(f"  ⚠ Rate limit hit")
                if attempt < self.retry_config.max_attempts:
                    delay = self._calculate_delay(attempt)
                    print(f"  ⏱ Waiting {delay:.1f}s before retry")
                    time.sleep(delay)
                else:
                    print(f"  ✗ Max retries exceeded")
                    raise
            
            except APIError as e:
                print(f"  ✗ API error: {e}")
                
                # Check if error is recoverable
                if "context_length" in str(e).lower():
                    print(f"  ↻ Context too long, compressing")
                    prompt = self._compress_prompt(prompt)
                    continue
                else:
                    # Permanent error, don't retry
                    raise
            
            except Exception as e:
                print(f"  ✗ Unexpected error: {e}")
                if attempt < self.retry_config.max_attempts:
                    delay = self._calculate_delay(attempt)
                    print(f"  ⏱ Waiting {delay:.1f}s before retry")
                    time.sleep(delay)
                else:
                    raise
        
        raise Exception("Max retries exceeded")
    
    def _calculate_delay(self, attempt: int) -> float:
        """Calculate exponential backoff delay."""
        delay = (
            self.retry_config.base_delay * 
            (self.retry_config.exponential_base ** (attempt - 1))
        )
        return min(delay, self.retry_config.max_delay)
    
    def _compress_prompt(self, prompt: str, target_length: int = None) -> str:
        """Compress prompt if too long."""
        if target_length is None:
            target_length = len(prompt) // 2
        
        # Simple compression: truncate middle
        if len(prompt) > target_length:
            keep = target_length // 2
            return (
                prompt[:keep] + 
                "\n\n[... content compressed ...]\n\n" + 
                prompt[-keep:]
            )
        return prompt

def validate_json_output(output: str) -> bool:
    """Validate that output is valid JSON."""
    import json
    try:
        json.loads(output)
        return True
    except:
        return False

def validate_contains_code(output: str) -> bool:
    """Validate that output contains code block."""
    return "```" in output

def main():
    """Demonstrate robust error handling."""
    
    print("Robust Workflow: Error Handling & Recovery\n")
    
    engine = RobustWorkflowEngine()
    
    # Test 1: Validation with retry
    print("="*60)
    print("Test 1: Output Validation")
    print("="*60)
    
    prompt1 = """
Generate a JSON object with user information:
- name
- email
- age

Respond with ONLY the JSON, no other text.
"""
    
    try:
        result1 = engine.execute_with_retry(
            prompt1,
            validator=validate_json_output
        )
        print(f"\n✓ Valid JSON received:\n{result1}\n")
    except Exception as e:
        print(f"\n✗ Failed: {e}\n")
    
    # Test 2: Code generation with validation
    print("="*60)
    print("Test 2: Code Generation with Validation")
    print("="*60)
    
    prompt2 = """
Create a Python function to reverse a string.
Include the code in a proper code block.
"""
    
    try:
        result2 = engine.execute_with_retry(
            prompt2,
            validator=validate_contains_code
        )
        print(f"\n✓ Code generated successfully\n")
    except Exception as e:
        print(f"\n✗ Failed: {e}\n")
    
    # Test 3: Handle very long context (will trigger compression)
    print("="*60)
    print("Test 3: Context Length Handling")
    print("="*60)
    
    # Create artificially long prompt
    long_context = "Background information: " + ("word " * 10000)
    prompt3 = f"{long_context}\n\nQuestion: What is 2+2?"
    
    try:
        result3 = engine.execute_with_retry(prompt3)
        print(f"\n✓ Handled long context successfully\n")
    except Exception as e:
        print(f"\n✗ Failed: {e}\n")

if __name__ == "__main__":
    main()
EOF

python workflow_tutorial_5_error_handling.py
```

### 7.4 ✅ Checkpoint

You should now be able to:
- [x] Classify error types
- [x] Implement retry logic with exponential backoff
- [x] Add output validation
- [x] Handle context length issues
- [x] Build production-ready error handling

---

## 8. Tutorial 6: Production Workflows

### 8.1 Goal

Build a complete production-ready workflow combining all techniques learned.

**Time**: 30 minutes

### 8.2 Complete Production Workflow

This workflow demonstrates:
- Multi-step orchestration
- Selective context handoff
- Multi-LLM integration
- Error handling & retry
- Validation at each step
- Comprehensive logging

```python
cat > workflow_tutorial_6_production.py << 'EOF'
#!/usr/bin/env python3
"""
Tutorial 6: Production-Ready Workflow
Complete example with all best practices
"""

import os
import json
import time
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
from anthropic import Anthropic, RateLimitError
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
from enum import Enum

load_dotenv()

class WorkflowStatus(Enum):
    """Workflow execution status."""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"

@dataclass
class StepResult:
    """Result from a workflow step."""
    step_id: str
    step_name: str
    status: str
    output: str
    error: Optional[str] = None
    duration_seconds: float = 0.0
    llm_provider: str = "claude"
    timestamp: str = ""

@dataclass
class WorkflowResult:
    """Complete workflow execution result."""
    workflow_id: str
    status: WorkflowStatus
    steps: List[StepResult]
    total_duration: float
    started_at: str
    completed_at: str

class ProductionWorkflowEngine:
    """Production-ready workflow execution engine."""
    
    def __init__(self, log_dir: Path = None):
        self.client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        self.log_dir = log_dir or Path("logs")
        self.log_dir.mkdir(exist_ok=True)
        
    def log(self, message: str, level: str = "INFO"):
        """Log message to file and console."""
        timestamp = datetime.now().isoformat()
        log_entry = f"[{timestamp}] [{level}] {message}"
        print(log_entry)
        
        # Write to log file
        log_file = self.log_dir / f"workflow_{datetime.now().date()}.log"
        with open(log_file, 'a') as f:
            f.write(log_entry + "\n")
    
    def execute_step(
        self,
        step_id: str,
        step_name: str,
        prompt: str,
        validator: Optional[callable] = None,
        max_retries: int = 3
    ) -> StepResult:
        """Execute a single step with retry and validation."""
        
        self.log(f"Starting step: {step_name}", "INFO")
        start_time = time.time()
        
        for attempt in range(1, max_retries + 1):
            try:
                self.log(f"Attempt {attempt}/{max_retries}", "DEBUG")
                
                # Execute LLM call
                response = self.client.messages.create(
                    model="claude-sonnet-4-20250514",
                    max_tokens=4096,
                    messages=[{"role": "user", "content": prompt}]
                )
                
                output = response.content[0].text
                
                # Validate if validator provided
                if validator and not validator(output):
                    self.log("Output validation failed", "WARNING")
                    if attempt < max_retries:
                        prompt += "\n\nPrevious output failed validation. Try again."
                        continue
                    else:
                        raise ValueError("Validation failed after max retries")
                
                duration = time.time() - start_time
                
                self.log(f"Step completed: {step_name} ({duration:.2f}s)", "INFO")
                
                return StepResult(
                    step_id=step_id,
                    step_name=step_name,
                    status="success",
                    output=output,
                    duration_seconds=duration,
                    timestamp=datetime.now().isoformat()
                )
            
            except RateLimitError as e:
                self.log(f"Rate limit hit, waiting...", "WARNING")
                if attempt < max_retries:
                    time.sleep(2 ** attempt)  # Exponential backoff
                else:
                    raise
            
            except Exception as e:
                self.log(f"Step failed: {e}", "ERROR")
                if attempt >= max_retries:
                    return StepResult(
                        step_id=step_id,
                        step_name=step_name,
                        status="failed",
                        output="",
                        error=str(e),
                        duration_seconds=time.time() - start_time,
                        timestamp=datetime.now().isoformat()
                    )
        
        raise Exception("Max retries exceeded")
    
    def execute_workflow(
        self,
        workflow_id: str,
        steps_config: List[Dict]
    ) -> WorkflowResult:
        """Execute complete workflow."""
        
        self.log(f"Starting workflow: {workflow_id}", "INFO")
        start_time = time.time()
        started_at = datetime.now().isoformat()
        
        results = []
        context_store = {}  # Store outputs for selective handoff
        
        try:
            for step_config in steps_config:
                step_id = step_config['id']
                step_name = step_config['name']
                prompt_template = step_config['prompt']
                required_context = step_config.get('required_context', [])
                validator = step_config.get('validator')
                
                # Build prompt with selective context
                context_parts = []
                for ctx_id in required_context:
                    if ctx_id in context_store:
                        context_parts.append(
                            f"Output from {ctx_id}:\n{context_store[ctx_id]}"
                        )
                
                # Combine context with prompt
                if context_parts:
                    full_prompt = "\n\n---\n\n".join(context_parts)
                    full_prompt += f"\n\n---\n\n{prompt_template}"
                else:
                    full_prompt = prompt_template
                
                # Execute step
                result = self.execute_step(
                    step_id=step_id,
                    step_name=step_name,
                    prompt=full_prompt,
                    validator=validator
                )
                
                results.append(result)
                
                # Check if step failed
                if result.status == "failed":
                    self.log(f"Workflow failed at step: {step_name}", "ERROR")
                    break
                
                # Store output for potential use by later steps
                context_store[step_id] = result.output
            
            # Determine overall status
            if all(r.status == "success" for r in results):
                status = WorkflowStatus.COMPLETED
            else:
                status = WorkflowStatus.FAILED
            
            total_duration = time.time() - start_time
            completed_at = datetime.now().isoformat()
            
            workflow_result = WorkflowResult(
                workflow_id=workflow_id,
                status=status,
                steps=results,
                total_duration=total_duration,
                started_at=started_at,
                completed_at=completed_at
            )
            
            # Save results to file
            self.save_results(workflow_result)
            
            self.log(
                f"Workflow {status.value}: {workflow_id} "
                f"({total_duration:.2f}s)",
                "INFO"
            )
            
            return workflow_result
        
        except Exception as e:
            self.log(f"Workflow failed with exception: {e}", "ERROR")
            raise
    
    def save_results(self, result: WorkflowResult):
        """Save workflow results to JSON file."""
        results_dir = Path("results")
        results_dir.mkdir(exist_ok=True)
        
        filename = f"{result.workflow_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        filepath = results_dir / filename
        
        # Convert to dict for JSON serialization
        result_dict = {
            'workflow_id': result.workflow_id,
            'status': result.status.value,
            'total_duration': result.total_duration,
            'started_at': result.started_at,
            'completed_at': result.completed_at,
            'steps': [asdict(step) for step in result.steps]
        }
        
        with open(filepath, 'w') as f:
            json.dump(result_dict, f, indent=2)
        
        self.log(f"Results saved to: {filepath}", "INFO")

def validate_contains_section(section_name: str):
    """Create validator that checks for specific section."""
    def validator(output: str) -> bool:
        return section_name.lower() in output.lower()
    return validator

def main():
    """Run production workflow."""
    
    print("Production Workflow: Complete Feature Development\n")
    
    engine = ProductionWorkflowEngine()
    
    # Define workflow steps
    steps = [
        {
            'id': 'requirements',
            'name': 'Analyze Requirements',
            'prompt': """
Analyze these requirements and create a structured specification:

"Build a URL shortener service with:
- Shorten long URLs to compact codes
- Track click analytics
- Support custom aliases
- Rate limiting per user"

Provide: Functional requirements, technical requirements, constraints.
            """,
            'required_context': [],
            'validator': validate_contains_section('requirements')
        },
        {
            'id': 'architecture',
            'name': 'Design Architecture',
            'prompt': """
Design system architecture with:
- Component breakdown
- Data models
- API endpoints
- Technology stack
            """,
            'required_context': ['requirements'],
            'validator': validate_contains_section('architecture')
        },
        {
            'id': 'implementation',
            'name': 'Generate Code',
            'prompt': """
Implement the core URL shortening service:
- Python FastAPI application
- SQLite database
- Complete with error handling
            """,
            'required_context': ['architecture'],
            'validator': lambda x: '```python' in x
        },
        {
            'id': 'tests',
            'name': 'Create Tests',
            'prompt': """
Create comprehensive pytest test suite for the implementation above.
Include unit tests and integration tests.
            """,
            'required_context': ['implementation'],
            'validator': lambda x: 'def test_' in x
        },
        {
            'id': 'documentation',
            'name': 'Generate Documentation',
            'prompt': """
Create README.md with:
- Project overview
- Installation instructions
- API documentation
- Usage examples
            """,
            'required_context': ['architecture', 'implementation'],
            'validator': validate_contains_section('installation')
        }
    ]
    
    # Execute workflow
    result = engine.execute_workflow(
        workflow_id="url_shortener_v1",
        steps_config=steps
    )
    
    # Display summary
    print("\n" + "="*60)
    print("WORKFLOW SUMMARY")
    print("="*60)
    print(f"Status: {result.status.value}")
    print(f"Total Duration: {result.total_duration:.2f}s")
    print(f"\nSteps:")
    for step in result.steps:
        status_symbol = "✓" if step.status == "success" else "✗"
        print(f"  {status_symbol} {step.step_name} ({step.duration_seconds:.2f}s)")
    
    if result.status == WorkflowStatus.COMPLETED:
        print("\n✓ All steps completed successfully!")
        print(f"\nFinal output saved to results/")
    else:
        print("\n✗ Workflow failed")

if __name__ == "__main__":
    main()
EOF

python workflow_tutorial_6_production.py
```

### 8.3 ✅ Checkpoint

You've now built a production-ready workflow with:
- [x] Multi-step orchestration
- [x] Selective context handoff
- [x] Validation at each step
- [x] Retry logic with exponential backoff
- [x] Comprehensive logging
- [x] Result persistence

---

## 9. Advanced Patterns

### 9.1 Parallel Execution

For independent steps that can run concurrently:

```python
import asyncio
from concurrent.futures import ThreadPoolExecutor

async def execute_parallel_steps(steps: list) -> dict:
    """Execute independent steps in parallel."""
    
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {
            executor.submit(execute_step, step): step 
            for step in steps
        }
        
        results = {}
        for future in futures:
            step = futures[future]
            results[step['id']] = future.result()
        
        return results
```

### 9.2 Dynamic Component Selection

Select components based on runtime conditions:

```python
def select_components(task_type: str, complexity: str) -> list:
    """Dynamically select optimal components."""
    
    components = []
    
    # Base instruction
    components.append(f"instruction-{task_type}-v1.0.0.md")
    
    # Add persona based on complexity
    if complexity == "complex":
        components.append("persona-senior-expert-v1.0.0.md")
    else:
        components.append("persona-general-expert-v1.0.0.md")
    
    # Add constraints based on context
    if task_type == "code":
        components.append("constraint-secure-code-v2.0.0.md")
    
    return components
```

### 9.3 Workflow Templates

Reusable workflow patterns:

```yaml
# workflow-templates/code-development.yml
workflow_template:
  name: "Code Development Pipeline"
  description: "Complete code development workflow"
  
  parameters:
    - language: string
    - complexity: simple|moderate|complex
    - include_tests: boolean
    
  steps:
    - id: analyze
      name: "Analyze Requirements"
      components: ["instruction-analyze-requirements"]
      
    - id: design
      name: "Design Solution"
      components: ["instruction-design-architecture"]
      condition: "{{complexity}} != 'simple'"
      
    - id: implement
      name: "Generate Code"
      components:
        - "persona-{{language}}-expert"
        - "instruction-code-generation"
      
    - id: test
      name: "Create Tests"
      components: ["instruction-create-tests"]
      condition: "{{include_tests}}"
```

---

## 10. Best Practices

### 10.1 Workflow Design Principles

✅ **DO**:
- Keep steps focused and atomic
- Use selective context handoff (not full accumulation)
- Add validation at each step
- Implement retry logic for transient errors
- Log comprehensively
- Test workflows with various inputs
- Version your workflows

❌ **DON'T**:
- Create monolithic mega-steps
- Pass unnecessary context
- Ignore error handling
- Skip validation
- Assume steps always succeed
- Hardcode values (use parameters)

### 10.2 Performance Optimization

**Token Usage**:
- Use selective handoff over full accumulation
- Summarize long context before passing
- Remove redundant information
- Compress when approaching limits

**Latency**:
- Use faster LLMs for non-critical steps
- Run independent steps in parallel
- Cache repeated components
- Stream for user feedback

**Cost**:
- Use Gemini for bulk processing
- Use local LLMs for simple tasks
- Avoid redundant LLM calls
- Batch similar operations

### 10.3 Testing Workflows

**Test Pyramid**:

```
        /\
       /  \     E2E Tests (few)
      /____\    Test complete workflows
     /      \   
    /  Inte  \  Integration Tests (some)
   /  gration \  Test step interactions
  /____________\ 
 /              \ Unit Tests (many)
/_  Components  _\ Test individual components
```

**Test Strategy**:
1. Unit test components individually
2. Integration test step pairs
3. E2E test complete workflows
4. Test error scenarios
5. Test with different LLMs

---

## Conclusion

**You've mastered SPES workflow execution!** 🎓

Throughout this tutorial, you've learned:

✅ **Fundamentals** - Workflow structure and context handoff  
✅ **Sequential Workflows** - Multi-step orchestration  
✅ **Context Strategies** - Four handoff patterns  
✅ **Multi-LLM Integration** - Optimal LLM selection  
✅ **Conditional Logic** - Branching workflows  
✅ **Error Handling** - Production-ready robustness  
✅ **Complete Production** - End-to-end implementation  

**Next Steps**:

1. **Practice**: Build 5-10 workflows for real tasks
2. **Experiment**: Try different context strategies
3. **Optimize**: Profile and improve performance
4. **Share**: Contribute workflows to community

**Related Documentation**:
- **Intelligence Layer Setup** - Configure all LLM providers
- **Component Creation Guide** - Build effective components
- **Advanced Workflow Patterns** - Expert techniques

---

**Time Invested**: ⏱️ ~120-180 minutes  
**Skills Gained**: Production workflow engineering  
**Ready For**: Building complex, reliable SPES workflows
