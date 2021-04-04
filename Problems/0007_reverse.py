"""
7. Reverse Integer
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range 
[-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed/unsigned).

#pop operation:
pop = x % 10
x /= 10

# push operation:
temp = rev * 10 + pop
rev = temp

Result: 24 ms
"""


class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2 ** 31 - 1   # 2147483647
        MIN_INT = -2 ** 31      # -2147483648
        # Return 0 if out of boundary
        if x < MIN_INT or x > MAX_INT:
            return 0

        # If x is units digit, return x
        if -10 < x < 10:
            return x

        # Result is the final value, count is the number of digits
        result, count = 0, 0
        res = []

        # If x is a negative integer, reverse the sign
        if x >= 0:
            sign = True
        else:
            x, sign = -x, False

        while x != 0:
            res.append(x % 10)
            x //= 10
            count += 1

        for digit in res:
            result += digit * 10 ** (count - 1)
            count -= 1

        # Return 0 if final value is out of boundary
        if result < MIN_INT or result > MAX_INT:
            return 0

        # Return final value with sign
        if sign:
            return result
        else:
            return -result

    # Example code
    def reverse(self, x):
        s = (x > 0) - (x < 0)
        r = int(str(s*x)[::-1])
        return s*r * (r < 2**31)
