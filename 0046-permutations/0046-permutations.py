class Solution:
    def permute(self, nums):
        res, path = [], []
        used = [False] * len(nums)

        def dfs():
            if len(path) == len(nums):
                res.append(path[:])  # copy the built permutation
                return
            for i in range(len(nums)):
                if used[i]: 
                    continue
                used[i] = True
                path.append(nums[i])
                dfs()
                path.pop()
                used[i] = False

        dfs()
        return res
