from enums import VehicleType


class Vehicle:
    def __init__(self, vehicle_id: int, license_plate: str, vehicle_type: VehicleType):
        self.vehicle_id = vehicle_id
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type
    def __repr__(self):
        return f"Vehicle(id={self.vehicle_id}, plate={self.license_plate}, type={self.vehicle_type.name})"