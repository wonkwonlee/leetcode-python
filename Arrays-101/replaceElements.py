"""
Replace Elements with Greatest Element on Right Side
Given an array arr, replace every element in that array with the greatest 
element among the elements to its right, and replace the last element with -1.
Return the array.

Result: 3900 ms 
        116 ms
"""


class Solution:
    # Loop from the beginning
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Maximum value variable
        mx = 0
        # Loop from the first to the second last element
        for i in range(len(arr) - 1):
            # Find current max value
            mx = max(arr[i + 1:])
            # Update list with current maximum value
            arr[i] = mx

        # Set the last element is -1
        arr[-1] = -1

        return arr

    # Loop from the end
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Maximum value. Set -1 to skip one operation
        mx, val = -1, -1
        # Loop from the last element to the first
        for i in range(len(arr) - 1, -1, -1):
            # Update val if arr[i] is larger than mx
            if arr[i] > mx:
                val = arr[i]
            arr[i] = mx
            mx = val

        return arr
