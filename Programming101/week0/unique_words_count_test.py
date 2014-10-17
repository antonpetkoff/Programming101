import unittest
from unique_words_count import unique_words_count

class UniqueWordsCountTests(unittest.TestCase):

    def test_cases(self):
        input_1 = ["apple", "banana", "apple", "pie"]
        input_2 = ["python", "python", "python", "ruby"]
        input_3 = ["HELLO!"] * 10

        self.assertEqual(3, unique_words_count(input_1))
        self.assertEqual(2, unique_words_count(input_2))
        self.assertEqual(1, unique_words_count(input_3))

if __name__ == '__main__':
    unittest.main()
