"""
Test Data Fixtures
==================

Common test data and fixture objects for Day 13 testing.
"""

from typing import Dict, List, Any


# Sample agent goals for testing
SAMPLE_GOALS = {
    "simple": "Complete a simple task",
    "complex": "Analyze the problem, break it into subtasks, execute each subtask, and synthesize results",
    "search": "Search for information about Python testing best practices",
    "calculation": "Calculate the sum of numbers from 1 to 100"
}

# Sample observations for perception testing
SAMPLE_OBSERVATIONS = {
    "user_input": {
        "type": "user_input",
        "content": "What is the capital of France?",
        "timestamp": "2026-02-18T10:00:00Z"
    },
    "tool_result": {
        "type": "tool_result",
        "tool": "search",
        "result": {"results": ["Paris is the capital of France"]},
        "timestamp": "2026-02-18T10:00:01Z"
    },
    "error": {
        "type": "error",
        "error_type": "TimeoutError",
        "message": "Tool execution timed out",
        "timestamp": "2026-02-18T10:00:02Z"
    }
}

# Sample reasoning chains for ReAct testing
SAMPLE_REASONING_CHAINS = [
    {
        "thought": "I need to search for information",
        "action": "search",
        "action_input": "Python testing",
        "observation": "pytest is a popular testing framework"
    },
    {
        "thought": "Based on search results, I should calculate",
        "action": "calculate",
        "action_input": "2 + 2",
        "observation": "4"
    },
    {
        "thought": "I have enough information to answer",
        "action": "finish",
        "action_input": "The answer is 4",
        "observation": "Task completed"
    }
]

# Sample task decomposition for hierarchical agents
SAMPLE_TASK_DECOMPOSITION = {
    "goal": "Build a web application",
    "subtasks": [
        {"id": 1, "task": "Design database schema", "dependencies": []},
        {"id": 2, "task": "Implement backend API", "dependencies": [1]},
        {"id": 3, "task": "Create frontend UI", "dependencies": []},
        {"id": 4, "task": "Integrate frontend with backend", "dependencies": [2, 3]}
    ]
}

# Sample error scenarios for error recovery testing
SAMPLE_ERROR_SCENARIOS = {
    "retriable": {
        "error_type": "TimeoutError",
        "category": "retriable",
        "max_retries": 3,
        "expected_recovery": "retry_with_backoff"
    },
    "fixable": {
        "error_type": "ValueError",
        "category": "fixable",
        "message": "Invalid parameter format",
        "expected_recovery": "fix_and_retry"
    },
    "fallback": {
        "error_type": "NotImplementedError",
        "category": "fallback",
        "message": "Primary method not implemented",
        "expected_recovery": "execute_fallback"
    },
    "terminal": {
        "error_type": "RuntimeError",
        "category": "terminal",
        "message": "Unrecoverable error",
        "expected_recovery": "escalate"
    }
}

# Sample extended thinking outputs
SAMPLE_EXTENDED_THINKING = {
    "simple": "<thinking>Let me analyze this step by step...</thinking>",
    "complex": """
<thinking>
First, I need to understand the problem...
Then, I should consider alternative approaches...
Finally, I'll synthesize the solution...
</thinking>
    """,
    "with_budget": {
        "thinking": "<thinking>Analysis...</thinking>",
        "tokens_used": 150,
        "budget_limit": 1000
    }
}

# Sample cache scenarios
SAMPLE_CACHE_SCENARIOS = {
    "cache_hit": {
        "query": "What is 2+2?",
        "cached_response": "4",
        "hit": True
    },
    "cache_miss": {
        "query": "What is the meaning of life?",
        "cached_response": None,
        "hit": False
    },
    "cache_expired": {
        "query": "Current weather",
        "cached_response": "Expired data",
        "hit": False,
        "expired": True
    }
}

# Sample orchestrator decisions
SAMPLE_ORCHESTRATOR_DECISIONS = {
    "simple_query": {
        "query": "What is 2+2?",
        "recommended_technique": "direct",
        "confidence": 0.95
    },
    "complex_reasoning": {
        "query": "Solve this multi-step math problem...",
        "recommended_technique": "tree_of_thoughts",
        "confidence": 0.85
    },
    "search_task": {
        "query": "Find information about...",
        "recommended_technique": "react",
        "confidence": 0.90
    }
}

# Sample optimizer parameters
SAMPLE_OPTIMIZER_CONFIGS = {
    "token_optimizer": {
        "max_tokens": 1000,
        "current_usage": 500,
        "strategy": "truncate_context"
    },
    "latency_optimizer": {
        "max_latency_ms": 5000,
        "current_latency_ms": 3000,
        "strategy": "use_cache"
    },
    "cost_optimizer": {
        "max_cost": 1.00,
        "current_cost": 0.50,
        "strategy": "use_cheaper_model"
    }
}


def create_mock_agent_state(status: str = "initialized") -> Dict[str, Any]:
    """
    Create mock agent state for testing.

    Args:
        status: Agent status (initialized, perceiving, reasoning, acting, learning)

    Returns:
        Mock agent state dictionary
    """
    return {
        "status": status,
        "history": [],
        "memory": {},
        "current_goal": None,
        "actions_taken": 0,
        "observations_received": 0
    }


def create_mock_workflow_state() -> Dict[str, Any]:
    """Create mock workflow state for testing."""
    return {
        "workflow_id": "test_workflow_001",
        "status": "running",
        "completed_tasks": [],
        "pending_tasks": ["task1", "task2"],
        "agents": {"agent1": "active", "agent2": "idle"}
    }


def create_mock_tool_result(success: bool = True) -> Dict[str, Any]:
    """
    Create mock tool result for testing.

    Args:
        success: Whether tool execution succeeded

    Returns:
        Mock tool result dictionary
    """
    if success:
        return {
            "status": "success",
            "result": "Mock tool result data",
            "tool": "mock_tool",
            "execution_time_ms": 100
        }
    else:
        return {
            "status": "error",
            "error": "Mock tool error",
            "error_type": "MockExecutionError",
            "tool": "mock_tool"
        }
