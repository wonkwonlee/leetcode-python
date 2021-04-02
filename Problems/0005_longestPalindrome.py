"""
Longest Palindromic Substring
Given a string s, return the longest palindromic substring in s.

Palindrome is a word which reads the same backward as forward, such as madam.

Result: 

실패 케이스 : "cbbd"
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        check = False
        start = 0
        left, right = [], []
        
        for i in range(len(s)):
            left.append(s[i])
            right.append(s[-1 - i])
            
            if check and left[i] == right[i]:
                return "".join(left[start:i+1] + right[-i:-start])
            
            if left[i] == right[i]:
                check = True
                start = i
                print(start)
