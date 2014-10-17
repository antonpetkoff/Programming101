import unittest
from nth_fib_lists import nth_fib_lists


class NthFibListsTests(unittest.TestCase):

    def test_cases(self):
        self.assertEqual( , nth_fib_lists([1], [2], 1))
        self.assertEqual( , nth_fib_lists([1], [2], 2))
        self.assertEqual( , nth_fib_lists([1, 2], [1, 3], 3))
        self.assertEqual( , nth_fib_lists([], [1, 2, 3], 4))
        self.assertEqual( , nth_fib_lists([], [], 100))

if __name__ == '__main__':
    unittest.main()
