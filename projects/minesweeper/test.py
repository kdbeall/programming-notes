""" Tests for models.py """

import unittest
from models import Square


class TestSquare(unittest.TestCase):

    def test_square(self):
        """ Tests the Square class. """
        square = Square(False)
        self.assertTrue(True, square.has_mine)


if __name__ == '__main__':
    unittest.main()
