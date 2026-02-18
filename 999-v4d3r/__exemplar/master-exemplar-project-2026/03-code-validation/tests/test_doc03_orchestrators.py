"""
DOC-03 Unit Tests: Advanced Reasoning Architectures - Orchestrators
=====================================================================

Unit tests for Advanced Reasoning Architecture components including:
- AdaptiveReasoningOrchestrator: Dynamic reasoning technique selection
- TokenOptimizer: Token budget management and optimization
- LatencyOptimizer: Latency reduction strategies
- ArchitectureSelector: Architecture selection based on query complexity

Reference: doc3-advanced-reasoning-architectures-theory-to-practice.md
"""

import pytest
from typing import Dict, Any, List


# ============================================================================
# Stub Implementations (Based on DOC-03 patterns)
# ============================================================================

class ComplexityAssessment:
    """Assessment of query complexity for architecture selection."""

    def __init__(self, score: float, requires_external_info: bool,
                 features: Dict[str, Any]):
        self.score = score
        self.requires_external_info = requires_external_info
        self.features = features


class ComplexityAssessor:
    """Assess query complexity for architecture selection."""

    def assess(self, query: str) -> ComplexityAssessment:
        """
        Assess query complexity based on multiple features.

        Features considered:
        - Token count
        - Constraint count
        - Entity count
        - Operator count (and, or, not, if)
        - Nesting depth
        """
        # Simplified complexity scoring
        tokens = len(query.split())

        # Detect complexity indicators
        constraint_keywords = ['must', 'should', 'if', 'when', 'unless', 'constraints', 'conditions']
        constraint_count = sum(1 for kw in constraint_keywords if kw in query.lower())

        operator_count = query.lower().count(' and ') + query.lower().count(' or ')

        # Detect complexity words
        complexity_words = ['analyze', 'multi-step', 'problem', 'several', 'complex']
        complexity_indicators = sum(1 for word in complexity_words if word in query.lower())

        # Calculate complexity score
        complexity_score = (
            0.15 * tokens +
            2.0 * constraint_count +
            1.5 * operator_count +
            2.0 * complexity_indicators
        )

        # Normalize to 0-10 scale
        complexity_score = min(complexity_score, 10.0)

        # Detect external info requirement
        search_keywords = ['find', 'search', 'lookup', 'what is', 'current']
        requires_external = any(kw in query.lower() for kw in search_keywords)

        features = {
            'token_count': tokens,
            'constraint_count': constraint_count,
            'operator_count': operator_count,
            'complexity_score': complexity_score
        }

        return ComplexityAssessment(
            score=complexity_score,
            requires_external_info=requires_external,
            features=features
        )


class ArchitectureSelector:
    """
    Select optimal architecture based on query characteristics.

    Decision logic from DOC-03:
    - Latency constraint < 2000ms → CoT (fast, single pass)
    - Token constraint < 2000 → CoT (efficient)
    - High complexity + accuracy critical + high token budget → ToT
    - High complexity + moderate budget → Self-Consistency
    - External info needed → ReAct
    - Moderate complexity → Self-Consistency
    - Simple queries → CoT (default)
    """

    def select(self, complexity: ComplexityAssessment,
               constraints: Dict[str, Any]) -> str:
        """
        Decision tree for architecture selection.

        Args:
            complexity: Query complexity assessment
            constraints: Resource and performance constraints

        Returns:
            Selected architecture name
        """
        # Constraint: Latency budget
        if constraints.get('max_latency_ms', float('inf')) < 2000:
            return 'cot'  # Fast, single pass

        # Constraint: Token budget
        if constraints.get('max_tokens', float('inf')) < 2000:
            return 'cot'  # Efficient

        # High complexity + accuracy critical
        if complexity.score > 7 and constraints.get('accuracy_critical', False):
            if constraints.get('max_tokens', float('inf')) > 10000:
                return 'tot'  # Rich exploration
            else:
                return 'self_consistency'  # Reliable without explosion

        # External info needed
        if complexity.requires_external_info:
            return 'react'

        # Moderate complexity
        if complexity.score > 5:
            return 'self_consistency'  # Better than CoT, reasonable cost

        # Simple queries
        return 'cot'  # Default


