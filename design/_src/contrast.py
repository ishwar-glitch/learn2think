"""WCAG contrast check for the D3 token pairs. Run: python design/_src/contrast.py"""
def lum(h):
    h = h.lstrip("#"); c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    c = [x / 12.92 if x <= .03928 else ((x + .055) / 1.055) ** 2.4 for x in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]
def ratio(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True); return (la + .05) / (lb + .05)
L = dict(bg="#FAFBF3", surface="#FFFFFF", s2="#F3F6E3", sunken="#ECF0D6", hero="#EAEFBD", text="#37371F", t2="#56563F", t3="#65654D",
         bs="#8A8B6A", ring="#B86E00", accent="#EA9010", tea="#C9E3AC", okline="#5E8A3E", oksoft="#E3F0D4", warnsoft="#FCEBCF", warnline="#B86E00", trd="#FCEBCF")
D = dict(bg="#2E2E19", surface="#37371F", s2="#414128", sunken="#26261A", hero="#45452B", text="#EAEFBD", t2="#D2D6AE", t3="#B9BC98",
         bs="#9A9B78", ring="#EA9010", accent="#EA9010", okline="#90BE6D", oksoft="#3D4A2B", warnsoft="#4A3A1C", warnline="#EA9010", trd="#46391F")
TEXT = [("text", b) for b in ("bg", "surface", "s2", "sunken", "hero", "oksoft", "warnsoft", "trd")] + \
       [(t, b) for t in ("t2", "t3") for b in ("bg", "surface", "s2", "hero", "oksoft", "warnsoft")]
UI = [("bs", "bg"), ("bs", "surface"), ("ring", "bg"), ("ring", "surface"), ("okline", "oksoft"), ("warnline", "warnsoft"), ("okline", "surface"), ("warnline", "surface")]
fails = 0
for name, T in (("light", L), ("dark", D)):
    for kind, pairs, need in (("text", TEXT, 4.5), ("ui", UI, 3.0)):
        for a, b in pairs:
            r = ratio(T[a], T[b]); ok = r >= need; fails += not ok
            if not ok or kind == "ui": print("%-5s %-4s %-8s on %-8s %5.2f %s" % (name, kind, a, b, r, "OK" if ok else "FAIL"))
fixed = [("khaki on carrot (primary button)", "#37371F", "#EA9010", 4.5), ("khaki on tea (chip, tab pill)", "#37371F", "#C9E3AC", 4.5),
         ("cream on khaki (dark button)", "#FAFBF3", "#37371F", 4.5), ("khaki on cream (dark .btn.dark)", "#2E2E19", "#EAEFBD", 4.5),
         ("khaki on willow (ok key)", "#37371F", "#90BE6D", 4.5), ("willow text on dark bg", "#90BE6D", "#2E2E19", 4.5)]
for n, a, b, need in fixed:
    r = ratio(a, b); ok = r >= need; fails += not ok; print("fixed %-36s %5.2f %s" % (n, r, "OK" if ok else "FAIL"))
print("ALL PASS" if not fails else "%d FAIL" % fails)
