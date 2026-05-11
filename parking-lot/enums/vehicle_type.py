from enum import Enum

class VehicleType(Enum):
    """Type of vehicle. Determines spot compatibility and pricing tier."""

    CAR="CAR"
    BIKE="BIKE"
    TRUCK="TRUCK"