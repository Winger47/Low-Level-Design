from enum import Enum


class CardStatus(Enum):
    """Status of a bank card."""
    ACTIVE = "ACTIVE"
    BLOCKED = "BLOCKED"
    