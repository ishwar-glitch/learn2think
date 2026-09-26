# Learn2Think — frozen screen list and navigation map (D2)

Status: frozen for launch. Source: 19 wireframes in `design/wireframes/` (open `index.html`) with the 41 approved decisions in `D1_decisions.md` applied. Case text in the wireframes is sample only. Changes to this list go through the founder.

URLs use `[domain]` until the week-1 name decision.

## 1. Screens drawn

| ID | Name | Route | Tab | Purpose | Built by |
|---|---|---|---|---|---|
| 01 | Landing and waitlist | `/` | none | Explain in 10 seconds; try Day-1 case (no sign-up) or join waitlist | P2 (waitlist), P24 (full landing) |
| 02 | Onboarding | `/start/plan` | none | Role, current role (switchers), hours → plan in weeks (show-dates toggle), weekly goal, optional test-out | P10 |
| 03 | Day-1 case | `/day1` | none | 15-minute first win: brief, 3 asks, write, challenge, first Thinking Record; then sign-up | P10 |
| 04 | Home and skill map | `/home` | Home | One next action, weekly goal, skill map (second), error profile, path, Career preview until Stage 2, Personal Problem entry | P10 (home), P11 (map, errors) |
| 05 | Concept block | `/learn/:module/:concept` | none (focus) | Situation → Attempt (skippable, logged) → Reveal → Check → Go Deeper | P4 |
| 06 | Quiz with confidence | `/check/:id` | none (focus) | Item types with confidence gate (Guessing / Fairly sure / Very sure); no instant retry. Also the Daily Rep shell | P4, P5; Daily Rep in P14 |
| 07 | Tree builder | `/learn/:module/tree/:id` | none (focus) | Tap-and-place issue/driver/KPI tree, MECE and so-what checks. In M3, M6; ungraded tool in cases | P8 |
| 08 | Case inbox and brief | `/cases`, `/cases/:id` | Cases | Job-sim framing; choose variant first (Professional locked on Free) | P6 |
| 09 | Stakeholder chat | `/cases/:id/ask` | none (focus) | Scripted menu, 4 questions shown at a time, ask limit | P6 |
| 10 | Data room | `/cases/:id/data` | none (focus) | Exhibits, requests by name (3 misses → list), CSV download | P6 (SQL box: P17) |
| 11 | Submission, hints, self-review, results | `/cases/:id/draft` | none (focus) | Structured draft, hint ladder (one per tap), self-review, model answer, levels (Starting to Strong), most useful questions, capstone review button | P7 |
| 12 | Scripted Opponent | `/cases/:id/challenge` | none (focus) | 2 personas (core) or 3 (IC, capstone); no skip; stop and resume | P12 |
| 13 | Thinking Record | `/records/:id` | Cases | 12 fields by stage; "First take", "What would change my mind"; editable, version 1 kept | P7 |
| 14 | Portfolio and evidence | `/portfolio` | Portfolio | Private items, evidence checklist, public page (handle, per-item levels); capstone review link | P7 (private), P22 (public, review queue) |
| 15 | Interview Lab | `/career/interview` | Career | Timed rounds; text default, voice optional; locked tab visible on Free | P20 |
| 16 | Story Bank | `/career/stories` | Career | STAR, 2-minute, one-pager, résumé bullets (confirmed facts); one free story | P19 |
| 17 | JD Decoder | `/career/jd` | Career | Matched and gap skills, no percentage; saved only on Save | P21 |
| 18 | Pricing and paywall | `/pricing` | none | Annual first, 7-day first-purchase refund, founding code (waitlist only); paywall preview | P18 (billing), P24 (public page) |
| 19 | Personal Problem worksheet | `/learn/personal-problem` | Learn | 7-step worksheet → Thinking Record; unlimited on Free, challenge step on Plus; privacy note | **P14b (new, week 7)** |

## 2. States and screens not drawn

Built to the same patterns (calm, no guilt, one action per screen). Each needs a short state list when its batch starts; none needs a new wireframe round.

| Not drawn | Rule for the builder | Batch |
|---|---|---|
| Sign in / create account | Google only; appears after Day-1 (03), never before | P1, P10 |
| Empty states (no cases, no stories, no records, no saved JDs) | One sentence and one button; no blank pages | with each screen |
| Error and offline states | Plain message, saved work is never lost, retry button | with each screen; P30 |
| Settings and account (profile, weekly goal, plan pace, notifications, data export and delete, 18+) | Under a profile menu on Home, not in the bottom bar | P25, P10 |
| Billing page (plan, renewal date, cancel, refund) | Renewal date and cancel always visible | P18 |
| Daily Rep | Reuses 06 with a 5-minute set and weekly-goal bar | P14 |
| Diagnostic and test-out | Mastery Check flow, reuses 06 | P15 |
| Estimation duel, decision sim, red-team-the-AI | Variants of 06 and 08–11 | P9, P13 |
| SQL sandbox | Inside the Data room for DA cases | P17 |
| Capstone expert-review order and admin queue | Button on 11 and 14; queue is admin only | P22 |
| Experience Translator | Sits in the Career tab beside 16 | P19 |
| Tool Fluency Labs | Career tab, four labs | P22 area (content C33) |
| Public portfolio page, share cards, Case of the Week, legal pages | Public, no bottom bar | P22, P24, P25 |
| Emails (waitlist confirmation, weekly recap, renewal) | Plain text, no guilt nudges | P2, P23 |

## 3. Navigation map

**Bottom bar (5, phone; side rail on desktop):** Home · Learn · Cases · Career · Portfolio. Career shows a light preview until Stage 2 is reached; locked items are visible, quiet and tagged "Plus" on Free.

| Tab | Lands on | Reaches |
|---|---|---|
| Home (04) | Next-action card, weekly goal, skill map | Case (08), Daily Rep (06), Personal Problem (19), Career preview (15), Thinking Record via skill-map evidence (13) |
| Learn | Module list (Home's Path card, list not drawn) | Concept (05) → Check (06) → Tree (07) in M3, M6 → Personal Problem (19) |
| Cases | Inbox (08) | Ask (09) ↔ Data (10) ↔ Draft (11) → Opponent (12) → Thinking Record (13) |
| Career | Interview Lab (15) | Story Bank (16), JD Decoder (17); Translator |
| Portfolio | Cases tab (14) | Thinking Record (13), Evidence, Public page, capstone review (11) |

**Main flows**

1. First visit: 01 → 03 (Day-1, no account) → sign-up → 02 → 04.
2. Learning: 04 → 05 → 06 → 04 (or next concept).
3. Case: 08 → 09 ↔ 10 → 11 (draft, hints, self-review, results) → 12 → 13 → 14 or 16.
4. Career: 13 → 16 → 15; 14 (evidence gaps) → 17.
5. Upgrade: any locked item → paywall (18); Professional variant, Interview Lab, M3.
6. Personal Problem: 04 or Learn → 19 → 13.

**Focus-mode screens (no bottom bar, close icon returns to origin):** 03, 05, 06, 07, 09, 10, 11, 12. The case workspace tabs (Brief · Ask · Data · Draft) replace the bar inside a case; 08 and 13 keep it. 01, 02 and 18 have no bar.

**Rules that hold everywhere:** no streaks, points or leaderboards; weekly goal only; no employment or "job-ready" wording; hints, model answers and notes closed until asked; chat only as the scripted menu in 09.
