"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']'.
Determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Result:
"""


class Solution:
    def isValid(self, s: str) -> bool:
        pair = {'(': ')', '{': '}', '[': ']'}

        if len(s) % 2 != 0:
            return False

        if s[0] in ')}]':
            return False

        # Initialize a stack
        # First In, Last Out (FILO)
        in_stack = []
        in_stack.append(s[0])

        # ()[]{}
        for i in range(1, len(s)):
            if s[i] == pair[s[i - 1]]:
                in_stack.pop()
            else:
                in_stack.append(s[i])
