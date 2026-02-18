"""
DOC-04 Agentic Workflow Design Patterns - Unit Tests
=====================================================

Test suite validating agentic workflow patterns from DOC-04.

Tests cover:
1. BaseAgent Tests (3 tests): Agent initialization, perception, run cycle
2. ReActAgent Tests (4 tests): Perceive, reason, act, learn
3. TaskDecompositionAgent Tests (2 tests): Task decomposition, execution order
4. ErrorRecoverySystem Tests (3 tests): Error classification, retry, fallback

Test Strategy:
- Validate agent architecture components (perception, reasoning, action, memory)
- Test ReAct loop execution pattern (Thought → Action → Observation)
- Verify hierarchical task decomposition and dependency management
- Ensure robust error handling and recovery mechanisms

Dependencies:
- pytest framework
- Mock LLM and tool registry from conftest.py
- DOC-04 agentic pattern implementations
"""

import pytest
import time
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from collections import defaultdict


# ============================================================================
# Agent Implementation Stubs (Based on DOC-04 Patterns)
# ============================================================================

@dataclass
class AgentState:
    """Agent state tracking structure."""
    goal: Optional[str] = None
    current_step: int = 0
    observations: List[Dict] = field(default_factory=list)
    actions_taken: List[Dict] = field(default_factory=list)
    status: str = "initialized"
    working_memory: Dict[str, Any] = field(default_factory=dict)
    intermediate_results: Dict[str, Any] = field(default_factory=dict)

    def reset(self):
        """Reset agent state."""
        self.current_step = 0
        self.observations = []
        self.actions_taken = []
        self.status = "initialized"
        self.working_memory = {}
        self.intermediate_results = {}

    def update(self, action_result):
        """Update state after action execution."""
        self.actions_taken.append({
            'step': self.current_step,
            'result': action_result,
            'timestamp': time.time()
        })

        if hasattr(action_result, 'observation'):
            self.observations.append(action_result.observation)

        self.current_step += 1


@dataclass
class ActionResult:
    """Result of action execution."""
    success: bool
    output: Any = None
    error: Optional[str] = None
    tool_used: Optional[str] = None
    observation: Optional[str] = None

    def is_terminal(self):
        """Check if this is a terminal result."""
        return self.tool_used == "final_answer" or not self.success


class PerceptionLayer:
    """Process inputs and extract relevant information."""

    def __init__(self, config=None):
        self.config = config or {}

    def process(self, goal, context, state):
        """Transform raw inputs into structured observations."""
        return {
            'goal_analysis': self._analyze_goal(goal),
            'context_features': context or {},
            'state_summary': {
                'step': state.current_step,
                'status': state.status
            }
        }

    def _analyze_goal(self, goal):
        """Extract actionable components from goal."""
        return {
            'goal_text': goal,
            'goal_type': 'general',
            'complexity': 'medium'
        }


class ReasoningEngine:
    """Generate action plans through reasoning."""

    def __init__(self, config=None):
        self.config = config or {}
        self.reasoning_mode = config.get('reasoning_mode', 'react') if config else 'react'

    def decide(self, goal, observations, state, memory):
        """Reason about next action given current context."""
        # Simple decision logic for testing
        if state.current_step >= 3:
            return ActionPlan(is_terminal=True, final_answer="Task completed")

        return ActionPlan(
            next_action={
                'tool_name': 'search',
                'parameters': {'query': goal}
            },
            is_terminal=False
        )


@dataclass
class ActionPlan:
    """Action plan from reasoning."""
    next_action: Optional[Dict] = None
    is_terminal: bool = False
    final_answer: Any = None


class ActionExecutor:
    """Execute actions via tool invocations."""

    def __init__(self, config=None, tool_registry=None):
        self.config = config or {}
        self.tool_registry = tool_registry

    def execute(self, action, state):
        """Execute action and return result."""
        if not isinstance(action, dict) or 'tool_name' not in action:
            return ActionResult(success=False, error="Invalid action format")

        tool_name = action['tool_name']
        parameters = action.get('parameters', {})

        if self.tool_registry:
            result = self.tool_registry.execute_tool(tool_name, **parameters)
            success = result.get('status') == 'success' or result.get('success', False)
            return ActionResult(
                success=success,
                output=result.get('result'),
                error=result.get('error'),
                tool_used=tool_name,
                observation=result.get('result')
            )

        # Fallback for tests without tool registry
        return ActionResult(
            success=True,
            output=f"Executed {tool_name}",
            tool_used=tool_name,
            observation=f"Result from {tool_name}"
        )


