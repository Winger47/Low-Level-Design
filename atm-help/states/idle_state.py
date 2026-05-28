from states.atm_state import ATMState
from models.card import Card
from enums import TransactionType
from exceptions import CardBlockedError


class IdleState(ATMState):
    """ATM is idle. Only insert_card is allowed."""

    def insert_card(self, card: Card) -> None:
        if card.is_blocked():
            raise CardBlockedError(card.card_number)
        from states.card_inserted_state import CardInsertedState  # local import to avoid cycle
        self.atm.set_current_card(card)
        self.atm.set_state(CardInsertedState(self.atm))
        print(f"Card {card.card_number} inserted.")

    def enter_pin(self, pin: str) -> None:
        self._invalid_operation("enter_pin")

    def eject_card(self) -> None:
        self._invalid_operation("eject_card")

    def select_operation(self, operation: TransactionType) -> None:
        self._invalid_operation("select_operation")