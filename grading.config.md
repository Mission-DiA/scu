# Grading Engine — Configuration

> **Purpose:** Central config for Simmons' `/grade` command.
> **Edit this file** when submissions repo path changes or team members join.

---

## Submissions Source

| Setting | Value |
|---------|-------|
| **Submissions Repo Path** | `TBD` |
| **Blueprint File Pattern** | `blueprints/{name}.md` |
| **Full Blueprint Path** | `{submissions_repo}/blueprints/{name}.md` |

> **NOTE:** Update "Submissions Repo Path" once Director provides the shared repo location.
> Simmons will report "Submissions path not configured" until this is set.

---

## Team Roster

> Auto-populated on first grading. Add manually if needed.

| Name | Role | Joined | Notes |
|------|------|--------|-------|
| <!-- Add team members as they participate --> | | | |

---

## Phase Schedule

> Challenge starts Tuesday. One phase per day.
> Update start date when Director confirms.

| Phase | Day | Due Date | Max Score |
|-------|-----|----------|-----------|
| Phase 1: Foundation Audit (Q1-Q4) | Tue | TBD | 20 |
| Phase 2: Loop Map (Q5-Q8) | Wed | TBD | 20 |
| Phase 3: Self-Test (Q9-Q12) | Thu | TBD | 20 |
| Phase 4: Mentor Map (Q13-Q16) | Fri | TBD | 10 |
| Phase 5: Prevention Audit (Q17-Q20) | Mon | TBD | 10 |
| Phase 6: Architecture + Final (Q21-Q25) | Tue | TBD | 20 |

---

## File References

| File | Path |
|------|------|
| **Grading Rubric** | `bridging-the-gap-between-institution-and-industry/challenges/S2_Career_Blueprint_Challenge/S2_Grading_Rubric.md` |
| **Blueprint Template** | `bridging-the-gap-between-institution-and-industry/challenges/S2_Career_Blueprint_Challenge/S2_Blueprint_Template.md` |
| **Grading Tracker** | `bridging-the-gap-between-institution-and-industry/challenges/S2_Career_Blueprint_Challenge/GRADING_TRACKER.md` |
| **Feedback Directory** | `bridging-the-gap-between-institution-and-industry/challenges/S2_Career_Blueprint_Challenge/feedback/` |

---

## Grading Parameters

| Parameter | Value |
|-----------|-------|
| **Total Points** | 100 |
| **Phases** | 6 |
| **Authenticity Check** | 7-point LLM detection (run before scoring) |
| **1st Miss Penalty** | Warning only |
| **2nd Miss Penalty** | Phase max reduced by 20% |
| **3rd+ Miss Penalty** | Phase scores ZERO |
| **Cramming Penalty** | Both same-day phases take -20% |

---

*Last updated: 2026-03-02*
