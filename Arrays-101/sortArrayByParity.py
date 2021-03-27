"""
Sort Array By Parity

Given an array A of non-negative integers, return an array consisting of 
all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.
"""



class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:

        val = 0
        length = len(A)
        if length % 2 == 1:
            length += 1

        for i in range(length/2):
            if A[i] % 2 == 1:
                val = A[i]
            if A[i] % 2 == 0:
                A[even] = A[i]
                

