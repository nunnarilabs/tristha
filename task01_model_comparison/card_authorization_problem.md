# Task 1 — Card Authorization Reasoning Problem (hard)

**Paste everything below into Claude. Run it on Haiku, then Sonnet, then Opus, then Opus with Extended Thinking. Score each against the trainer answer key.**

> This version stresses real reasoning: cards that **share an account balance**, **foreign-currency conversion**, **channel-specific limits**, a **rolling-time-window** velocity rule, a **daily cumulative cap**, and a **reversal** that restores state. Process transactions strictly in order.

---

> Today's date is **6 June 2026** (so "this month" is 2026-06).

You are a card-authorization engine. Authorize each transaction **in order (T1 → T17)**, updating state as you go. Note that **two cards can share one account**, so an approval on one card reduces the shared balance for the other.

## Conversion, limits & rules

- **FX:** convert foreign currency to INR before any check. **USD 1 = ₹84, EUR 1 = ₹90.** Round to the nearest rupee. A non-INR transaction is **international**.
- **Channel per-transaction limit (on the INR amount):** POS ₹50,000 · ECOM ₹30,000 · ATM ₹25,000. "Exceeds" means strictly greater than the limit.
- **Account daily cap:** each **account** has a cumulative approved-spend cap of **₹80,000** across all its cards (starts at ₹0 today).
- **Velocity:** a card may have at most **3 approved transactions within any rolling 60-minute window**. Count only approved transactions whose time is **strictly within the last 60 minutes** of the current transaction. A reversal removes the reversed transaction from this count.
- **Reversal (REV):** refers to a previously approved transaction. It is **always processed** (never declined). It **restores** the account's available balance, **reduces** the account's daily cumulative, and **removes** the reversed transaction from that card's velocity count and approved-count.

## Decline-reason precedence — FIRST matching rule wins

1. Invalid card number (fails Luhn / marked invalid) → **14**
2. Card LOST → **41** · Card STOLEN → **43**
3. Card expired (expiry month before 2026-06) → **54**
4. International transaction on a card **not enabled for international** use → **62**
5. Invalid amount (amount ≤ 0) → **13**
6. Debit not permitted on the card → **57**
7. INR amount **>** the channel per-transaction limit → **61** (per-txn)
8. Card velocity: already **3 approved in the last 60 min** → **65**
9. Account daily cumulative **+** this INR amount **>** ₹80,000 → **61** (daily cap)
10. INR amount **>** account available balance → **51**
11. Otherwise → **Approved (00)** — reduce the account balance, add to the account's daily cumulative, and record the approval (time + count) for the card.

## Accounts (start of day)

| Account | Available balance | Cards on this account |
|---|---|---|
| ACC1 | ₹1,00,000 | CARD-A, CARD-B |
| ACC2 | ₹40,000 | CARD-C, CARD-F |
| ACC3 | ₹5,00,000 | CARD-E, CARD-G, CARD-H |

## Cards

| Card | Account | Number | Status | Expiry | Debit allowed | International enabled |
|---|---|---|---|---|---|---|
| CARD-A | ACC1 | Valid | ACTIVE | 12/2027 | Yes | Yes |
| CARD-B | ACC1 | Valid | ACTIVE | 11/2026 | Yes | **No** |
| CARD-C | ACC2 | Valid | ACTIVE | 12/2028 | Yes | Yes |
| CARD-D | ACC1 | **Invalid (Luhn)** | ACTIVE | 12/2027 | Yes | Yes |
| CARD-E | ACC3 | Valid | ACTIVE | 09/2026 | Yes | **No** |
| CARD-F | ACC2 | Valid | **STOLEN** | 01/2028 | Yes | Yes |
| CARD-G | ACC3 | Valid | ACTIVE | **03/2025** | Yes | Yes |
| CARD-H | ACC3 | Valid | ACTIVE | 01/2027 | **No** | Yes |

## Transactions (process in order)

| Txn | Time | Card | Channel | Amount |
|---|---|---|---|---|
| T1 | 09:00 | CARD-A | POS | ₹20,000 |
| T2 | 09:05 | CARD-D | POS | ₹5,000 |
| T3 | 09:10 | CARD-F | POS | ₹5,000 |
| T4 | 09:15 | CARD-G | POS | ₹5,000 |
| T5 | 09:20 | CARD-E | ECOM | USD 100 |
| T6 | 09:25 | CARD-H | POS | ₹5,000 |
| T7 | 09:30 | CARD-A | ECOM | ₹35,000 |
| T8 | 09:40 | CARD-B | POS | ₹50,000 |
| T9 | 09:45 | CARD-A | POS | ₹20,000 |
| T10 | 09:50 | — | REVERSAL | Reverse T8 |
| T11 | 09:55 | CARD-A | POS | ₹20,000 |
| T12 | 10:00 | CARD-C | ECOM | ₹5,000 |
| T13 | 10:10 | CARD-C | ECOM | ₹5,000 |
| T14 | 10:20 | CARD-C | ECOM | ₹5,000 |
| T15 | 10:30 | CARD-C | ECOM | ₹5,000 |
| T16 | 11:05 | CARD-C | ECOM | USD 360 |
| T17 | 11:10 | CARD-C | POS | ₹30,000 |

## Produce

A table: **Txn · Decision · Response code · One-line reason · Affected account's balance after · That card's approved-count after.**

Then state: **final ACC1 balance, final ACC2 balance, and the approved-count today for CARD-A, CARD-B, and CARD-C.**
