class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # If there are no prices, return 0 profit
        if not prices:
            return 0
        
        # Initialize DP variables
        min_price = prices[0]  # The minimum price so far
        max_profit = 0  # The maximum profit so far

        # Iterate through the list of prices
        for price in prices:
            # Calculate the profit if selling at the current price
            profit = price - min_price
            
            # Update the maximum profit
            max_profit = max(max_profit, profit)
            
            # Update the minimum price if we find a new lower price
            min_price = min(min_price, price)

        return max_profit
