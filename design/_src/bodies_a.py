"""D3 screen bodies 01-10. Text and interactions carried over from D2; layout and components redesigned."""
from ui import I, SAMPLE, radar, conf, tk, tklegend

B = {}


def ch(key, text, extra=""):
    return ('<button type="button" class="choice" data-act="select" %s><span class="key">%s</span><span class="txt">%s</span>'
            '<span class="state"></span></button>') % (extra, key, text)


def dock(inner):
    return '<div class="dock"><div>%s</div></div>' % inner


# ---------------------------------------------------------------- 01 Landing
B["01-landing"] = """
<header class="topnav"><a class="brand" href="#"><span class="mark">L2T</span>Learn2Think</a><a class="btn ghost sm" href="#">Sign in</a></header>
<section class="grid2 hero-l">
<div>
<p class="eyebrow">For students and career switchers · BA · DA · PM · PD</p>
<h1 class="display">Practise how you think, not what you memorised.</h1>
<p class="lede" style="margin:16px 0 24px">Real business problems, small steps, and feedback on your reasoning. Build a portfolio that shows how you think.</p>
<a class="btn primary block" style="max-width:360px" href="03-day1.html">Try the 15-minute Day-1 case """ + I("arrow") + """</a>
<p class="meta" style="margin-top:10px">No sign-up needed. Your progress is saved when you register.</p>
</div>
<div class="mock" aria-label="Preview of a case inbox">
<div class="mbar"><i></i><i></i><i></i></div>
<div style="padding:16px" class="stack">
<p class="eyebrow" style="margin:0">Case inbox · """ + SAMPLE + """</p>
<div class="list">
<div><span class="avatar alt">MI</span><div class="body"><div class="title">Whitefield delivery times</div><div class="sub">Meera Iyer · Head of Operations · Due Friday</div></div><span class="unread" aria-label="Unread"></span></div>
<div><span class="avatar alt">NR</span><div class="body"><div class="title">Fix our pricing</div><div class="sub">Neha Rao · Owner · Day-1 case</div></div></div>
</div>
<div class="tk evd"><div class="tk-h">""" + I("evidence", "sm") + """Evidence</div><span class="small">Riders wait 6 minutes per trip at the store (E2).</span></div>
<div class="tk asm"><div class="tk-h">""" + I("help", "sm") + """Assumption</div><span class="small">Picking, not riding, is the constraint.</span></div>
</div></div>
</section>

<section class="sec">
<div class="sec-h"><h2>How a session works</h2></div>
<div class="howit">
<div><h3>Try first</h3><p class="muted small">You attempt a small problem before anything is explained.</p></div>
<div><h3>See the idea</h3><p class="muted small">A short explanation, linked to what you just tried.</p></div>
<div><h3>Use it on a real case</h3><p class="muted small">Ask stakeholders, request data, write a recommendation, face a challenge.</p></div>
<div><h3>Keep the evidence</h3><p class="muted small">Each case leaves a Thinking Record in your portfolio.</p></div>
</div></section>

<section class="sec">
<div class="sec-h"><h2>Who it is for</h2></div>
<div class="chips"><span class="chip">Students</span><span class="chip">Career switchers</span><span class="chip">Business analysis</span><span class="chip">Data analysis</span><span class="chip">Product management</span><span class="chip">Product design</span></div>
</section>

<section class="sec grid2" style="align-items:start">
<div><h2>Join the waitlist</h2><p class="muted" style="margin-top:8px">We will email you once, when the first case is ready. Founding members (first 500) get a year at ₹1,499 with a code.</p></div>
<div class="card">
<label class="field"><span class="lab">Email</span><input type="email" placeholder="you@example.com" autocomplete="email"></label>
<div class="field"><span class="lab">I am aiming for</span><div class="choices inline" data-group>""" + "".join('<button type="button" class="choice" data-act="select"><span class="txt">%s</span></button>' % r for r in ["BA", "DA", "PM", "PD", "Not sure"]) + """</div></div>
<div class="field"><span class="lab">I am a</span><div class="segctl full" data-group><button type="button" class="sel" data-act="pill">Student</button><button type="button" data-act="pill">Career switcher</button></div></div>
<button class="btn dark block" data-act="reveal" data-target="wl" data-self="hide">Join the waitlist</button>
<div id="wl" class="hidden callout good" role="status">""" + I("ok") + """<div><b>You are on the list.</b> We will email you once, when the first case is ready, with your founding code.</div></div>
</div></section>

<section class="sec">
<div class="card flat row between"><div><h3>Free to start, priced for students</h3><p class="muted small" style="margin:4px 0 0">Stage 1 and the Day-1 case are free. Plus is ₹2,499 a year (about ₹208 a month) or ₹399 monthly.</p></div><a class="btn sm" href="18-pricing.html">See plans</a></div>
</section>
<footer class="meta row" style="margin-top:32px;gap:16px"><a href="#">FAQ</a><a href="#">Privacy</a><a href="#">Contact</a></footer>
"""

