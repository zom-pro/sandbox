import unittest
from my_collections.counting import counting_appearance, counting_appearance_old

class TestCounting(unittest.TestCase):
    def test_counting(self):
        sample = [2, 1, 2, 3, 3, 2, 3, 1, 2, 3, 1, 1]
        d1 = counting_appearance(sample)
        d2 = counting_appearance(sample)
        self.assertDictEqual(d1, d2)

if __name__ == '__main__':
    unittest.main()