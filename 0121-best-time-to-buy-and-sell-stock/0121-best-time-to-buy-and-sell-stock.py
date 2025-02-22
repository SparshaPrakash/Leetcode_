class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        dp = [0] * n  # Create an array to store the maximum profit on each day
        
        min_buy = prices[0]  # Initialize the first price as the minimum buy price

        for i in range(1, n):
            # Calculate the profit if we sell at the current price
            dp[i] = max(dp[i-1], prices[i] - min_buy)  # Keep the max profit so far
            min_buy = min(min_buy, prices[i])  # Update the min price if a new low is found
        
        return dp[-1]  # The last element in dp will have the maximum profit

        