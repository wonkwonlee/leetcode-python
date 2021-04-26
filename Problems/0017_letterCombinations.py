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

Result:
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        from itertools import product

        dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        result = []
        nums = []

        if len(digits) == 0:
            return result

        for i in range(len(digits)):
            nums.append(dic.get(digits[i]))

        print(nums)
        
        for i in range(len(nums)):
            for j in product(nums[i]):
                result.append(j)
                
        return result





