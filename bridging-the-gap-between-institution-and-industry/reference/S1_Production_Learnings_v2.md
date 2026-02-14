# SCU SEASON 1 — PRODUCTION LEARNINGS
## Master Reference Document
### Version 2.0 | January 2026

---

## PURPOSE

This document captures all production learnings from Season 1 that should be applied to:
1. Any Season 1 episode files that need updating
2. All Season 2 (and beyond) episode development
3. The Gemini Prompt Guide artifact

---

## UNIVERSAL PRODUCTION RULES

### Rule 1: ONE DIALOGUE PER SPEAKER PER PANEL

**The Problem:** Gemini gets confused when one character has multiple speech bubbles in the same panel — it can't determine which bubble belongs to whom.

**The Rule:**
- Multiple characters CAN speak in the same panel
- Each character gets a MAXIMUM of ONE speech bubble per panel
- If a character needs to say more, split into multiple panels

**Example — WRONG:**
```
SPEECH BUBBLE from Coulson: "Here's the thing about fear."
SPEECH BUBBLE from Coulson: "It never asks permission."
```

**Example — CORRECT:**
```
PANEL 1:
SPEECH BUBBLE from Coulson: "Here's the thing about fear."

PANEL 2:
SPEECH BUBBLE from Coulson: "It never asks permission."
```

---

### Rule 2: LOCKED CHARACTER BLOCKS

**The Problem:** Inconsistent character appearances across panels when specs are abbreviated or referenced lazily.

**The Rule:** Every character needs COMPLETE specs copy-pasted into EVERY panel where they appear. NO shortcuts like "same as Panel 1" or "Daisy (as before)".

**Locked Block Format:**
```
[CHARACTER NAME] FULL DESCRIPTION:
- Face & Body: [Actor], [ethnicity], [age], [build], [height]
- Hair: [Specific style with EXACT terminology]
- Costume: [Full costume with hex colors]
- Expression: [Specific to scene]
- Action: [Specific to scene]
- Position: [Specific to scene]
```

---

### Rule 3: TIERED WATERMARK SYSTEM

**Cover & End Card (PROMINENT):**
```
=== SCU BRANDING — PROMINENT (COVER/END SLIDE) ===

WATERMARK:
• Text: "SCU"
• Position: Bottom-left corner, approximately 20 pixels from edges
• Color: Deep red (#8B0000) with gold (#FFD700) outline/glow
• Size: 3% of image width
• Opacity: 85% — clearly visible, part of the design
```

**Story Slides (SUBTLE):**
```
=== SCU BRANDING — SUBTLE (STORY SLIDE) ===

WATERMARK:
• Text: "SCU"
• Position: Bottom-left corner
• Color: White or light grey (#CCCCCC)
• Size: 2% of image width
• Opacity: 30-40% — subtle, like a TV network bug
```

---

### Rule 4: NATURAL LANGUAGE FOR GEMINI

**The Problem:** Gemini sometimes renders technical terms as visible text in images.

**The Rule:** Use natural language in the main prompt body. Move technical specs to a separate section at the end.

**Words to AVOID in main prompt:**
- "FULL BLEED" → Use: "image extends to all edges"
- "30% opacity" → Use: "subtle", "faint", "barely visible"
- "1920x1080px" → Use: "16:9 aspect ratio"
- Technical hex codes in descriptions → Use: color names with hex in parentheses

---

### Rule 5: HAIRSTYLE DISTINCTIONS

**The Problem:** Different Daisy variants looked too similar because hairstyle differences weren't explicit enough.

**The Rule:** Use EXACT terminology for hairstyle positions:

| Variant | Hairstyle | Key Terminology |
|---------|-----------|-----------------|
| Prime | HIGH PONYTAIL | "at MID-HEAD level" |
| Engineering | DOWN | "completely loose, natural, free-flowing" |
| QA | HALF-UP | "TOP half secured at crown, BOTTOM half loose" |
| DevOps | LOW BUN | "at NAPE OF NECK (back of head)" |
| SRE | LOW PONYTAIL | "at NAPE OF NECK (NOT mid-head)" |

**Critical:** Always specify WHERE on the head (mid-head vs nape) to prevent confusion.

---

### Rule 6: CREDITS FORMAT

**Correct Format:**
```
"Created, Crafted & Made by @iSwamiK"
"In collaboration with Claude Code & Google Gemini"
```

**Common Errors:**
- ✗ "Created & Made by @iSwamiK" (missing "Crafted")
- ✗ "In collaboration with Claude Code & Gemini" (missing "Google")

---

### Rule 7: EXPLICIT CHARACTER COUNTS

**The Problem:** Gemini sometimes adds extra characters (2 Watchers, 6 Coulsons when only 5 intended).

**The Rule:** State exact counts multiple times in complex scenes.

