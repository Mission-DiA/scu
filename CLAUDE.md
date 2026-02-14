# SCU Hub — Mission Parameters

> **Project:** Swami Cinematic Universe (SCU)
> **Classification:** SHIELD Level 7
>
> **READ THIS FIRST. EVERY SESSION.**
> This file is the source of truth for the SCU Hub.

---

## CLASSIFIED: Project Significance

**SCU** stands for **Swami Cinematic Universe** — a multiverse anthology platform that transforms leadership and mentorship concepts into visual comic stories across parallel universes.

**Hidden Meaning (S.P. Protocol):** SCU also encodes **Sam Cinematic Universe** — a tribute to Sam Prasad (S.P.), the mentor whose philosophy forms the foundation of these stories. This is NEVER explicitly stated publicly; those who know, know. S.P. Easter eggs are scattered throughout episodes as subtle tributes.

---

## Team Configuration

| Agent | Role | Slash Command | Domain |
|-------|------|---------------|--------|
| **Coulson** | Director (Human) | N/A | Decisions, vision, final approval |
| **Jemma Simmons** | Creative Lead | `/simmons` | Story, screenplay, dialogue, Gemini prompts |
| **Melinda May** | Editor | `/may` | Accessibility, clarity, pacing, quality gate |

**Communication:** Async via `comms/` directory (per series). Director coordinates between terminals.

---

## Hub Architecture

```
/scu/                              ← SCU HUB (run Claude Code HERE)
├── CLAUDE.md                      ← Hub context (this file)
├── active-series.txt              ← Currently active series (optional)
├── .claude/
│   └── commands/
│       ├── simmons.md             ← Shared Creative Lead command
│       └── may.md                 ← Shared Editor command
│
├── bridging-the-gap-between-institution-and-industry/
│   ├── SERIES.md                  ← Series-specific context
│   ├── CREATIVE.md                ← Simmons' tracker (this series)
│   ├── EDITORIAL.md               ← May's tracker (this series)
│   ├── comms/                     ← Inter-agent comms (this series)
│   ├── reference/                 ← Production docs (this series)
│   ├── handover/                  ← Season transitions
│   ├── core/                      ← Source material (PDF)
│   └── image_prompts/             ← Episode prompt packages
│
├── [future-series-2]/
│   ├── SERIES.md
│   └── ...
│
└── [future-series-3]/
```

---

## Active Series

**How to switch series:**
1. Director says: "Working on [series-name]"
2. OR create `active-series.txt` with the series directory name

**Default series:** `bridging-the-gap-between-institution-and-industry`

**Current series roster:**

| Series | Directory | Status |
|--------|-----------|--------|
| Bridging the Gap | `bridging-the-gap-between-institution-and-industry/` | Active (S1-S3 complete, S4 next) |

---

## Shared Production Rules (All Series)

These rules apply to ALL SCU series:

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

## The 6 Universes (Shared Across Series)

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

## S.P. Easter Egg Protocol (All Series)

**Hidden in every episode, never explained:**

| Type | Example |
|------|---------|
| Slack message | "@sp: Good choice." |
| Code comment | "# SP's first rule: Do it YOUR way." |
| Document stamp | "Reviewed: S.P." |
| Photo label | "My mentor's mentor" |
| Form number | "FORM SP-117" |

---

## Credits Format (Exact Text)

```
Created, Crafted & Made by @iSwamiK
In collaboration with Claude Code & Google Gemini
```

---

## Production Pipeline (All Series)

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

## Comms Protocol (Per Series)

| Agent | Inbox | Outbox |
|-------|-------|--------|
| Simmons | `[series]/comms/may-to-simmons/` | `[series]/comms/simmons-to-may/` |
| May | `[series]/comms/simmons-to-may/` | `[series]/comms/may-to-simmons/` |

**Primary Committer:** Simmons (commits all agent work during safehouse)

---

## Adding a New Series

To add a new series:

1. Create new directory: `[series-name]/`
2. Create `SERIES.md` with series-specific context
3. Create `CREATIVE.md` and `EDITORIAL.md` (copy structure from existing)
4. Create `comms/` directory structure
5. Create `reference/` with series-specific docs
6. Create `core/` with source material
7. Update this file's series roster

---

## Document Version

| Document | Version | Updated |
|----------|---------|---------|
| CLAUDE.md (Hub) | 1.0.0 | 2026-02-14 |

---

*"One universe. Many stories. Every panel matters."* 🛡️
