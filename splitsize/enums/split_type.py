from enum import Enum


class SplitType(Enum):
    """Type of split used to divide an expense among participants."""
    EQUAL = "EQUAL"
    EXACT = "EXACT"