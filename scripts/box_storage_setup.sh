#!/bin/bash
set -e

TOKEN="${BOX_DEVELOPER_TOKEN:-f9PURW50E47k9dwoVKkBD64QLJLnC4Nx}"
API="https://api.box.com/2.0"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

log() { echo -e "${GREEN}[BOX]${NC} $1"; }
warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
error() { echo -e "${RED}[ERROR]${NC} $1"; exit 1; }

api_get() { curl -s -X GET "$API/$1" -H "Authorization: Bearer $TOKEN"; }
api_post() { curl -s -X POST "$API/$1" -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d "$2"; }
api_put() { curl -s -X PUT "$API/$1" -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d "$2"; }

log "Box.com Storage Setup starting..."
log "Token: ${TOKEN:0:20}..."

USER_INFO=$(api_get "users/me")
USER_NAME=$(echo "$USER_INFO" | python3 -c "import sys,json; print(json.load(sys.stdin).get('name','?'))" 2>/dev/null || echo "?")
log "Authenticated as: $USER_NAME"

PUBLIC_FOLDER=$(api_get "folders/0/items" | python3 -c "
import sys,json
items = json.load(sys.stdin).get('entries',[])
pub = [f for f in items if f.get('name')=='Public']
print(pub[0]['id'] if pub else '')
" 2>/dev/null || echo "")

if [ -z "$PUBLIC_FOLDER" ]; then
    log "Creating Public folder..."
    RESULT=$(api_post "folders" '{"name":"Public","parent":{"id":"0"}}')
    PUBLIC_FOLDER=$(echo "$RESULT" | python3 -c "import sys,json; print(json.load(sys.stdin).get('id',''))" 2>/dev/null || echo "")
    log "Public folder created: $PUBLIC_FOLDER"
else
    log "Public folder exists: $PUBLIC_FOLDER"
fi

api_put "folders/$PUBLIC_FOLDER" '{"shared_link":{"access":"open"}}' > /dev/null

CACHE_FOLDER=$(api_get "folders/0/items" | python3 -c "
import sys,json
items = json.load(sys.stdin).get('entries',[])
cache = [f for f in items if f.get('name')=='Cache']
print(cache[0]['id'] if cache else '')
" 2>/dev/null || echo "")

if [ -z "$CACHE_FOLDER" ]; then
    log "Creating Cache folder..."
    RESULT=$(api_post "folders" '{"name":"Cache","parent":{"id":"0"}}')
    CACHE_FOLDER=$(echo "$RESULT" | python3 -c "import sys,json; print(json.load(sys.stdin).get('id',''))" 2>/dev/null || echo "")
    log "Cache folder created: $CACHE_FOLDER"
else
    log "Cache folder exists: $CACHE_FOLDER"
fi

api_put "folders/$CACHE_FOLDER" '{"shared_link":{"access":"open"}}' > /dev/null

log "==========================================="
log "SETUP COMPLETE!"
log "==========================================="
log ""
log "Add these to your .env:"
log "  BOX_DEVELOPER_TOKEN=$TOKEN"
log "  BOX_PUBLIC_FOLDER_ID=$PUBLIC_FOLDER"
log "  BOX_CACHE_FOLDER_ID=$CACHE_FOLDER"
log "  BOX_STORAGE_API_KEY=generate_a_secure_random_key"
log ""
log "CORS domains in Box Developer Console:"
log "  http://localhost:3000"
log "  http://room-09-box-storage:3000"
log ""
log "==========================================="
log "SETUP COMPLETE!"
log "==========================================="
log ""
log "Add these to your .env file:"
log ""
log "  BOX_DEVELOPER_TOKEN=$TOKEN"
log "  BOX_PUBLIC_FOLDER_ID=$PUBLIC_FOLDER"
log "  BOX_CACHE_FOLDER_ID=$CACHE_FOLDER"
log "  BOX_STORAGE_API_KEY=generate_a_secure_random_key"
log ""
log "CORS domains to add in Box Developer Console:"
log "  - http://localhost:3000"
log "  - http://room-09-box-storage:3000"
log "  - https://your-domain.com"
log ""
log "Folder URLs:"
log "  Public: $PUBLIC_LINK"
log "  Cache:  https://app.box.com/s/$(echo $CACHE_FOLDER | cut -c1-10)..."
log ""
log "==========================================="