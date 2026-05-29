
from typing import List
from models.snake import Snake
from models.ladder import Ladder



class Board:
    """Represnts the board for the snake and ladder game"""
    def __init__(self,snakes: List[Snake],
     ladders: List[Ladder],
     size:int=100):
        self.snakes=snakes
        self.ladders=ladders
        self.size=size
           


    def get_final_position(self,position: int) -> int:

        if(position>self.size or  position<1):
            raise ValueError("NOT POSSIBLE POSITON")    
        for snakes in self.snakes:
            if snakes.head==position:
                return snakes.tail

        for ladders in self.ladders:
            if ladders.bottom==position:
                return ladders.top

        return position

    def __repr__(self):
        return f"<Board size={self.size} snakes={len(self.snakes)} ladders={len(self.ladders)}>"


        


    