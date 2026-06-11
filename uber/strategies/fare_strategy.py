from abc import ABC, abstractmethod

from models.trip import Trip


class FareStrategy(ABC):
    @abstractmethod
    def calculate_fare(self, trip: Trip) -> float:
        pass


class DistanceTimeFareStrategy(FareStrategy):
    def __init__(self, base_fare: float = 0.0, rate_per_km: float = 10.0,
                 pickup_rate_factor: float = 0.5):
        self.base_fare = base_fare
        self.rate_per_km = rate_per_km
        self.pickup_rate_factor = pickup_rate_factor

    def calculate_fare(self, trip: Trip) -> float:
        ride_distance = trip.pickup_location.distance_to(trip.dropoff_location)
        pickup_distance = trip.driver.location.distance_to(trip.pickup_location)

        fare = (
            self.base_fare
            + ride_distance * self.rate_per_km
            + pickup_distance * self.rate_per_km * self.pickup_rate_factor
        )
        return fare