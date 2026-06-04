"""agent/tools/ssh_ops.py — Run commands on Hostinger VPS over SSH."""

import subprocess

DEFAULT_HOST = "srv1726890.hstgr.cloud"
DEFAULT_USER = "root"
DEFAULT_KEY  = "~/.ssh/id_ed25519"


def ssh_run(cmd: str, host: str = None, user: str = None, timeout: int = 60) -> str:
    h = host or DEFAULT_HOST
    u = user or DEFAULT_USER
    ssh_cmd = [
        "ssh",
        "-i", DEFAULT_KEY,
        "-o", "StrictHostKeyChecking=no",
        "-o", "ConnectTimeout=10",
        "-o", "BatchMode=yes",
        f"{u}@{h}",
        cmd,
    ]
    try:
        result = subprocess.run(
            ssh_cmd,
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
            parts.append(f"[exit {result.returncode}]")
        return "\n".join(parts) if parts else "[no output]"
    except subprocess.TimeoutExpired:
        return f"[TIMEOUT] SSH command exceeded {timeout}s"
    except Exception as e:
        return f"[ERROR] ssh_run: {e}"
