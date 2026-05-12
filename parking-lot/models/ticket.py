from datetime import datetime
from models.vehicles import Vehicle
from models.parking_spot import ParkingSpot
from exceptions import InvalidTicketError


class Ticket:
    def __init__(self, ticket_id: str, vehicle: Vehicle, spot: ParkingSpot):
        self.ticket_id = ticket_id
        self.vehicle = vehicle
        self.spot = spot
        self.entry_time = datetime.now()
        self.exit_time = None

    def mark_exit(self) -> None:
        if self.exit_time:
            raise InvalidTicketError(self.ticket_id)
        self.exit_time = datetime.now()

    def get_duration_hours(self) -> float:
        end = self.exit_time if self.exit_time else datetime.now()
        return (end - self.entry_time).total_seconds() / 3600

    def __repr__(self):
        status = "Exited" if self.exit_time else "Active"
        return f"<Ticket {self.ticket_id} {status} vehicle={self.vehicle.license_plate} spot={self.spot.spot_id}>"