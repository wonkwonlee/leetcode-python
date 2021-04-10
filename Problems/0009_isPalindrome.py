"""
9. Palindrome Number
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. 
For example, 121 is palindrome while 123 is not.

Result: 44 ms
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
            
        # Integer to string
        x = str(x)
        if x == x[-1::-1]:
            return True
