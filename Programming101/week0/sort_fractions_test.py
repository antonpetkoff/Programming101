import unittest
from sort_fractions import sort_fractions


class SortFractionsTests(unittest.TestCase):

    def test_cases(self):
        result_1 = [(1, 2), (2, 3)]
        result_2 = [(1, 3), (1, 2), (2, 3)]
        result_3 = [(22, 78), (15, 32), (5, 6), (7, 8), (9, 6), (22, 7)]

        self.assertEqual(result_1, sort_fractions([(2, 3), (1, 2)]))
        self.assertEqual(result_2, sort_fractions([(2, 3), (1, 2), (1, 3)]))
        self.assertEqual(result_3, sort_fractions([(5, 6), (22, 78), (22, 7),
                                                   (7, 8), (9, 6), (15, 32)]))

    def test_with_equal_fractions(self):
        self.assertEqual([(4, 4), (5, 5)], sort_fractions([(5, 5), (4, 4)]))

if __name__ == '__main__':
    unittest.main()
