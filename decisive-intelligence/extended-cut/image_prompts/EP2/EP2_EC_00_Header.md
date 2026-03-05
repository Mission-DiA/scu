# DECISIVE INTELLIGENCE — EPISODE 2: THE TEST
## Director's Extended Cut — Gemini Image Generation Prompts

> **Version:** EC 1.0.0
> **Date:** 2026-03-04
> **Total Slides:** ~148 (main story + post-credits + transition cards)
> **Duration:** ~35 min story + ~5 min post-credits
> **Visual Style:** Dark Knight noir — photorealistic, high-contrast, Nolan-esque cinematography
> **Aspect Ratio:** 16:9 (1920×1080px)
> **Source:** EP2_THE_TEST_Extended_Screenplay.md (EC 1.0.0 — 207 panels + 15 post-credits)

---

## PRODUCTION RULES

1. **FULL BLEED** — Image extends to ALL edges, NO margins
2. **1-2px PANEL LINES** — Thin white lines between panels ONLY (for multi-panel compositions)
3. **FULL CHARACTER BLOCKS** — Complete specs in EVERY prompt — NO lazy references
4. **ONE DIALOGUE PER SPEAKER** — Each character gets MAX one speech bubble per panel
5. **MAX 2 TEXT ELEMENTS** — 1 caption + 1 speech OR 2 captions per slide
6. **PHOTOREALISTIC STYLE** — Dark Knight noir aesthetic throughout
7. **ACTOR NAMES IN ALL CHARACTER BLOCKS** — Prevents wrong actor renders
8. **SPEAKER MUST BE VISIBLE** — If a character has a speech bubble, they must appear in the panel
9. **JOKER SAFETY PROTOCOL** — Use "Heath Ledger as a theatrical villain" + full costume description. Test early for blocks.
10. **NO CHILD + WEAPON** — Gordon's son scenes: imply danger through staging, NOT weapon-to-minor

---

## TEXT STYLING REFERENCE

