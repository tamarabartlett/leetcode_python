#!/usr/bin/env python3

import sys

def findPeakElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    peak_index = 0
    for index in range(1, len(nums)):
        if nums[index] > nums[index-1]:
            peak_index = index

    return peak_index
# 
# if __name__ == '__main__':
#     # Map command line arguments to function arguments.
#     findPeakElement([1, 2, 3])
