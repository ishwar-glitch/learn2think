"""Builds the D3 mock-ups into design/wireframes/. Run: python design/_src/build.py"""
import sys, html
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from pages_a import PAGES as A
from pages_b import PAGES as B
from decided import DECIDED
from bodies import BODIES
from ui import I

OUT = Path(__file__).resolve().parent.parent / "wireframes"
PAGES = A + B
FONT = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">'
THEME = "<script>try{var t=localStorage.getItem('l2t-theme');if(t)document.documentElement.dataset.theme=t}catch(e){}</script>"

NAV = [("home", "Home", "04-dashboard.html"), ("learn", "Learn", "05-concept.html"),
       ("cases", "Cases", "08-inbox.html"), ("career", "Career", "15-interview-lab.html"),
       ("portfolio", "Portfolio", "14-portfolio.html")]

# mode, close target (focus), progress %, count label, workspace tab
SHELL = {
    "01-landing": ("public",), "02-onboarding": ("public",), "18-pricing": ("public",),
    "03-day1": ("focus", "01-landing.html", 20, "Step 1 of 5"),
    "05-concept": ("focus", "04-dashboard.html", 20, "Step 1 of 5"),
    "06-quiz": ("focus", "05-concept.html", 50, "Item 2 of 4"),
    "07-tree-builder": ("focus", "04-dashboard.html", 60, "Build the tree"),
    "09-stakeholder": ("focus", "08-inbox.html", 40, "", "ask"),
    "10-data-room": ("focus", "08-inbox.html", 60, "", "data"),
    "11-submit": ("focus", "08-inbox.html", 80, "", "draft"),
    "12-opponent": ("focus", "11-submit.html", 50, "Challenge 1 of 2"),
}
WS = [("brief", "Brief", "doc", "08-inbox.html"), ("ask", "Ask", "chat", "09-stakeholder.html"),
      ("data", "Data", "data", "10-data-room.html"), ("draft", "Draft", "pen", "11-submit.html")]


def brand():
    return '<a class="brand" href="04-dashboard.html"><span class="mark">L2T</span>Learn2Think</a>'


def review_bar(p, i):
    prev = PAGES[i - 1] if i > 0 else None
    nxt = PAGES[i + 1] if i < len(PAGES) - 1 else None
    a = lambda q, ic, lab, cls="": ('<a href="%s.html" title="%s">%s</a>' % (q["slug"], html.escape(q["title"]), ic)) if q else '<span style="width:36px"></span>'
    return ('<div class="review" role="navigation" aria-label="Mock-up review">'
            '%s<a href="index.html">%s<span class="lbl">Index</span></a>'
            '<span class="rt">%s / 19 · <b>%s</b></span>'
            '<button data-act="theme" aria-label="Switch light or dark theme">%s%s</button>'
            '<button class="notes-btn" data-act="notes" aria-expanded="false" aria-controls="notes">%s<span class="lbl">Notes</span></button>%s</div>'
            % (a(prev, I("left"), "Prev"), I("listcheck", "sm"), p["slug"][:2], html.escape(p["title"]),
               I("moon", "sm"), '', I("panel", "sm"), a(nxt, I("right"), "Next")))


def notes(p):
    h = ('<div class="scrim" data-act="notes"></div><aside class="drawer" id="notes" aria-label="Founder notes">'
         '<div class="drawer-h"><b>Notes for this screen</b><button class="icon-btn" data-act="notes" aria-label="Close notes">%s</button></div>' % I("x"))
    h += "<h4>What it is for</h4><p>%s</p>" % p["purpose"]
    h += "<h4>Decided (D1)</h4>%s" % "".join('<div class="dec">%s<span>%s</span></div>' % (I("ok", "sm"), q) for q in DECIDED[p["slug"]])
    h += "<h4>Spec notes</h4><ul>%s</ul>" % "".join("<li>%s</li>" % n for n in p["notes"])
    h += "<h4>Built from</h4><p>%s</p></aside>" % p["source"]
    return h


