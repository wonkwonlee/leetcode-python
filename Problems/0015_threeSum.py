"""
15. 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Result: 
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        # If length is less than 3, return an empty list
        if len(nums) < 3:
            return result
    
        if len(nums) == 3:
            # If length is 3, check if it meets condition
            if nums[0] + nums[1] + nums[2] == 0:
                result.append([nums[0], nums[1], nums[2]])
            
            return result
        
        # Sort nums to apply binary search
        nums.sort()
        # For each items in nums
        for i in range(len(nums)):
            temp = nums[i]
            nums.pop(i)
            
            # Binary search by using two-pointer
            start = 0
            end = len(nums) - 1
            while start < end:
                if nums[start] + nums[end] == -temp:
                    # Check if sorted array not exists
                    if sorted([temp, nums[start], nums[end]]) not in result:
                        # Store the sorted array to result
                        result.append(sorted([temp, nums[start], nums[end]]))
                    start += 1
                    end -= 1
                elif nums[start] + nums[end] > -temp:
                    end -= 1
                else:
                    start += 1
                    
            nums.insert(i, temp)
            
        return result

