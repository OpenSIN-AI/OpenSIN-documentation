# 🔄 Auth Rotator Systeme

OpenSIN betreibt zwei autonome Auth-Rotationssysteme, die Model-Quota-Erschöpfung erkennen und automatisch neue Accounts provisionieren.

## 1. openAntigravity-auth-rotator

**Zweck:** Automatisches Rotieren von Google Workspace Accounts wenn Antigravity-Model-Quotas erschöpft sind.

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
└──────────────────────────────────────────────────────┘
```

## 2. OpenSIN-Authenticator

**Zweck:** Multi-Provider Auth Management für 100+ LLM Provider.

**Repository:** [OpenSIN-AI/OpenSIN-Authenticator](https://github.com/OpenSIN-AI/OpenSIN-Authenticator)

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

### HF Spaces

| Account | Spaces | Status |
|---------|--------|--------|
| delqhi | 11 Spaces | ✅ Active |
| easeeeclip | 9 Spaces | ✅ Active (7 RUNNING, 1 ERROR, 1 BUILDING) |

### Rate Limits

- **Space Creation:** 20 pro Tag pro Account
- **API Requests:** 1000 pro 300s Window
- Bei Rate Limit: Warten bis Fenster zurückgesetzt oder anderen Account nutzen

## 4. SIN Platform Auth — Browser Session Management

**Repo:** `OpenSIN-backend/services/sin-platform-auth`  
**CLI:** `sin-platform-auth`  
**Status:** ✅ Production Ready (2026-04-04)

### Zero Human Intervention

sin-platform-auth extrahiert Browser-Sessions **automatisch** aus dem Chrome Default Profil des Users. Kein manuelles Login, keine Token-Eingabe.

**Workflow:**
1. User surft normal in Chrome und loggt sich auf Plattformen ein
2. sin-platform-auth erkennt eingeloggte Sessions via Chrome Cookie Database
3. Cookies werden mit Chrome Safe Storage Key (macOS Keychain) entschlüsselt
4. Auth-Cookies werden im sin-passwordmanager gespeichert
5. Platform Agents auf HF Spaces und Platform Workers injizieren Cookies automatisch

### Unterstützte Plattformen (17)

| Plattform | Login URL | Handle |
|-----------|-----------|--------|
| X (Twitter) | https://x.com/login | @opnsin |
| YouTube | https://youtube.com | @opnsin |
| Instagram | https://instagram.com/accounts/login | @opnsin |
| Reddit | https://reddit.com/login | opnsin |
| Discord | https://discord.com/login | opnsin |
| Medium | https://medium.com/m/signin | @opnsin |
| TikTok | https://tiktok.com/login | @opnsin |
| HuggingFace | https://huggingface.co/login | delqhi |
| LinkedIn | https://linkedin.com/login | opnsin |
| Telegram | https://web.telegram.org | @opnsin |
| Google-Apps | https://accounts.google.com | opnsin |
| GitHub (Community) | https://github.com/login | opnsin |
| DevTo | https://dev.to/enter | @opnsin |
| ProductHunt | https://www.producthunt.com/login | opnsin |
| StackOverflow | https://stackoverflow.com/users/login | opnsin |
| Quora | https://www.quora.com/login | opnsin |
| IndieHackers | https://www.indiehackers.com/signin | opnsin |

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

---

## 🔗 Verknüpfte Dokumentation

- [Best Practices & Sicherheit](./best-practices.md)
- [OpenSIN-Code Struktur](./opensin-code.md)
- [A2A Fleet](./a2a-fleet.md)
- [Platform Auth](./platform-auth.md)
