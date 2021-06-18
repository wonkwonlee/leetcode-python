"""
695. Max Area of Island
You are given an m x n binary matrix grid. 
An island is a group of 1's (representing land) connected 4-directionally 
(horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.
The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.


Result:
"""


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(x, y):
            if x <= -1 or x >= n or y <= -1 or y >= m:
                return False

            if grid[x][y] == 0:
                grid[x][y] = 1
                dfs(x-1, y)
                dfs(x+1, y)
                dfs(x, y-1)
                dfs(x, y+1)
                return True
            return False


        m = len(grid)
        n = len(grid[0])
        result = 0
        mx = 0
        ans = 0

        for i in range(m):
            for j in range(n):
               if dfs(i, j):
                result += 1

        return result

