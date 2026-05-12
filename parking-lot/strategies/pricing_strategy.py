
from abc import ABC, abstractmethod
from enums import VehicleType
from models.ticket import Ticket


class PricingStrategy(ABC):
    @abstractmethod
    def calculate(self, ticket:Ticket) -> float:
        """Return the parking fee for the given ticket."""

        

class HourlyPricing(PricingStrategy):
    def __init__(self,rate_per_hour: dict[VehicleType, float]):
        self.rate_per_hour=rate_per_hour

    def calculate(self, ticket:Ticket) -> float:
        hours=ticket.get_duration_hours()
        vehicle_type = ticket.vehicle.vehicle_type
        rate = self.rate_per_hour[vehicle_type]  
        return round(hours * rate, 2)

        