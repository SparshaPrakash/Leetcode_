class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0] * n for _ in range(n)]

        # Base case: If there's only one pile, the player takes it.
        for i in range(n):
            dp[i][i] = piles[i]

        # Fill DP table for ranges of increasing length
        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1
                dp[l][r] = max(
                    piles[l] - dp[l + 1][r],  # Choose left pile
                    piles[r] - dp[l][r - 1]   # Choose right pile
                )

        # If Alex (first player) can score more than Lee (second player), return True
        return dp[0][n - 1] > 0
