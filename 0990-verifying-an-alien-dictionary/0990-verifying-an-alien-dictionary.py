class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # check first different character
        # if word A is a prefix of word B, then word A should come before word B

        order_map = {}
        for index, val in enumerate(order):
            order_map[val] = index

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            for j in range(len(w1)):
                if j == len(w2):
                    return False
                if w1[j] != w2[j]:
                    if order_map[w2[j]] < order_map[w1[j]]:
                        return False
                    break # we stop checking these 2 words

        return True
        