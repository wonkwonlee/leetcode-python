"""
Remove Element
Given an array nums and a value val, remove all instances of that value 
in-place and return the new length.
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

        for i in range(nums.count(val)):
            nums.remove(val)

        length = len(nums)

        return length
