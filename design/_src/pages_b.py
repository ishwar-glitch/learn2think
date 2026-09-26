"""Screen metadata (purpose, notes, sources) for 11-19. Bodies live in bodies_b.py."""

PAGES = []


def add(**k):
    PAGES.append(k)


# ---------------------------------------------------------------- 11
add(slug="11-submit", title="Submission, hints and self-review", nav=None,
    purpose="Where the learner writes the recommendation, can climb the hint ladder, checks their own work against a checklist, and then sees the model answer.",
    source="T4 (deliverable, hint ladder L0–L5, self-review checklist, model answer, common mistakes); P7; F6, F7; Rubric.",
    notes=["Draft is <b>structured</b>, not a blank chat box. Evidence, assumptions, alternatives and trade-offs each have a different border style so the learner sees how they differ.",
           "Hint ladder: L1 restates the goal, L2 guiding question, L3 pointer to a concept or exhibit, L4 worked cue on another company, L5 parallel example. It is <b>never</b> the answer and never writes the learner's structure. Level used is logged, not penalized.",
           "Order after Submit: self-review ticks, then model answer with accepted alternatives, then common mistakes, then a level per dimension. No single score anywhere.",
           "Decided #21: one hint per tap. Decided #22: level names are Starting, Developing, Solid, Strong. Decided #23: the ₹999 review button appears here after a capstone submission and on the portfolio item.",
           "Confidence is asked once on the recommendation (50/70/90) and feeds calibration.",
           "Try: tap 'Need a hint?' several times; tick the checklist; press Submit."],
    questions=["Should the hint ladder be <b>one hint per tap</b> (as drawn) or a level picker?",
               "Levels shown after the case use rubric names (Emerging to Professional). Do these names feel right for students, or too grade-like?",
               "Founder review for capstones (₹999) starts from this screen. Where should the order button sit: here or on the portfolio page?"])

# ---------------------------------------------------------------- 12
add(slug="12-opponent", title="Scripted Opponent", nav=None,
    purpose="Stress-tests the recommendation with two or three persona challenges, then requires a revision and a written 'what changed and why'.",
    source="F1 scripted mode; T4 Opponent script (challenge, checklist, escalation, concession, revision prompt); P12.",
    notes=["Decided #24: no skip; stop and resume later. Decided #25: 2 personas in core modules (drawn), 3 in ICs and capstones.",
           "Each persona asks <b>one</b> challenge. The learner replies in their own words, then ticks a short checklist about that reply.",
           "Mostly yes shows a concession that names what they did well; mostly no shows one sharper challenge. Try both by ticking or not.",
           "Revision is mandatory and improving it moves the skill map more than a new attempt.",
           "Tone: firm, never abusive. Only case facts are used, and the Opponent never gives the answer.",
           "The live AI version later uses the same screen; only the source of the challenge changes."],
    questions=["Should the learner be able to <b>skip</b> a persona (e.g. after a bad day)? Recommendation: no skip, but they can stop and resume later.",
               "Three personas per case (Manager, CFO, Customer) as drawn, or two to keep it shorter?"])

# ---------------------------------------------------------------- 13
add(slug="13-thinking-record", title="Thinking Record", nav="cases",
    purpose="The artifact every case leaves behind: 12 fixed fields showing how the learner reasoned. Fields shown depend on the stage.",
    source="F2 Thinking Record (12 fields; shown by stage); P7; feeds portfolio (14) and Story Bank (16).",
    notes=["Fields 1–4 and 12 are shown in Stage 1 (Understand); 1–6 and 12 in Investigate; 1–10 and 12 in Decide; all 12 from Deliver on. The rest show as quiet placeholders naming the stage that unlocks them.",
           "The platform pre-fills what it can from the submission; the learner completes and edits the rest.",
           "Decided #26: labels are <b>First take</b> (field 2) and <b>What would change my mind</b> (field 11). Decided #27: editable after saving; version 1 is kept.",
           "Reflection (12) is written <b>before</b> the model answer is shown, and self-scored.",
           "Two actions: Save to portfolio (private by default) and Make a Story from this."],
    questions=["Fields are named in plain words (Problem, Initial interpretation…). Any you want relabelled?",
               "Should a learner be able to <b>edit</b> the record after saving? Recommendation: yes, with the original kept as version 1."])

