'''
파이썬에서는 숫자는 정수, 실수 상관없이 0이면 거짓, 0이 아닌 수는 참이다.
따라서 if (i == 1) : ~~ 대신, if i : ~~~ 이렇게 적어도 된다.

'''
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Store max value and count
        result , count = 0 , 0       
        
        for i in nums:
            # 만약 nums가 1,0 말고 다른 숫자가 있다면 i == 1,2 등 구체적으로 적어야함
            if i :
                count += 1
            else :
                count = 0
            # Compare count and max value
            result = max(count, result)
            
        return result

    