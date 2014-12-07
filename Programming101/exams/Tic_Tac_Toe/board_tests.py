import unittest
from board import Board


class BoardTests(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_is_user_turn(self):
        self.assertTrue(self.board.is_user_turn)
        self.board.make_move(Board.USER, 1, 1)
        self.assertFalse(self.board.is_user_turn)

if __name__ == '__main__':
    unittest.main()
