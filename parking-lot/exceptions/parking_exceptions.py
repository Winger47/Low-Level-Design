
from enums import VehicleType
class ParkingException(Exception):
    """Base class for all parking lot exceptions."""


class SpotNotAvailableError(ParkingException):
    """Raised when no suitable spot is available for a vehicle."""
    def __init__(self, vehicle_type: VehicleType):
        super().__init__(f"No available spot for vehicle type: {vehicle_type.name}")
        self.vehicle_type = vehicle_type

class InvalidTicketError(ParkingException):
    """Raised when a ticket is invalid or not found."""
    def __init__(self, ticket_id: str):
        super().__init__(f"Invalid or expired ticket: {ticket_id}")
        self.ticket_id = ticket_id
class PaymentFailedError(ParkingException):
    """Raised when payment fails."""
    def __init__(self, ticket_id: str):
        super().__init__(f"Payment failed for ticket: {ticket_id}")
        self.ticket_id = ticket_id

class VehicleNotFoundError(ParkingException):
    """Raised when a vehicle is not found."""
    def __init__(self, vehicle_id: str):
        super().__init__(f"Vehicle not found: {vehicle_id}")
        self.vehicle_id = vehicle_id