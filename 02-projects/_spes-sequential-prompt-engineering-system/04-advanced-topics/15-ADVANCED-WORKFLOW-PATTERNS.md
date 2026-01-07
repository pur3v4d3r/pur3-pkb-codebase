---
title: SPES Advanced Workflow Patterns
document_type: advanced_guide
tier: 3
priority: high
version: 1.0.0
status: published
prerequisites: ["Workflow Execution Tutorial", "Component Creation Guide", "Performance Optimization"]
estimated_time: 210-240 minutes
last_updated: 2025-12-25
---

# SPES Advanced Workflow Patterns

**Version**: 1.0.0  
**Document Type**: Advanced Patterns Guide  
**Audience**: Workflow architects, advanced developers  
**Time Required**: 210-240 minutes  
**Goal**: Master complex workflow patterns for production systems

---

## Table of Contents

1. [Workflow Architecture Patterns](#1-workflow-architecture-patterns)
2. [Multi-Agent Workflows](#2-multi-agent-workflows)
3. [Conditional Branching](#3-conditional-branching)
4. [Iterative Refinement](#4-iterative-refinement)
5. [Human-in-the-Loop](#5-human-in-the-loop)
6. [Error Recovery Strategies](#6-error-recovery-strategies)
7. [Workflow Composition](#7-workflow-composition)
8. [State Management](#8-state-management)
9. [Orchestration Patterns](#9-orchestration-patterns)
10. [Production Examples](#10-production-examples)

---

## 1. Workflow Architecture Patterns

### 1.1 Pattern Taxonomy

**Sequential Patterns**:
- Simple Chain: A → B → C
- Pipeline: A → B → C (with data transformation)

**Parallel Patterns**:
- Fan-Out/Fan-In: Split → [A, B, C] → Merge
- Map-Reduce: Map → [A₁, A₂, A₃] → Reduce

**Conditional Patterns**:
- Branch: If condition → A, Else → B
- Switch: Route based on multiple conditions

**Iterative Patterns**:
- Retry: Repeat until success
- Refinement: Iterate until quality threshold met
- Feedback Loop: Output → Evaluation → Refinement

**Hybrid Patterns**:
- Multi-Agent: Specialist agents collaborate
- Hierarchical: Coordinator delegates to sub-workflows

### 1.2 Pattern Selection Framework

```python
from enum import Enum
from typing import Dict, Any

class WorkflowPattern(Enum):
    """Workflow pattern types."""
    SEQUENTIAL = "sequential"
    PARALLEL = "parallel"
    CONDITIONAL = "conditional"
    ITERATIVE = "iterative"
    MULTI_AGENT = "multi_agent"
    HIERARCHICAL = "hierarchical"

class PatternSelector:
    """Select appropriate workflow pattern."""
    
    @staticmethod
    def select_pattern(requirements: Dict[str, Any]) -> WorkflowPattern:
        """
        Select pattern based on requirements.
        
        Args:
            requirements: Dict with:
                - independent_tasks: bool
                - need_decision: bool
                - quality_critical: bool
                - specialized_roles: bool
                - complex_coordination: bool
        
        Returns:
            Recommended pattern
        """
        
        # Parallel: Independent tasks that can run concurrently
        if requirements.get('independent_tasks'):
            return WorkflowPattern.PARALLEL
        
        # Multi-Agent: Specialized roles needed
        if requirements.get('specialized_roles'):
            return WorkflowPattern.MULTI_AGENT
        
        # Iterative: Quality critical, needs refinement
        if requirements.get('quality_critical'):
            return WorkflowPattern.ITERATIVE
        
        # Conditional: Decision points in workflow
        if requirements.get('need_decision'):
            return WorkflowPattern.CONDITIONAL
        
        # Hierarchical: Complex coordination
        if requirements.get('complex_coordination'):
            return WorkflowPattern.HIERARCHICAL
        
        # Default: Sequential
        return WorkflowPattern.SEQUENTIAL
```

---

## 2. Multi-Agent Workflows

### 2.1 Agent Architecture

```python
cat > workflows/multi_agent.py << 'EOF'
#!/usr/bin/env python3
"""
Multi-Agent Workflow System
Coordinate multiple specialized agents
"""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from pathlib import Path
import json

@dataclass
class Agent:
    """Specialized agent with role and components."""
    name: str
    role: str
    persona_component: Path
    instruction_component: Path
    output_format: Optional[Path] = None
    
    def get_prompt(self, task: str) -> str:
        """Build prompt for this agent."""
        
        parts = []
        
        # Load persona
        persona = self._load_component(self.persona_component)
        parts.append(persona)
        
        # Load instruction
        instruction = self._load_component(self.instruction_component)
        parts.append(instruction)
        
        # Load output format if specified
        if self.output_format:
            output_format = self._load_component(self.output_format)
            parts.append(output_format)
        
        # Add task
        parts.append(f"Task: {task}")
        
        return "\n\n".join(parts)
    
    def _load_component(self, path: Path) -> str:
        """Load component content."""
        content = path.read_text()
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                return parts[2].strip()
        return content

class MultiAgentWorkflow:
    """
    Coordinate multiple agents for complex tasks.
    
    Architecture:
        Coordinator Agent
            ↓
        [Agent 1, Agent 2, Agent 3]
            ↓
        Synthesis Agent
    """
    
    def __init__(self, adapter):
        self.adapter = adapter
        self.agents: Dict[str, Agent] = {}
    
    def register_agent(self, agent: Agent):
        """Register a specialized agent."""
        self.agents[agent.name] = agent
    
    def execute_parallel(
        self,
        task: str,
        agent_names: List[str]
    ) -> Dict[str, str]:
        """
        Execute task with multiple agents in parallel.
        
        Each agent works independently on the same task.
        """
        
        results = {}
        
        for agent_name in agent_names:
            if agent_name not in self.agents:
                raise ValueError(f"Unknown agent: {agent_name}")
            
            agent = self.agents[agent_name]
            
            print(f"🤖 {agent.name} ({agent.role}) working...")
            
            prompt = agent.get_prompt(task)
            response = self.adapter.generate(prompt, max_tokens=4096)
            
            results[agent_name] = response
            
            print(f"   ✓ Complete")
        
        return results
    
    def execute_sequential(
        self,
        task: str,
        agent_names: List[str]
    ) -> Dict[str, str]:
        """
        Execute task with agents in sequence.
        
        Each agent builds on previous agent's output.
        """
        
        results = {}
        current_input = task
        
        for agent_name in agent_names:
            if agent_name not in self.agents:
                raise ValueError(f"Unknown agent: {agent_name}")
            
            agent = self.agents[agent_name]
            
            print(f"🤖 {agent.name} ({agent.role}) working...")
            
            prompt = agent.get_prompt(current_input)
            response = self.adapter.generate(prompt, max_tokens=4096)
            
            results[agent_name] = response
            current_input = response  # Next agent gets previous output
            
            print(f"   ✓ Complete")
        
        return results
    
    def execute_with_synthesis(
        self,
        task: str,
        worker_agents: List[str],
        synthesizer_agent: str
    ) -> Dict[str, Any]:
        """
        Execute with multiple workers + synthesis.
        
        Pattern:
            1. Worker agents produce independent outputs
            2. Synthesizer combines them into final result
        """
        
        # Step 1: Workers produce outputs
        print("\n📋 Phase 1: Worker Agents")
        worker_results = self.execute_parallel(task, worker_agents)
        
        # Step 2: Synthesizer combines
        print("\n🔀 Phase 2: Synthesis")
        
        synthesizer = self.agents[synthesizer_agent]
        
        # Build synthesis prompt
        synthesis_parts = [f"## {name} Output\n\n{output}" 
                          for name, output in worker_results.items()]
        synthesis_input = (
            f"Original Task: {task}\n\n"
            f"Agent Outputs:\n\n" +
            "\n\n".join(synthesis_parts) +
            f"\n\nSynthesize these outputs into a comprehensive final result."
        )
        
        synthesis_prompt = synthesizer.get_prompt(synthesis_input)
        final_output = self.adapter.generate(synthesis_prompt, max_tokens=8192)
        
        return {
            'worker_outputs': worker_results,
            'final_output': final_output,
            'synthesis_agent': synthesizer_agent
        }
    
    def execute_debate(
        self,
        task: str,
        debater_agents: List[str],
        judge_agent: str,
        rounds: int = 2
    ) -> Dict[str, Any]:
        """
        Execute debate pattern.
        
        Pattern:
            1. Each debater presents their perspective
            2. Debaters respond to each other
            3. Judge evaluates and decides
        """
        
        debate_history = []
        
        # Round 1: Initial positions
        print(f"\n🗣️ Round 1: Initial Positions")
        positions = self.execute_parallel(task, debater_agents)
        debate_history.append({
            'round': 1,
            'type': 'positions',
            'outputs': positions
        })
        
        # Rounds 2+: Rebuttals
        for round_num in range(2, rounds + 1):
            print(f"\n🗣️ Round {round_num}: Rebuttals")
            
            rebuttals = {}
            
            for agent_name in debater_agents:
                agent = self.agents[agent_name]
                
                # Build context with other agents' positions
                other_positions = [
                    f"**{name}**: {positions[name]}"
                    for name in debater_agents
                    if name != agent_name
                ]
                
                rebuttal_task = (
                    f"Original task: {task}\n\n"
                    f"Your position: {positions[agent_name]}\n\n"
                    f"Other positions:\n" +
                    "\n\n".join(other_positions) +
                    f"\n\nProvide a rebuttal defending your position "
                    f"and addressing counterarguments."
                )
                
                prompt = agent.get_prompt(rebuttal_task)
                response = self.adapter.generate(prompt, max_tokens=4096)
                
                rebuttals[agent_name] = response
            
            debate_history.append({
                'round': round_num,
                'type': 'rebuttals',
                'outputs': rebuttals
            })
        
        # Judge evaluates
        print(f"\n⚖️ Judge Evaluation")
        
        judge = self.agents[judge_agent]
        
        # Build debate summary
        debate_summary = []
        for entry in debate_history:
            debate_summary.append(f"\n### Round {entry['round']} ({entry['type'].title()})\n")
            for agent_name, output in entry['outputs'].items():
                debate_summary.append(f"**{agent_name}**: {output[:200]}...\n")
        
        judgment_task = (
            f"Original task: {task}\n\n"
            f"Debate history:\n" +
            "".join(debate_summary) +
            f"\n\nEvaluate the arguments and provide a final decision "
            f"with reasoning."
        )
        
        judgment_prompt = judge.get_prompt(judgment_task)
        judgment = self.adapter.generate(judgment_prompt, max_tokens=8192)
        
        return {
            'debate_history': debate_history,
            'judgment': judgment,
            'judge_agent': judge_agent
        }

# Example usage
if __name__ == "__main__":
    from adapters import AdapterManager, LLMProvider
    
    manager = AdapterManager()
    adapter = manager.get_adapter(LLMProvider.CLAUDE)
    
    # Create multi-agent workflow
    workflow = MultiAgentWorkflow(adapter)
    
    # Register agents
    workflow.register_agent(Agent(
        name="code_architect",
        role="Software Architecture",
        persona_component=Path("components/core/personas/persona-software-architect-v1.0.0.md"),
        instruction_component=Path("components/core/instructions/instruction-design-architecture-v1.0.0.md")
    ))
    
    workflow.register_agent(Agent(
        name="security_expert",
        role="Security Analysis",
        persona_component=Path("components/core/personas/persona-security-expert-v1.0.0.md"),
        instruction_component=Path("components/core/instructions/instruction-security-review-v1.0.0.md")
    ))
    
    workflow.register_agent(Agent(
        name="performance_engineer",
        role="Performance Optimization",
        persona_component=Path("components/core/personas/persona-performance-engineer-v1.0.0.md"),
        instruction_component=Path("components/core/instructions/instruction-optimize-performance-v1.0.0.md")
    ))
    
    workflow.register_agent(Agent(
        name="tech_lead",
        role="Technical Leadership",
        persona_component=Path("components/core/personas/persona-tech-lead-v1.0.0.md"),
        instruction_component=Path("components/core/instructions/instruction-synthesize-v1.0.0.md")
    ))
    
    # Execute with synthesis
    task = "Design a microservices architecture for a high-traffic e-commerce platform"
    
    result = workflow.execute_with_synthesis(
        task=task,
        worker_agents=["code_architect", "security_expert", "performance_engineer"],
        synthesizer_agent="tech_lead"
    )
    
    print("\n" + "="*60)
    print("FINAL OUTPUT")
    print("="*60)
    print(result['final_output'])
EOF
```

**Save as**: `workflows/multi_agent.py`

---

## 3. Conditional Branching

### 3.1 Decision-Based Routing

```python
cat > workflows/conditional_workflow.py << 'EOF'
#!/usr/bin/env python3
"""
Conditional Workflow
Route based on conditions and LLM decisions
"""

from typing import Dict, Any, Callable, List
from enum import Enum
import json
import re

class ConditionType(Enum):
    """Types of conditions."""
    KEYWORD = "keyword"          # Check for keywords
    LENGTH = "length"            # Check content length
    FORMAT = "format"            # Check format/structure
    LLM_DECISION = "llm_decision"  # Use LLM to decide
    QUALITY = "quality"          # Quality score threshold

class ConditionalWorkflow:
    """Workflow with conditional branching."""
    
    def __init__(self, adapter):
        self.adapter = adapter
        self.branches = {}
    
    def register_branch(
        self,
        name: str,
        condition: Callable[[str], bool],
        workflow: Callable[[str], str]
    ):
        """Register a conditional branch."""
        self.branches[name] = {
            'condition': condition,
            'workflow': workflow
        }
    
    def execute(self, input_text: str) -> Dict[str, Any]:
        """Execute workflow with conditional routing."""
        
        # Evaluate conditions
        for branch_name, branch in self.branches.items():
            print(f"Checking condition: {branch_name}...")
            
            if branch['condition'](input_text):
                print(f"✓ Condition met: {branch_name}")
                
                result = branch['workflow'](input_text)
                
                return {
                    'branch_taken': branch_name,
                    'result': result
                }
        
        return {
            'branch_taken': 'none',
            'result': 'No conditions met',
            'error': 'No matching branch found'
        }
    
    def execute_switch(
        self,
        input_text: str,
        classifier_prompt: str,
        routes: Dict[str, Callable[[str], str]]
    ) -> Dict[str, Any]:
        """
        Execute switch/case pattern using LLM classification.
        
        Args:
            input_text: Input to classify
            classifier_prompt: Prompt for classification
            routes: Map of class -> workflow function
        """
        
        # Step 1: Classify input
        classification_full_prompt = f"""{classifier_prompt}

Input: {input_text}

Classify this input as one of: {', '.join(routes.keys())}

Respond with ONLY the classification label, nothing else."""
        
        classification = self.adapter.generate(
            classification_full_prompt,
            max_tokens=50
        ).strip().lower()
        
        print(f"Classification: {classification}")
        
        # Step 2: Route to appropriate workflow
        for route_name, workflow_fn in routes.items():
            if route_name.lower() in classification:
                print(f"Routing to: {route_name}")
                
                result = workflow_fn(input_text)
                
                return {
                    'classification': route_name,
                    'result': result
                }
        
        return {
            'classification': 'unknown',
            'result': None,
            'error': f'No route for classification: {classification}'
        }
    
    def execute_quality_gate(
        self,
        input_text: str,
        workflow: Callable[[str], str],
        quality_check: Callable[[str], float],
        threshold: float = 0.8,
        max_attempts: int = 3
    ) -> Dict[str, Any]:
        """
        Execute with quality gate.
        
        Pattern:
            1. Execute workflow
            2. Check quality
            3. If below threshold, retry with feedback
            4. Max attempts limit
        """
        
        attempts = []
        
        for attempt in range(1, max_attempts + 1):
            print(f"\nAttempt {attempt}/{max_attempts}...")
            
            # Execute workflow
            if attempt == 1:
                current_input = input_text
            else:
                # Add feedback from previous attempt
                previous = attempts[-1]
                current_input = (
                    f"{input_text}\n\n"
                    f"Previous attempt (quality: {previous['quality']:.2f}):\n"
                    f"{previous['output']}\n\n"
                    f"Improve the output to meet quality threshold of {threshold}."
                )
            
            output = workflow(current_input)
            
            # Check quality
            quality = quality_check(output)
            
            attempts.append({
                'attempt': attempt,
                'output': output,
                'quality': quality
            })
            
            print(f"Quality: {quality:.2f} (threshold: {threshold})")
            
            if quality >= threshold:
                print("✓ Quality gate passed!")
                
                return {
                    'success': True,
                    'attempts': attempt,
                    'output': output,
                    'quality': quality,
                    'history': attempts
                }
        
        # Failed to meet quality
        print("✗ Quality gate failed after max attempts")
        
        # Return best attempt
        best = max(attempts, key=lambda x: x['quality'])
        
        return {
            'success': False,
            'attempts': max_attempts,
            'output': best['output'],
            'quality': best['quality'],
            'history': attempts
        }

# Helper: Build condition functions
class ConditionBuilder:
    """Build common condition functions."""
    
    @staticmethod
    def keyword_condition(keywords: List[str]) -> Callable[[str], bool]:
        """Check if text contains keywords."""
        def condition(text: str) -> bool:
            text_lower = text.lower()
            return any(kw.lower() in text_lower for kw in keywords)
        return condition
    
    @staticmethod
    def length_condition(min_len: int = None, max_len: int = None) -> Callable[[str], bool]:
        """Check text length."""
        def condition(text: str) -> bool:
            length = len(text)
            if min_len and length < min_len:
                return False
            if max_len and length > max_len:
                return False
            return True
        return condition
    
    @staticmethod
    def format_condition(pattern: str) -> Callable[[str], bool]:
        """Check if text matches regex pattern."""
        def condition(text: str) -> bool:
            return bool(re.search(pattern, text))
        return condition
    
    @staticmethod
    def llm_decision_condition(
        adapter,
        decision_prompt: str
    ) -> Callable[[str], bool]:
        """Use LLM to make decision."""
        def condition(text: str) -> bool:
            full_prompt = f"""{decision_prompt}

Text: {text}

Answer with ONLY 'yes' or 'no'."""
            
            response = adapter.generate(full_prompt, max_tokens=10).strip().lower()
            return 'yes' in response
        return condition

# Example usage
if __name__ == "__main__":
    from adapters import AdapterManager, LLMProvider
    
    manager = AdapterManager()
    adapter = manager.get_adapter(LLMProvider.CLAUDE)
    
    workflow = ConditionalWorkflow(adapter)
    
    # Example 1: Simple keyword branching
    def code_workflow(text: str) -> str:
        return "Generating code..."
    
    def docs_workflow(text: str) -> str:
        return "Generating documentation..."
    
    workflow.register_branch(
        name="code_generation",
        condition=ConditionBuilder.keyword_condition(['code', 'function', 'class']),
        workflow=code_workflow
    )
    
    workflow.register_branch(
        name="documentation",
        condition=ConditionBuilder.keyword_condition(['document', 'explain', 'describe']),
        workflow=docs_workflow
    )
    
    # Example 2: Switch/case pattern
    routes = {
        'bug_fix': lambda t: "Analyzing bug and creating fix...",
        'feature': lambda t: "Designing and implementing feature...",
        'refactor': lambda t: "Refactoring code for better structure..."
    }
    
    result = workflow.execute_switch(
        input_text="The login function is throwing a null pointer exception",
        classifier_prompt="Classify this development task as: bug_fix, feature, or refactor",
        routes=routes
    )
    
    print(f"\nResult: {result}")
EOF
```

**Save as**: `workflows/conditional_workflow.py`

---

## 4. Iterative Refinement

### 4.1 Refinement Loop

```python
cat > workflows/iterative_refinement.py << 'EOF'
#!/usr/bin/env python3
"""
Iterative Refinement Workflow
Progressively improve output through feedback loops
"""

from typing import Dict, Any, Callable, List
from dataclasses import dataclass

@dataclass
class RefinementResult:
    """Result of refinement iteration."""
    iteration: int
    output: str
    score: float
    feedback: str
    improved: bool

class IterativeRefinement:
    """Iteratively refine output until quality threshold met."""
    
    def __init__(self, adapter):
        self.adapter = adapter
    
    def refine(
        self,
        initial_prompt: str,
        evaluator: Callable[[str], Dict[str, Any]],
        threshold: float = 0.8,
        max_iterations: int = 5
    ) -> Dict[str, Any]:
        """
        Refine output iteratively.
        
        Args:
            initial_prompt: Starting prompt
            evaluator: Function that scores output and gives feedback
            threshold: Quality threshold to meet
            max_iterations: Max refinement iterations
            
        Returns:
            Final result with history
        """
        
        history: List[RefinementResult] = []
        current_prompt = initial_prompt
        
        for iteration in range(1, max_iterations + 1):
            print(f"\n{'='*60}")
            print(f"Iteration {iteration}/{max_iterations}")
            print('='*60)
            
            # Generate output
            print("Generating...")
            output = self.adapter.generate(current_prompt, max_tokens=4096)
            
            # Evaluate
            print("Evaluating...")
            evaluation = evaluator(output)
            score = evaluation['score']
            feedback = evaluation['feedback']
            
            print(f"Score: {score:.2f} (threshold: {threshold})")
            
            # Record iteration
            improved = iteration == 1 or score > history[-1].score
            
            history.append(RefinementResult(
                iteration=iteration,
                output=output,
                score=score,
                feedback=feedback,
                improved=improved
            ))
            
            # Check if threshold met
            if score >= threshold:
                print(f"✓ Threshold met!")
                
                return {
                    'success': True,
                    'iterations': iteration,
                    'final_output': output,
                    'final_score': score,
                    'history': history
                }
            
            # Build refinement prompt
            print("Preparing refinement...")
            current_prompt = self._build_refinement_prompt(
                initial_prompt,
                output,
                feedback,
                iteration
            )
        
        # Max iterations reached
        print(f"\n✗ Max iterations reached without meeting threshold")
        
        # Return best attempt
        best = max(history, key=lambda x: x.score)
        
        return {
            'success': False,
            'iterations': max_iterations,
            'final_output': best.output,
            'final_score': best.score,
            'history': history
        }
    
    def _build_refinement_prompt(
        self,
        original_prompt: str,
        previous_output: str,
        feedback: str,
        iteration: int
    ) -> str:
        """Build prompt for refinement iteration."""
        
        return f"""{original_prompt}

Previous Attempt (Iteration {iteration}):
{previous_output}

Feedback:
{feedback}

Please revise the output to address the feedback and improve quality."""
    
    def refine_with_criteria(
        self,
        initial_prompt: str,
        criteria: List[Dict[str, Any]],
        max_iterations: int = 5
    ) -> Dict[str, Any]:
        """
        Refine using specific criteria.
        
        Args:
            initial_prompt: Starting prompt
            criteria: List of {name, check_fn, weight, threshold}
            max_iterations: Max iterations
        """
        
        def multi_criteria_evaluator(output: str) -> Dict[str, Any]:
            """Evaluate against all criteria."""
            
            criterion_scores = []
            feedback_parts = []
            
            for criterion in criteria:
                score = criterion['check_fn'](output)
                criterion_scores.append({
                    'name': criterion['name'],
                    'score': score,
                    'weight': criterion['weight'],
                    'threshold': criterion.get('threshold', 0.7)
                })
                
                if score < criterion.get('threshold', 0.7):
                    feedback_parts.append(
                        f"- {criterion['name']}: {score:.2f} "
                        f"(needs >= {criterion.get('threshold', 0.7)})"
                    )
            
            # Weighted average
            total_weight = sum(c['weight'] for c in criterion_scores)
            weighted_score = sum(
                c['score'] * c['weight'] for c in criterion_scores
            ) / total_weight
            
            feedback = "Areas needing improvement:\n" + "\n".join(feedback_parts) if feedback_parts else "All criteria met"
            
            return {
                'score': weighted_score,
                'feedback': feedback,
                'criterion_scores': criterion_scores
            }
        
        # Calculate overall threshold (weighted average of individual thresholds)
        total_weight = sum(c['weight'] for c in criteria)
        overall_threshold = sum(
            c.get('threshold', 0.7) * c['weight'] for c in criteria
        ) / total_weight
        
        return self.refine(
            initial_prompt,
            multi_criteria_evaluator,
            threshold=overall_threshold,
            max_iterations=max_iterations
        )
    
    def refine_with_examples(
        self,
        task: str,
        good_examples: List[str],
        bad_examples: List[str],
        evaluator: Callable[[str], Dict[str, Any]],
        max_iterations: int = 3
    ) -> Dict[str, Any]:
        """
        Refine using positive and negative examples.
        
        Pattern:
            1. Show good and bad examples
            2. Generate attempt
            3. Compare to examples
            4. Refine based on comparison
        """
        
        # Build initial prompt with examples
        initial_prompt = f"""Task: {task}

Good Examples (follow these patterns):
"""
        for i, example in enumerate(good_examples, 1):
            initial_prompt += f"\n{i}. {example}\n"
        
        initial_prompt += f"""
Bad Examples (avoid these patterns):
"""
        for i, example in enumerate(bad_examples, 1):
            initial_prompt += f"\n{i}. {example}\n"
        
        initial_prompt += f"""
Now complete the task, following the good examples and avoiding the bad examples."""
        
        return self.refine(
            initial_prompt,
            evaluator,
            max_iterations=max_iterations
        )

# Example usage
if __name__ == "__main__":
    from adapters import AdapterManager, LLMProvider
    
    manager = AdapterManager()
    adapter = manager.get_adapter(LLMProvider.CLAUDE)
    
    refinement = IterativeRefinement(adapter)
    
    # Example: Refine code with multiple criteria
    def check_has_docstring(code: str) -> float:
        return 1.0 if '"""' in code or "'''" in code else 0.0
    
    def check_has_type_hints(code: str) -> float:
        return 1.0 if '->' in code and ': ' in code else 0.5 if ': ' in code else 0.0
    
    def check_has_error_handling(code: str) -> float:
        return 1.0 if 'try:' in code or 'except' in code else 0.0
    
    def check_length(code: str) -> float:
        lines = len(code.split('\n'))
        if 10 <= lines <= 50:
            return 1.0
        elif 5 <= lines < 10 or 50 < lines <= 100:
            return 0.7
        else:
            return 0.3
    
    criteria = [
        {
            'name': 'Has Docstring',
            'check_fn': check_has_docstring,
            'weight': 2.0,
            'threshold': 1.0
        },
        {
            'name': 'Has Type Hints',
            'check_fn': check_has_type_hints,
            'weight': 1.5,
            'threshold': 1.0
        },
        {
            'name': 'Has Error Handling',
            'check_fn': check_has_error_handling,
            'weight': 1.0,
            'threshold': 1.0
        },
        {
            'name': 'Appropriate Length',
            'check_fn': check_length,
            'weight': 0.5,
            'threshold': 0.7
        }
    ]
    
    result = refinement.refine_with_criteria(
        initial_prompt="Create a Python function to parse JSON configuration files.",
        criteria=criteria,
        max_iterations=5
    )
    
    print("\n" + "="*60)
    print("FINAL RESULT")
    print("="*60)
    print(f"Success: {result['success']}")
    print(f"Iterations: {result['iterations']}")
    print(f"Final Score: {result['final_score']:.2f}")
    print(f"\nOutput:\n{result['final_output']}")
EOF
```

**Save as**: `workflows/iterative_refinement.py`

---

## 5. Human-in-the-Loop

### 5.1 Interactive Workflow

```python
cat > workflows/human_in_loop.py << 'EOF'
#!/usr/bin/env python3
"""
Human-in-the-Loop Workflow
Interactive workflows requiring human feedback
"""

from typing import Dict, Any, List, Optional, Callable
from dataclasses import dataclass
from enum import Enum

class ApprovalStatus(Enum):
    """Approval status."""
    APPROVED = "approved"
    REJECTED = "rejected"
    NEEDS_REVISION = "needs_revision"

@dataclass
class HumanFeedback:
    """Human feedback on output."""
    status: ApprovalStatus
    comments: str
    suggested_changes: Optional[str] = None

class HumanInLoopWorkflow:
    """Workflow with human approval gates."""
    
    def __init__(self, adapter):
        self.adapter = adapter
    
    def execute_with_approval(
        self,
        prompt: str,
        approval_fn: Callable[[str], HumanFeedback],
        max_revisions: int = 3
    ) -> Dict[str, Any]:
        """
        Execute with human approval gate.
        
        Pattern:
            1. Generate output
            2. Present to human for approval
            3. If approved → done
            4. If needs revision → incorporate feedback and retry
        """
        
        current_prompt = prompt
        revision_history = []
        
        for revision in range(max_revisions + 1):
            print(f"\n{'='*60}")
            if revision == 0:
                print("Initial Generation")
            else:
                print(f"Revision {revision}/{max_revisions}")
            print('='*60)
            
            # Generate
            print("Generating...")
            output = self.adapter.generate(current_prompt, max_tokens=4096)
            
            # Present for approval
            print("\n📋 Output ready for review")
            print("-" * 60)
            print(output[:500] + "..." if len(output) > 500 else output)
            print("-" * 60)
            
            feedback = approval_fn(output)
            
            # Record in history
            revision_history.append({
                'revision': revision,
                'output': output,
                'status': feedback.status.value,
                'comments': feedback.comments
            })
            
            # Check status
            if feedback.status == ApprovalStatus.APPROVED:
                print("✓ Approved!")
                
                return {
                    'success': True,
                    'approved': True,
                    'revisions': revision,
                    'final_output': output,
                    'history': revision_history
                }
            
            elif feedback.status == ApprovalStatus.REJECTED:
                print("✗ Rejected")
                
                return {
                    'success': False,
                    'approved': False,
                    'revisions': revision,
                    'final_output': output,
                    'rejection_reason': feedback.comments,
                    'history': revision_history
                }
            
            else:  # NEEDS_REVISION
                if revision >= max_revisions:
                    print("✗ Max revisions reached")
                    
                    return {
                        'success': False,
                        'approved': False,
                        'revisions': revision,
                        'final_output': output,
                        'reason': 'max_revisions_reached',
                        'history': revision_history
                    }
                
                print("🔄 Needs revision, incorporating feedback...")
                
                # Build revision prompt
                current_prompt = f"""{prompt}

Previous Attempt:
{output}

Feedback:
{feedback.comments}

{f'Suggested Changes: {feedback.suggested_changes}' if feedback.suggested_changes else ''}

Please revise the output to address the feedback."""
    
    def execute_with_choices(
        self,
        prompt: str,
        num_variations: int,
        selection_fn: Callable[[List[str]], int]
    ) -> Dict[str, Any]:
        """
        Generate multiple variations, let human choose.
        
        Pattern:
            1. Generate N variations
            2. Present to human
            3. Human selects best
            4. Optionally refine selected
        """
        
        print(f"Generating {num_variations} variations...\n")
        
        variations = []
        
        for i in range(num_variations):
            print(f"Variation {i+1}/{num_variations}...")
            
            # Add variation instruction
            varied_prompt = f"""{prompt}

(Generate variation {i+1} of {num_variations}, making it unique)"""
            
            output = self.adapter.generate(varied_prompt, max_tokens=4096)
            variations.append(output)
        
        # Present for selection
        print("\n📋 Variations ready for review")
        
        for i, var in enumerate(variations, 1):
            print(f"\n--- Variation {i} ---")
            print(var[:300] + "..." if len(var) > 300 else var)
        
        selected_idx = selection_fn(variations)
        
        print(f"\n✓ Selected variation {selected_idx + 1}")
        
        return {
            'success': True,
            'selected_index': selected_idx,
            'selected_output': variations[selected_idx],
            'all_variations': variations
        }
    
    def execute_progressive_disclosure(
        self,
        sections: List[Dict[str, str]],
        approval_fn: Callable[[str, str], HumanFeedback]
    ) -> Dict[str, Any]:
        """
        Progressive disclosure pattern.
        
        Pattern:
            1. Generate section by section
            2. Get approval for each section
            3. Build up complete document
        """
        
        approved_sections = []
        full_output = []
        
        for i, section in enumerate(sections, 1):
            print(f"\n{'='*60}")
            print(f"Section {i}/{len(sections)}: {section['name']}")
            print('='*60)
            
            # Build context with previously approved sections
            context = "\n\n".join(full_output) if full_output else ""
            
            section_prompt = f"""{context}

{section['prompt']}"""
            
            # Generate section
            print("Generating...")
            section_output = self.adapter.generate(section_prompt, max_tokens=2048)
            
            # Get approval
            feedback = approval_fn(section['name'], section_output)
            
            if feedback.status == ApprovalStatus.APPROVED:
                print(f"✓ Section approved")
                approved_sections.append(section['name'])
                full_output.append(section_output)
            
            elif feedback.status == ApprovalStatus.NEEDS_REVISION:
                print(f"🔄 Section needs revision")
                
                # Retry with feedback
                revised_prompt = f"""{section_prompt}

Previous attempt:
{section_output}

Feedback: {feedback.comments}

Please revise."""
                
                section_output = self.adapter.generate(revised_prompt, max_tokens=2048)
                
                # Ask again
                feedback_2 = approval_fn(section['name'], section_output)
                
                if feedback_2.status == ApprovalStatus.APPROVED:
                    print(f"✓ Revised section approved")
                    approved_sections.append(section['name'])
                    full_output.append(section_output)
                else:
                    print(f"✗ Section rejected after revision")
                    return {
                        'success': False,
                        'completed_sections': approved_sections,
                        'failed_at': section['name'],
                        'partial_output': "\n\n".join(full_output)
                    }
            
            else:  # REJECTED
                print(f"✗ Section rejected")
                return {
                    'success': False,
                    'completed_sections': approved_sections,
                    'failed_at': section['name'],
                    'partial_output': "\n\n".join(full_output)
                }
        
        # All sections approved
        print("\n✓ All sections approved!")
        
        return {
            'success': True,
            'completed_sections': approved_sections,
            'final_output': "\n\n".join(full_output)
        }

# Interactive helpers
class InteractiveFeedback:
    """Helper for interactive terminal feedback."""
    
    @staticmethod
    def get_approval(output: str) -> HumanFeedback:
        """Get approval from terminal user."""
        
        print("\nReview the output above.")
        print("\nOptions:")
        print("  1. Approve")
        print("  2. Reject")
        print("  3. Needs Revision")
        
        choice = input("\nYour choice (1-3): ").strip()
        
        if choice == '1':
            return HumanFeedback(
                status=ApprovalStatus.APPROVED,
                comments="Approved"
            )
        elif choice == '2':
            comments = input("Rejection reason: ")
            return HumanFeedback(
                status=ApprovalStatus.REJECTED,
                comments=comments
            )
        else:
            comments = input("What needs to change? ")
            suggested = input("Suggested changes (optional): ")
            return HumanFeedback(
                status=ApprovalStatus.NEEDS_REVISION,
                comments=comments,
                suggested_changes=suggested if suggested else None
            )
    
    @staticmethod
    def select_variation(variations: List[str]) -> int:
        """Select from variations."""
        
        print("\nWhich variation do you prefer?")
        choice = input(f"Enter number (1-{len(variations)}): ").strip()
        
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(variations):
                return idx
        except ValueError:
            pass
        
        print("Invalid choice, selecting first variation")
        return 0

# Example usage
if __name__ == "__main__":
    from adapters import AdapterManager, LLMProvider
    
    manager = AdapterManager()
    adapter = manager.get_adapter(LLMProvider.CLAUDE)
    
    workflow = HumanInLoopWorkflow(adapter)
    
    # Example: Generate with approval
    result = workflow.execute_with_approval(
        prompt="Write a function to validate email addresses",
        approval_fn=InteractiveFeedback.get_approval,
        max_revisions=3
    )
    
    print("\n" + "="*60)
    print("FINAL RESULT")
    print("="*60)
    print(f"Success: {result['success']}")
    print(f"Approved: {result['approved']}")
    print(f"Revisions: {result['revisions']}")
EOF
```

**Save as**: `workflows/human_in_loop.py`

---

## 6. Error Recovery Strategies

### 6.1 Resilient Workflow Execution

```python
cat > workflows/error_recovery.py << 'EOF'
#!/usr/bin/env python3
"""
Error Recovery Workflows
Robust execution with retry and fallback strategies
"""

import time
from typing import Dict, Any, Callable, Optional
from dataclasses import dataclass
from enum import Enum

class ErrorType(Enum):
    """Types of errors."""
    RATE_LIMIT = "rate_limit"
    TIMEOUT = "timeout"
    INVALID_OUTPUT = "invalid_output"
    API_ERROR = "api_error"
    VALIDATION_FAILED = "validation_failed"

@dataclass
class RetryConfig:
    """Retry configuration."""
    max_attempts: int = 3
    base_delay: float = 1.0  # seconds
    exponential_backoff: bool = True
    max_delay: float = 60.0

class ErrorRecoveryWorkflow:
    """Workflow with error recovery."""
    
    def __init__(self, adapter):
        self.adapter = adapter
    
    def execute_with_retry(
        self,
        prompt: str,
        validator: Optional[Callable[[str], bool]] = None,
        config: RetryConfig = None
    ) -> Dict[str, Any]:
        """
        Execute with automatic retry on failure.
        
        Args:
            prompt: Prompt to execute
            validator: Optional validation function
            config: Retry configuration
        """
        
        if config is None:
            config = RetryConfig()
        
        attempts = []
        
        for attempt in range(1, config.max_attempts + 1):
            print(f"\nAttempt {attempt}/{config.max_attempts}...")
            
            try:
                # Execute
                output = self.adapter.generate(prompt, max_tokens=4096)
                
                # Validate if validator provided
                if validator:
                    if not validator(output):
                        raise ValueError("Output failed validation")
                
                # Success!
                print("✓ Success")
                
                attempts.append({
                    'attempt': attempt,
                    'success': True,
                    'output': output,
                    'error': None
                })
                
                return {
                    'success': True,
                    'attempts': attempt,
                    'output': output,
                    'history': attempts
                }
            
            except Exception as e:
                error_msg = str(e)
                print(f"✗ Error: {error_msg}")
                
                attempts.append({
                    'attempt': attempt,
                    'success': False,
                    'output': None,
                    'error': error_msg
                })
                
                # If not last attempt, wait before retry
                if attempt < config.max_attempts:
                    delay = self._calculate_delay(attempt, config)
                    print(f"Retrying in {delay:.1f}s...")
                    time.sleep(delay)
        
        # All attempts failed
        print("✗ All attempts failed")
        
        return {
            'success': False,
            'attempts': config.max_attempts,
            'output': None,
            'error': 'Max retry attempts exceeded',
            'history': attempts
        }
    
    def execute_with_fallback(
        self,
        primary_fn: Callable[[], str],
        fallback_fns: list[Callable[[], str]]
    ) -> Dict[str, Any]:
        """
        Execute with fallback strategies.
        
        Pattern:
            1. Try primary approach
            2. If fails, try fallback 1
            3. If fails, try fallback 2
            4. etc.
        """
        
        attempts = []
        
        # Try primary
        print("Trying primary approach...")
        try:
            output = primary_fn()
            print("✓ Primary succeeded")
            
            return {
                'success': True,
                'approach': 'primary',
                'output': output,
                'attempts': 1
            }
        except Exception as e:
            print(f"✗ Primary failed: {e}")
            attempts.append({
                'approach': 'primary',
                'error': str(e)
            })
        
        # Try fallbacks
        for i, fallback_fn in enumerate(fallback_fns, 1):
            print(f"\nTrying fallback {i}...")
            try:
                output = fallback_fn()
                print(f"✓ Fallback {i} succeeded")
                
                return {
                    'success': True,
                    'approach': f'fallback_{i}',
                    'output': output,
                    'attempts': i + 1,
                    'failed_attempts': attempts
                }
            except Exception as e:
                print(f"✗ Fallback {i} failed: {e}")
                attempts.append({
                    'approach': f'fallback_{i}',
                    'error': str(e)
                })
        
        # All failed
        print("\n✗ All approaches failed")
        
        return {
            'success': False,
            'output': None,
            'failed_attempts': attempts
        }
    
    def execute_with_circuit_breaker(
        self,
        prompt: str,
        failure_threshold: int = 3,
        timeout_seconds: float = 60.0
    ) -> Dict[str, Any]:
        """
        Execute with circuit breaker pattern.
        
        Pattern:
            - Track consecutive failures
            - If failures exceed threshold, "open circuit" (stop trying)
            - After timeout, allow one test request ("half-open")
            - If test succeeds, "close circuit" (resume normal)
        """
        
        # Check circuit state
        state = getattr(self, '_circuit_state', 'closed')
        failures = getattr(self, '_circuit_failures', 0)
        last_failure = getattr(self, '_circuit_last_failure', 0)
        
        # Circuit open?
        if state == 'open':
            time_since_failure = time.time() - last_failure
            
            if time_since_failure < timeout_seconds:
                print(f"⚡ Circuit OPEN - blocking request")
                print(f"   Time until retry: {timeout_seconds - time_since_failure:.1f}s")
                
                return {
                    'success': False,
                    'circuit_state': 'open',
                    'error': 'Circuit breaker open'
                }
            else:
                # Try half-open
                print("⚡ Circuit HALF-OPEN - testing...")
                state = 'half-open'
        
        # Execute request
        try:
            output = self.adapter.generate(prompt, max_tokens=4096)
            
            # Success - close/keep circuit closed
            print("✓ Success - circuit CLOSED")
            self._circuit_state = 'closed'
            self._circuit_failures = 0
            
            return {
                'success': True,
                'circuit_state': 'closed',
                'output': output
            }
        
        except Exception as e:
            # Failure
            failures += 1
            self._circuit_failures = failures
            self._circuit_last_failure = time.time()
            
            print(f"✗ Failure {failures}/{failure_threshold}")
            
            if failures >= failure_threshold:
                print("⚡ Circuit OPENED")
                self._circuit_state = 'open'
                
                return {
                    'success': False,
                    'circuit_state': 'open',
                    'error': str(e),
                    'failures': failures
                }
            else:
                return {
                    'success': False,
                    'circuit_state': 'closed',
                    'error': str(e),
                    'failures': failures
                }
    
    def execute_with_graceful_degradation(
        self,
        prompt: str,
        quality_levels: list[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Execute with graceful degradation.
        
        Pattern:
            1. Try highest quality/most expensive approach
            2. If fails/timeout, degrade to simpler approach
            3. Continue degrading until something works
        """
        
        attempts = []
        
        for level in quality_levels:
            print(f"\nTrying: {level['name']} (quality: {level['quality']})")
            
            try:
                # Execute with level's configuration
                output = level['execute_fn'](prompt)
                
                print(f"✓ Success with {level['name']}")
                
                return {
                    'success': True,
                    'quality_level': level['name'],
                    'quality_score': level['quality'],
                    'output': output,
                    'degraded': len(attempts) > 0,
                    'attempts': attempts + [level['name']]
                }
            
            except Exception as e:
                print(f"✗ Failed: {e}")
                attempts.append(level['name'])
        
        # All levels failed
        return {
            'success': False,
            'output': None,
            'attempts': attempts
        }
    
    def _calculate_delay(self, attempt: int, config: RetryConfig) -> float:
        """Calculate retry delay."""
        
        if config.exponential_backoff:
            delay = config.base_delay * (2 ** (attempt - 1))
        else:
            delay = config.base_delay
        
        return min(delay, config.max_delay)

# Example usage
if __name__ == "__main__":
    from adapters import AdapterManager, LLMProvider
    
    manager = AdapterManager()
    adapter = manager.get_adapter(LLMProvider.CLAUDE)
    
    workflow = ErrorRecoveryWorkflow(adapter)
    
    # Example: Retry with validation
    def validate_code(output: str) -> bool:
        """Validate code output."""
        return 'def ' in output and '```python' in output
    
    result = workflow.execute_with_retry(
        prompt="Create a Python function to validate emails",
        validator=validate_code,
        config=RetryConfig(max_attempts=3, base_delay=2.0)
    )
    
    print(f"\n{'='*60}")
    print("RESULT")
    print('='*60)
    print(f"Success: {result['success']}")
    print(f"Attempts: {result['attempts']}")
    if result['success']:
        print(f"\nOutput:\n{result['output']}")
EOF
```

**Save as**: `workflows/error_recovery.py`

---

## 7. Workflow Composition

### 7.1 Composable Workflows

```python
cat > workflows/composition.py << 'EOF'
#!/usr/bin/env python3
"""
Workflow Composition
Build complex workflows from simple components
"""

from typing import Dict, Any, List, Callable
from dataclasses import dataclass
from abc import ABC, abstractmethod

class WorkflowStep(ABC):
    """Base class for workflow steps."""
    
    @abstractmethod
    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute step with context."""
        pass
    
    @abstractmethod
    def get_name(self) -> str:
        """Get step name."""
        pass

@dataclass
class LLMStep(WorkflowStep):
    """LLM execution step."""
    name: str
    prompt_template: str
    adapter: Any
    output_key: str = "output"
    
    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute LLM generation."""
        
        # Format prompt with context
        prompt = self.prompt_template.format(**context)
        
        # Generate
        output = self.adapter.generate(prompt, max_tokens=4096)
        
        # Update context
        context[self.output_key] = output
        
        return context
    
    def get_name(self) -> str:
        return self.name

@dataclass
class TransformStep(WorkflowStep):
    """Data transformation step."""
    name: str
    transform_fn: Callable[[Dict[str, Any]], Dict[str, Any]]
    
    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Apply transformation."""
        return self.transform_fn(context)
    
    def get_name(self) -> str:
        return self.name

@dataclass
class ConditionalStep(WorkflowStep):
    """Conditional execution step."""
    name: str
    condition: Callable[[Dict[str, Any]], bool]
    true_step: WorkflowStep
    false_step: Optional[WorkflowStep] = None
    
    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute conditionally."""
        
        if self.condition(context):
            return self.true_step.execute(context)
        elif self.false_step:
            return self.false_step.execute(context)
        else:
            return context
    
    def get_name(self) -> str:
        return self.name

class ComposableWorkflow:
    """Workflow built from composable steps."""
    
    def __init__(self, name: str):
        self.name = name
        self.steps: List[WorkflowStep] = []
    
    def add_step(self, step: WorkflowStep):
        """Add a step to workflow."""
        self.steps.append(step)
        return self  # For chaining
    
    def execute(self, initial_context: Dict[str, Any] = None) -> Dict[str, Any]:
        """Execute complete workflow."""
        
        context = initial_context or {}
        
        print(f"\n{'='*60}")
        print(f"Executing Workflow: {self.name}")
        print('='*60)
        
        for i, step in enumerate(self.steps, 1):
            print(f"\nStep {i}/{len(self.steps)}: {step.get_name()}")
            
            context = step.execute(context)
            
            print("✓ Complete")
        
        print(f"\n{'='*60}")
        print("Workflow Complete")
        print('='*60)
        
        return context
    
    def to_diagram(self) -> str:
        """Generate workflow diagram."""
        
        lines = [f"# Workflow: {self.name}\n"]
        lines.append("```")
        
        for i, step in enumerate(self.steps, 1):
            if i > 1:
                lines.append("    ↓")
            lines.append(f"[{step.get_name()}]")
        
        lines.append("```")
        
        return "\n".join(lines)

# Example: Build complex workflow
if __name__ == "__main__":
    from adapters import AdapterManager, LLMProvider
    
    manager = AdapterManager()
    adapter = manager.get_adapter(LLMProvider.CLAUDE)
    
    # Create workflow
    workflow = ComposableWorkflow("Code Review & Documentation")
    
    # Step 1: Analyze code
    workflow.add_step(LLMStep(
        name="Code Analysis",
        prompt_template="""Analyze this code:

{code}

Identify:
1. Potential bugs
2. Performance issues
3. Security concerns
4. Code quality issues

Output as JSON list.""",
        adapter=adapter,
        output_key="analysis"
    ))
    
    # Step 2: Extract issues
    workflow.add_step(TransformStep(
        name="Extract Issues",
        transform_fn=lambda ctx: {
            **ctx,
            'issue_count': ctx['analysis'].count('"severity"')
        }
    ))
    
    # Step 3: Conditional - if issues found, create fixes
    def has_issues(ctx):
        return ctx.get('issue_count', 0) > 0
    
    workflow.add_step(ConditionalStep(
        name="Fix Issues (if needed)",
        condition=has_issues,
        true_step=LLMStep(
            name="Generate Fixes",
            prompt_template="""Code:
{code}

Issues found:
{analysis}

Generate fixed code addressing all issues.""",
            adapter=adapter,
            output_key="fixed_code"
        )
    ))
    
    # Step 4: Generate documentation
    workflow.add_step(LLMStep(
        name="Generate Documentation",
        prompt_template="""Code:
{fixed_code}

Generate comprehensive documentation including:
- Function descriptions
- Parameters
- Return values
- Usage examples""",
        adapter=adapter,
        output_key="documentation"
    ))
    
    # Execute
    result = workflow.execute({
        'code': """
def process(data):
    result = []
    for i in range(len(data)):
        result.append(data[i] * 2)
    return result
"""
    })
    
    print("\nFinal Result:")
    print(f"Issues Found: {result.get('issue_count', 0)}")
    if 'fixed_code' in result:
        print(f"\nFixed Code:\n{result['fixed_code']}")
    print(f"\nDocumentation:\n{result['documentation']}")
    
    # Show diagram
    print("\n" + workflow.to_diagram())
EOF
```

**Save as**: `workflows/composition.py`

---

## 8. State Management

### 8.1 Stateful Workflows

```python
cat > workflows/stateful_workflow.py << 'EOF'
#!/usr/bin/env python3
"""
Stateful Workflows
Manage workflow state across executions
"""

import json
from pathlib import Path
from typing import Dict, Any, Optional
from datetime import datetime
from dataclasses import dataclass, asdict
from enum import Enum

class WorkflowStatus(Enum):
    """Workflow execution status."""
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    PAUSED = "paused"
    COMPLETED = "completed"
    FAILED = "failed"

@dataclass
class WorkflowState:
    """Workflow execution state."""
    workflow_id: str
    status: WorkflowStatus
    current_step: int
    total_steps: int
    context: Dict[str, Any]
    created_at: str
    updated_at: str
    completed_at: Optional[str] = None
    error: Optional[str] = None
    
    def to_dict(self) -> Dict:
        """Convert to dictionary."""
        d = asdict(self)
        d['status'] = self.status.value
        return d
    
    @classmethod
    def from_dict(cls, d: Dict) -> 'WorkflowState':
        """Create from dictionary."""
        d = d.copy()
        d['status'] = WorkflowStatus(d['status'])
        return cls(**d)

class StatefulWorkflowManager:
    """Manage stateful workflow execution."""
    
    def __init__(self, state_dir: Path = None):
        self.state_dir = state_dir or Path.home() / ".spes/workflow_state"
        self.state_dir.mkdir(parents=True, exist_ok=True)
    
    def create_workflow(
        self,
        workflow_id: str,
        total_steps: int,
        initial_context: Dict[str, Any] = None
    ) -> WorkflowState:
        """Create new workflow state."""
        
        now = datetime.now().isoformat()
        
        state = WorkflowState(
            workflow_id=workflow_id,
            status=WorkflowStatus.NOT_STARTED,
            current_step=0,
            total_steps=total_steps,
            context=initial_context or {},
            created_at=now,
            updated_at=now
        )
        
        self._save_state(state)
        
        return state
    
    def load_workflow(self, workflow_id: str) -> Optional[WorkflowState]:
        """Load workflow state."""
        
        state_file = self.state_dir / f"{workflow_id}.json"
        
        if not state_file.exists():
            return None
        
        with open(state_file, 'r') as f:
            data = json.load(f)
        
        return WorkflowState.from_dict(data)
    
    def update_workflow(
        self,
        workflow_id: str,
        status: WorkflowStatus = None,
        current_step: int = None,
        context: Dict[str, Any] = None,
        error: str = None
    ) -> WorkflowState:
        """Update workflow state."""
        
        state = self.load_workflow(workflow_id)
        
        if state is None:
            raise ValueError(f"Workflow not found: {workflow_id}")
        
        # Update fields
        if status is not None:
            state.status = status
        
        if current_step is not None:
            state.current_step = current_step
        
        if context is not None:
            state.context.update(context)
        
        if error is not None:
            state.error = error
        
        state.updated_at = datetime.now().isoformat()
        
        # Set completed_at if completed
        if status == WorkflowStatus.COMPLETED:
            state.completed_at = state.updated_at
        
        self._save_state(state)
        
        return state
    
    def execute_step(
        self,
        workflow_id: str,
        step_fn: Callable[[Dict[str, Any]], Dict[str, Any]]
    ) -> WorkflowState:
        """Execute next workflow step."""
        
        state = self.load_workflow(workflow_id)
        
        if state is None:
            raise ValueError(f"Workflow not found: {workflow_id}")
        
        if state.status == WorkflowStatus.COMPLETED:
            print("Workflow already completed")
            return state
        
        if state.status == WorkflowStatus.FAILED:
            print("Workflow has failed, cannot continue")
            return state
        
        # Update status to in_progress
        if state.status == WorkflowStatus.NOT_STARTED:
            state = self.update_workflow(
                workflow_id,
                status=WorkflowStatus.IN_PROGRESS
            )
        
        # Execute step
        next_step = state.current_step + 1
        
        print(f"Executing step {next_step}/{state.total_steps}...")
        
        try:
            # Execute
            updated_context = step_fn(state.context)
            
            # Update state
            state = self.update_workflow(
                workflow_id,
                current_step=next_step,
                context=updated_context,
                status=WorkflowStatus.COMPLETED if next_step >= state.total_steps else WorkflowStatus.IN_PROGRESS
            )
            
            print("✓ Step complete")
            
            return state
        
        except Exception as e:
            print(f"✗ Step failed: {e}")
            
            # Mark as failed
            state = self.update_workflow(
                workflow_id,
                status=WorkflowStatus.FAILED,
                error=str(e)
            )
            
            return state
    
    def pause_workflow(self, workflow_id: str) -> WorkflowState:
        """Pause workflow execution."""
        return self.update_workflow(workflow_id, status=WorkflowStatus.PAUSED)
    
    def resume_workflow(self, workflow_id: str) -> WorkflowState:
        """Resume paused workflow."""
        state = self.load_workflow(workflow_id)
        
        if state and state.status == WorkflowStatus.PAUSED:
            return self.update_workflow(workflow_id, status=WorkflowStatus.IN_PROGRESS)
        
        return state
    
    def list_workflows(self, status: WorkflowStatus = None) -> list[WorkflowState]:
        """List all workflows."""
        
        workflows = []
        
        for state_file in self.state_dir.glob("*.json"):
            with open(state_file, 'r') as f:
                data = json.load(f)
            
            state = WorkflowState.from_dict(data)
            
            if status is None or state.status == status:
                workflows.append(state)
        
        return workflows
    
    def _save_state(self, state: WorkflowState):
        """Save state to disk."""
        
        state_file = self.state_dir / f"{state.workflow_id}.json"
        
        with open(state_file, 'w') as f:
            json.dump(state.to_dict(), f, indent=2)

# Example usage
if __name__ == "__main__":
    manager = StatefulWorkflowManager()
    
    # Create workflow
    state = manager.create_workflow(
        workflow_id="data_pipeline_001",
        total_steps=4,
        initial_context={'dataset': 'customers.csv'}
    )
    
    print(f"Created workflow: {state.workflow_id}")
    
    # Execute steps
    def step1(ctx):
        print("  Loading data...")
        ctx['data_loaded'] = True
        return ctx
    
    def step2(ctx):
        print("  Cleaning data...")
        ctx['data_cleaned'] = True
        return ctx
    
    def step3(ctx):
        print("  Analyzing data...")
        ctx['analysis_complete'] = True
        return ctx
    
    def step4(ctx):
        print("  Generating report...")
        ctx['report_generated'] = True
        return ctx
    
    # Execute
    for step_fn in [step1, step2, step3, step4]:
        state = manager.execute_step(state.workflow_id, step_fn)
        print(f"Status: {state.status.value}, Step: {state.current_step}/{state.total_steps}\n")
    
    # List all workflows
    print("\nAll workflows:")
    for wf in manager.list_workflows():
        print(f"  {wf.workflow_id}: {wf.status.value}")
EOF
```

**Save as**: `workflows/stateful_workflow.py`

---

## 9. Orchestration Patterns

### 9.1 Advanced Orchestration

```python
cat > workflows/orchestration.py << 'EOF'
#!/usr/bin/env python3
"""
Advanced Orchestration Patterns
Map-Reduce, Fan-Out/Fan-In, Saga, etc.
"""

from typing import List, Dict, Any, Callable
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

class WorkflowOrchestrator:
    """Advanced workflow orchestration patterns."""
    
    def __init__(self, adapter, max_workers: int = 5):
        self.adapter = adapter
        self.max_workers = max_workers
    
    def map_reduce(
        self,
        items: List[Any],
        map_fn: Callable[[Any], Any],
        reduce_fn: Callable[[List[Any]], Any]
    ) -> Any:
        """
        Map-Reduce pattern.
        
        Pattern:
            items → [map(item1), map(item2), ...] → reduce(results) → final
        """
        
        print(f"\n{'='*60}")
        print(f"Map-Reduce: {len(items)} items")
        print('='*60)
        
        # Map phase (parallel)
        print("\n📊 Map Phase...")
        
        mapped_results = []
        
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {executor.submit(map_fn, item): item for item in items}
            
            for future in as_completed(futures):
                item = futures[future]
                try:
                    result = future.result()
                    mapped_results.append(result)
                    print(f"  ✓ Mapped: {str(item)[:50]}...")
                except Exception as e:
                    print(f"  ✗ Failed: {str(item)[:50]}... ({e})")
        
        # Reduce phase
        print("\n🔀 Reduce Phase...")
        final_result = reduce_fn(mapped_results)
        print("  ✓ Complete")
        
        return final_result
    
    def fan_out_fan_in(
        self,
        input_data: Any,
        worker_fns: List[Callable[[Any], Any]],
        aggregator_fn: Callable[[List[Any]], Any]
    ) -> Any:
        """
        Fan-Out/Fan-In pattern.
        
        Pattern:
                    → worker1(input) →
            input → worker2(input) → aggregator → result
                    → worker3(input) →
        """
        
        print(f"\n{'='*60}")
        print(f"Fan-Out/Fan-In: {len(worker_fns)} workers")
        print('='*60)
        
        # Fan-Out (parallel execution)
        print("\n📤 Fan-Out Phase...")
        
        results = []
        
        with ThreadPoolExecutor(max_workers=len(worker_fns)) as executor:
            futures = {
                executor.submit(fn, input_data): f"Worker {i+1}"
                for i, fn in enumerate(worker_fns)
            }
            
            for future in as_completed(futures):
                worker_name = futures[future]
                try:
                    result = future.result()
                    results.append(result)
                    print(f"  ✓ {worker_name} complete")
                except Exception as e:
                    print(f"  ✗ {worker_name} failed: {e}")
        
        # Fan-In (aggregate results)
        print("\n📥 Fan-In Phase...")
        final_result = aggregator_fn(results)
        print("  ✓ Aggregation complete")
        
        return final_result
    
    def saga(
        self,
        steps: List[Dict[str, Callable]],
        context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Saga pattern (with compensation).
        
        Pattern:
            Try each step, if any fails, compensate all completed steps
        """
        
        print(f"\n{'='*60}")
        print(f"Saga: {len(steps)} steps")
        print('='*60)
        
        completed_steps = []
        
        try:
            # Execute steps
            for i, step in enumerate(steps, 1):
                print(f"\nStep {i}/{len(steps)}: {step.get('name', f'Step {i}')}")
                
                # Execute
                context = step['execute'](context)
                completed_steps.append(step)
                
                print("  ✓ Complete")
            
            print("\n✓ Saga completed successfully")
            
            return {
                'success': True,
                'context': context,
                'completed_steps': len(completed_steps)
            }
        
        except Exception as e:
            print(f"\n✗ Saga failed: {e}")
            print("🔄 Compensating...")
            
            # Compensate in reverse order
            for step in reversed(completed_steps):
                if 'compensate' in step:
                    try:
                        print(f"  Compensating: {step.get('name', 'Unknown')}")
                        step['compensate'](context)
                        print("    ✓ Compensated")
                    except Exception as comp_error:
                        print(f"    ✗ Compensation failed: {comp_error}")
            
            return {
                'success': False,
                'error': str(e),
                'completed_steps': len(completed_steps),
                'compensated': True
            }
    
    def pipeline(
        self,
        data: Any,
        stages: List[Callable[[Any], Any]]
    ) -> Any:
        """
        Pipeline pattern.
        
        Pattern:
            data → stage1 → stage2 → stage3 → result
        """
        
        print(f"\n{'='*60}")
        print(f"Pipeline: {len(stages)} stages")
        print('='*60)
        
        current_data = data
        
        for i, stage in enumerate(stages, 1):
            stage_name = getattr(stage, '__name__', f'Stage {i}')
            print(f"\n Stage {i}/{len(stages)}: {stage_name}")
            
            start_time = time.time()
            current_data = stage(current_data)
            duration = time.time() - start_time
            
            print(f"  ✓ Complete ({duration:.2f}s)")
        
        return current_data
    
    def scatter_gather(
        self,
        query: Any,
        sources: List[Callable[[Any], Any]],
        timeout: float = 30.0
    ) -> List[Any]:
        """
        Scatter-Gather pattern.
        
        Pattern:
            Query multiple sources in parallel, gather results
        """
        
        print(f"\n{'='*60}")
        print(f"Scatter-Gather: {len(sources)} sources")
        print('='*60)
        
        results = []
        
        with ThreadPoolExecutor(max_workers=len(sources)) as executor:
            futures = {
                executor.submit(source, query): f"Source {i+1}"
                for i, source in enumerate(sources)
            }
            
            for future in as_completed(futures, timeout=timeout):
                source_name = futures[future]
                try:
                    result = future.result()
                    results.append(result)
                    print(f"  ✓ {source_name} responded")
                except Exception as e:
                    print(f"  ✗ {source_name} failed: {e}")
        
        print(f"\n✓ Gathered {len(results)}/{len(sources)} results")
        
        return results

# Example usage
if __name__ == "__main__":
    from adapters import AdapterManager, LLMProvider
    
    manager = AdapterManager()
    adapter = manager.get_adapter(LLMProvider.CLAUDE)
    
    orchestrator = WorkflowOrchestrator(adapter)
    
    # Example: Map-Reduce for batch summarization
    documents = [
        "Long document 1...",
        "Long document 2...",
        "Long document 3..."
    ]
    
    def map_summarize(doc):
        # Summarize individual document
        prompt = f"Summarize this document in 2 sentences:\n\n{doc}"
        return adapter.generate(prompt, max_tokens=200)
    
    def reduce_combine(summaries):
        # Combine all summaries
        combined = "\n\n".join(f"Document {i+1}: {s}" for i, s in enumerate(summaries))
        prompt = f"Synthesize these summaries into a cohesive overview:\n\n{combined}"
        return adapter.generate(prompt, max_tokens=500)
    
    result = orchestrator.map_reduce(
        items=documents,
        map_fn=map_summarize,
        reduce_fn=reduce_combine
    )
    
    print(f"\nFinal Result:\n{result}")
EOF
```

**Save as**: `workflows/orchestration.py`

---

## 10. Production Examples

### 10.1 Real-World Pattern: Research & Analysis

```python
cat > workflows/examples/research_analysis.py << 'EOF'
#!/usr/bin/env python3
"""
Production Example: Research & Analysis Workflow
Complete multi-agent research workflow
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from adapters import AdapterManager, LLMProvider
from workflows.multi_agent import MultiAgentWorkflow, Agent
from workflows.iterative_refinement import IterativeRefinement
from workflows.composition import ComposableWorkflow, LLMStep, TransformStep

def run_research_workflow(topic: str):
    """
    Execute comprehensive research workflow.
    
    Phases:
        1. Research Planning (multi-agent)
        2. Information Gathering (parallel)
        3. Analysis (iterative refinement)
        4. Synthesis (composition)
    """
    
    manager = AdapterManager()
    adapter = manager.get_adapter(LLMProvider.CLAUDE)
    
    print(f"\n{'='*60}")
    print(f"RESEARCH WORKFLOW: {topic}")
    print('='*60)
    
    # Phase 1: Planning
    print("\n📋 Phase 1: Research Planning")
    print("-" * 60)
    
    planner_prompt = f"""Create a comprehensive research plan for: {topic}

Output a JSON structure with:
{{
  "research_questions": [list of 3-5 key questions],
  "information_sources": [types of sources to consult],
  "analysis_framework": "framework to use",
  "expected_deliverables": [list of outputs]
}}"""
    
    plan = adapter.generate(planner_prompt, max_tokens=2048)
    print(f"Research Plan Generated:\n{plan[:300]}...")
    
    # Phase 2: Multi-Agent Information Gathering
    print("\n🔍 Phase 2: Information Gathering (Multi-Agent)")
    print("-" * 60)
    
    multi_agent = MultiAgentWorkflow(adapter)
    
    # Register research agents
    multi_agent.register_agent(Agent(
        name="literature_reviewer",
        role="Academic Literature Review",
        persona_component=Path("components/core/personas/persona-researcher-v1.0.0.md"),
        instruction_component=Path("components/core/instructions/instruction-literature-review-v1.0.0.md")
    ))
    
    multi_agent.register_agent(Agent(
        name="data_analyst",
        role="Data Analysis",
        persona_component=Path("components/core/personas/persona-data-scientist-v1.0.0.md"),
        instruction_component=Path("components/core/instructions/instruction-analyze-data-v1.0.0.md")
    ))
    
    multi_agent.register_agent(Agent(
        name="synthesizer",
        role="Research Synthesis",
        persona_component=Path("components/core/personas/persona-research-lead-v1.0.0.md"),
        instruction_component=Path("components/core/instructions/instruction-synthesize-v1.0.0.md")
    ))
    
    # Gather information
    research_results = multi_agent.execute_with_synthesis(
        task=f"Research: {topic}\n\nPlan:{plan}",
        worker_agents=["literature_reviewer", "data_analyst"],
        synthesizer_agent="synthesizer"
    )
    
    # Phase 3: Iterative Analysis Refinement
    print("\n🔬 Phase 3: Analysis Refinement")
    print("-" * 60)
    
    refinement = IterativeRefinement(adapter)
    
    def evaluate_analysis(output: str) -> Dict[str, Any]:
        """Evaluate analysis quality."""
        
        # Simple heuristic evaluation
        score = 0.0
        feedback_parts = []
        
        # Check for key elements
        if len(output) >= 1000:
            score += 0.3
        else:
            feedback_parts.append("Analysis too brief, needs more depth")
        
        if "conclusion" in output.lower():
            score += 0.2
        else:
            feedback_parts.append("Missing explicit conclusion")
        
        if output.count("evidence") >= 2:
            score += 0.2
        else:
            feedback_parts.append("Needs more evidence citations")
        
        if any(word in output.lower() for word in ["however", "although", "while"]):
            score += 0.15
        else:
            feedback_parts.append("Lacks nuanced argumentation")
        
        if output.count('\n\n') >= 5:
            score += 0.15
        else:
            feedback_parts.append("Needs better organization/structure")
        
        feedback = "Areas for improvement:\n- " + "\n- ".join(feedback_parts) if feedback_parts else "Analysis meets quality standards"
        
        return {
            'score': score,
            'feedback': feedback
        }
    
    analysis_result = refinement.refine(
        initial_prompt=f"""Based on this research:

{research_results['final_output']}

Provide a comprehensive analysis of: {topic}

Include:
1. Key findings
2. Supporting evidence
3. Contradictions or limitations
4. Implications
5. Conclusion""",
        evaluator=evaluate_analysis,
        threshold=0.8,
        max_iterations=3
    )
    
    # Phase 4: Final Synthesis
    print("\n📝 Phase 4: Final Synthesis")
    print("-" * 60)
    
    synthesis_workflow = ComposableWorkflow("Final Report Generation")
    
    # Add steps
    synthesis_workflow.add_step(LLMStep(
        name="Executive Summary",
        prompt_template="""Create an executive summary (200 words) for:

Topic: {topic}

Research: {research}

Analysis: {analysis}""",
        adapter=adapter,
        output_key="executive_summary"
    ))
    
    synthesis_workflow.add_step(LLMStep(
        name="Detailed Report",
        prompt_template="""Create a detailed research report including:

Executive Summary:
{executive_summary}

Full Analysis:
{analysis}

Structure the report with:
- Introduction
- Methodology
- Findings
- Analysis
- Conclusions
- Recommendations""",
        adapter=adapter,
        output_key="final_report"
    ))
    
    # Execute synthesis
    final_output = synthesis_workflow.execute({
        'topic': topic,
        'research': research_results['final_output'],
        'analysis': analysis_result['final_output'] if analysis_result['success'] else "Analysis incomplete"
    })
    
    # Output results
    print("\n" + "="*60)
    print("RESEARCH COMPLETE")
    print("="*60)
    
    print(f"\nExecutive Summary:\n{final_output['executive_summary']}\n")
    print(f"\nFull Report:\n{final_output['final_report'][:1000]}...")
    
    return final_output

if __name__ == "__main__":
    result = run_research_workflow("The impact of AI on software development practices")
EOF
```

**Save as**: `workflows/examples/research_analysis.py`

---

## Conclusion

**You've mastered advanced workflow patterns!** 🎓

**Patterns Covered**:
- ✅ Multi-Agent workflows (specialist collaboration)
- ✅ Conditional branching (decision-based routing)
- ✅ Iterative refinement (quality gates)
- ✅ Human-in-the-loop (interactive approval)
- ✅ Error recovery (retry, fallback, circuit breaker)
- ✅ Workflow composition (building blocks)
- ✅ State management (pause/resume)
- ✅ Orchestration (map-reduce, fan-out/fan-in, saga)

**Key Takeaways**:

1. **Pattern Selection Matters**
   - Match pattern to problem structure
   - Independent tasks → Parallel
   - Specialized roles → Multi-Agent
   - Quality critical → Iterative

2. **Composition Over Complexity**
   - Build complex workflows from simple steps
   - Reusable components
   - Clear separation of concerns

3. **Error Resilience is Critical**
   - Always plan for failure
   - Retry with backoff
   - Fallback strategies
   - Graceful degradation

4. **State Management Enables Scale**
   - Pause and resume workflows
   - Long-running processes
   - Distributed execution

5. **Human + AI Collaboration**
   - Approval gates for critical decisions
   - Progressive disclosure
   - Variations with selection

**Pattern Selection Guide**:

| Scenario | Best Pattern | Why |
|----------|--------------|-----|
| **Code review by multiple experts** | Multi-Agent | Specialized perspectives |
| **Classify then route** | Conditional | Decision-based routing |
| **Generate until perfect** | Iterative | Quality threshold |
| **Critical decision needed** | Human-in-Loop | Human judgment |
| **API might fail** | Error Recovery | Resilience |
| **Multi-phase pipeline** | Composition | Modularity |
| **Long-running task** | Stateful | Pause/resume |
| **Process 1000 documents** | Map-Reduce | Parallelism + aggregation |

**Time Invested**: ⏱️ 210-240 minutes  
**Ready For**: Production-grade complex workflows

Would you like to continue with the final Tier 3 document (Community Contribution Guide)?