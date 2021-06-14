"""
27. Remove Element
Given an array nums and a value val, remove all instances of that value 
in-place and return the new length.

The order of elements can be changed. 

Simplified and 'Pythonic' version of removeElement.py

Result: 24 ms
"""


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if nums.count(val) < 0:
            return 0

        [nums.remove(val) for x in range(nums.count(val))]
        return len(nums)
