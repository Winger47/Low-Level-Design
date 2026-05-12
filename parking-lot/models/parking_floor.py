from models.vehicles import Vehicle
from models.parking_spot import ParkingSpot
from typing import Optional
# from __future__ import annotations
class ParkingFloor:
    def __init__(self,floor_id:str,spots:list[ParkingSpot]):
        self.floor_id=floor_id
        self.spots=spots
    def find_available_spot(self, vehicle: Vehicle) -> Optional[ParkingSpot]:
        for spot in self.spots:
            if spot.can_fit(vehicle):
                return spot
        return None
    

    def get_available_count(self)->int:
        return sum(1 for spot in self.spots if not spot.is_occupied)

    def __repr__(self):
        return f"<ParkingFloor {self.floor_id} available={self.get_available_count()}/{len(self.spots)}"