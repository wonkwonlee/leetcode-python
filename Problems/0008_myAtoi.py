"""
8. String to Integer (atoi)
Implement the myAtoi(string s) function, which converts a string to a 32-bit 
signed integer (similar to C/C++'s atoi function).

1. Read in and ignore any leading whitespace.
2. Check if the next character is '-' or '+'.
This determines if the final result is negative or positive respectively. 
3. Read in next the characters until the next non-digit charcter or the end of 
the input is reached. 
4. Convert these digits into an integer. 
If no digits were read, then the integer is 0. Change the sign as necessary.
5. Check if the integer is out of the 32-bit integer range [-2^31, 2^31 - 1].
Clamp the integer so that it remains in the range. 
6. Return the integer as the final result.

Result:
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        

