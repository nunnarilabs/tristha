# Day 2+3 Combined — 6-Hour Hands-On Run Sheet
### Working with Claude · Tristha Global · Lead: Navaneeth Malingan

**Format:** fully hands-on. Theory was covered Day 1. Today every participant *does* each task.
**Assumes:** each participant has Claude Desktop + a plan supporting Cowork, Connectors, Code, Dispatch and Routines, and is signed in.
**Connectors used:** Google Drive, ClickUp, Gmail (sandbox / non-production only).
**Sample files:** in `Day2_Handson/taskNN_.../` — each task folder has an `EXERCISE.md` and any data.

> **Golden rules for the room (say up front):** no real customer data — generate synthetic;
> you review and own every output; connect only approved sandbox accounts.

---

## Timetable (6 hours, ~10:00–16:00 with lunch)

| # | Time | Task | Feature | Folder |
|---|---|---|---|---|
| — | 10:00 | Welcome, setup check, ground rules | — | — |
| 1 | 10:15 | Compare model outputs | Models + Extended Thinking | `task01_model_comparison` |
| 2 | 10:45 | Research & web search | Research / Web | `task02_research` |
| 3 | 11:05 | Chat Projects | Projects + knowledge + memory | `task03_projects` |
| 4 | 11:40 | Artifacts | Interactive + publishable | `task04_artifacts` |
| — | 12:10 | Break | — | — |
| 5 | 12:20 | Connectors | Drive / ClickUp / Gmail | `task05_connectors` |
| 6 | 12:50 | Skills | Built-in + custom skill | `task06_skills` |
| — | 13:20 | Lunch | — | — |
| 7 | 14:00 | Cowork | Local folder + context + schedule | `task07_cowork` |
| 12 | 14:35 | Work with local Excel files | Read/edit/build/clean .xlsx | `task12_excel` |
| 8 | 15:05 | Live artifacts | Connector-backed dashboard | `task08_live_artifacts` |
| 9 | 15:20 | Dispatch | Parallel / background | `task09_dispatch` |
| 10 | 15:35 | Code under Desktop | Claude Code | `task10_code_desktop` |
| 11 | 15:55 | Routines | Docs-in-sync + publish | `task11_routines` |
| — | 16:10 | Show & tell, wrap, feedback | — | — |

> Task 12 (Excel) sits right after Cowork because editing local files in place is a Cowork
> capability. If you're tight on time, fold it into the Cowork block (Parts A–C only) and finish by 16:00.

Buffer is built in; if a task runs long, the model-comparison and dispatch tasks compress most easily.

---

## Pre-flight (do before 10:00)
- [ ] Stage Google Drive folder **"Tristha Demo Specs"** with the two files in `task05_connectors/gdrive_files_to_stage/`.
- [ ] Create ClickUp list **"Demo Defects"** with 3–4 rows from `task04_artifacts/defects_export.csv`.
- [ ] Have a Gmail thread **"UAT Status — Demo Bank"** ready.
- [ ] Copy the `Day2_Handson` folder to each participant machine (or share via Drive) so local-folder tasks work.
- [ ] Confirm everyone can open Claude Desktop and reach claude.ai.
- [ ] Have the Task 1 **answer key** open on your machine only.

---

# TASK 1 — Compare model outputs  (30 min)
**Feature:** model selection + Extended Thinking. **File:** `task01_model_comparison/`

**The aha:** harder reasoning needs a stronger model — and *thinking* makes it reliable.

**Run:**
1. Everyone opens `card_authorization_problem.md` (the **hard** version) and pastes it into Claude.
2. Run the **same** prompt on **Haiku → Sonnet → Opus → Opus with Extended Thinking**.
3. Score each against the trainer answer key (`ANSWER_KEY_trainer_only.md` — yours only).

