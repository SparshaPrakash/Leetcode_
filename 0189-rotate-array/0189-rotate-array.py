from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(l: int, r: int) -> None:
            """Helper function to reverse nums between l and r."""
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1

        # Step 1: Handle k greater than length of nums
        k = k % len(nums)

        # Step 2: Reverse the entire array
        reverse(0, len(nums) - 1)

        # Step 3: Reverse the first k elements
        reverse(0, k - 1)

        # Step 4: Reverse the rest of the array
        reverse(k, len(nums) - 1)
