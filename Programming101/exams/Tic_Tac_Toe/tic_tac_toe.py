from board import Board


class TicTacToe:
    def __init__(self):
        self.board = Board()

    def main_loop(self):
        pass

    def prompt_integer(self, msg):
        while True:
            command = input('Enter {} digit: '.format(msg))

            if (len(command) != 1) or (not command.isdigit()) or\
               (not int(command) in range(1, 4)):
                print('Error: Enter 1 digit in the range [1,3]')
            else:
                return int(command)

    def prompt_user_mark(self):
        print('Enter X,Y coordinates for your move:')
        while True:
            x = self.prompt_integer('row')
            y = self.prompt_integer('column')

            if not self.board.is_pos_empty(x - 1, y - 1):
                print('Error: Position not available! Choose another!')
            else:
                return (x, y)


def main():
    ttt = TicTacToe()
    result = ttt.prompt_user_mark()
    print(result)


if __name__ == '__main__':
    main()
