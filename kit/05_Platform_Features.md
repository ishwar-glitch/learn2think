# Learn2Think — Platform Features (written once, used everywhere)

This file is for your developers, and it tells the content builder what **not** to write per module. Each feature below runs generically, driven by tags and fields inside the content.

## Scripted mode (launch)
**No live LLM calls at launch** (`business/02_Execution_Plan.md` §5). Every "AI" feature below runs from content written at build time. Where a feature says *Scripted*, that is the launch behavior; *Live upgrade* is a later batch and must keep the same content fields so nothing is rewritten.

| Feature | Scripted (launch) | Content it reads |
|---|---|---|
| F1 Opponent | Persona challenge → learner self-checks against the checklist → escalation once or concession → revision + "what changed" | T4 Opponent script |
| Stakeholder chat | Menu of questions, limited asks, canon-only answers; chosen questions feed the Questioning score | T4 Stakeholder menu |
| F6 Hints | Hint ladder L0–L5, level logged | T4 Hint ladder |
| F7 Scoring | Self-review checklist → model answer with alternatives → common mistakes; level per dimension from ticks plus platform checks | T4 Self-review checklist, Evaluator notes |
| `AUDIT` items | Pre-written AI analyses with planted flaws | T2, T6 |
| Personal Problem (F11) | Guided Thinking Loop worksheet | Platform template |
| F12–F14 | Templates, static taxonomy, keyword matching on learner-confirmed facts | T8, T9, T10 |

**Rules for all scripted features:** answers use only canon and case facts; never give the answer or write the learner's structure or recommendation; never abusive; no employment or "job-ready" claims; user text stays in the learner's account (nothing is sent to a model).

---

## F1. AI Opponent
Runs after a learner submits a case recommendation, at Stage 3 and above.

**Inputs:**
- the learner's submission
- the case's Evaluator notes
- the case's Opponent hooks

**Persona library:**

| Persona | Core attack |
|---|---|
| Skeptical Manager | "Why should I believe this?" (evidence, logic gaps) |
| CFO | Cost, return, payback, opportunity cost |
| Customer | "This makes my experience worse" (harm, friction, trust) |
| Competitor | "Here's how we respond" (strategic durability) |
| Frontline Employee | "This won't work on the ground" (feasibility, incentives) |
| Regulator / Risk | Compliance, fairness, privacy |

**Rules:**
1. Use the case's hooks to pick 2–4 personas and their angles.
2. Each persona asks one challenge. If the learner's answer is weak, it escalates once. If the learner addresses the concern with evidence or a trade-off, it concedes.
3. Only use facts that are in the case. Never give the answer. Never be abusive.
4. The learner then revises their recommendation and states what changed and why.

---

## F2. Thinking Record
Generated after every case. It has 12 fixed fields:

1. Problem
2. Initial interpretation
3. Assumptions
4. Questions asked
5. Hypotheses
6. Evidence
7. Alternatives
8. Trade-offs
9. Decision
10. Confidence
11. What could prove me wrong
12. Reflection

**Fields shown by stage:**

| Stage | Fields |
|---|---|
| Understand | 1–4, 12 |
| Investigate | 1–6, 12 |
| Decide | 1–10, 12 |
| Deliver and beyond | all 12 |

The platform pre-fills what it can from the learner's submission and asks the learner to complete the rest. Records are saved to the learner's **portfolio**.

---

## F3. Confidence & Calibration
- Every quiz item asks for confidence (50/70/90%) before the answer is revealed.
- The platform tracks accuracy by confidence band, per learner and per skill tag.
- Module M9 uses the learner's own calibration history as teaching material.
- **Calibration pass threshold** (used in Mastery Checks): average |confidence − accuracy| ≤ 15 points.

---

## F4. Diagnostic Placement (career switchers)
- The learner takes the Mastery Checks of M1–M10 before starting.
- Passing a module's check marks it "tested out". The learner can still take it optionally, and its case remains required for the portfolio.

---

## F5. Error Profile
Wrong answers carry Error Library tags. The platform aggregates each learner's most frequent errors and recommends which concept blocks and cases to revisit ("You often treat symptoms as problems — try CASE-M2 Professional").

---

