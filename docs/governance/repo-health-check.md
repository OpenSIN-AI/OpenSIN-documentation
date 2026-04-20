# Repo Health Check — Governance Documentation

**Issue:** [#98](https://github.com/OpenSIN-AI/OpenSIN-documentation/issues/98)
**Status:** Active
**Owner:** SIN-Zeus (control-plane)

---

## Overview

The **Repo Health Check** is a GitHub Action that automatically scans repositories in the OpenSIN-AI organization for compliance with project standards. It ensures every repo meets the minimum requirements for documentation, security, and A2A agent discoverability.

---

## What It Checks

### All Repositories
| Check | Description | Severity |
|-------|-------------|----------|
| `README.md` | Project documentation exists | High |
| `LICENSE` | Open source license file | Medium |
| `.gitignore` | Git ignore configuration | Low |
| Secret Detection | Scans for hardcoded API keys, passwords, tokens | Critical |
| GitHub Topics | Repository has at least 1 topic | Medium |

### A2A Agent Repositories
| Check | Description | Severity |
|-------|-------------|----------|
| `AGENTS.md` | Agent operating manual | Critical |
| `agent.json` | A2A agent card metadata | High |
| Topic `opensin-agent` | Discoverability tag | Medium |

### MCP Server Repositories
| Check | Description | Severity |
|-------|-------------|----------|
| `README.md` | Server documentation | Critical |
| `AGENTS.md` | Agent operating manual | Critical |
| `mcp-config.json` | MCP server configuration | High |
| Topic `opensin-mcp` | Discoverability tag | Medium |

---

## Triggers

### Automatic
- **On Push to `main`:** Scans the current repository
- **On Pull Request to `main`:** Scans the current repository

### Manual
- **Workflow Dispatch:** Can scan all repositories in the organization

---

## How to Run

### Automatic (No Action Required)
The workflow runs automatically on every push and pull request to `main`. Results appear in:
- **PR:** Check runs tab
- **Push:** Actions tab → "Repo Health Check"

### Manual Organization-Wide Scan
1. Go to **Actions** tab
2. Select **Repo Health Check**
3. Click **Run workflow**
4. Check **"Scan all repos in OpenSIN-AI org"**
5. Click **Run workflow**

### Via GitHub CLI
```bash
# Trigger workflow dispatch
gh workflow run repo-health-check.yml \
  --ref main \
  -f scan_all_repos=true \
  -f org=OpenSIN-AI

# Check results
gh run view --log
```

---

## Interpreting Results

### GitHub Step Summary
Results are written to `$GITHUB_STEP_SUMMARY` and displayed in:
- PR comment (for pull_request trigger)
- Workflow run summary (for push trigger)

### Symbols
| Symbol | Meaning |
|--------|---------|
| ✅ | Check passed |
| ❌ | Check failed — action required |
| ⚠️ | Warning — optional but recommended |
| 🔴 | Critical security issue — immediate action required |

### Secret Detection
If secrets are detected:
1. The file path is reported (but NOT the secret content)
2. **IMMEDIATELY** rotate the exposed credential
3. Add the file to `.gitignore` if it contains sensitive config
4. Remove the hardcoded value and use environment variables

---

## Adding Custom Checks

To add custom compliance checks, edit `.github/workflows/repo-health-check.yml`:

```yaml
# Add a new check in the "Check repo compliance" step:
if [ -f "YOUR-FILE" ]; then
  echo "- ✅ YOUR-FILE exists" >> $GITHUB_STEP_SUMMARY
else
  echo "- ❌ YOUR-FILE missing" >> $GITHUB_STEP_SUMMARY
fi
```

For organization-wide scanning, add a new table section in the "Scan all repos" step following the existing pattern.

---

## Configuration

### Required Secrets
| Secret | Description | Required |
|--------|-------------|----------|
| `GITHUB_TOKEN` | Provided automatically by GitHub Actions | Yes |

### Optional Inputs
| Input | Type | Default | Description |
|-------|------|---------|-------------|
| `scan_all_repos` | boolean | `false` | Scan all repos in org |
| `org` | string | `OpenSIN-AI` | Organization to scan |

---

## Compliance Tiers

Repositories are classified into tiers based on their role:

### Tier 1: A2A Agents
Must have: `AGENTS.md`, `agent.json`, topic `opensin-agent`, `README.md`
Examples: `A2A-SIN-TelegramBot`, `A2A-SIN-Google-Apps`

### Tier 2: MCP Servers
Must have: `README.md`, `AGENTS.md`, `mcp-config.json`, topic `opensin-mcp`
Examples: `MCP-SIN-usebrowser`, `MCP-SIN-memory`

### Tier 3: Infrastructure
Must have: `README.md`, `LICENSE`, `.gitignore`
Examples: `OpenSIN-documentation`, `Template-SIN-Agent-Worker`

### Tier 4: Utilities
Must have: `README.md`, `.gitignore`
Examples: `scripts/`, `tools/`

---

## Related Issues
- [#95](https://github.com/OpenSIN-AI/OpenSIN-documentation/issues/95) — 20 repos missing AGENTS.md
- [#96](https://github.com/OpenSIN-AI/OpenSIN-documentation/issues/96) — 7 MCP servers without README
- [#97](https://github.com/OpenSIN-AI/OpenSIN-documentation/issues/97) — 8 repos missing GitHub topics

---

## Relevante Mandate

| Mandat | Priority | Regel |
|--------|----------|-------|
| **Immediate Bug Registry** | -4.0 | JEDER Bug SOFORT als GitHub Issue |
| **PR-Watcher** | 0.0 | Alle Repos brauchen PR-Watcher |
| **Zeus/Hermes** | 0.0 | Fleet-Kommando via SIN-Zeus |

→ [Alle Mandate](/best-practices/error-handling)
