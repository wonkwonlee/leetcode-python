"""
17. Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent. Return the answer in any order.

2: abc
3: def
4: ghi
5: jkl
6: mno
7: pqrs
8: tuv
9: wxyz

Result: 20 ms
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # DFS algorithm
        def dfs(index, path):
            # Backtrack if digits are searched to the end
            if len(digits) == len(path):
                # Add current path to the result array
                result.append(path)
                # End the function
                return

            # Search from index to the length of digits
            for i in range(index, len(digits)):
                # Letters corresponding to the digit in dictionary
                for j in dic[digits[i]]:
                    # DFS recursively
                    # Search next index and next digit
                    dfs(i + 1, path + j)

        # If digits is an empty string, return an empty list
        if not digits:
            return []
        # Dictionary to to map digits to letters
        dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
               '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        result = []
        dfs(0, "")

        return result
