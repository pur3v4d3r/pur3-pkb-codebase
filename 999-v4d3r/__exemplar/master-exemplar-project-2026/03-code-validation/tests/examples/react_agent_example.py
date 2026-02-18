#!/usr/bin/env python3
"""
Minimal Working Example: ReAct Agent
=====================================

Demonstrates Reason-Act-Observe cycle for tool-using agents.

ReAct Pattern:
1. Thought: Reason about what to do next
2. Action: Execute tool with parameters
3. Observation: Observe tool result
4. Repeat until goal achieved

Usage:
    python react_agent_example.py
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "mocks"))

from mock_llm import MockLLMModel
from mock_tools import MockToolRegistry


class ReActAgent:
    """
    ReAct agent implementing Reasoning + Acting cycle.

    Based on ReAct paper: combines reasoning traces with task-specific actions.
    """

    def __init__(self, model=None, tools=None, max_steps=5):
        """Initialize ReAct agent."""
        self.model = model or MockLLMModel()
        self.tools = tools or MockToolRegistry()
        self.max_steps = max_steps
        self.current_goal = None
        self.reasoning_chain = []

    def perceive(self, goal, observation=None):
        """Process goal and optional observation."""
        self.current_goal = goal
        if observation:
            self.reasoning_chain.append({
                "type": "observation",
                "content": observation
            })
            print(f"[OBSERVE] {observation}")

    def reason(self):
        """Generate next thought and action."""
        # Create reasoning prompt
        prompt = f"Goal: {self.current_goal}\n"
        prompt += "Previous steps:\n"
        for step in self.reasoning_chain[-3:]:  # Last 3 steps for context
            prompt += f"  - {step['type']}: {step.get('content', '')}\n"
        prompt += "\nWhat should I do next?"

        # Generate thought
        thought = self.model.generate(prompt)

        # Extract action (simplified - real implementation would parse LLM output)
        action = "search"
        action_input = self.current_goal

        self.reasoning_chain.append({
            "type": "thought",
            "content": thought
        })

        print(f"[THINK] {thought}")
        print(f"[PLAN] Action: {action}({action_input})")

        return action, action_input

    def act(self, action, action_input):
        """Execute action using tools."""
        result = self.tools.execute_tool(action, query=action_input)

        self.reasoning_chain.append({
            "type": "action",
            "action": action,
            "input": action_input,
            "result": result
        })

        print(f"[ACT] Executed {action} → Status: {result['status']}")

        return result

    def is_goal_achieved(self, result):
        """Check if goal is achieved (simplified heuristic)."""
        return result.get('status') == 'success'

    def learn(self):
        """Update episodic memory from reasoning chain."""
        episode = {
            "goal": self.current_goal,
            "steps": len(self.reasoning_chain),
            "reasoning_chain": self.reasoning_chain.copy()
        }
        print(f"[LEARN] Stored episode with {episode['steps']} steps")
        return episode

    def run(self, goal):
        """Execute ReAct cycle until goal achieved or max steps reached."""
        print(f"\n{'='*60}")
        print(f"ReAct Agent Execution")
        print(f"{'='*60}")
        print(f"Goal: {goal}")
        print(f"Max Steps: {self.max_steps}\n")

        # Initial perception
        self.perceive(goal)

        # ReAct loop
        for step in range(self.max_steps):
            print(f"\n--- Step {step + 1}/{self.max_steps} ---")

            # 1. Reason: Generate thought and action
            action, action_input = self.reason()

            # 2. Act: Execute action
            result = self.act(action, action_input)

            # 3. Observe: Process result
            observation = f"Tool returned: {result.get('result', 'No result')}"
            self.perceive(goal, observation)

            # Check if goal achieved
            if self.is_goal_achieved(result):
                print(f"\n[SUCCESS] Goal achieved in {step + 1} steps!")
                break

        # Learn from episode
        episode = self.learn()

        print(f"\n{'='*60}")
        print(f"ReAct Cycle Complete!")
        print(f"Total steps: {len(self.reasoning_chain)}")
        print(f"Actions taken: {sum(1 for s in self.reasoning_chain if s['type'] == 'action')}")
        print(f"{'='*60}\n")

        return {
            'status': 'completed',
            'goal': goal,
            'steps': len(self.reasoning_chain),
            'episode': episode
        }


def main():
    """Run ReAct agent example."""
    print("\n" + "="*60)
    print("Minimal Working Example: ReAct Agent")
    print("="*60 + "\n")

    # Create agent
    print("[INIT] Creating ReAct agent...")
    agent = ReActAgent(max_steps=3)
    print("[INIT] Agent ready with max 3 reasoning steps\n")

    # Execute agent
    result = agent.run("Search for Python testing frameworks and select the best one")

    # Show final result
    print("\n[RESULT] ReAct execution completed:")
    print(f"  Status: {result['status']}")
    print(f"  Goal: {result['goal']}")
    print(f"  Total steps: {result['steps']}")
    print(f"  Episode stored: Yes")

    # Show reasoning chain summary
    print("\n[CHAIN] Reasoning Chain Summary:")
    for i, step in enumerate(result['episode']['reasoning_chain']):
        print(f"  {i+1}. {step['type'].upper()}: {step.get('content', step.get('action', ''))[:50]}...")

    print("\n" + "="*60)
    print("Example Complete! ✅")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
