#!/usr/bin/python3

"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


"""TestMaxInteger class"""
class TestMaxInteger(unittest.TestCase):
    def test_regular_case(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 2, 4]), 4)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -5, -3, -2]), -1)

    def test_duplilcate_numbers(self):
        self.assertEqual(max_integer([2, 3, 5, 4, 5]), 5)

    def test_single_element_list(self):
        self.assertEqual(max_integer([13]), 13)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 3, 0, 42, -5]), 42)

if __name__ == '__main__':
    unittest.main()
