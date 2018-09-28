""" Data models for a Minesweeper CLI game. """

import random


class Board:
    """ Represents a board with squares. """

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.number_of_mines = 0
        self.max_mines = (cols-1)*(rows-1)
        mines_percentage = 100 * self.max_mines / (rows*cols)
        self._create_squares(self.cols, self.rows, mines_percentage)

    def _create_squares(self, cols, rows, mines_percentage):
        """
            Create a grid of squares of size rows by cols.
        """
        self.squares = [[Square(mine=self._is_mine(mines_percentage))
                        for _ in range(cols)] for _ in range(rows)]

    def _is_mine(self, mines_percentage):
        """ Determine if a square is a mine. """
        is_mine = random.randrange(100) < mines_percentage
        if is_mine:
            if self.number_of_mines >= self.max_mines:
                return False
            self.number_of_mines = self.number_of_mines + 1
            return True
        return False

    def get_square(self, x, y):
        """ Return the square at row x column y. """
        return self.squares[x][y]


class Square:
    """
        Represents a single square in the minesweeper board.
        A square may have or may not have a mine, may be clicked or unclicked.
    """
    def __init__(self, mine):
        self.mine = mine
        self.clicked = False
