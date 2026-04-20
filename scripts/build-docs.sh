#!/usr/bin/env bash
set -euo pipefail

exec node node_modules/vitepress/bin/vitepress.js build docs
