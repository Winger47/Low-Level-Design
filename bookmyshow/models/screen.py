from typing import TYPE_CHECKING
from models.seat import Seat

if TYPE_CHECKING:
    from models.theater import Theater

class Screen:

    def __init__(self,screen_id:int,name:str,rows:int,cols:int,theater:"Theater",seats:list["Seat"]):
        self.screen_id=screen_id
        self.name=name  
        self.rows=rows
        self.cols=cols
        self.theater=theater
        self.seats=seats    

    def __repr__(self):
        return f"Screen(screen_id={self.screen_id},name={self.name})" 
        