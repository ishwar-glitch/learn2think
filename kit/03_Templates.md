# Learn2Think — Templates (v4.2, launch scope)

## IDs & file locations

| Item | ID pattern | File |
|---|---|---|
| Core module | `M1`…`M10` | `content/core/M1/` |
| Specialist module | `S1`…`S14`; launch builds S1–S8, S11, S12 | `content/specialist/S1/` |
| Concept block | `M2-C03` | inside `concepts.md` |
| Quiz item | `M2-C03-Q02` | inside `quiz_items.json` |
| Mastery item | `M2-MC-Q05` | inside `quiz_items.json` |
| Company | `U-IN-1`, `U-GL-3` | `content/universe/U-IN-1.md` |
| Case | `CASE-M2`, `CASE-BA-2`, `IC1`, `CAP-PM`, `DAY1` | `content/cases/<ID>.md` |
| Interview bank | `IB-SHARED`, `IB-BA`, `IB-DA`, `IB-PM`, `IB-PD` | `content/interview/<ID>.md` |
| Interview question | `IB-PM-03` | inside its bank file |
| Tool lab | `LAB-BA`, `LAB-DA`, `LAB-PM`, `LAB-PD` | `content/labs/<ID>.md` |
| Skills taxonomy | `TX-BA`, `TX-DA`, `TX-PM`, `TX-PD` | `content/taxonomy/<ID>.md` |

Launch tracks: BA, DA, PM, PD. Post-launch: SC, SD.

Each module folder contains exactly:

- `concepts.md`
- `mastery_check.md`
- `quiz_items.json` (all items from both files)
- `report.md`

---

## T1 — Concept Set (`concepts.md`)

```markdown
# <M2> — <Module title>
**Stage:** <Understand/…>   **Depth range:** <from Style Guide>
**Learner outcome:** By the end you can <observable behavior>.
**Applies (not re-taught):** <concepts + owner modules>

## <M2-C01> — <Concept name>
**Context:** IN | GLOBAL   **Company:** <Universe ID>

### Situation  (≤120 words; don't name the concept)
### Attempt    (one question the learner answers before any teaching)
### Reveal     (≤150 words: name it, link it to their attempt, when it helps, when it misleads)
### Concept Check  → item IDs listed here; full items in quiz_items.json
### Go Deeper  (one ungraded question)
```

Use 5–7 blocks per module. Group small related concepts into one block.

---

## T2 — Quiz item JSON (`quiz_items.json` = array of items)

```json
{
  "id": "M2-C01-Q01",
  "module": "M2",
  "type": "SCN",
  "depth": 1,
  "context": "IN",
  "stem": "…",
  "exhibit": null,
  "options": [
    {"id": "a", "text": "…", "correct": true, "feedback": "…"},
    {"id": "b", "text": "…", "correct": false, "error_tag": "E02", "feedback": "…"}
  ],
  "explanation": "…",
  "confidence_prompt": true,
  "skills": ["problem-framing"]
}
```

Type-specific fields:

- **FIX:** replace `options` with `criteria` (list), `model_answer` and `common_errors` (error tags).
- **EST:** add `accepted_range` and `approach_criteria`.
- **SORT / RANK:** use `items` plus `correct_groups` or `correct_order`.
- **AUDIT:** add `ai_text` and `planted_flaws` (a list of `{description, error_tag}`), plus `criteria`.

---

## T3 — Mastery Check (`mastery_check.md`)
- 8–10 items covering every concept in the module, mostly at the stage's ceiling depth.
- At least 3 are FIX, ASK, EST or AUDIT.
- All situations are new; no stems reused from concept checks.
- The file lists item IDs and one line per item on what it tests. The full items go in `quiz_items.json`.
- **Pass rule:** ≥ 70% correct and calibration within ±15 points. The same check is used for diagnostic placement.

---

## T4 — Case (`content/cases/<ID>.md`)

