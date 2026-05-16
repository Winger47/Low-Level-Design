from enum import Enum


class TransactionStatus(Enum):
    """Status of a transaction."""
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"