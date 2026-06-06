# Task 12 — Work with local Excel files

**Goal:** use Claude to read, fix, build, and clean real `.xlsx` files on your machine — the format
testers actually live in. Best done in **Cowork / Claude Desktop** (it can edit local files in place);
you can also do the read/analyse parts in claude.ai by uploading the file.

## Files in this folder
- `Test_Cases.xlsx` — a test-case workbook (sheet **Test Cases** + sheet **Requirements**). It has
  deliberate problems: blank Expected Results, inconsistent Severity values ("Critical", "High",
  "s2"…), a duplicate scenario, and a few blank Priority/Status cells.
- `Defect_Log.xlsx` — a raw defect log with **no summary formulas** yet.
- `Messy_Test_Data.xlsx` — a messy export: junk title rows on top, headers in row 5, trailing spaces,
  mixed date formats, amounts as text with ₹/commas, a negative amount, a non-numeric amount, a
  duplicate row, and a blank row.

> Point Cowork at this `task12_excel/` folder before you start.

## Part A — Read & analyse (no editing)
On `Test_Cases.xlsx`:
> "Review the 'Test Cases' sheet. List: rows with a missing Expected Result, any inconsistent
> Severity values, likely duplicate scenarios, and which acceptance criteria in the 'Requirements'
> sheet have **no** test case. Don't change the file — just report."

## Part B — Edit in place
> "Now fix `Test_Cases.xlsx`: normalise all Severity values to S1–S4 (map Critical→S1, High→S2,
> Medium→S3), fill the blank Expected Results based on each scenario, fill blank Priority/Status
> sensibly, add a new column **'Risk'** (High/Med/Low) derived from Severity, and apply conditional
> formatting so S1 rows are red. Save the file."
Open it in Excel and check the changes landed.

## Part C — Build formulas & a summary
On `Defect_Log.xlsx`:
> "Add a summary block: counts of defects by Severity (S1–S4) and by Status, and a count of P1
> defects older than 7 days — using live formulas (COUNTIFS), not hard-coded numbers. Add a small
> table I could turn into a chart, and apply conditional formatting to highlight S1 rows. Save it."
Change a status in the data and watch the formula totals update.

## Part D — Generate a worksheet from a story
> "From the fund-transfer user story (in `../task03_projects/sample_user_story.md`), generate a new
> sheet of test cases in our standard template and add it to `Test_Cases.xlsx` as a sheet called
> 'Generated'."

## Part E — Clean a messy export
On `Messy_Test_Data.xlsx`:
> "Clean this into a tidy table: drop the junk title rows, use row 5 as headers, trim spaces,
> standardise dates to YYYY-MM-DD, convert Amount to a number (strip ₹ and commas), standardise
> Currency (INR/USD), remove the duplicate and blank rows, and flag the negative and non-numeric
> amounts in an 'Issues' column. Save the result as a new sheet 'Cleaned'."

## Part F (stretch) — Build an RTM
> "Using the 'Requirements' and 'Test Cases' sheets, build a 'Traceability' sheet mapping each Req
> ID to its test case IDs with a coverage status (covered/partial/none). Flag uncovered requirements."

## Discuss
- Claude can **read, analyse, edit, generate, and clean** Excel files locally — the bread-and-butter
  of a test manager's week — without you writing formulas or macros.
- Always reopen and **review** the saved file. You own the result.

## BFSI relevance
Test-case workbooks, defect logs, RTMs, and messy data exports are where testers spend hours.
This turns "an afternoon in Excel" into a few prompts — kept local, no upload of client data required.
