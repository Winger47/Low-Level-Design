# Tic Tac Toe — Low Level Design (LLD)

A clean, object-oriented implementation of Tic Tac Toe in Python, built as part of a Low-Level Design (LLD) exercise.

## Features

- Configurable board size (default: 3×3)
- Two-player support with custom names and symbols
- Pluggable winning strategies using the **Strategy Design Pattern**
- Detects win, draw, and in-progress states
- Clean separation of concerns across multiple modules

## Project Structure

```
tic-tac/
├── main.py               # Entry point — runs the game
├── game.py               # Game controller (orchestrates moves & status)
├── board.py              # Board model (grid, placement, display)
├── player.py             # Player model (name + symbol)
├── models.py             # Enums: Symbol, GameStatus, Cell
└── winning_strategies.py # Strategy Pattern: Row, Col, Diagonal checks
```

## Design Patterns Used

### Strategy Pattern
Winning logic is encapsulated in separate strategy classes, all implementing the `WinningStrategy` abstract base class:

| Strategy              | Description                          |
|-----------------------|--------------------------------------|
| `RowWinningStrategy`  | Checks if any row is fully owned     |
| `ColWinningStrategy`  | Checks if any column is fully owned  |
| `DiagonalWinningStrategy` | Checks main and anti diagonals   |

Adding a new winning condition is as simple as creating a new strategy class — no changes needed in `Game`.

## How to Run

```bash
python3 main.py
```

### Example Gameplay

```
Welcome to Tic Tac Toe!
  |   |   |
  |   |   |
  |   |   |

Alice's Turn (Symbol: x)
Enter row (0, 1, or 2): 0
Enter col (0, 1, or 2): 0

x |   |   |
  |   |   |
  |   |   |
...
GAME OVER! Winner is Alice!
```

## Requirements

- Python 3.7+
- No external dependencies

## Game Status Values

| Status        | Meaning                  |
|---------------|--------------------------|
| `IN_PROGRESS` | Game is still running    |
| `DRAW`        | Board is full, no winner |
| `X_WINS`      | Player with X won        |
| `Y_WINS`      | Player with O won        |
