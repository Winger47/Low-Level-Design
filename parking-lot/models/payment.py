from enums import PaymentStatus
from exceptions import PaymentFailedError


class Payment:
    def __init__(self, payment_id: str,     ticket_id: str, amount: float):
        self.payment_id = payment_id
        self.ticket_id = ticket_id
        self.amount = amount
        self.status = PaymentStatus.PENDING

    def mark_completed(self) -> None:
        if self.status != PaymentStatus.PENDING:
            raise PaymentFailedError(self.ticket_id)
        self.status = PaymentStatus.COMPLETED

    def mark_failed(self) -> None:
        if self.status != PaymentStatus.PENDING:
            raise PaymentFailedError(self.ticket_id)
        self.status = PaymentStatus.FAILED

    def mark_refunded(self) -> None:
        if self.status != PaymentStatus.COMPLETED:
            raise PaymentFailedError(self.ticket_id)
        self.status = PaymentStatus.REFUNDED

    def __repr__(self):
        return f"<Payment {self.payment_id} ticket={self.ticket_id} {self.status.name} amount={self.amount}>"