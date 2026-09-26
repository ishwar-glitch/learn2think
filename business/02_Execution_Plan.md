# Learn2Think — Execution Plan (v1, 26 Sep 2026)

**Goal:** a full platform for BA, DA, PM and PD, with the career layer and payments, live by **25 Jan 2027**. Claude builds everything; you direct, review and run the business.
**Constraints:** Claude Pro plan only · run cost < ₹5,000/month · founder 10–20 h/week · no pilot gate.
**Operational queue:** `../BUILD_PLAN.md`. Session rules: `../CLAUDE.md`.

---

## 1. Timeline at a glance

| Phase | Weeks | Dates | Outcome |
|---|---|---|---|
| 0 Foundations | W1 | 28 Sep–4 Oct | Kit updated for launch scope; app skeleton deployed; waitlist live; Company Universe written |
| 1 Engine + Stage 1–2 | W2–W5 | 5 Oct–1 Nov | Sign-up, Day-1 case, concept player, quizzes, case player, tree builder; M1–M7 and IC1 content |
| 2 Decide/Deliver + BA | W6–W9 | 2–29 Nov | Scripted Opponent, decision sim, reps, placement, SQL sandbox; M8–M10, IC2, IC3, S1–S5, BA track |
| 3 Tracks + career + payments | W10–W13 | 30 Nov–27 Dec | DA, PM and PD tracks; Interview Lab, Story Bank, Translator, JD Decoder, public portfolio; Razorpay |
| 4 Launch readiness | W14–W16 | 28 Dec–17 Jan | Legal, security, tests, performance, friendly-tester week, fixes |
| Launch | W17–W18 | 18–31 Jan | Soft launch (18 Jan) → public launch (25 Jan); W19 is buffer |

**Claude work:** 71 planned sessions plus 9 buffer slots, at 5 slots a week. See `BUILD_PLAN.md` for each one.

## 2. Working within Claude Pro limits

Pro usage resets on a rolling 5-hour window and also has a weekly cap. **Claude.ai chat and Claude Code share the same limits.**

| Rule | Why |
|---|---|
| **1 batch = 1 session, sized for one usage window.** Start a new session for each batch. | Every turn re-reads the whole thread, so long threads burn quota. |
| **Default model: Sonnet 5.** Haiku 4.5 for mechanical work (renames, reformatting, marketing copy, re-running validator fixes). Opus for **one** pre-launch audit only (W16). | Opus uses quota several times faster. |
| **Short CLAUDE.md, targeted reads.** Claude reads only the files a batch needs. | Context is the main cost driver. |
| **Scripts do the checking.** Validators and tests run as commands, and Claude reads only the failures. | Avoids pasting large outputs. |
| **One consolidated feedback message per review.** Don't send one-line follow-ups. | Fewer turns. |
| **Screenshots only when needed.** Describe bugs as steps → expected → actual. | Images are token-heavy. |
| **Resume notes.** At each checkpoint Claude appends a line to the `BUILD_PLAN.md` log; if a limit hits mid-batch, the next session continues from it. | No lost work and no re-explaining. |
| **Hit the weekly cap?** Spend the remaining days on non-Claude tasks (§7). Apply the cut list (§9) if you're more than one week behind. | Protects the launch date. |
| **Auto-compaction warning?** End the session and start fresh from the resume note. | A compacted session has lost detail. |

**Claude tools and when to use them**

| Tool | Used for | Model |
|---|---|---|
| Claude Code (desktop app, Code tab), opened in the `Learn2Think/` folder | All K/P/C batches; you say "Continue the Learn2Think build plan." | Sonnet 5 |
| Built-in browser pane in Claude Code | Claude checks every UI batch at phone width (375px) and desktop | — |
| `/code-review` and `/simplify` | Midpoint (P16) and pre-launch (P31) | Sonnet 5 |
| `/security-review` | P26 (W14) | Sonnet 5 |
| Claude.ai Project "L2T Growth" (upload `01_Business_Plan.md` once) | LinkedIn posts, outreach messages, workshop scripts, waitlist replies | Haiku 4.5 |
| Opus session | Pre-launch audit (W16): architecture, scoring logic, launch checklist | Opus |

