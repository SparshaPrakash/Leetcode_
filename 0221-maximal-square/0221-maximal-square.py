from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # Get dimensions
        ROWS, COLS = len(matrix), len(matrix[0])
        # Memoization dictionary to store (r, c) → max square length
        cache = {}

        def helper(r, c):
            # If we're out of bounds, return 0 (base case)
            if r >= ROWS or c >= COLS:
                return 0

            # If already computed, return cached result
            if (r, c) in cache:
                return cache[(r, c)]

            # Recursively compute square size from neighbors
            down = helper(r + 1, c)
            right = helper(r, c + 1)
            diag = helper(r + 1, c + 1)

            # If current cell is '1', compute square size
            if matrix[r][c] == "1":
                cache[(r, c)] = 1 + min(down, right, diag)
            else:
                cache[(r, c)] = 0

            return cache[(r, c)]

        # Start from top-left corner
        helper(0, 0)

        # Find the largest square length from cache and return area
        return max(cache.values(), default=0) ** 2
