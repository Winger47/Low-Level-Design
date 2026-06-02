


from enums import booking_status
from datetime import datetime
from models.show import Show
from models.user import User
from enums.booking_status import BookingStatus
from models.seat import Seat
from exceptions import BookingNotCancellableError

class Booking:
    def __init__(self, booking_id: int, user: User, show: Show, seats: list[Seat]):
        self.booking_id=booking_id
        self.user=user
        self.show=show
        self.seats=seats
        self.total_amount:float=sum(seat.price for seat in seats)
        self.status=BookingStatus.PENDING   
        self.created_at=datetime.now()


    def confirm(self) -> None:
        if self.status != BookingStatus.PENDING:
            raise BookingNotCancellableError(f"Booking {self.booking_id} is not in PENDING state")
        self.status = BookingStatus.CONFIRMED
        for seat in self.seats:
            seat.book()

    
    def cancel(self):
        self.status = BookingStatus.CANCELLED
        for seat in self.seats:
            seat.release()    
    def __repr__(self):
        return (
            f"Booking(booking_id={self.booking_id}, user={self.user.name}, "
            f"show_id={self.show.show_id}, seats={len(self.seats)}, "
            f"total={self.total_amount}, status={self.status.name})"
        )