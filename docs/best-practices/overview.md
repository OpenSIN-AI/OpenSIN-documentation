# 🛡️ Best Practices & Safe Engineering

Willkommen bei den Best Practices von OpenSIN! Wir legen größten Wert auf **Sicherheit, Stabilität und professionelles Engineering**. Diese Richtlinien helfen dir, von Tag 1 an sauberen Code zu schreiben, der unseren Enterprise-Standards entspricht.

---

## 1. 🔐 Sicherheit & Credentials ("Safe & Compliant")

OpenSIN ist eine mächtige A2A (Agent-to-Agent) Plattform. Mit großer Kraft kommt große Verantwortung.

### Secrets Management

**NIEMALS:**
- ❌ API-Keys, Passwörter oder Tokens im Code hardcoden
- ❌ `.env`-Dateien committen
- ❌ Secrets in Logs ausgeben
- ❌ Secrets in URL-Query-Params übergeben
- ❌ Secrets in GitHub Actions Logs lecken lassen

**IMMER:**
- ✅ Umgebungsvariablen nutzen
- ✅ GitHub Secrets für CI/CD
- ✅ `.gitignore` für `.env*`-Dateien
- ✅ `sin-passwordmanager` für OpenSIN-interne Secrets
- ✅ Secrets regelmäßig rotieren (siehe [Auth Rotator](./auth-rotator.md))

### Input Validation

Jeder Agent MUSS:
- [ ] Alle Inputs mit Zod-Schemas validieren
- [ ] User-Input vor Verarbeitung sanitizen
- [ ] Parametrisierte Queries für Datenbank-Operationen
- [ ] File-Uploads validieren (Typ, Größe, Inhalt)
- [ ] API-Endpoints rate-limiten

### Guardrails

Jeder Agent MUSS haben:
- [ ] Prompt-Injection-Erkennung
- [ ] Jailbreak-Pattern-Erkennung
- [ ] PII-Erkennung (SSN, Kreditkarten, API-Keys)
- [ ] Toxicity-Scoring
- [ ] Halluzinations-Erkennung
- [ ] Invisible-Unicode-Erkennung

### Agent Security

- [ ] Alle Agent-Operationen werden in OpenSIN-Ledger geloggt
- [ ] Authorization-Token erforderlich für alle Agent-Aktionen
- [ ] Guardrails auf allen Inputs/Outputs
- [ ] Sandboxing für nicht-vertrauenswürdigen Code
- [ ] Allowlist für Agent-Capabilities

### Browser-Automatisierung Sicherheit

- [ ] Nur genehmigte, ethische Workflows nutzen (nodriver, keine Playwright/Docker-Container für Auth)
- [ ] Eigene Test-Accounts verwenden
- [ ] Isolierte Chrome-Profile pro Rotation
- [ ] Keine "Hacker"-Allüren – professionelle Enterprise-Software
- [ ] Credentials schützen via `sin-passwordmanager` oder env vars

---

## 2. 📸 Dokumentation: Visuals First!

> *"Bilder und Videos sagen mehr als tausend Worte."*

### README.md Pflichtinhalt

Jedes Repository MUSS haben:
- [ ] Projektname + Einzeiler-Beschreibung
- [ ] Badges (License, Stars, Build-Status)
- [ ] Table of Contents
- [ ] Quick Start (3 Commands max)
- [ ] Features-Liste
- [ ] Architektur-Diagramm (ASCII oder Bild)
- [ ] API-Reference oder Link zu Docs
- [ ] Contributing-Section mit Link zu CONTRIBUTING.md
- [ ] License-Section mit Link zu LICENSE
- [ ] Links zu verwandten Repos

### JSDoc/TSDoc für alle exportierten Funktionen

```typescript
/**
 * Erstellt eine neue A2A-Agent-Session.
 *
 * @param config - Session-Konfiguration
 * @param config.model - Zu verwendendes Modell (z.B. "gpt-4")
 * @param config.tools - Liste verfügbarer Tools
 * @returns Promise mit Session-ID
 * @throws {ValidationError} Wenn Config ungültig
 * @throws {ConnectionError} Wenn A2A-Server nicht erreichbar
 *
 * @example
 * ```typescript
 * const sessionId = await createSession({
 *   model: "gpt-4",
 *   tools: ["search", "code"],
 * })
 * ```
 */
export async function createSession(config: SessionConfig): Promise<string>
```

