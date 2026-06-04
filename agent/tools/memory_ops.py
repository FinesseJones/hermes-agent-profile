"""agent/tools/memory_ops.py — Persistent key-value memory backed by a JSON file."""

import json
import os
from pathlib import Path

MEMORY_FILE = str(Path.home() / "hermesd-dev" / "agent" / "memory" / "store.json")


def _load() -> dict:
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def _save(data: dict) -> None:
    os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def remember(key: str, value: str) -> str:
    data = _load()
    data[key] = value
    _save(data)
    return f"[OK] Remembered '{key}'"


def recall(key: str = None) -> str:
    data = _load()
    if not data:
        return "[MEMORY EMPTY]"
    if key:
        val = data.get(key)
        return f"{key}: {val}" if val is not None else f"[NOT FOUND] key='{key}'"
    lines = [f"{k}: {v}" for k, v in data.items()]
    return "\n".join(lines)
