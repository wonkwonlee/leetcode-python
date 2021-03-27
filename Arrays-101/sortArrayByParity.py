"""
Sort Array By Parity

Given an array A of non-negative integers, return an array consisting of 
all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

Result: 72 ms
"""


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:

        count = 0

        for i in range(len(A)):
            if A[i] % 2 == 0:
                # Change current val with count val
                A[i], A[count] = A[count], A[i]
                count += 1

        return A

    def sortArrayByParity(self, A: List[int]) -> List[int]:
        start = 0
        end = len(A) - 1

        # Use two pointers to go through both ends.
        while start < end:
            if A[start] % 2 == 0:
                start += 1
            elif A[end] % 2 != 0:
                end -= 1
            A[start], A[end] = A[end], A[start]
        return A
