from functools import reduce
from copy import deepcopy


class Board:
    EMPTY = ' '
    USER = 'X'
    AI = 'O'
    USER_WIN = 3
    AI_WIN = -3
    DRAW = 1
    NOT_OVER = None

    def __init__(self):
        self.state = [[self.EMPTY for col in range(3)] for row in range(3)]
        self.is_user_turn = True

    def make_move(self, player_mark, x, y):
        self.state[x][y] = player_mark
        self.is_user_turn = not self.is_user_turn     # user always plays first

    def draw_board(self):
        board_as_list = reduce(lambda a, b: a+b, self.state, [])
        row_splitter = '---|---|---\n'
        row = ' {} | {} | {} \n'
        template = row + row_splitter + row + row_splitter + row
        return template.format(*board_as_list)

    def is_pos_empty(self, x, y):
        return self.state[x][y] == self.EMPTY

    def get_available_moves(self):
        tuples = []
        for x in range(3):
            for y in range(3):
                if self.is_pos_empty(x, y):
                    tuples.append((x, y))
        return tuples

    def is_complete(self):
        for row in self.state:
            if self.EMPTY in row:
                return False
        return True

    def _has_3_equal_marks(self, list):    # helper method
        if list == [Board.USER]*3:
            return Board.USER_WIN
        elif list == [Board.AI]*3:
            return Board.AI_WIN
        return None

    def is_game_over(self):
        n = 3
        status = None
        main_diagonal = []
        secondary_diagonal = []

        for i in range(n):
            column = [self.state[0][i], self.state[1][i], self.state[2][i]]
            status = self._has_3_equal_marks(column)
            if status is not None:
                return status

        for x in range(n):
            status = self._has_3_equal_marks(self.state[x])     # check rows
            if status is not None:
                return status

            for y in range(n):                  # accumulate diagonals
                if x == y:
                    main_diagonal.append(self.state[x][y])
                if x + y == n - 1:
                    secondary_diagonal.append(self.state[x][y])

        status = self._has_3_equal_marks(main_diagonal)     # check main diag
        if status is not None:
            return status

        status = self._has_3_equal_marks(secondary_diagonal)    # secondary
        if status is not None:
            return status

        if self.is_complete():
            return Board.DRAW
        return Board.NOT_OVER

    def get_score(self, depth):
        if self.is_game_over() == self.USER_WIN:
            return depth - 10
        elif self.is_game_over() == self.AI_WIN:
            return 10 - depth
        return 0

    # artificial intelligence
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
            scores.append(board.minimax(deepcopy(board), depth, move))

        if len(scores) == 0:
            return board.get_score(depth)

        if not first_call:
            return max(scores) if self.is_user_turn else min(scores)

        return scores.index(max(scores))