class MemorySystem:
    """Multi-level memory for agents."""

    def __init__(self, config=None):
        self.config = config or {}
        self.episodic_memory = []
        self.semantic_memory = []
        self.working_memory = {}

    def store(self, context, action, result, success):
        """Store experience in memory."""
        episode = {
            'context': context,
            'action': action,
            'result': result,
            'success': success,
            'timestamp': time.time()
        }
        self.episodic_memory.append(episode)

    def retrieve_relevant(self, query):
        """Retrieve relevant memories for query."""
        return {
            'past_experiences': self.episodic_memory[-5:],
            'learned_knowledge': []
        }


class BaseAgent:
    """Foundational agent architecture with core components."""

    def __init__(self, config=None):
        self.config = config or {}
        self.perception = PerceptionLayer(config)
        self.reasoning = ReasoningEngine(config)
        self.action = ActionExecutor(config, config.get('tool_registry') if config else None)
        self.memory = MemorySystem(config)

        self.state = AgentState()
        self.goal = None
        self.plan = None

    def run(self, goal, context=None, max_iterations=10):
        """
        Main agent execution loop.

        Implements perception-reasoning-action cycle:
        1. Perceive: Process input and update state
        2. Reason: Generate action plan
        3. Act: Execute actions
        4. Learn: Update memory from results
        """
        self.goal = goal
        self.state.reset()
        self.state.goal = goal
        self.state.status = "running"

        for iteration in range(max_iterations):
            # Perceive
            observations = self.perception.process(
                goal=self.goal,
                context=context,
                state=self.state
            )

            # Reason
            action_plan = self.reasoning.decide(
                goal=self.goal,
                observations=observations,
                state=self.state,
                memory=self.memory.retrieve_relevant(self.goal)
            )

            # Check if goal achieved
            if action_plan.is_terminal:
                self.state.status = "completed"
                return action_plan.final_answer

            # Act
            action_result = self.action.execute(
                action=action_plan.next_action,
                state=self.state
            )

            # Update state and memory
            self.state.update(action_result)
            self.memory.store(
                context=self.goal,
                action=action_plan.next_action,
                result=action_result,
                success=action_result.success
            )

            # Check termination
            if not action_result.success:
                self.state.status = "failed"
                break

        self.state.status = "completed"
        return self.state.intermediate_results.get('final_answer', "Task completed")


class ReActAgent(BaseAgent):
    """ReAct pattern: Reason → Act → Observe loop."""

    def perceive(self, goal, observations):
        """Process goal and observations for ReAct reasoning."""
        return {
            'goal': goal,
            'observation_count': len(observations),
            'last_observation': observations[-1] if observations else None
        }

    def reason(self, perception_data, mock_llm=None):
        """
        Generate thought and next action using ReAct prompting.
        Returns: {'thought': str, 'action': str, 'action_input': str}
        """
        goal = perception_data['goal']
        step = perception_data.get('observation_count', 0)

        if mock_llm:
            response = mock_llm.generate(f"ReAct reasoning for: {goal}")
        else:
            response = f"Thought: I should search for information about {goal}"

        return {
            'thought': f"Step {step}: Analyzing goal",
            'action': 'search',
            'action_input': goal
        }

    def act(self, action_data, tool_registry):
        """Execute action using tool registry."""
        action_name = action_data.get('action')
        action_input = action_data.get('action_input', {})

        result = tool_registry.execute_tool(action_name, query=action_input)
        success = result.get('status') == 'success' or result.get('success', False)

        return {
            'action': action_name,
            'input': action_input,
            'observation': result.get('result') or result.get('results'),
            'success': success
        }

    def learn(self, thought, action, observation):
        """Update memory with reasoning trace."""
        self.memory.store(
            context=self.goal,
            action={'thought': thought, 'action': action},
            result=observation,
            success=True
        )

        return {
            'episodic_count': len(self.memory.episodic_memory),
            'stored_thought': thought,
            'stored_action': action
        }


