# SCU Gemini Production Lessons

> **Scope:** ALL SCU series — any universe using Gemini for image generation
> **Purpose:** Capture every rendering issue, fix, and rule. Read BEFORE writing any new image prompts.
> **Updated:** 2026-03-05
> **Version:** 1.0.0

---

## How to Use This File

1. **Before writing prompts:** Read the Quick Reference Rules table below
2. **When Gemini renders wrong:** Log a new lesson with full context
3. **After fixing:** Extract the rule and add to Quick Reference
4. **Per-series Header files** should reference this document

---

## QUICK REFERENCE RULES

Rules extracted from production experience. Apply to ALL series.

| # | Rule | Category | Source |
|---|------|----------|--------|
| R-001 | Never use temporal/abstract words (PRESENT, FLASHBACK, MEMORY, PAST, FUTURE, DREAM) as panel section headers inside PROMPT blocks. Use concrete scene descriptions instead. | Text Leak | L-001 |
| R-002 | Never use opacity percentages (e.g., "30% opacity") — Gemini renders them as visible text. Use descriptive language: "nearly invisible, faded white" | Text Leak | EP1 Header, confirmed EP2 |
| R-003 | Always include "WHAT NOT TO DRAW" section for complex panels (multi-character, split panels, memory overlays, silhouettes) | Composition | EP1/EP2 production |
| R-004 | For silhouettes, explicitly add: "NO skin tone, NO facial features, NO hair detail — pure black shape" | Silhouette | EP1 L-implicit |
| R-005 | Actor name + role context bypasses safety blocks. Use "Heath Ledger as a theatrical villain in clown makeup" not bare "Heath Ledger" | Safety | EP1/EP2 Header |
| R-006 | One speaker per panel. Speaker MUST be visible if they have a speech bubble. | Composition | EP1/EP2 production |
| R-007 | Max 2 text elements per panel (1 caption + 1 speech, or 2 captions). More causes garbled output. | Text Limit | EP1/EP2 production |
| R-008 | Distance requires explicit separation language: "FAR AWAY in deep background, vast empty distance" | Composition | EP1 Header |
| R-009 | Triptych panels need explicit shared backdrop instruction | Composition | EP1 Header |
| R-010 | Descriptive adjectives in composition sections can leak as visible text. Strip labels, keep only visual instructions. | Text Leak | L-001 (general pattern) |
| R-011 | Add "NO visible text other than the caption and watermark" to panels that have no intended text overlay | Text Leak | EP1 pattern |
| R-012 | In wide establishing shots with characters visible through windows/at distance, explicitly state characters are SMALL/TINY relative to the building. Add size constraint to WHAT NOT TO DRAW. | Scale | L-002 |
| R-013 | Always describe costumes/props matching the specific source film's visual language. Never use generic terms like "theatrical" or "colorful" — describe the actual movie look (e.g., "cheap rubber masks over street clothes" not "grotesque painted masks"). | Film Accuracy | L-003 |
| R-014 | Every named/significant character gets a full CHARACTER block with actor name, even minor roles. If they had a credited actor in the source film, name them. | Character | L-004 |
| R-015 | Only describe what's physically present in the depicted space. If action happens off-screen (e.g., vault in a back room), do NOT mention it — Gemini will render it in the visible frame. | Spatial Logic | L-005 |

---

## LESSON LOG

