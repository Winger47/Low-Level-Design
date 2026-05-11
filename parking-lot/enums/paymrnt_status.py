from enum import Enum


class PaymentStatus(Enum):
    """Lifecycle state of a payment transaction."""
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    REFUNDED = "REFUNDED"