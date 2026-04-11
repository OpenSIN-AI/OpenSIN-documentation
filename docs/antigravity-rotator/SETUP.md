# ⚙️ Setup & Konfiguration

Damit der `antigravity-rotator` vollautomatisch arbeiten kann, benötigt er Administrator-Zugriff auf die Google Workspace Umgebung.

**WICHTIG:** Ein normaler API-Key (beginnt mit `AIzaSy...`) reicht für das Admin SDK **nicht** aus! Das Admin SDK benötigt zwingend eine Service Account JSON-Datei mit OAuth2 "Domain-Wide Delegation".

## 1. Google Workspace Service Account JSON erstellen (Mini-Guide)

Folge diesen exakten Schritten, um die benötigte `.json` Datei in unter 2 Minuten zu erstellen:

### Schritt A: Admin SDK API aktivieren
1. Öffne diesen Link: [Admin SDK API aktivieren](https://console.cloud.google.com/apis/api/admin.googleapis.com/metrics?authuser=1&hl=de)
2. Wähle oben dein Cloud-Projekt aus (z.B. `antigravity-rotator`).
3. Klicke auf den blauen Button **"Aktivieren"**.

### Schritt B: Service Account (Anmeldedaten) erstellen
1. Öffne diesen Link: [Anmeldedaten erstellen](https://console.cloud.google.com/apis/credentials?authuser=1&hl=de)
2. Klicke oben auf **"+ Anmeldedaten erstellen"** ➔ wähle **"Dienstkonto"** (Service Account).
3. Gib einen Namen ein (z.B. `rotator-admin`) und klicke auf "Erstellen und Fortfahren".
4. Bei "Rolle wählen" suche nach **"Workspace Administrator"** (oder gewähre Projekt-Inhaber Rechte) und klicke auf "Fertig".

### Schritt C: JSON-Schlüssel herunterladen
1. Du siehst nun dein neues Dienstkonto unten in der Liste. Klicke auf die E-Mail-Adresse des Dienstkontos.
2. Gehe oben auf den Reiter **"Schlüssel"** (Keys).
3. Klicke auf **"Schlüssel hinzufügen"** ➔ **"Neuen Schlüssel erstellen"**.
4. Wähle **"JSON"** und klicke auf "Erstellen".
5. Die `.json`-Datei wird jetzt auf deinen Mac heruntergeladen!

### Schritt D: Domain-Wide Delegation im Workspace (WICHTIG!)
Damit das Dienstkonto deine Nutzer verwalten darf, muss es im Workspace freigeschaltet werden:
1. Kopiere die `Client-ID` (Einzigartige ID) deines neuen Dienstkontos aus der Google Cloud Console.
2. Gehe ins Google Workspace Admin Center: [admin.google.com](https://admin.google.com)
3. Gehe zu **Sicherheit** ➔ **Zugriffs- und Datensteuerung** ➔ **API-Steuerung** ➔ **Domainweite Delegierung verwalten**.
4. Füge einen neuen API-Client hinzu:
   - **Client-ID:** Die kopierte Nummer eintragen.
   - **OAuth-Bereiche:** `https://www.googleapis.com/auth/admin.directory.user`
5. Speichern.

### Schritt E: JSON Datei am richtigen Ort ablegen
Lege die heruntergeladene JSON-Datei auf deinem Mac exakt hier ab:
`~/.config/opencode/auth/google/zoe-admin-sdk-api.json`

*(Hinweis: Den Ordner `~/.config/opencode/auth/google/` musst du vorher eventuell erstellen).*

---

## 2. Umgebungsvariablen (Optional)
Der Rotator ist "Convention over Configuration". Falls Pfade abweichen, können diese in der `~/.zshrc` oder im LaunchAgent überschrieben werden:

| Variable | Default | Beschreibung |
|----------|---------|--------------|
| `ROTATOR_LOG_DIR` | `~/.local/share/opencode/log` | Pfad zu den Opencode Logs |
| `ROTATOR_DOMAIN` | `zukunftsorientierte-energie.de` | Die Workspace-Domain |
| `ROTATOR_PREFIX` | `rotator-` | Präfix für die Rotator-Accounts |
| `ROTATOR_PASSWORD` | `ZOE.jerry2024` | Passwort für wiederhergestellte Rotatoren |
| `ROTATOR_ADMIN` | `info@zukunftsorientierte-energie.de` | Der echte Workspace Admin |

