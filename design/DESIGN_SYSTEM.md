# Learn2Think — Design System (v2, 26 Sep 2026; v2 = D3 redesign)

**Direction:** modern and minimal. Calm, credible, lots of space, one accent. Not a game, school or coaching centre (V1 brand brief).
Applied by D2 (wireframes → styled mock-ups) and P1 (app tokens). This replaces the V1 ChatGPT palette.

## Palette (founder-chosen)

| Token | Hex | Name |
|---|---|---|
| `cream` | #EAEFBD | Cream |
| `tea` | #C9E3AC | Tea Green |
| `willow` | #90BE6D | Willow Green |
| `carrot` | #EA9010 | Carrot Orange |
| `khaki` | #37371F | Dark Khaki |

## Roles (light theme, default)

| Role | Value | Notes |
|---|---|---|
| Page background | #FBFCF2 (cream, lightened) | Full cream everywhere is heavy; keep it for sections |
| Surface / cards | #FFFFFF with a 1px border of `tea` | Flat; no shadows, or one very soft one |
| Section / highlight background | `cream` | Hero, onboarding, "next action" card |
| Text, icons | `khaki` | 11.8:1 on the page background |
| Secondary text | `khaki` at 70% opacity | Check ≥ 4.5:1 |
| **Primary action (button)** | `carrot` fill, **`khaki` text** | 4.9:1 ✓. **Never white text on carrot** (2.5:1 ✗) |
| Progress, success, skill-map fill | `willow` | Fill only. **Never as text** on light backgrounds (2.1:1 ✗) |
| Selected / soft state, chips | `tea` fill, `khaki` text | 8.7:1 ✓ |
| Focus ring | 2px `#B86E00` (dark carrot) + 2px offset; plain `carrot` in dark theme | Carrot on white is 2.5:1, below the 3:1 UI minimum |

**Accessibility rules:**
- `carrot` and `willow` are **never used for text** on light backgrounds.
- Correct/incorrect feedback never relies on colour alone: always add an icon (✓ / ✕) and a word.
- Error state: `khaki` text with a ✕ icon and a `carrot` left border. There's no red, per the V1 brief.

## Dark theme

| Role | Value |
|---|---|
| Background | `khaki` #37371F (surfaces a step lighter, e.g. #42422A) |
| Text | `cream` (10.2:1) |
| Primary button | `carrot` fill, `khaki` text |
| Progress / links | `willow` (5.7:1) or `tea` (8.7:1) |

## Minimal style rules
- **Type:** one sans family (Inter or Manrope; must include ₹), 3 weights (400, 500, 600), and a scale of 12 / 14 / 16 / 20 / 28 / 34–48 (display). Body is 16px with 1.6 line height.
- **Space:** 8px grid; generous whitespace; one column on phones; max text width 680px.
- **Shape:** 12px radius on cards and 999px on buttons and chips; 1px borders instead of shadows.
- **Colour budget per screen:** mostly cream, white and khaki; `carrot` only for the **one** primary action; `willow` only for progress and success.
- **Icons:** line icons at 1.5px stroke (e.g. Lucide), in khaki.
- **Motion:** 150–200 ms ease-out on state changes only; respect reduced-motion settings; no confetti.
- **Components:** button (primary / secondary outline / text), card, chip, progress bar, radar (skill map, `willow` fill at 40% with a khaki outline), bottom bar (5 items, active = khaki label + `tea` pill).
- **Content:** no decorative illustrations; diagrams only when they reduce reading (V3 brief).

## v2 tokens (D3; source of truth `wireframes/wf.css`, checked by `_src/contrast.py`, all AA)

