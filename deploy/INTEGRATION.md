# INTEGRATION — wiring the render-brain into the live engine

> Goal: make the versioned render-brain IP in this repo the thing the production design brain
> actually reads, so the live pipeline stops dropping the seconds hand, textures, arc, and
> stops pushing markers out of frame. This closes the "brain is fixed but the hand isn't" gap.

## 1. Deploy the IP onto the server
On the production server (where `/opt/factory` lives):
```bash
git clone <this-repo> /tmp/davle
cd /tmp/davle
bash deploy/sync_render_brain.sh        # or: FACTORY_ROOT=/opt/factory bash deploy/sync_render_brain.sh
```
This populates:
- `/opt/factory/render_brain/{reference,templates,workflows}/`
- `/opt/factory/render_brain/PRIMER.md`  ← single concatenated priming file
- `/opt/factory/factory_skills/`         ← all skills + registry

Re-run any time this repo updates. The script backs up previous versions.

## 2. Prime the design brain (the one change that fixes fidelity)
The design brain (`brain_bridge_mvp_v1.py` calling OpenAI) MUST receive the primer as
system/context BEFORE it writes a render prompt. Minimal change:

```python
PRIMER = open("/opt/factory/render_brain/PRIMER.md", encoding="utf-8").read()

system = (
    "You are the DAVLE design brain. Follow the render-brain spec EXACTLY. "
    "First emit a Component Manifest enumerating EVERY component in the reference "
    "(walk the WATCH_ANATOMY checklist; never leave a Drop-List item unknown). "
    "Then fill the RENDER_PROMPT_TEMPLATE. Name every component, attach a finish to each, "
    "assign each a radial band, and assemble the negative prompt.\n\n"
    + PRIMER
)
# messages=[{"role":"system","content":system},
#           {"role":"user","content": brief}, {reference image as image input if supported}]
```

Token note: the primer is ~a few thousand tokens. Cache it (prompt caching / a fixed prefix)
so it is not re-billed per order.

## 3. Enforce the QC loop before operator review
After the renderer returns candidates, the orchestrator runs `workflows/DESIGN_QC_LOOP_v1.md`:
score each candidate on the 12-axis / 24-point scorecard; if a candidate fails (total < 18,
any axis 0, or any Drop-List item < 2), append the targeted corrective deltas and re-render
(≤4 cycles). Only passing candidates reach `PENDING_OPERATOR_REVIEW`. Persist scorecards in
the order's `qc/`. This is the gate the old pipeline lacked.

## 4. Renderer options
- **Keep Ideogram** for text-exact dials; lean on the materials vocabulary for texture and
  accept a QC texture pass. Use `ideogram-v3-quality`.
- **Upgrade path for DAVLE-LUX photoreal:** route luxury hero renders to a stronger photoreal
  model (gemini-3-pro-image-hd / gpt-image-1-high / flux-2-pro). If the model supports image
  input, pass the reference for conditioning. Record model + path in `model.txt`.

## 5. Verify the wiring
Run one known order end-to-end and confirm the order dir contains: `manifest.json`,
`prompt.txt` (every Drop-List item named), `negative.txt`, `model.txt`, `candidates/`,
`qc/` scorecards, and that the chosen candidate scores ≥18 with no zeros. If the manifest
omits a Drop-List item, the priming did not take — re-check step 2.

## Acceptance
The fix is "real" (not just authored) when: the live `brain_bridge` loads `PRIMER.md`, every
generated `prompt.txt` enumerates the Drop List, and no candidate reaches the operator without
a passing QC scorecard.
