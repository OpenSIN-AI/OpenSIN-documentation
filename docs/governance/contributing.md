# 🤝 Mitwirken bei OpenSIN (Contributing)

Wir freuen uns riesig über deinen Beitrag zu **OpenSIN**! Egal ob du einen Bug gefunden hast, eine neue Funktion für den Marktplatz (z. B. `Team-SIN-Google`) bauen willst, oder unsere Dokumentation verbesserst – du bist herzlich willkommen.

Damit die Zusammenarbeit für alle reibungslos und super professionell (Enterprise-Niveau!) abläuft, beachte bitte diese einfachen Best Practices.

---

## 1. Visuals First! 📸🎥

Wir lieben Bilder, Screenshots und kleine Screen-Recordings.

- **Bug-Reports:** Füge einen Screenshot vom Terminal-Error oder vom Browser (mit offener DevTools-Konsole) hinzu.
- **Neue Features:** Füge ein kleines Video (10-30 Sekunden) deines Features in den Pull Request ein.
- **Architektur-Änderungen:** ASCII-Diagramme oder Bilder sind Pflicht.
- **Dokumentation:** Jeder neue Abschnitt braucht mindestens ein visuelles Element.

## 2. Der GitHub Workflow

### Schritt-für-Schritt

1. **Issue erstellen:** Diskutiere deine Idee oder den Bug erst im Repository (z. B. in `OpenSIN-Code` oder im `OpenSIN` UI-Repo).
2. **Branch erstellen:** Nutze sprechende Namen mit Conventional Commits Prefix:
   - `feat/team-sin-apple` – Neues Feature
   - `fix/dashboard-login` – Bug-Fix
   - `docs/a2a-fleet-update` – Dokumentation
   - `chore/dependency-updates` – Wartung
3. **Code schreiben:** Halte dich an unsere [Best Practices](./best-practices.md) und den [global-dev-docs-standard](https://github.com/OpenSIN-AI/global-dev-docs-standard).
4. **Tests schreiben:** Neue Features brauchen Tests (siehe [Testing Standards](./best-practices.md#4--testing)).
5. **Lokal testen:** `npm test` / `bun test` / `pytest` – je nach Projekt.
6. **PR eröffnen:** Mit visueller Dokumentation und klarer Beschreibung.

### PR-Beschreibung Template

```markdown
## Description
Was macht dieser PR?

## Related Issue
Closes #123

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Tests pass
- [ ] Manual testing completed

## Screenshots
(Füge hier Screenshots/Videos ein)
```

## 3. Code Style

### TypeScript/JavaScript
- TypeScript bevorzugen
- JSDoc/TSDoc auf allen exportierten Funktionen
- ESLint Config: `@opensin/eslint-config`
- Keine `console.log` in Production-Code

### Python
- Type Hints auf allen Funktionen
- Docstrings im Google-Style
- `ruff` oder `flake8` für Linting
- `pytest` für Tests

### Allgemein
- Bestehende Patterns im Codebase folgen
- Keine hardcoded Secrets
- Keine auskommentierten Code-Blöcke (Null-Leichen-Policy!)
- Max 30 Zeilen pro Micro-Script (Browser-Automatisierung)

## 4. Jedes Tool braucht eine Readme!

Arbeitest du am `OpenSIN-Code` Repository (z. B. an einem neuen MCP oder Skill)?

- Erstelle **immer** eine eigene `README.md` direkt im Unterordner des Tools.
- Mache sie anfängerfreundlich: Einleitungssatz, Screenshot/Video, Befehl zum Ausführen.
- Jeder Quereinsteiger soll sofort "Danke!" sagen, wenn er dein Tool sieht.

**README-Template für Plugins/MCPs/Skills:**
```markdown
# Plugin-Name

> Einzeiler: Was macht dieses Plugin?

## Quickstart
\`\`\`bash
# Installation
# Ausführung
\`\`\`

## Screenshot/GIF
![Plugin in action](./screenshot.png)

## Konfiguration
\`\`\`json
{ ... }
\`\`\`
```

## 5. Review-Prozess

### Bevor du einen PR eröffnest
- [ ] Tests lokal ausgeführt
- [ ] Linter lokal ausgeführt
- [ ] Eigenen Code zuerst selbst reviewed
- [ ] Screenshots/Videos für visuelle Änderungen
- [ ] CHANGELOG.md aktualisiert (wenn relevant)

### Reviewer-Checklist
- [ ] Code lesbar und gut organisiert
- [ ] Keine hardcoded Secrets
- [ ] Error Handling adäquat
- [ ] Tests coveren die Änderungen
- [ ] Dokumentation aktualisiert
- [ ] Keine unnötigen Dependencies

### Response Times
| Typ | Zeit |
|-----|------|
| Critical Bugs | Innerhalb 2 Stunden |
| Features | Innerhalb 24 Stunden |
| Documentation | Innerhalb 48 Stunden |

## 6. Marketing & Diskussionen 💬

Hast du Ideen für unsere Abo-Modelle auf `MyOpenSIN` (z. B. Preisgestaltung für `Team-SIN-BugBounty`) oder möchtest du beim Marketing helfen?

- Besuche unsere [GitHub Discussions](https://github.com/orgs/OpenSIN-AI/discussions) im Repo `OpenSIN-Marketing-Strategy`.
- Teile deine Gedanken, wir sind eine offene und transparente Community!

## 7. Dokumentation aktualisieren

Dokumentation MUSS aktualisiert werden bei:
- API-Änderungen
- Konfigurationsänderungen
- Setup-Prozess-Änderungen
- Architektur-Änderungen
- Dependency-Änderungen

---

> **Wir sind ein Team:** Wenn du irgendwo nicht weiterkommst, frag einfach in den Discussions nach. Wir bauen hier gemeinsam die fortschrittlichste und benutzerfreundlichste KI-A2A-Plattform!

### 🔗 Verknüpfte Dokumentation

- [Best Practices](./best-practices.md) – Sicherheit, Testing, CI/CD
- [Core Principles](./core-principles.md) – Unsere Leitlinien
- [Global Dev Docs Standard](https://github.com/OpenSIN-AI/global-dev-docs-standard) – Dokumentationsstandard
