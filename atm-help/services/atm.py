from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from models.card import Card
from models.cash_dispenser import CashDispenser
from enums import TransactionType
from exceptions import InvalidOperationError

if TYPE_CHECKING:
    from states.atm_state import ATMState


class ATM:
    """Main ATM controller that delegates operations to the current state."""

    def __init__(self, cash_dispenser: CashDispenser) -> None:
        from states.idle_state import IdleState

        self.cash_dispenser: CashDispenser = cash_dispenser
        self.current_state: ATMState = IdleState(self)
        self.current_card: Optional[Card] = None
        self.transactions: List = []
        self.transaction_counter: int = 0

    # ── State-machine delegations ──────────────────────────────────────

    def insert_card(self, card: Card) -> None:
        self.current_state.insert_card(card)

    def enter_pin(self, pin: str) -> None:
        self.current_state.enter_pin(pin)

    def eject_card(self) -> None:
        self.current_state.eject_card()

    def select_operation(self, operation: TransactionType) -> None:
        self.current_state.select_operation(operation)

    # ── Transaction-level operations (only valid in TransactionState) ──

    def withdraw(self, amount: float) -> None:
        if not hasattr(self.current_state, "withdraw"):
            raise InvalidOperationError("withdraw", type(self.current_state).__name__)
        self.current_state.withdraw(amount)

    def deposit(self, amount: float) -> None:
        if not hasattr(self.current_state, "deposit"):
            raise InvalidOperationError("deposit", type(self.current_state).__name__)
        self.current_state.deposit(amount)

    def check_balance(self) -> None:
        if not hasattr(self.current_state, "check_balance"):
            raise InvalidOperationError("check_balance", type(self.current_state).__name__)
        self.current_state.check_balance()

    def change_pin(self, old_pin: str, new_pin: str) -> None:
        if not hasattr(self.current_state, "change_pin"):
            raise InvalidOperationError("change_pin", type(self.current_state).__name__)
        self.current_state.change_pin(old_pin, new_pin)

    # ── Setters ────────────────────────────────────────────────────────

    def set_state(self, state: "ATMState") -> None:
        self.current_state = state

    def set_current_card(self, card: Optional[Card]) -> None:
        self.current_card = card

    # ── Helpers ────────────────────────────────────────────────────────

    def next_transaction_id(self) -> str:
        self.transaction_counter += 1
        return f"TXN-{self.transaction_counter:04d}"

    def __repr__(self) -> str:
        return f"ATM(state={type(self.current_state).__name__})"
