"""
Uber LLD — End-to-end demo.

Builds a world of many drivers and riders, then runs through every
scenario the system supports:
  1. Happy path (request -> start -> complete -> pay)
  2. Nearest-driver matching (closest of several is chosen)
  3. Vehicle-type filtering (BIKE request skips CARs)
  4. Driver held ON_TRIP until payment settles
  5. Cancellation with fee policy
  6. No-driver-available failure
  7. Concurrency: two riders racing for the last driver
  8. Ratings after trips
"""

import threading

from models.rider import Rider
from models.driver import Driver
from models.vehicle import Vehicle
from models.location import Location
from enums import VehicleType, DriverStatus
from exceptions import NoDriverAvailableError
from services.matching_service import MatchingService
from services.trip_service import TripService
from services.payment_service import PaymentService
from strategies.fare_strategy import DistanceTimeFareStrategy
from strategies.cancellation_policy import TimeBasedCancellationPolicy


# ----------------------------------------------------------------------
# World setup
# ----------------------------------------------------------------------
def build_world():
    matching_service = MatchingService()

    # A fleet of drivers spread across the map, mixed vehicle types.
    drivers = [
        Driver(1, "Bob",    Vehicle(1, "UP80-AB-1111", VehicleType.CAR),     Location(5, 5)),
        Driver(2, "Sam",    Vehicle(2, "UP80-AB-2222", VehicleType.CAR),     Location(1, 1)),
        Driver(3, "Raj",    Vehicle(3, "UP80-AB-3333", VehicleType.BIKE),    Location(2, 2)),
        Driver(4, "Asha",   Vehicle(4, "UP80-AB-4444", VehicleType.CAR),     Location(8, 8)),
        Driver(5, "Kiran",  Vehicle(5, "UP80-AB-5555", VehicleType.AUTO),    Location(3, 1)),
        Driver(6, "Meera",  Vehicle(6, "UP80-AB-6666", VehicleType.PREMIUM), Location(10, 10)),
        Driver(7, "Vik",    Vehicle(7, "UP80-AB-7777", VehicleType.BIKE),    Location(0, 1)),
        Driver(8, "Nina",   Vehicle(8, "UP80-AB-8888", VehicleType.CAR),     Location(2, 3)),
    ]
    for d in drivers:
        d.go_online()
        matching_service.add_driver(d)

    trip_service = TripService(
        matching_service,
        DistanceTimeFareStrategy(),
        TimeBasedCancellationPolicy(),
    )
    payment_service = PaymentService()

    riders = [
        Rider(1, "Alice"),
        Rider(2, "Bobby"),
        Rider(3, "Charu"),
        Rider(4, "Dev"),
        Rider(5, "Esha"),
    ]

    return riders, drivers, matching_service, trip_service, payment_service


# ----------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------
def run_full_ride(rider, pickup, drop, vehicle_type, trip_service, payment_service):
    """Request -> start -> complete -> pay, with prints at each step."""
    trip = trip_service.request_trip(rider, pickup, drop, vehicle_type)
    print(f"  requested  -> {trip.driver.name} assigned "
          f"({trip.driver.vehicle.vehicle_type.name}) | OTP={trip.otp} | {trip.status.name}")

    trip_service.start_trip(trip, trip.otp)
    print(f"  started    -> {trip.status.name}")

    fare = trip_service.complete_trip(trip)
    print(f"  completed  -> fare=₹{fare:.2f} | driver={trip.driver.status.name} (held)")

    payment = payment_service.process_payment(trip)
    print(f"  paid       -> {payment} | driver={trip.driver.status.name} (freed)")

    # both rate each other
    trip.driver.add_rating(5)
    trip.rider.add_rating(4)
    print(f"  rated      -> driver {trip.driver.name} {trip.driver.avg_rating:.1f}* | "
          f"rider {trip.rider.name} {trip.rider.avg_rating:.1f}*")
    return trip


