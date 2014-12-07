import unittest
from board import Board


class BoardTests(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_is_user_turn(self):
        self.assertTrue(self.board.is_user_turn)
        self.board.make_move(Board.USER, 1, 1)
        self.assertFalse(self.board.is_user_turn)

    def test_make_move(self):
        for i in range(3):
            self.board.make_move(Board.USER, 0, i)
        self.assertEqual(self.board.state[0], [Board.USER]*3)

    def test_is_pos_empty(self):
        self.assertTrue(self.board.is_pos_empty(0, 0))
        self.board.make_move(Board.AI, 0, 0)
        self.assertFalse(self.board.is_pos_empty(0, 0))

if __name__ == '__main__':
    unittest.main()
