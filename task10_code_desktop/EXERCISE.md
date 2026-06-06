# Task 10 — Code under the Desktop app (Claude Code)

**Goal:** even non-coders can use Claude Code in the Desktop app to understand, test, and fix real
code — and hand confident, specific change requests to developers.

> Claude Code runs in Claude Desktop. Point it at this folder. You don't type code — you ask in
> English and review what it proposes.

## Setup
Open Claude Code (Desktop) on the folder `task10_code_desktop/`.

## Part A — Understand the code
> "Explain what `card_auth_validator.py` does in plain English, and list the rules it enforces."

## Part B — Find the bugs (there are two)
> "Compare the code against the rules in `README.md` and the card auth spec. Find any boundary
> bugs — especially around the per-transaction limit and the velocity check. Show me the exact
> lines and why they're wrong."

Expected finds:
- Per-txn limit uses `amount >= 50000` — wrongly declines an amount of *exactly* 50,000 (should be `>`).
- Velocity uses `approved_today > 3` — wrongly allows a 4th transaction (should be `>= 3`).

## Part C — Fix and prove it
> "Fix both bugs, then write quick tests that prove: 50,000 is allowed (not 61), and the 4th
> approved transaction is declined with 65. Run them and show the results."

## Part D — Generate a developer-ready change request
> "Write a short change request I can paste into ClickUp: what was wrong, the fix, and the test
> evidence."

## Discuss
- A test manager can now read code, confirm a suspected bug, and raise a precise CR — not "it
  feels wrong" but "line 48, `>=` should be `>`, here's the failing case."

## BFSI relevance
Boundary bugs (= vs >, off-by-one on limits and velocity) are exactly the defects that slip through
in payments. Claude Code helps non-coders pinpoint them.
