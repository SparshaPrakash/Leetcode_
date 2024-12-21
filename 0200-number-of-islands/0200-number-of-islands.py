class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()

                # Neighbor directions: up, down, left, right
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (
                        nr in range(rows)
                        and nc in range(cols)
                        and grid[nr][nc] == "1"
                        and (nr, nc) not in visited
                    ):
                        q.append((nr, nc))
                        visited.add((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands

## DFS Solution

# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid:
#             return 0

#         rows, cols = len(grid), len(grid[0])
#         visited = set()
#         islands = 0

#         def dfs(r, c):
#      
#             if (
#                 r not in range(rows) or
#                 c not in range(cols) or
#                 (r, c) in visited or
#                 grid[r][c] == "0"
#             ):
#                 return

#            
#             visited.add((r, c))

#            
#             directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#             for dr, dc in directions:
#                 dfs(r + dr, c + dc)

#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == "1" and (r, c) not in visited:
#                     
#                     dfs(r, c)
#                     islands += 1

#         return islands

