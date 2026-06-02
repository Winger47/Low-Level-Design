from enum import Enum


class SeatStatus(Enum):
    """Status Of Seat"""
    AVAILABLE="AVAILABLE"
    BOOKED="BOOKED"
    HELD="HELD"   