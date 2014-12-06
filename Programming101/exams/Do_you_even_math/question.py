from random import randint


class Question:
    def __init__(self):
        self.correct_answer = 0
        self.text = 'What is the answer to {} {} {}?'

        self.__generate_question()

    def __generate_question(self):
        left = randint(1, 10)
        right = randint(1, 10)
        operand = randint(1, 2)

        if operand == 1:    # addition
            self.correct_answer = left + right
            self.text = self.text.format(left, '+', right)
        else:               # multiplication
            self.correct_answer = left * right
            self.text = self.text.format(left, '*', right)
