import unittest
from sum_numbers import sum_numbers
from uuid import uuid4
from os import remove


class SumNumbersTests(unittest.TestCase):

    def test_with_exisitng_file(self):
        fileName = str(uuid4())
        contents = "12 84 17 44 51 "
        sum = 208
        with open(fileName, "w") as writeFile:
            writeFile.write(contents)
        self.assertEqual(sum, sum_numbers(fileName))
        remove(fileName)

    def test_with_nonExisting_file(self):
        fileName = str(uuid4())
        callResult = "File {} not found!".format(fileName)
        self.assertEqual(callResult, sum_numbers(fileName))


if __name__ == '__main__':
    unittest.main()