# ----------------------------------------------------------------------
# Scenarios
# ----------------------------------------------------------------------
def scenario_happy_paths(riders, trip_service, payment_service):
    print("\n=== 1. Multiple riders, full ride each ===")

    print("\nAlice wants a CAR from (0,0) -> (3,4):")
    run_full_ride(riders[0], Location(0, 0), Location(3, 4),
                  VehicleType.CAR, trip_service, payment_service)

    print("\nCharu wants a BIKE from (0,0) -> (5,5):")
    run_full_ride(riders[2], Location(0, 0), Location(5, 5),
                  VehicleType.BIKE, trip_service, payment_service)

    print("\nDev wants an AUTO from (3,0) -> (6,2):")
    run_full_ride(riders[3], Location(3, 0), Location(6, 2),
                  VehicleType.AUTO, trip_service, payment_service)

    print("\nEsha wants a PREMIUM from (9,9) -> (12,12):")
    run_full_ride(riders[4], Location(9, 9), Location(12, 12),
                  VehicleType.PREMIUM, trip_service, payment_service)


def scenario_nearest_match(riders, trip_service, payment_service):
    print("\n=== 2. Nearest CAR is chosen ===")
    # Available CARs after scenario 1: Bob(5,5), Asha(8,8), Nina(2,3) -- Sam was used & freed too
    # From pickup (2,2), Nina(2,3) should be closest.
    trip = trip_service.request_trip(riders[1], Location(2, 2), Location(4, 4), VehicleType.CAR)
    print(f"  Bobby from (2,2) -> matched {trip.driver.name} at {trip.driver.location} "
          f"(nearest available CAR)")
    trip_service.start_trip(trip, trip.otp)
    trip_service.complete_trip(trip)
    payment_service.process_payment(trip)


def scenario_cancellation(riders, trip_service):
    print("\n=== 3. Cancellation (within free window -> no fee) ===")
    trip = trip_service.request_trip(riders[0], Location(1, 1), Location(2, 2), VehicleType.CAR)
    print(f"  requested -> {trip.driver.name} assigned | driver={trip.driver.status.name}")
    fee = trip_service.cancel_trip(trip, cancelled_by="rider")
    print(f"  cancelled -> {trip.status.name} | fee=₹{fee:.2f} | "
          f"driver={trip.driver.status.name} (freed)")


def scenario_no_driver(riders, trip_service):
    print("\n=== 4. No driver available (all PREMIUM busy/none) ===")
    # Meera is the only PREMIUM; if she's mid-trip or none match, this fails.
    # Request PREMIUM far from any premium driver after Meera is used.
    try:
        trip_service.request_trip(riders[1], Location(0, 0), Location(1, 1), VehicleType.PREMIUM)
        print("  unexpectedly matched a driver")
    except NoDriverAvailableError as e:
        print(f"  failed as expected -> {e}")


def scenario_concurrency(matching_service, trip_service):
    print("\n=== 5. Concurrency: two riders race for the LAST car ===")

    # Put the system in a state with exactly ONE available CAR.
    cars = [d for d in matching_service.drivers
            if d.vehicle.vehicle_type == VehicleType.CAR]
    # Force all CARs offline except one.
    last_car = None
    for d in cars:
        if d.is_available() and last_car is None:
            last_car = d
        else:
            d.go_offline()
    if last_car is None:
        # none were available; bring one back online for the demo
        last_car = cars[0]
        last_car.go_online()
        last_car.status = DriverStatus.AVAILABLE
    print(f"  only available CAR: {last_car.name} at {last_car.location}")

    results = []

    def grab(rider_name):
        try:
            t = trip_service.request_trip(
                Rider(99, rider_name), Location(0, 0), Location(1, 1), VehicleType.CAR
            )
            results.append(f"{rider_name} GOT {t.driver.name}")
        except NoDriverAvailableError:
            results.append(f"{rider_name} FAILED (no car)")

    t1 = threading.Thread(target=grab, args=("RiderX",))
    t2 = threading.Thread(target=grab, args=("RiderY",))
    t1.start(); t2.start()
    t1.join(); t2.join()

    for r in results:
        print(f"  {r}")
    print("  -> exactly one rider gets the car; the lock prevents double-booking")


def main():
    riders, drivers, matching_service, trip_service, payment_service = build_world()

    print("World built:")
    print(f"  {len(drivers)} drivers online, {len(riders)} riders")

    scenario_happy_paths(riders, trip_service, payment_service)
    scenario_nearest_match(riders, trip_service, payment_service)
    scenario_cancellation(riders, trip_service)
    scenario_no_driver(riders, trip_service)
    scenario_concurrency(matching_service, trip_service)

    print("\n=== Done ===")


if __name__ == "__main__":
    main()