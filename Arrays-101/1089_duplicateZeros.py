"""
1089. Duplicate Zeros
Given a fixed length array arr of integers, duplicate each occurrence of 
zero, shifting the remaining elements to the right.

Example
[1,0,2,3,0,4,5,0] -> [1,0,0,2,3,0,0,4]
[1,2,3] -> [1,2,3]
"""


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        cn = 0
        while cn < len(arr):
            if arr[cn] == 0:
                arr.insert(cn + 1, 0)
                arr.pop()
                cn += 1
            cn += 1

    def duplicateZeros(self, arr: List[int]) -> None:
        temp = []

        # If 0, append twice (Two zeros); else, append once
        for x in arr:
            if x == 0:
                temp.append(x)
            temp.append(x)

        # Slice the temp array to len(arr)
        ans = temp[:len(arr)]

        # Deep copy
        for i in range(len(arr)):
            arr[i] = ans[i]
