from models.parking_floor import ParkingFloor
from models.vehicles import Vehicle
from models.ticket import Ticket
from strategies.spot_assignment_strategy import SpotAssignmentStrategy
from exceptions import SpotNotAvailableError


class EntryGate:
    def __init__(self, gate_id: str, assigner: SpotAssignmentStrategy):

        self.gate_id=gate_id
        self.assigner=assigner
        self.ticket_counter=0
        # store gate_id, assigner
        # initialize ticket_counter = 0
        ...

    def park(self, floors: list[ParkingFloor], vehicle: Vehicle) -> Ticket:
        # find spot, validate, park, generate ticket id, return Ticket
        
        spot=self.assigner.find_spot(floors,vehicle)
        if not spot:
            raise SpotNotAvailableError(vehicle.vehicle_type)                  # ✅ SpotNotAvailableError(f"No spot available for {vehicle}")
        spot.park(vehicle)
        self.ticket_counter+=1  
        ticket_id=f"{self.gate_id}-{self.ticket_counter:03d}"
        return Ticket(ticket_id,vehicle,spot)
        ...

    def __repr__(self):
        return f"<EntryGate {self.gate_id} assigner={type(self.assigner).__name__}>"