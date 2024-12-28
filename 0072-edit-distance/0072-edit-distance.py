class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]

        for j in range(len(word2) + 1):
            cache[len(word1)][j] = len(word2) - j # filling in values where word 1 is an empty string
        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i # filling in values where word 2 is an empty string

        for i in range(len(word1) -1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i + 1][j + 1] # if the current value in both the string are the same
                else:
                    cache[i][j] =1 + min(cache[i + 1][j],  cache[i][j + 1], cache[i + 1][j + 1])

        return cache[0][0]
 
 # Insert operation- cache[i][j + 1]
 # Delete Operation- cache[i + 1][j]
 # Replace Operation- cache[i + 1][j + 1]
        