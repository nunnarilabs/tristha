# Card Auth Validator (demo)

A tiny card-authorization decision engine used in training.

## What it does
Given a card and an amount, returns an authorization decision and an ISO 8583 response code,
applying decline-reason precedence.

## Rules (v1.0)
1. Invalid number → 14
2. Lost → 41 / Stolen → 43
3. Expired → 54
4. Invalid amount → 13
5. Debit not permitted → 57
6. Over per-transaction limit → 61
7. Velocity exceeded → 65
8. Insufficient funds → 51
9. Otherwise approve → 00

## Run
`python card_auth_validator.py`

> Docs version: v1.0 — keep this README in sync when the rules or limits change (see Task 11).
