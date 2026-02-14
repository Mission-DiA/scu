# SCU GEMINI PROMPT GUIDE
## Proven Patterns for Image Generation
### Version 4.0 | January 2026

---

## GOLDEN RULES

> **1. COMPLETE CHARACTER DESCRIPTIONS IN EVERY PANEL**
>
> Gemini does NOT maintain consistency between panels. You MUST include the FULL character description (face, body, hair, costume with HEX CODES, expression, action, position) for EVERY character in EVERY panel — even if identical to the previous panel.

> **2. COMPLETE ENVIRONMENT/DISPLAY SPECS IN EVERY PANEL**
>
> Never abbreviate display content or environment specs. Copy the COMPLETE specification into every panel. "Same as Panel 1" does NOT work.

> **3. UNIVERSE BACKDROP COLOR IN EVERY SLIDE**
>
> Each universe has a PRIMARY COLOR that must dominate the scene as ambient glow. Specify this explicitly in every environment block.

> **4. FOREGROUND POSITIONING FOR CHARACTERS**
>
> Characters must be explicitly positioned in FOREGROUND with framing type (waist-up, close-up, etc.) or Gemini will push them to the background.

> **5. NO EXTRA PROPS**
>
> Gemini hallucinates furniture and props. Explicitly state "NO desks, NO chairs, NO coffee cups, NO plants, NO extra props" in every prompt.

> **6. REFERENCE FINALIZED COSTUME TESTS (NEW - S1E5)**
>
> **NEVER improvise costumes.** Before generating ANY prompts, reference the finalized costume tests for each character in the universe. Copy EXACT specs — hair, top, bottoms, shoes, accessories.

---

## CRITICAL REQUIREMENTS

Every Gemini prompt for SCU MUST include these elements:

| Requirement | Why It Matters |
|-------------|----------------|
| "FULL BLEED" | Prevents white margins around image |
| "1-2 pixel thin white lines between panels" | Prevents thick ugly borders |
| **Costumes from finalized tests** | Prevents improvised/inconsistent costumes |
| **"NO lanyards, NO badges" unless in test** | Prevents unwanted accessories |
| **Complete character descriptions in EVERY panel** | Prevents character inconsistency |
| **Complete display/environment specs in EVERY panel** | Prevents content drift |
| **Universe backdrop color** | Establishes visual identity |
| **FOREGROUND positioning with framing** | Prevents characters pushed to background |
| **"NO extra props" instruction** | Prevents hallucinated furniture |
| "black text, white fill, black outline" for speech bubbles | Ensures readable dialogue |
| "cloud-like edges" for thought bubbles | Distinguishes thoughts from speech |
| ONE SPEAKER PER PANEL | Prevents dialogue attribution errors |
| SCU watermark specification | Ensures branding appears |
| CRITICAL section at end | Reinforces key requirements |
| 16:9 aspect ratio (1920x1080px) | Consistent slide dimensions |

---

## UNIVERSE COLOR PALETTES

Each universe has a PRIMARY COLOR that dominates the scene:

| Universe | Primary Color | Hex Code | Environment Block |
|----------|--------------|----------|-------------------|
| Prime (SHIELD) | Steel blue | #4A90D9 | "PRIME UNIVERSE: Blue holographic glow throughout" |
| Engineering | Matrix green | #00FF41 | "ENGINEERING UNIVERSE: Green screen glow throughout" |
| QA | Purple | #8B5CF6 | "QA UNIVERSE: Purple methodical lighting throughout" |
| DevOps | Orange | #F97316 | "DEVOPS UNIVERSE: Dominant ORANGE (#F97316) ambient glow throughout" |
| SRE | Red alert | #EF4444 | "SRE UNIVERSE: RED (#EF4444) alert lighting throughout" |
| Nexus | Golden | #FFD700 | "NEXUS: Golden ethereal glow, all universe colors blending" |

---

## MASTER PROMPT TEMPLATE (v4.0)

