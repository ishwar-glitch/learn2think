"""Screen metadata (purpose, notes, sources) for 01-10. Bodies live in bodies_a.py."""
PAGES = []
SAMPLE = '<span class="sample">SAMPLE TEXT</span>'


def add(**k):
    PAGES.append(k)



# ---------------------------------------------------------------- 01
add(slug="01-landing", title="Landing and waitlist", nav=None,
    purpose="First contact. Explains the idea in 10 seconds, lets a visitor try the Day-1 case without signing up, and (before launch) joins the waitlist.",
    source="P2 waitlist page, P24 landing; Business Plan §5–6; Curriculum §2 (Thinking Loop). No job promises (06 §0).",
    notes=["Decided #2: the Day-1 case is playable before sign-up; progress is saved when the learner registers (screen 03).",
           "Two calls to action only: <b>Try the 15-minute Day-1 case</b> (goes to 03) and <b>Join the waitlist</b> (pre-launch only; the form is replaced by Sign in after launch).",
           "Waitlist asks three things: email, role you are aiming for, and student or career switcher. Nothing else.",
           "No claims about jobs, placements or being 'job-ready'. Copy says <i>evidence of how you reason</i>.",
           "No chat box, no stock photos of laptops; a real sample case screen is the hero image."],
    questions=["Headline: <b>\"Practise how you think, not what you memorised.\"</b> Keep, or do you want a different line?",
               "Should the free Day-1 case be playable <b>before</b> signup (my recommendation: yes, save progress only when they register)?"])

# ---------------------------------------------------------------- 02
add(slug="02-onboarding", title="Onboarding", nav=None,
    purpose="Turns four answers into a plan and a weekly goal, without a long form. Runs after the Day-1 case and sign-up (case, sign-up, onboarding, home).",
    source="P10 onboarding; 06 §5.1 (plan lengths); F16 weekly goal; F4 diagnostic placement for switchers.",
    notes=["One question per screen; progress dots on top.",
           "Output is a plan (Sprint about 14 weeks at 8–10 h/week; Steady about 28 weeks at 4–5 h/week) and a <b>weekly goal</b>, not a daily streak.",
           "Switchers get an optional test-out step: they can take a module's Mastery Check first (F4).",
           "'Not sure' is a valid role; the Day-1 case gives a light role-fit suggestion instead."],
    questions=["Ask <b>current role</b> only for switchers (shorter for students). OK?",
               "Should the plan show <b>calendar dates</b> (\"finish by 12 April\") or only \"about 14 weeks\"? Dates feel firm, weeks feel calmer."])

# ---------------------------------------------------------------- 03
add(slug="03-day1", title="Day-1 case (first 15 minutes)", nav=None,
    purpose="The first win: ask questions, write a 3-sentence recommendation, get challenged once, and leave with a first Thinking Record.",
    source="F9 Day-1 win; lite T4 (DAY1); stakeholder menu; Skeptical Manager script; Thinking Record fields 1–4 and 12.",
    notes=["Five steps: Brief, Ask (3 questions), Write, Challenge, Result. One step visible at a time.",
           "The learner sees only the question text. Whether a question was useful, irrelevant or leading is never shown as a mark; it feeds the Questioning level quietly.",
           "The challenge is scripted: the learner ticks a short checklist about their own answer, then sees the concession or the escalation.",
           "Result page shows the first Thinking Record fields and a first, incomplete skill map, plus a suggested role. It is a suggestion, not a gate."],
    questions=["Three questions is the limit here. Too few for a first case, or right?",
               "After step 5 the natural next screen is <b>onboarding</b> (02) then <b>home</b> (04). Should sign-up come <b>before</b> the case, or <b>after</b> (my recommendation)?"])

