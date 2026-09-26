# Learn2Think — Business Plan (v1, 26 Sep 2026)

Bootstrapped · India-first · freemium subscription · full launch (no pilot) targeted **25 Jan 2027**.
Companion: `02_Execution_Plan.md` (how it gets built with Claude Pro in ~4 months).

> Figures marked **(verify)** are approximate and must be checked before they're used in public copy or decisions.

---

## 1. Summary

| | |
|---|---|
| **Promise** | "We help you learn to think better." Practice that builds, and *proves*, professional reasoning. |
| **Who** | Indian college students, early-career professionals and career switchers targeting BA, DA, PM or PD roles |
| **What** | 10 core thinking modules, 3 integrated challenges, 4 role tracks with capstones, and a career-evidence layer (Interview Lab, Story Bank, Experience Translator, JD Decoder, public portfolio) |
| **Why it wins** | Interactive practice with a rubric instead of videos; an evidence portfolio instead of certificates; priced for students; near-zero running cost |
| **Model** | Freemium. Plus at ₹399/month or ₹2,499/year; capstone expert review ₹999 (capped) |
| **Cost to build** | ≈ ₹15–30k cash over 4 months (Claude Pro + domain + registration). No developers, no paid tools. |
| **Cost to run** | < ₹5,000/month at launch. Live AI switches on only when paid users fund it. |
| **Year-1 base case** | ~500 paid subscribers and ~₹1.7L MRR by month 12 after launch (§8) |

## 2. Problem

- India has **~4.3 crore students in higher education** (AISHE 2021–22) **(verify latest)**, and industry surveys put graduate employability at **only ~50–55%** (India Skills Report 2024/2025) **(verify)**.
- The gap is less about knowing tools and more about **thinking on unfamiliar problems**: framing, questioning, weighing evidence, trade-offs and communicating a decision. Interviews for BA, DA, PM and PD roles test exactly these.
- The options available today:
  - **Expensive bootcamps:** ₹1–4 lakh and heavy on syllabus.
  - **Passive courses:** videos with no feedback on reasoning.
  - **General AI chat:** hands over answers, which removes the thinking work.
- **Career switchers** already have experience but can't *translate* it into the language and evidence of a new role.

## 3. Solution

| Layer | What the learner does | Evidence produced |
|---|---|---|
| Day-1 micro-case | Solves a real mini-problem in 15 minutes | First Thinking Record |
| Core M1–M10 + IC1–IC3 | Struggles with the problem first, then learns the concept, then applies it; cases in the fictional Company Universe | Scored cases on the Thinking Quality Rubric |
| Role tracks (BA, DA, PM, PD) | Specialist modules, 4 track cases and a capstone | Capstone, optionally expert-reviewed |
| Career layer | Interview Lab, Story Bank, Experience Translator, JD Decoder, Tool Fluency Labs | Interview stories, résumé bullets, public portfolio |
| Habit layer | Daily Reps (5 minutes), weekly goal, skill map, Personal Problem worksheet | Calibration and skill growth over time |

**AI without runtime cost at launch:** every "AI" interaction ships in scripted form, written by Claude at build time: stakeholder question menus, persona challenges with strong-answer checklists, hint ladders and planted-flaw analyses. Live AI (Claude Haiku 4.5) is added for paid users once revenue covers it (§7). See Execution Plan §5.

## 4. Customers

