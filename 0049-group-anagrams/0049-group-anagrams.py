class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping charCpunt to list of Anagrams

        for s in strs:
            count = [0] * 26 # space for a to z

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return list(res.values())


    # this has a time complexity of O(m * n)
        