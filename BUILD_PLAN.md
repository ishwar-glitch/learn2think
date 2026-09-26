# Learn2Think — Build Plan (launch queue)

**Statuses:** `PENDING` · `PARTIAL` · `BUILT – awaiting review` · `APPROVED` · `CHECK`
**Types:** **K** = kit/rules · **P** = platform code (`app/`) · **C** = content (`content/`)

The founder only ever says: **"Continue the Learn2Think build plan."** Take the next `PENDING` batch whose dependencies are `APPROVED` (P and C batches may alternate; follow the week order). One batch per session.

Plan and rationale: `business/02_Execution_Plan.md`. Session rules: `CLAUDE.md`.
Launch scope: BA, DA, PM, PD + career layer. **SC and SD are out of scope until after launch** (S9, S10, S13, S14 and U-IN-5 not built).

| ID | Wk | Contents | Depends on | Status |
|---|---|---|---|---|
| **K1** | 1 | Update kit for launch: add scripted-AI fields to T4/T6 (stakeholder question menu, opponent script with checklist/escalation/concession, hint ladder L0–L5, self-review checklist); add templates T8 interview bank, T9 tool lab, T10 skills taxonomy; add F9–F16 and "scripted mode" to `05_Platform_Features.md`; change the curriculum to 4 tracks; replace streaks with a weekly goal (V3 anti-goal); slim the `00_Build_Rules` read order (only the Universe profiles and modules the batch uses; `python`, not `python3`, on Windows); move ideas from `kit/06` into the kit where they now apply | — | APPROVED |
| **P1** | 1 | Scaffold `app/` (Astro + React + TS + Tailwind), design tokens from `design/DESIGN_SYSTEM.md` (light + dark), icons from `L2T_V1.0/brand`; Firebase project (Auth: Google + email link, Firestore, rules emulator tests); git init, private GitHub repo (**ask the founder before pushing**), Cloudflare Pages deploy, CI running validators; fill the commands in `CLAUDE.md` | — | BUILT – awaiting review |
| **P2** | 1 | Waitlist landing page (email + role + student/switcher), PostHog, Sentry | P1 | PENDING |
| **D1** | 1 | Clickable low-fidelity wireframes (plain HTML, phone-first, grey boxes, real sample text from CASE-M2) in `design/wireframes/`: landing, onboarding, Day-1 case, dashboard + skill map, concept block (Situation→Attempt→Reveal), quiz with confidence, tree builder, case inbox + stakeholder chat + data room, submission + self-review + Opponent, Thinking Record, portfolio (private/public), Interview Lab, Story Bank, JD Decoder, pricing/paywall. Follow the V3 Design & UX brief (calm, no chat-box default, progressive disclosure). Founder reviews in one pass; the approved screens become the spec for P4 onward. | K1 | APPROVED |
| **D2** | 2 | Restyle the wireframes as modern, minimal mock-ups using `design/DESIGN_SYSTEM.md`; apply `design/D1_decisions.md` (approved) and any wireframe feedback; freeze the screen list and navigation map (`design/SCREENS.md`) | D1 | APPROVED |
| **D3** | 2 | Full UI/UX redesign of the 19 mock-ups | D2 | APPROVED |
| **C0** | 1 | Company Universe: 8 profiles (U-IN-1…4, U-GL-1…4) per T5 | K1 | APPROVED |
| **P3** | 2 | Content pipeline: zod schemas for T1–T10, content collections from `../content`, module/case routes, CI validation | P1, K1 | PENDING |
| **P4** | 2 | (needs D2) Concept block player (Situation → Attempt → Reveal → Check → Go Deeper); quiz engine 1 (mcq, multi, order, classify); confidence prompt; attempts saved | P3 | PENDING |
| **P5** | 2 | Quiz engine 2 (fill, estimate, AUDIT); error tags; hints; Mastery Check scoring + calibration pass rule | P4 | PENDING |
| **C1** | 2 | M1 How Businesses Work + CASE-M1 | C0 | PENDING |
| **C2** | 2 | M2 Problems & Questions + CASE-M2 | C0 | PENDING |
| **P6** | 3 | Case player 1: inbox brief (job-sim wrapper), Student/Professional variants, stakeholder chat (menu), data room (exhibit requests logged) | P5 | PENDING |
| **P7** | 3 | Case player 2: submission, hint ladder, self-review vs checklist, model answer reveal, Thinking Record (fields by stage), private portfolio | P6 | PENDING |
| **CHK** | 3 | **Template check** (replaces the old pilot gate; code work continues). Founder + 3–5 people play M1–M2 end to end for 2 days, then send one consolidated feedback list. | P7, C1, C2 | CHECK |
| **K2** | 3 | Apply template-check feedback to kit/02, kit/03 and M1–M2; log changes | CHK | PENDING |
| **C3** | 3 | M3 Structuring Problems + CASE-M3 | K2 | PENDING |
| **P8** | 4 | Tree builder (issue/driver/KPI trees, MECE and "so what?" checks, distractors; port the V1 `tree` drill) | P5 | PENDING |
| **C4** | 4 | M4 Research Methods + CASE-M4 | K2 | PENDING |
| **C5** | 4 | M5 Evidence & Causation + CASE-M5 | K2 | PENDING |
| **C6** | 4 | M6 Numbers & Metrics + CASE-M6 | K2 | PENDING |
| **P9** | 4 | Estimation duel (range + confidence); calibration tracking (F3) | P5 | PENDING |
| **C7** | 5 | IC1 The Broken Business + Day-1 micro-case (`DAY1`, fictional restaurant, Neha Rao: the one non-Universe exception) | C6 | PENDING |
| **P10** | 5 | Onboarding (role, student/switcher, hours → plan), Day-1 flow, dashboard | P7 | PENDING |
| **P11** | 5 | Skill map (rubric levels per Thinking Loop stage), error profile (F5), progress | P7 | PENDING |
| **C8** | 5 | M7 Decisions & Trade-offs + CASE-M7 | K2 | PENDING |
| **P12** | 6 | Scripted AI Opponent: persona challenge → response → self-check → escalate/concede → revision + "what changed" | P7 | PENDING |
| **C9** | 6 | M8 Systems & Stakeholders + CASE-M8 | K2 | PENDING |
| **C10** | 6 | IC2 The System Under Pressure | C9 | PENDING |
| **P13** | 6 | Decision sim (multi-round) + red-team-the-AI audit screen | P7 | PENDING |
| **C11** | 7 | M9 Judgment & AI + CASE-M9 | K2 | PENDING |
| **C12** | 7 | M10 Communicate & Execute + CASE-M10 | K2 | PENDING |
| **C13** | 7 | IC3 The Master Challenge | C12 | PENDING |
| **P14** | 7 | Daily Reps generator (tags + error profile, spaced repetition, weekly goal), weekly recap email | P11 | PENDING |
| **P14b** | 7 | Personal Problem worksheet (Thinking Loop steps → Thinking Record; unlimited on Free, challenge step on Plus; privacy note) | P7 | PENDING |
| **P15** | 7 | Diagnostic placement: test out via Mastery Checks (F4), switcher path | P5 | PENDING |
| **C14** | 8 | S1 User Research | K2 | PENDING |
| **C15** | 8 | S2 Experimentation | K2 | PENDING |
| **C16** | 8 | S3 Processes & Requirements + CASE-BA-1 | K2 | PENDING |
| **C17** | 8 | S4 Solutions & Change + CASE-BA-2 | C16 | PENDING |
| **P16** | 8 | Midpoint `/code-review` + `/simplify`; fix backlog; low-end Android check | P15 | PENDING |
| **C18** | 9 | CASE-BA-3, CASE-BA-4 | C17 | PENDING |
| **C19** | 9 | CAP-BA (loan-origination transformation, U-IN-2) | C18 | PENDING |
| **C20** | 9 | S5 Working with Data & SQL + CASE-DA-1 (exhibits as tables) | K2 | PENDING |
| **P17** | 9 | SQL sandbox (sql.js; case exhibits loaded as tables; answer checking) | P7 | PENDING |
| **C21** | 10 | S6 Statistical & Causal Analysis + CASE-DA-2 | C20 | PENDING |
| **C22** | 10 | CASE-DA-3, CASE-DA-4 | C21 | PENDING |
| **C23** | 10 | CAP-DA (cutting discounts, U-GL-2) | C22 | PENDING |
| **C24** | 10 | S7 Product Discovery & Strategy + CASE-PM-1 | C14 | PENDING |
| **P18** | 10 | Razorpay subscriptions (monthly, annual, founding), entitlements and paywall, webhook Cloud Function, billing page, refunds | P10 | PENDING |
| **C25** | 11 | S8 Product Metrics, Economics & Launch + CASE-PM-2 | C24 | PENDING |
| **C26** | 11 | CASE-PM-3, CASE-PM-4 | C25 | PENDING |
| **C27** | 11 | CAP-PM (quick-commerce subscription tier, U-IN-1) | C26 | PENDING |
| **C28** | 11 | S11 Interaction & Usability + CASE-PD-1 | C14 | PENDING |
| **P19** | 11 | Story Bank + Experience Translator | P7 | PENDING |
| **C29** | 12 | S12 Design at Scale & AI UX + CASE-PD-2 | C28 | PENDING |
| **C30** | 12 | CASE-PD-3, CASE-PD-4 | C29 | PENDING |
| **C31** | 12 | CAP-PD (first-time digital-loan applicant, U-IN-2) | C30 | PENDING |
| **P20** | 12 | Interview Lab (timed rounds, on-device audio, self-rating, Mock Loop) + evidence checklist | P19 | PENDING |
| **P21** | 12 | JD Decoder (paste JD → taxonomy match → gaps → recommendations) | P19 | PENDING |
| **C32** | 13 | Interview banks: shared behavioral + BA, DA, PM, PD (T8) | K1 | PENDING |
| **C33** | 13 | Tool Fluency Labs ×4 (T9) + Translator and JD skill taxonomies (T10) | K1 | PENDING |
| **P22** | 13 | Public portfolio (opt-in, share cards), expert-review queue (admin), PD image/link upload | P18 | PENDING |
| **P23** | 13 | Lifecycle emails (welcome, weekly recap, renewal reminder; no guilt nudges) | P18 | PENDING |
| **P24** | 14 | Landing, pricing, public Case-of-the-Week and SEO pages; invite waitlist to accounts | P18 | PENDING |
| **P25** | 14 | Legal pages (terms, privacy, refund, grievance), DPDP consent, data export/delete, 18+ gate | P18 | PENDING |
| **C34** | 14 | Final content QA: validator on everything, concept-ownership check, IN/GLOBAL balance, `content/reports/FINAL_QA.md` | all C | PENDING |
| **P26** | 14 | `/security-review`; Firestore Security Rules audit; secrets check | P25 | PENDING |
| **P27** | 15 | Playwright smoke tests for core journeys; accessibility pass | P26 | PENDING |
| **P28** | 15 | Fixes from friendly testers (1) | P27 | PENDING |
| **P29** | 15 | Fixes from friendly testers (2) | P28 | PENDING |
| **P30** | 16 | Performance (low-end Android, slow network), 375px pass, analytics events verified | P29 | PENDING |
| **P31** | 16 | Final `/code-review` + fixes; runbook in `CLAUDE.md` | P30 | PENDING |
| **AUD** | 16 | **Opus** pre-launch audit: scoring logic, entitlements, launch checklist (Execution Plan §8) | P31 | PENDING |