## 3. Tech stack (free tiers; verify current limits at setup)

| Need | Choice | Cost | Why |
|---|---|---|---|
| Web app | **Astro + React islands + TypeScript + Tailwind** | ₹0 | Content-first; markdown content collections with schema validation; static pages load fast on low-end phones |
| Hosting | **Cloudflare Pages** | ₹0 (commercial use allowed) | Free tier with a generous request limit |
| Auth, database, server functions | **Firebase** (Auth: Google + email link; Firestore with Security Rules; Cloud Functions) | ₹0 within free quotas; Blaze plan (card on file) required for Functions; budget alert at ₹500 | Founder already knows the Firebase console; no server to maintain |
| Payments | **Razorpay** Subscriptions | ~2% per transaction, no monthly fee | Indian cards, UPI and wallets |
| SQL sandbox (DA) | **sql.js** (SQLite in the browser) | ₹0 | Runs on the learner's device; the V1 validator already checks SQL answers |
| Email | **Resend** free tier | ₹0 | Magic links, welcome email, weekly recap |
| Analytics | **PostHog** free tier | ₹0 | Funnel, retention and cohort metrics |
| Errors | **Sentry** free tier | ₹0 | Catches production bugs a non-coder can't see |
| Code backup and CI | **GitHub** private repo + Actions | ₹0 | Backup; runs validators and tests on each push; Cloudflare deploys from it |

Brand: reuse `L2T_V1.0/brand/` and `app/assets/` icons, and the V1 drill UI ideas and `validate.py` SQL checks.

## 4. Architecture

```
Learn2Think/
├─ CLAUDE.md, BUILD_PLAN.md
├─ kit/             rules, templates, rubric, platform features
├─ business/        this plan + business plan
├─ content/         markdown/JSON: universe, core, specialist, cases, career
├─ tools/           validators (content)
└─ app/             Astro project; reads ../content via content collections (zod schemas = content QA)
   ├─ src/islands/  interactive formats (quiz, tree, stakeholder chat, data room, opponent, SQL, interview)
   └─ firebase/     firestore.rules, indexes, Cloud Functions (razorpay-webhook, scheduled backup, later ai-proxy)
```

**Firestore collections** (every collection locked down by Security Rules; users only read and write their own documents):
- `profiles`, `plans` (onboarding goals)
- `attempts` (item, answer, correct, confidence, error tags)
- `case_sessions` (questions asked, exhibits requested, hints used)
- `submissions` (text, self-review, revision number)
- `thinking_records`, `portfolio_items` (with a public flag)
- `stories`, `interview_attempts`
- `subscriptions`, `expert_reviews`, `rep_queue`

## 5. "AI" at launch without AI running costs

Claude writes all of the following **at build time**, so the product costs nothing to run. The case template (T4) gains new fields in batch K1.

| Feature | Launch version (scripted, ₹0) | Live upgrade (paid users, after MRR ≥ ₹50k) |
|---|---|---|
| Stakeholder chat | Menu of 10–15 questions per stakeholder (useful, irrelevant, leading); limited number of asks; answers drawn from canon facts; the questions chosen feed the Questioning score | Free-text questions answered by the LLM, restricted to case facts |
| AI Opponent (F1) | 2–4 persona challenges per case, each with a strong-answer checklist, one escalation and a concession. The learner self-checks, then must revise and say "what changed". | The LLM persona reads the submission and escalates adaptively |
| Feedback on written answers | Rubric self-review checklist, then the model answer with accepted alternatives, then the common mistakes | LLM structure check suggests a rubric level with reasons (F7 step 1) |
| Earned assistance | Hint ladder, levels 0–5, per case (V3 AI spec) | Adaptive Socratic hints |
| Red-team the AI (`AUDIT`) | Pre-written "AI analyses" with planted flaws | Same; stays scripted |
| Personal Problem mode | Guided Thinking Loop worksheet that produces a Thinking Record | Socratic coach |
| Story Bank, Translator, JD Decoder | Templates, a static skills taxonomy and keyword matching, using only learner-confirmed facts | The LLM rephrases learner-confirmed facts |
| Interview Lab | Timed question banks; audio recorded **on the device** (never uploaded); self-rating against model answers; Mock Loop | LLM interviewer with follow-up questions |
| Capstone review | Founder review (paid add-on, 5 a week) | LLM pre-review to speed up the founder's review |

