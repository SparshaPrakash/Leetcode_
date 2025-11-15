class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = {}

        for i in nums:
            if i in n:
                return True

            n[i] = True

        return False