class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        to_be_used = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            for i, v in enumerate(t):
                if v == target[i]:
                    to_be_used.add(i)

        return len(to_be_used) == 3