from db_manager import DBManager
from question import Question


class GameCLI:
    def __init__(self):
        self.db = DBManager()
        self.player_name = ''

    def game_start_up(self):
        first_msg = 'Welcome to the \"Do you even math?\" game!\n'
        first_msg += 'Here are your options:\n- start\n- highscores\n- quit\n'
        print(first_msg)

        player_name = input('Enter your playername> ')
        self.player_name = player_name
        self.db.add_player(player_name)
        print('Welcome {}! Let the game begin!'.format(player_name))

    def answer_questions(self):
        counter = 0

        while True:
            question = Question()
            print('Question #{}:'.format(counter + 1))
            print(question.text)
            answer = input('?> ')

            if answer == str(question.correct_answer):
                print('Correct!')
                counter += 1
            else:
                score = counter * counter
                msg = 'Incorrect! Ending game. '
                msg += 'Your score is: {}'.format(score)
                print(msg)

                if self.db.is_score_better(self.player_name, score):
                    self.db.update_score(self.player_name, score)

                return

    def main_loop(self):
        self.game_start_up()

        while True:
            command = input('?> ')

            if command == 'start':
                self.answer_questions()
                break
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
