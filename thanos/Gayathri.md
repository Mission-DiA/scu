## YOUR DETAILS

- **Name:** Gayathri Vandana M
- **Current Role:** DevOps Engineer
- **Years in Current Role:** 3 years above
- **Date Submitted:** March 3, 2026

## PHASE 1: THE FOUNDATION AUDIT
*From S2E1 — "That's what you finished. What did you build?"*

Coulson showed Daisy two agents. Same start date. Same effort. Different results. Agent A completed tasks. Agent B built systems, trained people, created frameworks.

### Q1. List your top 5 accomplishments from the last 6 months.

| # | Accomplishment |
|---|---------------|
| 1 | Created Lambda deployment pipelines at past company — enabled application-level deployments that didn't exist before |
| 2 | Led AWS EKS POC (70% complete) at past company — covered cluster setup, ArgoCD, and deployments to evaluate migration from ECS |
| 3 | Built Azure AD + AWS Cognito SSO integration POC at past company — fulfilled a critical client requirement on short notice |
| 4 | Migrated 3 major production environments (US, Europe, Asia) from zonal to regional GKE clusters at current company — zero downtime, completed in 3 months |
| 5 | Conducted and submitted post-migration cost analysis at current company — documented savings and outcomes for the team |

---

### Q2. Now be honest — for each one, mark it:

