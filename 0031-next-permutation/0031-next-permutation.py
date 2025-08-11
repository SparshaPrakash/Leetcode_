class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2

        #  Find pivot (first index from right where nums[i] < nums[i+1])
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1

        #  If pivot exists, find successor and swap
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]  # swap pivot and successor

        #  Reverse suffix starting at i+1
        l, r = i + 1, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
