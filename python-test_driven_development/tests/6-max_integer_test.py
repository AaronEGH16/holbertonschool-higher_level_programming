#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        test = max_integer([])
        self.assertEqual(test, None)

    def test_simple_case(self):
        test = max_integer([1, 2, 3, 7, 4, 5, 6])
        self.assertEqual(test, 7)

    def test_negative_case(self):
        test = max_integer([-7, -6, -5, -1, -4, -3, -2])
        self.assertEqual(test, -1)

    def test_begining_max(self):
        test = max_integer([10, 1, 2, 3])
        self.assertEqual(test, 10)

    def test_last_max(self):
        test = max_integer([1, 2, 3, 10])
        self.assertEqual(test, 10)

    def test_single_element(self):
        test = max_integer([10])
        self.assertEqual(test, 10)