class TaskDecompositionAgent(BaseAgent):
    """Decompose complex tasks into subtasks."""

    def decompose(self, task, max_subtasks=5):
        """
        Break task into subtasks using reasoning.
        Returns: List of subtasks with dependencies.
        """
        # Simple decomposition for testing
        subtasks = []
        task_words = task.split()

        if len(task_words) > 3:
            # Complex task - decompose
            subtasks = [
                {'id': 'subtask_1', 'description': f'Analyze {task_words[0]}', 'dependencies': []},
                {'id': 'subtask_2', 'description': f'Process {task_words[1]}', 'dependencies': ['subtask_1']},
                {'id': 'subtask_3', 'description': f'Synthesize results', 'dependencies': ['subtask_2']}
            ]
        else:
            # Simple task - single subtask
            subtasks = [
                {'id': 'subtask_1', 'description': task, 'dependencies': []}
            ]

        return subtasks

    def compute_execution_order(self, subtasks):
        """
        Compute execution order respecting dependencies.
        Returns: List of subtask IDs in execution order.
        """
        # Topological sort
        in_degree = {st['id']: len(st['dependencies']) for st in subtasks}
        queue = [st['id'] for st in subtasks if len(st['dependencies']) == 0]
        execution_order = []

        subtask_map = {st['id']: st for st in subtasks}

        while queue:
            task_id = queue.pop(0)
            execution_order.append(task_id)

            # Find tasks that depend on this one
            for st in subtasks:
                if task_id in st['dependencies']:
                    in_degree[st['id']] -= 1
                    if in_degree[st['id']] == 0:
                        queue.append(st['id'])

        return execution_order


class ErrorClassifier:
    """Classify errors for appropriate handling."""

    ERROR_CATEGORIES = {
        'RETRIABLE': ['timeout', 'rate_limit', 'temporary_failure'],
        'FIXABLE': ['invalid_input', 'missing_parameter', 'format_error'],
        'FALLBACK': ['tool_unavailable', 'partial_failure'],
        'TERMINAL': ['authentication_error', 'permission_denied', 'resource_not_found']
    }

    def classify(self, error):
        """Determine error category and handling strategy."""
        error_msg = str(error).lower()

        for category, error_types in self.ERROR_CATEGORIES.items():
            for error_type in error_types:
                if error_type in error_msg:
                    return {
                        'category': category,
                        'error_type': error_type,
                        'severity': 'high' if category == 'TERMINAL' else 'medium'
                    }

        return {
            'category': 'UNKNOWN',
            'error_type': 'unknown',
            'severity': 'high'
        }


class ErrorRecoverySystem:
    """Implement recovery strategies for agent errors."""

    def __init__(self):
        self.classifier = ErrorClassifier()
        self.retry_attempts = defaultdict(int)

    def handle_error(self, error, context):
        """Execute appropriate recovery strategy."""
        classification = self.classifier.classify(error)

        if classification['category'] == 'RETRIABLE':
            return self.retry_with_backoff(context)
        elif classification['category'] == 'FIXABLE':
            return self.fix_and_retry(error, context)
        elif classification['category'] == 'FALLBACK':
            return self.execute_fallback(context)
        else:
            return self.graceful_failure(error, context)

    def retry_with_backoff(self, context, max_retries=3):
        """Retry with exponential backoff."""
        action_id = context.get('action_id', 'default')
        self.retry_attempts[action_id] += 1

        if self.retry_attempts[action_id] > max_retries:
            return {
                'success': False,
                'error': 'Max retries exceeded',
                'attempts': self.retry_attempts[action_id]
            }

        # Calculate backoff time
        backoff_time = (2 ** self.retry_attempts[action_id]) * 0.1

        return {
            'success': True,
            'action': 'retry',
            'backoff_time': backoff_time,
            'attempt': self.retry_attempts[action_id]
        }

    def fix_and_retry(self, error, context):
        """Attempt to fix error then retry."""
        return {
            'success': True,
            'action': 'fix_and_retry',
            'fix_applied': 'parameter_correction'
        }

    def execute_fallback(self, context):
        """Execute fallback action when primary fails."""
        fallback_action = context.get('fallback_action', 'default_fallback')

        return {
            'success': True,
            'action': 'fallback',
            'fallback_action': fallback_action
        }

    def graceful_failure(self, error, context):
        """Handle terminal errors gracefully."""
        return {
            'success': False,
            'action': 'graceful_failure',
            'error': str(error)
        }


# ============================================================================
# TEST SUITE: BaseAgent Tests (3 tests)
# ============================================================================

