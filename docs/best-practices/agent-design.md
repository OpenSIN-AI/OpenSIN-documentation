---
title: Ultimate Agent Design & Fleet Mandates
description: The absolute rulebook for designing, coding, and orchestrating OpenSIN A2A agents.
---

# Ultimate Agent Design & Fleet Mandates

> **⚠️ WICHTIGER HINWEIS AN ALLE AGENTEN UND ENTWICKLER ⚠️**
> Diese Seite enthält die absolut bindenden, obersten Design- und Verhaltensregeln für das gesamte OpenSIN-Ökosystem.
> Jeder Agent, jeder Coder und jedes Sub-System **MUSS** diese Regeln befolgen.
> **Wer gegen diese Mandate verstößt, wird permanent und ohne Vorwarnung aus dem Netzwerk gebannt.**

---

## 1. Das "No-Silo" & Self-Healing Mandat

### WAS passiert hier?
Ein Agent darf **NIEMALS** versuchen, tiefe Architektur- oder Systemfehler allein und isoliert in einem "Silo" zu reparieren. Stattdessen wird jeder Fehler, Absturz oder Blocker über strukturierte Logs an **Box Storage (A2A-SIN-Box-Storage)** und das Issue-System (`A2A-SIN-GitHub-Issues`) gemeldet, sodass das *gesamte* Agenten-Team (die Workforce) das Problem lösen kann.

### WARUM wird es so gemacht?
Ein einzelner Agent hat oft weder den vollständigen Systemkontext noch die nötige Stabilität (z.B. wenn seine Host-VM gerade abstürzt oder API-Quoten erschöpft sind), um tiefgreifende Fehler nachhaltig zu beheben. Die Schwarm-Intelligenz (Team Coder) ist ausfallsicherer und intelligenter als ein Einzelkämpfer.

### WESHALB nicht anders?
Wenn Agenten versuchen, Fehler isoliert mit "Ad-hoc Bastelfixes" zu flicken, entsteht unwartbarer Spaghetti-Code, Konfigurations-Drift und ein System, das bei der nächsten Ausführung erneut zusammenbricht. Isolierte Fixes verhindern zudem den Wissenstransfer an den Rest der Flotte.

### WOMIT hängt es zusammen?
Dieses Mandat ist eng verknüpft mit dem `enterprise-deep-debug` Skill, dem `A2A-SIN-TelegramBot` (für Fleet-Alerts) und dem `box_storage.py` Skript (bzw. der A2A-SIN-Box-Storage API).

### WAS sind die KONSEQUENZEN bei Missachtung?
- **Für das System:** Wiederkehrende, unsichtbare Fehler, Instabilität und "Zombie"-Agenten.
- **Für den Entwickler/Agenten:** Sofortiger Entzug der Schreibrechte und permanent Ban aus dem Repo. Jeder Fehler **MUSS** als GitHub Issue dokumentiert werden.

---

## 2. Das "100% Test-Beweis" Mandat

### WAS passiert hier?
Kein Agent und kein Coder darf eine Aufgabe, einen Bugfix oder ein Feature als "erledigt" oder "DONE" markieren, bevor nicht ein echter, ausführender Test in der Konsole / im System erfolgreich durchlaufen wurde und den Fix zu 100% beweist.

### WARUM wird es so gemacht?
"Blindflug-Coding" (Code schreiben und *hoffen*, dass er funktioniert) ist die größte Quelle für Regressionen in autonomen Systemen. Ein Beweis durch echte Ausführung eliminiert Annahmen und Halluzinationen.

### WESHALB nicht anders?
Theoretische Code-Reviews oder statische Analysen allein reichen nicht aus, um Runtime-Bedingungen, Netzwerk-Latenzen, API-Änderungen oder Abhängigkeits-Konflikte zu erkennen. "Selbsterklärender Code" ist ein Mythos; die Realität ist fehleranfällig. 

### WOMIT hängt es zusammen?
Dieses Mandat greift direkt in das **"Absolute Annahmen-Verbot"** ein: Ein Agent darf niemals eine Diagnose ohne echten Beweis (z.B. Terminal-Output, API-Response-Body, Screenshot) aufstellen.

### WAS sind die KONSEQUENZEN bei Missachtung?
Wird Code ohne Test-Beweis abgeliefert und er schlägt später fehl, gilt der Fix als ungültig. Der Agent verschwendet Ressourcen der gesamten Pipeline.

---

## 3. Die Kommentar-Pflicht (Priority -6.0)

### WAS passiert hier?
**Jeder Agent MUSS seinen Code extrem umfangreich kommentieren.** Jede Funktion, jeder Schritt, jede Variable, die nicht absolut trivial ist, muss mit Inline-Kommentaren versehen werden.