**Live AI implementation (after the trigger, one batch):**
- A Cloud Function `ai-proxy` keeps the API key server-side.
- Uses Claude Haiku 4.5 ($1 input / $5 output per million tokens).
- Per-user daily caps, paid users only.
- Estimated cost is about ₹3.4 per 6-turn persona session and under ₹1 per evaluation.

## 6. Week-by-week plan

**K** = kit or rules batch · **P** = platform code · **C** = content.

| Week | Claude batches (≈ 1 session each) | Your non-Claude tasks | Exit check |
|---|---|---|---|
| **W1** 28 Sep | K1 kit update · **D1 clickable wireframes** · P1 scaffold + deploy · P2 waitlist page + analytics · C0 Company Universe | Decide name; CA call (entity); bank account; domain; open GitHub, Firebase (upgrade to Blaze + ₹500 budget alert), Cloudflare, PostHog, Resend and Sentry accounts; **apply for Razorpay**; IP India trademark search; 15-minute competitor price check; first LinkedIn post | Waitlist URL live; wireframes reviewed |
| **W2** 5 Oct | D2 wireframe fixes + screen map · P3 content pipeline · P4 concept player + quiz engine 1 · P5 quiz engine 2 + Mastery Check · C1 M1 + CASE-M1 · C2 M2 + CASE-M2 | Review C1/C2 as the expert; 2 LinkedIn posts | M1 playable |
| **W3** 12 Oct | P6 case player 1 (inbox, variants, stakeholder chat, data room) · P7 case player 2 (submit, hints, self-review, Thinking Record, portfolio) · **template check** · K2 template fixes · C3 M3 + CASE-M3 | **Template check:** you and 3–5 trusted people click through M1–M2 end to end for 2 days; send one consolidated feedback message | M1–M2 complete end to end |
| **W4** 19 Oct | P8 tree builder · C4 M4 · C5 M5 · C6 M6 (each with its case) · P9 estimation duel + calibration | List 20 campus clubs; start outreach | M1–M6 playable |
| **W5** 26 Oct | C7 IC1 + Day-1 micro-case · P10 onboarding, Day-1 flow, dashboard · P11 skill map + error profile · C8 M7 + CASE-M7 · buffer | Run the first campus workshop (IC1) | **Phase 1 done:** a new user can sign up and complete Day 1 through IC1 |
| **W6** 2 Nov | P12 scripted Opponent · C9 M8 + CASE-M8 · C10 IC2 · P13 decision sim + audit format · buffer | Review IC1 fully | Opponent works on CASE-M7 |
| **W7** 9 Nov | C11 M9 · C12 M10 (with cases) · C13 IC3 · P14 Daily Reps + weekly recap · P15 diagnostic placement | 2 workshops | Core M1–M10 + IC1–IC3 complete |
| **W8** 16 Nov | C14 S1 · C15 S2 · C16 S3 + CASE-BA-1 · C17 S4 + CASE-BA-2 · P16 midpoint `/code-review` + fixes | **Confirm reviewers** for any role outside your expertise | Midpoint review clean |
| **W9** 23 Nov | C18 CASE-BA-3, 4 · C19 CAP-BA · C20 S5 + CASE-DA-1 · P17 SQL sandbox · buffer | Review CAP-BA fully | **Phase 2 done:** BA track complete |
| **W10** 30 Nov | C21 S6 + CASE-DA-2 · C22 CASE-DA-3, 4 · C23 CAP-DA · C24 S7 + CASE-PM-1 · P18 Razorpay subscriptions + paywall | Razorpay test keys in place | Test payment works |
| **W11** 7 Dec | C25 S8 + CASE-PM-2 · C26 CASE-PM-3, 4 · C27 CAP-PM · C28 S11 + CASE-PD-1 · P19 Story Bank + Translator | Review CAP-DA and CAP-PM | DA and PM complete |
| **W12** 14 Dec | C29 S12 + CASE-PD-2 · C30 CASE-PD-3, 4 · C31 CAP-PD · P20 Interview Lab + evidence checklist · P21 JD Decoder | Privacy policy and terms review | PD complete |
| **W13** 21 Dec | C32 interview banks · C33 Tool Labs + taxonomies · P22 public portfolio + expert-review queue + PD uploads · P23 lifecycle emails · buffer (holiday week) | Pick 10–20 friendly testers from the waitlist | **Phase 3 done:** feature-complete |
| **W14** 28 Dec | P24 landing, pricing and SEO pages · P25 legal, privacy, DPDP consent, data export/delete, 18+ gate · C34 final content QA · P26 `/security-review` + Security Rules audit · buffer | Lawyer or CA glance at terms (optional) | Security review clean |
| **W15** 4 Jan | **Friendly-tester week** (not a gate) · P27 Playwright smoke tests + accessibility · P28–P29 fixes from testers | Switch Razorpay to **live** keys; collect tester feedback in one list | No P0 bugs open |
| **W16** 11 Jan | P30 performance (low-end Android, slow 3G) + mobile pass + analytics check · P31 final `/code-review` + fixes · **Opus pre-launch audit** | Prepare launch posts and emails (Haiku) | Launch checklist (§8) green |
| **W17** 18 Jan | Buffer and fixes | **Soft launch** to waitlist with founding price | 150 paid |
| **W18** 25 Jan | Buffer and fixes | **Public launch** | 2,000 signups in month 1 |

