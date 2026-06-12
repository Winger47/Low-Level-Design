from enums import DriverStatus, TripStatus, VehicleType
from strategies.fare_strategy import FareStrategy
from models.trip import Trip
from models.location import Location
from models.rider import Rider
from services.matching_service import MatchingService
import threading
from strategies.cancellation_policy import TimeBasedCancellationPolicy,CancellationPolicy
# from datetime import datetime

class TripService:
    def __init__(self, matching_service: MatchingService, fare_strategy: FareStrategy,cancellation_policy:CancellationPolicy)   :
        self.trips = []
        self.trip_counter = 0
        self.matching_service = matching_service
        self.fare_strategy = fare_strategy
        self.cancellation_policy = cancellation_policy
        self._lock=threading.Lock()

        # self.requested_at = datetime.now() 

    def request_trip(self, rider: Rider, pickup: Location,
                     dropoff: Location, vehicle_type: VehicleType) -> Trip:
        with self._lock:
            driver = self.matching_service.find_nearest_driver(pickup, vehicle_type)

            self.trip_counter += 1
            trip = Trip(self.trip_counter, rider, pickup, dropoff)
            trip.assign_driver(driver)
            driver.status = DriverStatus.ON_TRIP
            self.trips.append(trip)
        return trip

    def start_trip(self, trip: Trip, otp: int) -> None:
        trip.start(otp)

    def complete_trip(self, trip: Trip) -> float:
        trip.complete()
        fare = self.fare_strategy.calculate_fare(trip)
        trip.fare = fare
        # trip.driver.status = DriverStatus.AVAILABLE
        return fare

    def cancel_trip(self, trip, cancelled_by) -> float:
        fee = self.cancellation_policy.compute_fee(trip, cancelled_by)
        trip.cancel()
        if trip.driver is not None:
            trip.driver.status = DriverStatus.AVAILABLE
        return fee

    # def cancel_trip(self, trip: Trip) -> None:
    #     trip.cancel()
    #     if trip.driver is not None:
    #         trip.driver.status = DriverStatus.AVAILABLE