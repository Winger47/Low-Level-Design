from models.location import Location
from models.vehicle import Vehicle
from enums import DriverStatus


class Driver:
    def __init__(self, driver_id: int, name: str, vehicle: Vehicle, location: Location):
        self.driver_id = driver_id
        self.name = name
        self.vehicle = vehicle
        self.location = location
        self.status = DriverStatus.OFFLINE
        self.rating_sum = 0.0
        self.rating_count = 0

    def update_location(self, new_location: Location) -> None:
        self.location = new_location

    def go_online(self) -> None:
        self.status = DriverStatus.AVAILABLE

    def go_offline(self) -> None:
        self.status = DriverStatus.OFFLINE

    def is_available(self) -> bool:
        return self.status == DriverStatus.AVAILABLE

    def add_rating(self, rating: float) -> None:
        self.rating_sum += rating
        self.rating_count += 1

    @property
    def avg_rating(self) -> float:
        if self.rating_count == 0:
            return 0.0
        return self.rating_sum / self.rating_count

    def __repr__(self):
        return (f"Driver(id={self.driver_id}, name={self.name}, "
                f"status={self.status.name}, rating={self.avg_rating:.1f})")