```markdown
# <CASE-M2> — <Title>
**Company:** <Universe ID>   **Context:** IN | GLOBAL   **Currency:** ₹ | USD
**Used by:** <modules/tracks>   **Depth:** D3 | D4   **Rubric dimensions scored:** <list>

## Scenario (learner-facing, ≤200 words)

## Inbox brief (job-sim wrapper, ≤80 words)
From: <recurring character from the Universe profile> · Subject · the ask · deadline. Framing only; the Scenario carries the facts.

## Student variant
Prompt · Deliverable · Exhibits provided: E1, E2 … · Hints: see the Hint ladder (L1–L5 on request)

## Professional variant
Manager message · Deliverable · Exhibits available only on request (list what exists; the learner must ask) · No hints (the stakeholder menu and data room do that job)

## Exhibits
E1 <title> — CSV-ready table
E2 …
(Stakeholder quotes at Stage 3+.) Each exhibit gets a request name and 2–3 alias phrases so the data room can match a learner's wording.

## Stakeholder menu (scripted stakeholder chat)
Per stakeholder (1–3 per case), 10–15 questions. Learner-facing answers use only canon and case facts.

| ID | Question (≤ 20 words) | Kind | Answer (≤ 60 words) | Unlocks | Score signal |
|---|---|---|---|---|---|
| SQ-CASE-M2-01 | … | useful / irrelevant / leading | … | E2 or – | e.g. Questioning: baseline asked |

- Mix per stakeholder: about 5–7 useful, 3–4 irrelevant or low-value, 2–3 leading (tag `E17`; the answer is honest but shows the trap).
- Ask limit: **6 asks** per stakeholder in the Professional variant (Student: 10). Say so in the brief.
- At least 2 useful questions must be needed to unlock the exhibits the model answer depends on.
- An irrelevant question gets a short, polite non-answer, never a hint.

## Opponent script (scripted AI Opponent, feeds F1)
2–4 personas from `05_Platform_Features.md`. For each:
- **Challenge** (≤ 40 words, in the persona's voice, using only case facts)
- **Strong-answer checklist:** 2–4 yes/no items the learner checks against their own reply (each cites the evidence or trade-off a strong reply contains)
- **Escalation** (≤ 40 words): shown once if the learner marks the checklist mostly "no"; sharper, still uses only case facts
- **Concession** (≤ 30 words): shown if the checklist is mostly "yes"; names what the learner did well
- **Revision prompt:** one sentence pointing at the part of the recommendation the challenge targets

## Hint ladder (earned assistance; the platform records the level used, never penalizes)
| Level | Gives | Rule |
|---|---|---|
| L0 | Nothing | The task as written |
| L1 | Restates the goal | What a good answer must achieve, in other words |
| L2 | A guiding question | One question that points at the gap, no answer inside it |
| L3 | A pointer | Names the relevant concept (owner module) or exhibit to look at |
| L4 | A worked cue | The kind of evidence or step needed, on a different company's example |
| L5 | A parallel example | A short worked example on a different situation; never this case's answer or structure |

Write L1–L5 for every Student variant. Each ≤ 40 words. The hints never reveal the recommendation or write the learner's structure.

## Self-review checklist (learner-facing, shown before the model answer)
6–8 yes/no statements the learner ticks about their own submission, each mapped to a rubric dimension (e.g. "I stated what would prove me wrong" → Reflection). The platform then shows the model answer with accepted alternatives and the common mistakes; the level per dimension comes from the learner's ticks plus the platform's checks.

## Opponent hooks (design notes for the Opponent script)
- Skeptical Manager: <the weakest point to probe>
- <Persona>: <angle>
(2–4 hooks; each has a matching script entry above.)

## Evaluator notes (hidden)
- What is really happening
- Planted signals, noise and red herrings, and where they are
- Consistency Check (key calculations)
- Model answer: reasoning path, assumptions, confidence, acceptable alternative conclusions
- Common failure patterns (error tags)
```

**Day-1 micro-case (`DAY1`)** uses a lite T4: one stakeholder with 8–10 menu questions and a 3-ask limit, one persona (Skeptical Manager) in the Opponent script, no hint ladder beyond L1–L2, and a 5-item self-review. Learner output is a 3-sentence recommendation. Thinking Record fields 1–4 and 12.

---

## T5 — Company Profile (`content/universe/<ID>.md`)
- Name
- Context & currency
- One-paragraph story
- Business model
- **Canon facts** (8–12 numbers or facts that never change: scale, cities or markets, revenue band, key metrics, founding year)
- Org chart with 5–6 named recurring characters
- Known strengths and weaknesses (as seeds for cases)
- Which cases use it (keep this list updated)

---

## T6 — Integrated Challenge / Capstone
Use T4 (including the stakeholder menu, Opponent script, hint ladder and self-review checklist), plus:
- a **stage list:** the Thinking Loop steps required, each with its own deliverable, time guide, **its own self-review checklist** (4–5 items) and hint ladder L1–L3
- an **AI-generated analysis** with planted flaws (IC3 and all capstones): written out in full as the pre-written "AI analysis", with `planted_flaws` (description, error tag, location) and a criteria list, per the `AUDIT` format in T2
- a **boss-round Opponent script:** 3–4 personas in order, each with the T4 checklist, escalation and concession, plus a closing "what changed and why" prompt
- rubric weighting per dimension
- a note that human review is required; capstones are marked "Founder review (paid add-on)" and the model answer is shown after the learner's self-review

