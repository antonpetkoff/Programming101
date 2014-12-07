import unittest
from random import randint
from board import Board


class BoardTests(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def __fill_rows(self, rows, mark):
        for row in rows:
            for col in range(3):
                self.board.make_move(mark, row, col)

    def test_is_user_turn(self):
        self.assertTrue(self.board.is_user_turn)
        self.board.make_move(Board.USER, 1, 1)
        self.assertFalse(self.board.is_user_turn)

    def test_make_move(self):
        self.__fill_rows(range(1), Board.USER)
        self.assertEqual(self.board.state[0], [Board.USER]*3)

    def test_is_pos_empty(self):
        self.assertTrue(self.board.is_pos_empty(0, 0))
        self.board.make_move(Board.AI, 0, 0)
        self.assertFalse(self.board.is_pos_empty(0, 0))

    def test_get_available_moves(self):
        self.__fill_rows(range(1), Board.USER)
        result = []
        for row in range(1, 3):
            for col in range(0, 3):
                result.append((row, col))
        self.assertEqual(self.board.get_available_moves(), result)

    def test_is_complete(self):
        self.assertFalse(self.board.is_complete())
        self.__fill_rows(range(3), Board.USER)
        self.assertTrue(self.board.is_complete())

    def test_has_3_equal_marks_all_outcomes(self):
        self.assertEqual(self.board._has_3_equal_marks(self.board.state[0]),
                         None)

        self.__fill_rows(range(1), Board.USER)
        self.assertEqual(self.board._has_3_equal_marks(self.board.state[0]),
                         Board.USER_WIN)

        self.__fill_rows(range(1), Board.AI)
        self.assertEqual(self.board._has_3_equal_marks(self.board.state[0]),
                         Board.AI_WIN)

    def test_is_game_over_all_outcomes_rows(self):
        self.assertEqual(self.board.is_game_over(), Board.NOT_OVER)

        self.__fill_rows(range(1), Board.USER)
        self.assertEqual(self.board.is_game_over(), Board.USER_WIN)

        self.__fill_rows(range(1), Board.AI)
        self.assertEqual(self.board.is_game_over(), Board.AI_WIN)

        self.board.state = [[Board.USER, Board.USER, Board.AI],
                            [Board.AI,   Board.AI,   Board.USER],
                            [Board.USER, Board.AI,   Board.USER]]
        self.assertEqual(self.board.is_game_over(), Board.DRAW)

    def test_is_game_over_diagonals(self):
        self.board.state = [[Board.USER, Board.EMPTY, Board.AI],
                            [Board.AI,   Board.USER,  Board.AI],
                            [Board.USER, Board.AI,    Board.USER]]
        self.assertEqual(self.board.is_game_over(), Board.USER_WIN)

        self.board.state = [[Board.USER, Board.USER, Board.AI],
                            [Board.AI,   Board.AI,   Board.USER],
                            [Board.AI,   Board.USER, Board.EMPTY]]
        self.assertEqual(self.board.is_game_over(), Board.AI_WIN)

    def test_is_game_over_columns(self):
        self.board.state = [[Board.USER, Board.EMPTY, Board.AI],
                            [Board.USER, Board.AI,    Board.USER],
                            [Board.USER, Board.AI,    Board.AI]]
        self.assertEqual(self.board.is_game_over(), Board.USER_WIN)

    def test_get_score_all_outcomes(self):
        self.assertEqual(self.board.get_score(5), 0)

        self.board.state = [[Board.USER, Board.EMPTY, Board.AI],
                            [Board.USER, Board.AI,    Board.USER],
                            [Board.USER, Board.AI,    Board.AI]]
        self.assertEqual(self.board.get_score(3), -7)

        self.board.state = [[Board.USER, Board.USER, Board.AI],
                            [Board.AI,   Board.AI,   Board.USER],
                            [Board.AI,   Board.USER, Board.EMPTY]]
        self.assertEqual(self.board.get_score(2), 8)

    def test_minimax(self):
        tests_count = 5
        results = []

        for test in range(tests_count):
            is_game_over = Board.NOT_OVER
            while is_game_over is Board.NOT_OVER:
                if self.board.is_user_turn:
                    moves = self.board.get_available_moves()
                    pos = moves[randint(0, len(moves) - 1)]
                    self.board.make_move(Board.USER, *pos)
                else:
                    moves = self.board.get_available_moves()
                    best_turn = self.board.minimax(self.board, 0, None, True)
                    self.board.make_move(Board.AI, *moves[best_turn])
                is_game_over = self.board.is_game_over()

            results.append(is_game_over)
            self.board = Board()        # refresh board

        self.assertNotIn(Board.USER_WIN, results)


if __name__ == '__main__':
    unittest.main()
