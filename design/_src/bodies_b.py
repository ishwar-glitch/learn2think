"""D3 screen bodies 11-19."""
from ui import I, SAMPLE, meter, conf, tk, tklegend
from bodies_a import dock

B = {}

# ---------------------------------------------------------------- 11 Draft
HINTS = [("L1", "Goal", "A strong answer says what the problem is, not what to buy."),
         ("L2", "Question", "What could make evening deliveries slower without needing more riders?"),
         ("L3", "Pointer", "Look at E2. Concept: symptom vs problem (M2, concept 2)."),
         ("L4", "Worked cue", "In a restaurant case, comparing wait times by hour showed the kitchen, not the drivers, was the constraint."),
         ("L5", "Parallel example", "A short worked example on a different company.")]
B["11-submit"] = """
<div id="d1" data-step="80|">
<div class="layout"><div>
<p class="eyebrow">Deliverable · """ + SAMPLE + """</p>
<h1 style="margin-bottom:8px">Your recommendation</h1>
<p class="muted">Structured, not a blank page. Each kind of thinking has its own look:</p>
""" + tklegend() + """
<h3 class="row" style="margin:28px 0 12px"><span class="chip solid">1</span> Frame</h3>
<label class="field"><span class="lab">Problem statement</span><span class="help">2–3 sentences. Name a gap, not a solution.</span><textarea placeholder="The real problem is…"></textarea></label>
<h3 class="row" style="margin:28px 0 12px"><span class="chip solid">2</span> Reason</h3>
<div class="stack">
""" + tk("evd", '<textarea aria-label="What I know" placeholder="What I know, from the exhibits…"></textarea>', "Evidence · what I know") \
    + tk("asm", '<textarea aria-label="What I am assuming" placeholder="What must be true for this to hold…"></textarea>', "Assumptions · what I am assuming") \
    + tk("alt", '<textarea aria-label="Options I considered" placeholder="Options other than more riders…"></textarea>', "Alternatives · options I considered") \
    + tk("trd", '<textarea aria-label="Trade-offs" placeholder="What each option costs or risks…"></textarea>', "Trade-offs · what each costs") + """
</div>
<h3 class="row" style="margin:28px 0 12px"><span class="chip solid">3</span> Decide</h3>
<label class="field"><span class="lab">My recommendation, and what I would check first</span><textarea></textarea></label>
<div class="field"><span class="lab">How sure are you?</span>""" + conf() + """</div>
<label class="field"><span class="lab">What would change my mind?</span><textarea></textarea></label>
</div>
<aside class="card pad-sm">
<div class="row between"><h3 class="row" style="gap:6px">""" + I("bulb") + """ Need a hint?</h3></div>
<p id="hintcount" class="meta" style="margin:4px 0 12px">One per tap. Logged, never penalised.</p>
<ol class="ladder">""" + "".join('<li class="hidden"><span class="lv">%s</span><div><div class="lk">%s</div><div class="small">%s</div></div></li>' % h for h in HINTS) + """</ol>
<button class="btn block sm" data-act="hint">""" + I("plus", "sm") + """<span> Show hint L1</span></button>
<p class="meta" style="margin:8px 0 0">Hints never give the answer or write your structure.</p>
</aside></div>
""" + dock('<button class="btn primary block" data-act="reveal" data-target="d2" data-hide="d1">Submit</button>') + """</div>

<div id="d2" class="hidden" data-step="90|">
<p class="eyebrow">Self-review</p><h1>Check your own work</h1>
<p class="muted" style="margin:8px 0 20px">Before you see the model answer, tick what is true of yours.</p>
<div class="checks" data-ticks>
""" + "".join('<label class="check"><input type="checkbox"> %s</label>' % s for s in [
    "My problem statement names a gap, not a solution.", "I used at least two exhibits as evidence.",
    "I listed assumptions and marked the riskiest.", "I considered an option other than more riders.",
    "I said what would change my mind.", "I put my answer first."]) + """
<div class="checkfoot"><span class="tickcount">0 of 6 ticked</span></div></div>
""" + dock('<button class="btn primary block" data-act="reveal" data-target="d3" data-hide="d2">Show the model answer</button>') + """</div>

<div id="d3" class="hidden" data-step="100|">
<p class="eyebrow">Results · CASE-M2</p><h1>Model answer</h1>
<div class="layout" style="margin-top:20px"><div class="stack">
""" + tk("evd", '<p class="small" style="margin:0">The delay is concentrated in the 7–9 pm slots. Riders wait about 6 minutes per trip at the store, and 18% of evening orders are re-picked. That points to picking and stock, not rider numbers.</p>', "Reasoning path") + """
""" + tk("alt", '<p class="small" style="margin:0">A test of extra riders for one week at peak, if you name what result would prove the constraint is riders.</p>', "Also acceptable") + """
<div class="card pad-sm"><p class="eyebrow">Common mistakes</p><div class="chips"><span class="chip">E03 Request treated as the problem</span><span class="chip">E07 Assumed late delivery caused the rating drop</span><span class="chip">E05 No baseline</span></div></div>
<div class="card pad-sm"><p class="eyebrow">Your most useful questions</p>
<div class="list" style="border:0">
<div style="padding:10px 0">""" + I("ok") + """<div class="body"><div class="sub">Most useful</div>“When did the delay start, and did anything change that week?” <span class="meta">→ E1</span><br>“How many riders are on shift, and how busy are they?” <span class="meta">→ E2</span></div></div>
<div style="padding:10px 0">""" + I("info") + """<div class="body"><div class="sub">Not needed</div>“Which competitor do you admire most?”</div></div>
<div style="padding:10px 0">""" + I("flag") + """<div class="body"><div class="sub">Leading</div>“Would you agree the riders are the issue?”</div></div></div>
<p class="meta" style="margin:0">Shown after the case, never during it.</p></div>
</div>
<aside class="stack">
<div class="card pad-sm"><p class="eyebrow">Your levels</p><div class="levels">
""" + meter("Problem framing", 2) + meter("Questioning", 3) + meter("Assumptions", 1) + meter("Reflection", 2) + """
</div><p class="meta" style="margin:12px 0 0">From your checklist and the platform’s checks. Hints used: up to L2. No single score.</p></div>
<div class="card flat pad-sm"><div class="row between"><h3>Founder review</h3><span class="chip">Capstones · ₹999</span></div>
<p class="meta" style="margin:6px 0 12px">A written review against the rubric. Offered after a capstone submission, and from the portfolio item.</p><button class="btn sm">Request founder review</button></div>
</aside></div>
""" + dock('<a class="btn primary block" href="12-opponent.html">Face the Opponent</a>') + """</div>
"""

