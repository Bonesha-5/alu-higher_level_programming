#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_negative(self):
        self.assertEqual(max_integer([-1, -5, -10]), -1)

    def test_one_element(self):
        self.assertEqual(max_integer([8]), 8)

    def test_empty(self):
        self.assertIsNone(max_integer([]))

    def test_mixed(self):
        self.assertEqual(max_integer([2, -3, 0, 100]), 100)

    def test_float(self):
        self.assertEqual(max_integer([1.5, 2.3, -4.0]), 2.3)

    def test_string(self):
        self.assertEqual(max_integer("string"), "t")

    def test_same_values(self):
        self.assertEqual(max_integer([5, 5, 5]), 5)

    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)