# ---------------------------------------------------------------- 04
add(slug="04-dashboard", title="Home and skill map", nav="home",
    purpose="Orients the learner around what to practise next. The skill map shows rubric level per Thinking Loop stage; there are no points.",
    source="P10 dashboard, P11 skill map and error profile; F5 error profile; F10 daily rep; F16 weekly goal; 06 §3.",
    notes=["Top card is always <b>one</b> next action (continue the case, or a 5-minute rep).",
           "Weekly goal is a plain fraction. No flame icon, no red states, no 'you broke your streak'.",
           "Bottom bar keeps 5 items (decided #7); the Career tab shows a light preview until Stage 2. Skill map sits second, under the next-action card (decided #8). Skill map: each axis is a Thinking Loop stage, scaled to rubric levels 1–4 (Starting to Strong). Unscored stages stay empty. Tap an axis to see the evidence behind it (screen 14).",
           "Error profile shows the learner's most repeated error tag and a case to revisit (F5).",
           "Locked Plus items are visible but quiet; a small 'Plus' tag, no nagging."],
    questions=["Bottom bar has 5 items: <b>Home, Learn, Cases, Career, Portfolio</b>. Right set, or should Career wait until later stages?",
               "Should the skill map be the <b>main</b> thing on home (as drawn, second) or first, above the next-action card?"])

# ---------------------------------------------------------------- 05
add(slug="05-concept", title="Concept block", nav=None,
    purpose="Teaches one idea the struggle-first way: Situation, Attempt, Reveal, Check, Go Deeper.",
    source="T1 concept block; P4 concept player; Style Guide §1 (struggle first) and length limits (Situation ≤120 words, Reveal ≤150).",
    notes=["Five steps, one on screen at a time. The concept is <b>not named</b> until the Reveal.",
           "The Attempt is a real answer, not a click. It is saved and shown back to the learner in the Reveal.",
           "Focus mode: bottom bar hidden; a close icon returns to Learn.",
           "The Check is 3–5 quick items (screen 06), each with a confidence prompt."],
    questions=["Should the learner be able to <b>skip the Attempt</b> (\"I don't know\") and still see the Reveal? Recommendation: yes, but it is logged.",
               "Reveal has a <b>\"when it misleads\"</b> line on purpose. Keep it?"])

# ---------------------------------------------------------------- 06
add(slug="06-quiz", title="Quiz with confidence", nav=None,
    purpose="Shows the interaction patterns used for checks and Daily Reps, so the product is not all multiple choice. Every item asks for confidence first.",
    source="T2 item types (SCN, SORT, RANK, EST, AUDIT, FIX); P4/P5 quiz engines; F3 confidence and calibration; Design brief §5.",
    notes=["Tabs are only for this wireframe. In the product each item appears alone, one after another.",
           "Confidence (Guessing / Fairly sure / Very sure, with the percentage small) must be chosen <b>before</b> Check is enabled. Try pressing Check without it.",
           "Feedback names the error and why it was tempting; it talks about the reasoning, never the learner's ability.",
           "Wrong choices carry an error tag behind the scenes (feeds the error profile).",
           "After a wrong answer there is no immediate retry; the item resurfaces in Daily Reps (decided #12).",
           "Written items (FIX, ASK) are self-checked against criteria at launch; the model answer appears after."],
    questions=["Confidence has three levels (50/70/90). Is that clear enough for a first-time learner?",
               "After a wrong answer, should the learner be able to <b>retry the same item</b> immediately, or only see it again later?"])

# ---------------------------------------------------------------- 07
add(slug="07-tree-builder", title="Tree builder", nav=None,
    purpose="Lets learners build an issue or driver tree by placing pieces, then checks it for overlap (MECE) and asks 'so what?'.",
    source="P8 tree builder; M3 (issue trees, MECE) and M6 (driver/KPI trees); V1 'tree' drill; Design brief §5 (map causes).",
    notes=["Tap a chip in the tray, then tap a slot to place it. Tap a filled slot to take it back. Try placing 'App downloads' and press Check.",
           "Tray includes <b>distractors</b> (relevant-looking but off-topic). Placing one is flagged with a hatch pattern and a reason.",
           "The MECE check names <b>overlaps</b> (two branches that count the same thing) and <b>gaps</b>; it does not give a score.",
           "The 'so what?' box asks what the learner would do differently if each branch turned out to be the cause.",
           "Decided #13: tap-and-place only at launch, no free typing of nodes. Decided #14: appears in M3 and M6, plus as an optional, ungraded tool inside cases.",
           "On a phone the tree scrolls down; on desktop it can sit side by side with the tray."],
    questions=["Building by tap-and-place suits a phone. Do you also want free typing of node names (harder to check, more open)?",
               "Should the tree builder appear only in M3/M6, or also as an optional tool inside cases?"])

