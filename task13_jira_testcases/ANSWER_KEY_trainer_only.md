# Task 13 — Sample output (trainer only)

Generated live by Claude from **KAN-4** via the Jira connector. Use it to judge participant
answers — not a single "correct" set, but the coverage a strong answer should hit.

## Test-case table (Exercise B)

| Test ID | Title | Type | Preconditions | Steps | Test Data | Expected Result | AC | Priority |
|---|---|---|---|---|---|---|---|---|
| TC-01 | Approve valid purchase | Positive | Valid card, balance ≥ amount | Submit purchase | Card ****-4321, bal ₹50,000, amt ₹3,000 | Approved < 2s, 6-digit auth code returned | 1 | High |
| TC-02 | Auth latency under load | Performance (NFR) | 500 TPS load harness | Drive 500 TPS for 5 min | Mixed valid txns | p95 response < 2s | NFR | High |
| TC-03 | Decline on insufficient funds | Negative | Valid card, balance < amount | Submit purchase | bal ₹200, amt ₹5,000 | Decline, reason **51 – Insufficient Funds** | 2 | High |
| TC-04 | Decline expired card | Negative | Card past expiry | Submit purchase | Exp 01/2024 | Decline, reason **54 – Expired Card** | 3 | High |
| TC-05 | Decline blocked card | Negative | Card status = blocked | Submit purchase | Card ****-1234 (blocked) | Decline, reason **62 – Restricted Card** | 4 | High |
| TC-06 | Decline reported-lost card | Negative | Card status = lost | Submit purchase | Card ****-7788 (lost) | Decline, reason **62 – Restricted Card** | 4 | Medium |
| TC-07 | Below limit approves | Boundary | Valid card, sufficient bal | Submit purchase | amt ₹1,99,999 | Approved | 5 | Medium |
| TC-08 | At limit approves | Boundary | Valid card, sufficient bal | Submit purchase | amt ₹2,00,000 | Approved (limit is "above" 2,00,000) | 5 | High |
| TC-09 | Above limit declines + flags | Boundary | Valid card, sufficient bal | Submit purchase | amt ₹2,00,001 | Decline + flag for manual review | 5 | High |
| TC-10 | Decimal just over limit | Boundary | Valid card, sufficient bal | Submit purchase | amt ₹2,00,000.50 | Decline + flag (catches KAN-8) | 5 | Medium |
| TC-11 | Fraud lock on 4th attempt | Security | 3 declines logged < 60s | Submit 4th attempt | Same card, within 60s | Card locked 30 min + fraud alert raised | 6 | High |
| TC-12 | No lock outside window | Boundary | 3 declines, then wait > 60s | Submit 4th attempt | 4th at 61s | Not locked; processed normally | 6 | Medium |
| TC-13 | Audit log on approval | Audit | Logging enabled | Approve txn, inspect log | Any approved txn | Log has timestamp, masked PAN (last 4), amount, currency, reason | 7 | High |
| TC-14 | Audit log on decline | Audit | Logging enabled | Decline txn, inspect log | Any declined txn | Same fields logged with decline reason | 7 | Medium |
| TC-15 | No full PAN anywhere | Security (PCI) | DEBUG logging on | Submit txn, scan logs + API response | Card ****-4321 | Full 16-digit PAN never present (catches KAN-7) | NFR | High |
| TC-16 | Currency is INR / ISO-4217 | Positive | Valid card | Submit purchase | amt ₹3,000 | Response amount in INR, currency code = "INR" | NFR | Low |

## Ambiguous / untestable as written (Claude should flag these)
- **AC #1 "within 2 seconds":** functional vs performance test, and per-request vs p95 not stated. Pair with TC-02.
- **AC #5 boundary:** "above 2,00,000" implies exactly 2,00,000 is allowed — confirm with BA (TC-08).
- **AC #6 "3 declined attempts":** any decline reason, or only certain ones? Does the 30-min lock auto-release or need an unblock action?
- **AC #7 / NFR overlap:** masking is stated twice (AC #7 and NFR) — dedupe to avoid double-counting coverage.

## Coverage check (16 cases)
Positive 3 · Negative 4 · Boundary 4 · Security/PCI 3 · Audit 2 · Performance 1 — all 7 ACs + key NFRs covered. Three seeded defects (KAN-6, KAN-7, KAN-8) are caught by TC-03, TC-15, and TC-10 respectively.
