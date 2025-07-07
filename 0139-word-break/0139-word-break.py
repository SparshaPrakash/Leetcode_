class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)       # Faster lookup: O(1)
        n = len(s) + 1                 # We use a dp array of size len(s) + 1
        dp = [False] * n
        dp[0] = True                   # Base case: empty string is "breakable"
        
        trues = [0]                    # Track indices where dp[i] is True
        
        for i in range(1, n):
            for j in trues:
                if s[j:i] in wordDict:
                    dp[i] = True       # s[0:i] can be broken
                    trues.append(i)    # Save new True index
                    break              # No need to check more j's for this i
        
        return dp[-1]                  # dp[n-1] tells if full string is breakable
