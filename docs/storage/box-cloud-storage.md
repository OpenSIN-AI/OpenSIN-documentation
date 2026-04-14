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
| room-07-gitlab-storage | Box.com Upload Agent |
| `gitlab_logcenter.py` uploads | `box_storage.py` uploads |

### Migration Script

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

---

## Docker Integration

### Box Storage Agent in docker-compose.yml

```yaml
# Box Storage Service (replaces GitLab Storage)
room-07-box-storage:
  build:
    context: ./services/box-storage
    dockerfile: Dockerfile
  image: sin-box-storage:latest
  container_name: room-07-box-storage
  restart: unless-stopped
  environment:
    - BOX_DEVELOPER_TOKEN=${BOX_DEVELOPER_TOKEN}
    - BOX_PUBLIC_FOLDER_ID=${BOX_PUBLIC_FOLDER_ID}
    - BOX_CACHE_FOLDER_ID=${BOX_CACHE_FOLDER_ID}
  networks:
    haus-netzwerk:
      ipv4_address: 172.20.0.107
  ports:
    - "8099:8099"
  healthcheck:
    test: ["CMD", "curl", "-f", "http://127.0.0.1:8099/health"]
```

### .env Template

```bash
# Box.com Storage
BOX_DEVELOPER_TOKEN=
BOX_PUBLIC_FOLDER_ID=
BOX_CACHE_FOLDER_ID=

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
