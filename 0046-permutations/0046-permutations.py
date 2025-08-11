class Solution:
    def permute(self, nums):
        res = []

        def backtrack(start):
            # Base case: all positions fixed → store a copy
            if start == len(nums):
                res.append(nums[:])
                return

            for i in range(start, len(nums)):
                # 1️⃣ Swap the element at "start" with the one at "i"
                nums[start], nums[i] = nums[i], nums[start]

                # 2️⃣ Recurse to fix the next position
                backtrack(start + 1)

                # 3️⃣ Swap back to restore the original order
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return res