- **C** = Completed (you did the work, it's done, nothing remains)
- **B** = Built (it continues to create value without you actively doing it)

| # | C or B? | Why? |
|---|---------|------|
| 1 | B | Developers at the past company still use the Lambda pipelines daily — reduces manual effort without any involvement from me |
| 2 | B | The POC educated the team on EKS advantages they didn't know before — they can now implement it independently |
| 3 | B | The POC is replicable — the client and team can integrate SSO without my presence |
| 4 | C + B | The migration work is done, but the infrastructure continues to deliver value through cost savings and stability |
| 5 | C + B | The analysis is submitted and complete, but it continues to serve as a reference for the team's post-migration decisions |

---

### Q3. If you disappeared tomorrow, which of those 5 things would still matter in 6 months? Why?

```
All 5 would still matter.

I already "disappeared" from my past company — and all 3 accomplishments there are
still alive:
- Developers still rely on the Lambda pipelines for daily deployments
- The EKS POC gives the team a clear path to migrate without starting from scratch
- The SSO POC is documented and replicable for the client's integration

At my current company, the regional migration's biggest impact is cost reduction —
that saving continues automatically. The cost analysis I submitted gives the team
visibility into post-migration results, which they'll reference for future decisions.

None of these required me to stay for them to keep creating value.
```

---

### Q4. What is your career INTENTION right now? Not your job title. Not your task list. What are you actively, deliberately building?

```
My intention is to build toward being a Cloud Infrastructure
Architect — someone who doesn't just execute migrations and
pipelines, but designs systems that teams rely on long after
I've moved on.

Every major thing I've done — Lambda pipelines, EKS POC,
SSO integration, GKE regional migration — I drove end to end.
That's not execution. That's architecture ownership.

I don't learn in courses. I learn by doing — by taking a
problem no one has solved yet, building the solution myself,
and leaving something that runs without me. That's already
my pattern. Now I'm doing it deliberately.

I'm building toward owning infrastructure decisions at a
design level — multi-cloud, zero-downtime, cost-aware.
The title and recognition will follow. The work already proves
the direction.
```

---

## PHASE 2: THE LOOP MAP
*From S2E2 — "You're shipping. You're not looping."*

Coulson showed Daisy the D3O loop: **Design → Develop → Deploy → Operate → back to Design.** She'd been stuck in Develop → Deploy. Shipping other people's designs. Never hearing what happened after.

### Q5. Think about your last major project or initiative. Map it to the D3O loop:

**Project: Regional GKE Cluster Migration (Current Company)**

| D3O Stage | What YOU Did (be specific) | What SOMEONE ELSE Did |
|-----------|---------------------------|----------------------|
| **Design** (deciding WHAT to build and WHY) | Was assigned the task by manager and senior. They asked me to do the analysis on WHY we needed to migrate from zonal to regional. I researched and documented the reasons (reliability, disaster recovery, cost optimization). However, my senior and manager already knew the answer — they were having me understand the "why" so I could execute better. | Senior mentor and manager had already decided the migration was necessary. They knew the business reasons and set the scope (3 regions: US, Europe, Asia) and timeline (3 months). My analysis was for learning, not decision-making. |
| **Develop** (building / executing it) | Completed all prerequisite steps. Designed the regional cluster architecture. Planned and executed the migration strategy for all 3 regions. Configured infrastructure and prepared deployment approaches. | Senior mentor reviewed my PRs, corrected me in areas where I missed things, and validated that all steps were executed properly. Guided me when I went off track. |
| **Deploy** (shipping / releasing / presenting it) | Deployed everything in the production clusters for all 3 environments (US, Europe, Asia) with zero downtime. Executed the actual cutover process and coordinated the migration. | Senior mentor added the ingress IP in Cloudflare (I didn't have access to Cloudflare). Senior mentor reviewed my PRs throughout the process and corrected me in areas where I missed things during development. |
| **Operate** (monitoring, learning from results, feedback) | Checked monitoring after migration to ensure cluster health and stability. Conducted post-migration cost analysis, reviewed the findings, and submitted the report to the team. | Senior mentor helped validate that everything was working fine post-migration. Management reviewed the cost analysis report and made decisions about future migrations based on the findings. |

---

### Q6. Look at your map. Which stages are you dominant in? Which are empty?

```
Dominant: Develop (70-75% ownership) and Deploy (70% ownership)

I spent most of my energy and ownership in the execution stages. I did the
technical work — architecting the regional clusters, configuring infrastructure,
executing the migration. I deployed everything in production across 3 regions
with zero downtime. This is where I'm strongest and most comfortable.

Moderate: Operate (50-60% ownership)

I checked monitoring and did the cost analysis, which is good. But I didn't
participate as much in the "what do we learn from this?" or "what should we do
differently next time?" discussions. I submitted the analysis, and management
made decisions based on it. I was present in this stage, but not driving it.

Growing: Design (30-40% ownership)

I was asked to analyze WHY we needed to migrate, and I did it. However, the
decision was already made. My analysis was for me to understand the context so
I could execute better — not to influence whether we should migrate or what
success criteria should be. I'm working on this stage too, but not at full
capacity yet.

The loop is incomplete:

I don't loop back from Operate to Design as much as I should. I finished the
migration, did the analysis, submitted it, and moved on to the next assigned
task. I didn't use what I learned to propose "based on this migration, here's
what we should design next."

I'm shipping, but I'm not looping fully yet.
```

---

### Q7. Coulson told Daisy: "AI can do Develop-Deploy faster than any human now." What parts of YOUR work could AI do today? What parts require your judgment, your relationships, your context?

```
What AI COULD do today (or will do very soon):

- Generate Terraform/infrastructure code for regional GKE cluster setup
- Write migration scripts and automation for moving workloads
- Create ArgoCD configurations and deployment pipelines
- Generate documentation for the migration process
- Analyze cloud billing data and produce cost analysis reports
- Parse logs and metrics to identify issues during migration
- Suggest optimization strategies based on best practices
- Even debug common infrastructure problems faster than I can

Most of my current work in Develop and Deploy is in this category. AI can
write infrastructure code, execute migrations, and analyze results. It's
getting faster and better at this every month.

---

What REQUIRES me (human judgment, relationships, context):

- Understanding WHY my manager and senior mentor decided this migration was
  important (business priorities, team goals, organizational strategy)
  — I'm working on this by doing the analysis they ask for
- Knowing which production environments are most critical and which can
  tolerate more risk during cutover
- Making real-time decisions during migration when unexpected issues happen
  (Do I roll back? Do I push forward? Who do I call?)
- Building trust with my senior mentor so they're comfortable giving me
  more ownership — this is happening through PR reviews and corrections
- Learning from my senior mentor's PR reviews — not just what to fix, but
  WHY they think that way
- Recognizing when I don't have access (like Cloudflare) and asking for help
  instead of being blocked
- Understanding team dynamics and organizational constraints that affect what's
  actually possible vs. technically correct
- Using the cost analysis results to say "here's what we should do next"
  instead of just submitting a report — I need to work on this more

---

The reality:

I'm strongest in Develop-Deploy (execution), which AI is getting better at.
I'm working on Design and Operate (context, influence), but not at full
capacity yet. I need to shift more energy toward owning those stages where
humans are irreplaceable.
```

---

### Q8. When was the last time you shipped something that YOU designed — not something assigned to you?

```
The Lambda deployment pipelines at my past company.

That's the last time I truly owned the full loop — Design through Operate.

Nobody assigned it to me. I saw developers struggling with manual deployments
and application-level deployments that didn't exist. I recognized the problem,
decided it was worth solving, designed the pipeline solution, built it,
deployed it, and it's still being used today.

That was probably 6-12 months ago (before I left my past company).

Everything since then has been assigned:
- EKS POC → assigned by management to evaluate migration from ECS
- Azure AD + Cognito integration → assigned due to client requirement
- Regional GKE migration → assigned by manager and senior mentor
- Cost analysis → assigned as part of the migration deliverable

I executed all of these well. But I didn't design them. Someone else decided
"we need this" and I figured out "how to do it."

At my current company, I haven't yet shipped something I designed from
scratch based on a problem I identified.

```
---

## PHASE 3: THE SELF-TEST
*From S2E3 — "You have test plans for every feature. What's the test plan for your career?"*

### Q9. Where do you want to be in 2 years? (Be specific — title, responsibility, skill level)

```
In 2 years, I want to be a Senior DevOps Engineer who thinks like a DevOps
Architect:

Title/Role:
- Senior DevOps Engineer (with architectural mindset)
- Recognized as a technical decision-maker, not just an executor
- The person who thinks architecturally about DevOps solutions — not just
  implementing tools, but designing how systems should work together

Responsibilities:
- OWNS the Design stage — I identify infrastructure problems before I'm assigned
  them, and I propose solutions with clear "why" reasoning
- DRIVES architectural decisions for DevOps infrastructure and processes
- THINKS like an architect — considering scalability, maintainability, cost,
  and long-term implications, not just "make it work"
- LEADS projects from Design → Operate → back to Design (full loop ownership)
- MENTORS 2-3 junior engineers in infrastructure and DevOps practices
- INFLUENCES team direction by using Operate insights to propose what we should
  Design next

Skill Level:
- Can design DevOps architecture independently (not just implement it)
- Can evaluate trade-offs between approaches and defend my decisions with
  architectural reasoning
- Can translate business requirements into technical solutions
- Can lead technical discussions and explain complex concepts to non-technical
  stakeholders
- Have deep expertise in at least one domain (Kubernetes, CI/CD, or cloud
  infrastructure) that makes me the go-to person

The key shift: From "excellent executor of assigned work" to "DevOps architect
who identifies problems, designs scalable solutions, and drives them through
the full loop."
```

---

### Q10. Now write the acceptance criteria. How will you KNOW you're ready? Not "I feel ready" — measurable criteria.

| # | Acceptance Criteria | Current Status (Met / Partially / Not Met) |
|---|--------------------|--------------------------------------------|
| 1 | **Shipped 3+ projects that I designed from scratch** — not assigned, not asked to do, but problems I identified and proposed solutions for. Evidence: project proposals, design docs, PRs with context. | **Partially Met** — Currently working on Jenkins to Cloud Build migration where I'm designing the solution from scratch (in progress). At current company: 0 completed self-designed projects yet, but I've started doing design-led work. |
| 2 | **Led at least 2 full D3O loops** — from identifying the problem (Design) through implementation (Develop-Deploy) to monitoring results (Operate) and proposing the next iteration based on learnings. Evidence: documented loop with clear "what we learned → what we're doing next" connections. | **Partially Met** — I joined the company a few months back. I have driven the full loop execution on assigned work (GKE migration from Design through Operate), but I haven't contributed the idea or identified the problem myself — it was assigned to me. I can execute the full loop, but I haven't yet initiated one from problem identification. |
| 3 | **Mentored 2-3 junior engineers with measurable impact** — they can now do things independently that they couldn't do before because of my guidance. Evidence: their shipped work, their feedback, their reduced dependency on seniors. | **Not Met** — I haven't actively mentored anyone yet. I've helped colleagues when asked, but no structured mentorship. |
| 4 | **Influenced 2+ major architectural decisions** — my analysis, proposal, or recommendation changed the team's direction. Evidence: design docs I authored that were approved and implemented, architecture decisions recorded in team docs that cite my input. | **Partially Met** — During the GKE migration, I conducted cost analysis and provided insights the team didn't know previously (GKE Enterprise vs Standard cost differences, automatic conversion from Enterprise to Standard). I informed the team of findings that influenced their understanding. However, I haven't yet driven architectural decisions from initial proposal to implementation. I'm contributing valuable analysis, but not yet leading the decision-making process. |
| 5 | **Built or automated 2+ recurring problems** — turned firefighting into prevention. Evidence: monitoring dashboards, automation scripts, runbooks, or infrastructure that prevents issues instead of just fixing them. | **Partially Met** — Lambda pipelines at past company (B). Haven't built prevention systems at current company yet. |

---

### Q11. What are your edge cases — the risks that could derail your career path?

| # | Edge Case / Risk | Mitigation Plan |
|---|-----------------|-----------------|
| 1 | **Comfort zone trap:** I stay in Develop-Deploy because I'm good at it and it feels safe. I keep accepting assigned tasks instead of identifying problems myself. | **Mitigation:** I've already started doing this — I share ideas with my senior mentors and I'm growing on it. I review recent projects and propose improvements based on what I learned. I'm building the habit of asking "what problem can I solve that nobody assigned me?" and tracking my self-initiated vs assigned work. |
| 2 | **AI displacement:** AI gets better at Develop-Deploy (where I'm strongest) faster than I move upstream to Design-Operate. My execution skills become commoditized. | **Mitigation:** I've already started working on Design-Operate with small ideas. For example, when AWS zones were recently attacked in ME-CENTRAL1 region, I proactively told my senior we should think about similar risks in GCP. I discussed the related data with my senior, and now I've been assigned a task related to this. I'm deliberately shifting time from pure execution to design thinking and proposing solutions. |
| 3 | **Waiting for permission:** I wait for my manager or senior to give me more Design ownership instead of taking it. I assume I need a title change before I can act differently. | **Mitigation:** Start proposing small improvements NOW without waiting for permission. Bring 1 problem + proposed solution to my 1:1 meetings every 2 weeks. Don't wait for "Senior" title to act like a senior — demonstrate the behavior first, then the title follows. |
| 4 | **Analysis paralysis:** I spend too long learning/researching and not enough shipping. I use "I'm not ready yet" as an excuse to avoid Design ownership. | **Mitigation:** I accept this is a real issue for me. I keep doing deep analysis so I can prove I'm perfectly right, but I should change that. Instead of deep analysis until perfection, I should start sharing ideas earlier — even if imperfect. Set a rule: If I've spent 2 weeks researching something, I MUST propose a solution. Use Viktor's lesson: "You don't have to be an expert to help someone. You just have to be one step ahead." |

---

### Q12. Coulson asked Daisy: "Would you ship a product with that test plan?" Looking at your answers above — would YOU?

```
Honestly? No. I wouldn't ship this test plan as-is.

Here's why:

1. **High-risk dependencies:** 4 out of 5 acceptance criteria are "Partially Met."
   If this were a product, I'd flag this as "in progress but not ready for
   production." The foundation is being built, but it's not solid yet.

2. **Unclear timeline:** I said "2 years" but I didn't break down when each
   acceptance criterion needs to be met. No milestones. No checkpoints. In a
   product test plan, I'd have quarterly targets.

3. **Missing feedback loops:** My mitigation plans are one-way actions. There's
   no "check after 3 months and adjust" mechanism. No way to know if the
   mitigations are working.

4. **Incomplete edge case coverage:** I listed 4 risks, but there are probably
   more I'm not seeing (organizational changes, team restructuring, tech stack
   shifts, burnout, etc.).

What would make this shippable:

- Add quarterly milestones for each acceptance criterion
- Define "what good looks like" at 6 months, 12 months, 18 months
- Build in feedback checkpoints: "If X isn't true by Month 6, I need to
  adjust Y"
- Add monitoring: How will I measure progress monthly? What metrics will tell
  me I'm on track vs off track?

The brutal truth: I've been treating my career like a product I'd never ship.
I need to apply the same rigor to this test plan that I'd apply to production
infrastructure.
```