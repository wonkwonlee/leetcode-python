"""
283. Move Zeroes
Given an integer array nums, move all 0's to the end of it while maintaining 
the relative order of the non-zero elements.

Result : 48 ms
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Use two pointers, zeroes and non_zeroes
        zeroes, non_zeroes = 0, 0
        for x in nums:
            # Count number of zeroes
            if x == 0:
                zeroes += 1
            # If element is not 0, move to the first element
            else:
                nums[non_zeroes] = x
                non_zeroes += 1

        # Fill 0 from the last elements
        for i in range(1, zeroes + 1):
            nums[-i] = 0

    def moveZeroes(self, nums: List[int]) -> None:
        start = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[start] = nums[i]
                start += 1

        # Fill 0 after the index
        for i in range(start, len(nums)):
            nums[i] = 0