Buffer: 9 slots, 3 used (D1, D2, P14b) across W5, W6, W9, W13, W14, plus W17–W19. If more than 5 slots behind, apply the cut list in Execution Plan §9.

## Notes from the founder
- No pilot gate. The template check (CHK) is the only pause, and it pauses content only.
- Default model: Sonnet 5. Opus only for AUD.
- Plans and summaries: markdown in this folder.

## Log
<!-- One line per session: date · batch · outcome · resume note if PARTIAL · any kit changes -->
- 2026-09-26 · planning · Business plan, execution plan, CLAUDE.md and this queue written; old B0–B12 queue replaced (B-content mapped to C0–C34; SC/SD deferred)
- 2026-09-26 · K1 · BUILT – awaiting review · kit changes: `03` T4/T6 scripted-AI fields (inbox brief, stakeholder menu, Opponent script, hint ladder L0–L5, self-review checklist, lite DAY1 case), new T8–T10 and ID rows, `content/interview|labs|taxonomy` folders; `05` scripted-mode table + F9–F16 (weekly goal replaces streaks); `01` cut to 4 launch tracks (S9/S10/S13/S14, SC, SD, U-IN-5 marked post-launch; S11/S12 kept), career layer §10; `02` struggle-first rule, scripted length limits, checklist items 13–15; `00` read order slimmed, `python` not `python3` (also `tools/validate_quiz.py`); `06` reduced to constraints, mapping table, post-launch, metrics, risks
- 2026-09-26 · D1 · BUILT – awaiting review · 19 wireframe screens + index + FEEDBACK.md in `design/wireframes/` (open `index.html`); K1 treated as approved when the founder said go (its 3 review items still open). Plan gap found: Personal Problem mode (F11) has no P batch. No kit changes.
- 2026-09-26 · D1 decisions approved (design/D1_decisions.md); P14b added
- 2026-09-26 · D1 · APPROVED · founder answered all 41 questions in `design/D1_decisions.md` (input for D2; includes knock-ons: P14b Personal Problem in W7, Business Plan §6 Free tier, rubric level names, Thinking Record labels)
- 2026-09-26 · D2 · BUILT – awaiting review · all 41 decisions applied to the 19 wireframe screens (each has a "Decided" box; generator scripts kept in `design/_src/`); `design/SCREENS.md` written (screen list, states not drawn, navigation map); domain in URLs left as `[domain]` until the week-1 name decision. Kit changes: `04_Rubric` level names now Starting/Developing/Solid/Strong (no K1 template used the old names); `05` F2 fields 2 "First take" and 11 "What would change my mind" (also in F11's step list). Business Plan §6: Plus row now names the Personal Problem challenge step and Story Bank; refund note already present. P14b and the buffer line were already in place (9 slots, 3 used).
- 2026-09-26 · Design system set (design/DESIGN_SYSTEM.md): founder palette, minimal style; D2 and P1 updated
- 2026-09-26 · D2 (restyle) · BUILT – awaiting review · all 19 screens restyled via design/wireframes/wf.css with DESIGN_SYSTEM tokens (light + dark, Inter, carrot primary with khaki text, willow progress, ✓/✕ plus colour for feedback); SVG radar recoloured in _src; checked at 375px in light and dark. Preview: Claude Code launch config 'wireframes' (python http.server on 8735).
- 2026-09-26 · D3 · BUILT – awaiting review · full redesign of the 19 mock-ups: audit in `design/D3_audit.md`; new shell (desktop rail, phone tab bar with Lucide icons, focus mode with sticky action), new components (choice/confidence, thinking types with icon+label+pattern+tint, skill-map radar, Thinking Record document, hint ladder, tree, exhibits), light/dark tokens, notes moved to a drawer. Quiz feedback fixed. All 41 decisions kept. Contrast AA verified by `design/_src/contrast.py`; 375px and 1280px checked in light and dark; no horizontal overflow; interactions tested. Sources: `_src/ui.py`, `bodies_a.py`, `bodies_b.py` (metadata still in `pages_a/b.py`). `DESIGN_SYSTEM.md` now v2 with component inventory.
- 2026-09-26 · D2, D3 · APPROVED by founder
- 2026-09-26 · C0 · BUILT – awaiting review · 8 Universe profiles + `tools/validate_universe.py` (0 failures); summary `content/reports/C0_summary.md`; no kit changes
- 2026-09-26 · C0 · APPROVED with changes · renamed U-IN-1 to Pinlo, U-IN-2 to Tarazu Credit, U-GL-3 to Fixnest (name collisions found by web search); wireframe sample data aligned to canon; DAY1 exception recorded (kit/00_Build_Rules, C7 row)
- 2026-09-26 · P1 · BUILT – awaiting review · `app/` (Astro 5 + React + Tailwind 4, D3 tokens light/dark, V1 icons, home + /signin, content collections on ../content), `firebase/` (rules, indexes, function stubs, Google + email-link code on placeholder config, 52 emulator tests pass), git init, CI workflow, `app/DEPLOY.md`, CLAUDE.md Commands. Build passes; checked 375px + desktop, light + dark. Not done (founder): Firebase project, GitHub repo + push, Cloudflare Pages. Note: firebase-tools pinned 13.35.1 (Java 11 here).
