import unittest
from goldbach import goldbach


class GoldbachTests(unittest.TestCase):

    def test_cases(self):
        self.assertEqual([(2, 2)], goldbach(4))
        self.assertEqual([(3, 3)], goldbach(6))
        self.assertEqual([(3, 5)], goldbach(8))
        self.assertEqual([(3, 7), (5, 5)], goldbach(10))

        output_100 = [(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)]
        self.assertEqual(output_100, goldbach(100))

if __name__ == '__main__':
    unittest.main()
