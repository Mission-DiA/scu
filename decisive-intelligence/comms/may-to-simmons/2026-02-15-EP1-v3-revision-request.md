---
from: may
to: simmons
date: 2026-02-15
topic: EP1 Prompts — v3 Revision Request (Tighter + Minor-Safe)
urgency: request
status: responded
---

# EP1 THE FOUNDATION — v3 Revision Request

Simmons,

v2 was good. But we've hit two walls:

1. **Gemini is refusing childhood slides** — minor in distress triggers safety filters
2. **Director wants tighter** — 55-60 slides, not 94

This revision solves both.

---

## The Ask

| Metric | v2 | v3 Target |
|--------|-----|-----------|
| Slides | 94 | 55-60 |
| Duration | ~10 min | ~6-7 min |
| Reduction | — | ~40% further |

---

## Problem 1: Minor Depiction

**What's happening:**
Slide 4 prompt shows "8-year-old Bruce screaming, overwhelmed by bats" — Gemini refuses to generate. Safety filters block minors in distress.

**Root cause:**
- Direct depiction of child's face in terror
- Detailed description of minor's emotional state
- "Screaming," "overwhelmed," "terrified" applied to a child

**Solution: SILHOUETTE APPROACH**

For ALL Young Bruce scenes (Scenes 1-2), use:
- Child as SHADOW/SILHOUETTE — not detailed face
- Focus on ENVIRONMENT (bats, cave, darkness) — not child's expression
- Abstract/symbolic representation — not literal depiction
- Adults (Thomas, Alfred) in focus — child obscured or background

---

## Problem 2: Young Bruce Consistency

**What's happening:**
Without an actor anchor, Gemini draws a different boy for each slide.

**Solution: SILHOUETTE APPROACH (same fix)**

When Young Bruce is a silhouette:
- No face to be inconsistent
- Shadow figure is consistent by nature
- Focus shifts to environment and emotion
- Artistic, Nolan-esque, works better anyway

---

## Scenes 1-2 Rewrite (THE FALL + THE BATS)

**Current:** 8 slides
**Target:** 3-4 slides

### SLIDE 1 — THE FALL (Panels 1.1-1.5 COMBINED)
**VERTICAL TRIPTYCH — SILHOUETTE**

```
PROMPT:
Create a photorealistic, cinematic comic panel in 16:9 aspect ratio.
Dark Knight noir style. VERTICAL TRIPTYCH. SYMBOLIC.

SCENE: The fall — three moments, child as SILHOUETTE only.

COMPOSITION:
- THREE VERTICAL PANELS side by side, thin white lines (1-2px) dividing
- LEFT: Wayne Manor against stormy sky, lightning flash, small SILHOUETTE
  of a child running toward well in distance — NO FACE DETAIL
- CENTER: SILHOUETTE of small figure falling through black void,
  arms outstretched, well opening shrinking above — SHADOW ONLY
- RIGHT: Cave floor impact, dust cloud, small crumpled SHADOW FIGURE
  among rocks — NO FACE VISIBLE

CRITICAL: The child is depicted as SILHOUETTE/SHADOW only.
No facial features, no detailed expression. The ENVIRONMENT
tells the story — the darkness, the fall, the void.

ATMOSPHERE:
- Gothic, symbolic
- Fear through environment, not expression
- Childhood trauma as abstract concept

TEXT OVERLAY:
- Caption (dark navy #1a1a4e, white text) left panel: "Every framework begins with a fall."
- Caption (dark navy #1a1a4e, white text) center panel: "Fear found him."
- Caption (dark navy #1a1a4e, white text) right panel: "Into the dark."

STYLE: Photorealistic, cinematic, SILHOUETTE approach. Full bleed.
```

---

### SLIDE 2 — THE BATS (Panels 2.1-2.3 COMBINED)
**FULL BLEED — SWARM FOCUS**

```
PROMPT:
Create a photorealistic, cinematic comic panel in 16:9 aspect ratio.
Dark Knight noir style. HORROR. BAT FOCUS.

SCENE: Bats explode from darkness — the swarm is the subject.

COMPOSITION:
- FULL BLEED: THOUSANDS OF BATS spiraling in tornado formation
- At center: A small SHADOW FIGURE — silhouette only,
  arms raised defensively, consumed by the swarm
- The BATS are the focus — photorealistic detail on nearest ones
  (leathery wings, small eyes, fangs)
- ONE BAT in extreme foreground, face detailed, fangs exposed
- The child is ABSTRACT — a dark shape being overwhelmed

CRITICAL: The human figure is a SILHOUETTE only. No face,
no detailed expression. The BATS are photorealistic.
The child is a SHAPE consumed by darkness.

ATMOSPHERE:
- Pure nightmare
- The swarm is the terror
- Childhood trauma as symbolic darkness

TEXT OVERLAY:
- Caption (dark navy #1a1a4e, white text) bottom-center:
  "He would remember this moment for the rest of his life."

STYLE: Photorealistic BATS, SILHOUETTE child. Full bleed.
```

---

### SLIDE 3 — THE RESCUE (Panels 2.4-2.7 COMBINED)
**SINGLE — THOMAS FOCUS**

