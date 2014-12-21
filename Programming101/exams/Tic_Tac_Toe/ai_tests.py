import unittest
from random import randint
from board import Board
from ai import AI


class AITests(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_minimax(self):
        tests_count = 5
        ai_wins = 0
        user_wins = 0

        for test in range(tests_count):
            is_game_over = Board.NOT_OVER
            while is_game_over is Board.NOT_OVER:
                if self.board.is_user_turn:
                    moves = self.board.get_available_moves()
                    pos = moves[randint(0, len(moves) - 1)]
                    self.board.make_move(Board.USER, *pos)
                else:
                    moves = self.board.get_available_moves()
                    best = AI(self.board, self.board.is_user_turn).best_move()
                    self.board.make_move(Board.AI, *moves[best])
                is_game_over = self.board.is_game_over()

            if is_game_over is Board.AI_WIN:
                ai_wins += 1
            elif is_game_over is Board.USER_WIN:
                user_wins += 1
            self.board = Board()        # refresh board

        self.assertGreaterEqual(ai_wins, user_wins)


if __name__ == '__main__':
    unittest.main()
