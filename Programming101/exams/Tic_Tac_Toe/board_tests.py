import unittest
from board import Board


class BoardTests(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def __fill_rows(self, rows):
        for row in rows:
            for col in range(3):
                self.board.make_move(Board.USER, row, col)

    def test_is_user_turn(self):
        self.assertTrue(self.board.is_user_turn)
        self.board.make_move(Board.USER, 1, 1)
        self.assertFalse(self.board.is_user_turn)

    def test_make_move(self):
        self.__fill_rows(range(1))
        self.assertEqual(self.board.state[0], [Board.USER]*3)

    def test_is_pos_empty(self):
        self.assertTrue(self.board.is_pos_empty(0, 0))
        self.board.make_move(Board.AI, 0, 0)
        self.assertFalse(self.board.is_pos_empty(0, 0))

    def test_get_available_moves(self):
        self.__fill_rows(range(1))
        result = []
        for row in range(1, 3):
            for col in range(0, 3):
                result.append((row, col))
        self.assertEqual(self.board.get_available_moves(), result)

    def test_is_complete(self):
        self.assertFalse(self.board.is_complete())
        self.__fill_rows(range(3))
        self.assertTrue(self.board.is_complete())


if __name__ == '__main__':
    unittest.main()
