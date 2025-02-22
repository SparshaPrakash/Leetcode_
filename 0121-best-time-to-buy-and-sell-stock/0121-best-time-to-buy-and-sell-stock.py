class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        min_buy = prices[0]  # Start with the first price as the initial minimum price
        mx_profit = 0  # Initialize the maximum profit as 0
        
        for i in range(1, len(prices)):  # Start from the second price onward
            # Calculate profit if sold at current price
            profit = prices[i] - min_buy
            
            # Update maximum profit
            mx_profit = max(mx_profit, profit)
            
            # Update minimum buy price if a lower price is found
            min_buy = min(min_buy, prices[i])
        
        return mx_profit

        