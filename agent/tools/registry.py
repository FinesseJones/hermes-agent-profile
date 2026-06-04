"""
registry.py — Master tool registry for Hermes Agent.
Every @tool() decorated function is auto-registered and sent to the model.
"""
import inspect
import json
import os
import subprocess
import shutil
import socket
import urllib.request
import urllib.error
from pathlib import Path
from agent.config import (
    WORKSPACE, HERMES_RUNTIME, VPS_HOST, VPS_USER, VPS_PORT,
    DEPLOY_SCRIPT, SKILLS_DIR, HERMES_SKILLS, REQUIRE_APPROVAL,
)
from agent.memory.store import remember as _remember, recall as _recall

_REGISTRY: dict = {}


def tool(name: str = None, description: str = ""):
    def decorator(fn):
        tname = name or fn.__name__
        sig = inspect.signature(fn)
        props = {}
        required = []
        for pname, param in sig.parameters.items():
            ann = param.annotation
            if ann == inspect.Parameter.empty:
                ann = str
            ptype = {str: "string", int: "integer", bool: "boolean", list: "array"}.get(ann, "string")
            props[pname] = {"type": ptype, "description": pname.replace("_", " ")}
            if param.default == inspect.Parameter.empty:
                required.append(pname)
        _REGISTRY[tname] = {
            "fn": fn,
            "schema": {
                "name": tname,
                "description": description or fn.__doc__ or "",
                "parameters": {"type": "object", "properties": props, "required": required},
            }
        }
        return fn
    return decorator


def get_all_schemas() -> list:
    return [v["schema"] for v in _REGISTRY.values()]


def execute_tool(name: str, args: dict) -> str:
    if name not in _REGISTRY:
        return f"ERROR: unknown tool '{name}'. Available: {list(_REGISTRY.keys())}"
    try:
        result = _REGISTRY[name]["fn"](**args)
        return str(result) if result is not None else "done"
    except Exception as e:
        return f"ERROR in {name}: {type(e).__name__}: {e}"


# ── FILE TOOLS ────────────────────────────────────────────────────────────────

@tool(description="Read a file. Path is absolute or relative to ~/hermesd-dev.")
def read_file(path: str) -> str:
    p = Path(path) if Path(path).is_absolute() else WORKSPACE / path
    if not p.exists():
        return f"Not found: {p}"
    return p.read_text(errors="replace")[:8000]


@tool(description="Write content to a file, creating parent dirs as needed.")
def write_file(path: str, content: str) -> str:
    p = Path(path) if Path(path).is_absolute() else WORKSPACE / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content)
    return f"Written {len(content)} chars to {p}"


@tool(description="Append text to a file. Creates it if it does not exist.")
def append_file(path: str, content: str) -> str:
    p = Path(path) if Path(path).is_absolute() else WORKSPACE / path
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "a") as f:
        f.write(content)
    return f"Appended to {p}"


@tool(description="List files and subdirectories at a path (2 levels deep).")
def list_dir(path: str = ".") -> str:
    p = Path(path) if Path(path).is_absolute() else WORKSPACE / path
    if not p.exists():
        return f"Not found: {p}"
    lines = []
    for item in sorted(p.iterdir()):
        lines.append(f"{'[D]' if item.is_dir() else '[F]'} {item.name}")
        if item.is_dir():
            try:
                for sub in sorted(item.iterdir())[:8]:
                    lines.append(f"    {'[D]' if sub.is_dir() else '[F]'} {sub.name}")
            except PermissionError:
                pass
    return "\n".join(lines) if lines else "Empty"


@tool(description="Search for files matching a glob pattern under a directory.")
def find_files(path: str, pattern: str) -> str:
    p = Path(path) if Path(path).is_absolute() else WORKSPACE / path
    hits = list(p.glob(pattern))[:50]
    return "\n".join(str(h) for h in hits) if hits else f"No matches for {pattern}"


