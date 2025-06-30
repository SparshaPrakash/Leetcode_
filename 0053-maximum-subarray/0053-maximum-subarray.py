class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = 0

        for i in nums:
            cur_sum = max(cur_sum + i, i)
            max_sum = max(max_sum, cur_sum)

        return max_sum
        
           
        
        