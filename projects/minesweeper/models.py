""" Data models for a Minesweeper CLI game. """

import random


class Board:
    """ Represents a board with squares. """

    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self._create_squares(self.cols, self.rows)

    def _create_squares(self, cols, rows):
        self.squares = [[Square(has_mine=False)
                        for _ in range(cols)] for _ in range(rows)]

    def _is_mine(self, percent):
        return random.randrange(100) < percent

    def get_square(self, x, y):
        return self.squares[x][y]


class Square:
    """
        Represents a single square in the minesweeper board.
        A square may have or may not have a mine, may be clicked or unclicked.
    """
    def __init__(self, has_mine):
        self.has_mine = has_mine
        self.clicked = False