# ---------------------------------------------------------------- 02 Onboarding
def steps(n, total=4):
    return '<div class="steps" aria-label="Question %d of %d">%s</div>' % (n, total, "".join('<i class="%s"></i>' % ("cur" if i == n - 1 else "on" if i < n - 1 else "") for i in range(total)))


B["02-onboarding"] = """
<header class="topnav"><a class="brand" href="#"><span class="mark">L2T</span>Learn2Think</a><span class="meta">Set your plan · about 1 minute</span></header>
<div style="max-width:560px;margin:24px auto 0">
<div id="q1">""" + steps(1) + """
<p class="eyebrow">Question 1 of 4</p><h1>Which role are you aiming for?</h1>
<div class="choices" data-group style="margin:24px 0">
""" + ch("BA", "Business Analyst") + ch("DA", "Data Analyst") + ch("PM", "Product Manager") + ch("PD", "Product Designer") + ch("?", "Not sure yet <span class='meta'>· the Day-1 case suggested one</span>") + """
</div><button class="btn primary block" data-act="reveal" data-target="q2" data-hide="q1">Next</button></div>

<div id="q2" class="hidden">""" + steps(2) + """
<p class="eyebrow">Question 2 of 4</p><h1>Where are you now?</h1>
<div class="choices" data-group style="margin:24px 0">
""" + ch(I("learn", "sm"), "Student or fresh graduate") + ch(I("cases", "sm"), "Career switcher <span class='meta'>· I have work experience</span>", 'data-target="cur"') + """
</div>
<label id="cur" class="field hidden"><span class="lab">Your current role</span><span class="help">Only asked of switchers.</span><input type="text" placeholder="e.g. Operations executive"></label>
<button class="btn primary block" data-act="reveal" data-target="q3" data-hide="q2">Next</button></div>

<div id="q3" class="hidden">""" + steps(3) + """
<p class="eyebrow">Question 3 of 4</p><h1>How many hours a week can you give this?</h1>
<div class="choices" data-group style="margin:24px 0">""" + ch(I("clock", "sm"), "About 4–5 hours") + ch(I("clock", "sm"), "About 8–10 hours") + ch("?", "Not sure") + """</div>
<button class="btn primary block" data-act="reveal" data-target="q4" data-hide="q3">See my plan</button></div>

<div id="q4" class="hidden">""" + steps(4) + """
<p class="eyebrow">Your plan</p><h1>Steady pace, about 28 weeks</h1>
<p class="muted" style="margin-top:8px">4–5 hours a week. You can change this any time.</p>
<div class="card" style="margin:20px 0">
<ol class="stagerail">
<li class="cur"><span class="d"></span><div><b>Stage 1 · Understand</b><div class="meta">M1–M2 · free</div></div></li>
<li><span class="d"></span><div><b>Stage 2 · Investigate</b><div class="meta">M3–M6, IC1</div></div></li>
<li><span class="d"></span><div><b>Stage 3 · Decide</b><div class="meta">M7–M9, IC2</div></div></li>
<li><span class="d"></span><div><b>Stage 4 · Deliver</b><div class="meta">M10, IC3, then your track</div></div></li></ol>
<button class="link small" data-act="toggle" data-target="dates" aria-expanded="false">""" + I("clock", "sm") + """ Show dates</button>
<p id="dates" class="hidden meta" style="margin:8px 0 0">Roughly 12 April to 25 October if you start today. Dates move if you do; nothing is marked as late.</p>
</div>
<div class="field"><span class="lab">Weekly goal</span><span class="help">Practice reps per week. Miss a week and nothing resets or disappears.</span>
<div class="segctl full" data-group><button type="button" data-act="pill">2 reps</button><button type="button" class="sel" data-act="pill">3 reps</button><button type="button" data-act="pill">5 reps</button></div></div>
<div class="callout" style="margin-bottom:24px">""" + I("target") + """<div><b>Switching from another field?</b> Test out of modules you already know by taking their Mastery Check first. You still solve each case for your portfolio. <br><button class="link" style="margin-top:6px">Take a Mastery Check first</button></div></div>
<a class="btn primary block" href="04-dashboard.html">Go to my home</a></div>
</div>
"""

