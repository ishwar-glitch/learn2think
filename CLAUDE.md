# Learn2Think — session rules

Founder = non-coder domain expert who directs; Claude writes all code and content. Claude Pro plan: keep every session lean.

## Start of every session
1. Read `BUILD_PLAN.md`. Find the next batch per its rules (and any `PARTIAL` resume note in the Log).
2. Read **only** what that batch needs:
   - **K batch:** the kit files it names.
   - **C batch:** follow `kit/00_Build_Rules.md` (its read order and Session Protocol).
   - **P batch:** `business/02_Execution_Plan.md` §3–5 + the `app/` files you'll touch (find them with Grep/Glob; never read whole trees).
3. Show a ≤ 5-line plan; wait for "go" unless the Notes in `BUILD_PLAN.md` say otherwise.

## During
- One batch per session. At each checkpoint, append a one-line resume note to the `BUILD_PLAN.md` Log.
- Run validators and tests as commands; read only failures. Don't re-read files you just wrote or print large files.
- UI changes: check in the browser pane at 375px and desktop before calling it done.
- If the usage limit or auto-compaction is near: stop at a clean point, write the resume note, set `PARTIAL`, tell the founder.
- Mechanical follow-ups (renames, formatting, copy tweaks): suggest the founder switch to Haiku 4.5.

## End
- Update status and Log; commit `<batch-id>: <summary>`.
- Tell the founder in ≤ 10 lines: done / failed / needs review, then suggest a fresh session for the next batch.

## Stack (details: Execution Plan §3–4)
Astro + React islands + TypeScript + Tailwind in `app/` · content from `../content` via content collections (zod) · Firebase (Auth, Firestore + Security Rules, Cloud Functions; test rules in the emulator) · Cloudflare Pages · Razorpay · sql.js · PostHog · Resend · Sentry.

## Commands
Run from the repo root (Git Bash or PowerShell; use `python`, not `python3`).
- Dev server: `npm --prefix app run dev` (http://localhost:4321; preview config `app` in `.claude/launch.json`)
- Build: `npm --prefix app run build`
- Type check: `npm --prefix app run check`
- Rules tests (Firestore emulator; needs Java): `npm --prefix firebase test`
- Validators: `python tools/validate_universe.py content/universe`; `python tools/validate_quiz.py content/core/<module>`
- CI: `.github/workflows/ci.yml` runs all of the above on push.
- Env: copy `app/.env.example` to `app/.env` (never commit). Deploy settings: `app/DEPLOY.md`.
<!-- P1 fills these in: dev, build, check, test, validate content, deploy -->

## Hard rules
- **No live LLM calls in the product** until the founder enables the live-AI batch (Execution Plan §5). All "AI" is scripted content.
- Never commit secrets; use env vars. Ask before pushing to a remote or changing production settings.
- Every Firestore collection is locked down by Security Rules; users only see their own documents. Rules changes need emulator tests.
- No employment, placement or "job-ready" claims in product copy.
- Launch scope is BA, DA, PM, PD. Don't build SC/SD.

## Runbook
<!-- P31 fills in: deploy, roll back, refund, data export/delete request, restore backup -->
- `firebase-tools` is pinned to 13.35.1 in `firebase/` because this machine has Java 11 (newer versions need Java 21). CI uses Java 17.
- `content.config.ts` schemas are loose placeholders until P3.
