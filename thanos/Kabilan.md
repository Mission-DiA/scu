# THE CAREER BLUEPRINT CHALLENGE

### Season 2: Build Career, Not Just Get Job

---

> **"'I want a job' is survival. 'I want to build my career' is the appropriate statement."**
> — The Watcher, S2E6

You've read Season 2. Six episodes. Six universes. Six lessons.

Now it's your turn. This isn't a quiz about the story — it's about YOUR career. The same questions Coulson asked Daisy, you'll answer about yourself. No hiding behind "right-sounding" answers. Be specific. Be honest. Be brutal.

**Deadline:** 1 week from today
**Time needed:** 60-90 minutes of genuine reflection
**What happens after:** You will present Phase 6 (Your Architecture) to the team and defend it. Your colleagues will ask the tough questions.

---

## YOUR DETAILS

- **Name:** Kabilan S
- **Current Role:** SRE
- **Years in Current Role:** 5 months
- **Date Submitted:** 3rd March 2026

---

## PHASE 1: THE FOUNDATION AUDIT
*From S2E1 — "That's what you finished. What did you build?"*

Coulson showed Daisy two agents. Same start date. Same effort. Different results. Agent A completed tasks. Agent B built systems, trained people, created frameworks.

### Q1. List your top 5 accomplishments from the last 6 months.

| # | Accomplishment |
|---|---------------|
| 1 | Built my own cost spending tracker without coding a single word using AI |
| 2 | Built a website that scrapes Chennai powercut schedules and sends Telegram alerts at 6am daily — https://minnal-srk.vercel.app/ |
| 3 | Used to write blogs and post learnings on LinkedIn and Medium, also as media manager at FabLab I used to learn some technical stuffs in 3D printing and laser cutting, but stopped |
| 4 | Explored many documentation tools at the beginning of my internship and identified Mintlify, but stopped exploration |
| 5 | Solved Tavern testing errors across all environments at my internship |

### Q2. Now be honest — for each one, mark it:

