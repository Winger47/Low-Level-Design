

from enums import PaymentStatus
from datetime import datetime
from models.trip import Trip
from exceptions import InvalidPaymentError
class Payment:
    def __init__(self,payment_id:int,trip:Trip,amount:float):
        self.payment_id=payment_id
        self.trip=trip
        self.amount=amount
        # self.payment_method=payment_method
        self.created_at=datetime.now()
        self.status=PaymentStatus.PENDING

    def mark_paid(self)->None:
        if self.status!=PaymentStatus.PENDING:
            raise Exception("Payment already paid")
        self.status=PaymentStatus.PAID

    def mark_failed(self, reason: str = "") -> None:
        if self.status != PaymentStatus.PENDING:
            raise Exception("Payment already processed")
        self.status = PaymentStatus.FAILED
        self.failure_reason = reason

    def mark_refunded(self)->None:
        if self.status!=PaymentStatus.PAID:
            raise Exception("Payment not paid")
        self.status=PaymentStatus.REFUNDED
    
    def __repr__(self):
        return f"Payment(id={self.payment_id}, trip_id={self.trip.trip_id}, amount={self.amount})"  