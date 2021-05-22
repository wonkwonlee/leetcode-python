"""
18. 4Sum
Given an array nums of n integers, return an array of all the unique quadruplets
[nums[a], nums[b], nums[c], nums[d]] such that:
1. 0 <= a, b, c, d < n
2. a, b, c, and d are distinct.
3. nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.

Result:
"""


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        # Length is less than 4
        if len(nums) < 4:
            return result
        # Length is 4
        if len(nums) == 4:
            if sum(nums) == target:
                result.append([nums[0], nums[1], nums[2], nums[3]])
            return result

        nums.sort()

        # -2 -1 0 0 1 2
        for i in range(len(nums) - 2):
            

