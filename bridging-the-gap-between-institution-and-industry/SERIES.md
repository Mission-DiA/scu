# SCU — Mission Parameters

> **Project:** Swami Cinematic Universe — Bridging the Gap Series
> **Classification:** SHIELD Level 7
>
> **READ THIS FIRST. EVERY SESSION.**
> This file is the source of truth for project context.

---

## CLASSIFIED: Project Significance

**SCU** stands for **Swami Cinematic Universe** — a multiverse anthology series that transforms leadership and mentorship concepts into visual comic stories across parallel universes.

**Hidden Meaning (S.P. Protocol):** SCU also encodes **Sam Cinematic Universe** — a tribute to Sam Prasad (S.P.), the mentor whose philosophy forms the foundation of these stories. This is NEVER explicitly stated publicly; those who know, know. S.P. Easter eggs are scattered throughout episodes as subtle tributes.

---

## Team Configuration

| Agent | Role | Slash Command | Domain |
|-------|------|---------------|--------|
| **Coulson** | Director (Human) | N/A | Decisions, vision, final approval |
| **Jemma Simmons** | Creative Lead | `/simmons` | Story, screenplay, dialogue, Gemini prompts |
| **Melinda May** | Editor | `/may` | Accessibility, clarity, pacing, quality gate |

**Communication:** Async via `comms/` directory. Director coordinates between terminals.

**Tracking Files:**
| File | Owner | Purpose |
|------|-------|---------|
| `CREATIVE.md` | Simmons | Episode production, story development, prompt creation |
| `EDITORIAL.md` | May | Quality review, accessibility checks, publication readiness |

---

## Series Structure: 17 Seasons from Source

**Source:** "Bridging the Gap Between Institution & Industry" (2013 comic by iSwamiK)

### 5-PHASE NARRATIVE ARC

| Phase | Seasons | Theme | Daisy's State |
|-------|---------|-------|---------------|
| **THE AWAKENING** | S1-S4 | Entering professional world | "I don't know what I don't know" |
| **THE PRINCIPLES** | S5-S8 | Core philosophy | "Now I understand the rules" |
| **THE FORGE** | S9-S13 | Growth through challenge | "I'm being tested and growing" |
| **THE PHILOSOPHY** | S14-S15 | Deeper truths | "I see the deeper truth" |
| **THE TRANSFORMATION** | S16-S17 | Learner becomes mentor | "I become what my mentor was" |

### Current Production Status

| Season | Concept | PDF Page | Status |
|--------|---------|----------|--------|
| S1 | Do What YOU Want | p.3 | Complete |
| S2 | Build Career, Not Just Get Job | p.7 | Complete |
| S3 | College = Just Alphabets | p.8 | Complete |
| **S4** | **First Job = Foundation** | **p.9** | **Next** |
| S5-S17 | Remaining concepts | Various | Mapped |

**S4 Context:** "Your first job is like a foundation to a building!" — Final season of Phase 1: THE AWAKENING

---

## The 6 Universes

| Universe | Primary Color | Hex | Daisy Hair | Setting |
|----------|--------------|-----|------------|---------|
| **Prime** | Blue | #4A90D9 | HIGH PONYTAIL (mid-head) | SHIELD Command |
| **Engineering** | Green | #00FF41 | DOWN (loose) | Dev environments |
| **QA** | Purple | #8B5CF6 | HALF-UP (top secured) | Testing labs |
| **DevOps** | Orange | #F97316 | LOW BUN (nape) | CI/CD dashboards |
| **SRE** | Red | #EF4444 | LOW PONYTAIL (nape) | War rooms |
| **Nexus** | Gold | #FFD700 | Flowing | Cosmic convergence |

**CRITICAL:** Hair is the PRIMARY visual differentiator between Daisy variants. Always specify exact position (mid-head vs nape).

---

## 10 Production Rules (Non-Negotiable)

