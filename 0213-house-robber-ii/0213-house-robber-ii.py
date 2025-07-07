class Solution:
    def rob(self, nums: List[int]) -> int:
        # use helper funtion
        # pass parameters with first element included but not the last one
        # do the same for forts element not inlcuded but last one included
        # in ecah, check whats the max one an rob
        # rob 1, rob2, n, n + 1, n + 2
        # max of rob 1 + n or rob 2
        if len(nums) == 1:
            return nums[0]

        return max(self.helper(nums[1:]), self.helper(nums[:-1]))


    def helper(self, nums):
        rob1, rob2 = 0, 0

        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob

        return rob2
        