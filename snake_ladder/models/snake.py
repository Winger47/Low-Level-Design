

class Snake:
    """A snake on the board. Moves player from head down to tail."""
    def __init__(self,head:int,tail:int):
        self.head=head
        self.tail=tail

    def __repr__(self):
        return f"<Snake head={self.head} tail={self.tail}>"

