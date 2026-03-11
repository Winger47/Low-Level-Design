from board import Board
from player import Player
from models import Symbol
from winning_strategies import RowWinningStrategy,ColWinnnigStrategy,DiagonalWinningStrategy
from typing import List
from models import GameStatus


class Game():
    def __init__(self, size:int , players:List[Player]):
        self.board=Board(size)
        self.players=players

        self.winningStrategies=[RowWinningStrategy(),ColWinnnigStrategy(),DiagonalWinningStrategy()]


        self.currentPlayerNumber=0
        self.status=GameStatus.INT_PROGRESS
        self.winner=None
    

    def makeMove(self,row:int ,col:int,)->None:

        if self.status!=GameStatus.INT_PROGRESS:
            return False
        
        currentPlayer=self.players[self.currentPlayerNumber]

        success=self.board.placeSymbol(row,col,currentPlayer.getSymbol())

        if(success==False): return False   


        for strategy in self.winningStrategies:
            var=False
            if(strategy.checkWinner(self.board,currentPlayer)):
                self.winner=currentPlayer
                if currentPlayer.getSymbol().value == "x":
                    self.status = GameStatus.X_WINS
                else:
                    self.status = GameStatus.Y_WINS
                return

        var=self.board.isFull()
        if(var==True):
            self.status=GameStatus.DRAW
            return
        self.currentPlayerNumber=(self.currentPlayerNumber+1)%2
        




