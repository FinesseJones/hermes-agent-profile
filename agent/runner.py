#!/usr/bin/env python3
"""
agent/runner.py

CLI entry point for Hermes Agent.

Usage:
    python -m agent.runner "your goal here"
    python -m agent.runner "your goal here" --approve        # gate sensitive tools
    python -m agent.runner "your goal here" --run-id abc123  # named run

Examples:
    python -m agent.runner "check git status of hermesd-dev and push any changes"
    python -m agent.runner "scan the VPS for disk usage and report back"
    python -m agent.runner "read USER.md and summarize who I am" --approve
"""

import sys
import argparse
from agent.agent_loop import run_goal


def main():
    parser = argparse.ArgumentParser(
        description="Hermes Autonomous Agent — fully local, no cloud, no Codex."
    )
    parser.add_argument("goal", nargs="?", help="The goal to accomplish")
    parser.add_argument(
        "--approve", action="store_true",
        help="Require manual approval before shell/ssh/email tool calls"
    )
    parser.add_argument(
        "--run-id", default=None,
        help="Optional run ID for logging (auto-generated if omitted)"
    )
    args = parser.parse_args()

    if not args.goal:
        # Interactive mode
        print("🤖 Hermes Agent — Interactive Mode")
        print("   Type your goal and press Enter. Ctrl+C to quit.\n")
        while True:
            try:
                goal = input("Goal > ").strip()
                if not goal:
                    continue
                result = run_goal(goal, require_approval=args.approve, run_id=args.run_id)
                print(f"\n📋 RESULT: {result}\n")
            except KeyboardInterrupt:
                print("\n\nBye.")
                break
    else:
        result = run_goal(args.goal, require_approval=args.approve, run_id=args.run_id)
        print(f"\n📋 FINAL RESULT:\n{result}")
        sys.exit(0)


if __name__ == "__main__":
    main()