### Code Comments

**DO:**
- Erkläre WARUM, nicht WAS
- Dokumentiere komplexe Algorithmen
- Notiere Trade-offs und Limitationen
- Verlinke auf relevante Issues/PRs

**DON'T:**
- Offensichtlichen Code kommentieren
- Auskommentierten Code stehen lassen (Null-Leichen-Policy!)
- TODO ohne Issue-Link verwenden
- Veraltete Kommentare schreiben

### Dokumentation aktualisieren bei:
- API-Änderungen
- Konfigurationsänderungen
- Setup-Prozess-Änderungen
- Architektur-Änderungen
- Dependency-Änderungen

---

## 3. 🚦 Der "Check-Plan-Done" Workflow

Bevor du Code schreibst, plane ihn!

1. **Research:** Gibt es bereits ein Issue? Doku gelesen? Best Practices geprüft?
2. **Plan:** Skizziere Lösung kurz (im Issue oder lokal).
3. **Execute:** Schreibe den Code.
4. **Verify:** Teste gründlich, bevor du einen PR öffnest.
5. **Document:** Aktualisiere README, CHANGELOG, und relevante Docs.
6. **Visual Proof:** Poste Screenshots/Videos im PR.

---

## 4. 🧪 Testing

### Struktur

```
src/
  index.ts
  utils.ts
tests/
  index.test.ts
  utils.test.ts
```

### Coverage Thresholds

| Metrik | Minimum |
|--------|---------|
| Lines | 80% |
| Functions | 80% |
| Branches | 70% |
| Statements | 80% |

### Regeln

1. **Teste Verhalten, nicht Implementierung** – Was der Code tut, nicht wie
2. **Eine Assertion pro Test** – Jeder Test prüft eine Sache
3. **Sinnvolle Test-Namen** – "should X when Y"
4. **Externe Dependencies mocken** – Keine echten APIs in Tests
5. **Edge Cases testen** – Empty Input, Null, Undefined, Max Values
6. **Error Paths testen** – Nicht nur den Happy Path
7. **Tests schnell halten** – Komplette Suite unter 10 Sekunden

### Was NICHT zu testen ist
- ❌ Third-Party-Library-Internals
- ❌ Framework-Code
- ❌ Private Methods (über Public API testen)
- ❌ Simple Getter/Setter
- ❌ Console Output (außer es ist das Feature)

---

## 5. 🔍 Code Review

### Vor dem PR

- [ ] Tests lokal: `npm test`
- [ ] Linter lokal: `npm run lint`
- [ ] Type Checker: `npm run build`
- [ ] Eigenen Code zuerst selbst reviewen
- [ ] Klare PR-Beschreibung schreiben
- [ ] Related Issue verlinken
- [ ] Screenshots für visuelle Änderungen

### Reviewer Checklist

- [ ] Code lesbar und gut organisiert
- [ ] Keine hardcoded Secrets
- [ ] Error Handling adäquat
- [ ] Tests coveren die Änderungen
- [ ] Dokumentation aktualisiert
- [ ] Keine unnötigen Dependencies
- [ ] Performance-Impact bedacht
- [ ] Security-Implikationen bedacht

### Response Times

| Typ | Zeit |
|-----|------|
| Critical Bugs | Innerhalb 2 Stunden |
| Features | Innerhalb 24 Stunden |
| Documentation | Innerhalb 48 Stunden |
| Dependencies | Innerhalb 1 Woche |

### Review Etikette

- Konstruktiv, nicht kritisch
- Fragen stellen, nicht fordern
- Warum erklären, nicht nur was
- Alternativen vorschlagen
- Gute Arbeit anerkennen
- `nit:` für kleine Vorschläge
- `suggestion:` für optionale Verbesserungen

---

## 6. 🚀 CI/CD (n8n + A2A Pipeline)

OpenSIN nutzt **n8n + A2A CI/CD** – unser eigenes autonomes System.

### Pipeline-Stages

1. **Clone** – A2A CI/CD Agent cloned das Repo
2. **Lint** – bun lint / eslint / ruff / flake8
3. **Test** – bun test / pytest / vitest mit Coverage
4. **Security** – trivy / npm audit / bandit / codeql
5. **Build** – bun build / docker build
6. **Deploy** – Deploy zu OCI/HF wenn alle Stages passieren
7. **Notify** – Ergebnisse via Telegram/Discord

