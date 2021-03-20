class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Maximum consecutive value
        result = 0
        # Hold current maximum number of consecutive
        count = 0        
        
        for i in range(1, len(nums)):
            if nums[i] == 1:
                count += 1
                result = max(count, result)
                for j in range(1, len(nums)-i):
                    if nums[i+j] == 1:
                        count += 1
                        result = max(count, result)
                    else:
                        count = 0       # Reset
                        break
            else:
                count = 0
            
        return result