@tool(description="Delete a file or directory. Moves to Trash rather than hard delete.")
def delete_file(path: str) -> str:
    p = Path(path) if Path(path).is_absolute() else WORKSPACE / path
    if not p.exists():
        return f"Not found: {p}"
    trash = Path.home() / ".Trash" / p.name
    try:
        shutil.move(str(p), str(trash))
        return f"Moved to Trash: {p}"
    except Exception:
        shutil.rmtree(p) if p.is_dir() else p.unlink()
        return f"Deleted: {p}"


# ── SHELL ─────────────────────────────────────────────────────────────────────

_BLOCKLIST = {"rm -rf /", "mkfs", ":(){:|:&};:"}

@tool(description="Run a shell command in the workspace directory. 60s timeout.")
def exec_command(cmd: str, cwd: str = None) -> str:
    for blocked in _BLOCKLIST:
        if blocked in cmd:
            return f"BLOCKED: {blocked}"
    work = Path(cwd) if cwd else WORKSPACE
    try:
        r = subprocess.run(cmd, shell=True, text=True, capture_output=True,
                           timeout=60, cwd=str(work))
        out = r.stdout.strip()
        err = r.stderr.strip()
        return "\n".join(filter(None, [out, f"STDERR: {err}" if err else ""]))[:4000] or f"exit {r.returncode}"
    except subprocess.TimeoutExpired:
        return "TIMEOUT after 60s"
    except Exception as e:
        return f"ERROR: {e}"


# ── GIT ───────────────────────────────────────────────────────────────────────

@tool(description="Get git status and last 5 commits.")
def git_status() -> str:
    return exec_command("git status --short && git log --oneline -5")

@tool(description="Stage all changes and commit with a message.")
def git_commit(message: str) -> str:
    return exec_command(f'git add -A && git commit -m "{message}"')

@tool(description="Push committed changes to GitHub.")
def git_push() -> str:
    return exec_command("git push origin main")

@tool(description="Pull latest from GitHub.")
def git_pull() -> str:
    return exec_command("git pull origin main")

@tool(description="Show current diff.")
def git_diff() -> str:
    return exec_command("git diff HEAD")[:3000]


# ── VPS / SSH ─────────────────────────────────────────────────────────────────

def _ssh(remote_cmd: str, timeout: int = 30) -> str:
    cmd = ["ssh", "-o", "ConnectTimeout=10", "-o", "BatchMode=yes",
           "-o", "StrictHostKeyChecking=no",
           "-p", str(VPS_PORT), f"{VPS_USER}@{VPS_HOST}", remote_cmd]
    try:
        r = subprocess.run(cmd, text=True, capture_output=True, timeout=timeout)
        out = r.stdout.strip()
        err = r.stderr.strip()
        return "\n".join(filter(None, [out, f"STDERR: {err}" if err else ""]))[:3000]
    except subprocess.TimeoutExpired:
        return f"SSH timeout after {timeout}s"
    except Exception as e:
        return f"SSH error: {e}"

@tool(description="Run a shell command on the Hostinger VPS via SSH.")
def vps_exec(cmd: str) -> str:
    return _ssh(cmd)

@tool(description="Check Docker container health on the VPS.")
def vps_status() -> str:
    return _ssh("docker compose -f /docker/hermes-agent-ttiy/docker-compose.yml ps && "
                "docker compose -f /docker/hermes-agent-ttiy/docker-compose.yml logs --tail=10 hermes-agent")

@tool(description="Restart the Hermes Docker container on the VPS.")
def vps_restart() -> str:
    return _ssh("cd /docker/hermes-agent-ttiy && docker compose restart hermes-agent", timeout=60)

@tool(description="Deploy local ~/.hermes runtime to the Hostinger VPS. REQUIRES APPROVAL.")
def deploy_to_vps() -> str:
    if not DEPLOY_SCRIPT.exists():
        return f"Deploy script missing: {DEPLOY_SCRIPT}"
    r = subprocess.run(["bash", str(DEPLOY_SCRIPT)], text=True,
                       capture_output=True, timeout=300, cwd=str(WORKSPACE))
    return (r.stdout + r.stderr).strip()[:4000]


# ── WEB ───────────────────────────────────────────────────────────────────────

