"""
xml_tools.py — Parse XML tool calls from model output.
Handles <tools>, <function-calls>, and raw JSON blocks.
"""
import json
import re

def extract_tool_calls(content: str) -> list:
    calls = []
    # Match <tools>...</tools> or <function-calls>...</function-calls>
    pattern = r'<(?:tools|function-calls)>\s*(.*?)\s*</(?:tools|function-calls)>'
    matches = re.findall(pattern, content, re.DOTALL)
    for m in matches:
        try:
            data = json.loads(m.strip())
            calls.append({
                "id": f"call_{len(calls)}",
                "function": {
                    "name": data.get("name", ""),
                    "arguments": json.dumps(data.get("arguments", {}))
                }
            })
        except Exception:
            pass
    return calls
