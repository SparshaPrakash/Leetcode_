class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def comb(cur, k, n, start):
            if k == 0 and n == 0:
                result.append(cur)
                return
            if k <= 0:
                return

            for i in range(start, min(10, n + 1)):
                comb(cur + [i], k - 1, n - i, i + 1)
            return

        comb([], k, n, 1)

        return result

        