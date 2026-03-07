# DECISIVE INTELLIGENCE — EPISODE 2: THE TEST
## Director's Extended Cut — Gemini Image Generation Prompts

> **Version:** EC 3.0.0 (Ground-Zero v2 Rebuild)
> **Date:** 2026-03-07
> **Total Slides:** 109 (Slides 0-108: main story + post-credits + transition cards)
> **Duration:** ~35 min story + ~5 min post-credits
> **Visual Style:** Dark Knight noir — photorealistic, high-contrast, Nolan-esque cinematography
> **Aspect Ratio:** 16:9 (1920×1080px)
> **Source:** EP2_THE_TEST_Extended_Screenplay.md (EC 3.0.0 — Ground-Zero Rebuild from TDK screenplay)
> **Production Lessons:** See `/scu/reference/SCU_Gemini_Production_Lessons.md` — R-001 through R-015 applied

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

## EC STRUCTURE (v3.0.0 — Ground-Zero Rebuild)

| # | File | Scenes | Slides | Range |
|---|------|--------|--------|-------|
| 0 | Header (this file) | — | — | — |
| 1 | Cover + Chaos | Cover (0.1) + Opening (0.2) + Prologue P1-P4 | 14 | 0-13 |
| 2 | Prologue P5-P9 | Harvey (P5) + Gambol (P6) + Hong Kong (P7) + RICO (P8) + Ultimatum (P9) | 10 | 14-23 |
| 3 | Clarity | Act 1 — C1 (Fundraiser) through C8 (Coin-flip) | 17 | 24-40 |
| 4 | Courage | Act 2 — K1 ("I Am the Batman") through K4 (Rachel/Two-Face) | 17 | 41-57 |
| 5 | Commitment | Act 3 — M1 (Money Burn) through M7 (Ferry ★) | 18 | 58-75 |
| 6 | Movement + Closing | Act 4 — V1 (Prewitt) through V4 (Dark Knight ★) + X1-X3 (Cost/Arkham/Bane) | 17 | 76-92 |
| 7 | Post-Credits + Transitions | "This Was the Crisis" (25 panels → 14 slides) + Transition Cards (6 → 2 slides) | 16 | 93-108 |
| | **TOTAL** | | **109** | **0-108** |

---

## FILE INDEX

| File | Content | Slides |
|------|---------|--------|
| `EP2_EC_00_Header.md` | Production rules, text styling, Gemini notes (this file) | — |
| `EP2_EC_01_Cover_and_Chaos.md` | Cover + Opening + Bank Heist P1 + Scarecrow P2 + New Suit P3 + Mob Meeting P4 | 0-13 |
| `EP2_EC_02_Prologue_P5_P9.md` | Harvey Dent P5 + Gambol P6 + Hong Kong P7 + RICO P8 + Ultimatum P9 | 14-23 |
| `EP2_EC_03_Clarity.md` | Fundraiser C1 + Attacks C2 + Proposal C3 + Joker Crash C4 + Burma ★ C5 + Forensics C6 + Funeral C7 + Coin-flip C8 | 24-40 |
| `EP2_EC_04_Courage.md` | "I Am the Batman" K1 + Convoy K2 + Interrogation ★ K3 + Rachel Dies/Two-Face K4 | 41-57 |
| `EP2_EC_05_Commitment.md` | Money Burn M1 + Letter M2 + Hospital ★ M3 + Explosion M4 + Sonar ★ M5 + Revenge M6 + Ferry ★ M7 | 58-75 |
| `EP2_EC_06_Movement.md` | Prewitt V1 + Ace in Hole V2 + Two-Face Stand V3 + Dark Knight ★ V4 + Cost X1 + Arkham X2 + Bane X3 | 76-92 |
| `EP2_EC_07_PostCredits.md` | "This Was the Crisis" workplace parallel + 6 Transition Cards | 93-108 |

---
