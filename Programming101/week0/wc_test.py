import unittest
from wc import wc
from uuid import uuid4
from os import remove


class WCTests(unittest.TestCase):

    def setUp(self):
        self.test_file = str(uuid4())
        self.contents = "Neiko lapa slivi na poleto.\n\
A Ionko se zabavlqva s praseto."
        with open(self.test_file, "w") as writeFile:
            writeFile.write(self.contents)

    def tearDown(self):
        remove(self.test_file)

    def test_chars(self):
        self.assertEqual(wc("chars", self.test_file),
                         len(self.contents))

    def test_words(self):
        self.assertEqual(wc("words", self.test_file), 11)

    def test_lines(self):
        self.assertEqual(wc("lines", self.test_file), 2)

    def test_with_nonExisting_file(self):
        with self.assertRaises(FileNotFoundError):
            wc("lines", str(uuid4))


if __name__ == '__main__':
    unittest.main()
