from models.parking_floor import ParkingFloor
from models.vehicles import Vehicle
from models.ticket import Ticket
from models.payment import Payment
from gates.entry_gate import EntryGate
from gates.exit_gate import ExitGate


class ParkingLot:
    def __init__(self, lot_id: str, floors: list[ParkingFloor],
                 entry_gate: EntryGate, exit_gate: ExitGate):
        # store all four attributes
        self.lot_id=lot_id
        self.floors=floors
        self.entry_gate=entry_gate
        self.exit_gate=exit_gate

        

    def park_vehicle(self, vehicle: Vehicle) -> Ticket:
        return self.entry_gate.park(self.floors, vehicle)
        

    def exit_vehicle(self, ticket: Ticket) -> Payment:
        return self.exit_gate.process_exit(ticket)
    

    def total_available_spots(self) -> int:
        return sum(floor.get_available_count() for floor in self.floors)    # ✅
    def __repr__(self):
        return f"<ParkingLot {self.lot_id} floors={len(self.floors)} available_spots={self.total_available_spots()}>"