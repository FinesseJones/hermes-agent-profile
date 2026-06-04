# 🚀 Hermes Agent Profile & Developer Workspace

Welcome to your offline, local-first automation command center! This repository manages your custom agent configurations, skills, and orchestrations, syncing them directly to your remote Hostinger VPS.

---

## ⚡ TL;DR — Quick Reference (ADHD-Friendly)

```mermaid
flowchain
    Local_M4_Mac[Local M4 Mac] -->|Runs Model| llama_server[llama-server :8889]
    llama_server -->|API Translation| unsloth_proxy[unsloth_proxy :8890]
    unsloth_proxy -->|Orchestrator| Codex_CLI[Codex CLI]
    Codex_CLI -->|Git Sync| GitHub[GitHub Repo]
    Codex_CLI -->|Deploy Package| Hostinger_VPS[Hostinger VPS]
```

### 🏃‍♂️ Quick Start Commands
Run these in your terminal to start the environment:

1. **Verify Services are Running:**
   ```bash
   lsof -i :8889 -i :8890
   ```
2. **Execute Autonomous Sync & Deploy:**
   ```bash
   python3 ~/orchestrate_codex.py
   ```
3. **Verify VPS Agent Status:**
   ```bash
   ssh root@srv1726890.hstgr.cloud "docker compose -f /docker/hermes-agent-ttiy/docker-compose.yml ps"
   ```

---

## 📂 Workspace Map (Where Things Live)

### 💻 1. Local Workspace (`~/hermesd-dev`)
*Managed by this Git repository.*
* [skills/](file:///Users/finessejones1/hermesd-dev/skills/) — Your custom agent skills and tools.
* [scripts/](file:///Users/finessejones1/hermesd-dev/scripts/) — Deployment and automation scripts.
  * [deploy_to_hostinger.sh](file:///Users/finessejones1/hermesd-dev/scripts/deploy_to_hostinger.sh) — Optimized rsync packaging and deployment runner.
* [AGENTS.md](file:///Users/finessejones1/hermesd-dev/AGENTS.md) — Custom IT & Cybersecurity agent profile baseline.
* [SOUL.md](file:///Users/finessejones1/hermesd-dev/SOUL.md) — System instruction guidelines for the agent's behavior.
* [IDENTITY.md](file:///Users/finessejones1/hermesd-dev/IDENTITY.md) — Personal agent core identity settings.
* [TOOLS.md](file:///Users/finessejones1/hermesd-dev/TOOLS.md) — Manifest mapping available commands and tool boundaries.

### 💾 2. Local Live Runtime Cache (`~/.hermes`)
*The active local engine (200+ GB of data).*
* `skills/` — Active runtime skill scripts.
* `profiles/` — Agent memory databases and profile states (e.g., `jamiefirendstrategist`).
* `hermes-agent/` — Local NousResearch upstream framework installation.
* `node/` / `bin/` — Runtime binaries and node modules.

### 🌍 3. Remote VPS Environment (`srv1726890.hstgr.cloud`)
*Your live cloud instance running on Hostinger.*
* Location: `/docker/hermes-agent-ttiy/`
* Data Directory: `/docker/hermes-agent-ttiy/data/` (receives sync packages).
* Runs the `hvps-hermes-agent` Docker container on external port `32769` (mapped internally to `4860`).

---

## 📖 Next Steps: Read the Wiki
For the full technical breakdown, setup guides, troubleshooting steps, and agent architecture details, open the **[Master Wiki (WIKI.md)](file:///Users/finessejones1/hermesd-dev/WIKI.md)**.
