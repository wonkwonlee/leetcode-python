'''
Find Numbers with Even Number of Digits
Given an array nums of integers, return how many of them contain an even number of digits.
'''
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        # Input validation check
        if len(nums) < 1 or len(nums) > 500:
            return -1
        
        # Input validation check
        if min(nums) < 1 or max(nums) > 100000:
            return -1

        # Count even number of digits
        evn = 0

        for data in nums:
            # Count the quotient
            cn = 1

            # If data is divisible by 10, keep dividing by 10 and add a count
            while data // 10 != 0:
                data //= 10
                cn += 1
            
            if cn % 2 == 0:
                evn += 1

        return evn


    # Use list comprehension to simplify the code
    # len(str(x)) to get a number of digit
    def findNumbers(self, nums: List[int]) -> int:
        sn = [len(str(x)) % 2 == 0 for x in nums]
        return sum(sn)

