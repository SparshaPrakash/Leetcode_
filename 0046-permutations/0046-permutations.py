class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, cur = [], []

        def dfs():
            if len(cur) == n: 
                res.append(cur.copy())
                return

            for i in nums:
                if i not in cur:
                    cur.append(i)
                    dfs()
                    cur.pop()

        dfs()
        return res
                    
            

        