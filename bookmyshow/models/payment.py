

from enums import PaymentMethod
from models.booking import Booking
from datetime import datetime
from enums import PaymentStatus
from exceptions import InvalidPaymentError

class Payment:
    def __init__(self,payment_id:int,booking:Booking,payment_method:PaymentMethod,amount:int):
        self.payment_id=payment_id
        self.booking=booking
        self.amount=amount
        self.payment_method=payment_method
        self.created_at=datetime.now()
        self.reason=""
        self.status=PaymentStatus.PENDING   

    def mark_success(self)->None:
        if self.status != PaymentStatus.PENDING:
            raise InvalidPaymentError(f"Cannot mark payment {self.payment_id} as SUCCESS from {self.status.name}")
        self.status=PaymentStatus.SUCCESS

    def mark_failed(self,reason:str="")->None:
        if self.status != PaymentStatus.PENDING:
            raise InvalidPaymentError(f"Cannot mark payment {self.payment_id} as FAILED from {self.status.name}")
        self.status=PaymentStatus.FAILED
        self.reason=reason

    def mark_refunded(self)->None:
        if self.status != PaymentStatus.SUCCESS:
            raise InvalidPaymentError(f"Cannot mark payment {self.payment_id} as REFUNDED from {self.status.name}")
        self.status=PaymentStatus.REFUNDED
    def __repr__(self):
        return f"Payment(payment_id={self.payment_id}, booking={self.booking.booking_id}, amount={self.amount}, payment_method={self.payment_method}, status={self.status})"
    