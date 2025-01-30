class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = len(nums) - 2  # inversion point
        
        if k <= -1:
            return nums
        
        while k >= 0 and nums[k] >= nums[k + 1]:
            k -= 1
            
        if k == -1:
            nums.sort()
            return
        
        for i in range(len(nums) - 1, k, -1):
            if nums[i] > nums[k]:
                nums[i], nums[k] = nums[k], nums[i]
                break
        
        i = k + 1
        j = len(nums) - 1
        
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1