# ---------------------------------------------------------------- 08
add(slug="08-inbox", title="Case inbox and brief", nav="cases",
    purpose="Frames every case as a job assignment. The learner opens a message from a Company Universe character and chooses Student or Professional.",
    source="T4 (inbox brief, Student and Professional variants); P6 case player; 06 §2.4 job-sim wrapper; F6.",
    notes=["Inbox is framing only; no new content. Sender, subject and deadline come from the case file.",
           "<b>Student</b> variant: clear prompt, exhibits provided, hint ladder available. <b>Professional</b>: vague manager message, exhibits on request, no hints.",
           "Case workspace tabs (Brief, Ask, Data, Draft) appear once the case is opened; screens 09–11.",
           "Promotions (Intern to Analyst) are optional framing and are drawn on screen 14, not here."],
    questions=["Choose variant <b>before</b> opening the message (as drawn) or let learners switch mid-case? Recommendation: choose first; switching later resets hints and asks.",
               "Should the free tier show the Professional variant locked (Plus) or hide it?"])

# ---------------------------------------------------------------- 09
add(slug="09-stakeholder", title="Stakeholder chat (scripted)", nav=None,
    purpose="The learner asks a stakeholder questions from a menu. Answers use only case facts. Good questions unlock exhibits. It is not a free-text chat.",
    source="T4 stakeholder menu; F1 scripted mode; P6; Rubric: Questioning. Execution Plan §5.",
    notes=["Menu of 10–15 questions per stakeholder in the real case; 8 shown here. Kinds are useful, irrelevant or leading. Kind is <b>not</b> displayed to the learner.",
           "Decided #17: the menu shows 4 questions at a time, refreshed after each ask, to keep the struggle. Decided #18: the results page (11) lists your most useful questions.",
           "<b>Asks are limited</b> (6 in Professional, 10 in Student). The counter is always visible; when it hits zero the menu closes.",
           "Leading questions get an honest answer that shows the trap; irrelevant ones get a polite non-answer, never a hint.",
           "Useful questions can <b>unlock an exhibit</b> (a chip appears, and the exhibit becomes available on screen 10).",
           "Free-text questions are the paid 'Live AI' upgrade later; the menu design carries over."],
    questions=["A menu means the learner sees good questions before thinking of them. To keep the struggle, the menu could show <b>only 4 questions at a time</b>, refreshed after each ask. Do this?",
               "Do you want to show, after the case, <b>which of your questions were most useful</b> (as feedback)? Recommendation: yes, on the results page."])

# ---------------------------------------------------------------- 10
add(slug="10-data-room", title="Data room", nav=None,
    purpose="Where exhibits live. In the Student variant they are all visible; in the Professional variant the learner must ask for each by name, and the request is logged.",
    source="T4 exhibits with request names and aliases; F6; P6; Rubric: Questioning and Research &amp; Evidence.",
    notes=["Try typing <i>delivery time by hour</i> or <i>rider roster</i> or <i>complaints</i> in the request box.",
           "Exhibits unlocked by stakeholder answers (screen 09) appear here already open. The others need a request.",
           "A request that matches nothing gets a nudge to be more specific, not a hint about the answer.",
           "Decided #19: after 3 misses a list of exhibit titles appears (try three vague requests). Decided #20: every exhibit can be downloaded as CSV (Student always; Professional once requested).",
           "Every request is logged; asking for the right data is part of the Questioning score.",
           "For DA cases this room also has an in-browser SQL box over the same tables (P17, not drawn)."],
    questions=["Free-text requests matched by keywords can miss a good phrasing. Alternative: a list of all exhibits by title (no struggle). Recommendation: keep requests but allow <b>three</b> misses before offering a list. OK?",
               "Exhibits open as tables here. Do you want <b>download as CSV</b> for the Student variant so learners can use their own tools?"])