class AdaptiveReasoningOrchestrator:
    """
    Dynamically select and execute reasoning techniques based on query.

    From DOC-03 Pattern 2: Adaptive Architecture Selection
    """

    def __init__(self):
        self.complexity_assessor = ComplexityAssessor()
        self.architecture_selector = ArchitectureSelector()
        self.execution_history: List[Dict[str, Any]] = []

    def select_technique(self, query: str,
                        constraints: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Select optimal reasoning technique for query.

        Args:
            query: Input query
            constraints: Optional resource/performance constraints

        Returns:
            Selection decision with reasoning
        """
        constraints = constraints or {}

        # Assess complexity
        complexity = self.complexity_assessor.assess(query)

        # Select architecture
        selected_arch = self.architecture_selector.select(complexity, constraints)

        return {
            'selected_technique': selected_arch,
            'complexity_score': complexity.score,
            'complexity_features': complexity.features,
            'requires_external_info': complexity.requires_external_info,
            'constraints_applied': constraints
        }

    def execute(self, query: str, constraints: Dict[str, Any] = None,
                fallback_on_error: bool = True) -> Dict[str, Any]:
        """
        Execute query with selected technique and fallback handling.

        Args:
            query: Input query
            constraints: Optional constraints
            fallback_on_error: Whether to fallback to simpler technique on error

        Returns:
            Execution result with technique used
        """
        # Select technique
        selection = self.select_technique(query, constraints)
        selected_technique = selection['selected_technique']

        try:
            # Simulate execution
            result = self._execute_technique(query, selected_technique)

            # Log successful execution
            self.execution_history.append({
                'query': query,
                'technique': selected_technique,
                'status': 'success',
                'complexity': selection['complexity_score']
            })

            return {
                'answer': result,
                'technique_used': selected_technique,
                'status': 'success',
                'fallback_used': False,
                'selection_info': selection
            }

        except Exception as e:
            if not fallback_on_error:
                raise

            # Fallback chain: try simpler techniques until success or exhausted
            current_technique = selected_technique
            fallback_attempts = []

            while True:
                fallback_technique = self._get_fallback_technique(current_technique)
                fallback_attempts.append(fallback_technique)

                try:
                    result = self._execute_technique(query, fallback_technique)

                    self.execution_history.append({
                        'query': query,
                        'technique': fallback_technique,
                        'status': 'success_after_fallback',
                        'original_technique': selected_technique,
                        'fallback_attempts': fallback_attempts,
                        'complexity': selection['complexity_score']
                    })

                    return {
                        'answer': result,
                        'technique_used': fallback_technique,
                        'status': 'success',
                        'fallback_used': True,
                        'original_technique': selected_technique,
                        'fallback_attempts': fallback_attempts,
                        'selection_info': selection
                    }
                except Exception as fallback_error:
                    # If we've already tried CoT (the simplest), give up
                    if fallback_technique == 'cot':
                        self.execution_history.append({
                            'query': query,
                            'technique': selected_technique,
                            'status': 'failed',
                            'error': str(fallback_error),
                            'fallback_attempts': fallback_attempts
                        })
                        raise

                    # Otherwise, try next simpler technique
                    current_technique = fallback_technique

    def _execute_technique(self, query: str, technique: str) -> str:
        """Simulate technique execution (stub)."""
        # In real implementation, this would call actual reasoning modules
        # Only fail for non-CoT techniques to allow fallback testing
        if 'fail_execution' in query and technique != 'cot':
            raise RuntimeError("Simulated execution failure")
        return f"Result from {technique}"

    def _get_fallback_technique(self, technique: str) -> str:
        """Get simpler fallback technique."""
        fallback_map = {
            'tot': 'self_consistency',
            'self_consistency': 'cot',
            'react': 'cot',
            'cot': 'cot'  # No simpler fallback
        }
        return fallback_map.get(technique, 'cot')


class TokenOptimizer:
    """
    Optimize token usage for reasoning architectures.

    From DOC-03: Token Complexity Analysis and Optimization
    """

    def __init__(self, default_budget: int = 10000):
        self.default_budget = default_budget
        self.optimization_history: List[Dict[str, Any]] = []

    def optimize_tot_params(self, problem: Dict[str, Any],
                           budget_tokens: int) -> Dict[str, Any]:
        """
        Determine optimal ToT parameters for token budget.

        From DOC-03:
        - Estimate tokens per node (~150 for thought + evaluation)
        - Reserve tokens for solution extraction (~500)
        - Calculate feasible tree parameters
        - Prefer balanced tree: b^d ≈ max_nodes
        """
        # Estimate tokens per node
        tokens_per_node = 150  # thought generation + evaluation

        # Reserve for solution extraction
        solution_tokens = 500

        # Available for tree exploration
        available = budget_tokens - solution_tokens

        if available < 0:
            return {
                'feasible': False,
                'error': 'Budget too small for ToT',
                'min_required': solution_tokens + tokens_per_node
            }

        # Calculate feasible tree parameters
        max_nodes = available // tokens_per_node

        # Optimize branching and depth
        if max_nodes < 10:
            branching, depth = 2, 2  # Minimal tree
        elif max_nodes < 50:
            branching, depth = 3, 3
        elif max_nodes < 200:
            branching, depth = 4, 3
        else:
            branching, depth = 5, 4  # Rich exploration

        estimated_nodes = branching ** depth
        estimated_tokens = estimated_nodes * tokens_per_node + solution_tokens

        result = {
            'feasible': True,
            'branching': branching,
            'depth': depth,
            'estimated_nodes': estimated_nodes,
            'estimated_tokens': estimated_tokens,
            'budget_tokens': budget_tokens,
            'tokens_available': available,
            'utilization': estimated_tokens / budget_tokens
        }

        self.optimization_history.append({
            'problem': problem.get('id', 'unknown'),
            'budget': budget_tokens,
            'result': result
        })

        return result

    def optimize_self_consistency_samples(self, problem: Dict[str, Any],
                                         budget_tokens: int,
                                         target_accuracy: float = 0.85) -> Dict[str, Any]:
        """
        Determine optimal sample count for Self-Consistency.

        From DOC-03:
        - Accuracy ≈ base_accuracy + c√k where c ≈ 0.05
        - Minimum 3 samples for voting
        """
        tokens_per_sample = problem.get('estimated_tokens_per_sample', 1000)

        max_samples = budget_tokens // tokens_per_sample

        if max_samples < 3:
            return {
                'feasible': False,
                'error': 'Budget too small for Self-Consistency (min 3 samples)',
                'min_required': 3 * tokens_per_sample
            }

        # Base accuracy and improvement coefficient
        base_accuracy = problem.get('base_accuracy', 0.7)
        c = 0.05  # Empirical coefficient

        # Calculate required samples for target accuracy
        accuracy_gain_needed = target_accuracy - base_accuracy

        if accuracy_gain_needed <= 0:
            required_k = 3  # Minimum
        else:
            required_k = int((accuracy_gain_needed / c) ** 2)

        # Constrain to budget
        optimal_k = min(max(required_k, 3), max_samples)

        expected_accuracy = base_accuracy + c * (optimal_k ** 0.5)
        token_usage = optimal_k * tokens_per_sample

        result = {
            'feasible': True,
            'samples': optimal_k,
            'expected_accuracy': round(expected_accuracy, 3),
            'token_usage': token_usage,
            'budget_tokens': budget_tokens,
            'utilization': token_usage / budget_tokens,
            'base_accuracy': base_accuracy,
            'accuracy_gain': round(expected_accuracy - base_accuracy, 3)
        }

        self.optimization_history.append({
            'problem': problem.get('id', 'unknown'),
            'budget': budget_tokens,
            'result': result
        })

        return result

    def allocate_budget(self, total_budget: int,
                       tasks: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Allocate token budget across multiple tasks.

        Strategy: Proportional allocation based on complexity
        """
        if not tasks:
            return {'allocations': [], 'total_allocated': 0}

        # Calculate total complexity
        total_complexity = sum(task.get('complexity', 1.0) for task in tasks)

        # Allocate proportionally
        allocations = []
        remaining_budget = total_budget

        for i, task in enumerate(tasks):
            task_complexity = task.get('complexity', 1.0)

            # Last task gets remaining budget to avoid rounding issues
            if i == len(tasks) - 1:
                allocation = remaining_budget
            else:
                allocation = int((task_complexity / total_complexity) * total_budget)
                remaining_budget -= allocation

            allocations.append({
                'task_id': task.get('id', f'task_{i}'),
                'complexity': task_complexity,
                'allocated_tokens': allocation,
                'percentage': round((allocation / total_budget) * 100, 1)
            })

        return {
            'allocations': allocations,
            'total_allocated': total_budget,
            'num_tasks': len(tasks)
        }


class LatencyOptimizer:
    """
    Minimize latency for reasoning architectures.

    From DOC-03: Latency Analysis and Optimization
    """

    def __init__(self):
        self.optimization_history: List[Dict[str, Any]] = []

    def optimize_for_latency(self, query: str,
                           max_latency_ms: float,
                           techniques_available: List[str] = None) -> Dict[str, Any]:
        """
        Select and configure technique to meet latency constraint.

        From DOC-03 Latency Analysis:
        - CoT: 1-5 seconds (single LLM call)
        - ToT: depth × L_llm (sequential)
        - Self-Consistency: L_llm + L_agg (parallelizable k×)
        - ReAct: m × (L_llm + L_tool) (sequential)
        """
        techniques_available = techniques_available or ['cot', 'self_consistency', 'tot', 'react']

        # Latency estimates (milliseconds)
        latency_estimates = {
            'cot': {
                'sequential': 2000,
                'parallel': 2000,
                'description': 'Single pass reasoning'
            },
            'self_consistency': {
                'sequential': 10000,  # 5 samples × 2s
                'parallel': 2100,  # 2s LLM + 100ms aggregation
                'description': 'Ensemble with parallel execution'
            },
            'tot': {
                'sequential': 8000,  # depth=4 × 2s
                'parallel': 8000,  # Inherently sequential
                'description': 'Tree search (depth-dependent)'
            },
            'react': {
                'sequential': 6000,  # 3 iterations × 2s
                'parallel': 6000,  # Inherently sequential
                'description': 'Tool-augmented reasoning'
            }
        }

        # Find techniques that meet latency constraint
        feasible_techniques = []

        for technique in techniques_available:
            if technique not in latency_estimates:
                continue

            estimates = latency_estimates[technique]

            # Use parallel latency if available
            latency = estimates['parallel']

            if latency <= max_latency_ms:
                feasible_techniques.append({
                    'technique': technique,
                    'estimated_latency_ms': latency,
                    'can_parallelize': estimates['parallel'] < estimates['sequential'],
                    'speedup': estimates['sequential'] / estimates['parallel'],
                    'description': estimates['description']
                })

        # Sort by latency (fastest first)
        feasible_techniques.sort(key=lambda x: x['estimated_latency_ms'])

        result = {
            'max_latency_ms': max_latency_ms,
            'feasible_techniques': feasible_techniques,
            'recommended_technique': feasible_techniques[0]['technique'] if feasible_techniques else None,
            'all_techniques_exceed_budget': len(feasible_techniques) == 0
        }

        self.optimization_history.append({
            'query': query[:50],
            'max_latency': max_latency_ms,
            'result': result
        })

        return result

    def estimate_parallel_speedup(self, technique: str,
                                 config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Estimate speedup from parallelization.

        Only Self-Consistency benefits significantly from parallelization.
        """
        if technique == 'self_consistency':
            samples = config.get('samples', 5)
            l_llm = 2000  # ms
            l_agg = 100   # ms

            sequential_latency = samples * l_llm
            parallel_latency = l_llm + l_agg
            speedup = sequential_latency / parallel_latency

            return {
                'technique': technique,
                'parallelizable': True,
                'sequential_latency_ms': sequential_latency,
                'parallel_latency_ms': parallel_latency,
                'speedup': round(speedup, 2),
                'recommendation': 'Use parallel execution'
            }

        elif technique in ['tot', 'react', 'cot']:
            return {
                'technique': technique,
                'parallelizable': False,
                'reason': 'Inherently sequential dependencies',
                'recommendation': 'Cannot parallelize significantly'
            }

        else:
            return {
                'technique': technique,
                'parallelizable': False,
                'reason': 'Unknown technique'
            }


# ============================================================================
# TEST SUITE
# ============================================================================

@pytest.mark.doc03
@pytest.mark.unit
class TestAdaptiveReasoningOrchestrator:
    """Test suite for AdaptiveReasoningOrchestrator."""

    def test_orchestrator_technique_selection(self, sample_orchestrator_decisions):
        """
        Test reasoning technique selection logic.

        Validates that orchestrator correctly maps query characteristics
        to appropriate reasoning techniques following DOC-03 decision tree.
        """
        orchestrator = AdaptiveReasoningOrchestrator()

        # Test 1: Simple query → CoT
        simple_result = orchestrator.select_technique("Calculate 2 plus 2")
        assert simple_result['selected_technique'] == 'cot'
        assert simple_result['complexity_score'] < 5

        # Test 2: Complex query with constraints → appropriate technique
        complex_query = "Analyze this multi-step problem with several constraints and conditions"
        complex_result = orchestrator.select_technique(
            complex_query,
            constraints={'max_tokens': 15000, 'accuracy_critical': True}
        )
        # Should select ToT or Self-Consistency for complex queries
        assert complex_result['selected_technique'] in ['tot', 'self_consistency']
        assert complex_result['complexity_score'] > 5

        # Test 3: Search query → ReAct
        search_query = "Find current information about Python testing frameworks"
        search_result = orchestrator.select_technique(search_query)
        assert search_result['selected_technique'] == 'react'
        assert search_result['requires_external_info'] is True

        # Test 4: Latency constraint → fast technique
        latency_result = orchestrator.select_technique(
            "Moderate complexity query",
            constraints={'max_latency_ms': 1500}
        )
        assert latency_result['selected_technique'] == 'cot'  # Fast technique

        # Test 5: Token budget constraint → efficient technique
        budget_result = orchestrator.select_technique(
            "Complex analytical query",
            constraints={'max_tokens': 1500}
        )
        assert budget_result['selected_technique'] == 'cot'  # Efficient technique

    def test_orchestrator_execution(self):
        """
        Test technique execution with fallback handling.

        Validates that orchestrator can execute selected techniques and
        fallback to simpler techniques on failure as per DOC-03 patterns.
        """
        orchestrator = AdaptiveReasoningOrchestrator()

        # Test 1: Successful execution
        result = orchestrator.execute("Calculate 2 plus 2")
        assert result['status'] == 'success'
        assert 'answer' in result
        assert result['fallback_used'] is False
        assert result['technique_used'] == 'cot'

        # Test 2: Execution with fallback
        # Query that triggers error in execution - use highly complex query to trigger ToT
        fallback_result = orchestrator.execute(
            "fail_execution analyze this extremely complex multi-step problem with several constraints and conditions that must be satisfied",
            constraints={'accuracy_critical': True, 'max_tokens': 15000}
        )
        # Should fallback from tot to self_consistency or cot
        assert fallback_result['status'] == 'success'
        assert fallback_result['fallback_used'] is True
        assert fallback_result['technique_used'] in ['cot', 'self_consistency']

        # Test 3: Verify execution history logging
        assert len(orchestrator.execution_history) >= 2
        history_entry = orchestrator.execution_history[0]
        assert 'query' in history_entry
        assert 'technique' in history_entry
        assert 'status' in history_entry

        # Test 4: Execution without fallback should raise
        # Use complex query to trigger non-CoT technique
        with pytest.raises(RuntimeError):
            orchestrator.execute(
                "fail_execution analyze this extremely complex multi-step problem with several constraints",
                constraints={'accuracy_critical': True, 'max_tokens': 15000},
                fallback_on_error=False
            )


@pytest.mark.doc03
@pytest.mark.unit
class TestTokenOptimizer:
    """Test suite for TokenOptimizer."""

    def test_token_optimizer_budget_management(self, sample_optimizer_configs):
        """
        Test token budget allocation and optimization.

        Validates TokenOptimizer correctly allocates budgets and optimizes
        parameters for different reasoning techniques following DOC-03 models.
        """
        optimizer = TokenOptimizer(default_budget=10000)

        # Test 1: ToT parameter optimization
        tot_result = optimizer.optimize_tot_params(
            problem={'id': 'test_problem_1'},
            budget_tokens=5000
        )
        assert tot_result['feasible'] is True
        assert 'branching' in tot_result
        assert 'depth' in tot_result
        assert tot_result['estimated_tokens'] <= 5000
        assert 0 < tot_result['utilization'] <= 1.0

        # Test 2: ToT with insufficient budget
        small_budget_result = optimizer.optimize_tot_params(
            problem={'id': 'test_problem_2'},
            budget_tokens=400  # Too small
        )
        assert small_budget_result['feasible'] is False
        assert 'error' in small_budget_result

        # Test 3: Self-Consistency sample optimization
        sc_result = optimizer.optimize_self_consistency_samples(
            problem={
                'id': 'test_problem_3',
                'estimated_tokens_per_sample': 1000,
                'base_accuracy': 0.7
            },
            budget_tokens=10000,
            target_accuracy=0.85
        )
        assert sc_result['feasible'] is True
        assert sc_result['samples'] >= 3  # Minimum for voting
        assert sc_result['expected_accuracy'] >= sc_result['base_accuracy']
        assert sc_result['token_usage'] <= 10000

        # Test 4: SC with insufficient budget
        sc_small_budget = optimizer.optimize_self_consistency_samples(
            problem={
                'id': 'test_problem_4',
                'estimated_tokens_per_sample': 1000
            },
            budget_tokens=2000  # Only 2 samples possible
        )
        assert sc_small_budget['feasible'] is False

        # Test 5: Budget allocation across tasks
        tasks = [
            {'id': 'task1', 'complexity': 1.0},
            {'id': 'task2', 'complexity': 2.0},
            {'id': 'task3', 'complexity': 3.0}
        ]
        allocation_result = optimizer.allocate_budget(
            total_budget=6000,
            tasks=tasks
        )
        assert allocation_result['total_allocated'] == 6000
        assert len(allocation_result['allocations']) == 3
        # Verify proportional allocation (task3 should get most)
        allocations = allocation_result['allocations']
        assert allocations[2]['allocated_tokens'] > allocations[1]['allocated_tokens']
        assert allocations[1]['allocated_tokens'] > allocations[0]['allocated_tokens']

        # Test 6: Verify optimization history tracking
        # History includes: tot success, sc success (failures don't add to history)
        assert len(optimizer.optimization_history) >= 2


@pytest.mark.doc03
@pytest.mark.unit
class TestLatencyOptimizer:
    """Test suite for LatencyOptimizer."""

    def test_latency_optimizer_performance(self):
        """
        Test latency reduction strategies and optimization.

        Validates LatencyOptimizer correctly identifies techniques that meet
        latency constraints and recommends parallelization per DOC-03 analysis.
        """
        optimizer = LatencyOptimizer()

        # Test 1: Strict latency constraint → only fast techniques
        strict_result = optimizer.optimize_for_latency(
            query="Test query",
            max_latency_ms=2500,
            techniques_available=['cot', 'self_consistency', 'tot', 'react']
        )
        assert strict_result['max_latency_ms'] == 2500
        assert len(strict_result['feasible_techniques']) > 0
        # CoT and possibly parallel SC should be feasible
        recommended = strict_result['recommended_technique']
        assert recommended in ['cot', 'self_consistency']
        assert strict_result['all_techniques_exceed_budget'] is False

        # Test 2: Moderate latency constraint → more options
        moderate_result = optimizer.optimize_for_latency(
            query="Test query",
            max_latency_ms=7000
        )
        # Should have more feasible techniques
        assert len(moderate_result['feasible_techniques']) >= len(strict_result['feasible_techniques'])

        # Test 3: Very strict constraint → no feasible techniques
        impossible_result = optimizer.optimize_for_latency(
            query="Test query",
            max_latency_ms=500  # Unrealistically low
        )
        assert impossible_result['all_techniques_exceed_budget'] is True
        assert impossible_result['recommended_technique'] is None

        # Test 4: Parallel speedup estimation - Self-Consistency
        sc_speedup = optimizer.estimate_parallel_speedup(
            technique='self_consistency',
            config={'samples': 5}
        )
        assert sc_speedup['parallelizable'] is True
        assert sc_speedup['speedup'] > 1.0  # Should show speedup
        assert sc_speedup['parallel_latency_ms'] < sc_speedup['sequential_latency_ms']

        # Test 5: Parallel speedup estimation - ToT (not parallelizable)
        tot_speedup = optimizer.estimate_parallel_speedup(
            technique='tot',
            config={'branching': 3, 'depth': 4}
        )
        assert tot_speedup['parallelizable'] is False
        assert 'sequential' in tot_speedup['reason'].lower()

        # Test 6: Verify optimization history
        assert len(optimizer.optimization_history) >= 3


@pytest.mark.doc03
@pytest.mark.unit
class TestArchitectureSelector:
    """Test suite for ArchitectureSelector."""

    def test_architecture_selector_decision_tree(self):
        """
        Test architecture selection based on query complexity.

        Validates ArchitectureSelector implements correct decision tree
        from DOC-03 for mapping query characteristics to architectures.
        """
        selector = ArchitectureSelector()

        # Test 1: Simple query → CoT
        simple_complexity = ComplexityAssessment(
            score=3.0,
            requires_external_info=False,
            features={'token_count': 10}
        )
        simple_selection = selector.select(simple_complexity, {})
        assert simple_selection == 'cot'

        # Test 2: High complexity + accuracy critical + high budget → ToT
        complex_high_budget = ComplexityAssessment(
            score=8.5,
            requires_external_info=False,
            features={'token_count': 100, 'constraint_count': 5}
        )
        tot_selection = selector.select(
            complex_high_budget,
            {'accuracy_critical': True, 'max_tokens': 15000}
        )
        assert tot_selection == 'tot'

        # Test 3: High complexity + accuracy critical + moderate budget → SC
        sc_selection = selector.select(
            complex_high_budget,
            {'accuracy_critical': True, 'max_tokens': 5000}
        )
        assert sc_selection == 'self_consistency'

        # Test 4: External info required → ReAct
        external_info = ComplexityAssessment(
            score=5.0,
            requires_external_info=True,
            features={'token_count': 30}
        )
        react_selection = selector.select(external_info, {})
        assert react_selection == 'react'

        # Test 5: Latency constraint → CoT (fast)
        latency_constrained = ComplexityAssessment(
            score=6.0,
            requires_external_info=False,
            features={'token_count': 40}
        )
        latency_selection = selector.select(
            latency_constrained,
            {'max_latency_ms': 1500}
        )
        assert latency_selection == 'cot'

        # Test 6: Token budget constraint → CoT (efficient)
        token_constrained = ComplexityAssessment(
            score=7.0,
            requires_external_info=False,
            features={'token_count': 50}
        )
        token_selection = selector.select(
            token_constrained,
            {'max_tokens': 1500}
        )
        assert token_selection == 'cot'

        # Test 7: Moderate complexity → Self-Consistency
        moderate_complexity = ComplexityAssessment(
            score=6.0,
            requires_external_info=False,
            features={'token_count': 40}
        )
        moderate_selection = selector.select(moderate_complexity, {})
        assert moderate_selection == 'self_consistency'
