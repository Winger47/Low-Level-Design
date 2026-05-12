
from enums import VehicleType, SpotType


class Vehicle:
    def __init__(self, license_plate: str, vehicle_type: VehicleType):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type

    def spot_type(self)->SpotType:
        if self.vehicle_type == VehicleType.BIKE:
            return SpotType.SMALL
        elif self.vehicle_type == VehicleType.CAR:
            return SpotType.MEDIUM
        elif self.vehicle_type == VehicleType.TRUCK:
            return SpotType.LARGE   

    def __repr__(self):
        return f"<Vehicle {self.vehicle_type.name} {self.license_plate}>"


