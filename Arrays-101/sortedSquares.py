'''
Squares of a Sorted Array
Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.


## Square a number in Python
a ** b               3 ** 2 = 9
pow(a, b)            pow(3, 2) = 9

## Sorting in Python
arr.sort()
sorted(arr)
'''
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared = sorted([x**2 for x in nums])
        return squared