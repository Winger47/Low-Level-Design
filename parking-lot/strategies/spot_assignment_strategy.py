from abc import ABC, abstractmethod
from typing import Optional
from models.parking_floor import ParkingFloor
from models.parking_spot import ParkingSpot
from models.vehicles import Vehicle


class SpotAssignmentStrategy(ABC):

    @abstractmethod
    def find_spot(self,floors: list[ParkingFloor], vehicle: Vehicle) -> Optional[ParkingSpot]:
        """return available spot"""
class FirstAvailableSpotAssignment(SpotAssignmentStrategy):
    def find_spot(self,floors: list[ParkingFloor], vehicle: Vehicle) -> Optional[ParkingSpot] :
        for floor in floors:
            spot = floor.find_available_spot(vehicle)
            if spot:
                return spot
        return None    