| Element | Fill | Text | Outline | Notes |
|---------|------|------|---------|-------|
| Speech Bubbles | White (#FFFFFF) | Black, bold | Black (#000000), 2px | Tail points to speaker |
| Joker Speech | White, JAGGED edges | Black, bold | Black (#000000), 2px | Irregular bubble shape |
| Caption Boxes | Dark navy (#1a1a4e) | White | None | Top or bottom of panel |
| Internal Monologue | Light grey (#E5E7EB) | Dark grey, italic | Soft edges | Batman only |
| Pillar: CLARITY | Blue (#4A90D9) | White, bold | None | When pillar is named |
| Pillar: COURAGE | Red (#EF4444) | White, bold | None | When pillar is named |
| Pillar: COMMITMENT | White (#FFFFFF) | Black, bold | Black outline | When pillar is named |
| Pillar: MOVEMENT | Orange (#F97316) | White, bold | None | When pillar is named |

---

## WATERMARK

**ALL SLIDES:** "DI × SCU" watermark — bottom-LEFT corner, nearly invisible, faded white. ~2% image width. Present in EVERY slide. NOTE: Do NOT include opacity percentages in prompts — Gemini renders them as visible text.

---

## COMPRESSION TECHNIQUES

| Technique | Application | Panels Per Slide |
|-----------|-------------|------------------|
| **Single splash** | Key emotional beats, pillar reveals, cover, end card | 1 |
| **Split panel** | Two related moments (contrast, before/after, dual locations) | 2 |
| **Vertical triptych** | Three sequential moments | 3 |
| **Quad (2×2)** | Montage, parallel action, progress | 4 |
| **6-panel grid (2×3)** | Crisis montage, fragmented chaos | 6 (max) |

**Rule: Key moments get single panels. Montage/chaos can compress.**

---

## GEMINI COMPATIBILITY NOTES

1. **Actor names are REQUIRED** for correct likeness — generic descriptions render wrong actors
2. **"WHAT NOT TO DRAW"** sections prevent Gemini from filling in wrong defaults
3. **Camera angle specs** (FROM BELOW, FROM INSIDE) dramatically improve composition
4. **ONE moment per panel** — never two events in same panel
5. **Full character blocks in EVERY panel** — vague bullets = wrong costumes
6. **Always use full names** — "Heath Ledger" not "HL"
7. **Gemini leaks descriptive language as visible text** — strip adjectives from descriptions
8. **"NO other text" prevents hallucinated captions**
9. **Speaker must be VISIBLE** for speech bubbles
10. **One speaker per panel rule** — confirmed across all episodes
11. **Max 2 text elements per panel** — more causes garbled output
12. **Actor name + role context bypasses blocks** — `"Heath Ledger as a theatrical villain in clown makeup"` passes; bare `"Heath Ledger"` may get blocked
13. **Silhouette needs explicit exclusions** — add: `"NO skin tone, NO facial features"`
14. **Opacity percentages leak as visible text** — use `"nearly invisible, faded white"` instead
15. **Distance requires explicit separation** — `"FAR AWAY in deep background, vast empty distance"`
16. **Triptych panels need shared backdrop** — `"ALL THREE PANELS share the same backdrop"`
17. **Split panels need clear dividing line** — `"thin white 1-2px vertical line dividing"`

### EP2-SPECIFIC SAFETY NOTES

| Concern | Mitigation |
|---------|------------|
| **Heath Ledger as Joker** | Use: "Heath Ledger as a theatrical villain with smeared white face paint and green hair" + full costume. Test early. |
| **Hospital explosion** | Frame as "building exploding in background, character walking in foreground" — no people in blast |
| **Harvey's burns** | "Half his face showing burn scarring, movie-accurate" — not graphic. Test early. |
| **Child in danger** | NEVER show weapon pointed at child. Use: "imposing figure looming over frightened boy" — imply, don't show |
| **Rachel captive** | "Figure in dark warehouse, timer visible" — minimize helplessness cues |
| **Multiple Joker costumes** | Full character block with EXPLICIT costume in EVERY panel — 4 different looks |

---

## CREDITS FORMAT

```
CREATIVE HEAD: Raja
EXECUTIVE PRODUCER: Nisha P
PRODUCED BY: Susan L
THE DI TEAM: Balaji VG · Janani AP · Joy Besterwitch · Raj Gajendran · Suresh Kumar
In collaboration with Claude Code & Google Gemini

A SWAMI K FILM (2× larger, letter-spaced, gold glow)
```

---

## EC STRUCTURE

| # | File | Scenes | Est. Slides | Range |
|---|------|--------|-------------|-------|
| 0 | Header (this file) | — | — | — |
| 1 | Cover + Chaos | 1, 2, 3A, 3 | 14 | 0-13 |
| 2 | Paralysis + Framework + Batpod | 4, 5, 6, 9B | 12 | 14-25 |
| 3 | Clarity | 7, 8, 9, 10 | 18 | 26-43 |
| 4 | Courage | 11, 12, 13, 13B, 14 | 25 | 44-68 |
| 5 | Commitment | 14B, 15, 16, 17, 18, 19, 19B | 24 | 69-92 |
| 6 | Movement + Dark Knight | 20, 21, 22, 23, 24, 25, 26, 27, 28 | 28 | 93-120 |
| 7 | Post-Credits + Transition Cards | WP 1-15, TC 1-6 | 19 | 121-139 |
| 8 | Summary | — | — | — |
| | **TOTAL** | | **~140** | **0-139** |

---

## FILE INDEX

| File | Content | Slides |
|------|---------|--------|
| `EP2_EC_00_Header.md` | Production rules, text styling, Gemini notes | — |
| `EP2_EC_01_Cover_and_Chaos.md` | Cover + Opening + Bank Heist + Four Crises | 0-13 |
| `EP2_EC_02_Paralysis_Framework.md` | Batman frozen + Joker call + Ra's flashback + Batpod | 14-25 |
| `EP2_EC_03_Clarity.md` | Alfred + Burma Story + Choice + Race + The Lie | 26-43 |
| `EP2_EC_04_Courage.md` | Explosion + Interrogation + Hospital + Walk-Away + Ferry | 44-68 |
| `EP2_EC_05_Commitment.md` | Construction Site + Two-Face + Gordon's Family + Tackle + Fox Sonar | 69-92 |
| `EP2_EC_06_Movement_DarkKnight.md` | The Lie + Hunt + Bat-Signal + Dark Knight + Closing + Bane Tease | 93-120 |
| `EP2_EC_07_PostCredits_TransitionCards.md` | Workplace Story + Transition Cards | 121-139 |
| `EP2_EC_08_Summary.md` | Production summary, verification, version history | — |

---
