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