### L-001: Descriptive Panel Labels Leak as Visible Text
- **Series:** DI (Decisive Intelligence)
- **Episode:** EP2 — THE TEST
- **Slide:** 1 (Chessboard + Ra's)
- **Date:** 2026-03-05
- **Problem:** Prompt used `LEFT PANEL — PRESENT:` and `RIGHT PANEL — FLASHBACK:` as section headers inside the PROMPT block. Gemini rendered "PRESENT" and "FLASHBACK" as large visible text labels on the generated image.
- **Root Cause:** Gemini treats ALL text inside the prompt as potential render content. Section headers with abstract/temporal labels get picked up as intentional text.
- **Fix Applied:**
  1. Renamed panel headers to scene-descriptive: `LEFT PANEL — BATMAN AT CHESSBOARD:` / `RIGHT PANEL — MONASTERY TRAINING:`
  2. Removed the word "MEMORY" from description bullets
  3. Added to WHAT NOT TO DRAW: `NO text labels like "PRESENT", "FLASHBACK", "MEMORY" or any panel description rendered as visible text`
- **Result:** Regenerated image had no leaked labels. Fix confirmed.
- **Rule Extracted:** R-001
- **Scope:** Any slide with memory overlays, flashbacks, time splits, dream sequences, or contrasting timeframes.
- **Known Pending Instances:**
  - EP2 EC_02 (Burma flashback slides ~19-24)
  - EP2 EC_06 (Gordon memory slide 100)
  - EP1 EC_04 Slide 45 panel header "MEMORY AND PRESENT" (in markdown header only, NOT inside PROMPT block — lower risk, but worth standardizing)

### L-002: Character Scale Wrong in Wide Establishing Shots
- **Series:** DI (Decisive Intelligence)
- **Episode:** EP2 — THE TEST
- **Slide:** 4 (Bank Heist — Exterior + Interior)
- **Date:** 2026-03-05
- **Problem:** Left panel described figures "moving in the lobby" visible through glass. Gemini rendered the clown-masked figures LARGER than the school buses outside — breaking all sense of scale. The prompt didn't specify relative size or that this was a wide architectural shot.
- **Fix Applied:** Added explicit scale language: "FIVE SMALL FIGURES visible inside — silhouettes... barely distinguishable at this distance", "The figures are TINY relative to the building — this is a wide architectural shot, not a character close-up", and in WHAT NOT TO DRAW: "NO figures in the left panel larger than the bus"
- **Rule Extracted:** R-012
- **Scope:** Any panel mixing exterior wide shots with characters visible through windows/doors.

### L-003: Vague Costume Descriptions Produce Wrong Movie Look
- **Series:** DI (Decisive Intelligence)
- **Episode:** EP2 — THE TEST
- **Slide:** 4 (Bank Heist)
- **Date:** 2026-03-05
- **Problem:** Prompt described clown masks as "colorful", "grotesque, painted, theatrical." Gemini rendered elaborate circus-style clown costumes and face paint — looking like a different movie entirely. In The Dark Knight, the robbers wore cheap rubber/plastic mass-produced masks over dark street clothes.
- **Fix Applied:** Replaced vague descriptions with movie-specific: "cheap rubber clown masks — simple, mass-produced, plastic/rubber with painted features... NOT elaborate face paint or theatrical costumes. They wear dark street clothes (jackets, pants) with the masks pulled over their heads." Added to WHAT NOT TO DRAW: "NO elaborate face paint or circus costumes on the robbers — they wear cheap rubber masks over street clothes, movie-accurate to The Dark Knight (2008)"
- **Rule Extracted:** R-013
- **Scope:** ANY scene referencing a specific movie. Descriptions must match the actual film's visual language, not a generic interpretation.

### L-004: Named Characters Need Actor + Full Description (Even Minor Roles)
- **Series:** DI (Decisive Intelligence)
- **Episode:** EP2 — THE TEST
- **Slide:** 4 (Bank Heist)
- **Date:** 2026-03-05
- **Problem:** The bank manager was described only as "bank manager" — no actor name, no character block. Gemini rendered a generic businessman. In TDK, the bank manager was played by William Fichtner with a very specific defiant presence.
- **Fix Applied:** Added full CHARACTER block: William Fichtner, physical description, costume, expression ("Defiant, not cowering"), action, position.
- **Rule Extracted:** R-014
- **Scope:** ANY speaking or significant character, even minor ones. If they appear in the source film with a named actor, they get a full character block.

### L-005: Gemini Renders All Described Actions in One Room
- **Series:** DI (Decisive Intelligence)
- **Episode:** EP2 — THE TEST
- **Slide:** 4 (Bank Heist — Interior panel)
- **Date:** 2026-03-05
- **Problem:** Prompt described multiple simultaneous actions: "One cracking the vault, one disabling alarm, one holding gun on bank manager." Gemini placed ALL of these in the same room — vault door and alarm panel sitting in the marble lobby. In reality, the vault is in a separate back room, not visible from the public lobby.
- **Root Cause:** Gemini compresses all described elements into the visible frame. If you mention a vault, it renders a vault — even if logically it belongs in a different room.
- **Fix Applied:** Removed vault and alarm references from the panel. Described only what would be visible in the public lobby (robber with shotgun on bank manager, one clown watching). Added to WHAT NOT TO DRAW: "NO vault door, safe, or alarm panel visible — this is the public bank lobby only, not the back rooms."
- **Rule Extracted:** R-015
- **Scope:** Any scene with simultaneous action in multiple locations. Only describe what's physically present in the depicted space. Off-screen action stays off-screen.

---

## EP1 AUDIT FINDINGS (2026-03-05)

Reviewed all 9 EP1 Extended Cut files. Key observations:

| Finding | Status | Notes |
|---------|--------|-------|
| WHAT NOT TO DRAW sections present | Partial — 15+ instances across 3 of 7 content files | EC_04, EC_05, EC_06, EC_07 lack them |
| Temporal keywords in PROMPT blocks | Clean — keywords appear in markdown headers only, NOT inside ``` PROMPT ``` blocks | EP1 was more disciplined than EP2 on this |
| Opacity percentages | Clean — header explicitly warns against, content follows | ✅ |
| Actor names in all character blocks | Complete — all 6 primary actors named in every panel | ✅ |
| Silhouette exclusions | Strong — explicit "NO face detail" rules for child panels | ✅ |

**EP1 vs EP2 Gap:** EP2 put temporal labels INSIDE the PROMPT blocks (where Gemini sees them). EP1 kept them in markdown headers OUTSIDE the blocks. EP2's approach was the mistake — EP1's approach should be the standard.

---

## GEMINI BEHAVIOUR PATTERNS

General observations from production across episodes:

| Pattern | Description | Mitigation |
|---------|-------------|------------|
| **Text label leaking** | Any word used as a section header or descriptor can appear as rendered text | Use concrete scene descriptions, not abstract labels |
| **Opacity number leaking** | Percentages (30%, 2%) render as visible text | Use words: "nearly invisible", "faded" |
| **Descriptive adjective leaking** | Adjectives in composition notes sometimes appear as text | Strip unnecessary adjectives, keep visual instructions only |
| **Safety blocks on actors** | Bare actor names (especially deceased) may trigger blocks | Always pair actor name with role context |
| **Garbled text from overflow** | More than 2 text elements per panel = unreadable output | Strict 2-element limit |
| **Wrong costumes from vague refs** | "Same as before" or vague bullets = wrong costume renders | Full character block in EVERY panel, every time |
| **Hallucinated captions** | Gemini adds captions if prompt doesn't explicitly forbid them | Add "NO other text" to WHAT NOT TO DRAW |
| **Wrong actor from no name** | Generic descriptions render wrong actors | Actor name REQUIRED in every character block |

---

## PENDING FIXES

Known issues identified but not yet applied:

| Lesson | Series | Files | Fix Needed |
|--------|--------|-------|------------|
| L-001 | DI EP2 | EC_02_Paralysis_Framework.md | Rename FLASHBACK/MEMORY panel headers inside PROMPT blocks |
| L-001 | DI EP2 | EC_06_Movement_DarkKnight.md (Slide 100) | Rename MEMORY panel header inside PROMPT block |
| General | DI EP1 | EC_04, EC_05, EC_06, EC_07 | Add missing WHAT NOT TO DRAW sections for complex panels |

---

## CROSS-SERIES APPLICATION

This file applies to:

| Series | Directory | Gemini Used | Status |
|--------|-----------|-------------|--------|
| Decisive Intelligence (DI) | `decisive-intelligence/` | Yes — all EP image prompts | Active |
| Bridging the Gap (BTG) | `bridging-the-gap-between-institution-and-industry/` | Yes — episode image prompts | Active |
| [Future Series] | TBD | Expected | — |

**Per-series Header files** (e.g., `EP2_EC_00_Header.md`) should include:
```
> **Production Lessons:** See `/scu/reference/SCU_Gemini_Production_Lessons.md`
```

---

## VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-03-05 | Initial creation. L-001 logged (text label leak). EP1 audit complete. Quick Reference rules R-001 through R-011 extracted. |

---

*"Every failed render is intel. Log it, fix it, never repeat it."* 🛡️