# ---------------------------------------------------------------- 14
add(slug="14-portfolio", title="Portfolio and evidence", nav="portfolio",
    purpose="Shows what the learner has demonstrated, private by default, with an optional public page. It states facts, never a verdict or a 'ready' score.",
    source="F15 portfolio and evidence checklist; F2; T4 rubric; P22 public portfolio; 06 §0 (no employment claims).",
    notes=["Decided #28: a handle is allowed; real name optional. Decided #29: the learner picks, per item, which levels show publicly. Decided #23: capstone items link to the ₹999 founder review.",
           "Every item shows the rubric level per dimension and <b>how it was scored</b> (self-review + platform checks; capstones show whether the founder reviewed them).",
           "Each case has a Private / Public switch. Turning Public on asks for confirmation and shows exactly what will be visible.",
           "The evidence checklist lists what has been done (cases, capstone level, stories, interview rounds, lab artifacts). It never gives a percent or a readiness label.",
           "Stage progress may be phrased as optional titles (Intern, Analyst…) on this screen only."],
    questions=["Public page URL: <b>learn2think.in/p/&lt;name&gt;</b> style. Should learners use a real name, or may they choose a handle?",
               "Should the public page show <b>all</b> dimension levels or only levels 3–4 (Proficient and above)? Recommendation: learner picks per item."])

# ---------------------------------------------------------------- 15
add(slug="15-interview-lab", title="Interview Lab", nav="career",
    purpose="Timed interview practice from a question bank. The learner answers aloud (recorded on the device only) or in text, then self-rates against a checklist and a model answer.",
    source="F13 Interview Lab; T8 interview bank; P20; Execution Plan §5 (audio never uploaded).",
    notes=["Decided #30: text is the default, voice optional. Decided #31: the tab is visible but locked on Free (use the Free / Plus preview buttons).",
           "Three graded mock rounds per role, then an optional Mock Loop of all three. Shared behavioral bank sits under every role.",
           "Recording stays on the phone; the screen says so plainly. Nothing is uploaded at launch.",
           "After answering, the learner sees a scripted follow-up, then ticks 'A strong answer includes…' and reads the model answer. Ratings feed the evidence checklist.",
           "Career switcher and student see the same rounds; role is set at onboarding."],
    questions=["Voice answers are harder for many learners than typing. Should text answers be the <b>default</b> with voice optional? Recommendation: yes.",
               "Should Interview Lab be visible to free users as a locked tab, or hidden until Plus?"])

# ---------------------------------------------------------------- 16
add(slug="16-story-bank", title="Story Bank", nav="career",
    purpose="Turns a Thinking Record into interview stories, using only what the learner wrote and confirmed.",
    source="F12 Story Bank; P19; T10 competency tags; 06 §0 (the AI never writes the learner's answer for them).",
    notes=["Three views of one story: STAR, a 2-minute 'walk me through your thinking', and a one-page case summary.",
           "Stories are <b>assembled from the learner's own record fields</b> by template, not invented. Editing is expected.",
           "Each story is tagged by competency (from the role's skills taxonomy) so the learner can see coverage.",
           "Decided #32: one free story. Decided #33: résumé bullets are in at launch (template-based, confirmed facts only).",
           "Confirm box: the learner confirms each fact before it can appear in a résumé bullet."],
    questions=["Should the Story Bank be available to <b>free</b> learners for their first story (a taste), then Plus? Recommendation: yes, one free story.",
               "Résumé bullets are offered only for confirmed facts. Do you want this on the launch list or after?"])

