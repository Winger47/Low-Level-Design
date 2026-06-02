from enum import Enum


class BookingStatus(Enum):
    """Status Of Booking"""
    PENDING="PENDING"
    CONFIRMED="CONFIRMED"
    CANCELLED="CANCELLED"

    
    