**Expected (probabilistic):** Haiku ~10–13/17, Sonnet ~14–16/17, Opus ~16/17, Opus+Thinking 17/17.
**Watch the traps:** T9 (account daily cap beats balance), T10 (reversal must also cut the cumulative + velocity), T15 (rolling-60-min velocity), T16 (USD 360 → ₹30,240 crosses the ECOM limit), T17 (window has moved → it's a balance decline, not velocity). Plus shared-account bookkeeping across CARD-A/B.
**Debrief:** when do you reach for Opus/Thinking in real testing? (complex coverage, payment edge cases). Note non-determinism → always verify. **If a model surprises you (e.g. Haiku aces it), pivot:** "would you trust it on 50 transactions with no answer key? That's why we verify."
**BFSI tie:** this *is* an authorization-rules test — exactly your domain.

---

# TASK 2 — Research & web search  (20 min)
**Feature:** web search + Claude Research. **File:** `task02_research/research_brief.md`

**The aha:** Claude can pull current, *cited* information — not just memory.

**Run:** ask the ISO 20022 question (A) without web, (B) with web search, (C) as a full Research brief.
**Debrief:** compare staleness/citations/depth. When to use each. Always click through to verify sources.
**BFSI tie:** getting up to speed on a regulation/standard before scoping a test effort, with sources.

---

# TASK 3 — Chat Projects  (35 min)
**Feature:** Projects, knowledge files, cross-session memory. **File:** `task03_projects/EXERCISE.md`

**The aha:** set your standards once; every chat in the Project follows them.

**Run the 4 stages:** plain chat → Project (instructions only) → Project (+ knowledge files) → new chat in same Project (memory).
Files to use: `project_instructions.md`, `test_case_template.csv`, `severity_priority_definitions.md`, `naming_conventions.md`, `sample_user_story.md`.
**Watch for:** the jump in quality when knowledge files are added (their exact template/IDs/severity appear).
**BFSI tie:** a reusable team "Test Case Generator" that always uses Tristha's standard.

---

# TASK 4 — Artifacts  (30 min)
**Feature:** interactive + publishable artifacts. **File:** `task04_artifacts/EXERCISE.md`

**The aha:** raw data → a clickable dashboard and a client-ready report, no code.

**Run:** upload `defects_export.csv`. Part A: interactive defect dashboard (filter, charts, S1 in red), iterate in place. Part B: publishable one-page test summary; use publish/share.
**BFSI tie:** defect export → client status dashboard + written summary in minutes.

---

## ☕ Break (10 min)

---

# TASK 5 — Connectors under a Project  (30 min)
**Feature:** Drive, ClickUp, Gmail. **File:** `task05_connectors/EXERCISE.md`

**The aha:** Claude works from your live tools, not pasted text.

**Run:** enable the three connectors on the Project. A) Drive → read staged UPI spec, generate scenarios. B) ClickUp → summarise "Demo Defects". C) Gmail → draft a reply to the "UAT Status" thread (draft only).
**Say clearly:** admin-approved, permission-scoped, sandbox only; Claude drafts, you send.
**BFSI tie:** read the spec where it lives, pull defects from the tracker, draft the client email.

---

# TASK 6 — Skills & custom skills  (30 min)
**Feature:** built-in + custom skills. **File:** `task06_skills/EXERCISE.md`

**The aha:** a skill is plain-English instructions Claude invokes — and you can write your own.

**Run:** A) trigger a built-in skill (research). B) install the provided `tristha-testcase/SKILL.md`, then just ask for test cases — format auto-applies. C) co-author a new `bfsi-defect-report` skill live.
**BFSI tie:** encode Tristha's formats once; every analyst gets them automatically, everywhere.

---

## 🍴 Lunch

---

# TASK 7 — Cowork  (35 min)
**Feature:** local folder, multi-step, added context, scheduling. **File:** `task07_cowork/EXERCISE.md`

**The aha:** Claude works across a folder in several steps and saves real outputs.

**Run:** connect `task07_cowork/`. A) read all `specs/`, generate scenarios + consolidated strategy, save files. B) add context from a Drive file + a web link, update the strategy. C) set a weekday-9am scheduled scan.
**Watch for:** the autonomy — it chooses files, structure, and what to save.
**BFSI tie:** drop a sprint's specs in a folder → first-draft scenarios + strategy across all of them.

---

