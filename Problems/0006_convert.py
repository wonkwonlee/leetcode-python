"""
6. ZigZag Conversion
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of 
rows like this: 
    P   A   H   N
    A P L S I I G
    Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Given a number of rows, return converted string.


# Explanation
N = 3
P A Y P A L I S H I R I N G
0 1 2 1 0 1 2 1 0 1 2 1 0 1

N = 4
P A Y P A L I S H I R I N G
0 1 2 3 2 1 0 1 2 3 2 1 0 1


Result: 56 ms
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Dictionary to store index
        dic = {}

        # Index of zigzag string
        index = 0
        # Moving direction, down for +1 and up for -1
        down, up = 1, -1
        move = 0

        for char in s:
            # Index increases by 1 for each vertical move
            if index == 0:
                move = down
            # Index decreases by 1 for each diagonal move
            if index == numRows - 1:
                move = up

            dic[index] = dic.get(index, "") + char
            # Update index with current moving direction
            index += move

        return "".join(dic.values())
