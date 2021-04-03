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


Result: 

실패 케이스 : "cbbd"
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        list_s = list(s)
        # print(s)
        # print(list_s)
        
        for i in range(len(list_s)):
            left, right = list_s[i], list_s[-i-1]
            if left == right:
                result = list_s[i:-i]
                reverse_result = list(reversed(result))
                print(result)
                print(reverse_result)
#                 print("Same")
                
#                 if reverse_result == result
#                     return "".join(result)