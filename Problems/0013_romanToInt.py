"""
13. Roman to Integer
Given a roman numeral, convert it to an integer.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

Result: 40 ms
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        # Store integer value
        value = 0
        # Slice roman string for each step
        while s:
            if s[0] == 'M':
                value += 1000; s = s[1:]
            elif s[0] == 'D':
                value += 500; s = s[1:]
            elif s[0] == 'C':
                if len(s) == 1:
                    return value + 100
                elif s[1] == 'M':
                    value += 900; s = s[2:]
                elif s[1] == 'D':
                    value += 400; s = s[2:]
                else:
                    value += 100; s = s[1:]
            elif s[0] == 'L':
                value += 50; s = s[1:]
            elif s[0] == 'X':
                if len(s) == 1:
                    return value + 10
                elif s[1] == 'C':
                    value += 90; s = s[2:]
                elif s[1] == 'L':
                    value += 40; s = s[2:]
                else:
                    value += 10; s = s[1:]
            elif s[0] == 'V':
                value += 5; s = s[1:]
            else:
                if len(s) == 1:
                    return value + 1
                elif s[1] == 'X':
                    value += 9; s = s[2:]
                elif s[1] == 'V':
                    value += 4; s = s[2:]
                else:
                    value += 1; s = s[1:]

        return value


    # Example using dictionary
    def romanToInt(self, s: str) -> int:
        roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5,
                 'I': 1}
        result = 0
        for i in range(0, len(s) - 1):
            # Case of IV, IX, XL, XC, etc
            if roman[s[i]] < roman[s[i + 1]]:
                result -= roman[s[i]]
            else:
                result += roman[s[i]]
        return result + roman[s[-1]]
