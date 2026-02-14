# Comms Directory — Inter-Agent Communication Protocol

> **Project:** SCU (Swami Cinematic Universe)
> **Purpose:** Async message exchange between agents, coordinated by Director Coulson.
> **Principle:** Context lives in files, not memory.

---

## Structure

```
comms/
├── README.md                 ← This file
├── simmons-to-may/           ← Simmons writes here (work for review)
├── may-to-simmons/           ← May writes here (editorial feedback)
├── threads/                  ← Multi-party/multi-day discussions
│   └── YYYY-MM-DD-topic/     ← One folder per thread
├── decisions/                ← Finalized decisions
└── archive/                  ← Closed threads and old comms
```

---

## Quick Reference

| Task | Location |
|------|----------|
| Simmons sends work for review | `comms/simmons-to-may/` |
| May sends editorial feedback | `comms/may-to-simmons/` |
| Start complex thread | `comms/threads/YYYY-MM-DD-topic/_index.md` |
| Record Director decision | `comms/decisions/` |

---

## Message Format

**Location:** `comms/simmons-to-may/YYYY-MM-DD-topic.md` (or reverse)

```markdown
---
topic: Short description
from: simmons | may
to: may | simmons
date: YYYY-MM-DD
urgency: info | request | blocking
status: open | closed
---

## YYYY-MM-DD HH:MM — Simmons

[Message — work submitted for review, question, etc.]

---

## YYYY-MM-DD HH:MM — May

[Response — feedback, approval, questions, etc.]
```

---

## Participants

| Type | Who | How They Contribute |
|------|-----|---------------------|
| **Agent** | Simmons, May | Write directly to comms/ |
| **Director** | Coulson | Writes directly + relays external input |
| **External** | Stakeholders | Director relays their input |

---

## Primary Committer

**Simmons** is the primary committer for this project.

- Simmons commits all comms/ changes during safehouse
- May writes files but does not commit directly
- For urgent commits, write a `blocking` message

---

## Urgency Levels

| Level | Meaning | Response Time |
|-------|---------|---------------|
| `info` | FYI only | When convenient |
| `request` | Input needed | Next session |
| `blocking` | Can't proceed without response | ASAP |

---

## Status Values

| Status | Meaning | Action |
|--------|---------|--------|
| `open` | Active discussion | Respond when able |
| `closed` | Resolved | Archive during safehouse |

---

## Lifecycle

```
Create → Exchange → Close → Archive
```

- Mark `status: closed` when resolved
- Move closed messages to `archive/` during safehouse
- Never delete — archive only

---

*"Context lives in files, not memory."* 🛡️
