class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        values = {}
        for i in nums:
            if i in values:
                return True

            values[i] = True

        return False
        