from enum import Enum
from models import Board
""" Event handler for the Minesweeper game. """


class GameState(Enum):
    win = 1
    lose = 2
    on_going = 3


class Game:

    def __init__(self):
        self.game_state = GameState.on_going
        self.board = Board(rows=10, cols=10)

    def click_square(self, x, y):
        square = self.board.get_square(x, y)
        if square.mine:
            self.game_state = GameState.lose
            return
        square.clicked = True