# ---------------------------------------------------------------- 03 Day-1
B["03-day1"] = """
<div id="s1" data-step="20|Step 1 of 5">
<p class="eyebrow">Day-1 case · 15 minutes · """ + SAMPLE + """</p>
<h1>The restaurant that got busier and poorer</h1>
<div class="card" style="margin:20px 0 12px">
<div class="person" style="margin-bottom:12px"><span class="avatar lg alt">NR</span><div><b>Neha Rao</b><div class="meta">Owner · to you</div></div></div>
<h3 style="margin-bottom:8px">Fix our pricing</h3>
<p style="margin:0">Since we joined the delivery app, orders are up 40% but I am making less money every month. I think our prices are too low. Can you fix our pricing by Friday?</p></div>
<p class="meta">You can ask Neha up to 3 questions before you write anything.</p>
""" + dock('<button class="btn primary block" data-act="reveal" data-target="s2" data-hide="s1">Ask my questions</button>') + """</div>

<div id="s2" class="hidden" data-step="40|Step 2 of 5">
<div class="row between"><div class="person"><span class="avatar alt">NR</span><div><b>Ask Neha</b><div class="meta">Owner</div></div></div>
<span class="counter"><span class="pips"><i></i><i></i><i></i></span><span id="asks">3</span> left</span></div>
<div id="chat" class="chat" aria-live="polite"></div>
<div id="asksdone" class="hidden callout good">""" + I("ok") + """<div>That is your 3 questions. On to your recommendation.</div></div>
<div class="asklist" style="margin-top:12px">
""" + "".join('<button class="ask" data-act="ask" data-who="Neha" data-q="%s" data-a="%s"%s>%s<span class="grow">%s</span></button>' % (q, a, (' data-unlock="%s"' % u) if u else "", I("chat", "sm"), q) for q, a, u in [
    ("What has changed in your costs since you joined the app?", "The app takes 28% of each order. Packaging is also up, and I hired two more people for the rush.", ""),
    ("How many orders now come through the app compared with dine-in?", "About 55% of orders are app orders now. Dine-in has slowed a little.", ""),
    ("What colour is your new menu?", "Green. Why do you ask? I do not think that is our issue.", ""),
    ("Do you agree raising prices is the answer?", "That is what I thought. But you are the one I asked.", ""),
    ("Which dishes sell most through the app?", "Biryani and paneer combos. They are also our lowest-margin dishes.", "E1")]) + """
</div>
""" + dock('<button class="btn primary block" data-act="reveal" data-target="s3" data-hide="s2">Write my recommendation</button>') + """</div>

<div id="s3" class="hidden" data-step="60|Step 3 of 5">
<p class="eyebrow">Step 3 · Write</p><h1>Your recommendation</h1>
<p class="muted" style="margin:8px 0 20px">Three sentences: what you think the real problem is, what you would check first, and what you would do.</p>
<textarea style="min-height:180px" aria-label="Your recommendation" placeholder="1. The real problem is…&#10;2. I would check first…&#10;3. I recommend…"></textarea>
""" + dock('<button class="btn primary block" data-act="reveal" data-target="s4" data-hide="s3">Submit</button>') + """</div>

<div id="s4" class="hidden" data-step="80|Step 4 of 5">
<p class="eyebrow">Step 4 · Challenge</p>
<div class="card" style="margin-bottom:24px"><div class="person" style="margin-bottom:12px"><span class="avatar lg">SM</span><div><b>Skeptical Manager</b><div class="meta">Scripted challenge</div></div></div>
<p style="font-size:18px;line-height:1.5;margin:0">“You have told me what to do. Why should I believe that is the cause, and not just what you assumed at the start?”</p></div>
<h3>Check your own answer</h3><p class="meta">Tick what is true.</p>
<div class="checks" data-ticks data-decided="1">
<label class="check"><input type="checkbox"> I pointed to a number or fact Neha gave me.</label>
<label class="check"><input type="checkbox"> I said what I would check before changing prices.</label>
<label class="check"><input type="checkbox"> I separated “orders up” from “profit down”.</label>
<div class="checkfoot"><span class="tickcount">0 of 3 ticked</span><span class="tickverdict"></span></div></div>
<div id="con" class="hidden callout good" style="margin-top:12px">""" + I("ok") + """<div><b>Conceded.</b> “You used the commission figure and separated volume from profit. That is a fair basis to go on.”</div></div>
<div id="esc" class="callout attn" style="margin-top:12px">""" + I("flag") + """<div><b>Sharper.</b> “The app takes 28% of each order. Would higher prices even fix that, or is it a different problem?”</div></div>
<label class="field" style="margin-top:24px"><span class="lab">Revise your recommendation</span><span class="help">Then say what changed and why.</span><textarea placeholder="What I changed, and what made me change it…"></textarea></label>
""" + dock('<button class="btn primary block" data-act="reveal" data-target="s5" data-hide="s4">Finish</button>') + """</div>

<div id="s5" class="hidden" data-step="100|Done">
<p class="eyebrow">Done · 15 minutes</p><h1>Your first Thinking Record</h1>
<div class="record" style="margin:20px 0">
<div class="rf"><span class="n">1</span><div><div class="k">Problem</div><div class="v">Profit falling while orders rise.</div></div></div>
<div class="rf"><span class="n">2</span><div><div class="k">First take</div><div class="v">“Prices too low” (your first view).</div></div></div>
<div class="rf"><span class="n">3</span><div><div class="k">Assumptions</div><div class="v">App commission is the main cost change.</div></div></div>
<div class="rf"><span class="n">4</span><div><div class="k">Questions asked</div><div class="v">Costs since the app · app share of orders · best sellers.</div></div></div>
<div class="rf"><span class="n">12</span><div><div class="k">Reflection</div><div class="v">You wrote this at the end.</div></div></div></div>
<h2 style="margin-bottom:4px">First look at your skill map</h2><p class="meta">Only what you have shown so far is filled in.</p>
""" + radar([2, 2, 0, 0, 0, 0, 1, 2]) + """
<div class="callout" style="margin:20px 0">""" + I("career") + """<div><b>A suggestion, not a gate:</b> your questions leaned towards costs and numbers. Try a Data Analyst or Business Analyst path first. You can pick any.</div></div>
<button class="btn primary block" data-act="reveal" data-target="su" data-self="hide">Save my progress</button>
<div id="su" class="hidden card" style="margin-top:8px"><h3>Create your account</h3><p class="meta">Your Day-1 work is saved to it.</p>
<div class="stack"><button class="btn block">Continue with Google</button><button class="btn block">""" + I("mail", "sm") + """ Email me a sign-in link</button>
<a class="btn primary block" href="02-onboarding.html">Continue to set my plan</a></div></div>
</div>
"""

