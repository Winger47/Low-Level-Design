from datetime import datetime
from models.movie import Movie
from models.screen import Screen


class Show:
    def __init__(self,show_id:int,movie:Movie,screen:Screen,start_time:datetime,end_time:datetime):
        self.show_id = show_id
        self.movie = movie
        self.screen = screen
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return f"Show(show_id={self.show_id}, movie={self.movie.name}, screen={self.screen.name}, start={self.start_time})"