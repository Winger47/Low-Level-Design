import time
from enums import VehicleType, SpotType
from models.vehicles import Vehicle
from models.parking_spot import ParkingSpot
from models.parking_floor import ParkingFloor
from models.parking_lot import ParkingLot
from strategies.pricing_strategy import HourlyPricing
from strategies.spot_assignment_strategy import FirstAvailableSpotAssignment
from gates.entry_gate import EntryGate
from gates.exit_gate import ExitGate


def main():
    # 1. Build spots and floor
    spots = [
        ParkingSpot("F1-S01", SpotType.SMALL),
        ParkingSpot("F1-S02", SpotType.MEDIUM),
        ParkingSpot("F1-S03", SpotType.MEDIUM),
        ParkingSpot("F1-S04", SpotType.LARGE),
    ]
    floor = ParkingFloor("F1", spots)

    # 2. Strategies
    pricing = HourlyPricing({
        VehicleType.BIKE: 10.0,
        VehicleType.CAR: 20.0,
        VehicleType.TRUCK: 30.0,
    })
    assigner = FirstAvailableSpotAssignment()

    # 3. Gates
    entry = EntryGate("ENTRY-1", assigner)
    exit_gate = ExitGate("EXIT-1", pricing)

    # 4. The lot
    lot = ParkingLot("LOT-A", [floor], entry, exit_gate)
    print("Initial lot:", lot)

    # 5. Park vehicles
    car = Vehicle("KA-01-CAR", VehicleType.CAR)
    bike = Vehicle("KA-01-BIKE", VehicleType.BIKE)
    truck = Vehicle("KA-01-TRUCK", VehicleType.TRUCK)

    ticket_car = lot.park_vehicle(car)
    print("Parked:", ticket_car)
    ticket_bike = lot.park_vehicle(bike)
    print("Parked:", ticket_bike)
    ticket_truck = lot.park_vehicle(truck)
    print("Parked:", ticket_truck)

    print("After parking:", lot)

    # 6. Wait so duration > 0
    print("Waiting 2 seconds...")
    time.sleep(2)

    # 7. Exit
    payment_car = lot.exit_vehicle(ticket_car)
    print("Exited:", payment_car)
    payment_bike = lot.exit_vehicle(ticket_bike)
    print("Exited:", payment_bike)
    payment_truck = lot.exit_vehicle(ticket_truck)
    print("Exited:", payment_truck)

    print("Final lot:", lot)


if __name__ == "__main__":
    main()