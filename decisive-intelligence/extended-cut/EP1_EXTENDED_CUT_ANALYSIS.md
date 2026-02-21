# EP1 Extended Cut — Pre-Build Analysis
## What We Have, What We Lost, What We Learned

> **Date:** 2026-02-21
> **Purpose:** Review before building EP1 Extended Cut screenplay
> **Sources:** EP1 Screenplay (124 panels) + EP1 KLP Prompts v3 (60 slides)

---

## 1. THE COMPRESSION MAP

### What the KLP Cut Did

**124 screenplay panels → 60 slides (52% compression)**

The KLP cut had one job: tell the story in ~6-7 minutes. It did it well. But here's what it cost:

| Section | Screenplay Panels | KLP Slides | Compression | What Was Lost |
|---------|-------------------|------------|-------------|---------------|
| The Fall (Scenes 1-2) | 12 | 4 | 3:1 | Young Bruce detail (silhouette approach) |
| The Journey (Scenes 3-5) | 18 | 3 | 6:1 | **Entire Bhutan journey** — prison, monastery discovery, blue flower |
| Training (Scenes 6-13) | 40 | 6 | 6.7:1 | **Most training detail** — philosophy lessons, progress arc, ideology |
| CLARITY (Scene 14) | 16 | 6 | 2.7:1 | Some blindfold progression (4 attempts → condensed) |
| COURAGE (Scenes 15-16) | 12+4 | 6 | 2.7:1 | Some cave depth, fear-as-weapon philosophy |
| COMMITMENT (Scene 17) | 15 | 6 | 2.5:1 | Escape consequences, burning temple detail |
| Escape (Scene 18) | 5 | 2 | 2.5:1 | Minimal — captured well |
| Return (Scenes 19-20) | 17 | 4 | 4.3:1 | **Birthday party depth** — Ra's reveal nuance |
| MOVEMENT (Scene 21) | 8 | 4 | 2:1 | Batcave discovery detail |
| Batman Emerges (22-23) | 9 | 3 | 3:1 | **Suiting up sequence** — compressed to grid |
| Train Fight (Scene 24) | 20 | 8 | 2.5:1 | Several combat exchanges, pillar callbacks |
| Closing (Scenes 25-26) | 19 | 8 | 2.4:1 | Some Gordon/Batman exchange |

### Protected vs Compressed

| Status | Slides | % | Content |
|--------|--------|---|---------|
| **Protected** (pillar scenes) | 30 | 50% | CLARITY, COURAGE, COMMITMENT, MOVEMENT, ALL FOUR |
| **Compressed** (everything else) | 30 | 50% | Journey, training, return, suiting up |

**The pillars were protected. Everything BETWEEN the pillars was squeezed.**

---

## 2. WHAT THE EXTENDED CUT RESTORES

The Extended Cut target: ~35 minutes per episode. That's ~5x the KLP runtime.

### Sections That NEED Expansion (Heavy Compression in KLP)

| Section | KLP | Extended Target | Why It Matters |
|---------|-----|-----------------|----------------|
| **The Journey** | 3 slides (1 grid) | 10-12 slides | Bruce's transformation from prisoner to student. The audience needs to FEEL the journey, not skip it. |
| **Training** | 6 slides (2 grids) | 18-22 slides | This is where the MENTOR relationship builds. Ra's isn't just teaching moves — he's shaping a mind. Every philosophy lesson matters. |
| **Birthday/Ra's Reveal** | 4 slides | 8-10 slides | The moment the mentor becomes the enemy. This is HUGE emotionally — needs room to land. |
| **Suiting Up** | 3 slides (1 grid) | 6-8 slides | The transformation. Batman being born panel by panel. Iconic. |
| **Train Fight** | 8 slides | 14-16 slides | All four pillars applied. Each pillar callback deserves its own moment. |

### Sections That Are FINE (Adequate Depth in KLP)

| Section | KLP | Extended Target | Notes |
|---------|-----|-----------------|-------|
| The Fall | 4 slides | 5-6 slides | Silhouette approach works. Maybe 1-2 more. |
| CLARITY | 6 slides | 8-10 slides | Restore full 4-attempt progression |
| COURAGE | 6 slides | 8-10 slides | Restore fear-as-weapon philosophy |
| COMMITMENT | 6 slides | 8-10 slides | Restore burning temple, escape consequences |
| MOVEMENT | 4 slides | 6-8 slides | Restore Batcave discovery |
| Escape | 2 slides | 3-4 slides | Minimal expansion |
| Closing | 8 slides | 10-12 slides | Room for chessboard + Joker tease |

### Extended Cut Slide Estimate

| Section | Estimated Slides |
|---------|-----------------|
| Cover | 1 |
| The Fall | 5-6 |
| The Journey | 10-12 |
| Training | 18-22 |
| CLARITY | 8-10 |
| COURAGE | 8-10 |
| COMMITMENT | 8-10 |
| Escape | 3-4 |
| Return + Ra's Reveal | 8-10 |
| MOVEMENT | 6-8 |
| Batman Emerges | 6-8 |
| Train Fight | 14-16 |
| Closing | 10-12 |
| Post-Credits (Workplace) | 14 |
| **TOTAL** | **~120-145 slides** |

That's roughly 2x the KLP cut — restoring depth without padding.

---

## 3. GEMINI LEARNINGS — BAKED IN FROM DAY 1

### From 8 Sessions of Testing

