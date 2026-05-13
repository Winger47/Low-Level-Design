from abc import ABC, abstractmethod
from models.expense import Expense
from models.split import Split


class SplitStrategy(ABC):
    @abstractmethod
    def compute_splits(self, expense: Expense) -> list[Split]:
        """Return the per-participant splits for an expense."""


class EqualSplit(SplitStrategy):
    def compute_splits(self, expense: Expense) -> list[Split]:
        share = round(expense.amount / len(expense.participants), 2)
        return [Split(user, share) for user in expense.participants]


class ExactSplit(SplitStrategy):
    def compute_splits(self, expense: Expense) -> list[Split]:
        if expense.exact_amounts is None:
            raise ValueError("ExactSplit requires exact_amounts")

        total = sum(expense.exact_amounts.values())
        if round(total, 2) != round(expense.amount, 2):
            raise ValueError(f"Exact amounts sum to {total}, expected {expense.amount}")

        return [Split(user, amount) for user, amount in expense.exact_amounts.items()]