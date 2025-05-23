class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)  # -> adding the top level where we have to get to

        for i in range(len(cost) - 3, -1, -1):
            cost[i] = min(cost[i] + cost[i + 1], cost[i]+ cost[i + 2])   # for each elemeny, we check how much it costs, to take one step from it and taking two steps from it to reach the top

        return min(cost[0], cost[1])