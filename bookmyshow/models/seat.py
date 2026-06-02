from enums import SeatType, SeatStatus
from exceptions import SeatNotAvailableError


class Seat:
    def __init__(self,seat_id:int,row_num:int,seat_num:int,price:int,   seat_type:SeatType):
        self.seat_id=seat_id
        self.row_num=row_num
        self.seat_num=seat_num
        self.price=price
        self.seat_type=seat_type
        self.status=SeatStatus.AVAILABLE
        
    def hold(self):
        if self.status!=SeatStatus.AVAILABLE:
            raise SeatNotAvailableError("Seat is not available")
        self.status=SeatStatus.HELD  
    def release(self):
        self.status=SeatStatus.AVAILABLE

    def book(self):
        if self.status!=SeatStatus.HELD:
            raise SeatNotAvailableError("Seat is not available")
        self.status=SeatStatus.BOOKED  

    def __repr__(self):
        return f"Seat(seat_id={self.seat_id},row_num={self.row_num},seat_num={self.seat_num},price={self.price},seat_type={self.seat_type},status={self.status})"    