# ---------------------------------------------------------------- 12 Opponent
B["12-opponent"] = """
<div class="row between" style="margin-bottom:12px"><p class="eyebrow" style="margin:0">Challenge 1 of 2 · """ + SAMPLE + """</p>
<button class="btn ghost sm" data-act="reveal" data-target="stop">""" + I("pause", "sm") + """ Stop for now</button></div>
<div id="stop" class="hidden callout" style="margin-bottom:12px">""" + I("info") + """<div><b>Saved.</b> Pick this up from Home when you are ready. Challenges can’t be skipped.</div></div>
<div class="card" style="margin-bottom:24px">
<div class="person" style="margin-bottom:16px"><span class="avatar lg">SM</span><div><b>Skeptical Manager</b><div class="meta">Meera · scripted persona</div></div></div>
<p style="font-size:19px;line-height:1.5;margin:0;letter-spacing:-.01em">“You say the cause is picking, not riders. Why should I believe that, when I can see riders standing around and orders still late?”</p></div>
<label class="field"><span class="lab">Your reply</span><textarea placeholder="Reply in your own words…"></textarea></label>
<button class="btn primary block" data-act="reveal" data-target="o2" data-self="hide">Submit reply</button>

<div id="o2" class="hidden" style="margin-top:8px">
<h3 style="margin-bottom:4px">Check your reply</h3><p class="meta">Tick what your reply did.</p>
<div class="checks" data-ticks data-decided="1">
<label class="check"><input type="checkbox"> I cited the rider waiting time (E2).</label>
<label class="check"><input type="checkbox"> I explained why idle riders do not mean more riders are needed.</label>
<label class="check"><input type="checkbox"> I said how we could test my view cheaply.</label>
<div class="checkfoot"><span class="tickcount">0 of 3 ticked</span><span class="tickverdict"></span></div></div>
<div id="con" class="hidden callout good" style="margin-top:12px">""" + I("ok") + """<div><b>Conceded.</b> “Six minutes waiting at the store is a fair point. Show me the test.”</div></div>
<div id="esc" class="callout attn" style="margin-top:12px">""" + I("flag") + """<div><b>Sharper.</b> “Idle riders are exactly what I see. Convince me it is not the riders.”</div></div>
<h3 style="margin:28px 0 12px">Revise</h3>
<label class="field"><span class="lab">Your revised recommendation</span><textarea></textarea></label>
<label class="field"><span class="lab">What changed, and why?</span><span class="help">Required. One or two sentences. Revising moves your skill map most.</span><textarea></textarea></label>
<button class="btn primary block" data-act="reveal" data-target="o3" data-hide="o2">Next challenge</button></div>

<div id="o3" class="hidden" data-step="100|Challenge 2 of 2" style="margin-top:24px">
<div class="card"><div class="person" style="margin-bottom:16px"><span class="avatar lg">CF</span><div><b>CFO · Anil Shetty</b><div class="meta">Scripted persona</div></div></div>
<p style="font-size:19px;line-height:1.5;margin:0">“Fifteen riders cost ₹4.5 lakh a month. What does your fix cost, and when do I see the return?”</p></div>
<a class="btn primary block" style="margin-top:16px" href="13-thinking-record.html">Continue to the result (mock-up shortcut)</a></div>
"""