@tool(description="HTTP GET request. Returns first 4000 chars of response body.")
def http_get(url: str) -> str:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "HermesAgent/1.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.read().decode("utf-8", errors="replace")[:4000]
    except Exception as e:
        return f"Error: {e}"

@tool(description="HTTP POST with a JSON body string. Returns response body.")
def http_post(url: str, body: str) -> str:
    try:
        req = urllib.request.Request(url, data=body.encode(),
                                     headers={"Content-Type": "application/json",
                                              "User-Agent": "HermesAgent/1.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.read().decode("utf-8", errors="replace")[:4000]
    except Exception as e:
        return f"Error: {e}"


# ── MEMORY ────────────────────────────────────────────────────────────────────

@tool(description="Save a note to long-term memory. Persists across sessions.")
def memory_save(note: str) -> str:
    return _remember(note)

@tool(description="Search long-term memory for a query string.")
def memory_recall(query: str) -> str:
    return _recall(query)


# ── SKILLS ───────────────────────────────────────────────────────────────────

@tool(description="List all available Hermes skills. Optional filter string.")
def list_skills(filter: str = "") -> str:
    lines = []
    for base in [SKILLS_DIR, HERMES_SKILLS]:
        if base.exists():
            for d in sorted(base.iterdir()):
                if d.is_dir() and (not filter or filter.lower() in d.name.lower()):
                    has_md = (d / "SKILL.md").exists()
                    lines.append(f"{'✓' if has_md else '○'} {d.name}")
    return "\n".join(lines[:100]) if lines else "No skills found"

@tool(description="Read the SKILL.md for a named skill.")
def read_skill(skill_name: str) -> str:
    for base in [SKILLS_DIR, HERMES_SKILLS]:
        p = base / skill_name / "SKILL.md"
        if p.exists():
            return p.read_text()[:4000]
    return f"SKILL.md not found for '{skill_name}'"


# ── SYSTEM ────────────────────────────────────────────────────────────────────

@tool(description="List all registered tools with descriptions.")
def list_tools() -> str:
    lines = [f"  {n:35s} — {v['schema']['description'][:70]}"
             for n, v in _REGISTRY.items()]
    return "\n".join(lines)

@tool(description="Check health of llama-server (:8889) and unsloth_proxy (:8890).")
def system_status() -> str:
    results = []
    for port, name in [(8889, "llama-server"), (8890, "unsloth_proxy")]:
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=2):
                results.append(f"✅ {name} :{port}")
        except Exception:
            results.append(f"❌ {name} :{port} NOT RESPONDING")
    results.append(f"Workspace : {WORKSPACE}")
    results.append(f"VPS       : {VPS_USER}@{VPS_HOST}:{VPS_PORT}")
    return "\n".join(results)

@tool(description="Read a file from the ~/.hermes runtime directory.")
def read_hermes_file(path: str) -> str:
    p = HERMES_RUNTIME / path
    return p.read_text(errors="replace")[:6000] if p.exists() else f"Not found: {p}"

@tool(description="Write a file to the ~/.hermes runtime directory.")
def write_hermes_file(path: str, content: str) -> str:
    p = HERMES_RUNTIME / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content)
    return f"Written to {p}"

@tool(description="List files inside a named agent profile under ~/.hermes/profiles/")
def list_agent_profile(profile_name: str) -> str:
    p = HERMES_RUNTIME / "profiles" / profile_name
    if not p.exists():
        profiles = [d.name for d in (HERMES_RUNTIME / "profiles").iterdir()
                    if d.is_dir()] if (HERMES_RUNTIME / "profiles").exists() else []
        return f"Profile '{profile_name}' not found. Available: {profiles}"
    lines = []
    for item in sorted(p.iterdir()):
        lines.append(f"{'[D]' if item.is_dir() else '[F]'} {item.name}")
    return "\n".join(lines)

@tool(description="Run the Hermes deploy script to push runtime to VPS and restart container.")
def full_deploy() -> str:
    result = exec_command("bash scripts/deploy_to_hostinger.sh")
    return result

# ── Aliases expected by agent_loop.py ────────────────────────────────────────
TOOL_DEFINITIONS = get_all_schemas()
dispatch_tool = execute_tool
