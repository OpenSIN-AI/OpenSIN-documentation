# OpenSIN VS Code Extension — Features

Übersicht aller Feature-Dokumentationen für die SIN Code Extension.

## Feature-Übersicht

Die SIN Code Extension ist in drei Phasen aufgebaut, die schrittweise neue Fähigkeiten hinzufügen:

### Phase 1: Core AI Assistant
Der grundlegende KI-Assistent direkt im Editor.

| Feature | Beschreibung |
|---------|-------------|
| **Agent Modes** | Code, Plan, General – spezialisierte Modi für verschiedene Aufgaben |
| **Sidebar Chat** | Natürlichsprachlicher Chat mit dem KI-Agenten |
| **Memory Consolidation** | Automatische Speicherung von Kontext in `SIN-MEMORY.md` |
| **LSP Integration** | Language Server Protocol für Diagnosen, Symbole, Cursor-Kontext |
| **Model Selector** | Modell-Auswahl via Status Bar oder Command Palette |

→ [Phase 1 Details](./phase1-core-assistant.md)

### Phase 2: Intelligence Layer
Erweiterte Intelligenz durch Swarm-Koordination und Gamification.

| Feature | Beschreibung |
|---------|-------------|
| **Swarm Coordinator** | Multi-Agent-Delegation via OMOC Swarm |
| **BUDDY Gamification** | XP-System, Level-Ups, Belohnungen für Code-Qualität |
| **Auto Test Runner** | Automatische Test-Ausführung bei Code-Änderungen |
| **File Context** | Intelligenter Datei-Kontext für präzisere Antworten |

→ [Phase 2 Details](./phase2-intelligence-layer.md)

### Phase 3: Advanced Capabilities
Professionelle Features für Power-User.

| Feature | Beschreibung |
|---------|-------------|
| **Inline Completions** | KI-generierte Code-Vervollständigungen inline |
| **AI Code Actions** | Kontext-sensitive Code-Aktionen (Refactor, Explain, Fix) |
| **Agent Marketplace** | Community-Agenten installieren und konfigurieren |

→ [Phase 3 Details](./phase3-advanced-capabilities.md)

## Schnellstart

1. Lies die [Architektur-Übersicht](../architecture/overview.md) für das Gesamtsystem
2. Installiere die Extension ([Installationsanleitung](../setup/installation.md))
3. Starte mit [Phase 1](./phase1-core-assistant.md) für die Kernfunktionen
4. Arbeite dich zu [Phase 2](./phase2-intelligence-layer.md) und [Phase 3](./phase3-advanced-capabilities.md) vor

## Feature-Vergleich

| Feature | Phase 1 | Phase 2 | Phase 3 |
|---------|:-------:|:-------:|:-------:|
| Sidebar Chat | ✅ | ✅ | ✅ |
| Agent Modes | ✅ | ✅ | ✅ |
| Memory | ✅ | ✅ | ✅ |
| LSP Integration | ✅ | ✅ | ✅ |
| Model Selector | ✅ | ✅ | ✅ |
| Swarm Coordinator | ❌ | ✅ | ✅ |
| BUDDY Gamification | ❌ | ✅ | ✅ |
| Auto Test Runner | ❌ | ✅ | ✅ |
| Inline Completions | ❌ | ❌ | ✅ |
| AI Code Actions | ❌ | ❌ | ✅ |
| Agent Marketplace | ❌ | ❌ | ✅ |

## Bekannte Einschränkungen

Siehe [Troubleshooting Guide](../troubleshooting/guide.md#known-limitations) für aktuelle Limitationen und Workarounds.
