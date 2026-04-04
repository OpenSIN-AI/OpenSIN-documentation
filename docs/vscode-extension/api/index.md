# OpenSIN VS Code Extension — API Reference

Übersicht aller API-Dokumentationen für die SIN Code Extension.

## API-Dokumente

| Dokument | Beschreibung |
|----------|--------------|
| [CLI Bridge](./cli-bridge.md) | Kommunikation zwischen VS Code Extension und `opencode` CLI |
| [LSP Provider](./lsp-provider.md) | Language Server Protocol Integration für Diagnosen, Symbole, Cursor-Kontext |
| [Internal APIs](./internal-apis.md) | Interne Schnittstellen und Hilfsfunktionen |

## Architektur-Kontext

Die APIs sind Teil der größeren Extension-Architektur. Siehe:

- [Architektur-Übersicht](../architecture/overview.md) – Systemdesign und Datenfluss
- [Feature-Dokumentation](../features/) – Was die APIs ermöglichen

## CLI Bridge

Der CLI Bridge ist die zentrale Kommunikationsschicht:

```
VS Code Extension  ←→  CLI Bridge  ←→  opencode CLI  ←→  SIN-Stack
```

Er serialisiert Anfragen, verwaltet die Prozess-Lifecycle und leitet Streaming-Antworten zurück an die UI.

## LSP Provider

Der LSP Provider extrahiert Kontext aus dem Editor:

- **Diagnostics** – Fehler und Warnungen aus dem Language Server
- **Symbole** – Funktionen, Klassen, Variablen im aktuellen Dokument
- **Cursor-Kontext** – Aktuelle Position und umgebender Code

## Interne APIs

Interne Schnittstellen für State Management, Event Handling und Extension-Kommunikation. Details in [Internal APIs](./internal-apis.md).
