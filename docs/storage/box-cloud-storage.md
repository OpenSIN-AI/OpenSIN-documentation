# OpenSIN Cloud Storage Architecture — Box.com & Google Drive

> **OpenSIN Storage Guide** — Multi-provider cloud storage setup for autonomous AI agents

---

## ⚠️ IMPORTANT: GitLab Storage ist tot!

**GitLab hat unser Konto gesperrt** (zu viele Dateien hochgeladen). Ab sofort nutzt OpenSIN **Box.com** als primären Cloud Storage.

---

## Storage Providers

| Provider | Free Storage | Purpose | URL |
|----------|-------------|---------|-----|
| **Box.com** | 10 GB | Primär — Public Files + Cache | [Box.com](https://app.box.com) |
| **Google Drive** | 15 GB | Sekundär — Backup + User Data | [Drive](https://drive.google.com) |

### OpenSIN Box.com Ordner

| Folder | Shared Link | Content |
|--------|------------|---------|
| `/Public` | https://app.box.com/s/1st624o9eb5xdistusew5w0erb8offc7 | Logos, Bilder, Docs — öffentlich erreichbar |
| `/Cache` | https://app.box.com/s/9s5htoefw1ux9ajaqj656v9a02h7z7x1 | Logs, Cache, Debug-Artefekte |

---

## Box.com als Object Storage nutzen

### Setup

1. **Account erstellen:** https://www.box.com/signup/ (Free = 10 GB)
2. **Ordner erstellen:** `/OpenSIN-Public` und `/Cache`
3. **Sharing aktivieren:** Rechtsklick → Share → "People with the link" → "Can view"
4. **Developer Token:** https://app.box.com/developers/console → Custom App → Developer Token

### CLI Tools

```bash
# Box CLI installieren
brew install box-cli
box login

# Dateien hochladen
box files:upload ./screenshot.png --parent-folder-id FOLDER_ID

# Ordner auflisten
box folders:children 0
```

### API Usage

```bash
# Upload via API
curl -X POST "https://upload.box.com/api/2.0/files/content" \
  -H "Authorization: Bearer $BOX_DEVELOPER_TOKEN" \
  -F "attributes={\"name\":\"file.png\",\"parent\":{\"id\":\"$BOX_FOLDER_ID\"}}" \
  -F "file=@file.png"
```

### Python Integration für A2A Agenten

```python
import os
import requests
import json

BOX_TOKEN = os.getenv("BOX_DEVELOPER_TOKEN")
BOX_FOLDER_ID = os.getenv("BOX_PUBLIC_FOLDER_ID")

def upload_to_box(file_path, filename, folder_id=None):
    """Upload file to Box.com"""
    url = "https://upload.box.com/api/2.0/files/content"
    headers = {"Authorization": f"Bearer {BOX_TOKEN}"}
    target_folder = folder_id or BOX_FOLDER_ID
    attributes = {"name": filename, "parent": {"id": target_folder}}
    
    with open(file_path, "rb") as f:
        response = requests.post(
            url,
            headers=headers,
            data={"attributes": json.dumps(attributes)},
            files={"file": f}
        )
    return response.json()

def get_public_url(file_id):
    """Get public shared link for a Box file"""
    url = f"https://api.box.com/2.0/files/{file_id}"
    headers = {"Authorization": f"Bearer {BOX_TOKEN}"}
    response = requests.get(url, headers=headers)
    return response.json().get("shared_link", {}).get("url", "")
```

---

## Migration von GitLab Storage

### Was sich ändert:

| Alt (GitLab) | Neu (Box.com) |
|-------------|--------------|
| GitLab LogCenter Repos | Box.com `/Cache` Ordner |
| `room-07-gitlab-storage` | `room-09-box-storage` (A2A-SIN-Box-Storage) |
| `gitlab_logcenter.py` uploads | Box Storage API (`/api/v1/upload`) |

### Migration Script (Upload to Box Cache)

```bash
#!/bin/bash
# migrate-gitlab-to-box.sh

BOX_TOKEN="${BOX_DEVELOPER_TOKEN}"
BOX_FOLDER_ID="${BOX_CACHE_FOLDER_ID}"

for file in ./gitlab-exports/*; do
  echo "Uploading: $file to Box.com Cache folder"
  curl -s -X POST "https://upload.box.com/api/2.0/files/content" \
    -H "Authorization: Bearer $BOX_TOKEN" \
    -F "attributes={\"name\":\"$(basename $file)\",\"parent\":{\"id\":\"$BOX_FOLDER_ID\"}}" \
    -F "file=@$file" > /dev/null
  echo "✅ $(basename $file)"
done
```

### Update Agent Configurations

All agents must switch to the new Box Storage API:

1. Change endpoint from GitLab API to `http://room-09-box-storage:3000/api/v1/upload`
2. Set header `X-Box-Storage-Key: $BOX_STORAGE_API_KEY`
3. Remove all `gitlab_logcenter.py` imports and references
4. Test with a sample upload: `curl -F "file=@test.png" -H "X-Box-Storage-Key: xxx" http://localhost:3000/api/v1/upload`

> **BREAKING CHANGE:** No fallback to GitLab Storage will be provided. The `room-07-gitlab-storage` service is deprecated and removed from Infra-SIN-Docker-Empire v2.0.1+.

---

## Docker Integration

### Room 09: Box Storage Service (A2A-SIN-Box-Storage)

The **A2A-SIN-Box-Storage** service replaces `room-07-gitlab-storage`. Add to `docker-compose.yml`:

```yaml
# Box Storage Agent — Public File Upload API
room-09-box-storage:
  build:
    context: ./services/box-storage
    dockerfile: Dockerfile
  image: a2a-sin-box-storage:latest
  container_name: room-09-box-storage
  restart: unless-stopped
  environment:
    - BOX_DEVELOPER_TOKEN=${BOX_DEVELOPER_TOKEN:?ERROR: must be set in .env file}
    - BOX_PUBLIC_FOLDER_ID=${BOX_PUBLIC_FOLDER_ID:?ERROR: must be set in .env file}
    - BOX_CACHE_FOLDER_ID=${BOX_CACHE_FOLDER_ID:?ERROR: must be set in .env file}
    - API_KEY=${BOX_STORAGE_API_KEY:?ERROR: must be set in .env file}
    - PORT=3000
    - NODE_ENV=production
    - MAX_FILE_SIZE=2GB
    - ALLOWED_EXTENSIONS=.png,.jpg,.jpeg,.gif,.pdf,.doc,.docx,.txt,.zip
  volumes:
    - box_storage_logs:/app/logs
  networks:
    haus-netzwerk:
      ipv4_address: 172.20.0.109
  ports:
    - "3000:3000"
  healthcheck:
    test: ["CMD", "curl", "-f", "http://127.0.0.1:3000/health"]
    interval: 30s
    timeout: 10s
    retries: 3
    start_period: 30s

volumes:
  box_storage_logs:
```

> **Note:** The service source code lives in the standalone repository:  
> https://github.com/OpenSIN-AI/A2A-SIN-Box-Storage  
> Either:
> - Clone as submodule: `git submodule add https://github.com/OpenSIN-AI/A2A-SIN-Box-Storage.git services/box-storage`
> - Or copy the contents into `./services/box-storage` before `docker compose up`

### .env Template

```bash
# Box.com Storage (Required)
BOX_DEVELOPER_TOKEN=your_developer_token_here
BOX_PUBLIC_FOLDER_ID=1234567890
BOX_CACHE_FOLDER_ID=0987654321
BOX_STORAGE_API_KEY=shared_secret_for_agents_min_32_chars

# Google Drive Storage (optional)
GOOGLE_DRIVE_CLIENT_ID=
GOOGLE_DRIVE_CLIENT_SECRET=
GOOGLE_DRIVE_FOLDER_ID=
```

---

## Onboarding: Storage Auswahl

Beim OpenSIN Onboarding MUSS der User einen Storage Provider wählen:

### Box.com (Empfohlen)
- ✅ 10 GB free
- ✅ Einfache öffentliche Links
- ✅ Gute API für Automation
- ❌ Developer Token nur 60 Min gültig (JWT App needed für production)

### Google Drive (Alternative)
- ✅ 15 GB free (mehr als Box)
- ✅ Bessere Zugriffskontrolle
- ✅ Service Account für production
- ❌ Komplexere Setup für öffentliche Links

**Empfehlung:** Box.com für öffentliche Dateien, Google Drive für private User-Daten.

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| 404 bei Box Shared Link | Sharing prüfen → "People with the link" → "Can view" |
| Developer Token expired | Neuen Token generieren (max 60 Min) oder JWT App erstellen |
| Rate Limit | Box Free = 10 GB + 10k API calls/day |
| Upload failed | Folder ID prüfen: `box folders:children 0` |

---

## Related
- [Infra-SIN-Dev-Setup](https://github.com/OpenSIN-AI/Infra-SIN-Dev-Setup/blob/main/box-storage.md) — Detailed Box Storage Guide
- [Infra-SIN-Docker-Empire](https://github.com/OpenSIN-AI/Infra-SIN-Docker-Empire) — Docker Infrastructure
- [OpenSIN-onboarding](https://github.com/OpenSIN-AI/OpenSIN-onboarding) — User Onboarding
