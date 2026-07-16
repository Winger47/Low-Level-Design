from enums import Direction, ElevatorState


class Elevator:
    def __init__(self, car_id: int, current_floor: int = 0):
        self.car_id = car_id
        self.current_floor = current_floor
        self.direction = Direction.IDLE
        self.targets = set()          # floors this car must stop at

    def add_target(self, floor: int):
        self.targets.add(floor) 
        # TODO(you): add floor to targets

    def step(self):
        if not self.targets:
            self.direction=Direction.IDLE
            return
        if self.current_floor in self.targets:
            self.targets.remove(self.current_floor)
            self.direction=Direction.IDLE
            return
        self._update_direction()
        self.current_floor+=self.direction.value    
        # Case 1: no targets → go IDLE, return
        # Case 2: at a target floor → open doors, remove it, return (doors take the tick)
        # Case 3: keep moving → set direction (LOOK), then current_floor += direction.value

    def _update_direction(self):
        if self.direction==Direction.UP:
            if any(t>self.current_floor for t in self.targets):
                self.direction=Direction.UP
            else:
                self.direction=Direction.DOWN
        elif self.direction==Direction.DOWN:
            if any(t<self.current_floor for t in self.targets):
                self.direction=Direction.DOWN
            else:
                self.direction=Direction.UP
        else:
            if any(t>self.current_floor for t in self.targets):
                self.direction=Direction.UP
            elif any(t<self.current_floor for t in self.targets):
                self.direction=Direction.DOWN
            else:
                self.direction=Direction.IDLE

        # ⭐ THE LOOK LOGIC — the hard part
        # if going UP: stay UP if any target is above, else flip DOWN
        # if going DOWN: stay DOWN if any target is below, else flip UP
        # if IDLE: pick UP if target above, else DOWN