# ---------------------------------------------------------------- 04 Home
B["04-dashboard"] = """
<p class="meta" style="margin:0">Friday · Week 3 of about 28</p>
<h1 style="margin:2px 0 20px">Good evening, Aarav</h1>
<div class="home">
<section class="hero" style="grid-area:hero">
<p class="eyebrow">""" + I("cases", "sm") + """Continue where you left off</p>
<h2>The Slow Dark Store</h2>
<p class="meta" style="margin:4px 0 12px">CASE-M2 · Step 2 of 4 · Ask stakeholders · about 25 min left</p>
<div class="steps" style="margin:0 0 16px"><i class="on"></i><i class="cur"></i><i></i><i></i></div>
<a class="btn primary block" href="09-stakeholder.html">Continue the case """ + I("arrow") + """</a>
</section>

<section class="card" style="grid-area:map">
<div class="sec-h"><h2>Your skill map</h2><span class="meta"><a href="14-portfolio.html">Evidence """ + I("right", "sm") + """</a></span></div>
""" + radar([2, 2, 1, 0, 0, 0, 1, 2]) + """
<p class="meta" style="margin:12px 0 0">Rubric level per Thinking Loop stage, from your scored work. Revising an answer moves it most.</p>
</section>

<section class="card pad-sm" style="grid-area:week">
<div class="row between"><h3>This week</h3><span class="small"><b>2</b> of 3 reps</span></div>
<div class="steps" style="margin:10px 0 14px" aria-hidden="true"><i class="on"></i><i class="on"></i><i></i></div>
<div class="row between"><div><b class="small">Daily Rep · Spot the flaw</b><div class="meta">5 minutes</div></div><a class="btn sm" href="06-quiz.html">""" + I("repeat", "sm") + """ Start</a></div>
</section>

<section class="card pad-sm" style="grid-area:err">
<p class="eyebrow">What you often do</p>
<p style="margin:0 0 4px"><b>Treat a symptom as the problem</b> <span class="chip">E02 · 4 times</span></p>
<p class="meta" style="margin:0">Try CASE-M2 in the Professional variant.</p>
</section>

<section style="grid-area:path">
<div class="sec-h"><h2>Your path</h2></div>
<div class="list">
<a href="05-concept.html"><span class="lead">""" + I("learn") + """</span><div class="body"><div class="title">Stage 1 · Understand</div><div class="sub">M1 How Businesses Work · done<br>M2 Problems &amp; Questions · in progress</div></div>""" + I("right", "sm") + """</a>
<div class="lock"><span class="lead">""" + I("lock") + """</span><div class="body"><div class="title">Stage 2 · Investigate</div><div class="sub">M3–M6 · Integrated challenge IC1</div></div><span class="chip plus">Plus</span></div>
<div class="lock"><span class="lead">""" + I("lock") + """</span><div class="body"><div class="title">Stage 3 · Decide</div><div class="sub">M7–M9 · IC2</div></div><span class="chip plus">Plus</span></div>
</div></section>

<section class="card flat pad-sm" style="grid-area:career">
<div class="row between"><h3>Career tools</h3><span class="chip">Opens at Stage 2</span></div>
<p class="meta" style="margin:6px 0 12px">Interview Lab, Story Bank and JD Decoder. Take a look now.</p>
<a class="btn sm" href="15-interview-lab.html">""" + I("eye", "sm") + """ Preview</a></section>

<section class="card flat pad-sm" style="grid-area:pp">
<h3>Personal Problem</h3><p class="meta" style="margin:6px 0 12px">Bring a real decision from work or an interview.</p>
<a class="btn sm" href="19-personal-problem.html">""" + I("pen", "sm") + """ Start a worksheet</a></section>
</div>
"""

