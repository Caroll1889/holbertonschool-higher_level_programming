#!/usr/bin/pyhton3
"""Unittest for max_integer([..])"""

import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_only_negative(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_one_negative(self):
        self.assertEqual(max_integer([1, -2, 3, 4]), 4)

    def text_max_end(self):
        self.assertEqual(max_integer([1, 2, 3, 5]), 5)

    def test_max_beg(self):
        self.assertEqual(max_integer([5, 1, 2, 3]), 5)

    def test_max_mid(self):
        self.assertEqual(max_integer([1, 2, 5, 3]), 5)

    def test_one_elem(self):
        self.assertEqual(max_integer([1]), 1)

if __name__ == '__main__':
    unittest.main()
