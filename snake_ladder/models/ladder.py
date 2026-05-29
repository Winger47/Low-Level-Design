

class Ladder:
    """A ladder on the board. Moves player from bottom to top."""
    def __init__(self,top:int,bottom:int):
        self.top=top
        self.bottom=bottom

    def __repr__(self):
        return f"<Ladder top={self.top} bottom={self.bottom}>"    