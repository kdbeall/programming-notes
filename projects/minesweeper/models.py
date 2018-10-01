""" Data models for a Minesweeper CLI game. """

import random
import itertools

class Board:
    """ Represents a board with squares. """

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.number_of_mines = 0
        self.max_mines = (cols-1)*(rows-1)
        mines_percentage = 100 * self.max_mines / (rows*cols)
        self.__create_squares(self.cols, self.rows, mines_percentage)

    def get_square(self, row, col):
        """ Return the square at the given row and column."""
        return self.squares[row][col]

    def print_board(self):
        pass

    def __create_squares(self, cols, rows, mines_percentage):
        """
            Create a grid of squares of size rows by cols.
        """
        self.squares = [[Square(self, row, col, mine=self.__is_mine(mines_percentage))
                        for col in range(cols)] for row in range(rows)]

    def __is_mine(self, mines_percentage):
        """ Determine if a square is a mine while generating the board. """
        is_mine = random.randrange(100) < mines_percentage
        if is_mine:
            if self.number_of_mines >= self.max_mines:
                return False
            self.number_of_mines = self.number_of_mines + 1
            return True
        return False
       


class Square:
    """
        Represents a single square in the minesweeper board.
        A square may have or may not have a mine, may be clicked or unclicked.
    """
    def __init__(self, board, row, col, mine):
        self.board = board
        self.row = row
        self.col = col
        self.mine = mine
        self.clicked = False

    def neighbors(self):
        row_neighbors = list(filter(lambda val: val >= 0 and val < self.board.rows, [self.row-1, self.row, self.row+1])) 
        col_neighbors = list(filter(lambda val: val >= 0 and val < self.board.cols, [self.col-1, self.col, self.col+1]))
        return set(itertools.product(row_neighbors, col_neighbors)).remove((self.row, self.col))