"""
Median of Two Sorted Arrays
Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.

Result: 92 ms
"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # m, n are length of two arrays, respectively
        m, n = len(nums1), len(nums2)
        nums_sort = sorted(nums1 + nums2)

        # Even number: median is half of two middle values
        if (m + n) % 2 == 0:
            # Change type to int as float cannot be used in list index
            index = int((m + n) / 2)
            return (nums_sort[index - 1] + nums_sort[index]) / 2
        # Odd number: median is the middle value
        else:
            index = int((m + n) / 2)
            return float(nums_sort[index])
