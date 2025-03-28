class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_words = s.split()
        last_word = s_words[-1]

        len = 0

        for i in last_word:
            len += 1

        return len
