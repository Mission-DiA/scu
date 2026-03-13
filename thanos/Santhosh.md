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

- **Name:** Santhosh Kumar
- **Current Role:** QA-Automation Analyst
- **Years in Current Role:** 6.5
- **Date Submitted:** 03/03/2026

---

## PHASE 1: THE FOUNDATION AUDIT

*From S2E1 — "That's what you finished. What did you build?"*

Coulson showed Daisy two agents. Same start date. Same effort. Different results. Agent A completed tasks. Agent B built systems, trained people, created frameworks.

### Q1. List your top 5 accomplishments from the last 6 months.


| #   | Accomplishment                                                                                                                                                                                |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Built the first version of a Playwright-based automation framework. I use it for my own regression testing now, and the QA team has started adding to the repo too.                           |
| 2   | Got our Jenkins CI pipeline working and stable — tests run on every build now without someone having to manually kick them off.                                                               |
| 3   | Made a few small QA tools (testcase management, workload tracker, automation reporting) because I was tired of doing the same manual stuff over and over. A couple of teammates use them too. |
| 4   | Did some informal L2 debugging walkthroughs with QA teammates — showed them how I approach issues, what I look at first, shared real examples from recent incidents.                          |
| 5   | Started using AI (Claude mostly) as part of how I actually work day-to-day — code reviews, trying out ideas, quick prototyping. It's not a side thing anymore, it's just how I work now.      |


### Q2. Now be honest — for each one, mark it:

