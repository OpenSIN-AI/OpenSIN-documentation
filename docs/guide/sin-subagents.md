# SIN Subagents — Parallel Agent Execution

> **OpenSIN's Subagent System** — Lass Agenten parallel arbeiten, jeder mit eigenem Modell, Tools und Memory.

## Overview

Subagents sind isolierte Agenten-Instanzen die parallel zum Haupt-Agenten arbeiten. Jeder Subagent hat sein eigenes Modell, seine eigenen Tools und sein eigenes Memory.

## Subagent erstellen

```python
from opensin import Agent, Subagent

# Haupt-Agent
main_agent = Agent(name="main", model="gpt-4")

# Subagent parallel starten
subagent = Subagent(
    name="researcher",
    model="gpt-4",
    system_prompt="You are an expert researcher.",
    tools=["web_search", "summarizer"],
    background=True  # Im Hintergrund ausführen
)

# Nachricht an Subagent senden
await subagent.send("Research AI trends for 2026")

# Ergebnis abholen
result = await subagent.get_output()
```

## Parallele Subagents

```python
from opensin import SubagentPool

pool = SubagentPool()

# Mehrere Subagents parallel starten
results = await pool.execute([
    Subagent(name="researcher", task="Research topic A"),
    Subagent(name="analyst", task="Analyze data"),
    Subagent(name="writer", task="Write report"),
])

# Alle Ergebnisse sammeln
for result in results:
    print(f"{result.agent_name}: {result.output}")
```

## Subagent Typen

| Typ | Beschreibung | Use Case |
|-----|-------------|----------|
| `parallel` | Läuft parallel zum Haupt-Agenten | Recherche, Analyse |
| `background` | Läuft im Hintergrund mit File-Output | Lange Tasks, Monitoring |
| `sequential` | Läuft nacheinander | Pipeline-Verarbeitung |
| `coordinator` | Koordiniert andere Subagents | Team-Management |

## Subagent Kommunikation

```python
from opensin import Subagent, MessageBus

bus = MessageBus()

# Subagents registrieren
researcher = Subagent(name="researcher")
writer = Subagent(name="writer")

bus.register(researcher)
bus.register(writer)

# Nachrichten zwischen Subagents
await bus.send(
    from_agent="researcher",
    to_agent="writer",
    message="Here are the research results..."
)
```

## Subagent mit eigenem Modell

```python
# Teures Modell für komplexe Tasks
architect = Subagent(
    name="architect",
    model="gpt-4",  # Teuer aber smart
    task="Design system architecture"
)

# Günstiges Modell für einfache Tasks
formatter = Subagent(
    name="formatter",
    model="gpt-3.5-turbo",  # Günstig und schnell
    task="Format the output"
)

# Parallel ausführen
results = await SubagentPool().execute([architect, formatter])
```

## Subagent Memory

Jeder Subagent hat sein eigenes isoliertes Memory:

```python
subagent = Subagent(
    name="researcher",
    memory_enabled=True,
    memory_path=".sin/memory/researcher.json"
)

# Memory persistiert über Sessions
await subagent.save_memory()
await subagent.load_memory()
```

## Best Practices

1. **Modell-Mix** — Teure Modelle nur wo nötig
2. **Isolation** — Jeder Subagent = eigener Context
3. **Timeout** — Immer Timeout setzen
4. **Error Handling** — Subagent Crashes abfangen
5. **Resource Limits** — Max Subagents begrenzen

## Next Steps

- [Team Orchestration](/guide/team-orchestration)
- [SIN Hooks](/guide/sin-hooks)
