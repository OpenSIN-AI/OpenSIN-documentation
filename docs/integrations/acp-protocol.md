# 🔌 ACP Protocol (Agent Communication Protocol)

Das ACP (Agent Communication Protocol) ist das fundamentale Kommunikationsprotokoll von OpenSIN – JSON-RPC 2.0 über WebSocket mit Erweiterungen für Echtzeit-Agent-Kommunikation.

## 📋 Protokoll-Übersicht

| Eigenschaft | Wert |
|-------------|------|
| **Version** | 1.0.0 |
| **Transport** | WebSocket (primary), HTTP+SSE (secondary), CLI (fallback) |
| **Wire Format** | JSON-RPC 2.0 |
| **Default Port** | 8765 |
| **Max Message Size** | 16 MB |
| **Encoding** | UTF-8 |

## 🏗️ Architektur

```
┌─────────────────────────────────────────────────────────────┐
│                    ACP Protocol Stack                        │
├─────────────────────────────────────────────────────────────┤
│  Layer 4: Content Security                                  │
│  Input sanitization · Output encoding · Secret redaction     │
├─────────────────────────────────────────────────────────────┤
│  Layer 3: Tool Security                                     │
│  Permission matrix · Path traversal · Command injection      │
├─────────────────────────────────────────────────────────────┤
│  Layer 2: Transport Security                                │
│  TLS/WSS · Origin validation · Message size limits           │
├─────────────────────────────────────────────────────────────┤
│  Layer 1: Connection Security                               │
│  Localhost binding (dev) · Token auth (prod) · Rate limiting │
├─────────────────────────────────────────────────────────────┤
│  Transport: WebSocket (ws:// or wss://)                      │
├─────────────────────────────────────────────────────────────┤
│  Wire: JSON-RPC 2.0 (Request/Response/Notification)          │
└─────────────────────────────────────────────────────────────┘
```

## 🔑 JSON-RPC Envelope

### Request
```json
{
  "jsonrpc": "2.0",
  "id": "req-1712000000000-a1b2c3d4",
  "method": "initialize",
  "params": { ... }
}
```

### Response
```json
{
  "jsonrpc": "2.0",
  "id": "req-1712000000000-a1b2c3d4",
  "result": { ... },
  "error": null
}
```

### Notification (keine Antwort erwartet)
```json
{
  "jsonrpc": "2.0",
  "method": "session/update",
  "params": { ... }
}
```

## 🔄 Session Methods

| Method | Beschreibung |
|--------|-------------|
| `initialize` | Protokoll-Version aushandeln, Capabilities austauschen |
| `session/new` | Neue Session erstellen mit MCP-Server-Konfiguration |
| `session/load` | Bestehende Session laden |
| `session/list` | Alle verfügbaren Sessions auflisten |
| `session/close` | Session schließen und aufräumen |
| `prompt` | Nachricht an Agent senden |
| `prompt/cancel` | Laufenden Prompt abbrechen |
| `prompt/stream` | Gestreamte Antwort via SSE |

## 🎯 Session Modes

| Mode | Zweck | Datei-Zugriff | Terminal | Checkpoints |
|------|-------|---------------|----------|-------------|
| **Architect** | System-Design, Planung | Read-only | ❌ | Optional |
| **Code** | Implementierung, Refactoring | Read/Write (Review) | ✅ | Empfohlen |
| **Debug** | Fehleranalyse, Fixes | Read/Write (Review) | ✅ (diagnostisch) | Empfohlen |
| **Ask** | Fragen, Erklärungen | Read-only | ❌ | ❌ |

## 🛠️ Built-in Tools

| Tool | Permission | Beschreibung |
|------|-----------|-------------|
| `read_file` | read | Datei lesen |
| `write_file` | write | Datei schreiben/ändern |
| `search_files` | read | Dateien nach Pattern durchsuchen |
| `grep` | read | Datei-Inhalte durchsuchen |
| `list_directory` | read | Verzeichnis auflisten |
| `run_terminal` | execute | Shell-Befehl ausführen |
| `create_checkpoint` | write | Git-Checkpoint erstellen |
| `rollback_checkpoint` | write | Zu Checkpoint zurückkehren |

## 📡 Streaming Events

| Event | Daten-Typ | Beschreibung |
|-------|-----------|-------------|
| `chunk` | StreamChunk | Text-Chunk |
| `tool_call` | ToolCall | Tool-Aufruf initiiert |
| `plan_update` | Plan | Plan-Eintrag aktualisiert |
| `mode_update` | CurrentModeUpdate | Session-Modus geändert |
| `config_update` | ConfigOptionUpdate | Config-Optionen geändert |
| `complete` | null | Stream abgeschlossen |
| `error` | StreamError | Stream-Fehler |

## 🔐 Error Codes

| Code | Name | Beschreibung |
|------|------|-------------|
| `-32700` | Parse error | Ungültiges JSON |
| `-32600` | Invalid Request | Kein gültiger JSON-RPC Request |
| `-32601` | Method not found | Methode nicht verfügbar |
| `-32602` | Invalid params | Ungültige Parameter |
| `-32603` | Internal error | Interner Server-Fehler |
| `-32000` | Connection error | WebSocket verloren |
| `-32001` | Timeout | Request timed out |
| `-32002` | Tool error | Tool-Ausführung fehlgeschlagen |
| `-32003` | File error | Datei-Operation fehlgeschlagen |
| `-32004` | Terminal error | Terminal-Operation fehlgeschlagen |
| `-32005` | Checkpoint error | Checkpoint-Operation fehlgeschlagen |
| `-32006` | Session error | Session nicht gefunden |
| `-32007` | Provider error | LLM-Provider Fehler |
| `-32008` | Auth error | Authentifizierungsfehler |

## 📝 Content Block Types

| Typ | Beschreibung |
|-----|-------------|
| `TextBlock` | Plain text oder Markdown |
| `CodeBlock` | Strukturierter Code mit Sprache und Pfad |
| `ImageBlock` | Base64-kodierte Bilder für Vision-Modelle |
| `ResourceBlock` | Externe Ressourcen (file://, https://, data:, acp://) |
| `ToolUseBlock` | Tool-Aufruf innerhalb einer Antwort |
| `ToolResultBlock` | Ergebnis eines Tool-Aufrufs |

## 🚀 Quickstart

### SDK (Empfohlen)
```typescript
import { OpenSINClient } from '@opensin/sdk';

const client = new OpenSINClient({
  baseUrl: 'ws://localhost:8765',
  apiKey: process.env.OPENAI_API_KEY,
  timeout: 30_000,
  retries: 3,
});

await client.connect();
const { sessionId } = await client.createSession({
  cwd: '/Users/jeremy/dev/my-project',
  mcpServers: [],
});
const response = await client.prompt(sessionId, [
  { type: 'text', text: 'Explain the architecture' },
]);
```

### CLI Fallback
```bash
opencode run "Explain the architecture" --model openrouter/qwen/qwen3.6-plus:free
```

## 🔗 Verknüpfte Dokumentation

- [Session Modes](./acp-session-modes.md) – Architect, Code, Debug, Ask
- [Tool Calls](./acp-tool-calls.md) – Tool Lifecycle und Permissions
- [Content Model](./acp-content-model.md) – Multi-modal Content Blocks
- [Security](./acp-security.md) – Auth, Authorization, Path Safety
- [API Reference](./api-reference.md) – Vollständige API-Referenz
