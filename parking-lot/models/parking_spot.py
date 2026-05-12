from enums import SpotType
from exceptions import SpotNotAvailableError
from models.vehicles import Vehicle
from exceptions import ParkingException

SPOT_SIZE_ORDER = {
    SpotType.SMALL: 1,
    SpotType.MEDIUM: 2,
    SpotType.LARGE: 3,
}


class ParkingSpot:
    def __init__(self, spot_id: str, spot_type: SpotType):
        self.spot_id=spot_id
        self.spot_type=spot_type
        self.is_occupied=False
        self.parked_vehicle=None

    def can_fit(self, vehicle: Vehicle) -> bool:
        if self.is_occupied:
            return False
        return SPOT_SIZE_ORDER[self.spot_type] >= SPOT_SIZE_ORDER[vehicle.spot_type()]
        # check empty + size fits
        

    def park(self, vehicle: Vehicle) -> None:
        if not self.can_fit(vehicle):
            raise SpotNotAvailableError(vehicle.vehicle_type)
        self.is_occupied = True
        self.parked_vehicle = vehicle
        # raise SpotNotAvailableError if can't fit, else mark occupied
        

    def unpark(self) -> Vehicle:
        if not self.is_occupied:
            raise ParkingException(f"Spot {self.spot_id} is already empty")
        self.is_occupied = False
        vehicle=self.parked_vehicle
        self.parked_vehicle = None
        return vehicle
        # raise if empty, else return vehicle and clear
        

    def __repr__(self):
        return f"<ParkingSpot {self.spot_id} {self.spot_type.name} {'Occupied' if self.is_occupied else 'Available'}>"