---

## T7 — Module Report (`report.md`)
- Files created
- Self-Review Checklist results (15 lines, pass/fail, with fixes made)
- Validation script output summary
- **Needs human review:** every `[VERIFY]` item, anything uncertain, any concept needed but not owned
- New error tags added
- Universe changes (new canon facts or characters)

---

## T8 — Interview Bank (`content/interview/<IB-ID>.md`)
One shared bank (`IB-SHARED`: behavioral, motivation, composure) and one per role (`IB-BA`, `IB-DA`, `IB-PM`, `IB-PD`). The Interview Lab runs these as timed rounds; audio stays on the device.

```markdown
# <IB-PM> — <Role> interview bank
**Rounds:** 3 graded mock rounds (R1, R2, R3), 4–5 questions each, plus an optional Mock Loop of all three.
**Dimensions self-rated (1–4):** structure · clarity · composure · concision (+ role dimension below)

## Round R1 — <name, e.g. Product sense>
### <IB-PM-01> — <short title>
**Type:** behavioral | case | technical | portfolio | role-play   **Competency tag:** <from TX-<role>>
**Prompt** (≤ 40 words, read aloud or shown)
**Time:** answer 2–3 min
**Strong answer includes** (3–5 yes/no checklist items the learner self-rates)
**Weak patterns** (error tags, e.g. E01, E16)
**Scripted follow-up** (one, ≤ 30 words, shown after the answer; a probe on the weakest usual part)
**Model answer** (≤ 150 words, reasoning path shown)
**Links:** concept blocks or cases that build this skill
```

Role simulations (one per bank, in R1–R3): BA stakeholder-elicitation role-play and process problem; DA live SQL, metric-drop diagnosis and A/B readout; PM product sense, execution/metrics and prioritization; PD portfolio walk-through and design critique. The shared bank has 15–20 behavioral questions tagged by competency (feeds the Story Bank).

---

## T9 — Tool Fluency Lab (`content/labs/<LAB-ID>.md`)
Tool-agnostic; the output is a portfolio artifact, not a certificate.

```markdown
# <LAB-DA> — <Title>
**Role:** BA | DA | PM | PD   **Company:** <Universe ID>   **Time:** ≤ 90 min
**Artifact produced:** <e.g. one-page dashboard spec, PRD, process diagram, design rationale>
**Tool options:** two or three interchangeable tools (free tiers), plus "pen and paper" where possible

## Brief (≤ 150 words)
## Provided materials (exhibits or data; for DA the tables, CSV-ready, loaded into the in-browser sandbox)
## Steps (≤ 5; each step names the output)
## Artifact checklist (5–8 yes/no items the learner self-checks)
## Model artifact (short, annotated with why each part is there)
## Common mistakes (error tags where they apply)
## Portfolio caption (a template of 2 sentences the learner completes)
```

DA labs also list the expected queries and their results so the sandbox can compare row counts and values. Launch labs: BA (user stories + process diagram), DA (SQL, one dashboard, data-quality check), PM (PRD, roadmap, metrics read-out), PD (design rationale, critique).

---

## T10 — Skills Taxonomy (`content/taxonomy/<TX-ID>.md`)
Static data for the Experience Translator, JD Decoder and Evidence Checklist. Keyword matching only, no LLM.

```markdown
# <TX-PM> — <Role> skills taxonomy
**Last refreshed:** <date>   **Source:** <how the skills list was checked, e.g. N sampled postings> [VERIFY]

## Competencies (12–20)
| ID | Competency | Thinking Loop stage | Keywords and synonyms (for matching JDs and past duties) | Built by (modules, cases, labs) | Interview tag |
|---|---|---|---|---|---|

## Past-duty patterns (Translator)
| Learner says (typical phrasing) | Maps to competency | Suggested Professional case | Bullet stem (filled only with learner-confirmed facts) |
|---|---|---|---|

## JD signals
| JD phrase or tool | Competency | If not yet evidenced, recommend |
|---|---|---|

## Out of scope for matching
Skills the platform does not teach (list them, so the JD Decoder can say "not covered here").
```

Rules: never claim a competency is "achieved", only "evidenced" by a scored case, lab artifact or completed interview round. No "job-ready" language.