## F6. Hints & Variants
- The **Student** variant shows the case's hint ladder (L1–L5, see T4) on request, one level at a time. Each level used is logged; it is *not* penalized, but shown in feedback.
- The **Professional** variant withholds exhibits until the learner requests them by name or description, then logs which ones they asked for. Asking for the right data is part of the Questioning score.

---

## F7. Scoring pipeline
1. AI structure check against the rubric dimensions the case lists.
2. Comparison with the model answer and its accepted alternatives.
3. The learner self-scores Reflection.
4. Human review for integrated challenges and capstones.

**Output:** a level per dimension, with feedback. Never a single 0–100 score.

---

## F8. Required tooling by track

| Track | Tooling |
|---|---|
| DA | In-browser SQL sandbox with each case's exhibits loaded as tables |
| SD (post-launch) | Diagramming canvas; entry diagnostic for programming and web basics |
| PD | Image or link upload, plus written design rationale |

---

## F9. Day-1 win
Before M1, every new learner plays the `DAY1` micro-case (lite T4, about 15 minutes): ask up to 3 questions from the stakeholder menu (good questions unlock an exhibit), write a 3-sentence recommendation, self-check against one Skeptical Manager challenge, and revise once. Output: a first Thinking Record (fields 1–4 and 12) in the portfolio and a first look at the skill map. The questions chosen give a light role-fit hint (BA / DA / PM / PD); it is a suggestion, never a gate.

## F10. Daily Thinking Rep
5 minutes, generated from tagged quiz items and case exhibits (no new authoring). Rep types: Symptom or problem? · Spot the flaw · Estimate it (range + confidence) · Audit the AI · 60-second pre-mortem · Change my mind.
- Draws first on the learner's Error Profile (F5) tags and lapsed concepts (spaced repetition).
- Always ends with the confidence prompt (F3).
- Feeds the weekly goal (F16), not a daily counter.

## F11. Personal Problem mode
The learner brings a real work or interview problem. A guided worksheet walks the Thinking Loop stage by stage (problem, assumptions, questions to ask, hypotheses, options, trade-offs, decision, what could prove me wrong) using prompt questions only; it never supplies an answer. Output: a Thinking Record saved to the private portfolio. The learner's text never leaves their account at launch.

## F12. Story Bank and Experience Translator
- **Story Bank:** each Thinking Record converts, by template, into a STAR/CAR story, a 2-minute "walk me through your thinking" version and a one-page case summary, tagged by competency (T10). Only rephrases fields the learner wrote.
- **Experience Translator (switchers):** the learner lists past duties; the platform matches them to `TX-<role>` past-duty patterns and Thinking Loop stages, shows competency gaps, and suggests Professional case variants. Résumé bullet stems are filled only with facts the learner confirms.

## F13. Interview Lab
Runs T8 banks as timed rounds: prompt → learner answers aloud or in text (audio recorded and stored **on the device only**, never uploaded) → scripted follow-up → self-rating against the "strong answer includes" checklist and model answer. Three graded mock rounds per role plus an optional Mock Loop. Uses the shared behavioral bank. Ratings feed the evidence checklist (F15); no readiness score.

## F14. JD Decoder
The learner pastes a job description. The platform keyword-matches it to `TX-<role>` (T10), shows which competencies the learner has evidenced, which are gaps, and which skills the platform does not cover, and recommends cases and labs for the gaps. Runs in the browser; the pasted text is not stored unless the learner saves it.

## F15. Portfolio and evidence checklist
- **Portfolio:** private by default. The learner may publish chosen cases as a public page showing the rubric level per dimension, the Thinking Record and how each item was scored (self-review + platform checks; capstones show whether founder-reviewed). Revocable at any time.
- **Evidence checklist:** for a target role, lists what the learner has *demonstrated*: scored cases, capstone level, Story Bank coverage, interview rounds completed, lab artifacts, JD gaps. States facts, never a verdict, "job-ready" score or placement claim.

## F16. Weekly goal (replaces streaks)
- The learner sets a weekly practice goal (default 3 reps or 1 case step) at onboarding and can change it any time.
- Progress shows as "this week: 2 of 3". Missing a week resets nothing, removes nothing and sends no guilt copy.
- Rewards and milestones tie to thinking quality and revision (a revised answer after an Opponent challenge moves the skill map most), never to time on site, volume or streak length. No leaderboards.
- A weekly recap says where the learner improved and which error tag they still hit.
