from enums import Direction


class HallCall:
    def __init__(self, floor: int, direction: Direction):
        self.floor = floor
        self.direction = direction

    def __repr__(self) -> str:
        return f"HallCall(floor={self.floor}, direction={self.direction.name})"