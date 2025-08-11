class Solution:
    def permute(self, nums):
        res = []  # To store all permutations

        def backtrack(start):
            # If we've fixed positions for all numbers, record the permutation
            if start == len(nums):
                res.append(nums[:])  # make a copy
                return
            
            for i in range(start, len(nums)):
                # Swap the current element with the start position
                nums[start], nums[i] = nums[i], nums[start]
                
                # Recurse on the rest
                backtrack(start + 1)
                
                # Undo the swap (backtrack)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return res
