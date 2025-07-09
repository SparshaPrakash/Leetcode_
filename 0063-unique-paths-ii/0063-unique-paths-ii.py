from typing import List

class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # If start or end is an obstacle, return 0
        if grid[0][0] == 1 or grid[m - 1][n - 1] == 1:
            return 0

        # Initialize a 1D dp array for the first row
        dp = [0] * n
        dp[0] = 1  # Start cell has one way if not an obstacle

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dp[j] = 0  # No path through an obstacle
                elif j > 0:
                    dp[j] += dp[j - 1]  # Add left cell value

        return dp[-1]
