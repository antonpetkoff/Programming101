from os import remove
from cat import cat
import unittest
import uuid


class CatTests(unittest.TestCase):

    def setUp(self):
        self.fileName = "test_cat.txt"
        self.contents = "Neiko lapa slivi na poleto."
        with open(self.fileName, "w") as writeFile:
            writeFile.write(self.contents)

    def tearDown(self):
        remove(self.fileName)

    def test_cat_with_existing_file(self):
        self.assertEqual(self.contents, cat(self.fileName))

    def test_cat_with_nonExisting_file(self):
        randomName = str(uuid.uuid4())
        catResult = "File {} not found!".format(randomName)
        self.assertEqual(catResult, cat(randomName))


if __name__ == '__main__':
    unittest.main()