| Token | Light | Dark | Use |
|---|---|---|---|
| `--bg` | #FAFBF3 | #2E2E19 | Page |
| `--surface` | #FFFFFF | #37371F | Cards, inputs |
| `--surface-2` / `--sunken` | #F3F6E3 / #ECF0D6 | #414128 / #26261A | Quiet panels, tracks, trays |
| `--hero` | #EAEFBD (cream) | #45452B | The one "next action" surface |
| `--border` / `--border-strong` | #E1E7CB / #8A8B6A | #4E4E33 / #9A9B78 | Dividers / input and control outlines (≥3:1) |
| `--text` / `--text-2` / `--text-3` | #37371F / #56563F / #65654D | #EAEFBD / #D2D6AE / #B9BC98 | Body / secondary / meta (all ≥4.5:1) |
| `--accent` + `--on-accent` | carrot + khaki | same | Primary button only |
| `--ok-*` / `--warn-*` | willow fill, #5E8A3E line, #E3F0D4 soft / #B86E00 line, #FCEBCF soft | willow / carrot lines | Right / attention states, always with icon + word |
| `--t-evd/asm/alt/trd` | tints | tints | Thinking types (below) |

Radius 8/12/16/pill. Motion 180ms `cubic-bezier(.2,.7,.3,1)`; all motion off under reduced-motion. Icons: inline Lucide, 1.75 stroke (`_src/ui.py`).

## Component inventory (v2)

| Component | Class | Rule |
|---|---|---|
| Buttons | `.btn` `.primary` `.dark` `.ghost` `.sm` `.block` | One `primary` (carrot) per visible step. `dark` (khaki) for a second strong action, e.g. waitlist |
| App shell | `.rail` (desktop ≥1024), `.tabbar` (phone, 5 items, Lucide icons, tea pill), `.appbar` | Tabbed screens only |
| Focus mode | `.focusbar` (✕ close, title, step count, progress), `.wstabs` (Brief · Ask · Data · Draft), `.dock` | Sticky primary action in the thumb zone on phones |
| Hero card | `.hero` | Only the next action |
| List | `.list` rows with `.lead` icon, title, sub, chevron | Replaces stacks of cards |
| Chips | `.chip` `.tea` `.solid` `.plus` | Tags only; never tappable |
| Segmented control | `.segctl` | Two-to-four-way toggles (variant, Annual/Monthly, fact/assumption) |
| Tabs | `.tabs` | Sections within a screen |
| Choice | `.choice` with letter `.key` and `.state` | Answers; after Check: ✓/✕ icon + words + border + tint |
| Confidence | `.conf` (Guessing / Fairly sure / Very sure, bars + small %) | Required before Check |
| Checklist | `.checks` + `.checkfoot` | Self-review, Opponent self-check |
| Callout | `.callout` `.good` `.attn` | Always icon + words; no red |
| Thinking types | `.tk.evd` (solid willow border, clipboard-check), `.tk.asm` (dashed, question mark), `.tk.alt` (double border, branch), `.tk.trd` (dashed carrot, thick left edge, scale); `.tklegend` | Four cues each: icon, label, border pattern, tint |
| Level meter | `.levels` / `.meter` (4 segments + level word) | Rubric levels only; never a single score |
| Skill map | `radar()` in `_src/ui.py` | Level rings 1–4, dots, dashed "not yet" markers, text list beside it; aria-label reads all levels |
| Thinking Record | `.record` / `.rf` numbered fields; `.rf.locked` names the unlocking stage; `.stagerail` | Signature document look |
| Chat | `.msg.me/.them`, `.ask`, `.counter` with `.pips` | Scripted menu only |
| Exhibit | `details.exhibit` (`.locked`, `.fresh`), `table.data` | Highlight rows with `.hl` (tint + bold) |
| Hint ladder | `.ladder` | One level per tap; logged, never penalised |
| Tree | `.treeroot`, `.slot` (`.fill`, `.bad` with flag + reason), `.tray`, `.piece` | Tap-and-place |
| Worksheet | `details.ws` | Numbered, one open at a time |
| Plans | `.plans`, `.plan.best`, `.price`, `.ticks` | |

## States (for every batch)
- **Empty:** one sentence + one button (e.g. "No stories yet. Make one from a Thinking Record.").
- **Loading:** skeleton bars in `--sunken`, no spinners over 1 s; never block typing.
- **Error / offline:** `.callout.attn` with a plain message and a Retry button; typed work is kept locally and never lost.
- **Locked (Plus):** visible, quiet (`--text-3`), lock icon + `.chip.plus`; never a nag modal.
