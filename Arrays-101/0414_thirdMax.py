"""
414. Third Maximum Number
Given integer array nums, return the third maximum number in this array. 
If the third maximum does not exist, return the maximum number.


## Check list or Array is empty
a = []
if a is None:   # Wrong code to check if list is empty
    print('a is None!')

if not a:       # Right code to check if list is empty
    print('a is not!')

>> a is not!

## Set data structure : remove duplicates in the list
s = set(list)

Result: 48 ms
"""


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        firstMax = max(nums)  # First max
        if len(nums) < 3:
            return firstMax

        # Remove the first max value in the array
        for i in range(nums.count(firstMax)):
            nums.remove(firstMax)

        if len(nums) < 2:
            return firstMax

        # Remove the second max value in the array
        secondMax = max(nums)  # Second max
        for i in range(nums.count(secondMax)):
            nums.remove(secondMax)

        if not nums:
            return firstMax
        else:
            thirdMax = max(nums)  # Third max
            return thirdMax

    # 40 ms
    # Thought sort() would greatly increase time complexity
    def thirdMax(self, nums: List[int]) -> int:
        # Use set to remove duplicates in the list
        nums = list(set(nums))
        nums.sort()
        if len(nums) < 3:
            return max(nums)
        nums.pop(-1)
        nums.pop(-1)
        return nums.pop(-1)