# ---------------------------------------------------------------- 13 Thinking Record
def rf(n, k, v, tag=""):
    return '<div class="rf"><span class="n">%s</span><div><div class="k">%s%s</div><div class="v">%s</div></div></div>' % (n, k, tag, v)


def rfl(n, k, stage):
    return '<div class="rf locked"><span class="n">%s</span><div><div class="k">%s</div><div class="v">%s Unlocks at %s</div></div></div>' % (n, k, I("lock", "sm"), stage)


B["13-thinking-record"] = """
<div class="layout"><div>
<article class="record">
<header class="record-h"><p class="eyebrow">Thinking Record · CASE-M2 · """ + SAMPLE + """</p><h1>The Slow Dark Store</h1>
<div class="chips" style="margin-top:12px"><span class="chip">Professional</span><span class="chip">""" + I("lock", "sm") + """ Private</span><span class="chip">""" + I("history", "sm") + """ Version 1</span></div></header>
""" + rf(1, "Problem", "Evening deliveries in Whitefield are slower, ratings fell.", ' <span class="chip">pre-filled</span>') \
    + rf(2, "First take", "“Not enough riders” (from the manager’s request).") \
    + rf(3, "Assumptions", '<div class="tk asm" style="padding:10px 12px"><div class="tk-h">' + I("help", "sm") + 'Assumption</div>Delay is concentrated at 7–9 pm; picking, not riding, is the constraint.</div>') \
    + rf(4, "Questions asked", "When did it start · Is it all hours · Rider roster · Complaint tags", ' <span class="chip">from your asks</span>') \
    + rfl("5–6", "Hypotheses · Evidence", "Stage 2, Investigate") \
    + rfl("7–10", "Alternatives · Trade-offs · Decision · Confidence", "Stage 3, Decide") \
    + rfl(11, "What would change my mind", "Stage 4, Deliver") + """
<div class="rf"><span class="n">12</span><div><div class="k">Reflection</div><textarea aria-label="Reflection" placeholder="What did I miss at first, and what will I do differently?"></textarea></div></div>
</article>
<div class="stack" style="margin-top:16px">
<button class="btn primary block" data-act="reveal" data-target="sv" data-self="hide">Save to my portfolio (private)</button>
<div id="sv" class="hidden callout good">""" + I("ok") + """<div><b>Saved as version 1.</b> Editing later creates version 2; version 1 is kept. <button class="link">Edit</button></div></div>
<a class="btn block" href="16-story-bank.html">Make an interview story from this</a></div>
</div>
<aside class="card pad-sm"><p class="eyebrow">Fields grow with your stage</p>
<ol class="stagerail" style="margin-top:12px">
<li class="cur"><span class="d"></span><div><b>Understand</b><div class="meta">Fields 1–4 and 12 · you are here</div></div></li>
<li><span class="d"></span><div><b>Investigate</b><div class="meta">Adds 5–6</div></div></li>
<li><span class="d"></span><div><b>Decide</b><div class="meta">Adds 7–10</div></div></li>
<li><span class="d"></span><div><b>Deliver</b><div class="meta">All 12</div></div></li></ol>
<p class="meta" style="margin:0">The platform pre-fills what it can from your submission. Reflection is written before the model answer.</p></aside>
</div>
"""

