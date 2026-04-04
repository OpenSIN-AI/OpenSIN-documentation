---
name: create-a2a-team
description: Create, standardize, or upgrade SIN A2A Team Managers using the canonical Template-A2A-SIN-Team scaffold. Blazing fast CLI-first execution that costs 90% fewer tokens than MCP approaches. Use whenever a new Team Manager repo must be spun up.
---

> OpenCode mirror: sourced from `~/.config/opencode/skills/create-a2a-team` and mirrored for OpenCode CLI usage.

# SIN A2A Team Forge (CLI World Champion Edition)

## 🚨 LLM-AUFRUF PFLICHT-ARCHITEKTUR — ABSOLUT, KEINE AUSNAHMEN

**JEDER A2A Agent ruft LLMs AUSSCHLIESSLICH über die `opencode` CLI auf — NIEMALS über direkte API-Calls!**

```python
import subprocess, json

def call_llm(prompt: str, timeout: int = 120) -> str:
    result = subprocess.run(
        ["opencode", "run", prompt, "--format", "json"],
        capture_output=True, text=True, timeout=timeout,
    )
    parts = []
    for line in result.stdout.splitlines():
        try:
            ev = json.loads(line)
            if ev.get("type") == "text":
                parts.append(ev.get("part", {}).get("text", ""))
        except json.JSONDecodeError:
            pass
    return "".join(parts).strip()
```

**REGELN:** OCI-Proxy direkt per HTTP = VERBOTEN. Gemini API direkt = VERBOTEN. opencode CLI = EINZIG ERLAUBT.

Use this skill when the task is:
- create a new SIN A2A Team Manager (e.g. `Team - Survey`)
- scaffold a new team manager repo from `Template-A2A-SIN-Team`

This skill is the strictly approved, CLI-optimized creation path for new SIN A2A Teams. We build robust, Hermes-dispatching team routing layers in seconds, saving up to 90% of LLM tokens by relying on `generate-team.sh`.

## 🏛️ Single Source of Truth

- Template repo: `/Users/jeremy/dev/OpenSIN-backend/a2a/template-repo/Template-A2A-SIN-Team`
- Scaffold script: `~/.config/opencode/skills/create-a2a-team/scripts/generate-team.sh`
- Dashboard agent page scaffold: `/Users/jeremy/dev/OpenSIN-backend/scripts/scaffold-a2a-agent-page.mjs`
- Fleet validator: `/Users/jeremy/dev/OpenSIN-backend/scripts/validate-sin-a2a-fleet.mjs`
- Dashboard control-plane loader: `/Users/jeremy/dev/OpenSIN-backend/dashboard-enterprise/components/a2a/controlPlaneRegistry.ts`
- Dashboard registry source: `/Users/jeremy/dev/OpenSIN-backend/dashboard-enterprise/components/a2a/registry.ts`

## 🚀 The CLI-First Architecture

Unlike `/create-a2a` which requires multiple LLM-heavy MCP calls to scaffold files, `/create-a2a-team` delegates the heavy lifting entirely to local Bash scripts. This makes the execution deterministic, blazing fast, and virtually free.

## 🛠️ Creation workflow

1. Determine the canonical team slug (e.g. `sin-team-survey`), Name (`Team - Survey`), Manager (`SIN-Team-Survey`), and Description.
2. Run the bash generator:

```bash
~/.config/opencode/skills/create-a2a-team/scripts/generate-team.sh <slug> "<Team Name>" "<Manager Name>" "<Description>"
```

*Example:*
```bash
~/.config/opencode/skills/create-a2a-team/scripts/generate-team.sh sin-team-survey "Team - Survey" "SIN-Team-Survey" "Autonomes Management und Hermes-Routing fuer Survey- und Microtask-Monetarisierung (Freecash, MTurk)."
```

3. Register the new team in the dashboard registry (`dashboard-enterprise/components/a2a/registry.ts`).
4. Ensure the new repo implements `manager.ts` logic to dispatch work using Hermes.
5. Verify that the generated workflow also created `dashboard-enterprise/app/agents/<slug>/page.tsx` via the shared page scaffold.
6. Run the fleet validator before calling the team manager complete.