### Regeln

1. **KEINE GitHub Actions** – niemals, in keinem Repo
2. **`.github/workflows/ci.yml` entfernen** aus allen Repos
3. **`.github/dependabot.yml` entfernen** aus allen Repos
4. **n8n Webhook nutzen** – alles CI/CD über n8n
5. **A2A Agents nutzen** – lint, test, build, deploy, notify
6. **Auto-Deploy** – bei main push wenn alle Stages passieren

### A2A Dependency Agent

Ersetzt Dependabot:
- Läuft wöchentlich via n8n Cron
- Prüft alle Repos auf veraltete Dependencies
- Erstellt PRs mit aktualisierten Versionen
- Auto-Merge wenn Tests passieren

---

## 7. 🚢 Releases (SemVer)

Alle OpenSIN-AI Pakete nutzen [SemVer](https://semver.org/): `MAJOR.MINOR.PATCH`

| Teil | Bedeutung | Beispiel |
|------|-----------|----------|
| MAJOR | Breaking Changes | `2.0.0` |
| MINOR | Neue Features (abwärtskompatibel) | `0.2.0` |
| PATCH | Bug Fixes (abwärtskompatibel) | `0.1.1` |

### Release-Prozess

1. Version in `package.json` aktualisieren
2. `CHANGELOG.md` aktualisieren
3. Commit: `chore: release v1.2.0`
4. Tag: `git tag v1.2.0`
5. Push: `git push origin main --tags`

---

## 8. 🐳 Hugging Face Space Deployment

### ⚠️ GOLDENE REGELN: KEIN HF SPACE OHNE KEEP-ALIVE + MONITORING!

**Es darf NIEMALS ein HF Space erstellt werden OHNE:**
1. **Keep-Alive** in ALLEN 3 Systemen (n8n + OCI VM + Mac)
2. **Monitoring** in ALLEN 3 Systemen (Auto-Detection + Alert + Recovery)
3. **Dockerfile** im Repo (sonst kein Space möglich)

- Kein Keep-Alive = Space schläft nach 48h ein = Agent offline = Fleet broken
- Kein Monitoring = Space verschwindet unbemerkt = niemand weiß warum
- Kein Dockerfile = Space kann nicht deployed werden
- Diese Regeln sind NICHT verhandelbar.

### Pflicht-Checkliste für JEDES HF Space

- [ ] Space Visibility auf **PUBLIC** setzen (NIEMALS private!)
- [ ] `Dockerfile` – FROM node:22-slim, EXPOSE 7860, HEALTHCHECK
- [ ] `server.js` – Express mit `/health`, `/a2a/v1`, `/.well-known/agent-card.json`
- [ ] `.well-known/agent-card.json` – A2A Agent Discovery Card
- [ ] `package.json` – `@opensin/a2a-sin-<name>`, MIT License
- [ ] `app.py` – HF Space Detection
- [ ] **Space-Name in `~/.opensin/scripts/hf-keepalive.sh` eintragen**
- [ ] **Space-Name in `~/.opensin/scripts/hf-space-monitor.sh` eintragen**
- [ ] **n8n Workflow: Space-Name zur Space List hinzufügen**
- [ ] **OCI VM: Space-Name zu `/usr/local/bin/hf-keepalive.sh` hinzufügen**
- [ ] **OCI VM: Space-Name zu `/usr/local/bin/hf-space-monitor.sh` hinzufügen**
- [ ] LaunchAgent neuladen: `launchctl unload && launchctl load ~/Library/LaunchAgents/com.opensin.hf-keepalive.plist`
- [ ] Monitor LaunchAgent neuladen: `launchctl unload && launchctl load ~/Library/LaunchAgents/com.opensin.hf-monitor.plist`
- [ ] Space-URL testen: `curl -s -o /dev/null -w "%{http_code}" https://delqhi-<space>.hf.space/`
- [ ] Health Endpoint testen: `curl -s -o /dev/null -w "%{http_code}" https://delqhi-<space>.hf.space/health`
- [ ] Agent Card testen: `curl -s -o /dev/null -w "%{http_code}" https://delqhi-<space>.hf.space/.well-known/agent-card.json`
- [ ] Fleet-Validation: `npm run test:a2a:fleet`
- [ ] Live-Audit: `npm run test:a2a:live -- --agent <slug>`

### Hardware-Regel

- **IMMER** `cpu-basic` verwenden (FREE, UNBEGRENZT)
- **NIEMALS** GPU/ZeroGPU für Agent Runtimes

### Keep-Alive Implementation

```bash
# LaunchAgent: ~/Library/LaunchAgents/com.opensin.hf-keepalive.plist
# Script: ~/.opensin/scripts/hf-keepalive.sh
# Intervall: Alle 5 Minuten
# Log: /tmp/sin-hf-keepalive.log
```

**AKTUELLER STAND:** 15 Spaces deployed (von 68 A2A-SIN Repos).
53 Repos haben KEIN Dockerfile → KEIN HF Space möglich.

→ Vollständige Dokumentation: [HF Space Keep-Alive](./hf-keepalive.md)
→ Root Cause Analysis: [HF Space Crisis](./hf-space-crisis.md)
→ Root Cause Analysis: [HF Space Crisis](./hf-space-crisis.md)

---

## 9. 🧩 Modulare A2A-Teams

Wenn du an Marktplatz-Paketen arbeitest:
- Strenge Isolation – Ein Agent-Team darf keine Seiteneffekte auf andere haben
- MCPs, Skills und Tools sauber in jeweilige Verzeichnisse trennen
- Jedes Tool bekommt seine eigene `README.md`!
- A2A Completion Checklist durchgehen (siehe [A2A Fleet](./a2a-fleet.md))

---

## 10. 🌐 Umgang mit Browsern & Chrome-Profilen

- **Trennung von Arbeit und Privat:** Für administrative Aufgaben *immer* das `Geschäftlich` Profil
- **Verifizierung:** Automatisierungen immer sichtbar (nicht headless) testen
- **Isolierte Profile:** Pro Rotation ein frisches Chrome-Profil (`shutil.rmtree` vor jedem Run)
- **Singleton-Locks:** Vor Chrome-Start alle `Singleton*`-Files im Profil-Verzeichnis löschen
- **Kein Playwright/Docker für Auth:** Nur nodriver mit nativem Chrome

---

## 11. 🗑️ Null-Leichen-Policy

- **Kein toter Code** – Unbenutzte Dateien sofort löschen
- **Keine Backups** im Repo (`.bak`, `.old`, `backup/`)
- **Kein auskommentierter Code** – Wenn nicht gebraucht, löschen
- **Keine veralteten Docs** – Alte READMEs/SSOTs aktualisieren oder entfernen
- **Keine `.pyc`-Dateien** – In `.gitignore` aufnehmen

---

> **Danke, dass du diese Best Practices lebst!** Sie machen OpenSIN zu einem sicheren und großartigen Ort für alle.

---

## 12. 🏛️ Governance – 6 Programmatic Checks

`opensin-governance` erzwingt 6 programmatische Regeln:

| Check | Zweck |
|-------|-------|
| **Docs Root Gate** | Keine 0-Byte Dateien, keine leeren Platzhalter |
| **A2A Fleet Validation** | Kanonische MCP-Abdeckung pro Agent |
| **Contract Stability** | API-Verträge nicht brechen |
| **Cycle Detection** | Keine zirkulären Dependencies |
| **Guardrails** | Security/Policy-Checks |
| **Closure Artifacts** | Alle Artefakte vollständig |

**Commands:**
```bash
npm run test:docs:root          # Docs Root Gate
npm run test:a2a:fleet          # Fleet Validation
npm run test:contracts:active   # Contract Stability
npm run test:cycles             # Cycle Detection
npm run test:guardrails         # Guardrails
npm run test:closure:artifacts  # Closure Artifacts
```

---

## 13. 🛡️ Agent Safety – Iteration Caps, Circuit Breaker, Budget Guard

`opensin-agent-safety` schützt vor runaway Agents:

| Mechanismus | Zweck | Konfiguration |
|-------------|-------|---------------|
| **Iteration Caps** | Max Anzahl Agent-Iterationen pro Task | `max_iterations: 50` |
| **Circuit Breaker** | Stoppt Agent bei wiederholten Fehlern | `failure_threshold: 5`, `cooldown_sec: 300` |
| **Budget Guard** | Max Token-Kosten pro Task | `max_tokens: 100000`, `max_cost_usd: 1.0` |
| **Timeout Guard** | Max Ausführungszeit | `timeout_sec: 600` |

**Anti-Patterns:**
- ❌ Unbegrenzte Iterationen → Token-Exhaustion
- ❌ Keine Circuit Breaker → Endlose Error-Loops
- ❌ Kein Budget Guard → Unerwartete Kosten
- ❌ Keine Timeouts → Hängende Prozesse

---

## 14. 🔒 Merge Guard – Symbol-Level Locking via Tree-sitter

`opensin-merge-guard` verhindert Merge-Konflikte auf Symbol-Ebene:

- **Tree-sitter Parsing** – Erkennt Funktionen, Klassen, Variablen
- **Symbol-Level Locking** – Zwei Agents können verschiedene Funktionen in derselben Datei bearbeiten
- **Conflict Detection** – Warnt bei Überlappung von Symbol-Änderungen
- **Auto-Resolution** – Löst nicht-überlappende Changes automatisch

**Workflow:**
```
Agent A ändert function foo()  ─┐
                                 ├──→ Merge Guard prüft Symbol-Overlap → ✅ Kein Konflikt → Auto-Merge
Agent B ändert function bar()  ─┘

Agent C ändert function foo()  ─┐
                                 ├──→ Merge Guard prüft Symbol-Overlap → ❌ Konflikt → Manual Review
Agent D ändert function foo()  ─┘
```

---

## 15. 🔄 Self-Healing – Supervisor Trees, Health Probes, 4-Tier Recovery

`opensin-self-healing` stellt automatische Fehlerbehebung sicher:

### Supervisor Trees
- Jeder Agent läuft unter einem Supervisor
- Supervisor überwacht Health Probes
- Bei Crash: Automatische Neustarts mit Backoff

### Health Probes
| Probe | Intervall | Timeout | Action bei Failure |
|-------|-----------|---------|-------------------|
| **Liveness** | 10s | 5s | Restart Agent |
| **Readiness** | 5s | 3s | Remove from Load Balancer |
| **Startup** | 1s | 30s | Kill + Restart |

### 4-Tier Recovery
| Tier | Trigger | Aktion |
|------|---------|--------|
| **1 – Retry** | Transient Error | Sofortiger Retry (max 3x) |
| **2 – Restart** | Persistent Error | Agent Neustart |
| **3 – Failover** | Agent Unavailable | Backup Agent aktivieren |
| **4 – Escalate** | System Failure | Human-in-the-Loop Alert |

### Checkpoints
- Git-basierte Snapshots vor jeder Änderung
- Automatische Rollback-Fähigkeit
- Checkpoint-History für Audit-Zwecke

---

## 16. 🎨 UX Security – Credential Scrubbing, /color, /status

### Credential Scrubbing
Automatische Erkennung und Redaktion von Secrets in allen Outputs:

| Pattern | Beispiel | Redacted As |
|---------|---------|-------------|
| AWS Access Key | `AKIAIOSFODNN7EXAMPLE` | `[AWS_KEY_REDACTED]` |
| GitHub Token | `ghp_xxxxxxxxxxxx` | `[GITHUB_TOKEN_REDACTED]` |
| OpenAI Key | `sk-xxxxxxxxxxxxxxxx` | `[OPENAI_KEY_REDACTED]` |
| Generic API Key | `api_key=xxxxx` | `[API_KEY_REDACTED]` |
| Password | `password: xxxxx` | `[PASSWORD_REDACTED]` |
| Private Key | `-----BEGIN RSA PRIVATE KEY-----` | `[PRIVATE_KEY_REDACTED]` |
| JWT Token | `eyJhbGciOi...` | `[JWT_REDACTED]` |

**Konfiguration:**
```json
{
  "credential_scrub": {
    "enabled": true,
    "auto_scrub_transcripts": true,
    "auto_scrub_logs": true,
    "auto_scrub_outputs": true,
    "audit_log_enabled": true
  }
}
```

### /color Command
Farbcodierte Status-Anzeige:

| Farbe | Bedeutung |
|-------|-----------|
| 🟢 Grün | Running/Healthy |
| 🟡 Gelb | Idle/Warning |
| 🔴 Rot | Error/Critical |
| 🔵 Blau | Info |
| 🟣 Cyan | Debug |

### /status Command
Umfassende System-Übersicht:
- Agent Health (running/idle/error)
- Resource Usage (CPU, Memory, Disk)
- Security Posture (Scrubbing active, Credentials found today)
- Uptime und Version

---

## 17. 📋 Drop-in Policies – managed-settings.d/

Layered Configuration via Directory-basierte Policies (wie systemd conf.d):

### Naming Convention

| Prefix | Zweck | Beispiel |
|--------|-------|---------|
| `00-*` | Base Configuration | `00-base.json` |
| `10-*` | Security Policies | `10-security.json` |
| `20-*` bis `80-*` | Team/Project Overrides | `20-team-alpha.json` |
| `90-*` | Environment Overrides | `90-production.json` |
| `99-*` | Emergency Overrides | `99-emergency.json` |

### Merge-Regeln
- Lexikographische Reihenfolge (spätere Files überschreiben frühere)
- Deep Merge (nicht Shallow)
- Merge-Report mit Conflicts und Overrides
- Auto-Apply on Startup + Watch for Changes

### Beispiel
```json
// managed-settings.d/00-base.json
{
  "agents": { "max_concurrent": 8, "default_model": "gpt-4o" }
}

// managed-settings.d/10-security.json
{
  "security": { "credential_scrubbing": true, "allowed_tools": ["read_file", "write_file"] },
  "agents": { "max_concurrent": 4 }
}
```

---

## 18. 🤖 Adversary Mode – Selbstkritik für robuste Entscheidungen

Agent spielt den "Advocate of the Opposite":

- **Trigger:** `@adversary <prompt>` oder automatisch vor Production-Deploys
- **Ziel:** Schwachstellen in Plänen, Code und Architektur finden
- **Output:** Liste von Gegenargumenten, Risiken, alternativen Ansätzen
- **Use Cases:** Code-Reviews, Architektur-Entscheidungen, Security-Audits

**Beispiel:**
```
@adversary Should we migrate from REST to GraphQL?

→ Counter-Argument 1: GraphQL over-fetching bei einfachen Queries
→ Counter-Argument 2: Caching-Komplexität steigt signifikant
→ Counter-Argument 3: Team-Lernkurve für GraphQL Schema Design
→ Risk: Breaking Changes für alle bestehenden API-Clients
→ Alternative: REST mit DataLoader + Query-Parameter-Filtering
```

---

## 19. 📊 Best-of-N – Multi-Modell-Vergleich

Für kritische Tasks: Prompt an N Modelle senden und beste Antwort auswählen:

1. **Prompt an N Modelle** (Claude Sonnet, GPT-4o, Gemini Pro)
2. **Antworten sammeln** und parallel auswerten
3. **Bewertung** nach Qualität, Sicherheit, Vollständigkeit
4. **Beste Antwort auswählen** und zurückgeben

**Use Cases:** Code-Reviews, Architektur-Entscheidungen, Security-Audits

---

## 20. 🏠 Self-Hosted Deployment

OpenSIN kann vollständig self-hosted betrieben werden:

| Komponente | Self-Hosted Option |
|------------|-------------------|
| Room-13 | Docker Compose auf OCI VM |
| Supabase | Self-hosted Supabase auf OCI |
| NATS | Docker Container auf OCI |
| Restate | Docker Container auf OCI |
| Redis | Docker Container auf OCI |
| n8n | Docker Container auf OCI |
| HF Executors | Lokale Docker Container |

**Mindestanforderungen:** 8 CPU, 32GB RAM, 200GB SSD

### 🔗 Verknüpfte Dokumentation

- [A2A Fleet](./a2a-fleet.md) – Agent-Deployment-Checklist
- [Auth Rotator](./auth-rotator.md) – Credential-Rotation-Systeme
- [OMOC Swarm](./omoc-swarm.md) – Modell-Routing-Konfiguration
- [Security Policy](./SECURITY.md) – Vulnerability Reporting
- [ACP Protocol](./acp-protocol.md) – Kommunikationsprotokoll
- [Testing & Database](./testing-environment-database.md) – Testing, Env, DB
- [Master Reference](./master-reference.md) – Vollständige Referenz
