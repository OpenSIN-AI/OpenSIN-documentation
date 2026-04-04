# 👥 Agents Window

Paralleles Agent-Management über Repositories hinweg.

## Architektur

```
┌─────────────────────────────────────────────────────┐
│                  Agents Window                       │
├──────────┬──────────┬──────────┬────────────────────┤
│ Agent 1  │ Agent 2  │ Agent 3  │    Fleet View      │
│ /repo-a  │ /repo-b  │ /repo-c  │    Monitor         │
│ [active] │ [idle]   │ [busy]   │                    │
│          │          │          │  Health  Metrics   │
│ Terminal │ Terminal │ Terminal │  Controls          │
│ Output   │ Output   │ Output   │                    │
└──────────┴──────────┴──────────┴────────────────────┘
```

Jede Pane hat einen unabhängigen Session mit:
- Eigenem Working Directory und Repository-Kontext
- Tool Call History und Transcript
- Memory Index und Topic Store
- Hook Pipeline Konfiguration

## API Reference

| Method | Path | Beschreibung |
|--------|------|-------------|
| GET | `/api/agents/window` | Alle aktiven Agenten auflisten |
| POST | `/api/agents/window/spawn` | Neuen Agenten spawnen |
| POST | `/api/agents/window/:agentId/message` | Nachricht an Agent senden |
| GET | `/api/agents/window/:agentId/transcript` | Agent-Transcript abrufen |

## Konfiguration

```json
{
  "agents": {
    "window": {
      "max_concurrent": 8,
      "layout": "grid",
      "auto_focus": "active",
      "sync_memory": true,
      "transcript_dir": "~/.opensin/transcripts"
    }
  }
}
```

## Use Cases

- **Parallel Code Review:** 3 Agenten über 3 Repos gleichzeitig
- **Cross-Repository Refactoring:** Breaking Change über Core/Client/Server koordinieren
- **Fleet Monitoring:** Alle Agenten mit Health Metrics im Blick

## 🔗 Verknüpfte Dokumentation

- [OpenSIN Plattform](./opensin-platform.md) – Architektur-Übersicht
- [ACP Protocol](./acp-protocol.md) – Kommunikationsprotokoll
