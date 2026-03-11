from models import Symbol
from abc import ABC, abstractmethod
from board import Board
from player import Player

class WinningStrategy(ABC):

    @abstractmethod
    def checkWinner(self, board: Board, player: Player) -> bool:
        pass


class RowWinningStrategy(WinningStrategy):


    def checkWinner(self,board:Board,player:Player)->bool:

        for i in range(board.size):
            if board.getCell(i,0).symbol==player.symbol and board.getCell(i,1).symbol==player.symbol and board.getCell(i,2).symbol==player.symbol:
                return True
        return False

    
    
        
class ColWinnnigStrategy(WinningStrategy):
    def checkWinner(self,board:Board,player:Player)->bool:

        for i in range(board.size):
            if board.getCell(0,i).symbol==player.symbol and board.getCell(1,i).symbol==player.symbol and board.getCell(2,i).symbol==player.symbol:
                return True
        return False
class DiagonalWinningStrategy(WinningStrategy):
    
    def checkWinner(self, board: Board, player: Player) -> bool:
        
        # 1. Check Main Diagonal (Top-Left to Bottom-Right)
        won_main = True 
        for i in range(board.size):
            if board.getCell(i, i).symbol != player.symbol:
                won_main = False 
                break
        
        if won_main:
            return True
            
        # 2. Check Anti-Diagonal (Top-Right to Bottom-Left)
        won_anti = True 
        for i in range(board.size):
            col = (board.size - 1) - i
            
            if board.getCell(i, col).symbol != player.symbol:
                won_anti = False 
                break
                
        if won_anti:
            return True
            
        return False
