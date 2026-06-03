



from exceptions import BookingNotFoundError
from exceptions import BookingNotCancellableError
from exceptions import SeatNotAvailableError
from strategies.refund_policy import RefundPolicy
from services.show_service import ShowService
from models.booking import Booking
from models.hold import Hold
from models.payment import Payment
from models.user import User
from models.show import Show
from models.seat import Seat
from datetime import datetime   
from enums import SeatStatus,BookingStatus  
import threading
from exceptions import HoldExpiredError

from exceptions import MaxSeatsExceededError,UserAlreadyHasActiveHoldError   
class BookingService:
    def __init__(self,show_service:ShowService,refund_policy:RefundPolicy,):
        self.show_service=show_service
        self.bookings=[]
        self.holds=[]
        self.refund_policy=refund_policy
        self.booking_counter=0
        self.hold_counter=0    
        self.max_seats=10
        self._lock=threading.Lock()

        
    def create_hold(self,user:User,show:Show,seat_ids:list[int])->Hold:
        with self._lock:
            return self._create_hold(user,show,seat_ids)


    def _create_hold(self,user:User,show:Show,seat_ids:list[int])->Hold:


        if len(seat_ids)>self.max_seats:
            raise MaxSeatsExceededError(f"Maximum {self.max_seats} seats allowed per booking")

        if self.check_if_active_hold(user):
            raise UserAlreadyHasActiveHoldError(f"User {user.user_id} already has an active hold")
        
        seats=self.get_seats(seat_ids,show)

        for seat in seats:
            if seat.status!=SeatStatus.AVAILABLE:
                raise SeatNotAvailableError(f"Seat {seat.seat_id} is not available")

        for seat in seats:
            seat.hold()
        
        hold=Hold(self.hold_counter,user,show,seats)
        self.hold_counter+=1
        self.holds.append(hold)

        self.booking_counter+=1
        booking=Booking(self.booking_counter,user,show,seats)
        self.bookings.append(booking)

        return booking

        




    def check_if_active_hold(self,user:User)->bool:

        for hold in self.holds:
            if hold.user.user_id==user.user_id and hold.is_active and not hold.is_expired():
                return True
        return False
            
    def get_seats(self,seat_ids:list[int],show:Show)->list[Seat]:
        result=[]

        seats=self.show_service.get_seats(show)

        for seat_id in seat_ids:
            for seat in seats:
                if seat_id==seat.seat_id:
                    result.append(seat)
                    break
            else:
                raise SeatNotAvailableError(f"Seat {seat_id} not found")    
        return result
    def confirm_booking(self, booking_id: int) -> None:
        with self._lock:
            return self._confirm_booking(booking_id)

    def _confirm_booking(self,booking_id:int,)->None:
        booking=self._get_booking(booking_id)


        booking_hold=self._get_hold_for_booking(booking)   
        if booking_hold is None or booking_hold.is_expired():
            booking.cancel()
            raise HoldExpiredError(f"Hold for booking {booking_id} has expired")
        

        booking.confirm()
        booking_hold.is_active=False   
    
    def _get_booking(self, booking_id: int) -> Booking:
        for booking in self.bookings:        # ← iterate through all bookings
            if booking.booking_id == booking_id:    # ← match the ID
                return booking
        raise BookingNotFoundError(f"Booking {booking_id} not found")

    def _get_hold_for_booking(self, booking: Booking) -> Hold:
        for hold in self.holds:
            if (hold.user.user_id == booking.user.user_id 
                and hold.show.show_id == booking.show.show_id):
                booking_seat_ids = {s.seat_id for s in booking.seats}
                hold_seat_ids = {s.seat_id for s in hold.seats}
                if booking_seat_ids == hold_seat_ids:
                    return hold
        return None
    def cancel_booking(self, booking_id: int) -> float:
        with self._lock:
            return self._cancel_booking(booking_id)

    def _cancel_booking(self,booking_id:int)->float:
        booking=self._get_booking(booking_id)

        if booking.status==BookingStatus.CANCELLED:
            raise BookingNotCancellableError(f"Booking {booking_id} is not in CONFIRMED state")
        amount=self.refund_policy.compute_refund(booking)
        booking.cancel()

        hold=self._get_hold_for_booking(booking)
        if hold:
            hold.is_active=False
        return amount
        






            

