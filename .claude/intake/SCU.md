---
version: "1.0"
created: "2026-02-14"
status: active

mission_type: new
codename: "SCU"
objective: |
  The Swami Cinematic Universe (SCU) is a Marvel "What If?" style comic series that transforms
  real mentorship and career lessons into visual stories across five parallel universes — built
  entirely using human-AI collaboration (Claude + Gemini). Every season takes one concept from
  a 2013 comic called "Bridging the Gap Between Institution & Industry" and explores it through
  six episodes, each set in a different professional world (SHIELD ops, Engineering, QA, DevOps, SRE),
  all connected by a cosmic narrator called The Watcher. Three seasons are complete, seventeen
  are mapped — it's a leadership development tool disguised as a comic book universe.

  The first series within SCU is "Bridging the Gap Between Institution & Industry" — the source
  PDF at core/bridging-the-gap-between-industry-and-institution.pdf contains the 17 core concepts
  that drive this series.

agents:
  - id: simmons
    name: "Jemma Simmons"
    role: "Creative Lead"
    tracking_file: "CREATIVE.md"
    is_committer: true
    domain: "Story, screenplay, dialogue, Gemini prompts, character arcs, thematic depth"

  - id: may
    name: "Melinda May"
    role: "Editor"
    tracking_file: "EDITORIAL.md"
    is_committer: false
    domain: "Accessibility, clarity, pacing, reader experience, quality gate"

tech_stack:
  type: creative
  tools:
    - "Claude (screenplay, dialogue, story structure)"
    - "Gemini (image generation via prompts)"
    - "Markdown (documentation)"

repository:
  type: existing
  branch: main

comms:
  enabled: true
  primary_committer: "simmons"
  channels:
    - "simmons-to-may"
    - "may-to-simmons"

protocols:
  d3o: true
  safehouse: true
  tahiti: true
  shield_terminology: true
---

# Mission SCU — Intake Complete

This intake file captures the mission parameters for the Swami Cinematic Universe project.

## Team

| Agent | Role | Domain |
|-------|------|--------|
| Jemma Simmons | Creative Lead | Story, screenplay, dialogue, Gemini prompts |
| Melinda May | Editor | Accessibility, clarity, pacing, quality |

## Source Material

- `core/bridging-the-gap-between-industry-and-institution.pdf` — 17 core concepts
- `image_prompts/` — Existing seasons S1-S3 for reference

## Production Status

- Season 1: Complete
- Season 2: Complete
- Season 3: Complete
- Seasons 4-17: Mapped, awaiting production
