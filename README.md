# Learn2Think — How to Run the Build

## One-time setup (5 minutes)
1. Unzip `Learn2Think.zip` somewhere easy to find, e.g., your Documents folder.
2. Open the Claude desktop app, go to the **Code** tab, and open the `Learn2Think` folder. Pick **Sonnet 5** as the model.
3. Send:
   ```
   Continue the Learn2Think build plan.
   ```

## Every session after that
Send the same line:
```
Continue the Learn2Think build plan.
```

Claude will:
1. ask you to approve the last batch (reply **Approved**, or list your changes),
2. show a short plan for the next batch (reply **go**),
3. build, check and report.

**Your job per batch:**
- Read `content/reports/<batch>_summary.md`, especially the "Needs human review" list.
- Spot-read one module and one case in full.

## The template check (replaces the pilot gate)
In week 3, once M1–M2 are playable, you and 3–5 trusted people click through them for 2 days and send one list of feedback. Claude fixes the templates (batch K2) before the remaining content is written. Code work doesn't pause. Full schedule: `business/02_Execution_Plan.md`.

## Tips
- To skip plan approvals, add "don't ask for plans" under *Notes from the founder* in `BUILD_PLAN.md`.
- Keep the Claude desktop app open while a batch runs.
- Keep a backup copy of the folder, e.g., in Google Drive, after each approved batch.

## Folder map
| Path | Contents |
|---|---|
| `kit/` | The rules. Don't edit unless you're deliberately changing the design. |
| `BUILD_PLAN.md` | The queue and progress log |
| `content/universe/` | The fictional companies |
| `content/core/`, `content/specialist/` | Modules |
| `content/cases/` | All cases, challenges and capstones |
| `content/reports/` | Batch summaries |
| `tools/validate_quiz.py` | Automatic quiz quality checks |
