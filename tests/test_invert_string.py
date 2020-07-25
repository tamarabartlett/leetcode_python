"""
tests.test_invert_string
"""
from unittest import TestCase

from leetcode.invert_string import invert_string

class TestInvertString(TestCase):
    def test_invert_odd_string(self):
        input = ["h","e","l","l","o"]
        output = invert_string(input)
        expected_output =  ["o","l","l","e","h"]

        self.assertEqual(expected_output, output)

    def test_invert_even_string(self):
        input = ["H","a","n","n","a","h"]
        output = invert_string(input)
        expected_output =  ["h","a","n","n","a","H"]

        self.assertEqual(expected_output, output)
