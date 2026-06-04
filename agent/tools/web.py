"""agent/tools/web.py — HTTP GET/POST for web research and APIs."""

import json
from urllib import request as urllib_request, error as urllib_error


def http_get(url: str, headers: dict = None, timeout: int = 30) -> str:
    try:
        req = urllib_request.Request(url, headers=headers or {}, method="GET")
        req.add_header("User-Agent", "Hermes-Agent/1.0")
        with urllib_request.urlopen(req, timeout=timeout) as resp:
            body = resp.read().decode("utf-8", errors="replace")
            return body[:8000] + ("\n[TRUNCATED]" if len(body) > 8000 else "")
    except urllib_error.HTTPError as e:
        return f"[HTTP {e.code}] {e.reason}"
    except Exception as e:
        return f"[ERROR] http_get: {e}"


def http_post(url: str, body: dict, headers: dict = None, timeout: int = 30) -> str:
    try:
        data = json.dumps(body).encode("utf-8")
        h = {"Content-Type": "application/json", "User-Agent": "Hermes-Agent/1.0"}
        if headers:
            h.update(headers)
        req = urllib_request.Request(url, data=data, headers=h, method="POST")
        with urllib_request.urlopen(req, timeout=timeout) as resp:
            body_resp = resp.read().decode("utf-8", errors="replace")
            return body_resp[:8000] + ("\n[TRUNCATED]" if len(body_resp) > 8000 else "")
    except urllib_error.HTTPError as e:
        return f"[HTTP {e.code}] {e.reason}: {e.read().decode('utf-8', errors='replace')[:500]}"
    except Exception as e:
        return f"[ERROR] http_post: {e}"
