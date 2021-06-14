"""
26. Remove Duplicates from Sorted Array
Given a sorted array nums, remove the duplicates in-place such that 
each element appears only once and returns the new length.

Result : 72 ms
"""


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 0 <= len(nums) <= 30000
        if len(nums) == 0:
            return 0

        # Max value = last element in the list. (Ascending order)
        mx = nums[len(nums) - 1]
        # Less than minimum boundary 
        mn = -10001

        count = 0  # index
        for x in nums:
            if x > mn:
                nums[count] = x  # Update with new element
                count += 1
                mn = x  # Update current min value

            # Break the loop if x reaches max value
            if x == mx:
                break

        return count
