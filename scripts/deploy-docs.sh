#!/usr/bin/env bash
set -euo pipefail

exec ./node_modules/.bin/wrangler pages deploy docs/.vitepress/dist --project-name opensin-docs --commit-dirty=true
