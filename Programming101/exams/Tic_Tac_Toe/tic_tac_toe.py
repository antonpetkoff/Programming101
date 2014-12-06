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
        while True:
            command = input('Enter X,Y coordinates for your move: ')
            coords = list(filter(lambda x: x.isdigit(), list(command)))
            pos = [int(char) for char in coords]
            print(pos)

            if len(coords) != 2:
                print('Error: Enter 2 digits!')
            elif not(pos[0] in range(1, 4) and pos[1] in range(1, 4)):
                print('Error: Digits must be in the range [1,3]!')
            elif self.board[pos[0]-1][pos[1]-1] != ' ':
                print('Error: Position not available! Choose another!')
            else:
                return tuple(pos)


def main():
    ttt = TicTacToe()
    result = ttt.prompt_user_mark()
    print(result)


if __name__ == '__main__':
    main()
