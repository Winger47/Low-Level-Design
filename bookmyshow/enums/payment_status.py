from enum import Enum


class PaymentStatus(Enum):
    """Payment Status"""
    PENDING="PENDING"
    SUCCESS="SUCCESS"
    FAILED="FAILED"
    REFUNDED="REFUNDED" 