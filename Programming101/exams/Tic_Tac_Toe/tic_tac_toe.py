from board import Board


class TicTacToe:
    def __init__(self):
        self.board = Board()

    def main_loop(self):
        pass

    def prompt_user_mark(self):
        while True:
            command = input('Enter X,Y coordinates for your move: ')
            coords = list(filter(lambda x: x.isdigit(), list(command)))
            pos = [int(char) for char in coords]

            if len(coords) != 2:
                print('Error: Enter 2 digits!')
            elif not(pos[0] in range(1, 4) and pos[1] in range(1, 4)):
                print('Error: Digits must be in the range [1,3]!')
            elif not self.board.is_pos_empty(pos[0]-1, pos[1]-1):
                print('Error: Position not available! Choose another!')
            else:
                return tuple(pos)


def main():
    ttt = TicTacToe()
    result = ttt.prompt_user_mark()
    print(result)


if __name__ == '__main__':
    main()
