class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, n in enumerate(nums):
            compliment = target - n
            if compliment in hashmap:
                return ([i, hashmap[compliment]])

            hashmap[n] = i

        return []
        
        