**Example:**
```
**CHARACTER COUNT — CRITICAL:**
- Exactly FIVE (5) Daisys — no more, no less
- Exactly FIVE (5) Coulsons — no more, no less
- Exactly ONE (1) Watcher — no more, no less
- Total: 11 characters exactly
```

---

### Rule 8: VISUAL HIERARCHY IN GROUP SCENES

**The Rule:** When multiple characters appear, specify:
1. Rendering quality (opacity percentage)
2. Position (foreground/background)
3. Focus level (sharp vs soft)

**Example:**
```
**VISUAL HIERARCHY:**
- FOREGROUND (100% opacity, SHARP): Five Daisys with golden light
- BACKGROUND (70% opacity, soft): Five Coulson silhouettes
- ABOVE (80% opacity): One Watcher observing
```

---

### Rule 9: NO LAZY REFERENCES

**The Problem:** Gemini hallucinates wrong characters when prompts use lazy references like "silhouette visible," "visible in background," or "partially visible" without full character specifications.

**The Rule:** ANY time a character appears in a panel — foreground, background, silhouette, fragment, reflection, photo, or any visibility level — include the FULL character block.

**Lazy References to AVOID:**
- ✗ "Daisy's silhouette visible working"
- ✗ "Coulson visible in background"
- ✗ "Daisy partially visible in frame"
- ✗ "Someone struggling visible"
- ✗ "same as Panel 1"
- ✗ "Daisy (as before)"

**Common Scenarios Requiring Full Specs:**
| Scenario | Still Needs Full Description? |
|----------|------------------------------|
| Character in foreground | ✓ YES |
| Character in background | ✓ YES |
| Character as silhouette | ✓ YES |
| Character in universe fragment/bubble | ✓ YES |
| Character in reflection | ✓ YES |
| Character in photo on desk | ✓ YES |
| Character partially visible | ✓ YES |

---

### Rule 10: SEATED/STANDING CONTINUITY

**The Problem:** Gemini hallucinates character positions, causing disconnected panels where characters appear to teleport between sitting and standing.

**The Rule:** Explicitly define SEATED or STANDING for every character in every panel, and maintain logical flow across conversation sequences.

**Pattern for Natural Conversation Flow:**
```
Panel 1: Character A STANDING (approaching), Character B SEATED at desk
Panel 2: Character A still STANDING, Character B SEATED (swivels to face A)
Panel 3: Character A SITTING DOWN (pulling up chair), Character B SEATED
Panel 4+: Both SEATED (equals in conversation)
Final Panel: Character A STANDING UP to leave, Character B SEATED
```

**Lock Props Across Panels:**
- Define desk, chair, monitors ONCE in a props section
- Reference same props in every panel of that scene
- Prevents environment inconsistency

---

## UNIVERSE COLOR PALETTE (Quick Reference)

| Universe | Primary Color | Hex | Lighting |
|----------|--------------|-----|----------|
| Prime | Blue | #4A90D9 | Tactical, SHIELD blue |
| Engineering | Green | #00FF41 | Matrix green, dark IDE |
| QA | Purple | #8B5CF6 | Clean, methodical |
| DevOps | Orange | #F97316 | Dark room, orange glow |
| SRE | Red | #EF4444 | Alert, war room |
| Nexus | Golden | #FFD700 | Cosmic, transcendent |

---

## SUPPORTING CAST REFERENCE

| Character | Actor | Universe | First Appearance | Notes |
|-----------|-------|----------|------------------|-------|
| Marcus | Paul Giamatti | Engineering | S1E2 | Senior Principal Engineer, nearly two decades experience |
| Viktor | Stephen Root | DevOps | S1E4 | |
| Alex | Oscar Isaac | SRE | S1E5 | |
| Priya | Mindy Kaling | SRE | S1E5 | |
| Jordan | Awkwafina | SRE | S1E5 | |
| Mike | Sam Rockwell | SRE | S1E5 | |

---

## S.P. EASTER EGG PLACEMENTS (Season 1)

| Episode | Location | Easter Egg |
|---------|----------|------------|
| S1E1 | Slide 10, Panel 3 | "FORM SP-117" or stamp "Reviewed: S.P." |
| S1E2 | Slide 10, Panel 4 | "@sp: Good choice." Slack message |
| S1E3 | TBD | TBD |
| S1E4 | TBD | TBD |
| S1E5 | TBD | TBD |
| S1E6 | Slide 22 (Post-Credit) | Watcher holds file labeled "S.P. ARCHIVES" |

---

## VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | January 2026 | Initial production learnings from S1 |
| 2.0 | January 2026 | Added Rule 9 (NO LAZY REFERENCES), Rule 10 (SEATED/STANDING CONTINUITY), Marcus experience note |

---

*Document: S1_Production_Learnings.md*
*Version: 2.0*
*Project: Swami Cinematic Universe*
