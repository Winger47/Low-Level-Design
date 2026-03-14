from models import Symbol, GameStatus
from player import Player
from game import Game

def test_game():
    # 1. Create your two players
    player1 = Player("Alice", Symbol.X)
    player2 = Player("Bob", Symbol.O)
    
    # 2. Initialize the game with size 3 and the list of players
    game = Game(3, [player1, player2])
    print("Welcome to Tic Tac Toe!")
    game.board.printBoard()
    
    # 3. Game Loop
    # We keep running this loop as long as the status is INT_PROGRESS
    while game.status == GameStatus.INT_PROGRESS:
        
        # Get whose turn it is
        current_player = game.players[game.currentPlayerNumber]
        print(f"\n{current_player.name}'s Turn (Symbol: {current_player.symbol.value})")
        
        # Ask the user for input
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter col (0, 1, or 2): "))
        except ValueError:
            print("Please enter valid numbers.")
            continue
            
        # Try to make the move in your Game controller
        success = game.makeMove(row, col)
        
        # Check if they inputted an invalid square
        if success == False:
            print("Invalid Move! That space is taken or out of bounds. Try again.")
            continue
            
        # Print the board beautifully so they can see the result
        game.board.printBoard()

    # 4. End Game Messages
    if game.status == GameStatus.DRAW:
        print("\nThe game ended in a DRAW!")
    else:
        print(f"\nGAME OVER! Winner is {game.winner.name}!")

if __name__ == "__main__":
    test_game()

