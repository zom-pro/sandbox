'''
Created on Sep 12, 2015

@author: zompro
'''
import unittest
from property.settergetter import SetterGetter


class TestSetterGetter(unittest.TestCase):

    def test_settergetter(self):
        x_value = 10
        x_try_value = 5
        settergetter = SetterGetter(x_value)
        self.assertEqual(settergetter.x, x_value)
        settergetter.x = x_try_value
        self.assertNotEqual(settergetter.x, x_try_value)
        self.assertEqual(settergetter.x, x_value)


if __name__ == "__main__":
    unittest.main()