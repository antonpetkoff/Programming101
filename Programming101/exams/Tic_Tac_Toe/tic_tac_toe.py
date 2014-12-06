from functools import reduce


class TicTacToe:
    def __init__(self):
        self.board = [[' ', ' ', ' '] for i in range(3)]

    def play_game(self):
        pass

    def main_loop(self):
        pass

    def draw_board(self):
        board_as_list = reduce(lambda a, b: a+b, self.board, [])
        row_splitter = '---|---|---\n'
        row = ' {} | {} | {} \n'
        template = row + row_splitter + row + row_splitter + row
        return template.format(*board_as_list)[:-1]     # cut the last \n

    def prompt_user_mark(self):
        pass


def main():
    ttt = TicTacToe()
    print(ttt.draw_board())


if __name__ == '__main__':
    main()
