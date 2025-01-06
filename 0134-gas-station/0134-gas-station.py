class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1

        current_gas = 0
        start_city = 0

        for i in range(len(cost) - 1):
            current_gas += gas[i] - cost[i]
            if current_gas < 0:
                current_gas = 0
                start_city = i + 1
                continue

        return start_city

            

            

            
                

        