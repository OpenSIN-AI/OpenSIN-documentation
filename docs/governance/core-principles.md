# 🌟 Unsere Kernprinzipien (Core Principles)

Bei **OpenSIN** arbeiten wir nach einem klaren Leitfaden. Wir wollen die weltweit benutzerfreundlichste, modularste und gleichzeitig professionellste (Enterprise-Niveau!) A2A-Plattform bauen.

Damit sich jeder (ob Quereinsteiger oder Senior-Entwickler) sofort zurechtfindet und freut, halten wir uns an diese Prinzipien:

---

## 1. 🖼️ Bilder & Videos ("Visuals First")

**Ein Bild sagt mehr als tausend Worte – ein Video sagt noch mehr!**

- Wenn du etwas Neues in `OpenSIN-Code` baust (z. B. ein neues Plugin oder einen MCP-Server), **mache einen Screenshot oder ein kurzes Video** davon in Aktion.
- Wenn eine Anleitung ohne Bild schwer zu verstehen ist, füge eines hinzu.
- Dein Pull Request sollte immer einen visuellen Beweis (Vorher/Nachher) enthalten.
- **Regel:** Keine PRs ohne visuelle Dokumentation bei UI- oder Workflow-Änderungen.

## 2. 🧩 Modularität & Marktplatz-Denken

Wir bauen keine monolithischen Giganten, sondern modulare, verkaufbare und Open-Source-fähige Bausteine.

- **OpenSIN vs. MyOpenSIN:** Denke immer daran, ob dein Code in die kostenlose Open-Source-Version (`OpenSIN`) oder als Abo-Paket auf den Marktplatz (`website-my.opensin.ai`) gehört.
- **Kleine Pakete:** Ein A2A-Team wie `Team-SIN-Google` (für 3,99 €) oder `Team-SIN-Apple` (kostenlos) muss komplett in sich geschlossen und dokumentiert sein.
- **Isolation:** Module dürfen keine versteckten Abhängigkeiten zu anderen Modulen haben.
- **Wiederverwendbarkeit:** Jedes Modul sollte theoretisch als eigenständiges Produkt funktionieren.

## 3. 🛡️ Sicherheit & Enterprise-Qualität ("Safe by Design")

Wir sind professionelle Software-Entwickler. Wir nutzen modernste Automatisierung, aber immer nach ethischen und sicheren Best Practices.

- **Kein "Hacker"-Jargon:** Wir sprechen professionell. Wenn wir Automatisierungen für unsere Kunden bauen, nennen wir sie bei ihrem Namen (z. B. "Automatisierte Workflows", "Browser-Tests").
- **Credentials schützen:** Geheimnisse, API-Keys und Passwörter haben im Code nichts zu suchen. Nutze `sin-passwordmanager` oder Umgebungsvariablen.
- **Transparenz:** Wir dokumentieren offen, wie unsere Systeme arbeiten.
- **Guardrails:** Alle Agent-Inputs/Outputs werden auf Prompt-Injection, PII und Toxizität geprüft.
- **Audit-Logging:** Jede Agent-Operation wird in OpenSIN-Ledger protokolliert.

## 4. 🚀 "Quereinsteiger-Freundlichkeit" (Zero-Friction Onboarding)

Jeder neue Entwickler soll sich vom ersten Tag an bei OpenSIN zuhause fühlen – unabhängig von Vorerfahrung.

