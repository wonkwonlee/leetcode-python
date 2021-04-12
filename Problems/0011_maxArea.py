"""
Container With Most Water
Given n non-negative integers a1, a2, ..., an , where each represents a point at
coordinate (i, ai). n vertical lines are drawn such that the two endpoints of 
the line i is at (i, ai) and (i, 0). Find two lines, which, together with the
x-axis forms a container, such that the container contains the most water.

# Example
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

Input: height = [4,3,2,1,4]
Output: 16

# Sorted with lambda
a = [(1, 2), (0, 1), (5, 1), (5, 2), (3, 0)]
 
b = sorted(a)
>> b = [(0, 1), (1, 2), (3, 0), (5, 1), (5, 2)]

c = sorted(a, key = lambda x : x[0])
>> c = [(0, 1), (1, 2), (3, 0), (5, 1), (5, 2)]

d = sorted(a, key = lambda x : x[1])
>> d = [(3, 0), (0, 1), (5, 1), (1, 2), (5, 2)]

e = sorted(e, key = lambda x : (x[0], -x[1]))
>> e = [(0, 1), (1, 2), (3, 0), (5, 2), (5, 1)]

Result: 724 ms
"""


class Solution:
    # Brute Force - Time Limit Exceeded
    def maxArea(self, height: List[int]) -> int:
        xy_plane = []
        for i in range(len(height)):
            xy_plane.append((height[i], i + 1))  # xy_plane = [(height, width)]

        # Descending order by the first and ascending by the second element
        xy_plane.sort(key=lambda x: (-x[0], x[1]))
        result = 0
        for i in range(len(xy_plane)):
            for j in range(i + 1, len(xy_plane)):
                h = min(xy_plane[i][0], xy_plane[j][0])
                w = abs(xy_plane[i][1] - xy_plane[j][1])
                result = max(result, h * w)

        return result

    # Two Pointer Approach
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        result = 0
        while left <= right:
            h = min(height[left], height[right])
            w = right - left
            result = max(result, h * w)

            # The right is shorter than the left
            if height[left] >= height[right]:
                right -= 1
            # The left is shorter than the right 
            else:
                left += 1

        return result
