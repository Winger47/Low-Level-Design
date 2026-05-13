from splitsize.run_test import balances
from splitsize.strategies.split_strategy import SplitStrategy
from models.user import User
from models.expense import Expense
from models.split import Split


class BalanceSheet:
    def __init__(self):
        self.balances: dict[User, dict[User, float]] = {}

    def _add_to_balance(self, owed_to: User, owed_by: User, amount: float) -> None:
        self.balances.setdefault(owed_to, {})[owed_by] = (
            self.balances.get(owed_to, {}).get(owed_by, 0.0) + amount
        )
        self.balances.setdefault(owed_by, {})[owed_to] = (
            self.balances.get(owed_by, {}).get(owed_to, 0.0) - amount
        )
        
    def update(self, expense: Expense, splits: list[Split]) -> None:
        """for each split (skipping payer's own), update both directions"""
        for split in splits:
            if split.user != expense.paid_by:
                self._add_to_balance(split.user, expense.paid_by, split.amount)
    
    def get_balance(self, user_a: User, user_b: User) -> float:
        return self.balances.get(user_a, {}).get(user_b, 0.0)
    
    def get_overall_balance(self, user: User) -> float:
        balance=0.0
        for amount in self.balances.get(user, {}).values():
            balance+=amount
        return balance
    def show_all_balances(self) -> None:
        for user in self.balances:
            balance=self.get_overall_balance(user)
            if balance > 0:
                print(f"{user.name} is owed {balance}")
    

