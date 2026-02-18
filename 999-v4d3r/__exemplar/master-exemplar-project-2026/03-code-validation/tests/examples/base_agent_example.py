#!/usr/bin/env python3
"""
Minimal Working Example: BaseAgent
===================================

Demonstrates the basic agent architecture with perception-reasoning-action-learn cycle.

Usage:
    python base_agent_example.py
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "mocks"))

from mock_llm import MockLLMModel
from mock_tools import MockToolRegistry


class BaseAgent:
    """
    Base agent with 4-component architecture.

    Components:
    1. Perception - Process observations
    2. Reasoning - Generate plans
    3. Action - Execute actions
    4. Memory - Store experience
    """

    def __init__(self, model=None, tools=None):
        """Initialize agent with model and tools."""
        self.model = model or MockLLMModel()
        self.tools = tools or MockToolRegistry()
        self.status = 'initialized'
        self.history = []
        self.memory = {}
        self.current_goal = None

    def perceive(self, observation):
        """Process observation and update state."""
        self.status = 'perceiving'
        self.history.append({
            "type": "observation",
            "data": observation,
            "step": len(self.history)
        })
        print(f"[PERCEIVE] Received: {observation}")

    def reason(self, goal):
        """Generate reasoning about how to achieve goal."""
        self.status = 'reasoning'
        self.current_goal = goal

        # Use LLM to generate reasoning
        reasoning = self.model.generate(f"How to achieve: {goal}")
        print(f"[REASON] Generated plan: {reasoning}")

        return reasoning

    def act(self, action_plan):
        """Execute action based on reasoning."""
        self.status = 'acting'

        # Simple action: use search tool
        result = self.tools.execute_tool("search", query=action_plan)
        print(f"[ACT] Executed action, result: {result['status']}")

        return result

    def learn(self, experience):
        """Update memory from experience."""
        self.status = 'learning'

        # Store experience in memory
        self.memory[f"experience_{len(self.memory)}"] = experience
        print(f"[LEARN] Stored experience. Total memories: {len(self.memory)}")

    def run(self, goal):
        """Execute full agent cycle: perceive → reason → act → learn."""
        print(f"\n{'='*60}")
        print(f"BaseAgent Execution Cycle")
        print(f"{'='*60}")
        print(f"Goal: {goal}\n")

        # 1. Perceive goal
        self.perceive({"type": "goal", "content": goal})

        # 2. Reason about goal
        reasoning = self.reason(goal)

        # 3. Act on reasoning
        result = self.act(reasoning)

        # 4. Learn from result
        self.learn({
            "goal": goal,
            "reasoning": reasoning,
            "result": result,
            "success": result['status'] == 'success'
        })

        self.status = 'completed'

        print(f"\n{'='*60}")
        print(f"Cycle Complete!")
        print(f"Status: {self.status}")
        print(f"Total steps: {len(self.history)}")
        print(f"Memories: {len(self.memory)}")
        print(f"{'='*60}\n")

        return {
            'status': 'completed',
            'goal': goal,
            'actions_taken': 1,
            'memories_created': len(self.memory)
        }


def main():
    """Run BaseAgent example."""
    print("\n" + "="*60)
    print("Minimal Working Example: BaseAgent")
    print("="*60 + "\n")

    # Create agent
    print("[INIT] Creating BaseAgent with mock LLM and tools...")
    agent = BaseAgent()
    print(f"[INIT] Agent status: {agent.status}\n")

    # Execute agent cycle
    result = agent.run("Find information about Python testing best practices")

    # Show final result
    print("\n[RESULT] Agent execution completed:")
    for key, value in result.items():
        print(f"  {key}: {value}")

    print("\n" + "="*60)
    print("Example Complete! ✅")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
