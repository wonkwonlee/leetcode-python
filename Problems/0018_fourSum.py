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
        