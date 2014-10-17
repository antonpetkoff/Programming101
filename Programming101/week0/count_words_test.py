import unittest
from count_words import count_words

class CountWordsTests(unittest.TestCase):

    def test_unique_words(self):
        unique_input = ["apple", "banana", "pie"]
        unique_output = {'apple': 1, 'pie': 1, 'banana': 1}
        self.assertEqual(unique_output, count_words(unique_input))

    def test_repeating_words(self):
        repeating_input = ["apple", "banana", "apple", "pie", "apple"]
        repeating_output = {'pie': 1, 'apple': 3, 'banana': 1}
        self.assertEqual(repeating_output, count_words(repeating_input))

if __name__ == '__main__':
    unittest.main()
