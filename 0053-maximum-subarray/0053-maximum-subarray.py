class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum_array = [nums[0]]
        max_seen = nums[0]
        
        for num in nums[1:]:
            best_sum_at_pos = max(num, max_sum_array[-1] + num)
            if best_sum_at_pos > max_seen:
                max_seen = best_sum_at_pos
            max_sum_array.append(best_sum_at_pos)
            
        return max_seen