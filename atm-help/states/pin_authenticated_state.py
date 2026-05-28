from states.atm_state import ATMState
from models.card import Card
from enums import TransactionType


class PinAuthenticatedState(ATMState):
    """PIN has been verified. User can perform transactions or eject."""

    def insert_card(self, card: Card) -> None:
        self._invalid_operation("insert_card")

    def enter_pin(self, pin: str) -> None:
        self._invalid_operation("enter_pin")

    def eject_card(self) -> None:
        from states.idle_state import IdleState
        print(f"Card {self.atm.current_card.card_number} ejected.")
        self.atm.set_current_card(None)
        self.atm.set_state(IdleState(self.atm))

    def select_operation(self, operation: TransactionType) -> None:
        from states.transaction_state import TransactionState
        print(f"Selected: {operation.name}")
        self.atm.set_state(TransactionState(self.atm, operation))