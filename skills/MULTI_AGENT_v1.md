Multi-Agent Coordination (Claude + ChatGPT + Ideogram)
Purpose
Orchestrate multiple AI agents for watchface generation pipeline.
Agent Roles
Claude Code: System admin, builds, deployment
ChatGPT (OpenAI): Design brain, layout planning
Ideogram: Asset rendering, visual generation
Handoff Pattern
1. User → Claude: "REMAKE with bigger time digits"
2. Claude → ChatGPT: Design spec (JSON)
3. ChatGPT → Ideogram: Render prompt
4. Ideogram → Claude: PNG assets
5. Claude → ImageMagick: Process & preview
6. Claude → User: Updated watchface
Shared Evidence Directory
/opt/factory/evidence/REMAKE_<ORDER>_<TIMESTAMP>/
├── request.json (user feedback)
├── design_spec.json (ChatGPT output)
├── render_prompt.txt (Ideogram prompt)
├── assets/ (PNG files)
├── preview.png (final processed)
└── metadata.json (all metadata)
JSON Schema
{
  "orderId": "WF_HERO_001",
  "feedback": "Make time bigger",
  "timestamp": "2026-02-04T23:00:00Z",
  "agents": {
    "claude": {"status": "completed"},
    "chatgpt": {"status": "completed", "tokens": 1234},
    "ideogram": {"status": "completed", "credits": 1}
  }
}
Error Handling
Timeout: 5 min per agent
Retry: 3 attempts with exponential backoff
Fallback: Return to previous version
Evidence
Every agent logs to shared evidence directory.
