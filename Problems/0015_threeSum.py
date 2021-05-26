"""
15. 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Result: 9820 ms -> 860 ms
"""


class Solution:
    # My Code - 9820 ms
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

        # Remove elements that exist more than 3
        for n in nums:
            while nums.count(n) > 3:
                nums.remove(n)

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

    # Reference from "파이썬 알고리즘 인터뷰" - 876 ms
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for i in range(len(nums) - 2):
            # Ignore duplicate values
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Binary Search by using two-pointer method
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    result.append([temp, nums[start], nums[end]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return results

    # My Code modified - 860 ms
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        # If length is less than 3, return an empty list
        if len(nums) < 3:
            return result
        # If length is 3
        if len(nums) == 3:
            # Condition meets only if all elements are 0
            if nums[0] + nums[1] + nums[2] == 0:
                result.append([nums[0], nums[1], nums[2]])
            return result
        
        # Sort nums to apply binary search
        nums.sort()

        # For each items in nums
        for i in range(len(nums) - 2):
            # Ignore duplicates if index is after 0
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Binary search by using two-pointer
            start = i + 1
            end = len(nums) - 1
            while start < end:
                # Store current sum
                sum = nums[i] + nums[start] + nums[end]
                # Sum of triplet is less than 0
                if sum < 0:
                    start += 1
                # Sum of triplet is larger than 0
                elif sum > 0:
                    end -= 1
                # Sum of triplet is 0
                else:
                    # Store current triplet to the list
                    result.append([nums[i], nums[start], nums[end]])
                    # Ignore duplicate number in left side
                    while start < end and nums[start] == nums[start + 1]:
                        start += 1
                    # Ignore duplicate number in right side
                    while start < end and nums[end] == nums[end - 1]:
                        end -= 1
                    start += 1
                    end -= 1
            
        return result
