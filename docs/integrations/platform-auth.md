# SIN Platform Auth — Browser Session Management

**Datum:** 2026-04-04  
**Version:** 1.0.0  
**Status:** ✅ Production Ready  
**Repo:** `OpenSIN-backend/services/sin-platform-auth`

## Übersicht

**SIN Platform Auth** ist das autonome Cookie-Extraktions- und Injection-System für alle SIN Platform Agents. Es extrahiert Browser-Sessions direkt aus dem Chrome Default Profil des Users, entschlüsselt die Cookies mit dem macOS Keychain "Chrome Safe Storage" Key, und speichert sie im sin-passwordmanager für die Nutzung durch HF Space Agenten.

**Kein manuelles Login nötig.** Der User surft normal in Chrome — sin-platform-auth erkennt und extrahiert alle Sessions automatisch.

## Architektur

```
Chrome Default Profil (Cookies.db)
  ↓
sin-platform-auth (Cookie-Export)
  ↓
macOS Keychain (Chrome Safe Storage Key)
  ↓
PBKDF2-SHA1 + AES-128-CBC Entschlüsselung
  ↓
sin-passwordmanager (catalog.json + Keychain)
  ↓
HF Space Agents (Cookie-Injection)
```

## Unterstützte Plattformen (12)

| Plattform | Status | Auth Cookies | Handle | Login URL |
|-----------|--------|-------------|--------|-----------|
| **X (Twitter)** | ✅ LOGGED IN | 4 | @opnsin | https://x.com/login |
| **YouTube** | ✅ LOGGED IN | 29 | @opnsin | https://youtube.com |
| **Instagram** | ❌ NOT_VISITED | 0 | @opnsin | https://instagram.com/accounts/login |
| **Reddit** | ❌ NOT_VISITED | 0 | opnsin | https://reddit.com/login |
| **Discord** | ❌ NOT_VISITED | 0 | opnsin | https://discord.com/login |
| **Medium** | ❌ NOT_VISITED | 0 | @opnsin | https://medium.com/m/signin |
| **TikTok** | ⚠️ VISITED | 0 | @opnsin | https://tiktok.com/login |
| **HuggingFace** | ✅ LOGGED IN | 2 | delqhi | https://huggingface.co/login |
| **LinkedIn** | ✅ LOGGED IN | 2 | opnsin | https://linkedin.com/login |
| **Telegram** | ❌ NOT_VISITED | 0 | @opnsin | https://web.telegram.org |
| **Google-Apps** | ✅ LOGGED IN | 19 | opnsin | https://accounts.google.com |
| **Community** | ✅ LOGGED IN | 5 | opnsin | https://github.com/login |

**6/12 Plattformen eingeloggt, 1 besucht, 5 nicht besucht**

## CLI Usage

```bash
# Session Status aller Plattformen anzeigen
sin-platform-auth status

# Cookies für alle Plattformen exportieren
sin-platform-auth export

# Cookies für spezifische Plattform exportieren
sin-platform-auth export youtube

# Cookies exportieren und in sin-passwordmanager speichern
sin-platform-auth save
sin-platform-auth save youtube

# Unterstützte Plattformen auflisten
sin-platform-auth list
```

## MCP Tools

| Tool | Beschreibung |
|------|-------------|
| `platform_auth_status` | Login-Status für alle/spezifische Plattformen |
| `platform_auth_export` | Cookies für Plattform exportieren |
| `platform_auth_save` | Cookies exportieren und speichern |
| `platform_auth_load` | Gespeicherte Cookies laden |
| `platform_auth_list` | Alle unterstützten Plattformen |
| `platform_auth_inject_script` | Cookie-Injection Script für Browser generieren |

## Cookie-Entschlüsselung (Technical Deep Dive)

Chrome verschlüsselt Cookies auf macOS mit:

1. **v10 Format:** `v10` Prefix + AES-128-CBC verschlüsselte Daten
2. **Key:** Chrome Safe Storage String aus macOS Keychain (als UTF-8, NICHT base64-decoded!)
3. **PBKDF2:** SHA1, salt="saltysalt", iterations=1003, key length=16
4. **IV:** 16 Spaces (0x20)
5. **Padding:** Chrome verwendet nicht immer korrektes PKCS7 Padding → Fallback: Longest printable ASCII extraction

### BUG-091 Fix

**Problem:** Cookie-Entschlüsselung lieferte `null` für alle Cookies.

**Ursache:** Zwei Fehler:
1. Safe Storage Key wurde als base64-decoded bytes statt als UTF-8 String verwendet
2. Chrome 146 verwendet inkonsistentes PKCS7 Padding

**Lösung:**
```javascript
// Key als UTF-8 String (NICHT base64-decoded!)
const masterKey = Buffer.from(safeStorageKey, 'utf8');

// PKCS7 Padding mit Fallback auf ASCII extraction
const matches = text.match(/[\x20-\x7e]{8,}/g);
if (matches) return matches.reduce((a, b) => a.length > b.length ? a : b);
```

## Password Manager Integration

Gespeicherte Secrets im sin-passwordmanager:

| Secret Name | Plattform | Auth Cookies | Targets |
|------------|-----------|-------------|---------|
| `PLATFORM_AUTH_X_TWITTER` | x-twitter | 4 | easeeeclip/sin-x-twitter |
| `PLATFORM_AUTH_YOUTUBE` | youtube | 29 | easeeeclip/sin-youtube |
| `PLATFORM_AUTH_HUGGINGFACE` | huggingface | 2 | easeeeclip/sin-huggingface |
| `PLATFORM_AUTH_LINKEDIN` | linkedin | 2 | easeeeclip/sin-linkedin |
| `PLATFORM_AUTH_GOOGLE_APPS` | google-apps | 19 | easeeeclip/sin-google-apps |
| `PLATFORM_AUTH_COMMUNITY` | community | 5 | easeeeclip/sin-community |

## HF Space Cookie-Injection

Platform Agents auf HF Spaces können gespeicherte Cookies via MCP injizieren:

```javascript
// In Platform Agent (HF Space)
const cookies = await loadFromPasswordManager('youtube');
// Cookie-Injection via puppeteer/nodriver
for (const cookie of cookies) {
  await page.setCookie(cookie);
}
await page.goto('https://youtube.com');
```

## Security

- **Keine Tokens im Code:** Alle Credentials über sin-passwordmanager
- **macOS Keychain:** Chrome Safe Storage Key geschützt durch macOS Keychain
- **File Permissions:** Cookie-Files mit `chmod 600` (nur User lesbar)
- **Auto-Expiry:** Cookies haben expires_utc — abgelaufene Sessions werden erkannt

## Zero Human Intervention

sin-platform-auth implementiert das **Zero Human Intervention Mandate**:
- Kein manuelles Login in Platform Agents
- Keine manuelle Token-Eingabe
- Keine "klick mal bitte" Aufforderungen
- User surft normal in Chrome → Agenten arbeiten autonom mit extrahierten Sessions