| Segment | Job to be done | Willingness to pay | Launch priority |
|---|---|---|---|
| Final-year students and fresh graduates (Tier 1–3 cities) | "Get my first BA/DA/PM/PD job; stand out in interviews" | Low–medium; very price-sensitive | **Primary** |
| Career switchers (2–8 years' experience) | "Move into analytics/product without starting over" | Medium–high | **Primary** (highest ARPU and conversion) |
| Early-career professionals | "Grow faster, reason better at work" | Medium | Secondary |
| Colleges and placement cells | "Improve placement readiness at scale" | Budget exists; slow sales | After 6 months of outcome data |

## 5. Competition and positioning

Prices are approximate **(verify in week 1: 15-minute check)**.

| Alternative | Typical price | Where it falls short for this learner |
|---|---|---|
| Long bootcamps (Scaler, upGrad, Great Learning) | ₹1–4 lakh | Costly, tool- and syllabus-heavy; thinking isn't practised deliberately |
| Cohort fellowships (PM/analytics programmes) | ~₹30–60k | Time-bound; limited volume of practice |
| Self-paced courses (Coursera, Udemy, YouTube) | ₹0–5k | Passive; no feedback on reasoning |
| Practice platforms (Unstop, HackerRank) | Free–₹5k | Coding and aptitude focus, not business reasoning |
| General AI chat | Free–₹2k/month | Gives answers; no curriculum, rubric or evidence |
| **Learn2Think** | **₹0 / ₹2,499 a year** | Deliberate thinking practice + a verifiable evidence portfolio |

**Defensible assets:**
- The Thinking Quality Rubric.
- The Company Universe and its case library.
- Scripted interactive formats that are costly for others to copy well.
- The founder's domain expertise, which lets capstones be expert-reviewed.
- A cost structure that sustains student pricing.

**Positioning rules** (from the GTM v3 spec):
- Never promise jobs, placements or "job-ready in X days".
- Don't lead with AI.
- Certificates are never the headline; evidence is.

## 6. Business model and pricing

| Plan | Price | Includes |
|---|---|---|
| **Free** | ₹0 | Day-1 case; Stage 1 (M1, M2 and their cases); Daily Reps (3 a week); private portfolio; share cards for completed cases; unlimited Personal Problem worksheets; 1 Story Bank story |
| **Plus: monthly** | ₹399 | Everything: M3–M10, IC1–IC3, all 4 tracks and capstones, Professional variants, Interview Lab, Story Bank, Translator, JD Decoder, public portfolio, Tool Fluency Labs, unlimited reps, Personal Problem challenge step, unlimited Story Bank |
| **Plus: annual** | ₹2,499 | Same as monthly (about 6 months' price for 12) |
| **Founding member** | ₹1,499 for year 1 | First 500 waitlist members only; converts to the annual price at renewal |
| **Capstone expert review** | ₹999 per capstone | Written review by the founder against the rubric; **capped at 5 a week** |

**Policies:**
- 7-day refund on first purchase, to build trust.
- No auto-renew surprises: send a reminder 7 days before renewal.
- Prices include applicable taxes (§9).

**Later (not at launch):** college licences once outcome data exists, and team plans for companies.

### Unit economics (per paid subscriber per month)

| Item | Amount |
|---|---|
| Blended revenue (half monthly, half annual, net of ~2% payment fees) | **≈ ₹300** |
| Hosting and database share | ≈ ₹5–10 |
| Live AI (after trigger; Haiku 4.5 capped at ~15 persona sessions + 20 evaluations) | ≈ ₹66 (≈ ₹3.4 per session, < ₹1 per evaluation, at ₹90/$) |
| **Contribution margin** | **≈ 75% with live AI; ≈ 95% without** |

## 7. Costs

**Build phase (Oct 2026–Jan 2027), cash:**

| Item | Cost |
|---|---|
| Claude Pro | ~₹2,000/month × 4 **(verify with GST)** |
| Domain | ~₹1,000/year |
| Registration and CA consultation | ₹5–15k **(verify)** |
| Trademark (optional, class 41) | ~₹4,500 **(verify)** |
| Hosting, database, email, analytics | ₹0 (free tiers) |
| **Total** | **≈ ₹15–30k** |

**Running (launch year, monthly), within the ₹5,000 cap until live AI:**

| Item | Monthly |
|---|---|
| Claude Pro (maintenance and new content) | ~₹2,000 |
| Firebase Blaze plan (pay-as-you-go; needed for Cloud Functions; within free quotas at this scale) + daily Firestore backups | ~₹0–500 **(verify; set a ₹500 budget alert)** |
| Domain | ~₹100 |
| Cloudflare hosting, PostHog analytics, Resend email, Sentry monitoring | ₹0 (free tiers) |
| Razorpay | ~2% of revenue **(verify)** |
| Live AI (paid users only, after trigger) | ~₹66 per paid user |

**Live-AI trigger:** switch on when **MRR ≥ ₹50,000**, which is about month 5–6 in the base case. At that point AI is about 20% of paid revenue and is funded by it, not by the founder.

## 8. Financial projections (12 months after launch)

**Assumptions:**
- Organic acquisition only.
- New-signup conversion to paid within 30 days: 2.5% (conservative), 4% (base), 5% (strong).
- Monthly paid churn: 12%, 9% and 7% respectively.
- Blended revenue ₹300 per paid user; capstone reviews capped at 20 a month.
- Costs include ~₹2,200/month of backend and backup headroom from month 2 (conservative; Firebase is likely lower), live AI above ₹50k MRR, and payment fees.
- The founder's time is not costed.

| Scenario | Month | New signups/month | Cumulative free users | Paid users | MRR | Monthly costs | Cumulative net |
|---|---|---|---|---|---|---|---|
| **Conservative** | 3 | 314 | 844 | 19 | ₹7.2k | ₹4.5k | ₹3k |
| | 6 | 441 | 2,029 | 39 | ₹14.9k | ₹4.7k | ₹26k |
| | 12 | 870 | 6,033 | 96 | ₹36.4k | ₹5.2k | ₹1.6L |
| **Base** | 3 | 793 | 2,084 | 77 | ₹29.2k | ₹5.0k | ₹45k |
| | 6 | 1,207 | 5,252 | 175 | ₹66.3k | ₹17.4k | ₹1.7L |
| | 12 | 2,791 | 17,401 | 503 | ₹1.71L | ₹41.5k | ₹7.3L |
| **Strong** | 3 | 1,671 | 4,287 | 201 | ₹76.5k | ₹19.4k | ₹1.2L |
| | 6 | 2,745 | 11,330 | 493 | ₹1.68L | ₹40.8k | ₹4.3L |
| | 12 | 7,411 | 41,917 | 1,649 | ₹5.15L | ₹1.25L | ₹19.9L |

**What this means:**
- Cash-flow positive from month 1 in every scenario because fixed costs are tiny. The real question is **founder income**: base case clears about ₹1L a month net by month 9.
- Annual plans bring cash in upfront, so real cash is ahead of the MRR shown.
- The conservative case covers costs but not the founder, which triggers the decision rules below.

**Decision rules (in place of a pilot, the first 90 days after launch are the validation):**

| Signal by day 60 after launch | Action |
|---|---|
| Free→paid < 2% | Move the free/paid boundary (for example, make M3 free), then test the ₹1,999 annual price |
| D30 return < 8% | Pause new content; fix onboarding, reps and the first case |
| Refund rate > 10% | Interview refunders; fix the gap between promise and product |
| Switchers convert at twice the rate of students | Shift marketing to switchers; consider a ₹3,999 switcher bundle with expert reviews |
| Base case or better | Switch on live AI; start college pilots; plan SC and SD tracks |

## 9. Legal and compliance (confirm with a CA or lawyer)

**Entity:**
- A sole proprietorship with Udyam registration is the cheapest option for bootstrapping.
- An LLP or private limited company is better if you later raise money or add co-founders.
- Decide in week 1.

**GST:** registration is typically not mandatory below ₹20 lakh annual turnover for services **(verify for online education and your state)**. The live-AI API is an imported service; ask the CA about tax treatment.

**Personal data (DPDP Act 2023 and Rules):**
- Clear consent notice, purpose limitation, and data export and deletion on request.
- **Launch 18+ only**, to avoid verifiable parental consent for minors.
- Store the minimum; interview audio stays on the learner's device.

**Consumer terms:**
- Terms of service, refund policy and a grievance contact on the site. Check whether the Consumer Protection (E-Commerce) Rules 2020 apply to you.
- No outcome or placement claims in any copy.

**Payments:** Razorpay KYC can take days or weeks, so **apply in week 1**.

**Trademark:** run a public search on the IP India site before settling the name.

## 10. Go-to-market (bootstrapped, organic)

| When | Channel | Action | Target |
|---|---|---|---|
| Weeks 1–16 (build) | LinkedIn, building in public | 2 posts a week: "spot the flaw" and "symptom or problem?" puzzles taken from real content, plus build updates | 1,000 waitlist signups by launch |
| Weeks 4–16 | Campus clubs (consulting, product, analytics) and placement cells | Founder runs free 60-minute "Broken Business" workshops using IC1 (online) | 20 campuses contacted, 8 workshops |
| Weeks 8–16 | Communities (Reddit, Discord, Telegram, LinkedIn groups for PM/DA/BA aspirants) | Share free micro-cases; answer questions; no spam | 300 of the 1,000 waitlist |
| Week 17 | Soft launch to waitlist | Founding-member price for the first 500 | 150 paid |
| Week 18 | Public launch | Free Day-1 case with a share card; LinkedIn launch post; campus follow-ups | 2,000 signups in month 1 |
| Ongoing | Growth loops | Share cards on public portfolios (free); referrals (a month free for both sides); weekly public "Case of the Week" page for SEO and LinkedIn | — |
| Month 6+ | Colleges | Licence pitch backed by outcome data | 2 paying colleges by month 12 |

## 11. KPIs (targets; tracked in PostHog)

| Area | Metric | Launch target |
|---|---|---|
| Activation | Day-1 case completed / signups | ≥ 60% |
| Retention | D7 / D30 return to deep practice | ≥ 25% / ≥ 12% |
| Learning | Share of active paid users gaining ≥ 1 rubric level on ≥ 2 dimensions by their 5th case | ≥ 50% |
| Trust | "Feedback helped me improve" rating | ≥ 4/5 |
| Revenue | Free→paid within 30 days; monthly churn | ≥ 4%; ≤ 9% |
| Career evidence | Stories in the Story Bank; Mock Loops completed; self-reported interviews and offers at 90 and 180 days | Tracked; published only once verified |

## 12. Risks

| Risk | Likelihood | Mitigation |
|---|---|---|
| Built without a pilot, the product misses what learners need | Medium | Template check in week 3; friendly-tester week 15; decision rules in §8; fast fixes in weeks 17–20 |
| Solo founder overload (build, review, marketing, capstone reviews) | High | Fixed weekly rhythm; review caps; cut list; tasks automated via Claude |
| Claude Pro limits slow the build | Medium | Session sizing, Sonnet by default, 11 buffer slots, cut list (Execution Plan §2, §9) |
| Scripted "AI" feels shallow | Medium | Rich menus and checklists; live AI for paid users once MRR ≥ ₹50k |
| Content errors in unfamiliar roles | Medium | Validator, founder spot checks, full capstone review; recruit one reviewer for any role outside your experience |
| Non-coder maintaining code | Medium | Boring, documented stack; automated tests; runbook in CLAUDE.md |
| Price sensitivity | High | Generous free tier, founding price, annual plan, decision rules |
| Imitation by larger players | Low–medium | Speed; rubric and case IP; community of evidence |

## 13. Open decisions

1. **Name:** Learn2Think (brand assets exist) or Think 2 Learn (v3 specs). Decide in week 1, before the domain and trademark search.
2. **Your expert coverage:** which of BA, DA, PM and PD are you personally expert in? Any role outside that needs one outside reviewer by week 8.
3. **Entity type:** confirm with a CA in week 1.
