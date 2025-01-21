class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Create an array to store the number of ways to reach each sum
        dp = [0] * (target + 1)
        dp[0] = 1  # There's one way to make the sum 0 (use no numbers)
        
        # Iterate over every possible total from 1 to target
        for total in range(1, target + 1):
            # Check each number in the list to see if it can contribute
            for num in nums:
                if total >= num:  # Only use num if it fits into the current total
                    dp[total] += dp[total - num]  # Add ways to make (total - num)
        
        # The final answer is the number of ways to make the target
        return dp[target]
