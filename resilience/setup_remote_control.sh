#!/usr/bin/env bash
# Install claude remote-control as a systemd service so the factory is
# reachable from claude.ai/code and the Claude mobile app after every boot.
#
# Run on the factory server:  sudo bash resilience/setup_remote_control.sh
set -euo pipefail

SERVICE_USER="deploy"
UNIT_NAME="claude-remote-control.service"
UNIT_SRC="$(dirname "$(readlink -f "$0")")/${UNIT_NAME}"
UNIT_DST="/etc/systemd/system/${UNIT_NAME}"

say() { printf '%s\n' "$*"; }

[ "$(id -u)" -eq 0 ] || { say "🚫 Run with sudo."; exit 1; }
[ -f "$UNIT_SRC" ] || { say "🚫 Missing ${UNIT_SRC}"; exit 1; }
id "$SERVICE_USER" >/dev/null 2>&1 || { say "🚫 No such user: ${SERVICE_USER}"; exit 1; }

say "🎯 Locating the claude binary for ${SERVICE_USER}"
CLAUDE_BIN="$(sudo -u "$SERVICE_USER" bash -lc 'command -v claude' 2>/dev/null || true)"
if [ -z "$CLAUDE_BIN" ]; then
  say "🚫 claude is not on ${SERVICE_USER}'s PATH."
  say "   Install it, or run: sudo -u ${SERVICE_USER} bash -lc 'command -v claude'"
  exit 1
fi
say "   → ${CLAUDE_BIN}"

command -v script >/dev/null || { say "🚫 util-linux 'script' is required."; exit 1; }

# ANTHROPIC_API_KEY disables Remote Control. Warn rather than guess at a fix.
if sudo -u "$SERVICE_USER" bash -lc '[ -n "${ANTHROPIC_API_KEY:-}" ]'; then
  say "⚠️  ANTHROPIC_API_KEY is set for ${SERVICE_USER}."
  say "   Remote Control needs a claude.ai login instead. Unset it, then re-run."
fi

say "🔧 Installing ${UNIT_DST}"
sed "s|__CLAUDE_BIN__|${CLAUDE_BIN}|g" "$UNIT_SRC" > "$UNIT_DST"
chmod 0644 "$UNIT_DST"

say "🔧 Enabling and starting the service"
systemctl daemon-reload
systemctl enable "$UNIT_NAME" >/dev/null
systemctl restart "$UNIT_NAME"

sleep 5
if systemctl is-active --quiet "$UNIT_NAME"; then
  say "✅ ${UNIT_NAME} is running and enabled at boot."
  say ""
  say "   Open the Claude app → Code. A session named 'Factory' should appear"
  say "   with a computer icon and a green dot."
else
  say "❌ Service did not stay up. Last log lines:"
  journalctl -u "$UNIT_NAME" -n 30 --no-pager || true
  say ""
  say "   Most common cause: ${SERVICE_USER} is not logged in to claude.ai."
  say "   Fix with:  sudo -u ${SERVICE_USER} -i claude auth login"
  exit 1
fi
