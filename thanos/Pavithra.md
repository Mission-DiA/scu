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

- **Name:** Pavithra V
- **Current Role:** DevOps Engineer
- **Years in Current Role:** 5 
- **Date Submitted:** March 3, 2026

---

## PHASE 1: THE FOUNDATION AUDIT
*From S2E1 — "That's what you finished. What did you build?"*

Coulson showed Daisy two agents. Same start date. Same effort. Different results. Agent A completed tasks. Agent B built systems, trained people, created frameworks.

### Q1. List your top 5 accomplishments from the last 6 months.

| # | Accomplishment |
|---|---------------|
| 1 | Led major cost-optimization initiatives (GCP & AWS), achieving over $3,950/month in recurring savings through secrets cleanup, namespace optimization, and SQL instance decommissioning. |
| 2 | Executed Kissflow-v4 artifact repository cleanup, reducing storage by ~70% (from 815 GB) and cutting monthly costs from ~$85 to ~$25. |
| 3 | Successfully conducted the half-yearly MongoDB restoration drill, validating backup integrity and improving disaster recovery readiness. |
| 4 | Building a Jenkins PBR Build Status Tracker — a fully automated CI/CD pipeline that aggregates PROD, BLOM, and SCG Jenkins build statuses via GCP Cloud Functions and Firestore, and auto-completes Kissflow cards with zero manual intervention. (In Progress) |
| 5 | Actively leveraging AI in daily DevOps tasks and continuously learning new tools to improve efficiency and stay current with evolving technologies. |

### Q2. Now be honest — for each one, mark it:

