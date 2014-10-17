import unittest
from magic_square import magic_square


class MagicSquareTests(unittest.TestCase):

    def test_true(self):
        self.assertTrue(magic_square([[4, 9, 2],
                                      [3, 5, 7],
                                      [8, 1, 6]]))
        self.assertTrue(magic_square([[7, 12, 1, 14],
                                      [2, 13, 8, 11],
                                      [16, 3, 10, 5],
                                      [9, 6, 15, 4]]))
        self.assertTrue(magic_square([[23, 28, 21],
                                      [22, 24, 26],
                                      [27, 20, 25]]))

    def test_false(self):
        self.assertFalse(magic_square([[1, 2, 3],
                                       [4, 5, 6],
                                       [7, 8, 9]]))
        self.assertFalse(magic_square([[16, 23, 17],
                                       [78, 32, 21],
                                       [17, 16, 15]]))

if __name__ == '__main__':
    unittest.main()
