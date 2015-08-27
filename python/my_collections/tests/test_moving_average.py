import unittest
from my_collections.moving_average import old_moving_average, moving_average
from random import randint


class TestMovingAverage(unittest.TestCase):
    def test_moving_average(self):
        iterable = []
        for i in range(10):
            iterable.append(randint(1, 100))
        
        gen_1 = moving_average(iterable)
        gen_2 = old_moving_average(iterable)
        self.assertEqual(tuple(gen_1), tuple(gen_2))

if __name__ == '__main__':
    unittest.main()