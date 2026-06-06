# Task 9 — Dispatch (parallel / background work)

**Goal:** kick off several independent jobs at once and let them run in the background while you
keep working — instead of doing them one at a time in a single chat.

> "Dispatch" sends work to background agents that run in parallel and report back when done.
> Great for fan-out tasks where each item is independent.

## Exercise — fan out test-case generation
Use the five independent stories in `stories_batch.md`.
Brief:
> "Dispatch five parallel jobs — one per story in this list. For each, generate test cases in our
> standard (Tristha format, full coverage). Save each as `tests_<feature>.md` and notify me when
> all five are done."

Watch them run in parallel; review the five outputs together when they return.

## A second pattern — long-running background job
> "In the background, read the whole `task07_cowork/specs/` folder and produce a consolidated
> coverage matrix across all features. Ping me when ready — I'll keep working meanwhile."

## Discuss
- Dispatch = parallelism + background execution. You're not blocked waiting.
- Best for **independent** items (5 stories, 20 defects) or **long** jobs (whole-folder analysis).
- Each job still follows your skills/Project standards.

## BFSI relevance
A whole sprint's worth of stories turned into first-draft test cases at once, or an overnight
coverage analysis across an entire release — while the team does other work.
