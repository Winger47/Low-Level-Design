from models.ticket import Ticket
from models.payment import Payment
from strategies.pricing_strategy import PricingStrategy


class ExitGate:
    def __init__(self, gate_id: str, pricing: PricingStrategy):
        self.gate_id = gate_id
        self.pricing = pricing
        self.payment_counter = 0

    def process_exit(self, ticket: Ticket) -> Payment:
        ticket.mark_exit()
        amount = self.pricing.calculate(ticket)
        self.payment_counter += 1
        payment_id = f"{self.gate_id}-{self.payment_counter:03d}"
        payment = Payment(payment_id, ticket.ticket_id, amount)
        payment.mark_completed()
        ticket.spot.unpark()
        return payment

    def __repr__(self):
        return f"<ExitGate {self.gate_id} pricing={type(self.pricing).__name__}>"