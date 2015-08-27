import unittest
from my_collections.dict_of_lists import dict_of_lists_old, dict_of_lists

class TestDictOfLists(unittest.TestCase):
    def test_dict_of_dicts(self):
        sample = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
        d1 = dict_of_lists(sample)
        d2 = dict_of_lists_old(sample)
        self.assertDictEqual(d1, d2)

if __name__ == '__main__':
    unittest.main()