"""
config.py — Central configuration for Hermes Agent.
All paths, ports, and identities pinned to the live environment.
"""
import os
from pathlib import Path

HOME = Path.home()

# ── Model / Proxy ─────────────────────────────────────────────────────────────
PROXY_BASE_URL   = "http://localhost:8890/v1"
LLAMA_SERVER_URL = "http://localhost:8889"
MODEL_NAME       = "qwen2.5-coder:7b"
PROXY_API_KEY    = "local_privacy_shield"

# ── Agent behaviour ───────────────────────────────────────────────────────────
MAX_STEPS        = 50
STEP_DELAY_SEC   = 0.3
REQUEST_TIMEOUT  = 120
REQUIRE_APPROVAL = {
    "send_email",
    "post_to_discord",
    "post_tweet",
    "deploy_to_vps",
}

# ── Paths ─────────────────────────────────────────────────────────────────────
WORKSPACE        = HOME / "hermesd-dev"
HERMES_RUNTIME   = HOME / ".hermes"
AGENT_DIR        = WORKSPACE / "agent"
MEMORY_DIR       = AGENT_DIR / "memory"
RUN_LOG          = MEMORY_DIR / "run_log.jsonl"
LONG_TERM_MEMORY = MEMORY_DIR / "long_term.md"

# VPS
VPS_HOST         = "srv1726890.hstgr.cloud"
VPS_USER         = "root"
VPS_PORT         = 22
VPS_DEPLOY_DIR   = "/docker/hermes-agent-ttiy/data"
DEPLOY_SCRIPT    = WORKSPACE / "scripts" / "deploy_to_hostinger.sh"

# Git
GIT_REMOTE       = "git@github.com:FinesseJones/hermes-agent-profile.git"

# Skills
SKILLS_DIR       = WORKSPACE / "skills" / "consolidated"
HERMES_SKILLS    = HERMES_RUNTIME / "skills" / "consolidated"

# ── System prompt ─────────────────────────────────────────────────────────────
SYSTEM_PROMPT = """You are Hermes — a fully autonomous AI agent running on a local M4 Mac.

You are NOT a chatbot. You are an agent. Every response must either:
  1. Call a tool to make progress toward the goal, OR
  2. Return {"done": true, "summary": "..."} when the goal is fully complete.

Never explain what you are about to do without immediately doing it.
Never ask the user for clarification mid-task — make a reasonable decision and proceed.
Never output filler, preamble, or apologies.

You have access to a rich tool library. Use the right tool for each step.
After each tool result, reflect briefly (one sentence) then immediately call the next tool or finish.

When the goal is complete your final response must be plain JSON:
{"done": true, "summary": "what you accomplished"}
"""
