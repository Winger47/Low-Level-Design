
from exceptions import NoDriverAvailableError
from models.driver import Driver
from models.location import Location
from enums import VehicleType
class MatchingService:
    def __init__(self): 
        self.drivers=[]
    
    def add_driver(self,driver:Driver):
        self.drivers.append(driver)
    
    def find_nearest_driver(self,pickup:Location,vehicleType:VehicleType):

        nearest_driver=None
        min_dist=float("inf")

        for driver in self.drivers:
            if driver.vehicle.vehicle_type==vehicleType and driver.is_available():
                dist=pickup.distance_to(driver.location)
                if dist < min_dist:
                    min_dist=dist
                    nearest_driver=driver
        if nearest_driver is None:
            raise NoDriverAvailableError(f"No {vehicleType.name} driver available near pickup")
        return nearest_driver