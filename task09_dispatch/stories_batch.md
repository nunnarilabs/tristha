# Batch of stories to dispatch (Task 9)

Five independent features — ideal to process in parallel.

1. **LOGIN — OTP on login:** OTP of 6 digits, valid 5 minutes, max 3 resends, account locks after 5 wrong OTPs.
2. **CARD — Block/unblock card:** Customer can block a card instantly; unblock requires OTP; blocked card declines all transactions.
3. **UPI — Set UPI PIN:** First-time PIN set via debit-card + OTP; PIN is 6 digits; cannot reuse last 3 PINs.
4. **STMT — Download statement:** Date-range statement as PDF; max range 1 year; closing balance must show.
5. **LOAN — EMI prepayment:** Part-prepayment reduces tenure or EMI (customer choice); foreclosure after 6 EMIs at 2% of outstanding.