# ---------------------------------------------------------------- 05 Concept
B["05-concept"] = """
<p class="eyebrow">M2 Problems &amp; Questions · Concept 2 of 6 · """ + SAMPLE + """</p>
<div id="a1" data-step="20|Step 1 of 5">
<h1>Situation</h1>
<div class="card" style="margin:20px 0">
<p>A quick-commerce dark store in Whitefield, Bengaluru, used to deliver in <b>14 minutes</b> on average. Over three weeks that has become <b>19</b>. Ratings fell from 4.4 to 4.0.</p>
<div class="person" style="margin-top:16px;padding-top:16px;border-top:1px solid var(--border)"><span class="avatar alt">MI</span><div><div class="meta">Meera, operations head</div><b>“We need 15 more riders in Whitefield by Friday.”</b></div></div></div>
""" + dock('<button class="btn primary block" data-act="reveal" data-target="a2" data-hide="a1">Next: your attempt</button>') + """</div>

<div id="a2" class="hidden" data-step="40|Step 2 of 5">
<h1>Your attempt</h1>
<p class="muted" style="margin:8px 0 20px">In one sentence, what do you think the <b>real problem</b> is? Nothing is explained yet; that is on purpose.</p>
<textarea aria-label="Your attempt" placeholder="The real problem is…"></textarea>
""" + dock('<button class="btn ghost" data-act="reveal" data-target="a3" data-hide="a2">I don’t know</button><button class="btn primary grow" data-act="reveal" data-target="a3" data-hide="a2">Reveal</button>') + """
<p class="meta" style="margin-top:8px">“I don’t know” is logged, not penalised; it feeds your reps.</p></div>

<div id="a3" class="hidden" data-step="60|Step 3 of 5">
<p class="eyebrow">Reveal</p><h1>Symptom, request, or problem?</h1>
<div class="callout" style="margin:20px 0">""" + I("pen") + """<div><span class="meta">You wrote</span><br><i>“Not enough riders.”</i></div></div>
<div class="list">
<div><span class="lead">""" + I("eye") + """</span><div class="body"><div class="title">Symptom</div><div class="sub">Late deliveries and falling ratings: what you can see.</div></div></div>
<div><span class="lead">""" + I("mail") + """</span><div class="body"><div class="title">Request</div><div class="sub">“15 more riders”: a solution someone has already chosen.</div></div></div>
<div><span class="lead">""" + I("target") + """</span><div class="body"><div class="title">Problem</div><div class="sub">The gap between what should happen and what does, with a cause you could test.</div></div></div></div>
<div class="grid2" style="gap:12px;margin-top:12px">
<div class="callout good">""" + I("ok") + """<div><b>When it helps:</b> before you spend money on a fix.</div></div>
<div class="callout attn">""" + I("flag") + """<div><b>When it misleads:</b> if you keep asking “why” until you drift into problems nobody can act on.</div></div></div>
""" + dock('<button class="btn primary block" data-act="reveal" data-target="a4" data-hide="a3">Check yourself</button>') + """</div>

<div id="a4" class="hidden" data-step="80|Step 4 of 5">
<h1>Check</h1><p class="muted" style="margin:8px 0 20px">4 quick questions. You will say how sure you are before each answer.</p>
""" + dock('<button class="btn ghost" data-act="reveal" data-target="a5" data-hide="a4">Skip</button><a class="btn primary grow" href="06-quiz.html">Start the check</a>') + """</div>

<div id="a5" class="hidden" data-step="100|Step 5 of 5">
<div class="row"><h1>Go deeper</h1><span class="chip">Ungraded</span></div>
<label class="field" style="margin-top:20px"><span class="lab">Who might disagree with your problem statement, and why?</span><textarea></textarea></label>
""" + dock('<a class="btn primary block" href="04-dashboard.html">Done. Back to Learn</a>') + """</div>
"""

# ---------------------------------------------------------------- 06 Quiz
def conf_static():
    return conf(group=True)


