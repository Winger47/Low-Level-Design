from enum import Enum,auto

class Symbol(Enum):
    X = "x"
    O = "0"
    EMPTY = " "


class GameStatus(Enum):
    INT_PROGRESS=auto()
    DRAW=auto()
    X_WINS=auto()
    Y_WINS=auto()
class Cell:
    def __init__(self):
        self._symbol = Symbol.EMPTY
    
    def EmptyCell(self):
        return self._symbol == Symbol.EMPTY

    @property
    def symbol(self):
        return self._symbol
        
    @symbol.setter
    def symbol(self, symbol):
        self._symbol = symbol
