from models import Symbol
class Player():
    def __init__(self,name:str,symbol:Symbol):
        self.name=name
        self.symbol=symbol

    def getName(self):
        return self.name

    def getSymbol(self):
        return self.symbol

