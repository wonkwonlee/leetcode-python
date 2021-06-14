"""
485. Max Consecutive Ones
Given a binary array, find the maximum number of consecutive 1s in this array.


## Python Booleans as Numbers:
Booleans are considered a numeric type in Python.
All numbers except '0' are True and '0' is always False.

Both expressions work fine.
if (i == 1) : ~~~
if i : ~~~
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Store max value and count
        result, count = 0, 0

        for i in nums:
            # False = 0, True = any other number
            if i:
                count += 1
            else:
                count = 0
            # Compare count and max value
            result = max(count, result)

        return result
