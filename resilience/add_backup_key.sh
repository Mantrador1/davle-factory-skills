#!/usr/bin/env bash
# Append an extra SSH public key to deploy's authorized_keys.
# Never overwrites: it backs up first and skips keys that are already present.
#
# Run on the factory server, as deploy:
#   bash resilience/add_backup_key.sh "ssh-ed25519 AAAA... phone-termius"
set -euo pipefail

PUBKEY="${1:-}"
AUTH_DIR="${HOME}/.ssh"
AUTH_FILE="${AUTH_DIR}/authorized_keys"

say() { printf '%s\n' "$*"; }

if [ -z "$PUBKEY" ]; then
  say "Usage: bash $0 \"ssh-ed25519 AAAA... comment\""
  exit 1
fi

# Reject anything that is not a public key line - a private key here would be
# both useless and a leak.
case "$PUBKEY" in
  ssh-ed25519\ *|ssh-rsa\ *|ecdsa-sha2-nistp*\ *|sk-ssh-ed25519*\ *) ;;
  *) say "🚫 That does not look like an SSH public key."
     say "   It must start with ssh-ed25519, ssh-rsa or ecdsa-sha2-nistp..."
     exit 1 ;;
esac

mkdir -p "$AUTH_DIR"
chmod 700 "$AUTH_DIR"
touch "$AUTH_FILE"
chmod 600 "$AUTH_FILE"

# Compare on the key material only, so a different trailing comment still counts
# as the same key.
KEY_BODY="$(printf '%s' "$PUBKEY" | awk '{print $2}')"
if [ -n "$KEY_BODY" ] && grep -qF -- "$KEY_BODY" "$AUTH_FILE"; then
  say "✅ Key is already authorised. Nothing to do."
  exit 0
fi

BACKUP="${AUTH_FILE}.bak.$(date +%Y%m%d%H%M%S)"
cp -p "$AUTH_FILE" "$BACKUP"
say "🔧 Backup written to ${BACKUP}"

printf '%s\n' "$PUBKEY" >> "$AUTH_FILE"
say "✅ Key added to ${AUTH_FILE}"
say ""
say "   Test it from the other device BEFORE closing this session:"
say "   ssh ${USER:-$(id -un)}@$(hostname -I 2>/dev/null | awk '{print $1}')"
