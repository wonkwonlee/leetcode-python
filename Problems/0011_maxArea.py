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

# Greedy Algorithm

Result:
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        xy_plane = []

        for i in range(len(height)):
            # (heightm width) = [(1, 1), (8, 2), (6, 3), (2, 4), (5, 5), (4, 6), (8, 7), (3, 8), (7, 9)]
            xy_plane.append((height[i], i + 1))
        
        
        # [(8, 7), (8, 2), (7, 9), (6, 3), (5, 5), (4, 6), (3, 8), (2, 4), (1, 1)]
        xy_plane.sort(reverse=True)
        print(xy_plane)
        
        result, area = 0, 0
        for i in range(1, len(xy_plane)):
            if xy_plane[i - 1][0] == xy_plane[i] == 0:
                h
            else:
                h = min(xy_plane[i - 1][0], xy_plane[i][0])
                w = abs(xy_plane[i - 1][1] - xy_plane[i][1])
                result = max(result, h * w)
        
        return result