B["06-quiz"] = """
<p class="eyebrow">M2 Check · """ + SAMPLE + """</p>
<div data-tabs>
<div class="tabs" role="tablist" aria-label="Item types (preview only)"><button class="on" data-tab="scn" data-act="tab" role="tab">Choice</button><button data-tab="sort" data-act="tab" role="tab">Classify</button><button data-tab="rank" data-act="tab" role="tab">Rank</button><button data-tab="est" data-act="tab" role="tab">Estimate</button><button data-tab="audit" data-act="tab" role="tab">Audit the AI</button></div>

<div data-panel="scn"><div data-q="1">
<h2 style="margin-bottom:16px">Meera says: “Deliveries are late. Add 15 riders.” What is the best next step?</h2>
<div class="choices" data-group>
""" + ch("A", "Approve the riders; she knows operations.", 'data-choice data-fb="Tempting because it answers the request. It skips asking why deliveries are late. (E03 Request as problem)"') \
    + ch("B", "Ask where in the process the extra 5 minutes appear.", 'data-choice data-correct="1" data-fb="You need to know where the delay happens before choosing a fix."') \
    + ch("C", "Compare three rider-hiring vendors.", 'data-choice data-fb="Tempting because it feels rigorous. It is a solution search before a problem statement. (E01 Jumping to solution)"') + """
</div>
<h3 style="margin:24px 0 8px">How sure are you?</h3>
""" + conf_static() + """
<div class="need hidden callout attn" role="alert" style="margin-top:12px"></div>
<div class="fb hidden callout" role="status" style="margin-top:16px"><div><div class="fbh row" style="font-weight:600;gap:6px"></div><p class="fbtxt" style="margin:6px 0"></p><p class="cal meta" style="margin:0"></p></div></div>
""" + dock('<button class="btn primary block" data-act="check">Check</button><a class="btn primary block after-check hidden" href="04-dashboard.html">Next item</a>') + """
</div></div>

<div data-panel="sort" class="hidden"><h2 style="margin-bottom:16px">Fact or assumption?</h2><p class="meta">Mark each statement.</p>
<div class="list">""" + "".join('<div style="flex-wrap:wrap"><div class="body">%s</div><div class="segctl"><button type="button" data-act="pill">Fact</button><button type="button" data-act="pill">Assumption</button></div></div>' % s for s in [
    "Delivery time rose from 14 to 19 minutes.", "Riders are the bottleneck.", "Ratings fell because of late delivery."]) + """</div>
<h3 style="margin:24px 0 8px">How sure are you?</h3>""" + conf_static() + """<p class="meta" style="margin-top:12px">Preview of the item type; checking works on the Choice tab.</p></div>

<div data-panel="rank" class="hidden"><h2 style="margin-bottom:16px">Order these by what you would ask first.</h2>
<div class="list">""" + "".join('<div><span class="lead" style="font-weight:600">%d</span><div class="body">%s</div><button class="icon-btn" aria-label="Move up">%s</button><button class="icon-btn" aria-label="Move down">%s</button></div>' % (i + 1, s, I("down", "sm").replace('d="m6 9 6 6 6-6"', 'd="m18 15-6-6-6 6"'), I("down", "sm")) for i, s in enumerate([
    "Where do the 5 extra minutes come from?", "How many riders are free at peak?", "What does a 4.0 rating cost us?"])) + """</div>
<h3 style="margin:24px 0 8px">How sure are you?</h3>""" + conf_static() + """</div>

<div data-panel="est" class="hidden"><h2 style="margin-bottom:16px">How many orders does one dark store handle in a peak hour?</h2>
<div class="inputrow"><label class="field grow"><span class="lab">Low</span><input type="text" inputmode="numeric" placeholder="e.g. 150"></label><label class="field grow"><span class="lab">High</span><input type="text" inputmode="numeric" placeholder="e.g. 400"></label></div>
<label class="field"><span class="lab">Your approach</span><textarea placeholder="Riders × trips per hour…"></textarea></label>
<h3 style="margin:8px 0">How sure are you that the true value is inside your range?</h3>""" + conf_static() + """
<p class="meta" style="margin-top:12px">Scored on approach and on whether your range and confidence match, not on one number.</p></div>

<div data-panel="audit" class="hidden"><h2 style="margin-bottom:8px">An AI wrote this. Tap any sentence that is a problem.</h2>
<div class="choices" style="margin:16px 0">""" + "".join('<button type="button" class="choice" data-act="pill"><span class="key">%d</span><span class="txt">%s</span></button>' % (i + 1, s) for i, s in enumerate([
    "Delivery time rose 36% in three weeks.", "Therefore, the store needs more riders.", "Ratings correlate with delivery time, so late delivery caused the drop."])) + """</div>
<label class="field"><span class="lab">Why?</span><textarea></textarea></label>
<h3 style="margin:8px 0">How sure are you?</h3>""" + conf_static() + """</div>
</div>
"""

# ---------------------------------------------------------------- 07 Tree builder
def slot():
    return ('<button type="button" class="slot" data-act="place"><span class="lbl">Empty branch</span>'
            '<span class="flag">' + I("flag", "sm") + '<span>Check</span></span></button>')


B["07-tree-builder"] = """
<p class="eyebrow">M3 Structuring Problems · """ + SAMPLE + """</p>
<h1>Why did Whitefield’s rating fall?</h1>
<p class="muted" style="margin:8px 0 24px">Tap a piece, then tap a branch. Tap a placed piece to take it back.</p>
<div class="grid2" style="align-items:start;gap:24px">
<div>
<div class="treeroot">""" + I("target", "sm") + """ Average rating: 4.4 → 4.0 in one month</div>
<div class="tree">""" + slot() * 3 + """</div>
</div>
<div>
<h3 style="margin-bottom:8px">Pieces</h3>
<div class="tray">
<button type="button" class="piece" data-act="pick" data-id="p1">Delivery time</button>
<button type="button" class="piece" data-act="pick" data-id="p2">Item availability</button>
<button type="button" class="piece" data-act="pick" data-id="p3">Order accuracy</button>
<button type="button" class="piece" data-act="pick" data-id="p4" data-bad="Off-topic">App downloads</button>
<button type="button" class="piece" data-act="pick" data-id="p5" data-bad="Overlaps">Late orders</button></div>
<p id="treehelp" class="meta" style="margin-top:8px" aria-live="polite">Tap a piece, then tap a branch.</p>
</div></div>
<div id="treefb" class="hidden stack" style="margin-top:24px">
<h2>MECE check</h2>
<div class="list">
<div><span class="lead">""" + I("copy") + """</span><div class="body"><div class="title">Overlap</div><div class="sub">“Delivery time” and “Late orders” count the same thing.</div></div></div>
<div><span class="lead">""" + I("flag") + """</span><div class="body"><div class="title">Off-topic</div><div class="sub">“App downloads” does not explain a rating drop in one store.</div></div></div>
<div><span class="lead">""" + I("search") + """</span><div class="body"><div class="title">Gap</div><div class="sub">Nothing yet covers the customer’s experience after delivery.</div></div></div></div>
<label class="field card"><span class="lab">So what?</span><span class="help">If “Item availability” were the cause, what would you do differently from “Delivery time”?</span><textarea></textarea></label>
</div>
""" + dock('<button class="btn primary block" data-act="treecheck">Check my tree</button>')

