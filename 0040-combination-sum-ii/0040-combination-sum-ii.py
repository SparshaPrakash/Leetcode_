class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def backtrack(i, cur, target):
            if target == 0:
                res.append(cur.copy())
                return
            if target <= 0:
                return

            prev = -1    
            for n in range(i, len(candidates)):
                if candidates[n] == prev:
                    continue
                cur.append(candidates[n])
                backtrack(n + 1, cur, target - candidates[n])
                cur.pop()
                prev = candidates[n]

        backtrack(0, [], target)
        return res