# ---------------------------------------------------------------- 17
add(slug="17-jd-decoder", title="JD Decoder", nav="career",
    purpose="The learner pastes a job description and sees which skills they have evidenced, which are gaps, and which the platform does not cover.",
    source="F14 JD Decoder; T10 skills taxonomy (keywords and synonyms); P21; no LLM at launch.",
    notes=["Decided #34: saved only when the learner taps Save. Decided #35: matched and gap skills, no percentage.",
           "Runs in the browser; the pasted text is not stored unless the learner saves it.",
           "Three result groups: <b>Evidenced</b> (you have scored work for it), <b>Gaps</b> (with a recommended case or lab), <b>Not covered here</b> (honest about limits).",
           "Never says 'you are ready' or 'you would get this job'. It states what the learner has and has not shown.",
           "Keyword matching only; the taxonomy is refreshed quarterly from sampled postings."],
    questions=["Should saved JDs be kept (a list of roles the learner is targeting) or discarded after each use? Recommendation: keep only if the learner taps Save.",
               "Show a <b>match percentage</b>? Recommendation: no, because it reads like a job-readiness score."])

# ---------------------------------------------------------------- 18
add(slug="18-pricing", title="Pricing and paywall", nav=None,
    purpose="Explains Free vs Plus plainly, and shows the soft paywall a learner meets at Stage 2.",
    source="Business Plan §6 (Free, Plus ₹399 / ₹2,499, Founding member ₹1,499, Capstone review ₹999, capped at 5 a week); P18 Razorpay and paywall.",
    notes=["Decided #36: annual first, monthly secondary. #37: 7-day refund on the first purchase. #38: the founding offer needs a code, sent only to waitlist members. #40: Personal Problem unlimited on Free; Plus adds the challenge step.",
           "Prices, plan contents and the founding-member offer are taken from the Business Plan; confirm before build.",
           "Paywall appears when a learner opens M3. It says what they keep for free and what Plus adds. It never blocks portfolio access to work they have done.",
           "Prices include taxes (Business Plan §9). No auto-renew surprises: renewal date and cancellation are visible.",
           "No job or placement claims in any plan description.",
           "Toggle Monthly / Annual to see the price swap."],
    questions=["Show <b>₹2,499/year</b> as the main option (about ₹208/month) and monthly as secondary? Recommendation: yes.",
               "Is there a <b>refund window</b> to state on this screen (e.g. 7 days)? Not in the Business Plan yet; needs your decision.",
               "Founding-member offer: visible to everyone or only to waitlist members?"])

# ---------------------------------------------------------------- 19
add(slug="19-personal-problem", title="Personal Problem worksheet", nav="learn",
    purpose="The learner brings a real work or interview problem and works it through the Thinking Loop by answering prompts, ending in a Thinking Record.",
    source="F11 Personal Problem mode; Design brief §7 (Personal Problem UX). Built by batch P14b (week 7). Scripted worksheet at launch, never supplies the answer.",
    notes=["Seven steps from the brief: real situation, the decision or question, known/unknown/assumed, alternatives and consequences, decision, challenge the reasoning, next action.",
           "Decided #39: built in P14b. #40: unlimited on Free; step 6 (the challenge) is Plus. #41: the privacy note stays.",
           "Each step is a set of prompt questions; the platform never writes an answer or a recommendation.",
           "Text stays in the learner's account; nothing is sent to a model at launch.",
           "Step 6 uses the same self-check checklist pattern as the Opponent.",
           "Later, learners can revisit the record 'as the real situation evolves' (step 7 reminder)."],
    questions=["<b>Plan gap:</b> Personal Problem mode (F11) is not assigned to any P batch. Add it to a week-7 slot (P14 area)? Recommendation: yes.",
               "Personal Problem is one worksheet a month on Free. Should it be unlimited for Free (it is the strongest retention hook) and Plus adds the challenge step?",
               "Should there be a privacy note on this screen (\"Do not include confidential company data\")? Recommendation: yes."])
