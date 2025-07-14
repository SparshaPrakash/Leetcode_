from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        max_len = 0
        majority = 0
        counts = defaultdict(int)

        while right < len(s):
            counts[s[right]] += 1
            majority = max(majority, counts[s[right]])
            while (right - left + 1) - majority > k:
                counts[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len
        