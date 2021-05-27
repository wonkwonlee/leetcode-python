"""
18. 4Sum
Given an array nums of n integers, return an array of all the unique quadruplets
[nums[a], nums[b], nums[c], nums[d]] such that:
1. 0 <= a, b, c, d < n
2. a, b, c, and d are distinct.
3. nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.

kSums: k-1 pointer technique

# Set
Set() method can only convert hashable type (int, string, tuple).
Hence, set([[a],[b],[c]]) prints out TypeError: unhashable type: 'list' 

Result: 1048 ms
"""


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        # Length is less than 4
        if len(nums) < 4:
            return result
        # Length is 4
        if len(nums) == 4:
            # Return current quadruplet
            if sum(nums) == target:
                result.append([nums[0], nums[1], nums[2], nums[3]])
            return result

        nums.sort()

        # Three-pointer Technique
        for i in range(len(nums) - 3):
            # Ignore duplicates if index is after 0
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            for j in range(i + 1, len(nums) - 2):
                # Binary Search
                start, end = j + 1, len(nums) - 1
                while start < end:
                    # Sum of quadruplet
                    four_sum = nums[i] + nums[j] + nums[start] + nums[end]
                    # Sum of quadruplet is less than target
                    if four_sum < target:
                        start += 1
                    # Sum of quadruplet is larger than target
                    elif four_sum > target:
                        end -= 1
                    # Sum of quadruplet is same as target
                    else:
                        # Store current quadruplet tuple
                        result.append((nums[i], nums[j], nums[start], nums[end]))
                        # Ignore duplicate number in left side
                        while start < end and nums[start] == nums[start + 1]:
                            start += 1
                        # Ignore duplicate number in right side
                        while start < end and nums[end] == nums[end - 1]:
                            end -= 1
                        start += 1
                        end -= 1

        # Remove duplicates
        result = set(result)
        # Technically, need to be converted to list
        # But, LeetCode accepts both set and list type
        # result = list(set(result))

        return result
