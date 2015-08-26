import unittest
from my_collections.my_dict import MyDict
from _collections import defaultdict

class TestMyDict(unittest.TestCase):
    def test_my_dict(self):
        my_dict = MyDict(default_value=0);
        my_dict[(1, 1)] = 1
        self.assertEqual(my_dict[(1, 1)], 1)
        self.assertEqual(my_dict[(1, 0)], 0)
    
    def test_my_dict_alternative(self):
        def default():
            return 0

        my_dict = defaultdict(default);
        my_dict[(1, 1)] = 1
        self.assertEqual(my_dict[(1, 1)], 1)
        self.assertEqual(my_dict[(1, 0)], 0)

if __name__ == '__main__':
    unittest.main()