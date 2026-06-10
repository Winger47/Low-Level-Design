import math

class Location():
    """Represents the geographical coordinates of a location."""

    def __init__(self,latitude:float,longitude:float):
        self.latitude=latitude
        self.longitude=longitude
    
    def distance_to(self, other: "Location") -> float:
        return math.sqrt(
            (self.latitude - other.latitude) ** 2
            + (self.longitude - other.longitude) ** 2
        )

    def __repr__(self):
      return f"Location(lat={self.latitude}, lng={self.longitude})"

      


    

    