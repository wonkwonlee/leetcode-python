"""
15. 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Result: 
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dic = {}
        result = []


        for i, val in enumerate(nums):
            dic[val] = i


        for _ in range(1, nums):
            if nums


        return result