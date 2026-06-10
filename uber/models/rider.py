from enums import VehicleType
class Rider:
    def __init__(self, rider_id: int, name: str):
        self.rider_id = rider_id
        self.name = name
        self.rating_sum = 0.0
        self.rating_count = 0          # int, not 0.0

    def add_rating(self, rating: float) -> None:
        self.rating_sum += rating
        self.rating_count += 1

    @property
    def avg_rating(self) -> float:
        if self.rating_count == 0:
            return 0.0
        return self.rating_sum / self.rating_count

    def __repr__(self):
        return f"Rider(id={self.rider_id}, name={self.name}, rating={self.avg_rating:.1f})"

