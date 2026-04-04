# 🔄 Auth Rotator Systeme

OpenSIN betreibt zwei autonome Auth-Rotationssysteme, die Model-Quota-Erschöpfung erkennen und automatisch neue Accounts provisionieren.

## 1. openAntigravity-auth-rotator

**Zweck:** Automatisches Rotieren von Google Workspace Accounts wenn Antigravity-Model-Quotas (Claude + Gemini) erschöpft sind.

**Repository:** [OpenSIN-AI/openAntigravity-auth-rotator](https://github.com/OpenSIN-AI/openAntigravity-auth-rotator)

### Architektur

```
┌──────────────────────────────────────────────────────┐
│              openAntigravity-auth-rotator             │
├──────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌──────────────┐  ┌────────────┐ │
│  │   Watcher   │  │  Orchestrator│  │   Steps    │ │
│  │ (LaunchAgent│→ │   (runner.py)│→ │  (atomic)  │ │
│  │  plist)     │  │              │  │  ≤20 lines │ │
│  └─────────────┘  └──────────────┘  └────────────┘ │
│         │                │                 │         │
│  iTerm2 Scan      VTP Runner      Workspace API     │
│  Pattern Match    Chrome mgmt     Browser Auth      │
│  Notification     Step exec       Token Exchange    │
└──────────────────────────────────────────────────────┘
```

### Funktionsweise

1. **Watcher** scannt iTerm2 Scrollback auf Quota-Exhaustion-Patterns
2. **Orchestrator** startet die Visual Truth Protocol (VTP) Step-Pipeline
3. **Steps** sind atomare Micro-Skripte (≤20 Zeilen, 1 Aktion = 1 Datei)
4. **Browser-Automation** via nodriver (Chrome, kein Playwright/Docker)
5. **Token Exchange** injiziert neue Credentials in `antigravity-accounts.json`
6. **Session Resume** schickt "mach weiter" an alle betroffenen iTerm2-Sessions

### Model-Kompatibilität

| Modell | Status | Hinweise |
|--------|--------|----------|
| `antigravity-claude-sonnet-4-6` | ✅ Works | Primary model, quota resets ~weekly |
| `antigravity-claude-opus-4-6-thinking` | ✅ Works | Higher tier, separate quota |
| `antigravity-gemini-3-flash` | ✅ Works | Fallback model |
| `antigravity-gemini-3.1-pro` | ⚠️ 404 | Plugin sends wrong model ID (`-preview` suffix) |
| `antigravity-gemini-3.1-pro-low` | ✅ Works | Correct resolved name |
| `gemini-2.5-flash` | ✅ Works | Available on free tier |
| `gemini-2.5-pro` | ⚠️ 503 | Capacity issues |

### Bekannte Bugs (Dokumentiert)

| Bug | Beschreibung | Status |
|-----|-------------|--------|
| RBUG-017 | Managed Project ID Provisioning | ✅ Fixed |
| RBUG-018 | AppleScript→TTY writes on macOS 26 | ✅ Fixed (use AppleScript `write text`) |
| RBUG-019 | In-memory cache after account update | ✅ Fixed (restart opencode processes) |
| RBUG-022 | Soft quota threshold (90%) | ✅ Fixed (`antigravity.json` config) |
| RBUG-023 | Phantom 404 on gemini-3.1-pro | ✅ Fixed (use `-low` suffix) |
| RBUG-024 | Zombie opencode processes | ✅ Fixed |
| RBUG-027 | ms03 blank session (missing `--continue`) | ✅ Fixed |
| RBUG-028 | Duplicate watcher processes | ✅ Fixed |
| RBUG-029 | Stale lock files | ✅ Fixed |
| RBUG-030 | gemini-3.1-pro entity not found | ✅ Fixed |
| RBUG-031 | Double log writes | ✅ Fixed |
| RBUG-032+ | Chrome launch, rotation, session bugs | ✅ Fixed |

### Konfiguration

```json
// ~/.config/opencode/antigravity.json
{
  "soft_quota_threshold_percent": 100,
  "cli_first": false,
  "quota_fallback": false
}
```

---

## 2. opencodex-auth-rotator

**Zweck:** Automatisches Rotieren von OpenAI Accounts wenn GPT-Model-Quotas erschöpft sind.

**Repository:** [OpenSIN-AI/opencodex-auth-rotator](https://github.com/OpenSIN-AI/opencodex-auth-rotator)

### Architektur

```
┌──────────────────────────────────────────────────────┐
│               opencodex-auth-rotator                  │
├──────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌──────────────┐  ┌────────────┐ │
│  │   Guard     │  │   Rotator    │  │   Steps    │ │
│  │ (LaunchAgent│→ │  (main.py)   │→ │  (atomic)  │ │
│  │  plist)     │  │              │  │  ≤30 lines │ │
│  └─────────────┘  └──────────────┘  └────────────┘ │
│         │                │                 │         │
│  Auth.json Check  Registration    temp-mail.org    │
│  Single Trigger   Pipeline        nodriver/Chrome  │
│  No GPT Test      Token Exchange  DOM Validation   │
└──────────────────────────────────────────────────────┘
```

### Pipeline-Schritte (17 Steps)

| Step | Datei | Aktion |
|------|-------|--------|
| s01 | `s01_nav_oauth.py` | Navigiere zu OAuth-Seite |
| s02 | `s02_click_signup.py` | Klicke Signup |
| s03 | `s04_click_continue_email.py` | Email-Login wählen |
| s04 | `s06_fill_password.py` | Passwort eingeben |
| s05 | `s07_click_weiter_pw.py` | Weiter klicken |
| s06 | `s08_wait_email_page.py` | Auf Email-Seite warten |
| s07 | `s09_poll_otp.py` | OTP von temp-mail.org abholen |
| s08 | `s10_fill_otp.py` | OTP eingeben |
| s09 | `s10b_submit_otp.py` | OTP absenden |
| s10 | `s10c_wait_about_page.py` | Auf About-You-Seite warten |
| s11 | `s11_fill_name.py` | Name eingeben |
| s12 | `s12_fill_birthday.py` | Geburtstag eingeben (Spinbuttons) |
| s13 | `s13_click_about_continue.py` | Weiter auf About-Seite |
| s14 | `s14_consent.py` | Consent-Seite bestätigen |
| s15 | `s15_token_exchange.py` | Token austauschen |

### LaunchAgents

Beide Rotator-Systeme sind über LaunchAgents getrennt:

| LaunchAgent | Projekt | Plist |
|-------------|---------|-------|
| `com.openAntigravity.ratelimit-watcher` | openAntigravity-auth-rotator | `~/Library/LaunchAgents/` |
| `com.opencode.auth-guard` | opencodex-auth-rotator | `~/Library/LaunchAgents/` |

### Hammerspoon Shortcuts

Globale Tastenkürzel zum manuellen Triggern:

| Shortcut | Aktion |
|----------|--------|
| `⌘R→C` | opencodex-auth-rotator starten |
| `⌘R→A` | openAntigravity-auth-rotator starten |

---

## 3. HuggingFace Token Management

OpenSIN verwaltet mehrere HuggingFace Accounts für Space-Deployment und API-Zugriff. Tokens werden über sin-passwordmanager verwaltet und im macOS Keychain gespeichert.

### HF Account Registry

| ID | Account | Token Prefix | Zweck | Status |
|----|---------|-------------|-------|--------|
| HF_TOKEN_1 | OpenJerro | `hf_QZEaRY...` | Primary delqhi Org Spaces | ✅ Valid |
| HF_TOKEN_2 | mazingaimaze | - | Secondary Spaces | 📋 Keychain |
| HF_TOKEN_3 | funviral | - | Secondary Spaces | 📋 Keychain |
| HF_TOKEN_4 | lolitaexibabe | - | Secondary Spaces | 📋 Keychain |
| HF_TOKEN_5 | Mulimul | - | Secondary Spaces | 📋 Keychain |
| HF_TOKEN_6 | appimepp | - | Secondary Spaces | 📋 Keychain |
| HF_TOKEN_7 | - | - | Secondary Spaces | 📋 Keychain |
| HF_API_9 | easeeeclip | `hf_XIVHYl...` | Platform Agents (8 Spaces) | ✅ Valid |

### HF_API_9 (easeeeclip) — Platform Agent Spaces

Erstellt am 2026-04-04. Spaces unter `easeeeclip/` erstellt:

| Space | URL | Status |
|-------|-----|--------|
| sin-reddit | https://huggingface.co/spaces/easeeeclip/sin-reddit | ✅ Created |
| sin-discord | https://huggingface.co/spaces/easeeeclip/sin-discord | ✅ Created |
| sin-youtube | https://huggingface.co/spaces/easeeeclip/sin-youtube | ✅ Created |
| sin-tiktok | https://huggingface.co/spaces/easeeeclip/sin-tiktok | ✅ Created |
| sin-medium | https://huggingface.co/spaces/easeeeclip/sin-medium | ✅ Created |
| sin-instagram | https://huggingface.co/spaces/easeeeclip/sin-instagram | ✅ Created |
| sin-x-twitter | https://huggingface.co/spaces/easeeeclip/sin-x-twitter | ✅ Created |
| sin-community | https://huggingface.co/spaces/easeeeclip/sin-community | ✅ Created |

### Token-Speicherung

```
macOS Keychain:
  Service: sin.passwordmanager
  Accounts:
    secret:HUGGINGFACE_TOKEN  → Primary Token
    secret:HF_API_9           → easeeeclip Token
    HF_TOKEN_1_OpenJerro      → OpenJerro Token
    HF_TOKEN_2_mazingaimaze   → mazingaimaze Token
    ...

sin-passwordmanager catalog.json:
  secrets.HUGGINGFACE_TOKEN → 9 Targets (delqhi Spaces + GitHub Actions)
  secrets.HF_API_9          → 8 Targets (easeeeclip Platform Spaces)
```

### Rate Limits

- **Space Creation:** 20 pro Tag pro Account
- **API Requests:** 1000 pro 300s Window
- Bei Rate Limit: Warten bis Fenster zurückgesetzt oder anderen Account nutzen

---

## 3. HuggingFace Token Management

OpenSIN verwaltet mehrere HuggingFace Accounts für Space-Deployment und API-Zugriff. Tokens werden über sin-passwordmanager verwaltet und im macOS Keychain gespeichert.

### HF Account Registry

| ID | Account | Token Prefix | Zweck | Status |
|----|---------|-------------|-------|--------|
| HF_TOKEN_1 | OpenJerro | `hf_QZEaRY...` | Primary delqhi Org Spaces | ✅ Valid |
| HF_TOKEN_2 | mazingaimaze | - | Secondary Spaces | 📋 Keychain |
| HF_TOKEN_3 | funviral | - | Secondary Spaces | 📋 Keychain |
| HF_TOKEN_4 | lolitaexibabe | - | Secondary Spaces | 📋 Keychain |
| HF_TOKEN_5 | Mulimul | - | Secondary Spaces | 📋 Keychain |
| HF_TOKEN_6 | appimepp | - | Secondary Spaces | 📋 Keychain |
| HF_TOKEN_7 | - | - | Secondary Spaces | 📋 Keychain |
| HF_API_9 | easeeeclip | `hf_XIVHYl...` | Platform Agents (8 Spaces) | ✅ Valid |

### HF_API_9 (easeeeclip) — Platform Agent Spaces

Erstellt am 2026-04-04. Spaces unter `easeeeclip/` erstellt:

| Space | URL | Status |
|-------|-----|--------|
| sin-reddit | https://huggingface.co/spaces/easeeeclip/sin-reddit | ✅ Created |
| sin-discord | https://huggingface.co/spaces/easeeeclip/sin-discord | ✅ Created |
| sin-youtube | https://huggingface.co/spaces/easeeeclip/sin-youtube | ✅ Created |
| sin-tiktok | https://huggingface.co/spaces/easeeeclip/sin-tiktok | ✅ Created |
| sin-medium | https://huggingface.co/spaces/easeeeclip/sin-medium | ✅ Created |
| sin-instagram | https://huggingface.co/spaces/easeeeclip/sin-instagram | ✅ Created |
| sin-x-twitter | https://huggingface.co/spaces/easeeeclip/sin-x-twitter | ✅ Created |
| sin-community | https://huggingface.co/spaces/easeeeclip/sin-community | ✅ Created |

### Token-Speicherung

```
macOS Keychain:
  Service: sin.passwordmanager
  Accounts:
    secret:HUGGINGFACE_TOKEN  → Primary Token
    secret:HF_API_9           → easeeeclip Token
    HF_TOKEN_1_OpenJerro      → OpenJerro Token
    HF_TOKEN_2_mazingaimaze   → mazingaimaze Token
    ...

sin-passwordmanager catalog.json:
  secrets.HUGGINGFACE_TOKEN → 9 Targets (delqhi Spaces + GitHub Actions)
  secrets.HF_API_9          → 8 Targets (easeeeclip Platform Spaces)
```

### Rate Limits

- **Space Creation:** 20 pro Tag pro Account
- **API Requests:** 1000 pro 300s Window
- Bei Rate Limit: Warten bis Fenster zurückgesetzt oder anderen Account nutzen

---

## 4. SIN Platform Auth — Browser Session Management

**Repo:** `OpenSIN-backend/services/sin-platform-auth`  
**CLI:** `sin-platform-auth`  
**Status:** ✅ Production Ready (2026-04-04)

### Zero Human Intervention

sin-platform-auth extrahiert Browser-Sessions **automatisch** aus dem Chrome Default Profil des Users. Kein manuelles Login, keine Token-Eingabe, keine "klick mal bitte" Aufforderungen.

**Workflow:**
1. User surft normal in Chrome und loggt sich auf Plattformen ein
2. sin-platform-auth erkennt eingeloggte Sessions via Chrome Cookie Database
3. Cookies werden mit Chrome Safe Storage Key (macOS Keychain) entschlüsselt
4. Auth-Cookies werden im sin-passwordmanager gespeichert
5. Platform Agents auf HF Spaces injizieren Cookies automatisch

### Unterstützte Plattformen (12)

| Plattform | Status | Auth Cookies | Handle |
|-----------|--------|-------------|--------|
| X (Twitter) | ✅ LOGGED IN | 4 | @opnsin |
| YouTube | ✅ LOGGED IN | 29 | @opnsin |
| Instagram | ❌ NOT_VISITED | 0 | @opnsin |
| Reddit | ❌ NOT_VISITED | 0 | opnsin |
| Discord | ❌ NOT_VISITED | 0 | opnsin |
| Medium | ❌ NOT_VISITED | 0 | @opnsin |
| TikTok | ⚠️ VISITED | 0 | @opnsin |
| HuggingFace | ✅ LOGGED IN | 2 | delqhi |
| LinkedIn | ✅ LOGGED IN | 2 | opnsin |
| Telegram | ❌ NOT_VISITED | 0 | @opnsin |
| Google-Apps | ✅ LOGGED IN | 19 | opnsin |
| Community | ✅ LOGGED IN | 5 | opnsin |

**6/12 Plattformen eingeloggt**

### Cookie-Entschlüsselung

Chrome v10 Format: `v10` + AES-128-CBC(PBKDF2-SHA1(key, "saltysalt", 1003), IV=" "*16, data)

**Key:** Chrome Safe Storage String aus macOS Keychain (als UTF-8, NICHT base64-decoded!)

**BUG-091 Fix:** Chrome 146 verwendet inkonsistentes PKCS7 Padding → Fallback auf longest printable ASCII extraction.

### CLI Commands

```bash
sin-platform-auth status          # Session Status aller Plattformen
sin-platform-auth export youtube  # Cookies exportieren
sin-platform-auth save            # Alle Cookies speichern
sin-platform-auth list            # Unterstützte Plattformen
```

### MCP Integration

Platform Agents nutzen `sin-platform-auth` MCP Tools:
- `platform_auth_status` — Login-Status prüfen
- `platform_auth_export` — Cookies exportieren
- `platform_auth_load` — Gespeicherte Cookies laden
- `platform_auth_inject_script` — Injection Script generieren

---

## 🔗 Verknüpfte Dokumentation

- [Best Practices & Sicherheit](./best-practices.md)
- [OpenSIN-Code Struktur](./opensin-code.md)
- [A2A Fleet](./a2a-fleet.md)
- [Platform Auth](./platform-auth.md)
