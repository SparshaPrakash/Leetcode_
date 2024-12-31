import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * i for i in stones]
        heapq.heapify(stones)
        while True:
            if len(stones) == 0:
                return 0
            if len(stones) == 1:
                return -1 * stones[0]

            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            z = -1 * abs(x - y)
            if z != 0:
                heapq.heappush(stones, z)


        