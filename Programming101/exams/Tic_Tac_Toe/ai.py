from board import Board
from copy import deepcopy


class AI:
    def __init__(self, board, user_turn):
        self.board = board
        self.user_turn = user_turn

    def best_move(self):
        best_turn = self.minimax(self.board, 0, None, True)
        return best_turn

    def minimax(self, board, depth, move=None, first_call=False):
        if move is not None:
            if board.is_user_turn:
                board.make_move(Board.USER, *move)
            else:
                board.make_move(Board.AI, *move)

        if board.is_game_over():
            return board.get_score(depth)

        depth += 1
        scores = []
        for move in board.get_available_moves():
            scores.append(self.minimax(deepcopy(board), depth, move))

        if len(scores) == 0:
            return board.get_score(depth)

        if not first_call:
            return max(scores) if self.user_turn else min(scores)

        return scores.index(max(scores))
