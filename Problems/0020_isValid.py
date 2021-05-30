"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']'.
Determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Result: 20 ms
"""


class Solution:
    def isValid(self, s: str) -> bool:
        # Open and close brackets
        open_bracket = ['(', '{', '[']
        close_bracket = [')', '}', ']']

        # Dictionary to store open and close bracket pair
        pair = dict(zip(open_bracket, close_bracket))

        if len(s) % 2 != 0:
            return False

        if s[0] in ')}]':
            return False

        # Initialize a stack (First In, Last Out)
        stack = []

        for i in range(len(s)):
            # If char is in open bracket
            if s[i] in open_bracket:
                # Push char to stack
                stack.append(pair[s[i]])
            # If char is in close bracket
            else:
                # If stack is not empty and char is same as top
                if stack and s[i] == stack[-1]:
                    # Remove top from the stack
                    stack.pop()
                # Else return false
                else:
                    return False

        # If stack is empty
        if not stack:
            return True
        # If stack is not empty
        else:
            return False
