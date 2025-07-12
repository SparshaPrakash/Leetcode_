class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1) + 1, len(text2) + 1  # to coomocate the first 0 col and row
        dp = [[0 for i in range(cols)] for j in range(rows)]
        for row in range(1, rows):  # not conisdering the 0 col and 0 row
            for col in range(1, cols):
                if text1[row - 1] == text2[col - 1]: # if chacetrs are equal 
                    dp[row][col] = dp[row-1][col-1] + 1
                else:
                    dp[row][col] = max(dp[row -1][col], dp[row][col - 1])

        return dp[row][col]
        