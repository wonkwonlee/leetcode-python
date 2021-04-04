"""
4. Median of Two Sorted Arrays
Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.

# Floor Division, //
Python uses // as the floor division operator and % as the modulo operator.
By using floor division, we can only acquire quotient.

Result: 80 ms
"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # m, n are length of two arrays, respectively
        m, n = len(nums1), len(nums2)
        nums_sort = sorted(nums1 + nums2)

        # Even number: median is half of two middle values
        if (m + n) % 2 == 0:
            # Use // operation (floor division) to ignore decimals
            index = (m + n) // 2
            return (nums_sort[index - 1] + nums_sort[index]) / 2
        # Odd number: median is the middle value
        else:
            index = (m + n) // 2
            return float(nums_sort[index])