```
Create a FULL BLEED digital comic panel in Pixar-meets-MCU style at 16:9 aspect ratio (1920x1080px). The image must extend to ALL EDGES with NO outer margins, borders, or frames.

SCENE: [Brief scene description]

LAYOUT: [Panel configuration] with 1-2 pixel thin white lines between panels.

---

PANEL [X] ([width]% width, [position]):
[Shot type] — [Scene description]

[CHARACTER NAME] FULL DESCRIPTION:
- Face & Body: [Actor reference], [ethnicity], [age], [build], [height]
- Hair: [Description including style for this universe — FROM COSTUME TEST]
- Costume: [Full costume description with HEX CODES — FROM COSTUME TEST]
- Expression: [ONE clear emotional state — be specific]
- Action: [What they're doing physically]
- Position: FOREGROUND [LEFT/CENTER/RIGHT], [he/she] is the PRIMARY SUBJECT, [waist-up/close-up/full body] framing
- Body Language: [Specific posture notes if needed]
- Gaze Direction: [Where they're looking — at another character, at a screen, etc.]

ENVIRONMENT — [UNIVERSE] UNIVERSE:
- [UNIVERSE] UNIVERSE: Dark room with dominant [COLOR] (#HEX) ambient glow throughout
- [COLOR] (#HEX) is the PRIMARY UNIVERSE COLOR — walls, floor, atmosphere tinted [color]
- [Specific environment details]
- NO bright white lighting, NO daylight — dark room with [COLOR] glow only
- NO desks, NO chairs, NO coffee cups, NO plants, NO extra props

TEXT IN THIS PANEL:
- SPEECH BUBBLE from [Character] (white fill, black outline, black text): "[Dialogue]"
- Position: [upper left / upper right / lower left / lower right], tail points to [character's] mouth
- DO NOT include text from other panels.

---

STYLE REQUIREMENTS:
- Pixar-level 3D rendering with MCU tactical aesthetic
- [UNIVERSE] UNIVERSE LIGHTING: Dominant [COLOR] (#HEX) ambient glow throughout
- Comic book speech bubbles with black text, white fill, black outline
- Thought bubbles with cloud-like edges
- Caption boxes with dark blue (#1a1a4e) background, white text

SCU WATERMARK: Add subtle "SCU" text in bottom-left corner, white color, 2% of image width, 30% opacity.

---

CRITICAL:
- FULL BLEED — image extends to all edges, NO margins or borders
- Only 1-2 pixel thin white lines between panels
- Complete character descriptions repeated in EVERY panel — NO abbreviations
- Costumes match FINALIZED COSTUME TESTS — no improvisation
- NO lanyards, NO badges unless explicitly in costume test
- Complete display/environment specs in EVERY panel — NO shortcuts
- [UNIVERSE] UNIVERSE = [COLOR] (#HEX) — entire scene bathed in [color] ambient glow
- Characters in FOREGROUND — large, prominent, not pushed to background
- DO NOT add extra props: NO desks, NO chairs, NO laptops, NO coffee cups, NO plants
- ONE speaker per panel — do not mix dialogue from multiple characters
- TEXT IN THIS PANEL ONLY — do not duplicate text across panels
```

---

## GEMINI TROUBLESHOOTING PATTERNS (19 Patterns)

### Pattern 1: Narration vs Dialogue
**Issue:** Gemini confuses narrator voice (Watcher) with character speech
**Fix:** Use CAPTION BOXES for narration, explicitly state "NOT character dialogue"

### Pattern 2: Mixed Emotional Signals
**Issue:** Instructions like "trying to look X but feeling Y" create confused renders
**Fix:** Show emotion CLEARLY in isolation. One clear emotion per panel.

### Pattern 3: Multi-Speaker Panels
**Issue:** Back-and-forth dialogue in same panel causes attribution errors
**Fix:** ONE SPEAKER PER PANEL rule — increase panel count if needed

### Pattern 4: Desaturation Not Rendering
**Issue:** Character desaturation (Marcus in S1E2) doesn't render
**Fix:** Add EXPLICIT instructions with multiple phrasings — "grey filter", "40% reduced vibrancy", "faded, washed out"

### Pattern 5: Watermark Missing
**Issue:** SCU watermark not appearing
**Fix:** Explicitly add in both STYLE REQUIREMENTS and CRITICAL sections

### Pattern 6: Coulson Below Daisy
**Issue:** Coulson rendered at same level or below Daisy, undermining mentor authority
**Fix:** Add explicit hierarchy instruction — "Coulson must be positioned ABOVE Daisy"

### Pattern 7: Character Looks Different Between Panels
**Issue:** Same character looks different in different panels
**Fix:** Copy-paste the EXACT same character description block into every panel

### Pattern 8: Characters Pushed to Background
**Issue:** Characters rendered small, pushed to backdrop, not prominent
**Fix:** Add explicit FOREGROUND positioning with framing type and PRIMARY SUBJECT designation

### Pattern 9: Extra Props Appearing
**Issue:** Gemini adds random desks, chairs, coffee cups that weren't requested
**Fix:** Explicitly forbid extra props in ENVIRONMENT and CRITICAL sections

