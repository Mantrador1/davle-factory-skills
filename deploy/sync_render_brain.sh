#!/usr/bin/env bash
# sync_render_brain.sh — deploy the DAVLE render-brain IP onto the production server.
#
# Run this ON the server (where /opt/factory lives), from a fresh clone of this repo:
#   git clone <repo> /tmp/davle && cd /tmp/davle && bash deploy/sync_render_brain.sh
#
# It copies the versioned render-brain (reference/, templates/, workflows/) and the active
# skills into /opt/factory so the live brain_bridge can read the same IP this repo defines.
# Idempotent. Backs up any existing target before overwriting.

set -euo pipefail

FACTORY="${FACTORY_ROOT:-/opt/factory}"
SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BRAIN_DST="$FACTORY/render_brain"
SKILLS_DST="$FACTORY/factory_skills"
STAMP="$(date +%Y%m%d-%H%M%S)"

echo "🎯 Deploying render-brain from $SRC -> $FACTORY"

if [ ! -d "$FACTORY" ]; then
  echo "🚫 $FACTORY not found. Set FACTORY_ROOT or run on the production server." >&2
  exit 1
fi

backup() {  # backup <dir> if it exists
  if [ -d "$1" ]; then
    echo "🔧 Backing up $1 -> $1.bak-$STAMP"
    cp -a "$1" "$1.bak-$STAMP"
  fi
}

backup "$BRAIN_DST"
mkdir -p "$BRAIN_DST"
cp -a "$SRC/reference"  "$BRAIN_DST/"
cp -a "$SRC/templates"  "$BRAIN_DST/"
cp -a "$SRC/workflows"  "$BRAIN_DST/"
echo "✅ render_brain synced (reference/ templates/ workflows/)"

backup "$SKILLS_DST"
mkdir -p "$SKILLS_DST"
cp -a "$SRC/skills/." "$SKILLS_DST/"
cp -a "$SRC/SKILLS_REGISTRY.md" "$SKILLS_DST/"
echo "✅ factory_skills synced ($(ls -1 "$SKILLS_DST"/*.md | wc -l) skills)"

# Emit the single concatenated priming file the design brain should be fed (see INTEGRATION.md).
PRIMER="$BRAIN_DST/PRIMER.md"
{
  echo "# DAVLE RENDER-BRAIN PRIMER (auto-generated $STAMP)"
  echo "# Feed this entire file to the design brain BEFORE it writes any render prompt."
  for f in \
    "$BRAIN_DST/reference/WATCH_ANATOMY_v1.md" \
    "$BRAIN_DST/reference/MATERIALS_FINISHES_LIGHTING_v1.md" \
    "$BRAIN_DST/reference/FRAMING_LAYOUT_v1.md" \
    "$BRAIN_DST/reference/NEGATIVE_PROMPTS_v1.md" \
    "$BRAIN_DST/templates/RENDER_PROMPT_TEMPLATE_v1.md"; do
    echo; echo "=============================================================="; echo "# SOURCE: ${f#$BRAIN_DST/}"; echo "=============================================================="
    cat "$f"
  done
} > "$PRIMER"
echo "✅ Wrote primer: $PRIMER ($(wc -l < "$PRIMER") lines)"

echo "🎯 Next: point brain_bridge at $PRIMER (see deploy/INTEGRATION.md). Done."
