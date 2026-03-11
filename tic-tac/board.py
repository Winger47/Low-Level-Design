from typing import List
from models import Cell,Symbol


class Board():
    def __init__(self,size :int):
        self.size=size
        self.movesCount=0
        self.board=[]

        self.intializeBoard()

    def intializeBoard(self):
        for i in range(self.size):  
            row=[Cell() for _ in range(self.size)]
            self.board.append(row)
    def getCell(self,row:int ,col:int,)->Cell:
        return self.board[row][col]
    def placeSymbol(self,row:int ,col:int,symbol:Symbol)->bool:
        if row>=0 and row<self.size and col>=0 and col<self.size:
            if self.getCell(row,col).symbol==Symbol.EMPTY:
                self.getCell(row,col).symbol=symbol 
                self.movesCount+=1
                return True
            else: return False   
        else: return False
    def isFull(self)->bool:
        return self.movesCount==self.size*self.size 
    def printBoard(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.board[i][j].symbol.value,end=" | ")
            print()