# ---------------------------------------------------------------- 14 Portfolio
B["14-portfolio"] = """
<h1>Your portfolio</h1><p class="meta" style="margin:4px 0 20px">Private by default. Facts about your work, never a verdict.</p>
<div data-tabs>
<div class="tabs" role="tablist"><button class="on" data-tab="cases" data-act="tab" role="tab">Cases</button><button data-tab="evd" data-act="tab" role="tab">Evidence</button><button data-tab="pub" data-act="tab" role="tab">Public page</button></div>
<div data-panel="cases" class="stack">
<div class="card">
<div class="row between"><div><h3>The Slow Dark Store</h3><div class="meta">CASE-M2 · Professional · """ + SAMPLE + """</div></div><span class="chip">""" + I("lock", "sm") + """ Private</span></div>
<div class="levels" style="margin:16px 0">""" + meter("Problem framing", 2) + meter("Questioning", 3) + """</div>
<p class="meta">Scored by: your self-review + platform checks.</p>
<div class="row"><a class="btn sm" href="13-thinking-record.html">""" + I("doc", "sm") + """ Open record</a><button class="btn sm" data-act="reveal" data-target="conf" data-self="hide">""" + I("globe", "sm") + """ Make public</button></div>
<div id="conf" class="hidden callout attn" style="margin-top:12px">""" + I("eye") + """<div>This makes the case, its record and the levels you pick visible to anyone with the link. You can turn it off any time.<br><button class="btn sm dark" style="margin-top:8px" data-act="reveal" data-target="pubok" data-hide="conf">Yes, make public</button></div></div>
<div id="pubok" class="hidden callout good" style="margin-top:12px">""" + I("ok") + """<div><b>Public.</b> Link: [domain]/p/aarav/case-m2</div></div></div>
<div class="list">
<a href="#"><span class="lead">""" + I("doc") + """</span><div class="body"><div class="title">Where the Margin Went</div><div class="sub">CASE-M1 · Student · Private</div></div>""" + I("right", "sm") + """</a>
<div><span class="lead">""" + I("flag") + """</span><div class="body"><div class="title">Quick-commerce subscription tier</div><div class="sub">CAP-PM · Capstone · Submitted</div></div><a class="btn sm" href="11-submit.html">Review · ₹999</a></div>
<div class="lock"><span class="lead">""" + I("lock") + """</span><div class="body"><div class="title">The Broken Business</div><div class="sub">IC1</div></div><span class="chip plus">Plus</span></div></div>
</div>
<div data-panel="evd" class="hidden stack">
<p class="meta">What you have shown so far for <b>Product Manager</b>. Facts only; no percentage.</p>
<div class="list">""" + "".join('<div><div class="body">%s</div><b>%s</b></div>' % r for r in [
    ("Cases scored", "2 of 12 launched"), ("Capstone", "Not started"), ("Stories in Story Bank", "1"), ("Interview rounds", "0 of 3"), ("Lab artifacts", "0 of 4")]) + """</div>
<div class="card flat pad-sm"><h3>Gaps from a job description you pasted</h3><p class="meta" style="margin:6px 0 12px">Metrics read-out · Roadmap</p><a class="btn sm" href="17-jd-decoder.html">Open JD Decoder</a></div></div>
<div data-panel="pub" class="hidden stack">
<p class="meta">What visitors would see. Only items you switch to Public appear.</p>
<div class="mock"><div class="mbar"><i></i><i></i><i></i></div><div style="padding:20px" class="stack">
<div class="person"><span class="avatar lg">A</span><div><b>aarav</b> <span class="chip">handle</span><div class="meta">Working towards Product Management · Real name is optional: <a href="#">add</a></div></div></div>
<div class="card pad-sm"><h3>The Slow Dark Store</h3><p class="meta" style="margin:4px 0 8px">Scored by self-review and platform checks.</p>
<p class="eyebrow" style="margin-top:12px">Levels shown on your public page</p>
<div class="checks"><label class="check"><input type="checkbox" checked> Problem framing · Developing</label><label class="check"><input type="checkbox" checked> Questioning · Solid</label><label class="check"><input type="checkbox"> Assumptions · Starting</label></div></div></div></div>
<button class="btn block">""" + I("copy", "sm") + """ Copy link</button></div>
</div>
"""

