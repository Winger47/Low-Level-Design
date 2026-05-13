from typing import Optional
from enums import SplitType
from models.user import User


class Expense:
    def __init__(
        self,
        expense_id: str,
        paid_by: User,
        amount: float,
        participants: list[User],
        split_type: SplitType,
        exact_amounts: Optional[dict[User, float]] = None,
    ):
        self.expense_id = expense_id
        self.paid_by = paid_by
        self.amount = amount
        self.participants = participants
        self.split_type = split_type
        self.exact_amounts = exact_amounts

    def __repr__(self):
        return f"<Expense {self.expense_id} paid_by={self.paid_by.name} amount={self.amount} participants={len(self.participants)}>"