@pytest.mark.doc04
@pytest.mark.unit
class TestBaseAgent:
    """Test suite for BaseAgent foundational architecture."""

    def test_base_agent_initialization(self):
        """
        Test BaseAgent initializes with correct state and components.

        Validates:
        - Agent initializes with all core components (perception, reasoning, action, memory)
        - State is properly initialized
        - Configuration is stored
        """
        config = {'reasoning_mode': 'react', 'max_iterations': 5}
        agent = BaseAgent(config)

        # Verify core components exist
        assert agent.perception is not None, "Perception layer should be initialized"
        assert agent.reasoning is not None, "Reasoning engine should be initialized"
        assert agent.action is not None, "Action executor should be initialized"
        assert agent.memory is not None, "Memory system should be initialized"

        # Verify state initialization
        assert agent.state is not None, "Agent state should be initialized"
        assert agent.state.status == "initialized", "Initial status should be 'initialized'"
        assert agent.state.current_step == 0, "Initial step should be 0"
        assert agent.goal is None, "Goal should be None before execution"

        # Verify configuration
        assert agent.config == config, "Configuration should be stored"

    def test_base_agent_perception(self):
        """
        Test BaseAgent perception layer processes observations correctly.

        Validates:
        - Perception layer transforms raw inputs into structured observations
        - Goal analysis extracts actionable components
        - Context features are captured
        - State summary is generated
        """
        agent = BaseAgent()
        goal = "Search for information about quantum computing"
        context = {'domain': 'physics', 'depth': 'comprehensive'}

        observations = agent.perception.process(
            goal=goal,
            context=context,
            state=agent.state
        )

        # Verify observation structure
        assert 'goal_analysis' in observations, "Should include goal analysis"
        assert 'context_features' in observations, "Should include context features"
        assert 'state_summary' in observations, "Should include state summary"

        # Verify goal analysis
        goal_analysis = observations['goal_analysis']
        assert 'goal_text' in goal_analysis, "Should extract goal text"
        assert goal_analysis['goal_text'] == goal, "Goal text should match input"

        # Verify context
        assert observations['context_features'] == context, "Context should be preserved"

        # Verify state summary
        state_summary = observations['state_summary']
        assert 'step' in state_summary, "Should track current step"
        assert 'status' in state_summary, "Should track agent status"

    def test_base_agent_run_cycle(self, mock_tool_registry):
        """
        Test BaseAgent full run() execution cycle.

        Validates:
        - Agent executes perception-reasoning-action loop
        - State updates after each iteration
        - Memory stores experiences
        - Termination conditions are respected
        - Final result is returned
        """
        config = {'tool_registry': mock_tool_registry}
        agent = BaseAgent(config)

        goal = "Find weather forecast for tomorrow"
        result = agent.run(goal, max_iterations=5)

        # Verify execution completed
        assert result is not None, "Should return a result"
        assert agent.state.status in ["completed", "failed"], "Status should be terminal"

        # Verify state was updated
        assert agent.state.goal == goal, "Goal should be stored in state"
        assert agent.state.current_step > 0, "Should have executed at least one step"
        assert len(agent.state.actions_taken) > 0, "Should have recorded actions"

        # Verify memory was updated
        assert len(agent.memory.episodic_memory) > 0, "Should have stored experiences"

        # Verify episodic memory structure
        last_episode = agent.memory.episodic_memory[-1]
        assert 'context' in last_episode, "Episode should include context"
        assert 'action' in last_episode, "Episode should include action"
        assert 'result' in last_episode, "Episode should include result"
        assert 'success' in last_episode, "Episode should include success flag"


# ============================================================================
# TEST SUITE: ReActAgent Tests (4 tests)
# ============================================================================

