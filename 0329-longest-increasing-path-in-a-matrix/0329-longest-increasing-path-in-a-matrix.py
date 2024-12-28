class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[-1] * COLS for _ in range(ROWS)]  # 2D DP array initialized with -1

        def dfs(r, c, prevVal):
            if (r < 0 or r >= ROWS or c < 0 or 
                c >= COLS or matrix[r][c] <= prevVal):
                return 0
            if dp[r][c] != -1:  # Check if the result is already computed
                return dp[r][c]

            res = 1
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
            dp[r][c] = res  # Store the result in the DP table
            return res

        maxLength = 0
        for r in range(ROWS):
            for c in range(COLS):
                maxLength = max(maxLength, dfs(r, c, -1))
        return maxLength