def shell(p, body):
    cfg = SHELL.get(p["slug"], ("tabbed",))
    mode = cfg[0]
    if mode == "public":
        return '<div class="app public"><main class="main" id="main">%s</main></div>' % body
    if mode == "focus":
        _, close, pct, count = cfg[:4]
        ws = cfg[4] if len(cfg) > 4 else None
        top = ('<div class="focusbar"><div class="fb-top"><a class="icon-btn" href="%s" aria-label="Close and go back">%s</a>'
               '<span class="t">%s</span><span class="count" id="stepcount">%s</span></div>' % (close, I("x"), html.escape(p.get("short", p["title"])), count))
        if ws:
            top += '<nav class="wstabs" aria-label="Case workspace">%s</nav>' % "".join(
                '<a class="%s" href="%s"%s>%s%s</a>' % ("on" if k == ws else "", h, ' aria-current="page"' if k == ws else "", I(ic, "sm"), l) for k, l, ic, h in WS)
        top += '<div class="progress" aria-hidden="true"><i id="stepbar" style="width:%d%%"></i></div></div>' % pct
        return '<div class="app focus">%s<main class="main" id="main">%s</main></div>' % (top, body)
    active = p.get("nav")
    rail = '<nav class="rail" aria-label="Main">%s%s<div class="spacer"></div><a href="#">%s Profile and settings</a></nav>' % (
        brand(), "".join('<a class="%s" href="%s"%s>%s%s</a>' % ("on" if k == active else "", h, ' aria-current="page"' if k == active else "", I(k), l) for k, l, h in NAV),
        '<span class="avatar">A</span>')
    appbar = '<header class="appbar phone-only">%s<span class="t"></span><a class="icon-btn" href="#" aria-label="Profile and settings"><span class="avatar">A</span></a></header>' % brand()
    tabbar = '<nav class="tabbar" aria-label="Main">%s</nav>' % "".join(
        '<a class="%s" href="%s"%s><span class="pillbg">%s</span>%s</a>' % ("on" if k == active else "", h, ' aria-current="page"' if k == active else "", I(k), l) for k, l, h in NAV)
    return '<div class="app tabbed">%s<div class="grow">%s<main class="main" id="main">%s</main></div>%s</div>' % (rail, appbar, body, tabbar)


def page(p, i):
    return """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>%s · Learn2Think mock-up</title>%s
%s<link rel="stylesheet" href="wf.css"></head>
<body>%s%s%s
<script src="wf.js"></script></body></html>""" % (html.escape(p["title"]), THEME, FONT, review_bar(p, i), shell(p, BODIES[p["slug"]]), notes(p))


for i, p in enumerate(PAGES):
    (OUT / (p["slug"] + ".html")).write_text(page(p, i), encoding="utf-8")

# Index
cards = "".join('<a class="idx-card" href="%s.html"><span class="num">%s</span><b>%s</b><span class="meta">%s</span></a>' % (
    p["slug"], p["slug"][:2], html.escape(p["title"]), p["purpose"]) for p in PAGES)
index = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Learn2Think mock-ups (D3)</title>%s%s<link rel="stylesheet" href="wf.css"></head>
<body><div class="review"><span class="rt"><b>Learn2Think</b> · D3 mock-ups</span><button data-act="theme" aria-label="Switch light or dark theme">%s</button></div>
<div class="app public"><main class="main">
<p class="eyebrow">Batch D3 · full redesign</p>
<h1 class="display">19 screens, one calm system.</h1>
<p class="lede" style="margin-top:12px;max-width:640px">Phone-first, with a real desktop layout. Light and dark themes (the moon button switches). Every screen keeps its D1 decisions in the <b>Notes</b> drawer, top right.</p>
<div class="callout" style="margin:20px 0"><span>%s</span><div>All case text is a <b>sample</b> (a quick-commerce company, U-IN-1). The real CASE-M2 arrives in batch C2. Numbers are illustrative.</div></div>
<h2 style="margin:32px 0 12px">How to review</h2>
<ol><li>Start at 01 and use the arrows in the top strip to walk the flow to 19.</li>
<li>Try it on your phone and on your computer; resize to see the desktop layout.</li>
<li>Try the quiz (06), stakeholder chat (09), data room (10), hint ladder (11), Opponent (12) and tree builder (07).</li>
<li>Look for: anything that feels like a game, school or chatbot; any job promise; too much on one screen.</li></ol>
<h2 style="margin:32px 0 12px">Screens</h2><div class="idx-grid">%s</div>
</main></div><script src="wf.js"></script></body></html>""" % (THEME, FONT, I("moon", "sm"), I("info"), cards)
(OUT / "index.html").write_text(index, encoding="utf-8")

fb = "# D1 wireframe decisions (applied in D2, kept in D3)\n\nThe founder's answers are in `../D1_decisions.md`. Each screen shows its own decisions in the Notes drawer.\n\n"
for p in PAGES:
    fb += "## %s: %s\n" % (p["slug"][:2], p["title"]) + "".join("- %s\n" % q for q in DECIDED[p["slug"]]) + "\n"
(OUT / "FEEDBACK.md").write_text(fb, encoding="utf-8")
print(len(PAGES), "pages")
