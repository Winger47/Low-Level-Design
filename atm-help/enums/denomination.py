from enum import Enum


class Denomination(Enum):
    """Denominations of currency supported by the ATM."""
    TWO_THOUSAND=2000
    FIVE_HUNDRED = 500
    HUNDRED = 100
    