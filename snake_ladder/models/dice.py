
import random
class Dice:
    """ Represnts The Dice."""
    def __init__(self,faces: int=6  ):
        if faces <1:
            raise ValueError("Faces must be positive")
        self.faces=faces    

    def roll(self) -> int:
        """ Returns The Random Number between 1 to faces."""
        return random.randint(1,self.faces)    
    
    def __repr__(self):
        return f"<Dice faces={self.faces}>"
    

