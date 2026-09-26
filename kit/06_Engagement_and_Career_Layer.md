# Learn2Think — Engagement & Career-Evidence Layer (v4.2: launch scope moved into the kit)

Adds stickiness, interactivity and a credible path to jobs **without adding units** and **without breaking earlier decisions**. Features are built once on the platform and driven by tags in existing content, per the lean rules in `01_Curriculum_v4.md`.

## 0. Constraints inherited from earlier work (this layer must obey them)

Sources: Business Pack v3 GTM spec, Business Pack v4 PRD, Curriculum v2, and the V1 prototype.

| Earlier decision | Where | How this layer respects it |
|---|---|---|
| Never promise employment or "job-ready in X days"; certificates are not the value proposition | GTM v3 §5, §8 | Job-readiness is delivered as **verifiable evidence and interview practice**, never as a claim. No "job-ready score", no placement promise. |
| Hard wedge: BA, DA, PM, PD first; 3–6 fully designed topics; quality over quantity | PRD v4 §7, §12 | Everything is phased (§9). SC and SD tracks exist in Curriculum v4 but sit outside the PRD wedge: treated as later. |
| Heavy social, community and leaderboards are out of v1 | PRD v4 §3.2, §12 | Social features moved to post-v1 and made opt-in. No leaderboards at any stage. |
| Don't optimise time-on-site; production over consumption | PRD v4 §11 | Weekly goals and rewards tie to thinking quality, never volume or time. |
| Earned assistance; the AI never writes the learner's structure or recommendation | PRD v4 §5, §11 | Reps, Story Bank and Translator only rephrase what the learner produced. |
| Scores are evidence of behaviour in practice, not fixed ability | PRD v4 §7.3 | Rubric levels per dimension only; no single number (already F7). |
| Personal / work problem mode is a leading indicator of repeat utility | PRD v4 §7.4, §10 | Promoted to a core retention feature (§2.3). |
| **Struggle first, then teach the concept** ("Here is a company where fixing one problem keeps creating another. Figure out why.") | Curriculum v2 §12 | Adopted as a rule for every concept block (§4.3). v4's "concept set + quiz" risks losing this. |
| Audience: Indian students (Tier 2/3), switchers, professionals; must feel credible, "not a game, school or coaching centre" | V1 brand brief | Sticky mechanics stay calm and adult; no confetti-style gamification, no kids' tone. |

## 1. Where the ideas now live (moved in batch K1, 26 Sep 2026)

The launch-scope engagement and career features are now specified in the kit. This file keeps the constraints, the post-launch plan, the metrics and the risks.

| Idea (old section) | Now specified in |
|---|---|
| Day-1 win (§2.1) | `05` F9; `03` T4 (lite `DAY1` case) |
| Daily Thinking Rep (§2.2) | `05` F10 |
| Personal Problem mode (§2.3) | `05` F11 |
| Job-simulation wrapper (§2.4) | `03` T4 "Inbox brief"; `01` §3 |
| Skill map, revision as reward, no XP (§3) | `05` F16, F5; `01` §9 |
| Weekly goal instead of streak | `05` F16 |
| Stakeholder chat, data room, Opponent, red-team | `05` scripted-mode table, F1, F6; `03` T4, T6 |
| Tree builder, decision sim, estimation duel (§4) | Platform batches P8, P9, P13 in `BUILD_PLAN.md` |
| Struggle first, then teach (§4.3) | `02` §1 |
| Onboarding plan (§5.1) | Platform batch P10 in `BUILD_PLAN.md` |
| Experience Translator, Story Bank (§5.2–5.3) | `05` F12; `03` T10 |
| Interview Lab (§5.4) | `05` F13; `03` T8 |
| JD Decoder (§5.5) | `05` F14; `03` T10 |
| Public portfolio, evidence checklist (§5.6–5.7) | `05` F15 |
| Tool Fluency Labs (§5.8) | `03` T9 |

## 2. Grow (post-first-job, post-v1)

| Code | Module | Owns |
|---|---|---|
| L1 | Career Launch | interview structures, telling a thinking story, résumé as evidence, JD reading, networking, negotiation basics, first 90 days |
| L2 | Lead With Thinking | raising thinking quality in a team, managing up, scoping ambiguity, decision meetings, promotion cases |

Also: monthly Live Cases from real public events, and a six-month Career Compass re-diagnostic that suggests the next module or track.

## 3. Social layer (post-v1, opt-in only)
Consistent with the PRD, nothing social ships in v1. Later: small pods with rubric-based peer review, a weekly "same case, compare Thinking Records" view, and mentor office hours. No leaderboards.

## 4. Reconciling the user's goal ("makes people job-ready")
The goal stands, but the GTM spec is right that outcomes can't be promised before evidence exists. So the platform aims to make the *evidence* of readiness strong (portfolio, stories, interview reps, JD-matched gaps) and measures real outcomes (§10), then earns the right to make claims later.

## 5. Phasing (fits PRD scope)

> **Superseded (26 Sep 2026):** the founder chose a full launch with no pilot. The v1 and v1.5 rows below both ship at launch for BA, DA, PM and PD, with AI features in scripted form. See `business/02_Execution_Plan.md`. The v2 row still applies.

| Phase | Ships | Rationale |
|---|---|---|
| **v1 (BA, DA, PM, PD; 3–6 topics)** | Day-1 win, Daily Rep, Personal Problem mode, skill map, tree builder, stakeholder chat, estimation duel, AI Opponent, Thinking Record, portfolio (private), struggle-first rule | Activation, first-week retention, visible progress |
| **v1.5** | Story Bank, Experience Translator, Interview Lab (4 roles), JD Decoder, public portfolio, Tool Fluency Labs, decision sim | Career value once the learning loop is validated |
| **v2** | SC and SD tracks, L1/L2, Live Cases, pods and peer review, employer view, Career Compass | Expansion after evidence |

## 6. Measure it (aligned with PRD metrics and GTM validation order)

| Question | Metric |
|---|---|
| Do they understand it quickly? | Day-1 case completion |
| Do they return? | D1 / D7 / D30 to deep practice; Daily Rep and Personal Problem use |
| Are they learning? | Rubric level change per dimension between first and latest case; revision improvement; calibration gap |
| Do they trust the feedback? | Feedback helpfulness rating; complete-answer leakage rate |
| Is it job-relevant? | Interviews completed in Lab, interview invites and role changes at 90/180 days (self-reported, later verified) |
| Will they pay? | Conversion after Day-1 win, Interview Lab and Story Bank (natural paid-tier candidates; still an open question in the PRD) |

## 7. Risks
- **Gamification eroding thinking:** rewards tied to rubric level and revision only.
- **AI scoring drift:** human sampling of at least 10% of scored work.
- **Scope creep against the PRD's hard wedge:** anything outside the launch scope waits.
- **Content ageing:** quarterly market refresh; one named owner for Live Cases.
- **AI cost:** cap Opponent and Interview Lab sessions per day; cache persona prompts.
- **Privacy:** portfolio and résumé data private by default; explicit opt-in for sharing.
- **Naming drift:** docs use both "Learn2Think" and "Think 2 Learn"; settle on one before public copy.