- **C** = Completed (you did the work, it's done, nothing remains)
- **B** = Built (it continues to create value without you actively doing it)


| #   | C or B? | Why?                                                                                                                                                                         |
| --- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | B       | The framework is there, someone else can pick it up. The folder structure, helpers, base specs — all reusable. They don’t need me to extend it.                              |
| 2   | B       | Pipeline runs on its own. I tweak it sometimes but it doesn’t need me daily. People push code, get results, that’s it.                                                       |
| 3   | B       | Simple tools but people keep using them. They sit in the repo, anyone can run them without me being in the room.                                                             |
| 4   | C       | These were sessions, not systems. I helped people in the moment but didn’t document anything or record it. Once the call ended, the knowledge stayed with whoever was there. |
| 5   | B       | This one’s more about how I think now. I default to pairing with AI on new problems. That habit sticks with me regardless of what project I’m on.                            |


### Q3. If you disappeared tomorrow, which of those 5 things would still matter in 6 months? Why?

```
The Playwright framework and Jenkins pipeline would definitely still matter — someone can add test cases to the framework without starting over, and the pipeline just keeps running as long as the credentials don’t expire. The QA tools would still be in the repo too, maybe someone uses them, maybe not.

The L2 walkthroughs? Probably not. I didn’t write anything down or record them, so whatever I shared in those sessions is gone unless the people who attended remember it.

The AI stuff is weird to measure — it’s more that the decisions I made while working with AI (what to automate, how to structure things) are baked into the systems I left behind. But nobody would look at the code and say "oh this exists because Santhosh used AI."
```

### Q4. What is your career INTENTION right now? Not your job title. Not your task list. What are you actively, deliberately building?

```
Honestly, I want to stop being “the guy who runs tests” and become the guy who builds the systems that run the tests. That’s the shift I’m trying to make.

Right now that looks like — building out the automation framework so the team can use it without me, getting comfortable with CI/CD end to end, and making AI just a normal part of how I work (not something I experiment with on the side).

I also want to be the person people come to when they’re stuck on a hard debugging problem or need a small tool built. Not because I’m the expert on everything, but because I’ve been through enough of those situations.
```

> **Gut check:** If you struggled to answer Q4, that IS the answer.

---

## PHASE 2: THE LOOP MAP

*From S2E2 — "You're shipping. You're not looping."*

Coulson showed Daisy the D3O loop: **Design → Develop → Deploy → Operate → back to Design.** She'd been stuck in Develop → Deploy. Shipping other people's designs. Never hearing what happened after.

### Q5. Think about your last major project or initiative. Map it to the D3O loop:


| D3O Stage                                                 | What YOU Did (be specific)                                                                                                                                                                       | What SOMEONE ELSE Did                                                                                   |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------- |
| **Design** (deciding WHAT to build and WHY)               | Noticed that L2 screening was taking a lot of manual time and was inconsistent between people. I wrote down the current steps, pain points, and decided to automate the repetitive checks first. | Got early feedback from one QA teammate on which parts of L2 screening slow them down the most.         |
| **Develop** (building / executing it)                     | Built a Playwright-based prototype that can run through the basic L2 checks, used AI to help with boilerplate and code reviews, and iterated on the structure based on my own usage.             | used AI for validating the scenarios and edge cases                                                     |
| **Deploy** (shipping / releasing / presenting it)         | Created a separate branch and demoed the tool informally to a teammate. I’m now packaging it so that it can run from Jenkins and be triggered with minimal setup.                                | I will need infra/DevOps support to hook this cleanly into our existing Jenkins jobs and environments.  |
| **Operate** (monitoring, learning from results, feedback) | My plan (once it’s on Hellicarier) is to track how often the tool catches issues before manual L2, how much time it saves, and collect feedback from the QA team every 2–3 weeks.                | I expect the QA lead to help decide how this fits into our official process and which metrics we track. |


### Q6. Look at your map. Which stages are you dominant in? Which are empty?

```
Design and Develop — that’s where I’m comfortable. I can look at a messy manual process, figure out what to build, and get a working version out pretty fast especially with AI helping.

Deploy and Operate are my weak spots, and I know it. I build stuff but then it sits on my branch or my machine. I don’t properly package it so others can use it without asking me. And I almost never go back to check if the thing I built is actually helping — I just assume it is and move on to the next thing.

What I need to do (and keep not doing):
- Actually pair with someone from DevOps on a real deployment instead of figuring it out alone
- Write a “how to use this” doc even if it’s short
- Check back with the team after a few weeks to see if the tool is actually being used
```

### Q7. Coulson told Daisy: "AI can do Develop-Deploy faster than any human now." What parts of YOUR work could AI do today? What parts require your judgment, your relationships, your context?

```
AI can already do a lot of what I spend time on — writing Playwright boilerplate, generating test cases from a feature description, drafting Jenkinsfile configs, even writing documentation. If I describe the scenario clearly enough, it gets me 70-80% there.

But it can’t decide which L2 flows actually matter. That comes from me knowing which things broke last month, which customers complained, what the team can realistically handle. AI doesn’t know our system history — like when a weird error in the logs is actually expected because of how our environment is set up.

And it definitely can’t sit in a room with the dev lead and negotiate what gets automated this sprint vs next. Or tell a junior teammate “don’t trust AI on this part, it’ll hallucinate the edge cases.” That’s still me.
```

### Q8. When was the last time you shipped something that YOU designed — not something assigned to you?

```
The L2 screening automation — Jan/Feb 2026. Nobody assigned it to me. I just got frustrated watching us repeat the same manual checks every single L2 investigation, so I started building it.

I picked which parts to automate first, set up the project structure, figured out where AI could help with the code generation. Showed the early version to a teammate, got some feedback, and now I'm trying to get it stable enough to run from Jenkins.

It's not done yet. But it's the first thing in a while where I went from "this is a problem" to "I'm going to build something" without waiting for someone to tell me to.
```

---

## PHASE 3: THE SELF-TEST

*From S2E3 — "You have test plans for every feature. What's the test plan for your career?"*

Daisy had 94% automated coverage on her products and 0% on her own career. Coulson asked: "Would you ship a product with that test plan?"

### Q9. Where do you want to be in 2 years? (Be specific — title, responsibility, skill level)

```
In 2 years I want to be at a senior QA automation level — but what that actually means to me is:

I want to own the automation and quality approach for at least one product end to end. Not just “write tests” but decide what we test, how we test it, what gets automated vs monitored. The L2 framework should be something the team actually relies on daily by then, not just my side project.

I should be comfortable with CI pipelines fully — setting them up, fixing them, not needing to ask DevOps for help every time something breaks.

Basically when something new comes in, people should think “let's check with Santhosh on how to test this” instead of “let's assign Santhosh to test this.” There's a difference.
```

### Q10. Now write the acceptance criteria. How will you KNOW you're ready? Not "I feel ready" — measurable criteria.


| #   | Acceptance Criteria                                                                                                                                                                                                    | Current Status (Met / Partially / Not Met) |
| --- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| 1   | I have at least **one automation framework** (for example, L2 screening) that is used by **more than just me**, with clear documentation and at least one release note showing improvements based on team feedback.    | Partially met                              |
| 2   | I have **end‑to‑end ownership of a Jenkins (or similar) pipeline**: I can create, modify, and fix it without hand‑holding, and it has been running reliably for at least 3 months.                                     | met                                        |
| 3   | I can point to **two concrete incidents** where my tools or frameworks reduced investigation/resolution time in a measurable way (e.g., “we saved ~30 minutes per incident over a month”).                             | Not met                                    |
| 4   | I run a **regular knowledge‑sharing practice** (even if it’s once a month) where I walk teammates through debugging approaches, tools, or new automation I’ve built, and at least one person has reused what I shared. | met                                        |


### Q11. What are your edge cases — the risks that could derail your career path?


| #   | Edge Case / Risk                                                                                                                                                                       | Mitigation Plan                                                                                                                                                 |
| --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | I lean on AI heavily and sometimes I don’t fully understand what the generated code is doing. That’s fine now but it could catch up with me if I never build the deeper understanding. | I don’t have a perfect plan for this honestly. But I’m trying to manually rewrite or at least read through non-trivial AI code instead of just copy-pasting.    |
| 2   | AI tools change fast. What I’m using now might be outdated in 6 months.                                                                                                                | Try new tools on real small problems every couple of weeks, not just read about them. If it helps, use it. If not, drop it.                                     |
| 3   | I sometimes build something experimental and it quietly becomes “the way we do things” without anyone deciding that. Then it’s hard to maintain.                                       | Pilot with 1-2 people first. Keep a note on how to roll back if it doesn’t work. Don’t let experiments become permanent by accident.                            |
| 4   | I try to solve everything alone. When I’m stuck on infra or deployment stuff, I waste time instead of just asking someone who knows better.                                            | Try to do at least one pairing session a month with someone from DevOps or whoever’s strong in my weak areas. Come with specific questions, not just “help me.” |


### Q12. Coulson asked Daisy: "Would you ship a product with that test plan?" Looking at your answers above — would YOU?

```
No. Not yet.

I know the direction — own systems, not just tasks. And I’ve started. But my acceptance criteria don’t lie: I can’t point to concrete incidents where my tools actually saved time in a measurable way. And the knowledge sharing is inconsistent.

If this were a product I’d say it’s in staging. Good enough to test, not ready to ship. I need a few more months of actually following through before I’d call this production-ready.
```

---

## PHASE 4: THE MENTOR MAP

*From S2E4 — "You don't have to be an expert to help someone. You just have to be one step ahead."*

Viktor was scared his advice wasn't good enough. It was fumbling, confusing, imperfect — and it was exactly what Daisy needed. Because he was one step ahead.

### Q13. Who are you ONE STEP AHEAD of right now? (Name a real person or describe the type of person — a junior colleague, a new hire, someone in another team.)

```
QA teammate who has recently started taking L2 issues but is still not very confident with debugging logs, reading stack traces, or deciding what to try next when things & setting the automated pipelines, designing the framework even with the different language.
```

### Q14. What specific thing could you teach or share with them THIS week? Not next quarter. This week.

```
This week, I can sit with them for **For How to use the claude for desiging a tool with the best practices that I know** and:

- Walk through my actual thought process step by step.
- Share the simple checklist I follow (what I look at first, second, and third).
- Show how I use AI as a second opinion instead of a decision‑maker.
```

### Q15. What has STOPPED you from mentoring or sharing so far? Be honest — is it time, fear of being wrong, not feeling expert enough, or something else?

```
Two main things:

1. **Feeling “not expert enough”** – I often tell myself, “I’m still figuring this out, who am I to teach someone else?” especially on topics like deployment or architecture.
2. **Assuming people are busy** – I don’t want to add to their calendar, so I wait for a “perfect time” that never really comes.
3. **Not getting the outcome which I expect** - No matter how hard I try to communicate,mentor or share knowledge with the team when i don't see a slight change, I feel de-motivated as well

I don’t need to teach everything; I just need to share the part I already do slightly better or more often than they do.
```

### Q16. Viktor said: "What if my advice is wrong? I'm still figuring this out myself." Have you ever held back from helping someone because you didn't feel qualified? What happened?

```
Yes. There have been times when a teammate struggled with a Jenkins issue or a tricky test failure, and I quietly tried to solve it on my own instead of offering to pair. I told myself, “Let me first figure it out fully, then I’ll share,” but by the time I was ready, the moment had passed.

The result was:
- They didn’t see my process or learn from it.
- I carried the stress alone instead of sharing responsibility.

Looking back, even a half‑baked suggestion or a “Let’s debug this together for 30 minutes” would have been more helpful than my silence.
```

---

## PHASE 5: THE PREVENTION AUDIT

*From S2E5 — "You're not building your replacement. You're building your ladder."*

Daisy had the fastest incident response on the team. Three SEV-1s in a month, all handled under 4 minutes. Same root cause. She was winning battles in a war she never tried to end.

### Q17. What are you doing repeatedly at work that you could prevent, automate, or delegate? List 3 recurring tasks that eat your time.


| #   | Recurring Task                                                                                                       | How Often | Could Be: Prevented / Automated / Delegated?                                                                                                                                                                                                                                                                                                                                   |
| --- | -------------------------------------------------------------------------------------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1   | L2 Tickets QA debugging                                                                                              | Daily     | Automated: Because the Process is same ( Validate information -> Refere GCP logs -> Bucket the issue -> Reproduce -> Tag it to the right team) this is a repeated process for the L2 screening but issue incoming perspective is different ( if automated it'll save a hell amount of time for me and my team as well)                                                         |
| 2   | Maintaining the Existing Automation framewrok                                                                        | Daily     | I feel, we can build the automation framework but it should be maintaned regullarly considering the volume of production pushes now, the maintance is tedious where we can think of Agentic AI to run & monitor the existing framework so that the suite is always stand tall and we can make use of it and leverage it (In short building an self healing workflow)           |
| 3   | There is a no process or centralized place to make use of the automation and get the right results to the right time | Daily     | Need to carefully think and implement a startergy where triggering the pipeline is simple & getting the result should be accurate and In the code base well, instead of using the API calls to prepare the test data, As a team we have to move it to the stubbing method this will improve the running time of the automation & consumers can leverage the timing and results |


### Q18. If you automated or delegated those 3 things, what would you do with the freed time? (Not "more of the same" — what HIGHER problem would you work on?)

```
I would spend time on exploring in to the AI world which i'm currently doing as well, but if those pain points are addressed I can focus on building an meaning AI agents & other tools in the QA field which can be leveraged by the team. Also my thought process is not to force-fit the AI everywhere but carefully think the usecase and implement the AI in the right area
```

### Q19. Are you a firefighter or an architect right now? Firefighters fight the same fires forever. Architects automate the known to hunt the unknown.

```
I would say Both because, As a fire-fighter i'm also debugging the L2 tickets and as an senior in the team guiding & mentoring other on both playwright automation as well as AI & to my self started building apps using the AI to leverage it within the team, I personallly feel I have been doing both fireFighter task and Architect apps using AI and passing the knowledge to the team as well
```

### Q20. What's your biggest fear about automating or delegating your current work? Is it that you'll be replaced, or is it something else?

```
To be Honest, I don't have any fear of automating my current work, Because I feel if that can be automated I can concentrate on the other things and learn new skills (It can be professionally or personal) as well and I feel automating the current work is challenging and In the process of Automating it I feel I would learn much and I'd be gratefull.
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

Foundation: I’m moving from being “the person who tests” to the person who builds testing systems. That means frameworks (like L2 automation), CI pipelines, and small tools that other people actually use day‑to‑day. I want to be known as the guy who makes debugging and testing easier for the whole team, not just someone who closes tickets faster

D3O Loop:  Which stages do I need to own next?
I’m fairly comfortable with Design and Develop. The big gap is Deploy and Operate. I need to properly ship the L2 framework into Jenkins, write a simple “how to use this” guide, add basic metrics (like how often it catches issues or saves time), and then review that data with my lead instead of just assuming it’s helping.

Test Plan – What are my acceptance criteria?
I’ll call it a pass when
At least one automation framework I built (L2 or similar) is used by more than just me, with clear docs and at least one improvement release based on team feedback.
I can set up and maintain a Jenkins pipeline end‑to‑end for our QA needs, and it runs reliably for a few months.
I can point to at least two real incidents where my tools clearly reduced investigation or fix time.
I’m running regular knowledge‑sharing, and I can see at least one teammate using something I taught.

Mentoring: Who am I one step ahead of, and how?
I’m one step ahead of the newer QA folks who are just starting with L2 issues, reading logs, and setting up automation. My job is to sit with them more often, walk through how I think about a problem, show how I use AI without blindly trusting it, and slowly hand over pieces of the L2/automation work so they can own parts of it.

Prevention: What fires am I still fighting repeatedly?
I still repeat a lot of the same things: re‑doing similar L2 checks by hand, explaining the same debugging steps again and again, and dealing with flaky tests. The plan is to turn these into checklists, small tools, or automation (for common L2 flows), so people don’t have to ping me every time. That’s how I stop being just the firefighter and start acting more like the architect
```

### Q22. What is the ONE THING you will do differently starting this week — not this quarter, not "eventually" — THIS WEEK?

```
I would start from planning each day, Becasue that gives the clarity what i'm going to work on and what i'll. not be taking on my plate on that particular day
```

### Q23. Complete this sentence:

> "I've been *a good team player and a mentor*________**. Now I'm going to *become a best lead and a better team player & men***."

---

## FINAL REFLECTION

### Q24. Which episode hit you the hardest? Why?

```
Episode 3 – Testing Your Career Like a System & Episode 6 – Long-Term Thinking and Reflection Becasue I felt these episodes are co-related to each other because, whenever we take up a task/doing a POC we should always challenge our skill set and move up the ladder, & while solving that task solution should always be the longterm running instead of building a system and its fails on few months, Foundation should be stronger
```

### Q25. Was there a specific scene or dialogue that made you stop and think about your own work life? Describe the moment and what it triggered in you.

```
To be Honest, None I can understand the context of the episode and intention to relate it to our self, but unfortunaltely there is no specific dailoge/scene that triggered me
```

### Q26. If you had to explain Season 2 to a colleague who hasn't read it — not the plot, but why it matters — what would you tell them?

```
Don’t just show up and do tasks; know how today’s work connects to where you want your career to go.
Being constantly busy doesn’t mean you’re growing – what matters is new skills, impact, and better opportunities.
Treat your career like a system you’d build at work: have a plan, get feedback, and keep improving it.
Don’t wait for your manager to “grow” you; take ownership, look for chances to learn, and create your own path.
Be clear about where you want to be in a few years, and check in regularly to see if your daily work is really taking you there.
```

### Q27. What did Season 2 make you feel or realize that Season 1 didn't? What changed between reading the first season and finishing this one?

```
Season 1 was a wake-up call: it made me see that my career is my responsibility. No one else is going to drive it for me.Season 2 went a level deeper. It made me realize that just “taking responsibility” isn’t enough. I can’t just say, “Yeah, I’ll own it” and then wing it. I need a system: a plan, clear acceptance criteria, and a way to regularly check if I’m actually moving forward.If Season 1 was about deciding to sit in the driver’s seat, Season 2 was about realizing I also need a map, a route, and a way to know whether I’m even heading in the right direction.
```

### Q28. If you were creating Season 3, what would you keep exactly as is — and what would you do differently?

**Keep as is:**

```
Honeslty I don't want to impose my thoughts to the creator, I'd rather be an audiance who enjoy's and reflect the season 3
```

**Do differently:**

```
Honeslty I don't want to impose my thoughts to the creator, I'd rather be an audiance who enjoy's and reflect the season 3
```

### Q29. Which question in this blueprint was the hardest to answer? What does that tell you?

```
Q1. List your top 5 accomplishments from the last 6 months.   Beacase, i did lot of things in the last 6 months & because of not documented it properly I was not able to recollect the tasks, & evaluate it based on the priority and how it helped me and the QA team as well.
```



---

> **Remember:** You will present Phase 6 (Your Architecture) to the team. They will ask questions. The goal isn't to have perfect answers — it's to have honest ones.
>
> *"Same bricks. Same effort. Different result."* — Coulson, S2E1

---

**Submit to:** Director Coulson
**Deadline:** [DATE]