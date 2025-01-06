class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {} # creating a hash map to store the last index of a char

        for i, c in enumerate(s):
            lastIndex[c] = i

        res = []
        size, end = 0, 0
        for i, c in enumerate(s):
            size +=1 
            end = max(end, lastIndex[c])  

            if i == end:
                res.append(size)
                size = 0 # reset the partition soze to 0 after fdining the prev partiotion's szie

        return res
        