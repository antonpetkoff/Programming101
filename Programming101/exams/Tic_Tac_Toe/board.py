from functools import reduce
from random import randint
import numpy

# check for score
# states


class Board:
    def __init__(self):
        self.state = [[' ', ' ', ' '] for i in range(3)]

    def make_move(self, player_mark, x, y):
        self.state[x][y] = player_mark

    def draw_board(self):
        board_as_list = reduce(lambda a, b: a+b, self.state, [])
        row_splitter = '---|---|---\n'
        row = ' {} | {} | {} \n'
        template = row + row_splitter + row + row_splitter + row
        return template.format(*board_as_list)[:-1]     # cut the last \n

    def is_pos_empty(self, x, y):
        return self.state[x][y] == ' '

    def get_available_moves(self):
        tuples = []
        for x in range(3):
            for y in range(3):
                if self.is_pos_empty(x, y):
                    tuples.append((x, y))
        return tuples

    def is_complete(self):
        for row in self.state:
            if ' ' in row:
                return False
        return True

    def _has_3_equal_marks(self, list, mark):    # helper method
        return list[0] == mark and list[1] == mark and list[2] == mark

    def is_game_won(self, mark):
        n = 3
        main_diagonal = []
        secondary_diagonal = []
        transposed = numpy.matrix(self.state).transpose().tolist()

        for row in transposed:
            if self._has_3_equal_marks(row, mark):            # check columns
                return True

        for x in range(n):
            if self._has_3_equal_marks(self.state[x], mark):  # check rows
                return True
            for y in range(n):
                if x == y:
                    main_diagonal.append(self.state[x][y])
                if x + y == n - 1:
                    secondary_diagonal.append(self.state[x][y])

        if self._has_3_equal_marks(main_diagonal, mark) or\
           self._has_3_equal_marks(secondary_diagonal, mark):   # diagonals
            return True

        return False


def main():
    board = Board()

    moves = board.get_available_moves()
    for pos in moves:
        if randint(1, 2) == 1:
            board.make_move('X', *pos)
        else:
            board.make_move('O', *pos)
    print(board.draw_board())

if __name__ == '__main__':
    main()