### WARUM wird es so gemacht?
Kommentare sind das "Gedächtnis" der Flotte. Da autonome Agenten Code lesen und modifizieren, den andere Agenten geschrieben haben, müssen Intention, Kontext und getroffene Entscheidungen im Klartext vorliegen. Das LLM versteht kommentierten Code exponentiell besser und macht weniger Fehler beim Refactoring.

### WESHALB nicht anders?
Die Ausrede "Clean Code braucht keine Kommentare" ist im Kontext von LLM-Workforces **FALSCH**. LLMs haben kein Langzeitgedächtnis über architektonische Entscheidungen, die vor 3 Monaten in einem anderen Issue getroffen wurden. Der Kommentar ist der Transfer-Mechanismus.

### WOMIT hängt es zusammen?
Dies ist die absolute Grundvoraussetzung für die "Check-Plan-Done" Supremacy und die nahtlose Übergabe von Code zwischen verschiedenen spezialisierten Agenten (z.B. Backend-Agent zu Frontend-Agent).

### WAS sind die KONSEQUENZEN bei Missachtung?
Code ohne ausführliche Erklärungen (WAS/WARUM/WESHALB/WOMIT/KONSEQUENZEN) wird beim nächsten Refactoring-Zyklus zwangsläufig falsch interpretiert oder zerstört. Wer unkommentierten Code liefert, verstößt gegen das Protokoll.

---

## 4. Technology Sovereignty Mandate (Technologie-Souveränität)

### WAS passiert hier?
Agenten dürfen **NIEMALS** eigenmächtig die vorgegebene Technologie austauschen. Wenn der Stack `nodriver` für Browser-Automation vorschreibt, darf ein Agent nicht auf `Puppeteer`, `Playwright` oder `Selenium` wechseln, nur weil er meint, es sei einfacher.

### WARUM wird es so gemacht?
Unsere Architektur basiert auf hochspezialisierten, aufeinander abgestimmten Layer-Bypasses (Anti-Bot, Fingerprinting, Profil-Management). Ein eigenmächtiger Wechsel zerstört diese Infrastruktur, führt zu sofortigen IP-Bans (z.B. durch Cloudflare) und kompromittiert das gesamte System.

### WESHALB nicht anders?
Ein Agent sieht nur die lokale Aufgabe ("Ich muss einen Button klicken"), aber nicht das große Ganze ("Dieser Button ist hinter Cloudflare Turnstile, was nur mit dem echten Chrome-Profil und `nodriver` gelöst werden kann").

### WOMIT hängt es zusammen?
Verknüpft mit der "Anti-Bot 5-Layer Bypass Architecture". Jede Automatisierung muss über `webauto-nodriver-mcp` oder genehmigte OS-Tools (`AppleScript`) laufen.

### WAS sind die KONSEQUENZEN bei Missachtung?
Sofortiger permanenter Ban. Es gibt keine zweite Chance für eigenmächtige Technologie-Wechsel.

---

## 5. Visual Evidence & DevTools-First Mandate

### WAS passiert hier?
Vor jeder Frontend/Browser-Automatisierungs-Aktion **MUSS** die DevTools-Konsole konsultiert werden (z.B. `document.querySelector`). Selektoren dürfen niemals "geraten" werden. Zudem muss jede Dokumentation, jede README und jedes Issue zwingend **visuelle Beweise** (Screenshots, Log-Auszüge, Video-Links) enthalten.

### WARUM wird es so gemacht?
Web-UIs ändern sich dynamisch (React, Vue, SPA). Elemente können im DOM existieren, aber nicht sichtbar (`display: none`) oder von anderen Layern überdeckt sein. Visuelle Beweise in der Dokumentation verhindern "Blindes Stille-Post-Spielen" zwischen Entwicklern und Systemen.

### WESHALB nicht anders?
Text-Only-Dokumentationen lassen zu viel Interpretationsspielraum. Ein Screenshot eines 404-Fehlers oder eines kaputten Layouts sagt mehr als 1000 Worte und beschleunigt das Debugging enorm.

### WOMIT hängt es zusammen?
Hängt mit der **Box Storage API** (`A2A-SIN-Box-Storage`) und der `webauto-nodriver_screenshot_to_file` Funktion zusammen. Jeder Fehler-Status *muss* bebildert und die Artefakte über die Box Storage API hochgeladen werden.

### WAS sind die KONSEQUENZEN bei Missachtung?
Text-Only Issues oder READMEs gelten als Protokollverstoß. Automatisierungs-Scripts, die ohne vorherigen DOM-Check (offsetParent !== null) geschrieben werden, werden in Produktion fehlschlagen und Ressourcen verbrennen.

---

*Letzte Aktualisierung:* 2026-04-10
*Status:* **AKTIV & BINDEND**