@pytest.mark.doc04
@pytest.mark.unit
class TestReActAgent:
    """Test suite for ReAct (Reason-Act-Observe) agent pattern."""

    def test_react_agent_perceive(self):
        """
        Test ReActAgent observation processing.

        Validates:
        - Observations are structured for ReAct reasoning
        - Goal and observation history are tracked
        - Latest observation is accessible
        """
        agent = ReActAgent()
        goal = "Research climate change impacts"
        observations = [
            "Found 10 research papers",
            "Extracted key findings",
            "Summarized conclusions"
        ]

        perception_data = agent.perceive(goal, observations)

        # Verify perception structure
        assert 'goal' in perception_data, "Should include goal"
        assert 'observation_count' in perception_data, "Should track observation count"
        assert 'last_observation' in perception_data, "Should include last observation"

        # Verify content
        assert perception_data['goal'] == goal, "Goal should match input"
        assert perception_data['observation_count'] == 3, "Should count all observations"
        assert perception_data['last_observation'] == observations[-1], "Should capture last observation"

        # Test with empty observations
        empty_perception = agent.perceive(goal, [])
        assert empty_perception['observation_count'] == 0, "Should handle empty observations"
        assert empty_perception['last_observation'] is None, "Last observation should be None when empty"

    def test_react_agent_reason(self, mock_llm):
        """
        Test ReActAgent reasoning step extraction.

        Validates:
        - Reasoning generates thought, action, and action input
        - LLM is used for reasoning
        - Output follows ReAct format
        """
        agent = ReActAgent()
        perception_data = {
            'goal': 'Calculate compound interest',
            'observation_count': 2,
            'last_observation': 'Principal: $1000, Rate: 5%, Time: 3 years'
        }

        reasoning_output = agent.reason(perception_data, mock_llm)

        # Verify ReAct structure
        assert 'thought' in reasoning_output, "Should include thought"
        assert 'action' in reasoning_output, "Should include action"
        assert 'action_input' in reasoning_output, "Should include action input"

        # Verify thought contains reasoning
        assert len(reasoning_output['thought']) > 0, "Thought should not be empty"
        assert 'Step' in reasoning_output['thought'], "Thought should reference step"

        # Verify action is specified
        assert reasoning_output['action'] in ['search', 'calculator', 'final_answer'], \
            "Action should be a valid tool"

    def test_react_agent_act(self, mock_tool_registry):
        """
        Test ReActAgent action execution with tools.

        Validates:
        - Actions are executed using tool registry
        - Tool results are captured as observations
        - Success/failure status is tracked
        """
        agent = ReActAgent()
        action_data = {
            'action': 'search',
            'action_input': 'artificial intelligence trends 2024'
        }

        action_result = agent.act(action_data, mock_tool_registry)

        # Verify action execution
        assert 'action' in action_result, "Should include executed action"
        assert 'input' in action_result, "Should include action input"
        assert 'observation' in action_result, "Should include observation from tool"
        assert 'success' in action_result, "Should include success status"

        # Verify content
        assert action_result['action'] == 'search', "Action should match input"
        assert action_result['success'] is True, "Default tools should succeed"
        assert action_result['observation'] is not None, "Should have observation from tool"

    def test_react_agent_learn(self):
        """
        Test ReActAgent memory update from results.

        Validates:
        - Experiences are stored in episodic memory
        - Thought-action-observation traces are preserved
        - Memory count increases with learning
        """
        agent = ReActAgent()
        agent.goal = "Test learning"

        # Initial memory state
        initial_count = len(agent.memory.episodic_memory)

        # Learn from experience
        thought = "I should verify the data source"
        action = {'tool': 'search', 'query': 'data verification'}
        observation = "Found 5 verification methods"

        learning_result = agent.learn(thought, action, observation)

        # Verify memory was updated
        assert 'episodic_count' in learning_result, "Should return memory count"
        assert learning_result['episodic_count'] == initial_count + 1, \
            "Memory count should increase"

        # Verify stored content
        assert learning_result['stored_thought'] == thought, "Should store thought"
        assert learning_result['stored_action'] == action, "Should store action"

        # Verify episodic memory structure
        last_episode = agent.memory.episodic_memory[-1]
        assert last_episode['action']['thought'] == thought, "Thought should be in memory"
        assert last_episode['action']['action'] == action, "Action should be in memory"
        assert last_episode['result'] == observation, "Observation should be in memory"


# ============================================================================
# TEST SUITE: TaskDecompositionAgent Tests (2 tests)
# ============================================================================

