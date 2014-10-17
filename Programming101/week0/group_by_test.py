import unittest
from group_by import groupby


class GroupByTests(unittest.TestCase):

    def test_cases(self):
        result_1 = {0: [0, 2, 4, 6], 1: [1, 3, 5, 7]}
        self.assertEquals(result_1, groupby(lambda x: x % 2, [0, 1, 2, 3, 4, 5, 6, 7]))

        result_2 = {'even': [2, 8, 10, 12], 'odd': [1, 3, 5, 9]}
        self.assertEquals(result_2, groupby(lambda x: 'odd' if x % 2 else 'even',
                                            [1, 2, 3, 5, 8, 9, 10, 12]))

        result_3 = {0: [0, 3, 6], 1: [1, 4, 7], 2: [2, 5]}
        self.assertEquals(result_3, groupby(lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7]))

if __name__ == '__main__':
    unittest.main()
