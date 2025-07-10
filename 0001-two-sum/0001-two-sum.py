class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, n in enumerate(nums):
            compliment = target - n
            if compliment in hashMap:
                return [i, hashMap[compliment]]

            hashMap[n] = i

        return []
        