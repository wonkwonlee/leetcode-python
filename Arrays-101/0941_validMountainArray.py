"""
941. Valid Mountain Array

Given an array of integers arr, return true if and only if it is a 
valid mountain array.

Result : 188 ms
"""


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        mx = max(arr)

        # If max value is the first or the last element
        if arr[0] == mx or arr[len(arr) - 1] == mx:
            return False

        mx_idx = arr.index(mx)

        # Strictly increasing and strictly decreasing arrays
        inc, dec = arr[0:mx_idx + 1], arr[mx_idx + 1:]

        # Check whether the array is strictly increasing
        for i in range(1, len(inc)):
            if inc[i] <= inc[i - 1]:
                return False

        # Check whether the array is strictly decreasing
        for i in range(1, len(dec)):
            if dec[i] >= dec[i - 1]:
                return False

        return True
