class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a 2D array dp, initialized to 0
        dp = [[0] * n for _ in range(m)]

        # The bottom-right corner has 1 way (the destination)
        dp[m - 1][n - 1] = 1

        # Fill the last row and last column with 1s, as there's only one way to move to the edge (either right or down)
        for i in range(m - 2, -1, -1):  # Iterate from second last row to the first row
            dp[i][n - 1] = 1  # Only 1 way to go down
        for j in range(n - 2, -1, -1):  # Iterate from second last column to the first column
            dp[m - 1][j] = 1  # Only 1 way to go right

        # Now, fill the rest of the dp table by summing the cells to the right and below
        for i in range(m - 2, -1, -1):  # Iterate from second last row to the first row
            for j in range(n - 2, -1, -1):  # Iterate from second last column to the first column
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]  # Sum of paths from below and right

        # The result is stored in dp[0][0], the top-left corner
        return dp[0][0]

