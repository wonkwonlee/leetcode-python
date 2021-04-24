"""
16. 3Sum Closest
Given an array nums of n integers and an integer target, find three integers in 
nums such that the sum is closest to target. Return the sum of the three integers.
You may assume that each input would have exactly one solution.

# Binary Search using two pointer

Result:
"""


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Sort nums array binary search
        nums.sort()
        # Store closest sum
        result = 0
        # Current minimum difference; initialized with max integer val
        min_val = 2 ** 31 - 1

        for i in range(len(nums) - 2):
            start = i + 1
            end = len(nums) - 1
            # Binary Search using two pointer
            while start < end:
                # Current three sum
                sum = nums[i] + nums[start] + nums[end]
                # Current difference between three sum and target
                diff = abs(sum - target)
                # Update current minimum and store current three sum
                if diff < min_val:
                    min_val = diff
                    result = sum
                if sum < target:
                    start += 1
                elif sum > target:
                    end -= 1
                else:
                    # If sum is equal to target, return sum
                    return sum

        return result