- **Schreibe für Anfänger:** Erkläre lieber einen Schritt zu viel als einen zu wenig. Vermeide unerklärte Akronyme und setze keine Vorkenntnisse voraus.
- **Nutze den Standard:** Halte dich immer an das [global-dev-docs-standard](https://github.com/OpenSIN-AI/global-dev-docs-standard) Repository für konsistente Dokumentationsqualität.
- **Jedes Tool eine Readme:** Egal ob Plugin, MCP, Skill, Tool, Watcher oder Wrapper in `OpenSIN-Code` – jedes Element bekommt seine eigene `README.md` mit Quickstart!
- **Fehlertoleranz:** Anleitungen sollten so geschrieben sein, dass ein Neuling ihnen blind folgen kann und am Ende ein funktionierendes Ergebnis hat.
- **Mentoring:** Erfahrene Team-Mitglieder sind angehalten, neue Contributor aktiv zu unterstützen – über GitHub Discussions, PR-Reviews oder Pair Programming.

## 5. 🔄 "Atomic Architecture" (Ein File = Eine Aufgabe)

Jede Datei tut genau eine Sache – nicht mehr, nicht weniger.

- **Micro-Scripts:** Browser-Automatisierungsskripte sind maximal 20-30 Zeilen lang
- **Keine Monolithen:** Keine 800-Zeilen-Skripte – aufteilen in atomare Steps
- **Smart Polling:** Keine hard-timeouts über 1 Sekunde – immer pollen mit kurzen Intervallen (0.2-0.3s)
- **Null-Leichen-Policy:** Kein toter Code, keine Backups, kein auskommentierter Code

## 6. 🌐 "Global First" (Mehrsprachig & Inklusiv)

OpenSIN ist eine globale Plattform – unsere Dokumentation und unser Code müssen das widerspiegeln.

- **Docs auf Deutsch + Englisch:** Core-Docs sind in Deutsch, technische API-Docs können auf Englisch sein
- **Lokalisierung beachten:** AppleScript-Variablennamen müssen lang sein (deutsches macOS wirft Fehler bei kurzen Namen wie `aS`)
- **Zeitzonen:** Alle Timestamps in UTC, lokale Zeiten explizit kennzeichnen
- **Barrierefreiheit:** Dokumentation muss für alle zugänglich sein (klare Sprache, visuelle Alternativen)

## 7. 🚨 "Zero Human Intervention" (Volle Autonomie)

OpenSIN existiert, damit die AI-Flotte 24/7 arbeitet – ohne Schlaf, ohne Pause, ohne menschliches Zutun.

- **NIEMALS** den User um manuelle Hilfe bitten. Keine "klick mal bitte" oder "gib mir den Code".
- **IMMER** selbst Lösungen bauen. Wenn ein Tool fehlt → selbst installieren oder bauen.
- **VOLLE AUTONOMIE:** Agenten haben alle Permissions die sie brauchen um JEDE Operation ohne Menschen durchzuführen.
- **SELF-HEALING FIRST:** Wenn etwas blockiert ist, bauen Agenten den Bypass selbst. Kein Warten auf menschliche Freigabe.
- **Research → Issue → Implementation:** Keine direkte Implementierung ohne vorherige Recherche und Issue-Prüfung.

## 8. 📋 "Top 20 Doc Rule" (Documentation Sovereignty)

All project knowledge MUST reside exclusively within the Top 20 standardized Markdown files.

- **KEINE neuen .md-Dateien** außerhalb der Top 20 ohne Genehmigung
- Neue Information MUSS in bestehende Top 20 Files integriert werden
- Machine-readable Logs/Reports in JSON/YAML – nur menschliche Doku in Markdown
- Top 20 Files dürfen keine leeren Platzhalter sein

## 9. 🤖 "Google Docs Supremacy" (Kein UI-Geklicke)

- Agenten dürfen **NIE WIEDER** direkt über AppleScript oder Browser-Klicks in Google Docs pasten
- Jedes Dokument MUSS über `sin-document-forge` MCP (oder CLI) offline als `.docx` generiert werden
- Fertige `.docx` Files kommen in den lokalen Google Drive Sync-Folder
- Kein manuelles UI-Geklicke, keine unformatierten Markdown-Reste

## 10. 🔗 "No-Silo Mandate" (Self-Healing Fleet)

- JEDER Agent der einen Error, Crash oder Limitation feststellt DARF sich NICHT selbst im Silo reparieren
- **Loggen & Senden:** Umfangreiche Logs → `A2A-SIN-GitHub-Issues` → GitHub Issue → `SIN-Hermes` → Team Coder
- Jedes Problem eines einzelnen Agents wird zur Aufgabe der gesamten Coders-Flotte

## 7. 🚨 "Zero Human Intervention" (Volle Autonomie)

OpenSIN existiert, damit die AI-Flotte 24/7 arbeitet – ohne Schlaf, ohne Pause, ohne menschliches Zutun.

- **NIEMALS** den User um manuelle Hilfe bitten. Keine "klick mal bitte" oder "gib mir den Code".
- **IMMER** selbst Lösungen bauen. Wenn ein Tool fehlt → selbst installieren oder bauen.
- **VOLLE AUTONOMIE:** Agenten haben alle Permissions die sie brauchen um JEDE Operation ohne Menschen durchzuführen.
- **SELF-HEALING FIRST:** Wenn etwas blockiert ist, bauen Agenten den Bypass selbst. Kein Warten auf menschliche Freigabe.
- **Research → Issue → Implementation:** Keine direkte Implementierung ohne vorherige Recherche und Issue-Prüfung.

## 8. 📋 "Top 20 Doc Rule" (Documentation Sovereignty)

All project knowledge MUST reside exclusively within the Top 20 standardized Markdown files.

- **KEINE neuen .md-Dateien** außerhalb der Top 20 ohne Genehmigung
- Neue Information MUSS in bestehende Top 20 Files integriert werden
- Machine-readable Logs/Reports in JSON/YAML – nur menschliche Doku in Markdown
- Top 20 Files dürfen keine leeren Platzhalter sein

## 9. 🤖 "Google Docs Supremacy" (Kein UI-Geklicke)

- Agenten dürfen **NIE WIEDER** direkt über AppleScript oder Browser-Klicks in Google Docs pasten
- Jedes Dokument MUSS über `sin-document-forge` MCP (oder CLI) offline als `.docx` generiert werden
- Fertige `.docx` Files kommen in den lokalen Google Drive Sync-Folder
- Kein manuelles UI-Geklicke, keine unformatierten Markdown-Reste

## 10. 🔗 "No-Silo Mandate" (Self-Healing Fleet)

- JEDER Agent der einen Error, Crash oder Limitation feststellt DARF sich NICHT selbst im Silo reparieren
- **Loggen & Senden:** Umfangreiche Logs → `A2A-SIN-GitHub-Issues` → GitHub Issue → `SIN-Hermes` → Team Coder
- Jedes Problem eines einzelnen Agents wird zur Aufgabe der gesamten Coders-Flotte

---
*Wenn wir uns alle an diese Prinzipien halten, wird OpenSIN nicht nur die beste A2A-Plattform, sondern auch die großartigste Open-Source-Community!*
