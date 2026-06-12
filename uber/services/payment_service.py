

from enums import TripStatus,DriverStatus
from models.payment import Payment
from models.trip import Trip
class PaymentService:

    def __init__(self):
        self.payments=[]
        self.payment_counter=0

    def process_payment(self,trip:Trip)->Payment:

        if trip.status!=TripStatus.COMPLETED:
            raise Exception("Trip not completed")
        self.payment_counter+=1
        payment=Payment(self.payment_counter,trip,trip.fare)
        

        payment.mark_paid()
        self.payments.append(payment)
        trip.driver.status=DriverStatus.AVAILABLE  
        return payment
    def refund_payment(self,payment:Payment)->None:
        payment.mark_refunded()

        
    




        