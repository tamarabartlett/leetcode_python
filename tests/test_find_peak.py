"""
tests.test_find_peak
"""
from unittest import TestCase

from leetcode.find_peak import findPeakElement

class TestFindPeak(TestCase):
    def test_find_peak(self):
        peak_index = findPeakElement([1, 2, 3])

        self.assertEqual(2, peak_index)
