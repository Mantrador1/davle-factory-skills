# DAVLE Factory — Skills & Render-Brain Registry

Single source of truth for what exists in this repo. Keep in sync with the files on disk.

## Render brain (the design IP — NEW)
These are the artifacts whose absence caused the fidelity loss (dropped seconds hand,
missing textures/arc, out-of-frame markers, sloppy cuts). The renderer/brain reads these.

| File | Role |
|---|---|
| `reference/WATCH_ANATOMY_v1.md` | Component taxonomy → Component Manifest. Enumerate everything. |
| `reference/MATERIALS_FINISHES_LIGHTING_v1.md` | Surface/finish/lighting vocabulary. Kills flatness. |
| `reference/FRAMING_LAYOUT_v1.md` | Radial safe-area + composition. Kills off-frame & sloppy cuts. |
| `reference/NEGATIVE_PROMPTS_v1.md` | Defect-suppression blocks. |
| `templates/RENDER_PROMPT_TEMPLATE_v1.md` | Four-file prompt assembly (manifest/prompt/negative/model). |
| `workflows/REFERENCE_TO_PROMPT_v1.md` | Image-conditioned ingest → prompt method. |
| `workflows/DESIGN_QC_LOOP_v1.md` | Closed-loop render→score→re-prompt. The art-director gate. |

## Skills
| File | Role | Status |
|---|---|---|
| `skills/LYSIEN_HERO_ART_v2.md` | Artistic director — owns render pipeline + reject rights | active |
| `skills/LYSIEN_HERO_ART_v1.md` | Original brand slogan | superseded by v2 |
| `skills/FACTORY_WORKFLOW_v1.md` | Evidence-first orchestration, paths, providers | active |
| `skills/MULTI_AGENT_v1.md` | Claude+ChatGPT+renderer handoff | active (see note) |
| `skills/PLANNING_WITH_FILES_v1.md` | Durable task state (was broken/empty) | active (fixed) |
| `skills/SSOT_KEEPER_v1.md` | Living docs + evidence trail | active |
| `skills/EXECUTE_NO_BULLSHIT_v1.md` | Bias-to-action operating mode | active |
| `skills/MARKET_INTEL_v1.md` | Wear OS market doctrine — applies to DAVLE-COCKPIT only | active (scoped) |
| `skills/GSD_STYLE_v1.md` | Meta-prompting / skill-authoring style | active |
| `skills/SKILL_CREATOR_v1.md` | How to author new skills | active |
| `skills/IMAGEMAGICK_BATCH_v1.md` | Asset pipeline (mask/resize/optimize) | active |
| `skills/ANDROID_BUILD_v1.md` | Gradle AAB/APK builds (Phase 3 app) | active |
| `skills/FLASK_API_v1.md` | Python Flask backend | active |
| `skills/SYSTEMD_ADMIN_v1.md` | Service management | active |
| `skills/WEB_RESEARCH_v1.md` | Research helper | active |

## Notes / open follow-ups
- **MULTI_AGENT_v1** describes one-shot text-to-image. The QC loop + image-conditioning in
  `workflows/` are the upgrade; MULTI_AGENT should be revised to call them. (next pass)
- **Renderer:** production uses Ideogram on the server (`/opt/factory`). In Claude-Code-on-web
  sessions, stronger photoreal models are reachable via the Gamma image backends
  (gemini-3-pro-image-hd, gpt-image-1-high, flux-2-pro, imagen-4-ultra) — candidate upgrade
  for DAVLE-LUX hero renders.
- **Server mirror:** `/opt/factory` is NOT in this repo. The render-brain files here should be
  the SSOT and mirrored to the server so the live engine consumes the same IP.
- Skill files have no YAML frontmatter (name/description/triggers); adding it would enable
  reliable auto-activation. (next pass)
