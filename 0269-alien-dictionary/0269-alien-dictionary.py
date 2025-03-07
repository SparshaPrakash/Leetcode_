class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # check the first 2 words -> check the first letter, add it to the graph, check the next to and add it according to the lexicographical order

        # wrt; wrf
        # compare w and w -> add w
        # compare r and r -> add r -> w, r
        # comapre t and f -> add them in order -> w, r, t, f
        
        adj = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            minLen = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visited = {}
        res = []

        # post order dfs

        def dfs(c):

            if c in visited:
                return visited[c]
            visited[c] = True

            for nei in adj[c]:
                if dfs(nei):
                    return True

            visited[c] = False
            res.append(c)

        for c in adj:
            if dfs(c):
                return ""

        res.reverse()
        return "".join(res)


        