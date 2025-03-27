class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        # we'll take an arbitrary string to iterate through
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]

        return res

        



