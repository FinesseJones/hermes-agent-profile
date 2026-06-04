"""agent/tools/git_ops.py — Git operations on hermesd-dev."""

import subprocess
from pathlib import Path

DEFAULT_REPO = str(Path.home() / "hermesd-dev")


def _git(args: list, repo: str) -> str:
    result = subprocess.run(
        ["git"] + args,
        cwd=repo,
        capture_output=True,
        text=True,
        timeout=60,
    )
    out = result.stdout.strip()
    err = result.stderr.strip()
    return (out + ("\n" + err if err else "")).strip() or "[no output]"


def git_status(repo_path: str = None) -> str:
    repo = repo_path or DEFAULT_REPO
    return _git(["status", "--short"], repo)


def git_commit_push(message: str, repo_path: str = None) -> str:
    repo = repo_path or DEFAULT_REPO
    add = _git(["add", "-A"], repo)
    diff = _git(["diff-index", "--quiet", "HEAD"], repo)
    if not diff or diff == "[no output]":
        return "[OK] Nothing to commit, working tree clean."
    commit = _git(["commit", "-m", message], repo)
    push = _git(["push", "origin", "main"], repo)
    return f"ADD: {add}\nCOMMIT: {commit}\nPUSH: {push}"
