# MATERIALS, FINISHES & LIGHTING — Surface Vocabulary

> **Purpose.** "Λείπουν οι υφές" (textures are missing) is a *material-language* failure.
> A renderer paints flat plastic when the prompt says "sub-dial". It paints brushed metal
> with micro-grain when the prompt says "concentric azurage guilloché on a recessed sub-dial,
> circular-brushed, soft snailed reflection rotating around its own center". This file gives
> the design brain the exact phrases that trigger real surface detail.

> Pair with `WATCH_ANATOMY_v1.md` (what the parts are) and `NEGATIVE_PROMPTS_v1.md` (forbidding "flat", "plastic").

---

## Principle: a watch is a study in *contrasting finishes*

Premium watches read as premium because adjacent surfaces have **different** finishes that
catch light differently. Flatness = a single uniform finish everywhere. Every prompt should
deliberately stack contrasting finishes:

- polished (mirror) **next to** brushed (matte directional)
- sunray (radial sheen) **next to** guilloché (engraved pattern)
- recessed (in shadow) **next to** applied (catching the key light)

If a render looks cheap, the usual cause is "everything is the same finish."

---

## Metals & cases

| Phrase to use | Visual result |
|---|---|
| `brushed rose gold, fine vertical grain` | warm matte directional metal |
| `polished rose gold, mirror finish` | sharp specular highlights, reflects environment |
| `satin-brushed stainless steel` | cool neutral matte |
| `polished steel bevels with brushed top surfaces` | the premium two-finish case look |
| `gunmetal PVD / DLC matte black coating` | stealth dark metal, low reflection |
| `titanium, fine bead-blasted matte` | muted grey, very low gloss |

**Always pair a metal with its grain direction** ("vertical grain", "circular grain",
"radial brushing"). Direction is what makes brushed metal look real.

---

## Dial finishes (the base plate)

| Phrase | Result |
|---|---|
| `matte black dial with ultra-fine grain` | deep, light-absorbing, premium black |
| `sunray-brushed dial` | radial sheen sweeping from center, shifts with angle |
| `fumé / smoked gradient dial, light center to dark edge` | luxury gradient |
| `lacquered glossy dial, deep reflection` | piano-black wet look |
| `opaline / silvered dial, soft satin` | bright dressy base |
| `grand-feu enamel, glassy with faint depth` | high-end white/ivory |
| `meteorite dial, Widmanstätten crystalline pattern` | exotic texture |

---

## Sub-dial textures (THE most-dropped texture — be aggressive here)

Sub-dials are recessed mini-dials. Naming the engraving pattern is mandatory.

| Phrase | Result |
|---|---|
| `concentric guilloché (azurage), fine grooves rotating around the sub-dial center` | classic ringed counter |
| `snailed / colimaçon finish, spiral brushing catching a soft rotating highlight` | the "snail" sheen |
| `clous de Paris / hobnail guilloché, tiny raised pyramids` | textured grid |
| `circular satin brushing` | simplest acceptable; better than flat |
| `vertical brushed counter recessed below the main dial` | industrial look |

**Always add:** `recessed below the dial plane with a soft inner shadow at its upper edge,
framed by a thin polished metal ring with a crisp circular edge.` — this single clause kills
both "flat sub-dial" and "sloppy sub-dial cuts" at once.

---

## Markers & hands finishes

| Phrase | Result |
|---|---|
| `applied faceted baton markers, polished metal, each catching a sharp highlight on one facet` | 3D applied indices |
| `diamond-cut bevelled edges on markers and hands` | the bright edge-line that signals quality |
| `dauphine hands with a polished facet down the spine and a brushed flank` | two-finish hands |
| `lume-filled hands and markers, cream/ice-blue Super-LumiNova` | glow inserts |
| `thin central seconds hand, counterweighted tail, lacquered tip in <accent>` | crisp seconds |
| `heat-blued steel hands` | iridescent blue |

---

## Module / LCD finishes (hybrid faces)

- `recessed circular LCD under its own polished metal bezel ring, soft inner drop-shadow`
- `amber 7-segment digits with faint phosphor glow and subtle pixel grid`
- `crisp anti-aliased OLED digits, pure emissive, slight bloom`
- `faint glass reflection arc across the top-left of the module`

---

## Lighting model (use ONE coherent setup, do not stack contradictory lights)

The reference look is almost always **studio product photography**:

> `single large soft key light from upper-left, gentle gradient falloff to lower-right;
> soft fill to keep shadows readable; one crisp specular highlight per polished surface;
> dark studio environment reflected in the polished metal; subtle ambient occlusion where
> sub-dials and markers meet the dial.`

Rules:
- **One key light direction.** Multiple hard lights = confused, AI-looking reflections.
- **Specular highlights are features, not noise.** Each polished baton/hand gets ~one bright glint.
- **Ambient occlusion** in the recesses (under markers, inside sub-dials, around the module ring)
  is what creates depth. State it.
- **Crystal optics:** `domed sapphire crystal, faint anti-reflective blue-violet sheen,
  slight refraction/distortion of the chapter ring near the rim.`

---

## Macro / quality boosters (append to luxury prompts)

`macro product photography, extreme detail, tack-sharp focus on the dial, shallow depth of
field falling off at the case edge, 100mm macro lens look, high microcontrast, no motion blur,
physically based rendering, 8k texture detail.`

---

## Finish-stacking template (drop into any luxury prompt)

```
CASE: <metal> brushed top with polished bevels, <bezel texture> bezel.
DIAL: <dial finish> base.
SUBDIALS: recessed, <guilloché type>, polished ring, soft inner shadow.
MARKERS/HANDS: applied/faceted, diamond-cut bevels, one specular glint each.
MODULE: recessed under polished ring, <segment style>, faint glass reflection.
LIGHT: single soft key upper-left, dark studio reflections, ambient occlusion in recesses.
OPTICS: domed sapphire, faint AR blue, rim refraction.
QUALITY: macro product photography, PBR, tack-sharp, high microcontrast.
```
