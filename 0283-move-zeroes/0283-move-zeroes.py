class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insert_pos = 0

        # moving non zero element foeard
        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1

        # filling in the rest with 0
        for i in range(insert_pos, len(nums)):
            nums[i] = 0
        