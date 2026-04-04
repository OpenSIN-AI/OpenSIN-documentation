# 🚀 Dein erster Tag bei OpenSIN (Getting Started)

Herzlichen Glückwunsch, du bist jetzt Teil der OpenSIN-Familie! Wir haben diesen Guide extrem benutzerfreundlich gestaltet, damit du in 15 Minuten deinen ersten Erfolg feiern kannst.

## 🎯 1. Was bauen wir?

Wir bauen **OpenSIN**, eine Open-Source Agent-to-Agent (A2A) Plattform.
*   **Für die Community:** Open-Source-Version (Dashboard: `a2a.delqhi.com`, zukünftig `chat.opensin.ai`).
*   **Für Enterprise:** `MyOpenSIN` (Abo-Version, wo Nutzer A2A-Teams wie *Team-SIN-Google* oder *Team-SIN-BugBounty* abonnieren).
*   **Das Fleet:** 130+ autonome Agenten in 8 Kategorien (Infrastructure, Teams, Apple, Security, Code, Social/Comms, Legal/Finance, Specialized).

## 🛠️ 2. Deine Arbeitsumgebung (Setup)

1.  **Clone die Kern-Repositories:**
    ```bash
    git clone https://github.com/OpenSIN-AI/OpenSIN.git
    git clone https://github.com/OpenSIN-AI/OpenSIN-backend.git
    git clone https://github.com/OpenSIN-AI/OpenSIN-Code.git
    git clone https://github.com/OpenSIN-AI/OpenSIN-documentation.git
    ```

2.  **Verstehe den Standard:**
    Wir schreiben Docs auf Enterprise-Niveau. Schau dir dafür kurz [global-dev-docs-standard](https://github.com/OpenSIN-AI/global-dev-docs-standard) an.

3.  **Installiere die Basis:**
    ```bash
    curl -fsSL https://raw.githubusercontent.com/OpenSIN-AI/OpenSIN-backend/main/install.sh | bash
    ```

4.  **Starte OpenSIN-Code (Die Kommandozeile):**
    Wechsle in das `OpenSIN-Code` Verzeichnis und lies dort die Haupt-`readme.md`. Sie zeigt dir Schritt für Schritt, wie du die CLI startest.

5.  **Optional: VS Code Extension (SIN Code):**
    Installiere die [SIN Code Extension](./opensin-vscode-extension/README.md) für agentic AI coding direkt in VS Code.

## 📸 3. Mach ein Beweisfoto!

Hast du das Setup erfolgreich abgeschlossen? Perfekt!
Wir lieben visuelle Bestätigungen. So gehst du vor:

1. **Terminal-Screenshot:** Mache einen Screenshot deines Terminals, das die erfolgreiche Installation zeigt (z. B. die Ausgabe von `opencode --version`).
2. **Dashboard-Check:** Öffne `a2a.delqhi.com` im Browser und stelle sicher, dass du dich einloggen kannst.
3. **PR-Anhang:** Wenn du deinen ersten Pull Request erstellst, hänge beide Screenshots an. Das zeigt dem Reviewer sofort: "Es klappt!"

**Beispiel für einen erfolgreichen Check:**
```bash
$ opencode --version
opencode 0.x.x
```

## 🗺️ 4. Nächste Schritte

| Schritt | Dokumentation | Dauer |
|---------|--------------|-------|
| Architektur verstehen | [Architektur & Repositories](./architecture.md) | 10 Min |
| A2A Fleet kennenlernen | [A2A Fleet](./a2a-fleet.md) | 15 Min |
| Best Practices lesen | [Best Practices & Sicherheit](./best-practices.md) | 10 Min |
| OpenSIN-Code Struktur | [OpenSIN-Code](./opensin-code.md) | 10 Min |
| OMOC Swarm verstehen | [OMOC Swarm](./omoc-swarm.md) | 10 Min |
| Mitwirken | [Contributing](./contributing.md) | 5 Min |

---
*Bist du bereit? Dann schau dir als Nächstes die [Architektur](./architecture.md) an, um zu verstehen, wie unsere Websites, das Backend, die CLI und das A2A Fleet zusammenarbeiten.*
