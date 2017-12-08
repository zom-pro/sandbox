import unittest
from multiplier.math_functions.sum_lib import sum


class SumTest(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(1, 2), 3)


if __name__ == '__main__':
    unittest.main()