# ---------------------------------------------------------------- 08 Inbox
B["08-inbox"] = """
<div class="split">
<section>
<div class="sec-h"><h1>Inbox</h1><span class="meta">1 new</span></div>
<div class="list">
<a href="#brief" aria-current="true" style="background:var(--surface-2)"><span class="avatar alt">MI</span><div class="body"><div class="title">Whitefield delivery times</div><div class="sub">Meera Iyer · Head of Operations<br>Due Friday · CASE-M2</div></div><span class="unread" aria-label="New"></span></a>
<div><span class="avatar alt">KS</span><div class="body"><div class="title" style="font-weight:500">Roster for next week</div><div class="sub">Karthik · Store manager · Read</div></div></div>
<div class="lock"><span class="avatar" style="background:var(--surface-2);color:var(--text-3)">""" + I("lock", "sm") + """</span><div class="body"><div class="title">Complaint summary</div><div class="sub">Divya · Support · Arrives when you start the case</div></div></div>
</div></section>

<section id="brief" class="card">
<div class="person" style="margin-bottom:16px"><span class="avatar lg alt">MI</span><div><b>Meera Iyer</b><div class="meta">Head of Operations · to you · Due Friday</div></div></div>
<h2>Whitefield delivery times</h2>
<p class="meta" style="margin:4px 0 20px">""" + SAMPLE + """ Quick commerce (U-IN-1) · India · ₹</p>
<div class="field"><span class="lab">Choose your variant</span><span class="help">Choose now. Switching later resets your hints and asks.</span>
<div class="segctl full"><button type="button" class="sel" data-act="pill" data-show="stu" data-hide="pro">Student</button><button type="button" data-act="pill" data-show="pro" data-hide="stu">""" + I("lock", "sm") + """ Professional</button></div></div>
<div id="stu" class="stack">
<p>Hi, deliveries from Whitefield are slow and customers are complaining. Ratings fell from 4.4 to 4.0 in a month. I need 15 more riders there by Friday. Can you put together the plan?</p>
<div class="callout">""" + I("target") + """<div><b>Your task:</b> write a problem statement (2–3 sentences), rank your top 3 questions, and say what you would check first.</div></div>
<div><p class="eyebrow" style="margin-bottom:6px">Exhibits provided</p><div class="chips"><span class="chip">E1 Delivery time by hour</span><span class="chip">E2 Rider roster</span><span class="chip">E3 Complaint tags</span><span class="chip">E4 Stock-outs</span></div></div>
<p class="meta" style="margin:0">""" + I("bulb", "sm") + """ Hint ladder available · 5 levels</p></div>
<div id="pro" class="stack hidden">
<p>Whitefield is slow. Get me 15 riders by Friday. Thanks.<br>— Meera</p>
<p class="meta">No exhibits shown. Ask stakeholders and request data by name. No hints in this variant.</p>
<div class="callout attn">""" + I("lock") + """<div><b>Part of Plus.</b> On the Free plan this variant is visible but locked. <a href="18-pricing.html">See Plus</a></div></div></div>
<div style="margin-top:24px"><a class="btn primary block" href="09-stakeholder.html">Start the case</a></div>
</section></div>
"""

# ---------------------------------------------------------------- 09 Stakeholder
QS = [("When did the delay start, and did anything change that week?", "Three weeks ago. That was when we opened a second lane of evening delivery slots.", "E1"),
      ("Is it slow at all hours, or only some?", "Mostly evenings, from about 7 to 9. Mornings are fine.", "E1"),
      ("How many riders are on shift in the evening, and how busy are they?", "Forty on the evening roster. I have not checked how many are actually waiting for orders.", "E2"),
      ("What do customers actually complain about?", "Divya has the tags. Late delivery, mostly, but I have heard missing items too.", "E3"),
      ("What would 15 more riders cost per month?", "About ₹4.5 lakh a month in guaranteed minimum pay, before per-order pay.", ""),
      ("Would you agree the riders are the issue?", "That is what I think. You are meant to tell me if I am wrong.", ""),
      ("Which competitor do you admire most?", "I would rather stay on Whitefield for now.", ""),
      ("What did stock-outs look like in the same weeks?", "Karthik would know. Ask him.", "E4")]
