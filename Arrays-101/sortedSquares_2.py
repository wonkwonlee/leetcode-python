"""
Squares of a Sorted Array
Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.


Squaring each element and sorting the new array is very trivial, 
could you find an O(n) solution using a different approach?

Result: 208 ms
"""


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([x ** 2 for x in nums])

    # 204 ms
    # Use in-place operations to reduce time complexity
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] *= nums[i]

        return sorted(nums)
