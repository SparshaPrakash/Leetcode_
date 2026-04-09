import heapq
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies O(N)
        count = Counter(nums)
        
        # Step 2: Build the heap O(N log K)
        heap = []
        
        for num, freq in count.items():
            # We push a tuple: (frequency, number)
            # Python heaps order by the first element of the tuple
            heapq.heappush(heap, (freq, num))
            
            # If the heap exceeds size k, remove the smallest frequency
            if len(heap) > k:
                heapq.heappop(heap)
        
        # Step 3: Extract the numbers from the heap O(K log K)
        # The heap contains (freq, num), we just want the num
        return [pair[1] for pair in heap]