from typing import List

class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        
        # Initialize a DP table with all zeros
        dp = [[0] * N for _ in range(M)]
        
        # If the start or end is an obstacle, return 0 (no paths possible)
        if grid[0][0] == 1 or grid[M-1][N-1] == 1:
            return 0

        # Set the starting position
        dp[0][0] = 1
        
        # Fill the DP table row by row
        for r in range(M):
            for c in range(N):
                if grid[r][c] == 1:  # If it's an obstacle, set paths to 0
                    dp[r][c] = 0
                else:
                    if r > 0:
                        dp[r][c] += dp[r-1][c]  # Paths from top cell
                    if c > 0:
                        dp[r][c] += dp[r][c-1]  # Paths from left cell

        return dp[M-1][N-1]  # Bottom-right cell contains the total paths
