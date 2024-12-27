class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (len(coins) + 1) for i in range(amount + 1)]
        dp[0] = [1] * (len(coins) + 1)


        for a in range(1, amount + 1):
            for i in range(len(coins) - 1, -1, -1):
                dp[a][i] = dp[a][i + 1] # not using the current coin here -> moving to next coin
                if a - coins[i] >= 0: # if we do use the current coin
                    dp[a][i] += dp[a-coins[i]][i]

        return dp[amount][0]
        