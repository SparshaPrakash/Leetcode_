from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0

        for n in nums:
            if count == 0:
                res = n
            if n == res:
                count += 1
            else:
                count -= 1

        # Optional: Double-check if 'res' is truly the majority
        # count = sum(1 for num in nums if num == res)
        # if count > len(nums) // 2:
        #     return res
        # else:
        #     return -1

        return res

        
        