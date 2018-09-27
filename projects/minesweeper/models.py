""" Data models for a Minesweeper CLI game. """


class Board:
    """ Represents a board with squares. """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__create_squares(self.x, self.y)

    def __create_squares(self, x, y):
        self.squares = []
        return


class Square:
    """
        Represents a single square in the minesweeper board.
        A square may have or may not have a mine, may be clicked or unclicked.
    """
    def __init__(self, has_mine):
        self.has_mine = has_mine
        self.clicked = False
