# Migrations Overview — OpenSIN-AI Migration Guides

**Status:** Active
**Owner:** Team Coding

---

## What Are Migrations?

Migration guides document the process of transitioning between versions, architectures, or configurations in the OpenSIN-AI ecosystem. They ensure fleet-wide consistency and prevent breakage during upgrades.

---

## Migration Categories

### 1. OpenCode Config Migrations
Changes to `~/.config/opencode/opencode.json` that require fleet-wide sync:
- Model updates or additions
- Provider configuration changes
- Plugin additions/removals
- MCP server registration changes

**Sync command:** `sin-sync` (pushes Mac → OCI VM → HF VMs)

### 2. Agent Migrations
Updating agent configurations across teams:
- Team member additions/removals
- Model reassignments
- Capability registry updates
- Telegram bot re-registration

### 3. Database Migrations
Supabase schema changes:
- New tables for agent pools
- Column additions/modifications
- Index optimizations
- Data migrations

### 4. Infrastructure Migrations
OCI VM, Cloudflare Workers, HF Space changes:
- Container image updates
- Proxy configuration changes
- SSL/TLS certificate rotations
- Domain migrations

---

## Migration Protocol

1. **Announce**: Create GitHub Issue with migration details
2. **Test**: Apply migration on staging/dev environment
3. **Document**: Update migration guide with steps and rollback plan
4. **Execute**: Run migration during low-traffic window
5. **Verify**: Run health checks across all fleet nodes
6. **Sync**: Run `sin-sync` to propagate config changes

---

## Rollback Procedure

Every migration MUST have a rollback plan:
1. Revert config changes from backup
2. Restore database from snapshot
3. Run `sin-sync` with previous config
4. Verify fleet health returns to baseline

---

## Active Migrations

| Migration | Status | Date | Impact |
|-----------|--------|------|--------|
| *(none currently active)* | — | — | — |

---

## Past Migrations

| Migration | Completed | Notes |
|-----------|-----------|-------|
| Antigravity Plugin Migration | 2026-04 | All fleet nodes updated to use Antigravity OAuth |
| Bun Package Manager Mandate | 2026-03 | npm permanently banned, bun enforced |
| Technology Sovereignty Mandate | 2026-03 | Camoufox/Playwright/Puppeteer/Selenium banned |

---

## Related

- [sin-sync Documentation](/guide/deployment)
- [OpenCode Config Guide](/guide/agent-configuration)
- [Governance Overview](/governance/overview)

---

## Relevante Mandate

| Mandat | Priority | Regel |
|--------|----------|-------|
| **Bun-Only** | -1.5 | `bun install` / `bun run` statt npm |
| **Annahmen-Verbot** | -5.0 | KEINE Diagnose ohne Beweis |
| **Test-Beweis-Pflicht** | 0.0 | KEIN "Done" ohne echten Test-Lauf |

→ [Alle Mandate](/best-practices/code-quality)
