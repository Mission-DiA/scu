# DECISIVE INTELLIGENCE — EPISODE 1: THE FOUNDATION
## Director's Extended Cut — Gemini Image Generation Prompts

> **Version:** EC 1.0.0
> **Date:** 2026-02-21
> **Total Slides:** ~140 (main story + post-credits + transition cards)
> **Duration:** ~35 min story + ~5 min post-credits
> **Visual Style:** Dark Knight noir — photorealistic, high-contrast, Nolan-esque cinematography
> **Aspect Ratio:** 16:9 (1920×1080px)
> **Source:** EP1_FOUNDATION_Extended_Screenplay.md (EC 1.2.0 — 168 panels)

---

## PRODUCTION RULES

1. **FULL BLEED** — Image extends to ALL edges, NO margins
2. **1-2px PANEL LINES** — Thin white lines between panels ONLY (for multi-panel compositions)
3. **FULL CHARACTER BLOCKS** — Complete specs in EVERY prompt — NO lazy references
4. **ONE DIALOGUE PER SPEAKER** — Each character gets MAX one speech bubble per panel
5. **MAX 2 TEXT ELEMENTS** — 1 caption + 1 speech OR 2 captions per slide
6. **PHOTOREALISTIC STYLE** — Dark Knight noir aesthetic throughout
7. **SILHOUETTE APPROACH** — Young Bruce (child) depicted as SHADOW only, no face detail
8. **ADULT FOCUS** — Thomas Wayne, Alfred, Gordon carry emotion; child is abstract presence
9. **ACTOR NAMES IN ALL CHARACTER BLOCKS** — Prevents wrong actor renders
10. **SPEAKER MUST BE VISIBLE** — If a character has a speech bubble, they must appear in the panel

---

## TEXT STYLING REFERENCE

| Element | Fill | Text | Outline | Notes |
|---------|------|------|---------|-------|
| Speech Bubbles | White (#FFFFFF) | Black, bold | Black (#000000), 2px | Tail points to speaker |
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
| **Split panel** | Two related moments (contrast, before/after) | 2 |
| **Vertical triptych** | Three sequential moments (fall, transformation) | 3 |
| **Quad (2×2)** | Montage, parallel action, progress | 4 |
| **6-panel grid (2×3)** | Training montage, combat sequence | 6 (max) |

**Rule: Key moments get single panels. Montage/training can compress.**

---

## GEMINI COMPATIBILITY NOTES

1. **Actor names are REQUIRED** for correct likeness — generic descriptions render wrong actors
2. **"WHAT NOT TO DRAW"** sections prevent Gemini from filling in wrong defaults
3. **Camera angle specs** (FROM BELOW, FROM INSIDE) dramatically improve composition
4. **ONE moment per panel** — never two events in same panel
5. **Full character blocks in EVERY panel** — vague bullets = wrong costumes
6. **"Robert Downey Jr." works; "RDJ" gets blocked** — always use full names
7. **Gemini leaks descriptive prompt language as visible text** — strip adjectives
8. **"NO other text" instruction prevents hallucinated captions**
9. **Speaker must be VISIBLE** for speech bubbles — off-panel attribution fails
10. **One speaker per panel rule** — confirmed across all episodes
11. **Silhouette approach for minors** — proven safe in KLP v3
12. **Max 2 text elements per panel** — more causes garbled output
13. **Actor name + role context bypasses blocks** — `"Gary Oldman as a young police sergeant"` passes; bare `"Gary Oldman"` gets blocked. Always pair actor name with fictional role.
14. **Silhouette needs explicit exclusions** — `"silhouette"` alone still renders skin/hair. Must add: `"NO skin tone, NO hair detail, NO facial features, NO clothing detail, pure black shape"`
15. **Opacity percentages leak as visible text** — `"25-30% opacity"` renders literally. Use `"nearly invisible, faded white"` instead — no numbers for Gemini to print.

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

| # | Section | Scenes | Est. Slides | Technique |
|---|---------|--------|-------------|-----------|
| 0 | Cover | 0.1 | 1 | Single splash |
| 1 | The Fall | 1-2 | 10 | Mix of triptych, single, split |
| 2 | The Journey | 3-4 | 8 | Singles + grid |
| 3 | The Training | 5-6B | 7 | Grid + singles |
| 4 | Philosophy | 7-13 | 14 | Singles + splits |
| 5 | CLARITY (Pivotal) | 14 | 10 | Singles (protected) |
| 6 | COURAGE (Pivotal) | 15-16 | 10 | Singles (protected) |
| 7 | COMMITMENT (Pivotal) | 17 | 9 | Singles (protected) |
| 8 | Escape | 18 | 4 | Triptych + singles |
| 9 | Return + Fox | 19-19B | 8 | Singles + splits |
| 10 | Birthday / Reveal | 20 | 6 | Singles (emotional) |
| 11 | Manor Burns (MOVEMENT) | 21 | 6 | Singles (protected) |
| 12 | Batman Emerges | 22-22B | 6 | Singles + triptych |
| 13 | Train Fight (ALL FOUR) | 23-24 | 12 | Singles (climax) |
| 14 | Closing | 25-26 | 10 | Singles + end cards |
| 15 | Post-Credits | WP 1-15 | 13 | Singles |
| 16 | Transition Cards | TC 1-6 | 6 | Text cards |
| | **TOTAL** | | **118** | |

---

## FILE INDEX

| File | Content | Slides |
|------|---------|--------|
| `EP1_EC_00_Header.md` | Production rules, text styling, Gemini notes | — |
| `EP1_EC_01_Cover_and_Fall.md` | Cover + Scenes 1-2 (The Fall) | 0-10 |
| `EP1_EC_02_Journey_Training.md` | Scenes 3-6B (Journey + Training) | 11-21 |
| `EP1_EC_03_Philosophy_Clarity.md` | Scenes 7-14 (Philosophy + CLARITY) | 22-41 |
| `EP1_EC_04_Courage_Commitment_Escape.md` | Scenes 15-17 (COURAGE + COMMITMENT) | 42-57 |
| `EP1_EC_05_Return_Birthday_Movement.md` | Scenes 18-21 (Escape + Return + Birthday + MOVEMENT) | 58-72 |
| `EP1_EC_06_Batman_Train_Closing.md` | Scenes 22-26 (Batman + Train Fight + Closing) | 73-98 |
| `EP1_EC_07_PostCredits_TransitionCards.md` | Post-Credits Workplace Story + Transition Cards | 99-117 |
| `EP1_EC_08_Summary.md` | Production summary, verification, version history | — |

---

