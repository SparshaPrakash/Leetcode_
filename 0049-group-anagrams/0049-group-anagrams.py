from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # defaultdict prevents KeyError if the key doesn't exist yet
        anagram_map = defaultdict(list)

        for s in strs:
            # Sort the string to create a 'signature'
            # sorted("eat") returns ['a', 'e', 't'], so we join it into a string
            sorted_s = "".join(sorted(s))
            
            # Add the original string to the list corresponding to that signature
            anagram_map[sorted_s].append(s)

        # Return just the values (the groups of anagrams)
        return list(anagram_map.values())