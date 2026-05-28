


from states.atm_state import ATMState
from models.card import Card
from enums import TransactionType
from exceptions import InvalidPinError, CardBlockedError
class CardInsertedState(ATMState):

    def insert_card(self, card: Card) -> None:
           self._invalid_operation("insert_card")
        
    def enter_pin(self, pin: str) -> None:
        card=self.atm.current_card
        if card.verify_pin(pin):
            from states.pin_authenticated_state import PinAuthenticatedState
            card.failed_pin_attempts = 0
            self.atm.set_state(PinAuthenticatedState(self.atm))
            print("PIN accepted. Select operation.")
        else:
            card.failed_pin_attempts += 1
            attempts_remaining = 3 - card.failed_pin_attempts
    
            if attempts_remaining <= 0:
                # Block card, eject, back to idle
                from states.idle_state import IdleState
                card.block()
                self.atm.set_current_card(None)
                self.atm.set_state(IdleState(self.atm))
                raise CardBlockedError(card.card_number)    
            else:
                print(f"Invalid PIN. {attempts_remaining} attempts remaining.")
                raise InvalidPinError(attempts_remaining)  


    def eject_card(self) -> None:
        from states.idle_state import IdleState
        print(f"Card {self.atm.current_card.card_number} ejected.")
        self.atm.set_current_card(None)
        self.atm.set_state(IdleState(self.atm))

    def select_operation(self, operation: TransactionType) -> None:
        self._invalid_operation("select_operation")

