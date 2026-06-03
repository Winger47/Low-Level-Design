



from models.show import Show
from models.movie import Movie  
from models.booking import Booking  
from models.seat import Seat
from typing import Optional  
class ShowService:
    def __init__(self,shows:list[Show]):
        self.shows=shows
    
    def search_shows(self,city:str,movie_name:str, theater_id: Optional[int] = None)->list[Show]:

        found_shows=[]
        for show in self.shows:
            if show.screen.theater.city==city and show.movie.name==movie_name:
                if theater_id is None or show.screen.theater.theater_id == theater_id:
                    found_shows.append(show)
        return found_shows        
    
    def get_show(self,show_id:int)->Show:
        for show in self.shows:
            if show_id==show.show_id:
                return show
        raise ValueError(f"Show {show_id} not found")

    
    def get_seats(self,show:Show)->list[Seat]:
            return show.screen.seats
    