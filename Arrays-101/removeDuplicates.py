'''
Remove Duplicates from Sorted Array
Given a sorted array nums, remove the duplicates in-place such that 
each element appears only once and returns the new length.



Result : 80 ms
'''
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """      
        # 0 <= len(nums) <= 30000
        if len(nums) == 0:
            return 0

        # Max value = last element in list. (Ascending order)
        mx = nums[len(nums)-1]
        # Out of min boundary(-10000)    
        mn = -10001               
        
        i = 0                   # index
        for x in nums:
            if x > mn:
                nums[i] = x     # Update with new element
                i += 1
                mn = x          # Update current min value   
        return i    