"""agent/tools/shell.py — Guarded shell execution on local Mac."""

import subprocess
import os
from pathlib import Path

DEFAULT_CWD = str(Path.home() / "hermesd-dev")

# Commands that are never allowed regardless of goal
BLOCKED = ["rm -rf /", "mkfs", "dd if=/dev/zero", ":(){:|:&};:"]


def run_shell(cmd: str, cwd: str = None, timeout: int = 60) -> str:
    for blocked in BLOCKED:
        if blocked in cmd:
            return f"[BLOCKED] Command contains forbidden pattern: '{blocked}'"

    work_dir = os.path.expanduser(cwd) if cwd else DEFAULT_CWD
    if not os.path.isdir(work_dir):
        work_dir = str(Path.home())

    try:
        result = subprocess.run(
            cmd,
            shell=True,
            executable="/bin/bash",
            cwd=work_dir,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        out = result.stdout.strip()
        err = result.stderr.strip()
        parts = []
        if out:
            parts.append(out)
        if err:
            parts.append(f"[stderr] {err}")
        if result.returncode != 0:
            parts.append(f"[exit code {result.returncode}]")
        return "\n".join(parts) if parts else "[no output]"
    except subprocess.TimeoutExpired:
        return f"[TIMEOUT] Command exceeded {timeout}s: {cmd}"
    except Exception as e:
        return f"[ERROR] shell: {e}"
