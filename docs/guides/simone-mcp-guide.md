# 🔌 Simone MCP Adoption Guide

Simone MCP ist die 2026-Nachfolge von Serena MCP für die SIN-Solver A2A-Flotte.

## Problem mit Serena MCP

| Problem | Auswirkung |
|---------|-----------|
| Keine A2A-Discovery | Andere Agenten können Serena nicht automatisch finden |
| Synchrone Blockade | Aufrufender Agent muss warten |
| Lokaler Speicher | `.serena/memories/` geht bei VM-Neustarts verloren |
| Kein Self-Healing | Manuelles Deployment, kein Keep-Alive |

## Simone MCP Lösung

| Dimension | Serena MCP | Simone MCP |
|-----------|------------|------------|
| **Discovery** | Manuell | ✅ A2A `agent-card.json` |
| **Runtime** | Sync blocking | ✅ Async (Supabase Events) |
| **Memory** | Local files | ✅ Cloud (pgvector) |
| **Dashboard** | Basic CLI | ✅ Enterprise UI |
| **Deployment** | Manual | ✅ Live HF Space + Keep-Alive |

## Migration

**Statt (Serena):**
```python
result = serena.find_symbol("my_function")
edit_code(result)
```

**Wird zu (Simone):**
```python
task_id = await simone.find_symbol("my_function")
# Agent macht weiter mit anderen Tasks
result = await wait_for_task(task_id)
```

## Quick Start

```bash
# Simone MCP aktivieren (öffnet Dashboard)
activate_simone

# Oder direkt als A2A-Agent nutzen
npx a2a send --agent simone-mcp --action code.find_symbol --params '{"query":"calculate_discount"}'
```

## Live State

- Public A2A landing: `https://a2a.delqhi.com/agents/simone-mcp`
- HF runtime: `https://delqhi-simone-mcp.hf.space`

## 🔗 Verknüpfte Dokumentation

- [OpenSIN Packages](./opensin-packages.md) – Alle 372 Packages
- [ACP Protocol](./acp-protocol.md) – Kommunikationsprotokoll
