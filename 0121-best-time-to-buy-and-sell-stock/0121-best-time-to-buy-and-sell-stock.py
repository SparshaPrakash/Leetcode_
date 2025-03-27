class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        dp = [0] * n

        min_buy = prices[0]

        for i in range(1, n):
            dp[i] = max(dp[i - 1], prices[i] - min_buy)
            min_buy = min(min_buy, prices[i])

        return dp[-1]





        
       