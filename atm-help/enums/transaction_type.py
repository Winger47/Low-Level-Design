from enum import Enum


class TransactionType(Enum):
    """Type of transaction."""
    WITHDRAW = "WITHDRAW"
    DEPOSIT = "DEPOSIT"
    CHECK_BALANCE = "CHECK_BALANCE"
    CHANGE_PIN = "CHANGE_PIN"
        