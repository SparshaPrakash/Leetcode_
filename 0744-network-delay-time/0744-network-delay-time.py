class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)

        # creating an adjacency list
        for u, v, w in times:
            edges[u].append((v,w))

        # initializing min heap with the source value and its weight
        minHeap = [(0, k)]
        visited = set()
        res = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)

            res = max(res, w1)

            # for neighbours of n1
            for n2, w2 in edges[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w2 + w1, n2))

        return res if len(visited) == n else -1 

        