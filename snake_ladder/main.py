from models.snake import Snake
from models.ladder import Ladder
from models.player import Player
from models.dice import Dice
from models.board import Board
from services.game import Game


def main():
    # Build the board
    snakes = [
        Snake(99, 24),
        Snake(80, 12),
        Snake(54, 6),
    ]
    ladders = [
        Ladder(30, 10),    # bottom=10, top=30  (note: your Ladder is (top, bottom) — adjust if needed)
        Ladder(60, 40),
        Ladder(95, 75),
    ]
    board = Board(snakes, ladders, size=100)

    # Players
    players = [
        Player("Alice"),
        Player("Bob"),
    ]

    # Dice
    dice = Dice()

    # Game
    game = Game(board, players, dice)
    game.start()


if __name__ == "__main__":
    main()