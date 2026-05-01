---
title: Ultimate Browser Automation & Anti-Bot Bypass
description: The mandatory protocols for web interactions, DevTools-first coding, and evading bot detection.
---

# Ultimate Browser Automation & Anti-Bot Bypass

> **⚠️ WICHTIGER HINWEIS AN ALLE AGENTEN UND ENTWICKLER ⚠️**
> Diese Seite definiert die **EINZIG ERLAUBTEN** Methoden zur Interaktion mit Webseiten.
> Wer bei einer Web-Aufgabe eigenmächtig auf veraltete Tools wie Puppeteer oder Selenium zurückgreift,
> oder CSS-Selektoren "rät", anstatt sie in den DevTools zu verifizieren, **fliegt permanent aus dem Netzwerk.**

---

## 1. Technology Sovereignty Mandate (Priority -2)

### WAS passiert hier?

Alle Web-Interaktionen, Logins, Captcha-Lösungen und Scraping-Aufgaben müssen **AUSSCHLIESSLICH** über `nodriver`, `skylight-cli-mcp`, `CDP` (Chrome DevTools Protocol) oder `curl_cffi` (für TLS-Spoofing) erfolgen.

### WARUM wird es so gemacht?

`nodriver` steuert den Browser nicht über den erkennbaren WebDriver-Port, sondern klinkt sich nativ in den Browser ein. Es nutzt das **echte** Chrome-Profil des Nutzers, inklusive all seiner echten Cookies, History und Session-Tokens. Cloudflare und andere WAFs (Web Application Firewalls) stufen diese Interaktionen als "menschlich" ein.

### WESHALB nicht anders?

Frameworks wie **Playwright, Puppeteer oder Selenium** setzen ein `webdriver: true` Flag im Browser-Fingerprint. Cloudflare Turnstile, DataDome und reCAPTCHA erkennen dies in Millisekunden und blockieren die IP (`403 Forbidden` oder Endlos-Captchas). Auch "Camoufox" oder andere Firefox-basierte Tarnkappen sind streng verboten, da sie unser Chrome-Profil-Ökosystem (Password-Manager, gespeicherte Sessions) brechen.

### WOMIT hängt es zusammen?

- **skylight-cli-mcp**: Unser zentrales MCP-Tool für alle Agenten.
- **Chrome Profile Regel**: Die Automation _muss_ in einem eingeloggten Profil stattfinden.

### WAS sind die KONSEQUENZEN bei Missachtung?

- Ein Agent, der Playwright `npm install playwright` ausführt, verliert sofort seine Schreibrechte.
- Das Projekt wird von Cloudflare gebannt, die IP verbrannt, und potenzielle Bug-Bounties oder Freelance-Jobs gehen verloren.

---

## 2. DevTools-First Mandate (Priority -1)

### WAS passiert hier?

Vor **JEDEM** Klick, **JEDEM** Ausfüllen eines Formulars und **JEDEM** geschriebenen CSS-Selektor **MUSS** der Agent die Chrome DevTools (Console, Elements, Network) konsultieren, um die Annahme zu verifizieren.

1. **Elements-Tab**: Exakte HTML-Struktur inkl. `id`, `class`, `data-*` prüfen.
2. **Console**: `document.querySelector('.dein-selektor')` ausführen. Wenn `null` zurückkommt → **STOP**. Falscher Selektor.
3. **Sichtbarkeits-Check**: `element.offsetParent !== null` und `window.getComputedStyle(el).display` prüfen.
4. **Console Errors**: Alle JS-Errors _vor_ dem Klick lesen!

### WARUM wird es so gemacht?

Moderne Webseiten (React, Vue, SPAs) generieren dynamische Klassen (z.B. `.btn-xk29a`), verstecken Elemente hinter Overlays (`display: none`) oder fangen Klicks über unsichtbare `<div>`-Layer ab. Ein LLM-Agent, der Selektoren aus seinem Trainingsdaten-Gedächtnis "rät" (z.B. `button[type="submit"]`), klickt oft ins Leere oder löst React-Fehler aus.

### WESHALB nicht anders?

Blindes Automatisieren ("Fire and Forget") führt zu Scripts, die beim ersten Run funktionieren und beim zweiten (weil der DOM langsamer lädt) crashen. Ein Skript, das nicht dynamisch den echten DOM-Status ausliest, ist unzuverlässig.

### WOMIT hängt es zusammen?

