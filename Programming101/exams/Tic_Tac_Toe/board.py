from functools import reduce

# is game won? check vertical, horizontal, diagonal triplets
# check for score
# state
# available moves; empty (x,y) tuples


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


def main():
    board = Board()
    board.make_move('X', 0, 0)
    board.make_move('O', 2, 1)
    print(board.is_pos_empty(1, 1))
    print(board.is_pos_empty(2, 1))
    available_moves = board.get_available_moves()
    print(available_moves)
    board.make_move('X', *available_moves[0])
    print(board.draw_board())

if __name__ == '__main__':
    main()
