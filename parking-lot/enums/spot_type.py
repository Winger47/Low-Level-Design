from enum import Enum


class SpotType(Enum):
    """
    Size category of a parking spot.
    
    Compatibility rule: a spot can fit a vehicle whose required size
    is equal to or smaller than the spot. Larger spots are more permissive.
    
    SMALL  -> bikes only
    MEDIUM -> bikes, cars
    LARGE  -> bikes, cars, trucks
    """
    SMALL = "SMALL"
    MEDIUM = "MEDIUM"
    LARGE = "LARGE"