Das **Visual Evidence Mandate**: Bei jedem `FAIL` und bei jedem kritischen Schritt muss ein Screenshot (`/tmp/mXX_stepname_RESULT.png`) gemacht werden. Die DevTools-Ausgabe (via CDP `Runtime.exceptionThrown`) muss geloggt werden.

### WAS sind die KONSEQUENZEN bei Missachtung?

- Wer einen CSS-Selektor in ein Skript schreibt, ohne den Console-Beweis vorzulegen, begeht einen Protokollverstoß.
- Klicks ins Leere verursachen Timeout-Loops, die teure Compute-Ressourcen binden.

---

## 3. Die strikte Chrome Profile Regel

### WAS passiert hier?

Es gibt genau dokumentierte Chrome-Profile, die für spezifische Aufgaben reserviert sind. Es darf **NIEMALS** ein leeres, temporäres Profil (`user_data_dir=None`) für Bot-Aufgaben verwendet werden!

| Profil           | Email                                   | WANN NUTZEN                                                                     |
| ---------------- | --------------------------------------- | ------------------------------------------------------------------------------- |
| **Geschäftlich** | `info@zukunftsorientierte-energie.de`   | **NUR** für Google Admin Console, Domain-Wide Delegation, Workspace Management. |
| **Default**      | `zukunftsorientierte.energie@gmail.com` | **NUR** privat/Agent-Work. Niemals für Admin-Tasks!                             |
| **Profile X**    | div.                                    | Spezifische Agenten-Aufgaben (z.B. Bug-Bounties).                               |

### WARUM wird es so gemacht?

Die Trennung der Profile verhindert Session-Hijacking zwischen Projekten und schützt kritische Infrastruktur (Google Admin). Zudem sind die Profile bereits durch manuelle Logins mit Trust-Cookies (Google OAuth, Cloudflare Clearance) aufgeladen.

### WESHALB nicht anders?

Ein neues, leeres Profil hat keine Cookie-Historie. Wenn ein Agent mit einem leeren Profil auf eine stark geschützte Seite zugreift, wird er zu 100% als Bot eingestuft und mit Captchas blockiert.

### WOMIT hängt es zusammen?

- **Nur EINE Session pro Profil!** Ein Profil-Verzeichnis (z.B. `/Default`) ist exklusiv gelockt, sobald Chrome läuft. Ein Agent darf niemals versuchen, eine zweite Instanz auf dasselbe Profil zu erzwingen (führt zu WindowServer-Sperren auf macOS). Er muss sich via CDP in die _existierende_ Instanz einklinken oder einen anderen Port / ein anderes freies Profil nutzen.

### WAS sind die KONSEQUENZEN bei Missachtung?

- Nutzung des "Default"-Profils für Admin-Tasks: **SOFORTIGER BAN**.
- Überschreiben von Trust-Cookies durch "Clean State" Neustarts: Verlust des hart erarbeiteten Bot-Trust-Scores.

---

## 4. Anti-Bot 5-Layer Bypass Architecture (2026)

### WAS passiert hier?

Für alle Geld-verdienenden Agenten (Freelancing, Bug-Bounties, Surveys) muss diese Architektur implementiert werden:

1. **Layer 1: IP Reputation** → Niemals direkte OCI/Datacenter-IPs für Ziel-Webseiten nutzen. Immer Residential/Mobile-Proxys vorschalten.
2. **Layer 2: TLS Fingerprint (JA3/JA4)** → HTTP-Requests erfolgen über `curl_cffi` (impersonate Chrome) oder nativ über `nodriver`.
3. **Layer 3: Browser Fingerprint** → `nodriver` mit `headless=False` (Pflicht!) und echtem macOS/Windows User-Agent.
4. **Layer 4: Behavioral Analysis** → Nutzung von Human-Emulation-Layers (zufällige Pausen, Maus-Kurven, Scroll-Delays). Niemals 5 Formularfelder in 0.01 Sekunden ausfüllen.
5. **Layer 5: Active Challenges** → Persistente Sessions (Cookies speichern) zur Wiederverwendung.

### WARUM wird es so gemacht?

Plattformen wie Prolific, Outlier, HackerOne oder Upwork nutzen militärische Bot-Erkennung. Fällt der Agent nur auf einem dieser Layer durch, wird das Konto sofort gesperrt und die Einnahmequelle ist tot.

---

_Letzte Aktualisierung:_ 2026-04-10
_Status:_ **AKTIV & BINDEND**
_Verantwortlich:_ sin-zeus
