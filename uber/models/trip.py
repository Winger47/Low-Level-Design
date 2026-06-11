

from models.rider import Rider
from models.location import Location
from models.driver import Driver
from enums import TripStatus
import random
class Trip:
    def __init__(self,trip_id:int,rider:Rider,pickup_location:Location,dropoff_location:Location):
        self.trip_id=trip_id
        self.rider=rider
        self.pickup_location=pickup_location
        self.dropoff_location=dropoff_location
    
        self.status=TripStatus.REQUESTED
        self.driver=None
        self.fare=0.0
        self.otp=None


    def assign_driver(self,driver:Driver):
        if self.status!=TripStatus.REQUESTED:
            raise Exception("Trip already assigned")
        if self.driver!=None:
            raise Exception("Driver already assigned")  
        self.driver=driver
        self.otp = random.randint(1000, 9999)
        self.status=TripStatus.ACCEPTED 
        
    def start(self,otp:int):
        if self.status!=TripStatus.ACCEPTED:
            raise Exception("Driver not assigned")
        if self.otp!=otp:
            raise Exception("Invalid OTP")
        self.status=TripStatus.ONGOING
    def complete(self):
        if self.status!=TripStatus.ONGOING:
            raise Exception("Trip not started")
        self.status=TripStatus.COMPLETED

    def cancel(self):
        if self.status==TripStatus.COMPLETED or self.status==TripStatus.CANCELLED:
            raise Exception("Trip is completed or cancelled")
        self.status=TripStatus.CANCELLED

    def __repr__(self):
        driver_name = self.driver.name if self.driver else "None"
        return (f"Trip(id={self.trip_id}, rider={self.rider.name}, "
                f"driver={driver_name}, status={self.status.name}, fare={self.fare})")

    

    