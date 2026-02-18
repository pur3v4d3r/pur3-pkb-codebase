"""
Pytest Configuration and Shared Fixtures
=========================================

Configuration and fixtures for Day 13 Code Validation test suite.
"""

import pytest
from pathlib import Path
import sys

# Add mocks directory to path for imports
TESTS_DIR = Path(__file__).parent
MOCKS_DIR = TESTS_DIR / "mocks"
sys.path.insert(0, str(MOCKS_DIR))

from mock_llm import MockLLMModel, MockStreamingLLM
from mock_tools import MockToolRegistry, MockTool, FailingMockTool
from fixtures import (
    SAMPLE_GOALS,
    SAMPLE_OBSERVATIONS,
    SAMPLE_REASONING_CHAINS,
    SAMPLE_ERROR_SCENARIOS,
    SAMPLE_EXTENDED_THINKING,
    SAMPLE_CACHE_SCENARIOS,
    SAMPLE_ORCHESTRATOR_DECISIONS,
    SAMPLE_OPTIMIZER_CONFIGS,
    create_mock_agent_state,
    create_mock_workflow_state,
    create_mock_tool_result
)


# ============================================================================
# LLM Fixtures
# ============================================================================

@pytest.fixture
def mock_llm():
    """Fixture providing mock LLM model."""
    return MockLLMModel()


@pytest.fixture
def mock_streaming_llm():
    """Fixture providing mock streaming LLM model."""
    return MockStreamingLLM()


@pytest.fixture
def mock_llm_with_custom_responses():
    """Fixture providing mock LLM with custom responses."""
    return MockLLMModel(responses={
        "reasoning": "After careful analysis, the solution is...",
        "action": "execute_tool: search query='test'",
        "reflection": "The previous attempt failed due to invalid input",
        "summary": "In conclusion, the answer is 42"
    })


# ============================================================================
# Tool Fixtures
# ============================================================================

@pytest.fixture
def mock_tool_registry():
    """Fixture providing mock tool registry with default tools."""
    return MockToolRegistry()


@pytest.fixture
def mock_tool_registry_empty():
    """Fixture providing empty mock tool registry."""
    return MockToolRegistry(custom_tools={})


@pytest.fixture
def mock_failing_tool():
    """Fixture providing a tool that simulates failures."""
    return FailingMockTool("failing_tool", failure_mode="timeout")


@pytest.fixture
def mock_tool_registry_with_failures():
    """Fixture providing tool registry with both working and failing tools."""
    registry = MockToolRegistry()
    registry.tools["failing_search"] = FailingMockTool("failing_search", "timeout")
    registry.tools["invalid_calc"] = FailingMockTool("invalid_calc", "invalid_params")
    return registry


# ============================================================================
# Data Fixtures
# ============================================================================

@pytest.fixture
def sample_goals():
    """Fixture providing sample agent goals."""
    return SAMPLE_GOALS


@pytest.fixture
def sample_observations():
    """Fixture providing sample observations."""
    return SAMPLE_OBSERVATIONS


@pytest.fixture
def sample_reasoning_chains():
    """Fixture providing sample ReAct reasoning chains."""
    return SAMPLE_REASONING_CHAINS


@pytest.fixture
def sample_error_scenarios():
    """Fixture providing sample error scenarios."""
    return SAMPLE_ERROR_SCENARIOS


@pytest.fixture
def sample_extended_thinking():
    """Fixture providing sample extended thinking outputs."""
    return SAMPLE_EXTENDED_THINKING


@pytest.fixture
def sample_cache_scenarios():
    """Fixture providing sample cache scenarios."""
    return SAMPLE_CACHE_SCENARIOS


@pytest.fixture
def sample_orchestrator_decisions():
    """Fixture providing sample orchestrator decisions."""
    return SAMPLE_ORCHESTRATOR_DECISIONS


@pytest.fixture
def sample_optimizer_configs():
    """Fixture providing sample optimizer configurations."""
    return SAMPLE_OPTIMIZER_CONFIGS


# ============================================================================
# State Fixtures
# ============================================================================

@pytest.fixture
def mock_agent_state():
    """Fixture providing mock agent state."""
    return create_mock_agent_state()


@pytest.fixture
def mock_agent_state_active():
    """Fixture providing mock agent state in active status."""
    return create_mock_agent_state(status="reasoning")


@pytest.fixture
def mock_workflow_state():
    """Fixture providing mock workflow state."""
    return create_mock_workflow_state()


@pytest.fixture
def mock_tool_result_success():
    """Fixture providing successful tool result."""
    return create_mock_tool_result(success=True)


@pytest.fixture
def mock_tool_result_failure():
    """Fixture providing failed tool result."""
    return create_mock_tool_result(success=False)


# ============================================================================
# Pytest Configuration
# ============================================================================

def pytest_configure(config):
    """Configure pytest with custom markers."""
    config.addinivalue_line(
        "markers", "unit: Unit tests for individual components"
    )
    config.addinivalue_line(
        "markers", "integration: Integration tests for multi-component interactions"
    )
    config.addinivalue_line(
        "markers", "slow: Tests that take significant time to run"
    )
    config.addinivalue_line(
        "markers", "doc04: Tests for DOC-04 (Agentic Patterns)"
    )
    config.addinivalue_line(
        "markers", "doc03: Tests for DOC-03 (Advanced Reasoning)"
    )
    config.addinivalue_line(
        "markers", "doc02: Tests for DOC-02 (Extended Thinking)"
    )
    config.addinivalue_line(
        "markers", "doc01: Tests for DOC-01 (Reasoning Techniques)"
    )


def pytest_collection_modifyitems(config, items):
    """Modify test collection to add auto-markers based on filename."""
    for item in items:
        # Auto-mark tests based on filename
        if "test_doc04" in str(item.fspath):
            item.add_marker(pytest.mark.doc04)
        elif "test_doc03" in str(item.fspath):
            item.add_marker(pytest.mark.doc03)
        elif "test_doc02" in str(item.fspath):
            item.add_marker(pytest.mark.doc02)
        elif "test_doc01" in str(item.fspath):
            item.add_marker(pytest.mark.doc01)


# ============================================================================
# Cleanup Fixtures
# ============================================================================

@pytest.fixture(autouse=True)
def reset_mocks(mock_llm, mock_tool_registry):
    """Auto-reset mocks after each test."""
    yield
    # Reset LLM mock
    if hasattr(mock_llm, 'reset'):
        mock_llm.reset()
    # Reset tool registry
    if hasattr(mock_tool_registry, 'reset_all'):
        mock_tool_registry.reset_all()
