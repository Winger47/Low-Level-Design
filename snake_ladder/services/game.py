
from typing import Optional
from models.board import Board
from models.player import Player
from models.dice import Dice
from enums import GameState


class Game:
    def __init__(self,board:Board,players:list[Player],dice:Dice):
        self.board=board
        self.players=players
        self.dice=dice
        self.current_player_idx=0
        self.state=GameState.NOT_STARTED
        self.winner= None

    def start(self)->None:
        if self.state==GameState.NOT_STARTED:

            self.state=GameState.IN_PROGRESS
        while self.state == GameState.IN_PROGRESS:
            self.play_turn()

        print(f"Winner is {self.winner}")
    def play_turn(self)->None:
        if self.state != GameState.IN_PROGRESS:
            raise ValueError("game is not in progress")
        player=self.players[self.current_player_idx]
        dice_roll=self.dice.roll()
        new_position=player.position+dice_roll

        if new_position>self.board.size:
            print(f"{player.name} rolled a {dice_roll} but can't move")
            self.next_player()
            return
        # player.move_to(new_position)
        print(f"{player.name} rolled a {dice_roll} and moved to {new_position}")
        
        final_position=self.board.get_final_position(new_position)
        player.move_to(final_position)
        if final_position != new_position:
            print(f"{player.name} encountered a snake/ladder and moved to {final_position}")    
            
        if final_position==self.board.size:
            self.state=GameState.FINISHED
            self.winner=player
            return  

        self.next_player()  
    def next_player(self)-> None:
        self.current_player_idx=(self.current_player_idx+1) % len(self.players)     

    def __repr__(self):
        return f"<Game state={self.state} current_player_idx={self.current_player_idx} winner={self.winner}>"
            

     

    
