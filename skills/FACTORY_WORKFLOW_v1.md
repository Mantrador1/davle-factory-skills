# DAVLE Factory Workflow Skill

## Evidence-First Law
Every action writes evidence bundle to:
/opt/factory/evidence/ORDER_<NAME>_v<N>/<TIMESTAMP>/

## Key Paths
- Assets: /opt/factory/assets_curated/
- Evidence: /opt/factory/evidence/
- Panel: /opt/factory/panel/
- Bin: /opt/factory/bin/
- Config: /opt/factory/config/
- Secrets: /opt/factory/secrets/

## AI Providers
- OpenAI: design_brain, orchestrator_brain
  - Key: /opt/factory/secrets/openai_api_key_main.txt
- Ideogram: hero_art_detailing, rendering
  - Key: /opt/factory/secrets/ideogram_api_key_main.txt

## Watchface Structure
Each watchface has:
- design_spec.json (metadata)
- preview_active.png (454x454)
- preview_aod.png (simplified)

## Systemd Services
- factory-ideogram-runner.service
- factory-panel-mvp.service
- factory-brain-bridge.service

## Commands
- Ideogram: /opt/factory/bin/run_ideogram_canonical_v1.sh
- Brain: /opt/factory/bin/brain/brain_bridge_mvp_v1.py
