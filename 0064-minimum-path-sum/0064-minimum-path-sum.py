from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        # Create a (ROWS+1) x (COLS+1) DP table initialized with infinity
        res = [[float("inf")] * (COLS + 1) for _ in range(ROWS + 1)]
        
        # Base case: set the cell just outside the bottom-right corner to 0
        res[ROWS][COLS - 1] = 0
        
        # Fill the DP table from bottom-right to top-left
        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                res[r][c] = grid[r][c] + min(res[r + 1][c], res[r][c + 1])
        
        return res[0][0]