- **C** = Completed (you did the work, it's done, nothing remains)
- **B** = Built (it continues to create value without you actively doing it)

| # | C or B? | Why? |
|---|---------|------|
| 1 | B | Still using it daily to manage and track spends. My parents use it too. I'm planning to upgrade it with AI-powered spending analysis |
| 2 | B | The bot runs automatically every morning at 6am without me doing anything. The website continues to help anyone in Chennai check powercut schedules |
| 3 | C | Started writing blogs and posting on LinkedIn, then stopped completely after the commencement of internship |
| 4 | C | Explored and identified Mintlify as the right tool, then moved on to other work |
| 5 | C | Solved the testing errors and delivered the fix; not actively maintaining it anymore |

### Q3. If you disappeared tomorrow, which of those 5 things would still matter in 6 months? Why?

```
Two things would still matter:

1. Cost Tracker — My parents and I still use it daily to track our spending. Even if I stop maintaining it, the spending data we've logged shows our patterns and helps us understand where our money goes.

2. Powercut Bot — The Telegram bot runs automatically every morning at 6am without me doing anything. The website I built continues to help anyone in Chennai check their exact powercut schedules without depending on me to keep it running.
```

### Q4. What is your career INTENTION right now? Not your job title. Not your task list. What are you actively, deliberately building?

```
Building tools that solve real problems people face — not just finishing tasks assigned to me. Everyone struggles with metrics dashboards, and I want to be the one who builds something that actually works for them. I want to create tools that people use, tools that adapt to their needs, and tools that keep creating value without me having to maintain them every single day.
```

> **Gut check:** If you struggled to answer Q4, that IS the answer.

---

## PHASE 2: THE LOOP MAP
*From S2E2 — "You're shipping. You're not looping."*

Coulson showed Daisy the D3O loop: **Design → Develop → Deploy → Operate → back to Design.** She'd been stuck in Develop → Deploy. Shipping other people's designs. Never hearing what happened after.

### Q5. Think about your last major project or initiative. Map it to the D3O loop:

| D3O Stage | What YOU Did (be specific) | What SOMEONE ELSE Did |
|-----------|---------------------------|----------------------|
| **Design** (deciding WHAT to build and WHY) | Started: Aravindhan assigned the DOOR card with the requirement to automate Prowler (security findings validation). Now: Starting to own design decisions with Swami's guidance | Swami mentoring on design thinking; Aravindhan and Noordeen assigned the ticket and guided on problem-solving approach |
| **Develop** (building / executing it) | Coded the entire Prowler integration myself, using Claude to understand the framework and debug schema mappings with CIS 3.0 compliance | Claude assisted with code structure and debugging |
| **Deploy** (shipping / releasing / presenting it) | Created Jenkins pipeline and Cloud Run job for automation; configured cronjob scheduling and deployment workflow. Currently under verification with Deepika before production release | Deepika reviewing before production sign-off |
| **Operate** (monitoring, learning from results, feedback) | Monitoring it solo — watching security findings and learning how to rectify them by comparing with CIS 3.0 standards | No one else is monitoring this. Feedback comes directly in Google Space |

### Q6. Look at your map. Which stages are you dominant in? Which are empty?

```
Dominant stages: Develop and Deploy — I coded and deployed Prowler.

Empty/weak before: Design was completely assigned to me initially. I spent the first 2-3 months purely in Develop-Deploy — given a ticket, I executed it. No design involvement.

Growth happening NOW: In the last month with Swami's mentorship, I'm starting to own Design. For Custom Billing Dashboard, I'm now writing design docs, understanding requirements deeply, and suggesting approaches (like using MCP instead of HTTP to reduce cost). I'd estimate I'm now ~40% capable in Design and still improving. Still mostly Develop-Deploy, but the Design responsibility is growing.

Operate is all mine: I monitor what I build. That's different from before when I just shipped and moved on.
```

### Q7. Coulson told Daisy: "AI can do Develop-Deploy faster than any human now." What parts of YOUR work could AI do today? What parts require your judgment, your relationships, your context?

```
What AI can do in my SRE work:
- Log analysis and pattern matching (scan huge logs fast)
- Config generation for routine infrastructure (if context is set)
- Patch automation suggestions

What requires MY judgment and context:
1. Incident communication: Last Monday, ARIES was down. AI couldn't write customer-facing updates because it doesn't know: What info goes to customers vs. internal team? When should I post updates? What's safe to say publicly vs. technical details only for internal threads? I had to make these judgment calls. AI needs me to set context.

2. Architectural decisions: AI will suggest HTTP calls to fetch billing data. But I know our actual constraints: cost matters, latency matters. I proposed using MCP to collect from multiple clouds (GCP, AWS, Snowflake) and store in BigQuery, then serve via APIs. That reduces both cost and API calls. AI suggested the naive approach; I validated and improved it.

3. Runbooks: AI suggests steps, but I validate each one based on our actual infrastructure. Example: When Prowler crashed last month, AI said "clear the logs and restart the job." At first I believed it. But I knew we were in the middle of a compliance scan — restarting would break it. Instead, I fixed the schema mismatch that caused the crash, then restarted only after the scan completed. AI didn't know about the CIS validation window. I did.

AI is my assistant in these areas, not the decision-maker.
```

### Q8. When was the last time you shipped something that YOU designed — not something assigned to you?

```
At work: Prowler was assigned to me, not designed by me. But NOW — Custom Billing Dashboard is my first real design. It solves a real problem: teams need to see billing data from multiple clouds (GCP, AWS, Snowflake, MongoDB) in one place. I'm writing the design docs, making architectural choices, and proposing solutions. I'm not shipping it yet, but I'm starting to own the Design stage.

Personally: Minnal (September 2025) shows my design process. I identified a real problem: power cuts in Chennai. I couldn't remember when they'd happen, and I wanted alerts. I spent a week learning web scraping (Flask + parsing nested HTML), deployed to Vercel, and set up Telegram alerts at 6am. That took 1 week because I owned all 4 D3O stages.

Why the gap at work? Honestly, it's because I'm new (5 months). I've been learning the codebase, the infrastructure, the team processes. I spent the first 3 months just executing assigned tasks to get up to speed. Now, with Swami's mentorship, I have confidence to design. Custom Billing Dashboard is that inflection point.
```

---

## PHASE 3: THE SELF-TEST
*From S2E3 — "You have test plans for every feature. What's the test plan for your career?"*

Daisy had 94% automated coverage on her products and 0% on her own career. Coulson asked: "Would you ship a product with that test plan?"

### Q9. Where do you want to be in 2 years? (Be specific — title, responsibility, skill level)

```
[Your answer]
```

### Q10. Now write the acceptance criteria. How will you KNOW you're ready? Not "I feel ready" — measurable criteria.

| # | Acceptance Criteria | Current Status (Met / Partially / Not Met) |
|---|--------------------|--------------------------------------------|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |

### Q11. What are your edge cases — the risks that could derail your career path?

| # | Edge Case / Risk | Mitigation Plan |
|---|-----------------|-----------------|
| 1 | | |
| 2 | | |
| 3 | | |

### Q12. Coulson asked Daisy: "Would you ship a product with that test plan?" Looking at your answers above — would YOU?

```
[Your honest assessment]
```

---

## PHASE 4: THE MENTOR MAP
*From S2E4 — "You don't have to be an expert to help someone. You just have to be one step ahead."*

Viktor was scared his advice wasn't good enough. It was fumbling, confusing, imperfect — and it was exactly what Daisy needed. Because he was one step ahead.

### Q13. Who are you ONE STEP AHEAD of right now? (Name a real person or describe the type of person — a junior colleague, a new hire, someone in another team.)

```
[Your answer]
```

### Q14. What specific thing could you teach or share with them THIS week? Not next quarter. This week.

```
[Your answer]
```

### Q15. What has STOPPED you from mentoring or sharing so far? Be honest — is it time, fear of being wrong, not feeling expert enough, or something else?

```
[Your answer]
```

### Q16. Viktor said: "What if my advice is wrong? I'm still figuring this out myself." Have you ever held back from helping someone because you didn't feel qualified? What happened?

```
[Your answer]
```

---

## PHASE 5: THE PREVENTION AUDIT
*From S2E5 — "You're not building your replacement. You're building your ladder."*

Daisy had the fastest incident response on the team. Three SEV-1s in a month, all handled under 4 minutes. Same root cause. She was winning battles in a war she never tried to end.

### Q17. What are you doing repeatedly at work that you could prevent, automate, or delegate? List 3 recurring tasks that eat your time.

| # | Recurring Task | How Often | Could Be: Prevented / Automated / Delegated? |
|---|---------------|-----------|----------------------------------------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |

### Q18. If you automated or delegated those 3 things, what would you do with the freed time? (Not "more of the same" — what HIGHER problem would you work on?)

```
[Your answer]
```

### Q19. Are you a firefighter or an architect right now? Firefighters fight the same fires forever. Architects automate the known to hunt the unknown.

```
[Your honest answer — and what would need to change to shift]
```

### Q20. What's your biggest fear about automating or delegating your current work? Is it that you'll be replaced, or is it something else?

```
[Your answer]
```

---

## PHASE 6: YOUR ARCHITECTURE
*From S2E6 — "You are the architect. In every universe. Build accordingly."*

This is the one you'll present to the team. All five phases led here.

### Q21. YOUR CAREER BLUEPRINT

Fill in your personal architecture. Be specific — no vague aspirations.

```
                    MY CAREER ARCHITECTURE
                           │
      ┌──────────┬─────────┼─────────┬──────────┐
      │          │         │         │          │
      ▼          ▼         ▼         ▼          ▼
  FOUNDATION   D3O LOOP  TEST PLAN  MENTORING  PREVENTION
      │          │         │         │          │
  [What am I  [Which    [What are  [Who am I  [What fires
   building   stages do  my accept- one step   am I still
   with       I need to  ance       ahead of   fighting
   intention?] own next?] criteria?] & how?]    repeatedly?]
      │          │         │         │          │
      ▼          ▼         ▼         ▼          ▼
  ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐
  │        │ │        │ │        │ │        │ │        │
  │[FILL]  │ │[FILL]  │ │[FILL]  │ │[FILL]  │ │[FILL]  │
  │        │ │        │ │        │ │        │ │        │
  └────────┘ └────────┘ └────────┘ └────────┘ └────────┘
```

### Q22. What is the ONE THING you will do differently starting this week — not this quarter, not "eventually" — THIS WEEK?

```
[Your answer — be specific enough that someone could verify it happened]
```

### Q23. Complete this sentence:

> "I've been ________________. Now I'm going to ________________."

---

## FINAL REFLECTION

### Q24. Which episode hit you the hardest? Why?

```
[Your answer]
```

### Q25. Was there a specific scene or dialogue that made you stop and think about your own work life? Describe the moment and what it triggered in you.

```
[Your answer]
```

### Q26. If you had to explain Season 2 to a colleague who hasn't read it — not the plot, but why it matters — what would you tell them?

```
[Your answer]
```

### Q27. What did Season 2 make you feel or realize that Season 1 didn't? What changed between reading the first season and finishing this one?

```
[Your answer]
```

### Q28. If you were creating Season 3, what would you keep exactly as is — and what would you do differently?

**Keep as is:**
```
[Your answer]
```

**Do differently:**
```
[Your answer]
```

### Q29. Which question in this blueprint was the hardest to answer? What does that tell you?

```
[Your answer]
```

---

> **Remember:** You will present Phase 6 (Your Architecture) to the team. They will ask questions. The goal isn't to have perfect answers — it's to have honest ones.
>
> *"Same bricks. Same effort. Different result."* — Coulson, S2E1

---

**Submit to:** Director Coulson
**Deadline:** [DATE]