# ---------------------------------------------------------------- 15 Interview Lab
B["15-interview-lab"] = """
<div class="row between" style="margin-bottom:20px"><h1>Interview Lab</h1>
<div class="segctl" aria-label="Mock-up preview"><button type="button" class="sel" data-act="pill" data-show="fv" data-hide="pv">Free view</button><button type="button" data-act="pill" data-show="pv" data-hide="fv">Plus view</button></div></div>
<div id="fv" class="hero"><p class="eyebrow">""" + I("lock", "sm") + """ Part of Plus</p><h2>Practise interviews with your own cases</h2>
<p class="muted" style="margin:8px 0 16px">Three graded mock rounds per role, timed questions, follow-ups and a Mock Loop. The tab stays visible so you can see what is here.</p>
<a class="btn primary" href="18-pricing.html">See Plus</a></div>
<div id="pv" class="hidden">
<div class="tabs"><a href="#" class="on">Product Manager</a><a href="#">Behavioural (all roles)</a></div>
<div class="list">
<div><span class="lead">1</span><div class="body"><div class="title">Product sense</div><div class="sub">5 questions · about 20 minutes</div></div><button class="btn sm" data-act="reveal" data-target="run" data-self="hide">Start</button></div>
<div class="lock"><span class="lead">2</span><div class="body"><div class="title">Execution and metrics</div><div class="sub">Unlocks after Round 1</div></div>""" + I("lock", "sm") + """</div>
<div class="lock"><span class="lead">3</span><div class="body"><div class="title">Prioritisation</div><div class="sub">Unlocks after Round 2</div></div>""" + I("lock", "sm") + """</div></div>
<div id="run" class="hidden" style="margin-top:24px">
<div class="card"><div class="row between"><p class="eyebrow" style="margin:0">Question 2 of 5 · """ + SAMPLE + """</p><span class="counter">""" + I("clock", "sm") + """ 02:30</span></div>
<p style="font-size:19px;line-height:1.45;margin:12px 0 4px;font-weight:600">“A grocery app’s repeat orders are flat. Where would you start?”</p><p class="meta" style="margin:0">Suggested time: 2–3 minutes</p></div>
<label class="field" style="margin-top:16px"><span class="lab">Your answer</span><textarea style="min-height:140px" placeholder="Type your answer…"></textarea></label>
<div class="row between"><button class="btn sm">""" + I("mic", "sm") + """ Record instead</button><span class="meta">""" + I("shield", "sm") + """ Recordings stay on this device.</span></div>
<button class="btn block" style="margin-top:16px" data-act="reveal" data-target="r2" data-self="hide">I have answered</button>
<div id="r2" class="hidden stack" style="margin-top:16px">
<div class="callout">""" + I("chat") + """<div><b>Follow-up:</b> “You said ‘improve the app.’ Which single metric would you look at first, and why?”</div></div>
<h3>A strong answer includes</h3>
<div class="checks" data-ticks>""" + "".join('<label class="check"><input type="checkbox"> %s</label>' % s for s in [
    "A clear first question about the customer or the metric", "A segment or cohort, not “all users”", "A hypothesis I could test", "A recommendation, not only questions"]) + """</div>
<h3>Rate yourself</h3>
<div class="list">""" + "".join('<div style="flex-wrap:wrap"><div class="body">%s</div><div class="segctl">%s</div></div>' % (d, "".join('<button type="button" data-act="pill">%d</button>' % n for n in range(1, 5))) for d in ["Structure", "Clarity", "Composure", "Concision"]) + """</div>
<details class="exhibit"><summary><span class="code">""" + I("doc", "sm") + """</span><span class="grow"><b>Model answer</b></span><span class="chev">""" + I("down", "sm") + """</span></summary><div class="xb"><p class="small" style="margin:0">A short worked answer, with the reasoning shown.</p></div></details>
<button class="btn primary block">Next question</button></div></div>
</div>
"""

