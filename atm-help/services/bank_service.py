from typing import Optional

from models.user import User
from models.account import Account
from models.card import Card


class BankService:
    """Minimal bank service — creates accounts and cards for demo purposes."""

    def __init__(self) -> None:
        self._accounts: dict[str, Account] = {}
        self._cards: dict[str, Card] = {}

    def create_account(self, user: User, account_id: str, balance: float = 0.0) -> Account:
        account = Account(user=user, account_id=account_id, balance=balance)
        self._accounts[account_id] = account
        return account

    def create_card(self, card_number: str, account: Account, pin: str) -> Card:
        card = Card(card_number=card_number, account=account, pin=pin)
        self._cards[card_number] = card
        return card

    def get_account(self, account_id: str) -> Optional[Account]:
        return self._accounts.get(account_id)

    def get_card(self, card_number: str) -> Optional[Card]:
        return self._cards.get(card_number)

    def __repr__(self) -> str:
        return f"BankService(accounts={len(self._accounts)}, cards={len(self._cards)})"
