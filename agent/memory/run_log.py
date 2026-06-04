"""
run_log.py — RunLog class for agent_loop.py
"""
import json
import uuid
from datetime import datetime
from agent.config import RUN_LOG, MEMORY_DIR

class RunLog:
    def __init__(self, run_id=None, goal=None):
        self.run_id = run_id or uuid.uuid4().hex[:12]
        self.goal = goal or ""
        MEMORY_DIR.mkdir(parents=True, exist_ok=True)

    def _write(self, entry: dict):
        entry["ts"] = datetime.utcnow().isoformat()
        entry["run_id"] = self.run_id
        with open(RUN_LOG, "a") as f:
            f.write(json.dumps(entry) + "\n")

    def log_step(self, step: int, event: str, data=None):
        self._write({"step": step, "event": event, "data": data or {}})

    def log_finish(self, summary: str, success: bool):
        self._write({"event": "finish", "success": success, "summary": summary[:500]})

    def summary(self) -> str:
        return f"Run {self.run_id} logged to {RUN_LOG}"
