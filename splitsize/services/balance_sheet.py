from models.user import User
from models.expense import Expense
from models.split import Split


class BalanceSheet:
    def __init__(self):
        self.balances: dict[User, dict[User, float]] = {}

    def _add_to_balance(self, owed_to: User, owed_by: User, amount: float) -> None:
        if owed_to not in self.balances:
            self.balances[owed_to] = {}
        if owed_by not in self.balances[owed_to]:
            self.balances[owed_to][owed_by] = 0.0
        self.balances[owed_to][owed_by] += amount
        
    def update(self, expense, splits):
        payer = expense.paid_by
        for split in splits:
            if split.user == payer:
                continue
            self._add_to_balance(payer, split.user, split.amount)    # payer is owed
            self._add_to_balance(split.user, payer, -split.amount)   # participant owes
    
    def get_balance(self, user_a: User, user_b: User) -> float:
        return self.balances.get(user_a, {}).get(user_b, 0.0)
    
    def get_overall_balance(self, user: User) -> float:
        balance=0.0
        for amount in self.balances.get(user, {}).values():
            balance+=amount
        return balance
    def show_all_balances(self) -> None:
        for owed_to, debts in self.balances.items():
            for owed_by, amount in debts.items():
                if amount > 0:
                    print(f"{owed_by.name} owes {owed_to.name} {amount}")
    def __repr__(self):
        return f"<BalanceSheet users={len(self.balances)}>"