# ---------------------------------------------------------------- 16 Story Bank
B["16-story-bank"] = """
<h1>Story Bank</h1><p class="meta" style="margin:4px 0 20px">Built from your own Thinking Records. 1 story · 2 competencies · Free includes one story.</p>
<div class="card pad-sm" style="margin-bottom:20px"><div class="row between"><div><h3>The Slow Dark Store</h3><div class="meta">From CASE-M2 · """ + SAMPLE + """</div></div>""" + I("doc") + """</div>
<div class="chips" style="margin-top:10px"><span class="chip tea">Problem framing</span><span class="chip tea">Questioning</span></div></div>
<div data-tabs>
<div class="tabs" role="tablist"><button class="on" data-tab="star" data-act="tab" role="tab">STAR</button><button data-tab="two" data-act="tab" role="tab">2-minute</button><button data-tab="one" data-act="tab" role="tab">One-pager</button><button data-tab="res" data-act="tab" role="tab">Résumé bullets</button></div>
<div data-panel="star"><div class="record">
""" + rf("S", "Situation", "Evening deliveries were slower and ratings fell from 4.4 to 4.0.") + rf("T", "Task", "My manager asked for 15 more riders. I was asked for a plan.") \
    + rf("A", "Action", "I asked when the delay started, requested the rider roster and complaint tags, and compared hours.") + """
<div class="rf"><span class="n">R</span><div><div class="k">Result</div><textarea aria-label="Result" placeholder="Add your outcome, in your words."></textarea></div></div></div></div>
<div data-panel="two" class="hidden"><div class="card"><p class="eyebrow">Read aloud, then edit</p><p style="font-size:17px;line-height:1.6;margin:0">“Deliveries from one store had slowed in the evenings and ratings dropped. My manager’s first idea was more riders. Before agreeing, I asked when it started and looked at delivery time by hour…”</p></div></div>
<div data-panel="one" class="hidden"><div class="mock"><div class="mbar"><i></i><i></i><i></i></div><div style="padding:20px"><h3>The Slow Dark Store · one-page summary</h3><p class="meta">Problem · What I did · What I learned</p><div style="height:8px;background:var(--sunken);border-radius:4px;margin:10px 0"></div><div style="height:8px;background:var(--sunken);border-radius:4px;margin:10px 0;width:80%"></div><div style="height:8px;background:var(--sunken);border-radius:4px;margin:10px 0;width:60%"></div></div></div></div>
<div data-panel="res" class="hidden"><ul class="ticks card">
<li>""" + I("check", "sm") + """Analysed delivery time by hour and rider idle time to locate the delay in picking, not rider numbers.</li>
<li>""" + I("check", "sm") + """Asked stakeholders four targeted questions and requested two data exhibits before recommending.</li></ul>
<p class="meta" style="margin-top:8px">Template-based, built only from facts you confirm below. Edit before you use them.</p></div></div>
<div class="checks" style="margin:20px 0 16px"><label class="check"><input type="checkbox"> I confirm these facts are true of my work.</label></div>
<a class="btn primary block" href="15-interview-lab.html">Practise this story in Interview Lab</a>
"""

