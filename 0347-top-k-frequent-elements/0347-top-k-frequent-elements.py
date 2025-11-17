from collections import defaultdict

class Solution:
    def topKFrequent(self, nums, k):
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        # buckets[index] = list of numbers with frequency = index
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, f in freq.items():
            buckets[f].append(num)

        res = []
        # iterate frequencies from high to low
        for f in range(len(nums), 0, -1):
            for num in buckets[f]:
                res.append(num)
                if len(res) == k:
                    return res
