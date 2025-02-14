class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or not grid[r][c]  or (r, c) in visited):
                return 0

            visited.add((r,c))
            res = 1  # we know that we initially passed a grid value that was 1, so the res will atleats be 1
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                res += dfs(r + dr, c + dc)
            return res

        visited = set()
        land, borderLand = 0, 0
        for r in range(ROWS):
            for c in range(COLS):
                land += grid[r][c] # only adding 1 will make a difference, adding a 0 wont make a difference anyway
                if (grid[r][c] and (r,c) not in visited and (c in [0, COLS - 1] or r in [0, ROWS - 1])):
                    borderLand += dfs(r, c)

        return land - borderLand

        