B["09-stakeholder"] = """
<div class="layout"><div>
<div class="row between" style="margin-bottom:4px"><div class="person"><span class="avatar lg alt">MI</span><div><b>Meera Iyer</b><div class="meta">Head of Operations · """ + SAMPLE + """</div></div></div>
<span class="counter" aria-label="Asks left"><span class="pips">""" + "<i></i>" * 6 + """</span><span id="asks">6</span> left</span></div>
<div id="chat" class="chat" aria-live="polite"></div>
<div id="asksdone" class="hidden callout">""" + I("info") + """<div>You have used your asks. Go to <a href="10-data-room.html">Data</a> or <a href="11-submit.html">Draft</a>.</div></div>
<div class="sec-h" style="margin-top:8px"><h3>Ask Meera</h3><span class="meta">4 at a time · refreshes after each ask</span></div>
<div class="asklist" data-menu="4">
""" + "".join('<button class="ask" data-act="ask" data-who="Meera" data-q="%s" data-a="%s"%s>%s<span class="grow">%s</span></button>' % (q, a, (' data-unlock="%s"' % u) if u else "", I("chat", "sm"), q) for q, a, u in QS) + """
</div></div>
<aside class="stack">
<div class="card pad-sm"><p class="eyebrow">Other people you can ask</p>
<div class="list" style="border:0"><a href="#" style="padding:10px 0"><span class="avatar alt">KS</span><div class="body"><div class="title">Karthik</div><div class="sub">Store manager</div></div>""" + I("right", "sm") + """</a>
<a href="#" style="padding:10px 0"><span class="avatar alt">DV</span><div class="body"><div class="title">Divya</div><div class="sub">Customer support</div></div>""" + I("right", "sm") + """</a></div></div>
<div class="callout">""" + I("info") + """<div>Answers use only case facts. Good questions can unlock exhibits in <b>Data</b>.</div></div>
</aside></div>
"""

# ---------------------------------------------------------------- 10 Data room
def exhibit(code, title, body, alias, locked=True, open_=False):
    return ('<details class="exhibit%s" id="ex-%s" data-alias="%s" data-name="%s %s"%s><summary><span class="code">%s</span>'
            '<span class="grow"><b>%s</b></span>%s<span class="chev">%s</span></summary><div class="xb">%s'
            '<button class="btn sm" style="margin-top:12px">%s Download CSV</button></div></details>') % (
        " locked" if locked else "", code, alias, code, title, " open" if open_ else "", code, title,
        ('<span class="lk meta row" style="gap:4px">%s Request</span>' % I("lock", "sm")) if locked else "", I("down", "sm"), body, I("download", "sm"))


B["10-data-room"] = """
<div class="layout"><div>
<h1 style="margin-bottom:4px">Data room</h1><p class="meta">Professional variant: you see only what you ask for.</p>
<div class="card pad-sm" style="margin:16px 0 24px">
<label class="field" style="margin:0"><span class="lab">Request data by name</span>
<div class="inputrow"><input id="reqin" type="text" placeholder="e.g. delivery time by hour"><button class="btn primary" data-act="req">Request</button></div></label>
<div id="reqout" class="meta" style="margin-top:10px" aria-live="polite">Every request is logged; asking for the right data is part of your Questioning level.</div>
<div id="exlist" class="hidden callout" style="margin-top:10px">""" + I("listcheck") + """<div><b>Not finding it?</b> Exhibits in this case: E1 Delivery time by hour · E2 Rider roster and idle time · E3 Complaint tags · E4 Stock-outs by SKU</div></div>
</div>
<div class="sec-h"><h3>Exhibits</h3><span class="meta">1 of 4 open</span></div>
<div class="stack">
""" + exhibit("E1", "Delivery time by hour", '<table class="data"><thead><tr><th>Hour</th><th class="num">Avg delivery (min)</th><th class="num">Orders</th></tr></thead><tbody>'
              '<tr><td>6–7 pm</td><td class="num">14</td><td class="num">85</td></tr><tr class="hl"><td>7–8 pm</td><td class="num">22</td><td class="num">120</td></tr>'
              '<tr class="hl"><td>8–9 pm</td><td class="num">27</td><td class="num">130</td></tr><tr><td>9–10 pm</td><td class="num">25</td><td class="num">105</td></tr>'
              '<tr><td>10–11 pm</td><td class="num">15</td><td class="num">60</td></tr></tbody></table>', "delivery|hour|time|slow", locked=False, open_=True) \
    + exhibit("E2", "Rider roster and idle time", '<p class="small" style="margin:0">40 riders rostered at 7–9 pm; average 6 minutes waiting per trip at the store.</p>', "rider|roster|shift|staff") \
    + exhibit("E3", "Complaint tags", '<p class="small" style="margin:0">Late delivery 46% · Missing item 31% · Wrong item 9% · Other 14%.</p>', "complaint|tag|support|rating") \
    + exhibit("E4", "Stock-outs by SKU", '<p class="small" style="margin:0">18% of evening orders had at least one item substituted or re-picked.</p>', "stock|out of stock|availability|inventory") + """
</div>
<p class="meta" style="margin-top:16px">""" + SAMPLE + """ Numbers are illustrative; the real exhibits reconcile in CASE-M2.</p>
</div>
<aside class="callout">""" + I("data") + """<div><b>Tip:</b> name what it measures and for which period, e.g. “rider idle time, evenings”. After 3 misses you get the list of titles. SQL box for DA cases comes in P17.</div></aside>
</div>
"""
