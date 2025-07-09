from typing import List

class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # If the starting or ending cell is an obstacle, return 0 immediately
        if grid[0][0] == 1 or grid[m - 1][n - 1] == 1:
            return 0

        # Create DP table
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1  # 1 way to be at the start

        # Fill first row
        for j in range(1, n):
            if grid[0][j] == 0:
                dp[0][j] = dp[0][j - 1]
            # else it stays 0 (obstacle)

        # Fill first column
        for i in range(1, m):
            if grid[i][0] == 0:
                dp[i][0] = dp[i - 1][0]

        # Fill the rest of the grid
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]
