"""
Height Checker
Students are asked to stand in non-decreasing order of heights for an annual photo.

Return the minimum number of students that must move in order for all students 
to be standing in non-decreasing order of height.

## sorted(array) vs array.sort()
sorted() returns the sorted array. 
While sort() just sorts the array and does not return.
In other words, type(sorted(array)) is 'array', but type(array.sort()) is 'None'

Result: 36 ms
"""


class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        if len(heights) <= 0:
            return -1

        sorted_heights = sorted(heights)
        # This way we can know exact elements
        return len([i for i, j in zip(heights, sorted_heights) if i != j])

        # 24 ms

    def heightChecker(self, heights: List[int]) -> int:
        new = sorted(heights)
        counter = 0
        # This way we do not know exact elements, but it's faster
        for i in range(len(heights)):
            if heights[i] != new[i]:
                counter += 1
        return counter
