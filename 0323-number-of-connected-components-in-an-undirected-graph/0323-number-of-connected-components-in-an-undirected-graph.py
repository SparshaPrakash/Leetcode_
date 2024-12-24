class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n


        def find(n1):
            res = n1

            while res != par[res]: # until the result is not the parent of itself
                par[res] = par[par[res]] # path compression
                res = par[res]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0 # not perfoming any union operation

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return 1 # did perform a union operation

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)

        return res

# Using DFS

# class Solution:
#     def countComponents(self, n: int, edges: List[List[int]]) -> int:
#         adj = [[] for _ in range(n)]
#         visit = [False] * n
#         for u, v in edges:
#             adj[u].append(v)
#             adj[v].append(u)

#         def dfs(node):
#             for nei in adj[node]:
#                 if not visit[nei]:
#                     visit[nei] = True
#                     dfs(nei)
        
#         res = 0
#         for node in range(n):
#             if not visit[node]:
#                 visit[node] = True
#                 dfs(node)
#                 res += 1
#         return res

        