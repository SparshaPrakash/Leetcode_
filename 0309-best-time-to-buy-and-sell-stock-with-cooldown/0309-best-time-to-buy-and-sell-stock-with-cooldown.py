class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # there are 2 states- buying or selling
        # If we are buying- increament by 1 (i + 1)
        # if we are selling- increament by 2 (i + 2)- since we aways need a cool down day after selling
        
        # hashmap to cache the results
        dp = {} # Here, the key is (i, buying), val = max_profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if(i, buying) in dp:
                return dp[(i, buying)]

            if buying:
                # Buy the stock
                buy = dfs(i + 1, not buying) - prices[i] # after buying, we will be in a state of not buying
                # Cooldown (skip buying)
                cooldown = dfs(i +1, buying)
                dp[(i, buying)] = max(buy, cooldown)

            else:
                # sell the stock
                sell = dfs(i + 2, not buying) + prices[i]
                 # Cooldown (skip selling)
                cooldown = dfs(i + 1, buying)
                dp[(i, buying)] = max(sell, cooldown)

            return dp[(i, buying)]

        return dfs(0, True)


