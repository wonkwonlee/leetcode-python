"""
7. Reverse Integer
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range 
[-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed/unsigned).

Result:
"""

class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = -2 ** 31
        MIN_INT = 2 ** 31 - 1