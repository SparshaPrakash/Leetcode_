class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        count_2 = defaultdict(int) # hadh map for integer values

        for w in words2:
            count_w = Counter(w)
            for c, cnt in count_w.items():
                count_2[c] = max(count_2[c], cnt)   # merging all the words in words 2 in the hasmap, and getting the cmax count of each char for each word

        res = []
        for w in words1:
            counts_w = Counter(w)
            flag = True
            for c, cnt in count_2.items():
                if counts_w[c] < cnt:
                    flag = False
                    break
            if flag: # is True
                res.append(w)

        return res
        