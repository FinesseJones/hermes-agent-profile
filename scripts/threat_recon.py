#!/usr/bin/env python3
import os
import sys
import json
import urllib.request
import re
from pathlib import Path

try:
    import defusedxml.ElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

# Target directories aligned to soul.md setup
SKILLS_DIR = Path("/Users/finessejones1/.gemini/antigravity/scratch/Anthropic-Cybersecurity-Skills/skills")
LOCAL_LOG = Path("~/.hermes/logs/threat_intel.json").expanduser()

# Feeds focused on AI-Agent Exploits, OWASP GenAI, and CISA/MITRE Atlas alerts
# Using official XML/RSS feed URLs to prevent XML parsing exceptions from standard HTML pages
FEEDS = [
    "https://www.cisa.gov/cybersecurity-advisories/all.xml",
    "https://www.cisa.gov/news.xml",
]

KEYWORDS = ["agentic", "llm", "prompt injection", "rce", "tool hijack", "excessive agency", "hermes"]

# Compile word-boundary regexes to prevent short terms (like 'llm') from matching substrings in 'enrollment' or 'llmnr'
KEYWORDS_PATTERNS = [re.compile(rf"\b{re.escape(kw)}\b", re.IGNORECASE) for kw in KEYWORDS]

def fetch_threats():
    detected_threats = []
    for url in FEEDS:
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
            with urllib.request.urlopen(req, timeout=10) as response:
                root = ET.fromstring(response.read())
                for item in root.findall('.//item'):
                    title = item.find('title').text if item.find('title') is not None else ""
                    desc = item.find('description').text if item.find('description') is not None else ""
                    link = item.find('link').text if item.find('link') is not None else ""
                    
                    content_lower = f"{title} {desc}".lower()
                    if any(pattern.search(content_lower) for pattern in KEYWORDS_PATTERNS):
                        detected_threats.append({"title": title, "link": link, "severity": "HIGH"})
        except Exception as e:
            # Silently ignore connection or XML parse errors for specific feeds
            continue
    return detected_threats

def check_local_skills(threats):
    # Proactively read through the cybersecurity skills to cross-reference mitigations
    if not SKILLS_DIR.exists():
        return f"ERROR: Cybersecurity repository folder not found at {SKILLS_DIR}."
    
    matched_skills = []
    # Using recursive glob **/SKILL.md as the repository stores skills inside nested directories
    for skill_file in SKILLS_DIR.glob("**/SKILL.md"):
        try:
            content = skill_file.read_text(errors='ignore').lower()
            for threat in threats:
                # Find which specific keywords triggered this threat's alert
                threat_text = f"{threat['title']} {threat.get('link', '')}".lower()
                matched_patterns = [p for p in KEYWORDS_PATTERNS if p.search(threat_text)]
                
                # Only match this skill if it contains at least one of the whole-word keywords triggering the threat
                if matched_patterns and any(pattern.search(content) for pattern in matched_patterns):
                    # skill_file.parent.name gives the folder name representing the skill (e.g. 'detecting-ai-model-prompt-injection-attacks')
                    matched_skills.append(skill_file.parent.name)
        except Exception:
            continue
    return list(set(matched_skills))

if __name__ == "__main__":
    LOCAL_LOG.parent.mkdir(parents=True, exist_ok=True)
    live_threats = fetch_threats()
    
    if live_threats:
        matches = check_local_skills(live_threats)
        report = {"status": "ALERT", "threats": live_threats, "relevant_local_skills": matches}
        
        # Save to local log
        try:
            LOCAL_LOG.write_text(json.dumps(report, indent=2))
        except Exception:
            pass
            
        print(f"CRITICAL_ALERT: Detected {len(live_threats)} potential AI Agentic/Cyber threats matching your profile.")
        print(json.dumps(report, indent=2))
        sys.exit(1) # Exit with code 1 to explicitly force the Hermes agent to wake up and process the threat
    else:
        print("SYSTEM_SECURE: No new specific Agentic AI threats found online.")
        sys.exit(0)