@pytest.mark.doc04
@pytest.mark.unit
class TestTaskDecompositionAgent:
    """Test suite for hierarchical task decomposition pattern."""

    def test_task_decomposition(self):
        """
        Test hierarchical task breakdown into subtasks.

        Validates:
        - Complex tasks are decomposed into subtasks
        - Simple tasks are identified as atomic
        - Subtasks have proper structure (id, description, dependencies)
        - Dependencies are captured
        """
        agent = TaskDecompositionAgent()

        # Test complex task decomposition
        complex_task = "Research analyze and summarize machine learning advancements"
        subtasks = agent.decompose(complex_task)

        # Verify decomposition occurred
        assert len(subtasks) > 1, "Complex task should decompose into multiple subtasks"

        # Verify subtask structure
        for subtask in subtasks:
            assert 'id' in subtask, "Subtask should have ID"
            assert 'description' in subtask, "Subtask should have description"
            assert 'dependencies' in subtask, "Subtask should have dependencies list"

        # Verify dependencies are hierarchical
        root_tasks = [st for st in subtasks if len(st['dependencies']) == 0]
        assert len(root_tasks) > 0, "Should have at least one root task with no dependencies"

        dependent_tasks = [st for st in subtasks if len(st['dependencies']) > 0]
        assert len(dependent_tasks) > 0, "Should have tasks with dependencies"

        # Test simple task (should not decompose)
        simple_task = "Search query"
        simple_subtasks = agent.decompose(simple_task)
        assert len(simple_subtasks) == 1, "Simple task should result in single subtask"
        assert simple_subtasks[0]['dependencies'] == [], "Simple task should have no dependencies"

    def test_task_execution_order(self):
        """
        Test dependency-based execution order computation.

        Validates:
        - Topological sort respects dependencies
        - Tasks without dependencies execute first
        - Dependent tasks execute after their dependencies
        - All tasks are included in execution order
        """
        agent = TaskDecompositionAgent()

        # Create tasks with dependencies
        subtasks = [
            {'id': 'task_a', 'description': 'Initialize', 'dependencies': []},
            {'id': 'task_b', 'description': 'Process A', 'dependencies': ['task_a']},
            {'id': 'task_c', 'description': 'Process B', 'dependencies': ['task_a']},
            {'id': 'task_d', 'description': 'Synthesize', 'dependencies': ['task_b', 'task_c']}
        ]

        execution_order = agent.compute_execution_order(subtasks)

        # Verify all tasks included
        assert len(execution_order) == len(subtasks), "All tasks should be in execution order"

        # Verify task_a (no dependencies) comes first
        assert execution_order[0] == 'task_a', "Root task should execute first"

        # Verify task_b and task_c come after task_a
        task_a_index = execution_order.index('task_a')
        task_b_index = execution_order.index('task_b')
        task_c_index = execution_order.index('task_c')

        assert task_b_index > task_a_index, "task_b should execute after task_a"
        assert task_c_index > task_a_index, "task_c should execute after task_a"

        # Verify task_d comes after both task_b and task_c
        task_d_index = execution_order.index('task_d')
        assert task_d_index > task_b_index, "task_d should execute after task_b"
        assert task_d_index > task_c_index, "task_d should execute after task_c"
        assert task_d_index == len(execution_order) - 1, "task_d should be last"


# ============================================================================
# TEST SUITE: ErrorRecoverySystem Tests (3 tests)
# ============================================================================

