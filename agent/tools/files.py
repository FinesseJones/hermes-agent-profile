"""agent/tools/files.py — Local filesystem read/write/list."""

import os
from pathlib import Path


def _expand(path: str) -> str:
    return os.path.expanduser(path)


def read_file(path: str, lines: int = None) -> str:
    p = _expand(path)
    try:
        with open(p, "r", encoding="utf-8", errors="replace") as f:
            if lines:
                content = "".join(f.readline() for _ in range(lines))
            else:
                content = f.read()
        size = os.path.getsize(p)
        return f"[FILE: {p} | {size} bytes]\n{content}"
    except FileNotFoundError:
        return f"[ERROR] File not found: {p}"
    except Exception as e:
        return f"[ERROR] read_file: {e}"


def write_file(path: str, content: str) -> str:
    p = _expand(path)
    try:
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            f.write(content)
        return f"[OK] Written {len(content)} chars to {p}"
    except Exception as e:
        return f"[ERROR] write_file: {e}"


def append_file(path: str, content: str) -> str:
    p = _expand(path)
    try:
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "a", encoding="utf-8") as f:
            f.write(content)
        return f"[OK] Appended {len(content)} chars to {p}"
    except Exception as e:
        return f"[ERROR] append_file: {e}"


def list_dir(path: str, recursive: bool = False) -> str:
    p = _expand(path)
    try:
        if recursive:
            lines = []
            for root, dirs, files in os.walk(p):
                # Skip hidden and cache dirs
                dirs[:] = [d for d in dirs if not d.startswith(".") and d not in ("__pycache__", "node_modules")]
                rel = os.path.relpath(root, p)
                for f in files:
                    lines.append(os.path.join(rel, f) if rel != "." else f)
            return "\n".join(lines[:500]) or "[empty]"
        else:
            entries = os.listdir(p)
            result = []
            for e in sorted(entries):
                full = os.path.join(p, e)
                tag = "[D]" if os.path.isdir(full) else "[F]"
                result.append(f"{tag} {e}")
            return "\n".join(result) or "[empty]"
    except Exception as e:
        return f"[ERROR] list_dir: {e}"
