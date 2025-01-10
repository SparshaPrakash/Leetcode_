class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0 # this would be a good default value isnce n ^ (XOR) 0 = n

        for n in nums:
            res = n ^ res
        return res