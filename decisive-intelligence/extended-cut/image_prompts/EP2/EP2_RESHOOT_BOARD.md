# EP2 — RESHOOT BOARD

> **Purpose:** Track slides that need prompt revision after Gemini test renders
> **Workflow:** Shoot forward, flag issues, circle back in a dedicated reshoot pass
> **Updated:** 2026-03-07
> **Version:** EC 3.0.0 (Ground-Zero v2 Rebuild — all prompts rewritten from scratch)

---

## How to Use

1. **During shooting:** If a slide renders wrong, log it here with the issue
2. **Keep moving:** Continue to the next slide — don't get stuck
3. **Reshoot pass:** After all slides are shot, return here and fix in batch
4. **Close out:** Move fixed slides to the Completed section

---

## OPEN — Awaiting Reshoot

| # | Slide | File | Issue | Attempts | Notes |
|---|-------|------|-------|----------|-------|
| — | — | — | No open reshoots. All prompts rebuilt from scratch in v2. | — | Ready for fresh test renders. |

---

## IN PROGRESS — Being Fixed

| # | Slide | File | Issue | Fix Applied |
|---|-------|------|-------|-------------|

---

## COMPLETED — Fixed and Verified

| # | Slide | File | Issue | Fix | Verified |
|---|-------|------|-------|-----|----------|
| — | 1 | EC_01 (v1) | "PRESENT"/"FLASHBACK" leaked as text | Renamed to scene-descriptive headers | Yes — v1 |
| — | 4 | EC_01 (v1) | Scale wrong, wrong masks, no actor, vault in lobby | Scale constraints, TDK masks, Fichtner cast, lobby-only | Yes — v1 |
| — | 5 | EC_01 (v1) | Disconnected panels | Rewritten as chain of betrayals | Yes — v1 |
| RS-001 | 7 | EC_01 (v1) | Batman POV not rendering — perspective issue | **SUPERSEDED** — EC_01 fully rewritten in v2. Old Slide 7 no longer exists in same form. | v2 rebuild |
| — | ALL | ALL | Director ordered ground-zero wipe of all EC prompt files | ALL files (EC_01-EC_07) deleted and rebuilt from scratch per EC 3.0.0 screenplay | v2 complete |

---

## RESHOOT PATTERNS

Recurring issues to watch for during shooting:

| Pattern | Slides Hit | Mitigation |
|---------|-----------|------------|
| POV/perspective shots | 7 | Gemini struggles with unusual camera angles — prefer standard eye-level or slightly elevated |
| Split panel connection | 5, 7 | Same moment/two angles works better than two separate moments |
| Scale in wide shots | 4 | Always add explicit size constraints for figures in architectural shots |

---

*"We'll fix it in post."* 🎬
