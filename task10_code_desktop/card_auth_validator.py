"""
card_auth_validator.py
Simple card-authorization decision engine (demo for training).

Implements the decline-reason precedence from the card auth spec.
NOTE: this file contains two deliberate bugs for the hands-on exercise.
"""

PER_TXN_LIMIT = 50000
DAILY_VELOCITY = 3  # max approved transactions per card per day


def luhn_ok(number: str) -> bool:
    digits = [int(d) for d in number if d.isdigit()]
    checksum = 0
    parity = len(digits) % 2
    for i, d in enumerate(digits):
        if i % 2 == parity:
            d *= 2
            if d > 9:
                d -= 9
        checksum += d
    return checksum % 10 == 0


def authorize(card: dict, amount: int) -> dict:
    """Return {'decision':..., 'code':..., 'reason':...} and mutate card state on approval."""
    # 1. invalid card number
    if not card.get("number_valid", True) or not luhn_ok(card["number"]):
        return _decline("14", "Invalid card number")
    # 2. lost / stolen
    if card["status"] == "LOST":
        return _decline("41", "Card reported lost")
    if card["status"] == "STOLEN":
        return _decline("43", "Card reported stolen")
    # 3. expired
    if card["expired"]:
        return _decline("54", "Card expired")
    # 4. invalid amount
    if amount <= 0:
        return _decline("13", "Invalid amount")
    # 5. transaction not permitted
    if not card["debit_allowed"]:
        return _decline("57", "Transaction not permitted to cardholder")
    # 6. per-transaction limit  -- BUG: should decline only when amount > limit
    if amount >= PER_TXN_LIMIT:
        return _decline("61", "Exceeds per-transaction limit")
    # 7. velocity  -- BUG: should decline when approved_today >= DAILY_VELOCITY
    if card["approved_today"] > DAILY_VELOCITY:
        return _decline("65", "Exceeds frequency limit")
    # 8. insufficient balance
    if card["balance"] < amount:
        return _decline("51", "Insufficient funds")
    # 9. approve
    card["balance"] -= amount
    card["approved_today"] += 1
    return {"decision": "Approved", "code": "00", "reason": "Approved"}


def _decline(code, reason):
    return {"decision": "Declined", "code": code, "reason": reason}


if __name__ == "__main__":
    card_a = {"number": "4111111111111111", "number_valid": True, "status": "ACTIVE",
              "expired": False, "debit_allowed": True, "balance": 60000, "approved_today": 0}
    for amt in [20000, 50000, 10000, 10000, 5000]:
        print(amt, "->", authorize(card_a, amt))
