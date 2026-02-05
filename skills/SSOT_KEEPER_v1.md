# SSOT KEEPER - Single Source of Truth Management

## Purpose
Maintain living documentation and evidence trail for DAVLE Factory operations.

## Core Rules
1. Every action → Evidence file (timestamp + result)
2. SSOT files = Always current (auto-update)
3. Markdown everywhere (human-readable, git-friendly)

## Directories
- /opt/factory/ssot/ → Master status files
- /opt/factory/evidence/YYYY-MM-DD/ → Daily action logs
- /opt/factory/runbooks/ → Process docs

## Key SSOT Files
- FACTORY_STATUS.md (master dashboard)
- SKILLS_REGISTRY.md (all skills)
- PRODUCTION_LOG.md (watch faces)
- INFRASTRUCTURE.md (server state)

## Evidence Format
Every action creates: /opt/factory/evidence/YYYY-MM-DD/HH-MM-SS_action.md

## Quick Commands
```bash
# Log evidence
log_evidence() {
  local dir="/opt/factory/evidence/$(date +%Y-%m-%d)"
  mkdir -p "$dir"
  echo "# $1 - $(date '+%Y-%m-%d %H:%M:%S')" > "${dir}/$(date +%H-%M-%S)_$1.md"
  echo "Status: $2" >> "${dir}/$(date +%H-%M-%S)_$1.md"
}

# Health check
factory_health() {
  echo "Skills: $(ls -1 ~/.claude/factory_skills/ | wc -l)"
  echo "Docker: $(systemctl is-active docker)"
}
```

## Integration
- EXECUTE_NO_BULLSHIT: auto-log actions
- PLANNING_WITH_FILES: track tasks
- HERO_ART: log design decisions

Self-documenting factory. 📚
