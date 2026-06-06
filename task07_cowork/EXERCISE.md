# Task 7 — Cowork (work in a local folder, add context, schedule)

**Goal:** let Claude work across a folder of real files in multiple steps — read, decide, produce,
save — then add outside context and schedule it to repeat.

> Cowork runs in the Claude Desktop app. Point it at a folder on your machine and brief it like
> you'd brief a junior analyst.

## Setup
Open Cowork and connect this folder: `task07_cowork/` (it contains a `specs/` folder with three
specs and a strategy template).

## Part A — Work in the local folder
Brief:
> "Read every spec in the `specs/` folder. For each, generate test scenarios in our standard.
> Then produce one consolidated **test strategy** following `test_strategy_template.md`, covering
> all three features. Save each feature's scenarios as `scenarios_<feature>.md` and the strategy
> as `test_strategy_v1.md` in this folder."

Watch it: read multiple files → decide what matters → write several outputs → save them.
Open the saved files.

## Part B — Add context from a file, a Drive doc, and a link
> "Also factor in our daily-limit rule from the Google Drive file 'card_auth_rules_spec' and the
> latest UPI limits from [paste an RBI/NPCI URL]. Update `test_strategy_v1.md` accordingly and
> note what changed."

Shows Cowork pulling context from a local file + a Drive connector + a web link in one task.

## Part C — Schedule it
Set a scheduled task:
> "Every weekday at 9am, scan this folder for any new or changed spec and regenerate the affected
> scenarios, then leave me a short note of what changed in `daily_update.md`."

## Discuss
- Cowork = autonomy + planning across files (the agentic ingredients from Day 1).
- It made decisions you didn't dictate — which files, what structure, what to save.

## BFSI relevance
A test lead drops a sprint's specs in a folder and gets first-draft scenarios + a strategy doc
across all of them — overnight, on a schedule.
