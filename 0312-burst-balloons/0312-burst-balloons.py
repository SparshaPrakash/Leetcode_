# class Solution:
#     def maxCoins(self, nums: List[int]) -> int:
#         nums = [1] + nums + [1]
#         dp ={}

#         def dfs(l, r):
#             if l > r:
#                 return 0
#             if (l, r) in dp:
#                 return dp[(l, r)]
                
#             dp[(l, r)] = 0
#             for i in range(l, r + 1):  # considering that the ith balloon is the last one to burst
#                 coins = nums[i - 1] * nums[i] * nums[i + 1] 
#                 coins += dfs(l, i -1) + dfs(i + 1, r)
#                 dp[(l ,r)] = max(dp[(l, r)], coins)
#             return dp[(l, r)]

#         return dfs(1, len(nums) - 2)  # since we do not consider the first 1 and the last 1 value in the iteration


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]  # Add 1 at both ends to handle edge cases
        dp = {}  # Memoization dictionary

        def dfs(l, r):
            if l > r:
                return 0  # Base case: No balloons to burst
            if (l, r) in dp:
                return dp[(l, r)]
                
            dp[(l, r)] = 0
            for i in range(l, r + 1):  # considering that the ith balloon is the last one to burst
                coins = nums[l - 1] * nums[i] * nums[r + 1]  # Coins from bursting balloon i
                coins += dfs(l, i - 1) + dfs(i + 1, r)  # Coins from left and right subarrays
                dp[(l, r)] = max(dp[(l, r)], coins)  # Maximizing the coins

            return dp[(l, r)]

        return dfs(1, len(nums) - 2)   # since we do not consider the first 1 and the last 1 value in the iteration
