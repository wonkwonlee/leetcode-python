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

# Example
Input: s = "42"
Output: 42

Input: s = "   -42"
Output: -42

Input: s = "4193 with words"
Output: 4193

Input: s = "words and 987"
Output: 0

Input: s = "-91283472332"
Output: -2147483648

# isdigit
Returns true if input is digit

# isalpha
Returns true if input is string


"  +  413"


Result:
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        # Maximum boundary and minimum boundary        
        max_val = 2147483647
        min_val = -2147483648
        # Boolean to check before or after digit parsing
        after_digit = False
        # Store result string
        result = ""
        for i in range(len(s)):
            if not s[i].isdigit() and after_digit:
                break
            # If white space, ignore it
            if s[i] == ' ' : 
                continue
            # If '+', integer is positive
            elif s[i] == '+':
                result += '+'
            # If '-', integer is negative
            elif s[i] == '-':
                result += '-'
            # If char is digit, store the current digit
            elif s[i].isdigit():
                result += s[i]
            # If char is string or '.', break the loop
            elif s[i].isalpha()  or s[i] == '.':
                break

        
        # print(result)


        # Return 0 if result is empty
        if result == '' or (not result.isdigit() and not result[1:].isdigit()):
            return 0
        # Clamp result if out of boundary
        elif int(result) < min_val:
            return min_val
        elif int(result) > max_val:
            return max_val
        else:
            return int(result)




