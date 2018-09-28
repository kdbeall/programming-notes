"""
    Tests for models.py,
    run with python3 -m unittest -v test.py
"""

import unittest
from models import Square, Board


class TestSquare(unittest.TestCase):

    def test_square__init__(self):
        """ Tests the Square __init__. """
        square = Square(False)
        self.assertFalse(square.has_mine)
        self.assertFalse(square.clicked)
        square = Square(True)
        self.assertTrue(square.has_mine)
        self.assertFalse(square.clicked)


class TestBoard(unittest.TestCase):

    def test_board__init__(self):
        """ Tests the Board __init__. """
        board = Board(3, 3)
        self.assertEqual(3, board.cols)
        self.assertEqual(3, board.rows)

    def test_board_get_square(self):
        board = Board(3, 3)
        self.assertFalse(board.get_square(0, 0).clicked)


if __name__ == '__main__':
    unittest.main()
