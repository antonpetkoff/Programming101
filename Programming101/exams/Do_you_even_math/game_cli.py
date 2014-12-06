from db_manager import DBManager
from question import Question


class GameCLI:
    def __init__(self):
        self.db = DBManager()

    def game_start_up(self):
        first_msg = 'Welcome to the \"Do you even math?\" game!\n'
        first_msg += 'Here are your options:\n- start\n- highscores\n- quit\n'
        print(first_msg)

        player_name = input('Enter your playername> ')
        self.db.add_player(player_name)
        print('Welcome {}! Let the game begin!'.format(player_name))

    def answer_questions(self):
        print('Answer questions!')

    def main_loop(self):
        self.game_start_up()

        while True:
            command = input('?> ')

            if command == 'start':
                self.answer_questions()
            elif command == 'highscores':
                print(self.db.get_highscores())
            elif command == 'quit':
                print('Bye!')
                break
            else:
                print('Invalid command!')


def main():
    game = GameCLI()
    game.main_loop()


if __name__ == '__main__':
    main()
