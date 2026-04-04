# /create-github-account

GitHub Account Registrierung via Google OAuth mit Fallback.

## WANN VERWENDEN
- Wenn ein neuer GitHub Account via Google Workspace Account erstellt werden soll
- Wenn ein Agent sich bei GitHub mit einem Google Account anmelden muss
- Wenn ein bestehender GitHub Account mit diesem Google Account existiert (Fallback)

## 🚨 VORRAUSSETZUNG: CHROME MIT KRITISCHEN FLAGS 🚨

**BEVOR GitHub Signup gestartet wird MUSS Chrome mit diesen Flags laufen:**

```
--disable-features=SigninInterceptBubble,ExplicitBrowserSigninUIOnDesktop
--disable-sync
--no-first-run
--user-data-dir=/tmp/oar_openrouter_chrome_7656
```

Ohne diese Flags erscheint das native "Mein Chrome" Popup und blockiert den gesamten Flow!

Siehe `/undelete-login-google` für den kompletten Chrome-Start-Code.

## FLOW

### 1. Google muss eingeloggt sein
Stelle sicher dass Google bereits im Browser eingeloggt ist (siehe `/undelete-login-google`).

### 2. GitHub Signup
```python
from oar_steps.github_signup import github_signup_via_google

result = await github_signup_via_google(browser, email)
# result = {"status": "success", "username": "...", "email": "..."}
# ODER: {"status": "already_exists", "username": "..."}
# ODER: {"status": "already_signed_in"}
```

### 3. Ablauf im Detail
1. Navigiere zu `https://github.com/signup`
2. Schließe alle Overlays/Modals (Country Selector etc.)
3. Klicke "Continue with Google"
   - **Fallback**: Wenn Selektor nicht findet → JS click: `Array.from(document.querySelectorAll('button')).find(b => b.innerText.includes('Google')).click()`
4. Google Account Picker → Account auswählen
5. Username aus Name Generator eingeben
6. Passwort setzen
7. Account in Google Sheets loggen

### 4. Fallback: Bereits existierender Account
Wenn GitHub meldet dass der Account bereits existiert:
1. Versuche Login statt Signup
2. Navigiere zu `https://github.com/login`
3. Klicke "Sign in with Google"
4. Wähle Google Account
5. Verifiziere Login-Erfolg

### 5. Google Sheets Logging
Nach erfolgreicher Registrierung:
```
Nr | vorname | nachname | geburtsdatum | benutzername | passwort
```
Siehe Google Sheets Logging Skill für Details.

## SCREENSHOT PFLICHT
- `/tmp/github_01_signup_page.png`
- `/tmp/github_02_google_picker.png`
- `/tmp/github_03_username_page.png`
- `/tmp/github_04_final_state.png`

## LOG PFLICHT
Jeder Schritt MUSS loggen:
- URL vor und nach jeder Aktion
- Alle gefundenen/nicht-gefundenen Elemente
- Tab-Anzahl im Browser
- Seite-Text Vorschau (erste 200 chars)
- Screenshot bei jedem FAIL
