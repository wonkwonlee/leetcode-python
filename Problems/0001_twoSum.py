"""
1. Two Sum
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.


## Dictionary
A data structure with Key and Value pair(HashMap).
'Key' is immutable type, while 'value' can be both immutable and mutable.
dic = {Key1:Value1, Key2:Value2, Key3:Value3}
dic[key1] = Value1
"""


class Solution:
    # Brute force. 312 ms
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = []

        for i in range(len(nums)):
            ans = target - nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] == ans:
                    sol.append(i)
                    sol.append(j)

        return sol

    # Use dictionary. 44 ms
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize a dictionary (Hashmap)
        dic = {}

        # enumerate() returns both index and element in a list
        for i, num in enumerate(nums):
            if target - num in dic:
                return [dic[target - num], i]

            # Store Key and Value in reverse to find index from element in array
            dic[num] = i
