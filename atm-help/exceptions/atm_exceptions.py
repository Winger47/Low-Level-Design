


class ATMException(Exception):
    """Base exception for all ATM-related errors."""


class InvalidPinError(ATMException):
    def __init__(self,attempts_remaining: int):
        self.attempts_remaining=attempts_remaining
        super().__init__(f"Invalid PIN. {attempts_remaining} attempts remaining")   



class CardBlockedError(ATMException):
    def __init__(self,card_number:str):
        self.card_number=card_number
        super().__init__(f"Card {card_number} is blocked")

class InsufficientFundsError(ATMException):
    def __init__(self,requested_amount:int,available_balance:int):
        self.requested_amount=requested_amount
        self.available_balance=available_balance
        super().__init__(f"Insufficient funds. Requested: {requested_amount}, Available: {available_balance}")

class InvalidOperationError(ATMException):
    def __init__(self,operation: str, current_state: str):
        self.operation=operation
        self.current_state=current_state
        super().__init__(f"Cannot perform '{operation}' in state '{current_state}'")
class InsufficientCashInATMError(ATMException):
    """Raised when the ATM cannot dispense the requested amount."""

    def __init__(self, requested_amount: int):
        self.requested_amount = requested_amount
        super().__init__(f"ATM cannot dispense {requested_amount} with available denominations")