| # | Rule | Description |
|---|------|-------------|
| 1 | **ONE DIALOGUE PER SPEAKER** | Each character gets MAX one speech bubble per panel |
| 2 | **FULL CHARACTER BLOCKS** | Complete specs in EVERY panel — NO lazy references |
| 3 | **FULL BLEED** | Image extends to ALL edges, NO margins |
| 4 | **1-2px PANEL LINES** | Thin white lines between panels ONLY |
| 5 | **COULSON ABOVE DAISY** | Mentor positioned higher — standing when she sits |
| 6 | **UNIVERSE COLOR** | Each universe bathed in its primary color glow |
| 7 | **NO EXTRA PROPS** | Explicitly forbid desks, chairs, coffee cups |
| 8 | **FOREGROUND POSITIONING** | Characters large and prominent, not pushed back |
| 9 | **MARCUS DESATURATED** | 30-40% less color saturation — faded, ghostly |
| 10 | **SEATED/STANDING** | Always specify explicitly for continuity |

---

## Reference Files

| Document | Location | Purpose |
|----------|----------|---------|
| **Master Guide** | `reference/01_SCU_master_guide.md` | 17-concept breakdown, 5-phase arc |
| **Character Bible** | `reference/05_SCU_character_bible_v5.md` | Actor refs, costumes, hex codes |
| **Gemini Prompt Guide** | `reference/06_SCU_gemini_prompt_guide_v4.md` | 19 troubleshooting patterns |
| **Locked Character Blocks** | `reference/SCU_Locked_Character_Blocks_v2.md` | Copy-paste specs |
| **Production Learnings** | `reference/S1_Production_Learnings_v2.md` | 10 production rules |
| **S3 Handover** | `handover/SCU_S3_Handover_Document.md` | S3→S4 transition context |
| **Source PDF** | `core/bridging-the-gap-between-industry-and-institution.pdf` | Original 17 concepts |

---

## Repository Structure

```
/bridging-the-gap-between-institution-and-industry/
├── CLAUDE.md                  ← Mission parameters (this file)
├── CREATIVE.md                ← Simmons' production tracker
├── EDITORIAL.md               ← May's editorial tracker
├── .claude/commands/          ← Agent slash commands
├── comms/                     ← Inter-agent communication
├── core/                      ← Source PDF
├── reference/                 ← Production reference docs
├── handover/                  ← Season transition docs
└── image_prompts/             ← Episode prompt packages
    ├── S1/, S2/, S3/         ← Completed seasons
    └── S4/                    ← Next production
```

---

## S.P. Easter Egg Protocol

**Hidden in every episode, never explained:**

| Type | Example |
|------|---------|
| Slack message | "@sp: Good choice." |
| Code comment | "# SP's first rule: Do it YOUR way." |
| Document stamp | "Reviewed: S.P." |
| Photo label | "My mentor's mentor" |
| Form number | "FORM SP-117" |

---

## Production Pipeline

```
SOURCE CONCEPT → STORY → SCREENPLAY → GEMINI PROMPTS → IMAGES → EDITORIAL → PUBLISH
      ↑                                                              ↓
   (PDF)      ←←←←←←←←←← FEEDBACK LOOP ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←
```

| Phase | Owner | Deliverable |
|-------|-------|-------------|
| Source Analysis | Simmons | Concept extraction from PDF |
| Story Development | Simmons | Season arc, episode beats |
| Screenplay | Simmons | Scene-by-scene script with dialogue |
| Gemini Prompts | Simmons | Panel-by-panel image generation prompts |
| Editorial Review | May | Accessibility, clarity, effectiveness checks |
| Quality Gate | May | Final sign-off before image generation |

---

## Credits Format (Exact Text)

```
Created, Crafted & Made by @iSwamiK
In collaboration with Claude Code & Google Gemini
```

---

## Comms Protocol

| Agent | Inbox | Outbox |
|-------|-------|--------|
| Simmons | `comms/may-to-simmons/` | `comms/simmons-to-may/` |
| May | `comms/simmons-to-may/` | `comms/may-to-simmons/` |

**Primary Committer:** Simmons (commits all agent work during safehouse)

---

## Document Version

| Document | Version | Updated |
|----------|---------|---------|
| CLAUDE.md | 2.0.0 | 2026-02-14 |

---

*"Every story teaches. Every panel matters."* 🛡️
