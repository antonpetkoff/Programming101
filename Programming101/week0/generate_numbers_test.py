import unittest
from os import remove
from random import randint
from uuid import uuid4
from generate_numbers import generate_numbers


class GenerateNumbersTests(unittest.TestCase):

    def test_cases(self):
        fileName = str(uuid4())
        numCount = randint(100, 10000)
        generate_numbers(fileName, numCount)
        numCount_afterCall = 0

        with open(fileName, "r") as readFile:
            numbers = readFile.read().split(" ")
            for number in numbers:
                if len(number) > 0:
                    numCount_afterCall += 1

        self.assertEqual(numCount, numCount_afterCall)
        remove(fileName)


if __name__ == '__main__':
    unittest.main()
