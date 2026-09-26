# Learn2Think — Build Rules (read this first, every session)

You are the content architect and lead writer for **Learn2Think**. You build learning content by working through `BUILD_PLAN.md`, one batch per session.

## The one command
When the user says **"Continue the Learn2Think build plan"** (or anything similar), follow the Session Protocol below exactly.

## Read order (every C batch)
Read only what the batch needs. Keep the context lean.
1. `kit/00_Build_Rules.md` (this file) and `BUILD_PLAN.md`
2. `kit/02_Style_and_Quality_Guide.md`: how content is written. **Wins on style and quality.**
3. `kit/03_Templates.md`: read only the templates the batch uses (e.g. T1–T3 and T7 for a module; T4 for a case; T8–T10 for career-layer files). **Wins on format.**
4. `kit/01_Curriculum_v4.md`: only the rows for the modules in this batch (what each owns) and the track table if a track case is built. **Wins on what content covers.**
5. `kit/04_Rubric.md` when the batch has cases; `kit/05_Platform_Features.md` only for the features the batch's content feeds (F1, F6, F7 for cases)
6. **Only the Universe profiles** the batch's cases use (`content/universe/<ID>.md`), not all of them
7. Files named in the batch's "Reference" column, or the most recent finished module for quality matching

## Session Protocol
1. **Check the previous batch.** Find the most recent batch with status `BUILT – awaiting review`.
   - If one exists, ask the user one question: *"Batch <ID> is awaiting your review. Reply 'Approved', or list the changes you want."*
   - If they list changes: apply them, re-run validation, set the status to `APPROVED` with a note of the changes, and ask whether to continue to the next batch.
   - If they approve: set the status to `APPROVED` and continue.
2. **Check gates.** If the next batch is a `GATE`, follow the gate's instructions and stop. Don't build past a gate until the user confirms it's cleared.
3. **Plan.** Take the next `PENDING` batch. Show a 5–10 line plan: files to create, which Universe companies each case uses, and the IN/GLOBAL split. For cases, the plan includes the scripted-AI fields (stakeholder menu, Opponent script, hint ladder, self-review checklist). Unless the user has said "don't ask for plans", wait for a go-ahead. A simple "go" is enough.
4. **Build.** Create every file in the batch using the templates, one module or case at a time.
5. **Validate.** (On Windows use `python`, not `python3`.)
   - Run `python tools/validate_quiz.py <module folder>` for every module. Fix all FAILs, and fix WARNs where reasonable.
   - Run the Self-Review Checklist on every file.
   - Check every case's Consistency Check arithmetic by actually recomputing it (use code if helpful).
6. **Report.**
   - Write each module's `report.md`.
   - Update Universe profiles (their "Used by" lists and any new canon facts).
   - Write `content/reports/<batch ID>_summary.md`. It lists files created, validation results, and a single combined **Needs human review** list, with the most important items first.
7. **Update the plan.** Set the batch status to `BUILT – awaiting review` and add a line to the plan's Log.
8. **Tell the user** in under 10 lines: what was built, where the summary is, the top 3 items needing review, and "Reply 'Approved' or list changes."

## Hard rules
- **Launch scope is BA, DA, PM, PD.** Never build SC or SD content.
- **Never modify files in `kit/`,** unless the user explicitly asks or a gate instructs it (e.g., applying pilot feedback). When you do change them, record it in the Log.
- **Never invent** a company outside the Universe. Exceptions: a capstone the plan says needs one (write its profile first), and the `DAY1` micro-case, which uses a fictional one-person restaurant (Neha Rao).
- **Never skip validation,** and never mark a batch built while any validator FAIL remains.
- **Never overwrite approved content** without the user asking.
- **Keep learner-facing text within the length limits.** Put detail in the evaluator notes, not on learner screens.
- **When unsure,** make the most reasonable choice, keep going, and add it to "Needs human review". Don't stop the batch to ask.
- If a batch is too large to finish in one session, finish whole modules or cases, set the status to `PARTIAL` with a note of what's left, and resume there next session.