## 🚨 Hard rules

- Always use `generate-team.sh`. Do not manually copy/paste files or write boilerplate through MCP tools.
- A Team Manager does NOT execute domain work directly. It delegates to Worker agents via `Hermes`.
- The new Team Repo belongs in `/Users/jeremy/dev/OpenSIN-backend/a2a/team-[name]/A2A-SIN-Team-[Name]`.
- A team manager is not publish-ready until its dashboard detail page exists and the fleet validator accepts the route.
- **Security Hardening (April 2026):** Every team manager MUST include `.githooks/pre-commit`, `.githooks/pre-push`, `.secrets.baseline`, and `governance/source-code-classification.md`.
- **Browser/GUI Capabilities (April 2026):** Team managers MUST declare if their workers need sinInChrome (browser automation) or sin-computer-use (macOS GUI) capabilities in the team spec.

## 🚀 Team Manager Capabilities (April 2026)

Every new Team Manager MUST scaffold workers with awareness of OpenSIN's full capability stack:

### Browser Automation (sinInChrome)
- Workers can access 13 browser actions via API or MCP
- Free tier: 100 requests/hour, Premium: unlimited
- Multi-browser: Chrome, Brave, Arc, Chromium, Edge, Vivaldi, Opera

### macOS GUI Automation (sin-computer-use)
- Workers can access full macOS desktop control
- Screen capture, mouse/keyboard input, app management
- Requires macOS Accessibility + Screen Recording permissions

### Security Standards
- 7-layer security hardening mandatory for all team repos
- Pre-commit/pre-push hooks with leak detection
- CI/CD security scanning via GitHub Actions
- **Security Hardening (April 2026):** Every team manager MUST include `.githooks/pre-commit`, `.githooks/pre-push`, `.secrets.baseline`, and `governance/source-code-classification.md`.
- **Browser/GUI Capabilities (April 2026):** Team managers MUST declare if their workers need sinInChrome (browser automation) or sin-computer-use (macOS GUI) capabilities in the team spec.

## 🚀 Team Manager Capabilities (April 2026)

Every new Team Manager MUST scaffold workers with awareness of OpenSIN's full capability stack:

### Browser Automation (sinInChrome)
- Workers can access 13 browser actions via API or MCP
- Free tier: 100 requests/hour, Premium: unlimited
- Multi-browser: Chrome, Brave, Arc, Chromium, Edge, Vivaldi, Opera

### macOS GUI Automation (sin-computer-use)
- Workers can access full macOS desktop control
- Screen capture, mouse/keyboard input, app management
- Requires macOS Accessibility + Screen Recording permissions

### Security Standards
- 7-layer security hardening mandatory for all team repos
- Pre-commit/pre-push hooks with leak detection
- CI/CD security scanning via GitHub Actions

## Fail-closed completion gate

- `generate-team.sh` now uses the repo-local page scaffold so the public `/agents/<slug>` route exists from day zero.
- If the team manager will be linked publicly, the dashboard registry, route file, and control-plane projection must all agree on the same slug.
- `scripts/validate-sin-a2a-fleet.mjs` must pass the new route-page gate before you mark the team manager as ready.

## Google account matrix

- Team agents that touch Google Docs/Drive must inherit the global matrix in `~/.config/opencode/google-account-matrix.json`.
- Do not guess accounts. Existing Docs -> `zukunftsorientierte.energie@gmail.com`; Admin/Workspace -> `info@zukunftsorientierte-energie.de`; server jobs only on explicitly shared surfaces -> `ki-agent@artificial-biometrics.iam.gserviceaccount.com`.
- Prefer `sin-document-forge` for new high-speed enterprise documents.

- Google Docs access must use the Google account matrix plus the `sin-google-docs` commands `ensure-access`, `ensure-patent-structure`, and `replace-patent-tabs` when relevant.