# ---------------------------------------------------------------- 17 JD Decoder
B["17-jd-decoder"] = """
<h1>JD Decoder</h1><p class="meta" style="margin:4px 0 20px">""" + I("shield", "sm") + """ Runs in your browser. Nothing is kept unless you tap Save.</p>
<label class="field"><span class="lab">Paste a job description</span><textarea style="min-height:160px" placeholder="Paste text here"></textarea></label>
<button class="btn primary block" data-act="reveal" data-target="jr" data-self="hide">Decode</button>
<div id="jr" class="hidden stack-lg" style="margin-top:8px">
<section><div class="sec-h"><h2>Skills you have shown</h2><span class="meta">2</span></div>
<div class="card pad-sm"><div class="chips"><span class="chip solid">""" + I("check", "sm") + """ Problem framing</span><span class="chip solid">""" + I("check", "sm") + """ Stakeholder questions</span></div><p class="meta" style="margin:10px 0 0">From CASE-M2 and CASE-M1.</p></div></section>
<section><div class="sec-h"><h2>Gaps</h2><span class="meta">2</span></div>
<div class="list">
<a href="#"><span class="lead">""" + I("target") + """</span><div class="body"><div class="title">Metrics and dashboards</div><div class="sub">Asked for in the JD · Try M6 Numbers and Metrics, LAB-PM metrics read-out</div></div>""" + I("right", "sm") + """</a>
<a href="#"><span class="lead">""" + I("target") + """</span><div class="body"><div class="title">Prioritisation frameworks</div><div class="sub">Try M3 · CASE-M3</div></div>""" + I("right", "sm") + """</a></div></section>
<section><div class="sec-h"><h2>Not covered here</h2></div>
<div class="callout">""" + I("info") + """<div>“SQL (advanced)”, “Jira”, “Stakeholder workshops in person”. Learn2Think does not teach these.</div></div></section>
<div><button class="btn block">Save this role</button><p class="meta" style="margin-top:8px">No match percentage: it would read like a readiness score.</p></div>
</div>
"""

# ---------------------------------------------------------------- 18 Pricing
def ticks(items):
    return '<ul class="ticks">%s</ul>' % "".join("<li>%s%s</li>" % (I("check", "sm"), x) for x in items)


