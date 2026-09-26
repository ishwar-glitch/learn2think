"""Shared UI helpers for the D3 mock-ups: Lucide line icons and signature components."""
import math

P = {
    "home": '<path d="M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8"/><path d="M3 10a2 2 0 0 1 .709-1.528l7-5.999a2 2 0 0 1 2.582 0l7 5.999A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>',
    "learn": '<path d="M12 7v14"/><path d="M3 18a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h5a4 4 0 0 1 4 4 4 4 0 0 1 4-4h5a1 1 0 0 1 1 1v13a1 1 0 0 1-1 1h-6a3 3 0 0 0-3 3 3 3 0 0 0-3-3z"/>',
    "cases": '<path d="M16 20V4a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/><rect width="20" height="14" x="2" y="6" rx="2"/>',
    "career": '<circle cx="12" cy="12" r="10"/><path d="m16.24 7.76-2.12 6.36-6.36 2.12 2.12-6.36 6.36-2.12z"/>',
    "portfolio": '<path d="M20 20a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.9a2 2 0 0 1-1.69-.9L9.6 3.9A2 2 0 0 0 7.93 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2Z"/>',
    "x": '<path d="M18 6 6 18"/><path d="m6 6 12 12"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "right": '<path d="m9 18 6-6-6-6"/>',
    "left": '<path d="m15 18-6-6 6-6"/>',
    "down": '<path d="m6 9 6 6 6-6"/>',
    "lock": '<rect width="18" height="11" x="3" y="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    "info": '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/>',
    "shield": '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/>',
    "bulb": '<path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6"/><path d="M10 22h4"/>',
    "chat": '<path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/>',
    "data": '<ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5V19A9 3 0 0 0 21 19V5"/><path d="M3 12A9 3 0 0 0 21 12"/>',
    "doc": '<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M10 9H8"/><path d="M16 13H8"/><path d="M16 17H8"/>',
    "download": '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" x2="12" y1="15" y2="3"/>',
    "clock": '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
    "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2"/><path d="M12 20v2"/><path d="m4.93 4.93 1.41 1.41"/><path d="m17.66 17.66 1.41 1.41"/><path d="M2 12h2"/><path d="M20 12h2"/><path d="m6.34 17.66-1.41 1.41"/><path d="m19.07 4.93-1.41 1.41"/>',
    "moon": '<path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/>',
    "panel": '<rect width="18" height="18" x="3" y="3" rx="2"/><path d="M15 3v18"/>',
    "arrow": '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>',
    "help": '<circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/>',
    "branch": '<line x1="6" x2="6" y1="3" y2="15"/><circle cx="18" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M18 9a9 9 0 0 1-9 9"/>',
    "scale": '<path d="m16 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/><path d="m2 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/><path d="M7 21h10"/><path d="M12 3v18"/><path d="M3 7h2c2 0 5-1 7-2 2 1 5 2 7 2h2"/>',
    "evidence": '<rect width="8" height="4" x="8" y="2" rx="1" ry="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><path d="m9 14 2 2 4-4"/>',
    "mic": '<path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" x2="12" y1="19" y2="22"/>',
    "send": '<path d="m22 2-7 20-4-9-9-4Z"/><path d="M22 2 11 13"/>',
    "target": '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
    "search": '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
    "pen": '<path d="M12 20h9"/><path d="M16.5 3.5a2.12 2.12 0 0 1 3 3L7 19l-4 1 1-4Z"/>',
    "flag": '<path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"/><line x1="4" x2="4" y1="22" y2="15"/>',
    "listcheck": '<path d="m3 17 2 2 4-4"/><path d="m3 7 2 2 4-4"/><path d="M13 6h8"/><path d="M13 12h8"/><path d="M13 18h8"/>',
    "user": '<path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
    "eye": '<path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7Z"/><circle cx="12" cy="12" r="3"/>',
    "globe": '<circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/>',
    "copy": '<rect width="14" height="14" x="8" y="8" rx="2" ry="2"/><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c2.1 0 2 .9 2 2"/>',
    "history": '<path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/>',
    "pause": '<rect x="14" y="4" width="4" height="16" rx="1"/><rect x="6" y="4" width="4" height="16" rx="1"/>',
    "ok": '<circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/>',
    "no": '<circle cx="12" cy="12" r="10"/><path d="m15 9-6 6"/><path d="m9 9 6 6"/>',
    "plus": '<path d="M5 12h14"/><path d="M12 5v14"/>',
    "mail": '<rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>',
    "repeat": '<path d="m17 2 4 4-4 4"/><path d="M3 11v-1a4 4 0 0 1 4-4h14"/><path d="m7 22-4-4 4-4"/><path d="M21 13v1a4 4 0 0 1-4 4H3"/>',
}


