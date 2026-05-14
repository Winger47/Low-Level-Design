## Design Patterns Used

- **Strategy Pattern** — Splitting algorithms (Equal, Exact) are pluggable. Adding new split types (e.g., Percentage) needs no changes to existing code.
- **Custom Hashable Objects** — Users are dict keys via `__hash__` and `__eq__` on `user_id`, enabling O(1) balance lookups.
- **Separation of Concerns** — `Expense` records facts, `SplitStrategy` computes shares, `BalanceSheet` tracks running balances, `SplitwiseService` orchestrates.

## How to Run

```bash
python3 main.py
```

## Example Output
After dinner (equal split):
Bob owes Alice 1000.0
Charlie owes Alice 1000.0
After taxi (exact split):
Bob owes Alice 700.0
Charlie owes Alice 1000.0
Overall balances:
Alice is owed 1700.0
Bob owes 700.0
Charlie owes 1000.0

## Tech

- Python 3.9+
- No external dependencies