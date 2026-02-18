"""
Mock LLM Model for Testing
===========================

Provides mock LLM responses for agent testing without requiring actual API calls.
"""

from typing import Dict, List, Optional, Any


class MockLLMModel:
    """
    Mock language model that returns predefined responses.

    Simulates LLM behavior for testing agent logic without API costs.
    """

    def __init__(self, responses: Optional[Dict[str, str]] = None):
        """
        Initialize mock LLM with predefined responses.

        Args:
            responses: Dict mapping response types to mock outputs
                      Default provides reasoning and action responses
        """
        self.responses = responses or {
            "reasoning": "Let's think step by step about this problem...",
            "action": "tool_name: parameter_value",
            "reflection": "The previous approach failed because...",
            "summary": "Based on the analysis, the conclusion is...",
            "thought": "<thinking>Analyzing the problem...</thinking>",
            "default": "Mock LLM response"
        }
        self.call_count = 0
        self.call_history: List[Dict[str, Any]] = []

    def generate(self, prompt: str, **kwargs) -> str:
        """
        Generate mock response based on prompt content.

        Args:
            prompt: Input prompt
            **kwargs: Additional generation parameters (ignored in mock)

        Returns:
            Mock response string based on prompt keywords
        """
        self.call_count += 1
        self.call_history.append({
            "prompt": prompt,
            "kwargs": kwargs,
            "call_number": self.call_count
        })

        # Return response based on prompt content
        prompt_lower = prompt.lower()
        if "reason" in prompt_lower or "think" in prompt_lower:
            return self.responses["reasoning"]
        elif "action" in prompt_lower or "tool" in prompt_lower:
            return self.responses["action"]
        elif "reflect" in prompt_lower or "fail" in prompt_lower:
            return self.responses["reflection"]
        elif "summary" in prompt_lower or "conclude" in prompt_lower:
            return self.responses["summary"]
        elif "<thinking>" in prompt or "extended_thinking" in kwargs:
            return self.responses["thought"]
        else:
            return self.responses["default"]

    def async_generate(self, prompt: str, **kwargs) -> str:
        """Async version of generate (returns same as sync for testing)."""
        return self.generate(prompt, **kwargs)

    def reset(self):
        """Reset call history and counters."""
        self.call_count = 0
        self.call_history = []


class MockStreamingLLM(MockLLMModel):
    """Mock LLM that simulates streaming responses."""

    def stream_generate(self, prompt: str, **kwargs):
        """
        Simulate streaming response generation.

        Yields:
            Chunks of mock response
        """
        response = self.generate(prompt, **kwargs)
        # Split response into chunks to simulate streaming
        chunk_size = max(10, len(response) // 5)
        for i in range(0, len(response), chunk_size):
            yield response[i:i+chunk_size]
