"""
Mock Tool Registry for Testing
===============================

Provides mock tool implementations for agent testing.
"""

from typing import Dict, Callable, Any, List, Optional


class MockTool:
    """Mock tool with predefined behavior."""

    def __init__(self, name: str, handler: Optional[Callable] = None):
        """
        Initialize mock tool.

        Args:
            name: Tool name
            handler: Optional custom handler function
        """
        self.name = name
        self.handler = handler or self._default_handler
        self.call_count = 0
        self.call_history: List[Dict[str, Any]] = []

    def _default_handler(self, **kwargs) -> Dict[str, Any]:
        """Default handler returns success with echo of parameters."""
        return {
            "status": "success",
            "tool": self.name,
            "parameters": kwargs,
            "result": f"Mock {self.name} executed successfully"
        }

    def execute(self, **kwargs) -> Dict[str, Any]:
        """
        Execute mock tool.

        Args:
            **kwargs: Tool parameters

        Returns:
            Tool execution result
        """
        self.call_count += 1
        self.call_history.append({
            "parameters": kwargs,
            "call_number": self.call_count
        })
        return self.handler(**kwargs)

    def __call__(self, **kwargs) -> Dict[str, Any]:
        """Allow tool to be called directly."""
        return self.execute(**kwargs)


class MockToolRegistry:
    """
    Registry of mock tools for agent testing.

    Provides common tools (search, calculate, fetch) with mock implementations.
    """

    def __init__(self, custom_tools: Optional[Dict[str, Callable]] = None):
        """
        Initialize tool registry with default and custom tools.

        Args:
            custom_tools: Dict mapping tool names to handler functions
        """
        self.tools: Dict[str, MockTool] = {}

        # Register default tools
        self._register_default_tools()

        # Register custom tools
        if custom_tools:
            for name, handler in custom_tools.items():
                self.register_tool(name, handler)

    def _register_default_tools(self):
        """Register common mock tools."""
        # Search tool
        self.register_tool("search", lambda query: {
            "status": "success",
            "results": [
                {"title": "Result 1", "snippet": "Mock search result 1"},
                {"title": "Result 2", "snippet": "Mock search result 2"}
            ],
            "query": query
        })

        # Calculate tool
        self.register_tool("calculate", lambda expression: {
            "status": "success",
            "expression": expression,
            "result": 42  # Mock result
        })

        # Fetch tool
        self.register_tool("fetch", lambda url: {
            "status": "success",
            "url": url,
            "content": "Mock fetched content"
        })

        # Database query tool
        self.register_tool("query_db", lambda query: {
            "status": "success",
            "rows": [{"id": 1, "data": "mock_data"}],
            "query": query
        })

    def register_tool(self, name: str, handler: Callable):
        """
        Register a new tool or update existing one.

        Args:
            name: Tool name
            handler: Tool handler function
        """
        self.tools[name] = MockTool(name, handler)

    def get_tool(self, name: str) -> Optional[MockTool]:
        """
        Get tool by name.

        Args:
            name: Tool name

        Returns:
            MockTool instance or None if not found
        """
        return self.tools.get(name)

    def execute_tool(self, name: str, **kwargs) -> Dict[str, Any]:
        """
        Execute tool by name.

        Args:
            name: Tool name
            **kwargs: Tool parameters

        Returns:
            Tool execution result or error dict
        """
        tool = self.get_tool(name)
        if not tool:
            return {
                "status": "error",
                "error": f"Tool '{name}' not found",
                "available_tools": list(self.tools.keys())
            }
        return tool.execute(**kwargs)

    def list_tools(self) -> List[str]:
        """List all registered tool names."""
        return list(self.tools.keys())

    def reset_all(self):
        """Reset call history for all tools."""
        for tool in self.tools.values():
            tool.call_count = 0
            tool.call_history = []


class MockToolExecutionError(Exception):
    """Exception for simulating tool execution failures."""
    pass


class FailingMockTool(MockTool):
    """Mock tool that simulates failures for error handling tests."""

    def __init__(self, name: str, failure_mode: str = "timeout"):
        """
        Initialize failing mock tool.

        Args:
            name: Tool name
            failure_mode: Type of failure (timeout, invalid_params, not_found)
        """
        super().__init__(name)
        self.failure_mode = failure_mode

    def execute(self, **kwargs) -> Dict[str, Any]:
        """Execute tool and simulate failure."""
        self.call_count += 1
        self.call_history.append({
            "parameters": kwargs,
            "call_number": self.call_count,
            "failed": True
        })

        if self.failure_mode == "timeout":
            raise TimeoutError(f"Tool '{self.name}' timed out")
        elif self.failure_mode == "invalid_params":
            raise ValueError(f"Invalid parameters for tool '{self.name}'")
        elif self.failure_mode == "not_found":
            raise MockToolExecutionError(f"Tool '{self.name}' resource not found")
        else:
            raise Exception(f"Unknown error in tool '{self.name}'")
