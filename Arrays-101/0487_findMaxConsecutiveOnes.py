"""
487. Max Consecutive Ones II
Given a binary array nums, return the maximum number of consecutive 1's in the
array if you can flip at most one 0.

Result: 368 ms, 332 ms
"""


class Solution:
    # First Attempt - 368 ms
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Initialize variables
        result, count, prev = 0, 0, 0
        flip = False
        for num in nums:
            # Next element is 1    
            if num == 1:
                count += 1
            # Next element is 0
            else:
                # If already one 0 is flipped
                if flip:
                    # Flip is False
                    flip = False
                    # Prev stores 1s and one 0
                    prev, count = count + 1, 0
                # If 0 is not yet flipped
                else:
                    # Flip is True
                    flip = True
                    # Prev stores 1s and one 0
                    prev, count = count + 1, 0
            # print(f"{count},{prev},{flip}")
            result = max(result, count + prev)
        return result

    # Second Attempt - 332 ms
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Initialize variables
        # Prev is initialized with -1 as max = count + prev + 1 
        result, count, prev = 0, 0, -1

        for num in nums:
            if num:
                count += 1
            else:
                result = max(result, count + prev + 1)
                prev = count
                count = 0

        return max(result, count + prev + 1)
