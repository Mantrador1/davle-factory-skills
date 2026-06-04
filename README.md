# DAVLE Factory Skills for Claude Code

Production-ready skills for automated watchface factory.

See **`SKILLS_REGISTRY.md`** for the authoritative, always-current list.

## Render Brain (design IP)

The artifacts that enforce fidelity (so renders stop dropping the seconds hand, textures,
top arc, and pushing markers out of frame):

- **reference/WATCH_ANATOMY_v1.md** — component taxonomy → Component Manifest
- **reference/MATERIALS_FINISHES_LIGHTING_v1.md** — surface/finish/lighting vocabulary
- **reference/FRAMING_LAYOUT_v1.md** — radial safe-area + composition
- **reference/NEGATIVE_PROMPTS_v1.md** — defect-suppression blocks
- **templates/RENDER_PROMPT_TEMPLATE_v1.md** — four-file prompt assembly
- **workflows/REFERENCE_TO_PROMPT_v1.md** — image-conditioned ingest → prompt
- **workflows/DESIGN_QC_LOOP_v1.md** — closed-loop render → score → re-prompt

## Skills (14)

1. **LYSIEN_HERO_ART_v2.md** - Artistic director, owns render pipeline + reject rights (v1 superseded)
2. **FACTORY_WORKFLOW_v1.md** - Evidence-based workflow orchestration
3. **MULTI_AGENT_v1.md** - Claude + ChatGPT + renderer coordination
4. **PLANNING_WITH_FILES_v1.md** - Durable task state
5. **SSOT_KEEPER_v1.md** - Living docs + evidence trail
6. **EXECUTE_NO_BULLSHIT_v1.md** - Bias-to-action mode
7. **MARKET_INTEL_v1.md** - Wear OS market doctrine (scoped to DAVLE-COCKPIT)
8. **GSD_STYLE_v1.md** - Meta-prompting / authoring style
9. **SKILL_CREATOR_v1.md** - How to author skills
10. **IMAGEMAGICK_BATCH_v1.md** - Asset pipeline automation
11. **ANDROID_BUILD_v1.md** - Gradle AAB/APK builds
12. **FLASK_API_v1.md** - Python Flask development
13. **SYSTEMD_ADMIN_v1.md** - Service management with sudo
14. **WEB_RESEARCH_v1.md** - Research helper

## Installation

```bash
# Clone to Claude skills directory
git clone https://github.com/YOUR_USERNAME/davle-factory-skills.git /tmp/skills
cp /tmp/skills/skills/*.md ~/.claude/factory_skills/
Usage
Claude Code automatically reads skills from ~/.claude/factory_skills/ when enabled.
License
MIT
