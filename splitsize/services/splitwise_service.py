from typing import Optional
from models.user import User
from models.expense import Expense
from enums import SplitType
from strategies.split_strategy import EqualSplit, ExactSplit
from services.balance_sheet import BalanceSheet


class SplitwiseService:
    def __init__(self):
        self.users: dict[str, User] = {}
        self.expenses: list[Expense] = []
        self.balance_sheet = BalanceSheet()
        self.expense_counter = 0

    def add_user(self, user: User) -> None:
        if user.user_id in self.users:
            raise ValueError(f"User {user.user_id} already exists")
        self.users[user.user_id] = user

    def add_expense(
        self,
        paid_by: User,
        amount: float,
        participants: list[User],
        split_type: SplitType,
        exact_amounts: Optional[dict[User, float]] = None,
    ) -> Expense:
        if paid_by.user_id not in self.users:
            raise ValueError(f"Payer {paid_by.user_id} not registered")
        for participant in participants:
            if participant.user_id not in self.users:
                raise ValueError(f"Participant {participant.user_id} not registered")

        if split_type == SplitType.EQUAL:
            strategy = EqualSplit()
        elif split_type == SplitType.EXACT:
            strategy = ExactSplit()
        else:
            raise ValueError(f"Unsupported split type: {split_type}")

        self.expense_counter += 1
        expense_id = f"E-{self.expense_counter:03d}"
        expense = Expense(expense_id, paid_by, amount, participants, split_type, exact_amounts)

        splits = strategy.compute_splits(expense)
        self.balance_sheet.update(expense, splits)
        self.expenses.append(expense)
        return expense

    def show_balances(self) -> None:
        self.balance_sheet.show_all_balances()

    def __repr__(self):
        return f"<SplitwiseService users={len(self.users)} expenses={len(self.expenses)}>"