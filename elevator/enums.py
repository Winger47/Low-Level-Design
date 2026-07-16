from enum import Enum

class Direction(Enum):
    UP=1
    DOWN=-1
    IDLE=0

class ElevatorState(Enum):
    IDLE="IDLE"
    MOVING="MOVING"
    DOORS_OPEN="DOORS_OPEN"