| # | Learning | How to Apply in Extended Cut |
|---|---------|------------------------------|
| 1 | **Actor names needed for likeness** | Use actor names when face is visible. Physical-only when blocked. |
| 2 | **Child + distress = blocked** | Keep silhouette approach for Young Bruce. Proven safe. |
| 3 | **Hallucinated text from descriptions** | Strip flowery language. "Batman strikes" not "Batman delivers a precise targeted strike." |
| 4 | **Speaker must be visible in panel** | Never put a speech bubble in a panel where that character isn't shown. |
| 5 | **Full character blocks EVERY panel** | No shortcuts. No "same as above." Full block every time. |
| 6 | **Max 2 text elements per panel** | 1 caption + 1 speech bubble OR 2 captions. Never more. |
| 7 | **"WHAT NOT TO DRAW" sections** | Add for complex panels. Prevents Gemini defaults (desks, chairs, props). |
| 8 | **Descriptive language leaks as text** | Keep action descriptions factual. Gemini renders adjectives as visible text. |
| 9 | **Max 6 panels per grid** | 2×3 is the limit. Anything more = character detail lost. |
| 10 | **Actor name + certain costumes = blocked** | "Robert Downey Jr." works with civilian clothes, blocked with Doom armor. Test early. |
| 11 | **Generic descriptions = wrong actor** | "Grey hair, moustache, glasses" rendered Bryan Cranston, not Gary Oldman. Use actor name. |
| 12 | **Thomas Wayne rendering inconsistent** | Slide 3 flagged for regen. May need multiple attempts. |

### Character Block Status (Proven in Gemini)

| Character | Actor | Status | Notes |
|-----------|-------|--------|-------|
| Bruce Wayne | Christian Bale | ✅ Proven | All variations work |
| Ra's Al Ghul / Ducard | Liam Neeson | ✅ Proven | All 3 costumes work |
| Alfred | Michael Caine | ✅ Proven | Both age variations |
| Gordon | Gary Oldman | ✅ Proven | Works WITH actor name (without = Bryan Cranston) |
| Thomas Wayne | — | ⚠️ Inconsistent | Flagged for regen in KLP. Needs attention. |
| Ra's Decoy | Ken Watanabe | ✅ Proven | Works in KLP |
| Batman (suit) | Christian Bale | ✅ Proven | Full armor description works |

---

## 4. RECALIBRATIONS FOR EXTENDED CUT

### Things That Change

| Aspect | KLP Cut | Extended Cut |
|--------|---------|-------------|
| **Grids** | 4 × 6-panel grids | Minimize grids — expand to individual panels |
| **Runtime target** | ~6-7 min | ~35 min (story) + ~5 min (post-credits) |
| **Panel-to-slide ratio** | 2:1 average | Closer to 1:1 |
| **Training depth** | 2 grids (montage) | Scene-by-scene with dialogue |
| **Philosophy lessons** | Skipped/implied | Fully dramatized |
| **Pillar definitions** | Caption boxes at end of section | Can breathe more — moment + aftermath |
| **Post-credits** | Joker card tease | Workplace story (14 panels) |

### Things That Stay the Same

| Aspect | Why |
|--------|-----|
| **Silhouette approach (Young Bruce)** | Gemini-safe, proven, emotionally effective |
| **Full character blocks** | Non-negotiable. Every panel. |
| **Pillar colors** | Blue, Red, White/Silver, Orange |
| **Chessboard motif** | Four pieces, same colors |
| **"WHAT NOT TO DRAW"** | Keep for all complex panels |
| **Max 2 text elements per panel** | Prevents hallucination |
| **Credits format** | "Created, Crafted & Made by @iSwamiK" |
| **S.P. Easter Egg** | Hidden somewhere — different from KLP placement |

### New Elements for Extended Cut

| Element | Description |
|---------|-------------|
| **Post-credits workplace story** | 14 panels. Same characters in office. (Draft done) |
| **Deeper philosophy scenes** | Restore Scenes 7, 9, 10, 11, 12, 13 — each gets proper treatment |
| **Birthday party expansion** | Ra's reveal needs 8-10 panels. The emotional weight of mentor-becomes-enemy. |
| **Train fight full depth** | 20 screenplay panels → 14-16 slides. Each pillar callback gets its own moment. |
| **No grids for training** | Instead of 2 grids = "montage," each training moment gets individual panels |

---

## 5. RECOMMENDED APPROACH

### Step 1: Extended Screenplay
Take the existing 124-panel screenplay as the source. Don't rewrite — **expand**:
- Restore panels that were cut for KLP
- Add depth where the screenplay has room (training, philosophy)
- Keep pillar scenes at existing quality (they're already strong)
- Add post-credits section

### Step 2: Extended Prompts
Convert screenplay to Gemini prompts with:
- All 12 Gemini learnings applied
- Full character blocks in every panel
- 1-2 panels per slide (no heavy compression)
- "WHAT NOT TO DRAW" for complex panels

### Step 3: Director Review
Scene by scene, not all at once. Lock each section before moving to the next.

---

## 6. OPEN QUESTIONS FOR DIRECTOR

1. **Thomas Wayne rendering** — The KLP cut flagged Slide 3 for regen. Do we have a working Thomas Wayne image now, or does this need solving first?

2. **Training philosophy scenes** — The screenplay has 8 training scenes (6-13). The KLP cut compressed them to 2 grids. For Extended Cut, should we restore ALL 8, or are some less essential?

3. **Pillar naming** — EP1 screenplay says "framework experienced, NOT named." The pillar words (CLARITY, COURAGE, etc.) appear only in caption boxes. Extended Cut — same approach? Or since this is a standalone 35-min experience, should the naming be more prominent?

4. **Cover slide** — The KLP has a mountain monastery cover. Extended Cut — same cover or a different one to visually distinguish the product?

---

*"Read everything. Learn everything. Then build."* 🦇