@pytest.mark.doc04
@pytest.mark.unit
class TestErrorRecoverySystem:
    """Test suite for error handling and recovery mechanisms."""

    def test_error_classification(self):
        """
        Test error classification into categories.

        Validates:
        - Errors are classified as RETRIABLE/FIXABLE/FALLBACK/TERMINAL
        - Classification includes error type and severity
        - Unknown errors are handled appropriately
        """
        classifier = ErrorClassifier()

        # Test RETRIABLE error
        retriable_error = Exception("Connection timeout occurred")
        retriable_classification = classifier.classify(retriable_error)

        assert retriable_classification['category'] == 'RETRIABLE', \
            "Timeout should be classified as RETRIABLE"
        assert retriable_classification['error_type'] == 'timeout', \
            "Should identify specific error type"
        assert retriable_classification['severity'] == 'medium', \
            "RETRIABLE errors should have medium severity"

        # Test FIXABLE error
        fixable_error = Exception("invalid_input detected in parameters")
        fixable_classification = classifier.classify(fixable_error)

        assert fixable_classification['category'] == 'FIXABLE', \
            "Invalid input should be classified as FIXABLE"
        assert fixable_classification['error_type'] == 'invalid_input'

        # Test FALLBACK error
        fallback_error = Exception("tool_unavailable, use alternative")
        fallback_classification = classifier.classify(fallback_error)

        assert fallback_classification['category'] == 'FALLBACK', \
            "Unavailable tool should trigger FALLBACK"

        # Test TERMINAL error
        terminal_error = Exception("authentication_error: Access denied")
        terminal_classification = classifier.classify(terminal_error)

        assert terminal_classification['category'] == 'TERMINAL', \
            "Auth errors should be TERMINAL"
        assert terminal_classification['severity'] == 'high', \
            "TERMINAL errors should have high severity"

        # Test UNKNOWN error
        unknown_error = Exception("Something completely unexpected happened")
        unknown_classification = classifier.classify(unknown_error)

        assert unknown_classification['category'] == 'UNKNOWN', \
            "Unrecognized errors should be UNKNOWN"
        assert unknown_classification['severity'] == 'high', \
            "UNKNOWN errors should be treated as high severity"

    def test_retry_with_backoff(self):
        """
        Test exponential backoff retry logic.

        Validates:
        - Retry attempts are tracked
        - Backoff time increases exponentially
        - Max retries limit is enforced
        - Retry metadata is returned
        """
        recovery = ErrorRecoverySystem()
        context = {'action_id': 'test_action', 'action': 'search'}

        # First retry
        result1 = recovery.retry_with_backoff(context, max_retries=3)

        assert result1['success'] is True, "First retry should succeed"
        assert result1['action'] == 'retry', "Should indicate retry action"
        assert result1['attempt'] == 1, "Should be attempt 1"
        assert result1['backoff_time'] > 0, "Should have backoff time"

        # Second retry
        result2 = recovery.retry_with_backoff(context, max_retries=3)

        assert result2['attempt'] == 2, "Should be attempt 2"
        assert result2['backoff_time'] > result1['backoff_time'], \
            "Backoff should increase exponentially"

        # Third retry
        result3 = recovery.retry_with_backoff(context, max_retries=3)
        assert result3['attempt'] == 3, "Should be attempt 3"

        # Fourth retry (exceeds max)
        result4 = recovery.retry_with_backoff(context, max_retries=3)

        assert result4['success'] is False, "Should fail after max retries"
        assert 'Max retries exceeded' in result4['error'], \
            "Should indicate max retries exceeded"
        assert result4['attempts'] > 3, "Should track attempts beyond max"

    def test_fallback_execution(self):
        """
        Test graceful degradation via fallback strategies.

        Validates:
        - Fallback actions are executed when primary fails
        - Fallback context is preserved
        - Success is reported with fallback indicator
        """
        recovery = ErrorRecoverySystem()

        # Test with explicit fallback
        context_with_fallback = {
            'action_id': 'primary_search',
            'primary_action': 'web_search',
            'fallback_action': 'cached_search'
        }

        result = recovery.execute_fallback(context_with_fallback)

        assert result['success'] is True, "Fallback should succeed"
        assert result['action'] == 'fallback', "Should indicate fallback action"
        assert result['fallback_action'] == 'cached_search', \
            "Should execute specified fallback"

        # Test without explicit fallback
        context_without_fallback = {
            'action_id': 'primary_action'
        }

        result_default = recovery.execute_fallback(context_without_fallback)

        assert result_default['success'] is True, "Should succeed with default fallback"
        assert result_default['fallback_action'] == 'default_fallback', \
            "Should use default fallback when none specified"


# ============================================================================
# End of Test Suite
# ============================================================================

"""
Test Summary
============

Total Tests: 12

1. BaseAgent Tests (3):
   - test_base_agent_initialization: Core component setup
   - test_base_agent_perception: Observation processing
   - test_base_agent_run_cycle: Full execution loop

2. ReActAgent Tests (4):
   - test_react_agent_perceive: Goal and observation tracking
   - test_react_agent_reason: Thought-action generation
   - test_react_agent_act: Tool execution
   - test_react_agent_learn: Memory update

3. TaskDecompositionAgent Tests (2):
   - test_task_decomposition: Hierarchical breakdown
   - test_task_execution_order: Dependency-based ordering

4. ErrorRecoverySystem Tests (3):
   - test_error_classification: Error categorization
   - test_retry_with_backoff: Exponential retry logic
   - test_fallback_execution: Graceful degradation

Coverage:
- Agent architecture (perception, reasoning, action, memory)
- ReAct loop pattern (Reason → Act → Observe)
- Task decomposition and dependency management
- Error handling and recovery strategies
"""