- **C** = Completed (you did the work, it's done, nothing remains)
- **B** = Built (it continues to create value without you actively doing it)

| # | C or B? | Why? |
|---|---------|------|
| 1 | B | I completed the cost optimization, and the changes are still in use. Some resources are paused and can be resumed when needed. The steps are documented, so it continues to create savings without rework |
| 2 | B | The cleanup was completed, and I enabled policies so no manual intervention is needed. Storage reduction and cost savings continue automatically.|
| 3 | C | The drill was conducted earlier but was not documented properly. Now I have documented it clearly, so it can be repeated easily and creates long-term value |
| 4 | B | This is actively being built — once complete, the system will run automatically with no manual steps. It will continue to deliver value by removing the need for manual Kissflow card updates after every production build. |
| 5 | B | I actively use AI tools in daily operations which continues to improve my efficiency. New tools learned get applied directly to DevOps work, creating ongoing value beyond just personal growth. |

### Q3. If you disappeared tomorrow, which of those 5 things would still matter in 6 months? Why?

```
My documentation in Coda ensures a smooth handover, but the true lasting value comes from the automated systems I built. The cost-saving policies and security configurations (#1, #2, #4) would continue to run and deliver value automatically, saving money and protecting the system long after I'm gone. Those built systems are what would still matter.
```

### Q4. What is your career INTENTION right now? Not your job title. Not your task list. What are you actively, deliberately building?

```
My current career intention is to move beyond simply completing tasks and instead build deep technical understanding and ownership. I want to contribute at a design and decision-making level, not just at an operational level. Want to become Senior Technical Engineer. 
```

> **Gut check:** If you struggled to answer Q4, that IS the answer.

---

## PHASE 2: THE LOOP MAP
*From S2E2 — "You're shipping. You're not looping."*

Coulson showed Daisy the D3O loop: **Design → Develop → Deploy → Operate → back to Design.** She'd been stuck in Develop → Deploy. Shipping other people's designs. Never hearing what happened after.

### Q5. Think about your last major project or initiative. Map it to the D3O loop:

| D3O Stage | What YOU Did (be specific) | What SOMEONE ELSE Did |
|-----------|---------------------------|----------------------|
| **Design** (deciding WHAT to build and WHY) | Took ownership of the problem, defined the goals, drove the design direction, and produced the design document with AI assistance. Completed. | Noordeen identified the problem (manual Kissflow card updates after every prod build with wrong status). Claude (AI) helped structure and document the design. Aravind gave suggestions on the some areas. |
| **Develop** (building / executing it) | POC completed. Main Cloud Functions code is done (Jenkins API polling for PROD, BLOM, SCG, Firestore writes, Kissflow auto-completion logic). Currently integrating it with the Jenkinsfile. In Progress. | Claude (AI) assists with code generation and problem-solving throughout development. |
| **Deploy** (shipping / releasing / presenting it) | Not yet done. Next step — integrating Jenkins with the Kissflow PBR process and validating the end-to-end flow in a real environment. | Will involve DevOps team review before production rollout. |
| **Operate** (monitoring, learning from results, feedback) | Not yet reached. Once deployed, will monitor Cloud Function logs, Firestore writes, and Kissflow card updates to ensure the system runs without manual intervention. | End users (DevOps/Dev team) will operate and benefit from auto-completed Kissflow cards. |

### Q6. Look at your map. Which stages are you dominant in? Which are empty?

```
Dominant: Design and Develop.

Design — I took full ownership here. Even though Noordeen identified the problem, I chose
to act on it, defined the solution, structured the architecture, and produced the design
document. That ownership mindset is what separates completing tasks from building systems.

Develop — This is where I am spending most of my time right now. I built the POC,
completed the main Cloud Functions code, and am now integrating it with the Jenkinsfile.
I am not just executing someone else's instructions — I am making real technical decisions
at every step. This is my strongest stage.

Empty (not yet reached): Deploy and Operate.

Deploy — I haven't shipped anything to end users yet. The system exists, but no one is
using it in production. Until it goes live, it has created zero real-world impact.

Operate — This is completely blank. I have no feedback from users, no production metrics,
no signal on whether the system actually works as expected at scale. This is the most
critical gap — without Operate, there is no loop back to Design, which means I am still
shipping, not looping.

The honest takeaway: I am strong at building but I haven't closed the D3O loop yet.
The value of this project will only be proven once it is deployed and operating — and
that's the part I still need to own and push through.
```

### Q7. Coulson told Daisy: "AI can do Develop-Deploy faster than any human now." What parts of YOUR work could AI do today? What parts require your judgment, your relationships, your context?

```
Honestly, AI already does a big part of my Design and Develop work — and I use it deliberately.
I have fed my complete Kissflow infrastructure knowledge to AI, and because of that context,
it can write Python scripts, debug issues, generate Cloud Functions code, and suggest fixes
faster than I could do alone. That's real, and I won't pretend otherwise.

But what AI cannot do is decide what to build in the first place. Every time I say
"can you do this?" — that direction comes from me. My knowledge of the system, my
understanding of what's broken, my call on what's safe to change in production — that
is what AI depends on. Without my input, it has nothing to work with.

What still requires my judgment is knowing which problem matters, understanding the
Kissflow infra history, and validating whatever AI produces. AI can be wrong, and my
domain knowledge is what catches it. So while AI accelerates my execution, the thinking
that drives it — and the accountability for what gets deployed — is always mine.
```

### Q8. When was the last time you shipped something that YOU designed — not something assigned to you?

```
The GCS bucket size check automation. Around 30 cards had been raised over the years
for the same manual gsutil task. I noticed the pattern, took the initiative to automate
it as a self-service Jenkins job via the JYT process, and started building it without
being asked.

But it is still in progress — not shipped yet. Honestly, before this I cannot clearly
recall shipping something fully self-designed end-to-end. That is the truth.
```

---

## PHASE 3: THE SELF-TEST
*From S2E3 — "You have test plans for every feature. What's the test plan for your career?"*

Daisy had 94% automated coverage on her products and 0% on her own career. Coulson asked: "Would you ship a product with that test plan?"

### Q9. Where do you want to be in 2 years? (Be specific — title, responsibility, skill level)

```
Title: Senior DevOps Engineer

Responsibility:
Right now I am in a learning-and-doing phase — I execute well, I build
systems, but I still rely on direction from others for scope and priorities.
In 2 years, I want to be the person who defines the scope. I want to own
infrastructure decisions end-to-end — not just the Develop stage, but the
full D3O loop: Design → Develop → Deploy → Operate → back to Design.

Skill Level:
Today I am strong at building and designing, but Deploy and Operate are
gaps. In 2 years, I want those gaps closed. I want to be proficient in
production deployments, incident response patterns, and reading operational
signals to improve what I originally designed. I also want to be confident
enough to review and guide others' work — not just do my own.
```

### Q10. Now write the acceptance criteria. How will you KNOW you're ready? Not "I feel ready" — measurable criteria.

| # | Acceptance Criteria | Current Status (Met / Partially / Not Met) |
|---|--------------------|--------------------------------------------|
| 1 | Led at least one project through the full D3O loop — designed, deployed to production, and monitored post-deployment independently | Partially — strong in Design + Develop, Deploy and Operate not yet done |
| 2 | Build a clear understanding of concepts before implementing — not just executing but knowing why | Partially |
| 3 | Drive and share knowledge when someone asks — able to explain and guide without hesitation | Met |
| 4 | Take complete ownership of what I am doing — not just executing tasks but being fully accountable for the outcome end-to-end | Partially |

### Q11. What are your edge cases — the risks that could derail your career path?

| # | Edge Case / Risk | Mitigation Plan |
|---|-----------------|-----------------|
| 1 | Getting stuck in the same problem for too long — losing time that should go to other tasks and concepts | Set a personal time limit — if stuck for more than X time, move on and come back with fresh eyes or ask for help |
| 2 | Learning concepts but not implementing them — knowledge stays theoretical and never becomes a real skill | Practice "learning by doing" — every concept learned must have a hands-on task attached to it |
| 3 | Overthinking — spending too much time analyzing instead of acting, which delays progress and execution | Set a decision deadline — think, decide, act. Revisit and correct if wrong rather than waiting for the perfect answer |

### Q12. Coulson asked Daisy: "Would you ship a product with that test plan?" Looking at your answers above — would YOU?

```
No — not yet.

Most of my criteria are partially met, and I know why. I overthink
before acting, I learn without always implementing, and jen-pbr is
still in testing after months of building. That pattern shows up
in my career plan too.

But the plan is honest. I didn't write what I wanted to hear — I
wrote what is true. That's the starting point.

I'll ship it when Deploy and Operate are no longer blank stages
for me. Until then, this stays in staging.
```

---

## PHASE 4: THE MENTOR MAP
*From S2E4 — "You don't have to be an expert to help someone. You just have to be one step ahead."*

Viktor was scared his advice wasn't good enough. It was fumbling, confusing, imperfect — and it was exactly what Daisy needed. Because he was one step ahead.

### Q13. Who are you ONE STEP AHEAD of right now? (Name a real person or describe the type of person — a junior colleague, a new hire, someone in another team.)

```
Jagadesh, Kabilan, Pughaz, Naveen, Jerome, and Gayathri — all juniors
on the team. I am consistently one step ahead of them in production  
systems knowledge, GCP infrastructure, Jenkins pipelines, branching
strategy, debugging approaches, and how to navigate real problems in
our environment. Whenever I am around, I guide and support them without
being asked — not because it's expected, but because it's the right
thing to do. I genuinely want to share whatever knowledge I have
with them.
```

### Q14. What specific thing could you teach or share with them THIS week? Not next quarter. This week.

```
This week specifically, I shared knowledge with four people:

  Gayathri — was manually fetching GCS bucket sizes across 30-40 folders,
  which was taking too long. I shared the Jenkins job from my Bucket-size
  automation (still in progress) so she could get the results faster without
  waiting for the script to be fully complete. Immediate, practical value.

  Naveen — was releasing analyticsworkerv2 to production. I guided him
  through our branching strategy, explained what changes need to happen
  and where, and walked him through the full production release process
  step by step.

  Kabilan — was working on STG environment stabilization. I didn't do it
  for him — I pointed him to the right metrics, told him where to check
  CPU utilization, and let him do the analysis. We fixed it together.

  Jagadesh — got stuck on an image index mismatch in prod. I explained
  how the entire system works, identified the root cause, and guided him
  to the solution.

Not next quarter. This week. All four.
```

### Q15. What has STOPPED you from mentoring or sharing so far? Be honest — is it time, fear of being wrong, not feeling expert enough, or something else?

```
Honestly, nothing stops me. The examples from Q14 prove that.

  I didn't wait to be assigned a mentor role. I pinged Gayathri to check
  what she had done so far — she didn't come to me. I walked Naveen
  through production release until he understands completely. I pointed Kabilan to
  the right metrics instead of just fixing it myself. I explained the
  entire system to Jagadesh until he understood, not just until he had
  the answer.

  I don't step back when someone needs help. Not because of a process
  or expectation — just because that's how I work.

  If there is one honest gap, it's this: I share when I notice someone
  is stuck. But I don't always proactively share what I know before
  they get stuck. That's the difference between reactive mentoring and
  building knowledge in others before the problem hits.
```

### Q16. Viktor said: "What if my advice is wrong? I'm still figuring this out myself." Have you ever held back from helping someone because you didn't feel qualified? What happened?

```                                                                                                                                                                               
  I don't hold back even when I'm not fully expert in the area.                                                                                                                         
   
  Whatever I know that's relevant to the problem, I share it — without                                                                                                                  
  hesitation. I don't wait until I'm 100% sure before helping. If I'm
  mid-way through figuring it out myself, I still engage.

  And if I don't have the answer in that moment, I don't pretend or
  guess — I say "give me a minute, let me check" and come back with
  the right answer. That's not a weakness. That's honesty, and it
  builds more trust than faking confidence.

  Viktor's fear — "what if my advice is wrong?" — isn't mine. My
  approach has always been: share what I know, be honest about what
  I don't, and never leave someone stuck just because I'm not the
  expert in the room.
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
