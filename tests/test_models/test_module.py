#!/usr/bin/python3

import unittest
from your_module import YourClass

class TestYourClass(unittest.TestCase):
    def test_feature(self):
        obj = YourClass()
        result = obj.your_method()
        self.assertEqual(result, expected_result)

    def test_another_feature(self):
        obj = YourClass()
        result = obj.another_method()
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
