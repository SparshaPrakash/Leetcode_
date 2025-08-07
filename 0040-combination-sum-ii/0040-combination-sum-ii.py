class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        res = []

        def dfs(cur, start, target):
            if target == 0:
                res.append(cur.copy())
                return


            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i -1]:
                    continue
                if candidates[i] > target:
                    break
                
                cur.append(candidates[i])
                dfs(cur, i + 1, target - candidates[i])
                cur.pop()

        dfs([], 0, target)
        return res
        