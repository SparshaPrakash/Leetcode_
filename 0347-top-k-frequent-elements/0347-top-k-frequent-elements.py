import heapq
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count frequencies: {number: count}
        count = Counter(nums)
        
        # 2. Return the top k elements
        return heapq.nlargest(k, count.keys(), key=count.get)