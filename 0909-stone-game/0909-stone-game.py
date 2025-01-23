class Solution:
    def stoneGame(self, p: List[int]) -> bool:
        n = len(p)
        dp = p[:]  # Initialize dp as a copy of the piles array
        
        # Iterate over all possible subarray lengths
        for d in range(1, n):
            for i in range(n - d):
                # Update dp[i] based on the current subarray [i, i + d]
                dp[i] = max(p[i] - dp[i + 1], p[i + d] - dp[i])
        
        # If the maximum score difference starting at index 0 is positive, Alex wins
        return dp[0] > 0