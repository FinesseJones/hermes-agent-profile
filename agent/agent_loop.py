#!/usr/bin/env python3
"""
agent/agent_loop.py — Hermes core loop.
Uses XML tool calling (no OpenAI tool_choice) — matches what qwen outputs natively.
"""
import json
import time
import uuid
import traceback
from typing import Optional
from urllib import request as urllib_request, error as urllib_error

from agent.tools.registry import get_all_schemas, execute_tool
from agent.memory.run_log import RunLog
from agent.xml_tools import extract_tool_calls

PROXY_URL    = "http://localhost:8890/v1/chat/completions"
DEFAULT_MODEL = "qwen2.5-coder-14b-instruct-q4_k_m"
MAX_STEPS    = 20
TIMEOUT_SECS = 120

# Build tool list string for system prompt
def _tool_list() -> str:
    lines = []
    for s in get_all_schemas():
        props = list(s["parameters"].get("properties", {}).keys())
        lines.append(f"- {s['name']}({', '.join(props)}): {s['description'][:80]}")
    return "\n".join(lines)

SYSTEM_PROMPT = """You are Hermes, a fully autonomous AI agent on a local Mac.

To call a tool, respond ONLY with this exact format:
<tools>
{"name": "tool_name", "arguments": {"arg1": "value1"}}
</tools>

When the goal is complete, respond ONLY with:
<tools>
{"name": "finish", "arguments": {"summary": "what you did"}}
</tools>

Never explain. Never narrate. Always call a tool.

Available tools:
""" + _tool_list()


def call_llm(messages: list) -> dict:
    payload = {
        "model": DEFAULT_MODEL,
        "messages": messages,
        "temperature": 0.1,
        "max_tokens": 512,
        "stream": False,
    }
    data = json.dumps(payload).encode()
    req = urllib_request.Request(
        PROXY_URL, data=data,
        headers={"Content-Type": "application/json",
                 "Authorization": "Bearer local_privacy_shield"},
        method="POST",
    )
    with urllib_request.urlopen(req, timeout=TIMEOUT_SECS) as resp:
        return json.loads(resp.read().decode())


def run_goal(goal: str, require_approval: bool = False, run_id: Optional[str] = None) -> str:
    run_id = run_id or uuid.uuid4().hex[:12]
    log = RunLog(run_id=run_id, goal=goal)

    print(f"\n{'='*60}")
    print(f"🤖 HERMES AGENT  run_id={run_id}")
    print(f"🎯 GOAL: {goal}")
    print(f"{'='*60}\n")

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user",   "content": f"GOAL: {goal}\n\nStart immediately by calling the first tool."},
    ]

    last_tool = "none"

    for step in range(1, MAX_STEPS + 1):
        print(f"── Step {step}/{MAX_STEPS} ──────────────────────────────────")
        log.log_step(step=step, event="llm_call")

        try:
            response = call_llm(messages)
        except Exception as e:
            print(f"❌ LLM error: {e}")
            log.log_step(step=step, event="llm_error", data=str(e))
            time.sleep(2)
            continue

        msg     = response["choices"][0]["message"]
        content = (msg.get("content") or "").strip()
        messages.append({"role": "assistant", "content": content})

        if content:
            print(f"💬 {content[:400]}")

        tool_calls = extract_tool_calls(content)

        if not tool_calls:
            # nudge once then keep going
            messages.append({"role": "user",
                "content": "Call a tool now using the <tools> format. If done, call finish."})
            continue

        for tc in tool_calls:
            name = tc["function"]["name"]
            try:
                args = json.loads(tc["function"]["arguments"])
            except Exception:
                args = {}

            last_tool = name
            print(f"\n🔧 TOOL: {name}  ARGS: {json.dumps(args)[:200]}")
            log.log_step(step=step, event="tool_call", data={"tool": name, "args": args})

            if name == "finish":
                summary = args.get("summary", "Done.")
                print(f"\n✅ GOAL COMPLETE: {summary}")
                log.log_finish(summary=summary, success=True)
                return summary

            result = execute_tool(name, args)
            print(f"   RESULT: {str(result)[:300]}")
            log.log_step(step=step, event="tool_result",
                         data={"tool": name, "result": str(result)[:500]})

            messages.append({"role": "user",
                "content": f"[tool:{name} result]\n{str(result)[:1500]}\n\nContinue toward the goal or call finish if done."})

    summary = f"[STEP LIMIT] last_tool={last_tool}"
    log.log_finish(summary=summary, success=False)
    print(f"\n⚠️ {summary}")
    return summary