### Pattern 10: Boxer Stance / Aggressive Posture
**Issue:** "Leaning forward" or "direct gaze" makes mentor characters look aggressive
**Fix:** Use RELAXED, CONVERSATIONAL language for dialogue scenes

### Pattern 11: Gaze Direction Wrong
**Issue:** Characters looking at wrong thing or in wrong direction
**Fix:** Add explicit gaze direction instructions

### Pattern 12: Display Content Changing
**Issue:** Screen/display content inconsistent between panels
**Fix:** Copy COMPLETE display specification into EVERY panel

### Pattern 13: Light/Dark Mode Switching
**Issue:** Display switches between light and dark mode unexpectedly
**Fix:** Lock the mode explicitly in every display spec

### Pattern 14: Universe Color Missing
**Issue:** Scene lacks the universe's signature color
**Fix:** Add explicit universe backdrop instruction in ENVIRONMENT and CRITICAL

### Pattern 15: Two Locations Confused
**Issue:** Different screen types look identical
**Fix:** Create DISTINCT specifications with clear differentiators

### Pattern 16: Wrong Costume / Improvised Clothing
**Issue:** Character wearing costume that doesn't match finalized costume test
**Fix:** ALWAYS reference finalized costume tests before generating prompts. Never improvise.

### Pattern 17: Unwanted Lanyards / Badges
**Issue:** Characters rendered with lanyards or badges that weren't in the costume test
**Fix:** Explicitly forbid lanyards/badges in CRITICAL section

### Pattern 18: Multi-Universe Fragment Hallucination
**Issue:** Multiple universe fragments have inconsistent costumes
**Fix:** Include COMPLETE Daisy costume specification for EACH fragment

### Pattern 19: Dialogue Continuity Gap
**Issue:** Character responds to a question that was never asked
**Fix:** Check dialogue flow between consecutive slides during screenplay review

---

## TEXT HANDLING RULES

### Speech Bubbles
- Fill: White (#FFFFFF)
- Outline: Black (#000000), 2px
- Text: Black, bold
- Tail: Points to speaker's mouth
- ONE per character per panel

### Thought Bubbles
- Fill: White (#FFFFFF)
- Outline: Black (#000000), 2px
- Edges: Cloud-like, puffy (NOT pointed tail)
- Text: Black, italic

### Caption Boxes (Narration)
- Fill: Dark blue (#1a1a4e)
- Text: White
- Position: Top or bottom of panel
- NO tail (not attributed to visible character)

---

## QUALITY CHECKLIST v4.0

Before submitting to Gemini:

### Costume Check
- [ ] Referenced finalized costume test for this universe
- [ ] Hair description matches costume test (e.g., "low ponytail" not just "ponytail")
- [ ] Clothing matches costume test with exact hex codes
- [ ] Shoes match costume test
- [ ] Accessories match costume test (headset only for SRE)
- [ ] NO lanyards, NO badges unless in costume test

### Technical Check
- [ ] "FULL BLEED" in opening line
- [ ] "1-2 pixel thin white lines between panels"
- [ ] Universe backdrop color specified with hex code
- [ ] 16:9 aspect ratio (1920x1080px)

### Character Check
- [ ] Complete description in EVERY panel
- [ ] FOREGROUND positioning with framing type
- [ ] ONE speaker per panel
- [ ] Coulson positioned ABOVE Daisy

### Environment Check
- [ ] Universe color dominates scene
- [ ] Complete display specs in EVERY panel
- [ ] "NO extra props" instruction included
- [ ] Dark room with colored glow (not white lighting)

### Continuity Check
- [ ] Dialogue flows from previous slide
- [ ] Setup questions are asked before answers
- [ ] No gaps where characters respond to unasked questions

### Final Check
- [ ] SCU watermark specified
- [ ] CRITICAL section at end
- [ ] Key story beats reinforced
- [ ] No "same as Panel 1" shortcuts anywhere

---

## VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | January 2026 | Initial creation with 7 troubleshooting patterns |
| 2.0 | January 2026 | Added character copy blocks, tested patterns, quality checklist |
| 3.0 | January 2026 | S1E4 Overhaul: 8 new patterns (8-15), 5 Golden Rules, Universe Color Palettes |
| 4.0 | January 2026 | S1E5 Learnings: Golden Rule #6, 4 new patterns (16-19), corrected SRE costumes |

---

*Document: 06_SCU_gemini_prompt_guide.md*
*Version: 4.0*
*Project: Swami Cinematic Universe*
