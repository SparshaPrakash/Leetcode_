class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dp = [0] * N
        dp[N - 1] = 1

        # here Time: O(M*N); Space: O(N)
        for r in reversed(range(M)):
            for c in reversed(range(N)):
                if grid[r][c] == 1: # its an obstacle
                    dp[c] = 0 # its only c cause here we are doing the calculations in place
                elif c + 1 < N:# it was c + 1 = N, then we went out of bounds
                    dp[c] = dp[c] + dp[c + 1]   # here dp[c] is the bottom value and dp[c+1] is the right value

                else:
                    dp[c] = dp[c] + 0 # we dont really need this else case
        return dp[0]
