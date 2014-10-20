import unittest
from uuid import uuid4
from random import randint
from cat2 import cat2
from os import remove


class Cat2Tests(unittest.TestCase):

    def setUp(self):
        self.testsCount = randint(10, 30)
        self.fileNames = []
        self.contents = []
        for i in range(self.testsCount):
            self.fileNames.append(str(uuid4()))
            self.contents.append(str(uuid4()))
            with open(self.fileNames[i], "w") as writeFile:
                writeFile.write(self.contents[i])

    def tearDown(self):
        for i in range(self.testsCount):
            remove(self.fileNames[i])

    def test_cat2_with_existing_files(self):
        result = ""
        for i in range(self.testsCount):
            with open(self.fileNames[i], "r") as readFile:
                result += readFile.read()
        self.assertEqual(result, cat2(self.fileNames))

    def test_cat2_with_nonexisting_files(self):
        temp = self.fileNames[0]    # preserve original first name
        self.fileNames[0] = str(uuid4())
        with self.assertRaises(FileNotFoundError):
            cat2(self.fileNames)
        self.fileNames[0] = temp    # restore original first name

if __name__ == '__main__':
    unittest.main()
