"""
store.py — Durable memory for Hermes Agent.
Two layers:
  1. run_log.jsonl   — every step of every run (raw audit trail)
  2. long_term.md    — curated knowledge the agent updates itself
"""
import json
import time
from datetime import datetime
from pathlib import Path
from agent.config import RUN_LOG, LONG_TERM_MEMORY


def _ensure():
    RUN_LOG.parent.mkdir(parents=True, exist_ok=True)
    if not LONG_TERM_MEMORY.exists():
        LONG_TERM_MEMORY.write_text(
            "# Hermes Long-Term Memory\n\n"
            "_Updated automatically by the agent across sessions._\n\n"
        )


def log_step(run_id: str, step: int, kind: str, data: dict):
    _ensure()
    record = {
        "ts": datetime.utcnow().isoformat(),
        "run_id": run_id,
        "step": step,
        "kind": kind,
        **data,
    }
    with open(RUN_LOG, "a") as f:
        f.write(json.dumps(record) + "\n")


def get_recent_runs(n: int = 5) -> list:
    _ensure()
    if not RUN_LOG.exists():
        return []
    runs = {}
    with open(RUN_LOG) as f:
        for line in f:
            try:
                rec = json.loads(line)
                rid = rec.get("run_id", "?")
                if rec.get("kind") == "goal":
                    runs[rid] = {"run_id": rid, "goal": rec.get("goal"), "ts": rec.get("ts")}
                if rec.get("kind") == "done" and rid in runs:
                    runs[rid]["summary"] = rec.get("summary")
            except Exception:
                pass
    return list(runs.values())[-n:]


def read_long_term() -> str:
    _ensure()
    return LONG_TERM_MEMORY.read_text()


def remember(note: str) -> str:
    _ensure()
    ts = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    with open(LONG_TERM_MEMORY, "a") as f:
        f.write(f"\n## {ts}\n{note.strip()}\n")
    return f"Saved to memory: {note[:80]}"


def recall(query: str) -> str:
    content = read_long_term()
    hits = [l for l in content.split("\n")
            if any(w.lower() in l.lower() for w in query.split())]
    return "\n".join(hits[:20]) if hits else f"Nothing found for: {query}"