def I(name, cls=""):
    return '<svg class="i %s" viewBox="0 0 24 24" aria-hidden="true">%s</svg>' % (cls, P[name])


SAMPLE = '<span class="sample">Sample</span>'
LOOP = ["Ask", "Frame", "Structure", "Research", "Analyze", "Decide", "Communicate", "Reflect"]
LEVELS = ["Starting", "Developing", "Solid", "Strong"]


def radar(levels, labels=LOOP, legend=True):
    """Skill map: rubric level (1-4) per Thinking Loop stage. 0 = not yet shown."""
    cx, cy, r = 160, 150, 100
    n = len(labels)
    pt = lambda i, v: (cx + r * v / 4 * math.sin(2 * math.pi * i / n), cy - r * v / 4 * math.cos(2 * math.pi * i / n))
    s = ""
    for lv in (1, 2, 3, 4):
        s += '<polygon class="ring%s" points="%s"/>' % (" outer" if lv == 4 else "", " ".join("%.1f,%.1f" % pt(i, lv) for i in range(n)))
    for i in range(n):
        x, y = pt(i, 4)
        s += '<line class="axis" x1="%d" y1="%d" x2="%.1f" y2="%.1f"/>' % (cx, cy, x, y)
    for lv in (1, 2, 3, 4):
        x, y = pt(0, lv)
        s += '<text class="lv" x="%.1f" y="%.1f">%d</text>' % (x + 4, y + 3, lv)
    area = [pt(i, max(v, .15)) for i, v in enumerate(levels)]
    s += '<polygon class="area" points="%s"/>' % " ".join("%.1f,%.1f" % p for p in area)
    for i, v in enumerate(levels):
        x, y = pt(i, v) if v else pt(i, 1)
        s += ('<circle class="dot" cx="%.1f" cy="%.1f" r="3.5"/>' % (x, y)) if v else ('<circle class="empty" cx="%.1f" cy="%.1f" r="4"/>' % (x, y))
        a = 2 * math.pi * i / n
        lx, ly = cx + (r + 18) * math.sin(a), cy - (r + 14) * math.cos(a)
        anchor = "middle" if abs(math.sin(a)) < .3 else ("start" if math.sin(a) > 0 else "end")
        s += '<text x="%.1f" y="%.1f" text-anchor="%s">%s</text>' % (lx, ly + 4, anchor, labels[i])
    desc = "; ".join("%s: %s" % (labels[i], LEVELS[v - 1] if v else "not yet") for i, v in enumerate(levels))
    svg = '<svg class="radar" viewBox="-44 0 408 300" role="img" aria-label="Skill map. %s">%s</svg>' % (desc, s)
    if not legend:
        return svg
    li = "".join('<li class="%s"><span>%s</span><span>%s</span></li>' % ("has" if v else "", labels[i], LEVELS[v - 1] if v else "Not yet") for i, v in enumerate(levels))
    return '<div class="radarwrap side">%s<ul class="stagelist" aria-hidden="true">%s</ul></div>' % (svg, li)


def meter(name, lv):
    return ('<div class="level"><div class="lh"><span>%s</span><b>%s</b></div><div class="meter" aria-hidden="true">%s</div></div>'
            % (name, LEVELS[lv - 1], "".join('<i class="%s"></i>' % ("on" if i < lv else "") for i in range(4))))


def conf(group=True):
    bars = lambda n: '<span class="bars">%s</span>' % "".join('<i class="%s"></i>' % ("f" if i < n else "") for i in range(3))
    g = ' data-group' if group else ''
    return ('<div class="conf"%s role="radiogroup" aria-label="How sure are you?">'
            '<button type="button" data-act="select" data-conf="50">%sGuessing<small>50%%</small></button>'
            '<button type="button" data-act="select" data-conf="70">%sFairly sure<small>70%%</small></button>'
            '<button type="button" data-act="select" data-conf="90">%sVery sure<small>90%%</small></button></div>') % (g, bars(1), bars(2), bars(3))


TK = {"evd": ("evidence", "Evidence"), "asm": ("help", "Assumption"), "alt": ("branch", "Alternatives"), "trd": ("scale", "Trade-offs")}


def tk(kind, inner, label=None):
    ic, lab = TK[kind]
    return '<div class="tk %s"><div class="tk-h">%s%s</div>%s</div>' % (kind, I(ic, "sm"), label or lab, inner)


def tklegend():
    return '<div class="tklegend">%s</div>' % "".join('<span class="%s">%s%s</span>' % (k, I(v[0], "sm"), v[1]) for k, v in TK.items())
