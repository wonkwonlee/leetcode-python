"""
Check If N and Its Double Exist
Given an array arr of integers, check if there exists two integers N and M
such that N is the double of M (N = 2 * M).


The target value(arr[i]*2) is in the list AND the index of value is
different with the original index.
Consider if the value is 0 or 1, the target value is still 0 or 1 and
can be pointed to the orignal index.

## list.index(x) : returns the index of value x in the list. ValueError if not exists.
"""
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        # Validation check
        if len(arr) < 2 or len(arr) > 500:
            return False
        
        for i in range(len(arr)):
            if arr[i]*2 in arr and arr.index(arr[i]*2) != i :
                return True

        return False