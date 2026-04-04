# /undelete-login-google

Automatisierte Wiederherstellung gelöschter Google Workspace Accounts und Login in Chrome.

## WANN VERWENDEN
- Wenn ein alter Google Workspace Account (@zukunftsorientierte-energie.de) wiederhergestellt werden muss
- Wenn ein Agent einen Google Account in Chrome eingeloggt braucht
- Wenn Google Account-Erstellung blockiert ist (412 "abusive behavior")

## KRITISCHE INFOS
- Google Workspace Domain: `zukunftsorientierte-energie.de`
- Rotator Passwort: `ZOE.jerry2024`
- Chrome Port für Rotator: `7656`
- Mindestante für Restore: 170 Stunden (7 Tage)

## 🚨 CHROME START MIT KRITISCHEN FLAGS (DAMIT GOOGLE LOGIN FUNKTIONIERT) 🚨

**OHNE DIESE FLAGS SCHLÄGT DER GOOGLE LOGIN FEHLER!**

Das native "Mein Chrome" / "In Chrome anmelden?" Popup blockiert den Login. Diese Flags unterdrücken es:

```python
import subprocess, os, signal, shutil, time, urllib.request
from pathlib import Path

CHROME_BINARY = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
LOGIN_PROFILE = Path("/tmp/oar_openrouter_chrome_7656")
LOGIN_PID = Path("/tmp/oar_openrouter_chrome_7656.pid")
PORT = 7656

def launch_chrome():
    # Kill existing Chrome on port
    if LOGIN_PID.exists():
        try:
            pid = int(LOGIN_PID.read_text().strip())
            os.killpg(pid, signal.SIGTERM)
            time.sleep(0.5)
            try: os.killpg(pid, signal.SIGKILL)
            except: pass
        except: pass
        LOGIN_PID.unlink(missing_ok=True)
    
    # Fresh profile
    if LOGIN_PROFILE.exists():
        shutil.rmtree(LOGIN_PROFILE, ignore_errors=True)
    LOGIN_PROFILE.mkdir(parents=True, exist_ok=True)
    
    proc = subprocess.Popen(
        [
            CHROME_BINARY,
            f"--remote-debugging-port={PORT}",
            f"--user-data-dir={LOGIN_PROFILE}",
            "--no-first-run",
            "--no-default-browser-check",
            "--disable-extensions",
            "--disable-default-apps",
            "--disable-background-networking",
            "--disable-sync",
            "--hide-crash-restore-bubble",
            # KRITISCH: Unterdrückt natives "Mein Chrome" Sync Popup
            "--disable-features=SigninInterceptBubble,ExplicitBrowserSigninUIOnDesktop",
            "about:blank",
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        start_new_session=True,
    )
    LOGIN_PID.write_text(str(proc.pid))
    
    # Wait for Chrome ready
    for _ in range(40):
        if proc.poll() is not None:
            raise RuntimeError(f"Chrome exited early (code {proc.poll()})")
        try:
            with urllib.request.urlopen(f"http://127.0.0.1:{PORT}/json/version", timeout=1):
                return
        except: pass
        time.sleep(0.5)
    proc.kill()
    raise RuntimeError(f"Chrome not ready on port {PORT}")
```

**WICHTIGSTE FLAGS:**
- `--disable-features=SigninInterceptBubble,ExplicitBrowserSigninUIOnDesktop` → Unterdrückt natives Chrome Sync Popup
- `--disable-sync` → Verhindert Sync-Vorschläge
- `--no-first-run` → Kein Willkommens-Screen
- `--user-data-dir=/tmp/...` → Frisches Profil, keine alten Sessions

## FLOW

### 1. Account wiederherstellen
```python
import sys
sys.path.insert(0, '/Users/jeremy/.open-auth-rotator/antigravity')
from core.workspace_restore import restore_deleted_workspace_user

user = restore_deleted_workspace_user()
email = user["email"]
print(f"Restored: {email}")
```

### 2. Chrome starten (MIT FLAGS!)
```python
from oar_steps.chrome import launch_chrome, connect_browser

launch_chrome()  # Port 7656, MIT kritischen Flags!
browser = await connect_browser()
```

### 3. Google Login
```python
from oar_steps.google_login import google_login

ok = await google_login(browser, email, "ZOE.jerry2024")
if not ok:
    print("Google login failed!")
```

### 4. Verifizieren
```python
current_url = browser.tabs[0].url or ""
assert "myaccount.google.com" in current_url
print(f"Logged in: {current_url}")
```

## GOOGLE LOGIN DETAILS

Der Login verwendet nodriver mit diesen Schritten:
1. Navigiere zu `https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn`
2. Finde `input[type='email']` → Email eingeben
3. Klicke `#identifierNext` oder Enter
4. Finde `input[type='password']` → Passwort eingeben
5. Klicke `#passwordNext` oder Enter
6. Warte auf `myaccount.google.com` oder `mail.google`

**Fallbacks:**
- Wenn "Anderes Konto verwenden" erscheint → klicken
- Wenn TOS/Willkommen erscheint → akzeptieren
- Wenn Challenge/2FA → Screenshot speichern und fehlschlagen

## FEHLERBEHEBUNG

| Fehler | Lösung |
|--------|--------|
| 412 "abusive behavior" | Deleted Account Restore verwenden |
| 404 "userKey not found" | Account ist zu alt (>20 Tage), anderen versuchen |
| Chrome startet nicht | `pkill -f chrome` dann neu starten |
| Login scheitert | Passwort reset: `update_workspace_password(email, "ZOE.jerry2024")` |
| "Mein Chrome" Popup | Flags fehlen! `--disable-features=SigninInterceptBubble,ExplicitBrowserSigninUIOnDesktop` |
| Login landet auf signin | Chrome Profil war nicht frisch → `/tmp/oar_*` löschen |

## SCREENSHOT PFLICHT
Nach JEDEM Schritt Screenshot speichern:
- `/tmp/undelete_01_before.png`
- `/tmp/undelete_02_after_restore.png`
- `/tmp/undelete_03_google_login.png`
- `/tmp/undelete_04_after_login.png`
- `/tmp/undelete_05_final_state.png`

## LOG PFLICHT
Jeder Schritt MUSS loggen:
- URL vor und nach jeder Aktion
- Alle gefundenen/nicht-gefundenen Elemente
- Tab-Anzahl im Browser
- Seite-Text Vorschau (erste 200 chars)
- Screenshot bei jedem FAIL und kritischem OK