B["18-pricing"] = """
<header class="topnav"><a class="brand" href="04-dashboard.html"><span class="mark">L2T</span>Learn2Think</a><a class="btn ghost sm" href="04-dashboard.html">Back</a></header>
<div style="text-align:center;max-width:620px;margin:24px auto 24px">
<h1 class="display">Plans</h1>
<p class="lede" style="margin:12px 0 20px">Start free. Upgrade when you want the full path and the career tools. Prices include taxes.</p>
<div class="segctl"><button type="button" class="sel" data-act="pill" data-show="ann" data-hide="mon">Annual</button><button type="button" data-act="pill" data-show="mon" data-hide="ann">Monthly</button></div></div>
<div class="plans" style="max-width:860px;margin:0 auto">
<div class="plan"><div><h2>Free</h2><p class="meta" style="margin:4px 0 0">For getting started</p></div><div class="price">₹0</div>
""" + ticks(["Day-1 case", "Stage 1: M1, M2 and their cases", "3 Daily Reps a week", "Private portfolio", "Personal Problem worksheets, unlimited", "One Story Bank story"]) + """
<button class="btn block">Continue free</button></div>
<div class="plan best"><div class="row between"><h2>Plus</h2><span class="chip tea">Best value annually</span></div>
<div><div id="ann" class="price">₹2,499<small> / year</small><div class="meta" style="font-size:14px;margin-top:6px;font-weight:400">About ₹208 a month</div></div><div id="mon" class="price hidden">₹399<small> / month</small></div></div>
""" + ticks(["Everything in Free", "M3–M10 and IC1–IC3", "All four tracks and capstones", "Professional variants", "Interview Lab, Story Bank, Translator, JD Decoder", "Public portfolio and Tool Fluency Labs", "Challenge step in Personal Problem"]) + """
<button class="btn primary block">Get Plus</button>
<p class="meta" style="margin:0;text-align:center">7-day refund on your first purchase · renewal date and cancel always visible</p></div>
</div>
<div class="plans" style="max-width:860px;margin:16px auto 0">
<div class="card pad-sm"><h3>Founding member · ₹1,499 first year</h3><p class="meta" style="margin:4px 0 12px">First 500 waitlist members, by the code we emailed you. Renews at the annual price.</p>
<div class="inputrow"><input type="text" aria-label="Founding code" placeholder="Founding code"><button class="btn sm">Apply</button></div></div>
<div class="card pad-sm"><h3>Capstone expert review · ₹999</h3><p class="meta" style="margin:4px 0 0">A written review by the founder against the rubric. Limited to 5 a week.</p></div></div>
<section class="sec" style="max-width:520px;margin:48px auto 0">
<p class="eyebrow" style="justify-content:center">Paywall preview · when opening M3</p>
<div class="mock"><div class="mbar"><i></i><i></i><i></i></div><div style="padding:24px" class="stack">
<span class="avatar lg" style="background:var(--hero)">""" + I("lock") + """</span>
<h2>M3 Structuring Problems is part of Plus</h2>
<p class="muted small" style="margin:0">You keep Stage 1, your portfolio and your Daily Reps. Plus adds Stages 2–4, all four tracks and career tools.</p>
<button class="btn primary block">See Plus</button><button class="btn ghost block">Not now</button></div></div></section>
"""

# ---------------------------------------------------------------- 19 Personal Problem
def ws(n, title, inner, extra="", open_=False):
    return '<details class="ws"%s><summary><span class="n">%s</span><span>%s</span>%s<span class="chev">%s</span></summary><div class="wb">%s</div></details>' % (
        " open" if open_ else "", n, title, extra, I("down", "sm"), inner)


B["19-personal-problem"] = """
<p class="eyebrow">Learn · Personal Problem</p>
<h1>Bring a real decision</h1>
<p class="muted" style="margin:8px 0 16px">You do the thinking; the worksheet asks the questions. Your text stays private.</p>
<div class="callout attn" style="margin-bottom:20px">""" + I("shield") + """<div><b>Don’t include confidential company or personal data.</b></div></div>
""" + ws(1, "The real situation", '<label class="field" style="margin:0"><span class="help">What is happening, in two or three sentences?</span><textarea></textarea></label>', open_=True) \
    + ws(2, "The decision or question", '<label class="field" style="margin:0"><span class="help">What exactly do you need to decide, by when?</span><textarea></textarea></label>') \
    + ws(3, "Known, unknown, assumed", tk("evd", "<textarea aria-label='Known'></textarea>", "Known") + '<label class="field" style="margin:0"><span class="lab">Unknown</span><textarea></textarea></label>' + tk("asm", "<textarea aria-label='Assumed'></textarea>", "Assumed")) \
    + ws(4, "Alternatives and consequences", tk("alt", "<textarea aria-label='Options' placeholder='At least two options…'></textarea>", "Options") + tk("trd", "<textarea aria-label='Costs and risks'></textarea>", "What each costs or risks")) \
    + ws(5, "Your decision", '<textarea aria-label="Your decision"></textarea><span class="lab" style="font-weight:600">How sure are you?</span>' + conf()) \
    + ws(6, "Challenge your reasoning", '<p class="small" style="margin:0">Skeptical Manager: “What would make you change your mind?” Then tick what your reply covered.</p><textarea></textarea>', ' <span class="chip plus">Plus</span>') \
    + ws(7, "Next action", '<label class="field" style="margin:0"><span class="help">One thing you will do this week, and a date to revisit.</span><textarea></textarea></label>') + """
<a class="btn primary block" style="margin-top:24px" href="13-thinking-record.html">Save as a Thinking Record</a>
"""
