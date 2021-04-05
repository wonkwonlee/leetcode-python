"""
6. ZigZag Conversion
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of 
rows like this: 
    P   A   H   N
    A P L S I I G
    Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:


Result:
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) == numRows or len(s) == 1:
            return s

        ans = ""
        adj = [[0 for i in range(len(s))] for j in range(numRows)]

        for i in range(len(s)):
            # Vertical
            if i <= numRows:
                for j in range(numRows):
                    adj[i][j] = s[i]
            # Diagonoal
            for j in range(numRows):
                adj[i][j] = 

        for i in range(len(s))
            for row in range(numRows):
                adj[i][row] = s[i]

            















