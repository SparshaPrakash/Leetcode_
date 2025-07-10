from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for word in strs:
            lst = [0] * 26  # List to count frequency of each letter a-z
            for char in word:
                lst[ord(char) - ord('a')] += 1  # Map 'a' to 0, 'b' to 1, etc.

            lst = tuple(lst)  # Tuples can be used as dictionary keys
            dic[lst].append(word)

        return list(dic.values())  # Convert dict_values to list of lists
