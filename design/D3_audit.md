# D3 audit of the D2 mock-ups (before the redesign)

Scope: the 19 screens in `wireframes/`. Rules: `DESIGN_SYSTEM.md`, the 41 decisions in `D1_decisions.md`, and kit/06 §0 (calm, adult, no game mechanics, no readiness scores).

| Area | What D2 does | Problem | D3 fix |
|---|---|---|---|
| **Hierarchy** | Every block is the same bordered card; h1/h2 carry all the weight | Nothing leads the eye. The next action on Home looks like every other card | One hero surface per screen (the next action). Cards only where content groups; plain lists elsewhere. Type scale 12/14/16/20/28/40 with 3 weights |
| **One primary action** | Several full-width carrot buttons can show at once (Day-1, Opponent, pricing) | Colour budget broken; the choice is unclear | One carrot button per visible step. Others become secondary (outline) or text |
| **Cognitive load** | Long, flat screens (Draft has 9 fields, Personal Problem 7 open sections) | Feels like a form, not a thinking tool | Draft grouped into 3 steps with a stepper; worksheet sections numbered with a done state; notes, hints and model answers stay closed |
| **Thumb reach** | Primary buttons sit mid-scroll; the top bar holds the only exit | Hard to reach one-handed on a 375px phone | Sticky bottom action area in focus mode; close (✕) top-left; bottom tab bar with 44px targets |
| **Navigation** | Bottom bar icons are empty squares; no desktop nav | Icons carry no meaning; desktop is just a wide phone | Lucide line icons; desktop gets a left rail and a two-column layout (content + context) |
| **Thinking made visible** | Evidence, assumptions, alternatives and trade-offs differ only by border style | Too subtle; relies on noticing a dotted line | Each type gets an icon, a label, a border pattern and a tint (never colour alone) |
| **Signature components** | Radar is a plain polygon; Thinking Record is a stack of cards | The two things that make Learn2Think different look generic | Radar with level rings, labelled vertices, "not yet" markers and a text list beside it. Record as a numbered document with a stage rail |
| **Feedback** | Quiz feedback relies on classes that the check handler did not reliably trigger; the founder saw no result | Broken core loop | Quiz rebuilt: explicit state (answer, confidence, checked); ✓/✕ icon, word and border on each option, calibration line, no instant retry |
| **States** | Empty, loading and error states not shown | Builders will invent them | Documented patterns in DESIGN_SYSTEM (empty = one sentence + one button; error = plain message + retry; saved work never lost). Shown where natural (exhibits locked, no asks left, request misses) |
| **Consistency** | Chips, pills and option buttons use one class for three jobs | Selection vs tag vs filter look alike | Separate components: chip (tag), segmented control (toggle), choice (answer), tabs |
| **Accessibility** | Focus ring in carrot (2.5:1 on white) | Fails the 3:1 non-text contrast | Focus ring uses a darker carrot (#B86E00, ≥3:1) in light theme; all pairs checked by `_src/contrast.py` |
| **Founder notes** | A large amber panel beside every screen | Competes with the design | Moved into a slim review bar and a "Notes" drawer (closed by default) |
