# Task 6 — Skills & creating a custom skill

**Goal:** understand what a skill is (plain-English instructions Claude can invoke), use a
built-in one, then create your own team skill — no code.

## Part A — See a built-in skill in action
In Cowork/Desktop, ask:
> "Research deepweaver.ai and give me a one-paragraph company brief."
Watch a built-in research skill activate. Open a skill folder and read the first lines aloud —
*it's just Markdown instructions.*

## Part B — Install & use the custom skill in this folder
The folder `tristha-testcase/` contains `SKILL.md` — a custom skill that always outputs test
cases in Tristha's standard.
1. Add it as a skill (Settings → Capabilities/Skills → add the `tristha-testcase` folder),
   or drop the folder into your skills directory.
2. Then simply ask:
   > "Generate test cases for an OTP-on-login feature."
   Notice it auto-applies the Tristha format, IDs, severity scale and coverage rules —
   without you pasting any instructions.

## Part C — Create one live, together
Ask Claude to help you author a new skill:
> "Help me write a SKILL.md for a 'bfsi-defect-report' skill that turns a rough defect note
> into a clean report: title, steps to reproduce, expected vs actual, severity (S1–S4) with
> reason, and impact. Output the SKILL.md."
Save it, add it, and test it on a messy one-line defect.

## Discuss
- A **skill** = reusable behaviour packaged as Markdown; it activates when relevant.
- A **Project knowledge file** applies inside one project; a **skill** travels with you everywhere.
- Skills are how a team encodes its standards once and shares them.

## BFSI relevance
Encode Tristha's test-case format, defect-report format, or RTM rules as skills — every analyst
gets the same quality automatically.
