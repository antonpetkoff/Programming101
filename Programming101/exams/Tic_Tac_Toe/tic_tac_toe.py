from board import Board


class TicTacToe:
    def __init__(self):
        self.board = Board()

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
                return (x - 1, y - 1)

    def get_outcome(self, status):
        if status == Board.USER_WIN:
            return 'Congratulations! You WIN!!!'
        elif status == Board.AI_WIN:
            return 'Loooooser! You LOSE!'
        else:
            return 'The game is a DRAW!'

    def main_loop(self):
        print('Welcome to Tic-Tac-Toe!')
        print(self.board.draw_board())
        is_game_over = None
        while is_game_over is None:
            if self.board.is_user_turn:
                pos = self.prompt_user_mark()
                self.board.make_move(Board.USER, *pos)
            else:
                print('AI takes turn...')
                moves = self.board.get_available_moves()
                best_turn = self.board.minimax(self.board, 0, None, True)
                self.board.make_move(Board.AI, *moves[best_turn])
            print(self.board.draw_board())

            is_game_over = self.board.is_game_over()
        print(self.get_outcome(is_game_over))


def main():
    ttt = TicTacToe()
    ttt.main_loop()


if __name__ == '__main__':
    main()
