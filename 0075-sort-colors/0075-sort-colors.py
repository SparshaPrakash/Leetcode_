class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # [2, 0, 2, 1, 1, 0] l = 0, m = 0, h = 5
        # [0, 0, 2, 1, 1, 2] l = 0, m = 0, h = 4
        # [0, 0, 2, 1, 1, 2] l = 1, m = 1, h = 4
        # [0, 0, 2, 1, 1, 2] l = 2, m = 2, h = 4
        # [0, 0, 1, 1, 2, 2] l = 2, m = 2, h = 3
        # [0, 0, 1, 1, 2, 2] l = 2, m = 3, h = 3
        
        l, m, h = 0, 0, len(nums) - 1
        
        while m <= h:
            if nums[m] == 0:
                nums[l], nums[m] = nums[m], nums[l]
                l += 1
                m += 1
            elif nums[m] == 1:
                m += 1
            else:  # a[m] = 2
                nums[m], nums[h] = nums[h], nums[m]
                h -= 1
                