from typing import List

class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # If the starting or ending cell is an obstacle, return 0 immediately
        if grid[m - 1][n - 1] == 1 or grid[0][0] == 1:
            return 0

        # Create a 2D dp array initialized to 0
        dp = [[0] * n for _ in range(m)]

        # The bottom-right corner has 1 way if it's not an obstacle
        dp[m - 1][n - 1] = 1

        # Fill the last row (only moving right is possible)
        for i in range(m - 2, -1, -1):
            if grid[i][n - 1] == 1:
                dp[i][n - 1] = 0  # Obstacle blocks path
            else:
                dp[i][n - 1] = dp[i + 1][n - 1]

        # Fill the last column (only moving down is possible)
        for j in range(n - 2, -1, -1):
            if grid[m - 1][j] == 1:
                dp[m - 1][j] = 0  # Obstacle blocks path
            else:
                dp[m - 1][j] = dp[m - 1][j + 1]

        # Fill the rest of the DP table
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if grid[i][j] == 1:
                    dp[i][j] = 0  # Obstacle blocks path
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j + 1]  # Sum of paths from below and right

        # The result is stored in dp[0][0]
        return dp[0][0]
