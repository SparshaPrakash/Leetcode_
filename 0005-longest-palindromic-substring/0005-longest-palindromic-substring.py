class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        self.res =""
        self.res_length = 0 

        # odd palindrome

        for i in range(len(s)):
            l, r = i, i
            self.expand(l,r,s)

            # even pailndrome
            l, r = i, i + 1
            self.expand(l,r,s)

        return self.res

    def expand(self, l, r, s):
        while (l >= 0 and r <= len(s) - 1 and s[l] == s[r]):
            if (r - l + 1) > self.res_length:
                self.res = s[l:r + 1]
                self.res_length = r - l + 1
            r += 1
            l -= 1