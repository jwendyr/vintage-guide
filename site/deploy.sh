#!/usr/bin/env bash
# Rebuild from ../items.json and deploy to Cloudflare Pages project vintage-rostandy.
set -euo pipefail; cd "$(dirname "$0")"
python3 build.py
[ -n "${CLOUDFLARE_API_TOKEN:-}" ] || CLOUDFLARE_API_TOKEN="$(cat /home/box/.secrets/cf_pages_token)"
export CLOUDFLARE_API_TOKEN; unset CLOUDFLARE_EMAIL CLOUDFLARE_API_KEY
export CLOUDFLARE_ACCOUNT_ID=f5dbc4f1c3e4f3fbdacb83107b8088da
npx wrangler pages project create vintage-rostandy --production-branch=main >/dev/null 2>&1 || true
npx wrangler pages deploy dist --project-name=vintage-rostandy --branch=main --commit-dirty=true
