# Spec — Card Authorization Rules (stage this in Google Drive)

**Feature:** Real-time authorization decision for card transactions (POS / ATM).

## Validation & decision rules
- V1: Card number must pass Luhn; invalid → decline 14.
- V2: Card status LOST → 41, STOLEN → 43.
- V3: Expired card → 54.
- V4: Amount must be > 0 → else 13.
- V5: Transaction type must be permitted on the card (e.g. debit allowed) → else 57.
- V6: Per-transaction limit ₹50,000; amount over limit → 61.
- V7: Max 3 approved transactions per card per day; 4th+ → 65.
- V8: Available balance must cover the amount → else 51.
- V9: Otherwise approve (00); reduce balance and increment daily count.

## Notes
- Response codes follow ISO 8583 DE39.
- Decline-reason precedence applies top to bottom (V1 highest).
