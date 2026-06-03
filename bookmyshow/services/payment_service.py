


from exceptions import InvalidPaymentError
from models.booking import Booking
from services.booking_service import BookingService
from models.payment import Payment
from enums import PaymentMethod,PaymentStatus

class PaymentService:
    def __init__(self,booking_service:BookingService):
        self.booking_service=booking_service
        self.payments=[]
        self.payment_counter=0
    
    def process_payment(self,booking:Booking,payment_method:PaymentMethod)->Payment:
        self.payment_counter+=1

        payment=Payment(self.payment_counter,booking,payment_method,amount=booking.total_amount)


        self.payments.append(payment)
        print(f"Processing payment of ₹{booking.total_amount} via {payment_method.name}...")

        try:
            payment.mark_success()
            self.booking_service.confirm_booking(booking.booking_id)
            print(f"Payment {self.payment_counter} successful")
        except Exception as e:
            payment.mark_failed(reason=str(e))
            print(f"Payment {self.payment_counter} failed: {e}")
            raise
        return payment        
    

    def refund(self,payment:Payment,refund_amount:float)->None:
        if payment.status != PaymentStatus.SUCCESS:
            raise InvalidPaymentError(
                f"Cannot refund payment {payment.payment_id} in status {payment.status.name}"
            )
        print(f"Refunding ₹{refund_amount} for payment {payment.payment_id}")
        payment.mark_refunded()