```
PROMPT:
Create a photorealistic, cinematic comic panel in 16:9 aspect ratio.
Dark Knight noir style. EMOTIONAL. ADULT FOCUS.

SCENE: Thomas Wayne rescues his son — father is the subject.

COMPOSITION:
- SINGLE PANEL: Cave interior, bats gone
- THOMAS WAYNE in FOREGROUND — kneeling, arms wrapped protectively,
  flashlight beam cutting through darkness
- The child is PARTIALLY OBSCURED — held against Thomas's chest,
  back to camera, or face buried in father's shoulder
- Thomas's face shows love, concern, protection
- The rescue beam as hope in darkness

THOMAS WAYNE FULL DESCRIPTION:
- Face & Body: Late 30s, handsome Caucasian man, dark hair,
  strong jaw, expensive casual clothing now dirty
- Expression: Love, concern, fierce protection
- Action: Kneeling, holding child, flashlight in hand
- Position: Center foreground

CHILD: Back to camera OR face buried in father's shoulder.
NOT VISIBLE IN DETAIL. A small form being protected.

ATMOSPHERE:
- Father's love
- Rescue from nightmare
- Hope entering darkness

TEXT OVERLAY:
- Speech bubble (white, black text, 2px outline) from Thomas:
  "Why do we fall, Bruce?"

STYLE: Photorealistic, ADULT FOCUS. Full bleed.
```

---

### SLIDE 4 — ALFRED'S LESSON (Panels 2.6-2.7)
**SINGLE — ALFRED FOCUS**

```
PROMPT:
Create a photorealistic, cinematic comic panel in 16:9 aspect ratio.
Dark Knight noir style. EMOTIONAL.

SCENE: Alfred delivers the lesson — adult focus.

COMPOSITION:
- SINGLE PANEL: Wayne Manor interior, warm lighting
- ALFRED in foreground — speaking wisdom
- Young Bruce IMPLIED — perhaps a shadow on the wall,
  or Alfred looking toward off-camera child
- Do NOT show the child directly

ALFRED (YOUNGER) FULL DESCRIPTION:
- Face & Body: Michael Caine, British man, late 50s,
  distinguished, grey hair neatly combed, kind but firm eyes
- Costume: Butler's formal attire, dark vest, white shirt
- Expression: Gentle wisdom, teaching moment
- Action: Speaking to someone off-camera
- Position: Center frame

ATMOSPHERE:
- Wisdom delivered
- The lesson that matters
- Foundation being laid

TEXT OVERLAY:
- Speech bubble (white, black text, 2px outline) from Alfred:
  "So that we can learn to pick ourselves up."

STYLE: Photorealistic, ADULT FOCUS. Full bleed.
```

---

## Section-by-Section Targets

| Section | v2 | v3 Target | Technique |
|---------|-----|-----------|-----------|
| THE FALL (1-2) | 8 | 4 | Silhouette approach above |
| THE JOURNEY (3-5) | 7 | 3 | Single 6-panel montage + 2 key moments |
| THE TRAINING (6-13) | 16 | 6 | Two 6-panel grids + key teaching moments |
| CLARITY (14) | 11 | 6 | 6-panel progression + famous line |
| COURAGE (15-16) | 11 | 6 | 6-panel progression + famous line |
| COMMITMENT (17) | 11 | 6 | 6-panel progression + famous line |
| THE ESCAPE (18) | 3 | 2 | Jump cuts |
| THE RETURN (19-20) | 9 | 4 | Ra's reveal focus |
| MOVEMENT (21) | 7 | 4 | Manor burns sequence |
| BATMAN EMERGES (22-23) | 6 | 3 | Single transformation |
| ALL FOUR (24) | 14 | 8 | Train fight climax |
| THE CLOSING (25-26) | 12 | 8 | Joker tease + chessboard |
| **TOTAL** | 94 | **60** | — |

---

## New Compression Technique: 6-PANEL GRID

For training/montage sections, use 6-panel grids (2 rows × 3 columns):

```
┌─────┬─────┬─────┐
│  1  │  2  │  3  │
├─────┼─────┼─────┤
│  4  │  5  │  6  │
└─────┴─────┴─────┘
```

One slide = 6 moments. Use for:
- Training progression (Scenes 6-13)
- Journey montage (Scenes 3-5)
- Non-pivotal sequences

---

## Critical Rules for v3

### Rule 1: NO DETAILED CHILD DEPICTION
- Young Bruce (8 years old) = SILHOUETTE/SHADOW only
- No facial features, no expressions
- Environment and adults carry the emotion
- Child is abstract shape, symbolic presence

### Rule 2: ADULTS IN FOCUS
- Thomas Wayne = detailed, emotional, heroic
- Alfred = detailed, wise, caring
- Young Bruce = obscured, background, or off-camera

### Rule 3: 6-PANEL GRIDS FOR MONTAGE
- Training sequences: 6-panel grids
- Journey sequences: 6-panel grids
- Pivotal moments: Single slides (protected)

### Rule 4: PIVOTAL SCENES STILL PROTECTED
- Scene 14 (CLARITY): 6 slides minimum
- Scene 15-16 (COURAGE): 6 slides minimum
- Scene 17 (COMMITMENT): 6 slides minimum
- Scene 24 (ALL FOUR): 8 slides minimum
- These are ADULT Bruce — no restrictions

---

## Deliverable

**EP1_FOUNDATION_Prompts_v3.md**

| Metric | v2 | v3 |
|--------|-----|-----|
| Slides | 94 | 55-60 |
| Duration | ~10 min | ~6-7 min |
| Young Bruce | Detailed | Silhouette |
| Montages | Quad panels | 6-panel grids |
| Gemini blocks | Yes (Slide 4) | No (minor-safe) |

---

## Why This Works

1. **Gemini-safe:** No detailed minor depiction = no safety filter blocks
2. **Consistent:** Silhouettes don't vary between slides
3. **Artistic:** Nolan-esque, symbolic, sophisticated
4. **Tighter:** 6-panel grids compress without losing beats
5. **Focused:** Adults carry emotion, environment carries fear

---

The depth is still there. Now it's safe AND fast.

— May

*"The shadow tells the story. The swarm carries the fear."* 🦇