# TASK 12 — Work with local Excel files  (30 min)
**Feature:** read / edit / build / clean `.xlsx` locally (Cowork; read-only parts work in claude.ai). **File:** `task12_excel/EXERCISE.md`

**The aha:** Claude does the Excel grind testers live in — without you writing a formula or macro.

**Run (point Cowork at `task12_excel/`):**
- A) **Analyse** `Test_Cases.xlsx` — find blank Expected Results, inconsistent Severity, duplicates, uncovered ACs (report only).
- B) **Edit in place** — normalise Severity to S1–S4, fill blanks, add a Risk column, conditional-format S1 red, save.
- C) **Formulas** — on `Defect_Log.xlsx` add COUNTIFS summary (by severity/status, P1>7 days) + highlighting; change a value, watch totals update.
- D) **Generate** — turn the fund-transfer story into a 'Generated' sheet.
- E) **Clean** — fix `Messy_Test_Data.xlsx` (junk rows, dates, ₹/commas, dupes) into a 'Cleaned' sheet.
- F) stretch — build an RTM 'Traceability' sheet from Requirements + Test Cases.

**Watch for:** always reopen and review the saved file — they own the result.
**BFSI tie:** test-case workbooks, defect logs, RTMs, messy exports — an afternoon in Excel becomes a few prompts, all local (no client-data upload).

---

# TASK 8 — Live artifacts  (15 min)
**Feature:** connector-backed, self-refreshing artifact. **File:** `task08_live_artifacts/EXERCISE.md`

**The aha:** a saved page that re-queries your data every time it opens (vs Task 4's snapshot).

**Run:** in Cowork, build a live QA dashboard reading the ClickUp "Demo Defects" list; change a defect, hit Reload, watch it update.
**BFSI tie:** a standing "test status" page that's always current — no rebuilding dashboards.

---

# TASK 9 — Dispatch  (20 min)
**Feature:** parallel / background jobs. **File:** `task09_dispatch/EXERCISE.md`

**The aha:** fire off many independent jobs at once; keep working; review when they return.

**Run:** dispatch 5 parallel test-case jobs from `stories_batch.md`; optionally a background whole-folder coverage matrix.
**BFSI tie:** a whole sprint's stories drafted at once; overnight coverage analysis across a release.

---

# TASK 10 — Code under the Desktop app  (25 min)
**Feature:** Claude Code. **File:** `task10_code_desktop/EXERCISE.md`

**The aha:** non-coders can read code, confirm a bug, and raise a precise change request.

**Run:** open Claude Code on `task10_code_desktop/`. Explain the code → find the **two boundary bugs** (`>=` on the limit; `>` on velocity) → fix + prove with quick tests → generate a developer-ready CR.
**BFSI tie:** boundary bugs (= vs >, off-by-one) are exactly the defects that escape in payments.

---

# TASK 11 — Routines: docs in sync & publish  (20 min)
**Feature:** scheduled routine. **File:** `task11_routines/EXERCISE.md`

**The aha:** automation keeps documentation current with code — and publishes it.

**Run:** create a routine that, on code change, updates `README.md` + appends to `CHANGELOG.md` + publishes a link. Change `PER_TXN_LIMIT`, run it, verify docs + changelog + link.
**BFSI tie:** traceability — code and docs always agree, with a dated history, published for the team.

---

## Wrap (to 16:00)
- 3 volunteers show one thing they built today (any task).
- Recap the toolkit: models → research → Projects → artifacts → connectors → skills → Cowork → live artifacts → dispatch → code → routines.
- Each person names **one task they'll use on real work this week**.
- Collect feedback. Point them to the prompt library in the main deck's appendix.

## If you're short on time
Compress Task 1 (run Haiku + Opus+Thinking only) and Task 9 (one dispatch, skip the background job).
Protect Tasks 3, 5, 7 — Projects, Connectors and Cowork are the highest-value for this audience.

## If a connector/feature isn't available on someone's plan
Pair them with someone who has it for that task, and have them design the brief (inputs, expected
output, failure modes) on their own machine — they still learn the pattern.
