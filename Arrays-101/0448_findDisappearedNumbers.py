"""
448. Find All Numbers Disappeared in an Array
Given an array nums of n integers where nums[i] is in the range [1, n], 
return an array of all the integers in the range [1, n] that do not appear in nums.

Result: 316 ms
"""


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Set of nums
        set_nums = set(nums)
        # Set of range [1, n]
        set_all = set(range(1, len(nums) + 1))

        # Return difference of sets in list
        return list(set_all - set_nums)

    # 304 ms
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(range(1, len(nums) + 1)) - set(nums))
