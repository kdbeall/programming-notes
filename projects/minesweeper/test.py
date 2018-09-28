"""
    Tests for models.py,
    run with python3 -m unittest -v test.py
"""

import unittest
from models import Square, Board
from game import Game


class TestSquare(unittest.TestCase):

    def test_square__init__(self):
        """ Tests the Square __init__. """
        square = Square(False)
        self.assertFalse(square.mine)
        self.assertFalse(square.clicked)
        square = Square(True)
        self.assertTrue(square.mine)
        self.assertFalse(square.clicked)


class TestBoard(unittest.TestCase):

    def test_board__init__(self):
        board = Board(3, 3)
        self.assertEqual(3, board.cols)
        self.assertEqual(3, board.rows)

    def test_board__init__percentage(self):
        """ Tests mine percentages are calculated correctly. """
        rows = 5
        cols = 5
        max_mines = (cols-1)*(rows-1)
        mines_percent = 100 * max_mines / (rows*cols)
        self.assertEqual(64, mines_percent)

    def test_board_get_square(self):
        board = Board(3, 3)
        self.assertFalse(board.get_square(0, 0).clicked)


class TestGame(unittest.TestCase):
    def test_game__init__(self):
        game = Game()
        self.assertEqual(10, game.board.rows)
        self.assertEqual(10, game.board.cols)


if __name__ == '__main__':
    unittest.main()
