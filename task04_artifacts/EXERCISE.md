# Task 4 — Artifacts (interactive & publishable)

**Goal:** turn raw data into something usable beside the chat — an interactive view and a publishable document — without writing code.

## Part A — Interactive artifact (a defect dashboard)
1. Upload `defects_export.csv` to a chat (use your Project from Task 3 if you like).
2. Prompt:
   > "From this defect export, build an **interactive HTML dashboard** I can click through:
   > totals by status, a bar chart of defects by module, a breakdown by severity,
   > and a filterable table. Highlight all S1 defects in red. Make it self-contained."
3. Interact with the artifact in the side panel — filter, hover, click.
4. Iterate in place:
   > "Add a count of P1 defects older than 7 days, and a pie chart of defects by team."

## Part B — Publishable artifact (a test summary report)
1. Same data, new prompt:
   > "Now produce a **one-page test summary report** for the client: overall status,
   > top risks (the open S1/P1 items), counts by module, and recommended next steps.
   > Professional tone, no jargon, ready to share."
2. Review the document artifact; ask for tweaks (e.g. "make the risks section a table").
3. Copy it out, or use the artifact's **publish/share** option to get a shareable link.

## Discuss
- **Interactive** artifacts = dashboards, calculators, checklists you click through.
- **Publishable** artifacts = documents you copy into Word/email or publish via a link.
- Both came from one CSV and plain-English prompts — no coding.

## BFSI relevance
A test manager can turn a defect export into a client-ready status dashboard and a written
summary in minutes, instead of an hour in Excel + PowerPoint.
