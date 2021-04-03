"""
Longest Palindromic Substring
Given a string s, return the longest palindromic substring in s.
Palindrome is a word which reads the same backward as forward, such as madam.

# String -> List
str.split() : Split string by space
str.split("-") : Split string by -
list(str) : Store each char of string to list

# List -> String
new_str = "".join(list) : 

# Reverse a list
list.reverse() : Reverse the original list
reversed(arr) : Return reversed list
list(reversed(arr))
for i in reversed(arr):
    print(i)

# Reverse a string
str_reverse = str[:: -1]

Dynamic Programing


Result: 104 ms
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        ptr1, ptr2 = 0, 0
        # Loop through string s with index i
        for i in range(len(s)):
            # Check substring is same as revered substring
            if s[i - ptr2: i + 1] == s[i - ptr2: i + 1][::-1]:
                # Move pointers to current substring
                # ptr1 : ptr1 is i - previous ptr2
                # ptr2 : As i increases by 1, ptr2 increases by 1
                ptr1, ptr2 = i - ptr2, ptr2 + 1
                # print(s[ptr1: ptr1+ptr2])
            elif i - ptr2 > 0 and s[i - ptr2 - 1: i + 1] == s[i - ptr2 - 1: i + 1][::-1]:
                ptr1, ptr2 = i - ptr2 - 1, ptr2 + 2
                # print(s[ptr1: ptr1+ptr2])

        return s[ptr1: ptr1 + ptr2]
