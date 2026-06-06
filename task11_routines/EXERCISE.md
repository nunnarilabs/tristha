# Task 11 — Routines: keep docs in sync with code & publish

**Goal:** set up a repeating routine so that whenever code changes, the documentation is updated
and published automatically — no one forgets to update the README again.

> A routine is a saved, scheduled instruction Claude runs on its own. Here it watches the Task 10
> code folder and keeps the docs current.

## Pre-req
Use the folder from Task 10 (`task10_code_desktop/`) with `card_auth_validator.py` and `README.md`.
You'll have just fixed the two bugs in Task 10 — perfect trigger for a doc update.

## Set up the routine
In Cowork/Desktop, create a scheduled task / routine:
> "Every day at 6pm (and whenever I ask), check `card_auth_validator.py` for changes since the last
> run. If the rules, limits, or behaviour changed:
> 1. Update `README.md` so the rules section and the version number match the code.
> 2. Append a dated entry to `CHANGELOG.md` describing what changed (create the file if missing).
> 3. Publish the updated README as a shareable page and give me the link.
> Leave a one-line summary of what you changed each run."

## Prove it works
1. Make a small change to the code (e.g. change `PER_TXN_LIMIT` to 75000).
2. Run the routine now.
3. Check that `README.md` rules + version updated, `CHANGELOG.md` got a new dated entry, and you
   got a publish link.

## Discuss
- Routine = automation that runs on a schedule or trigger, applying your instructions every time.
- This closes a classic gap: docs drifting out of date from code.

## BFSI relevance
In regulated delivery, **traceability matters** — code and its documentation must agree, with a
dated history. A routine keeps the audit trail current automatically and publishes it for the team.
