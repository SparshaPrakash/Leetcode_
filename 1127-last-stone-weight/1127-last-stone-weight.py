class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones] 
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)  # heaviest stone
            second = heapq.heappop(stones)
            if second > first:   # it owuld actually have to be if forst > secons, but since we added a neg sign, we check second > first
                heapq.heappush(stones, first - second)
        
        stones.append(0)  # if there is no stoone left
        return abs(stones[0])

        