## 7. Your weekly rhythm (~12–16 h)

| When | What | Hours |
|---|---|---|
| Mon–Fri | Start one Claude session a day; answer its plan question; test the result for about 15 minutes | 5–7 |
| 2 review blocks (for example Tue and Thu evenings) | Read the batch summaries' "Needs human review" lists; spot-check one module and one case as the expert (read capstones in full); send one consolidated feedback message | 3–4 |
| Weekend | Business setup tasks; 2 LinkedIn posts; waitlist replies; workshop prep | 3–5 |

## 8. Quality gates and launch checklist

**Every content batch:**
- `tools/validate_quiz.py` passes.
- The kit's Self-Review Checklist is done.
- There's a batch summary with a "Needs human review" list.
- You spot-check it.

**Every code batch:**
- Type check, build and tests pass.
- Claude verifies the page in the browser pane at 375px and at desktop width.
- Changes are committed.

**Launch checklist (W16):**
- [ ] All 4 tracks playable end to end, free and paid paths
- [ ] Razorpay live: subscribe, renew, cancel, refund, webhook retries
- [ ] Firestore Security Rules tested (emulator tests): one user can't read another's data; public portfolio shows only opted-in items
- [ ] Privacy policy, terms, refund policy, grievance contact, 18+ gate, data export and delete
- [ ] No outcome or placement claims anywhere in the copy
- [ ] Sentry and PostHog receiving events; daily Firestore backups running
- [ ] Loads in under 3 seconds on a mid-range Android over 4G; usable at 375px
- [ ] Runbook in CLAUDE.md: how to deploy, roll back, refund, answer a data-deletion request

## 9. Cut list (apply in this order if more than 5 slots behind)

1. JD Decoder → first update after launch
2. Decision sim → IC2 uses static rounds
3. Interview Lab audio → text answers only
4. Share-card images → plain share links
5. Professional variants of track cases → Student variants only at launch
6. PD track → launch with BA, DA and PM; PD follows 4 weeks later

## 10. After launch (W19–W26)

- **W19–W20:** fixes only. Watch activation and the D7 dashboard daily.
- **Day 60:** apply the decision rules in Business Plan §8.
- **At MRR ≥ ₹50k:** live-AI batch (`ai-proxy`, Haiku 4.5, caps).
- **Monthly:** one Live Case (1 content session); quarterly job-posting refresh for the interview banks.
- **Month 6+:** college licence pitch; plan the SC and SD tracks.
