class Solution:
    def minFallingPathSum(self, matrix):
        """
        Find the minimum falling path sum for a given matrix using a bottom-up approach with O(n) space.

        :param matrix: List[List[int]] - a square matrix of integers
        :return: int - the minimum falling path sum
        """
        # recursive solution
        N = len(matrix)
        cache = {}
        
        def dfs(r, c):
            if r == N:
                return 0
            if c < 0 or c == N:
                return float("inf")   # retrunign a huge number so its going to not add any value in the minimum sum path
            if (r, c) in cache:
                return cache[(r, c)]

            res = matrix[r][c] + min(dfs(r + 1, c), dfs(r + 1, c - 1), dfs(r + 1, c + 1))

            cache[(r, c)] = res

            return res


        res = float("inf")
        for c in range(N):
            res = min(res, dfs(0, c))
        return res