class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # adjacency list
        preMap = { c : [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # Visited- course has been added to the output
        # Visiting- course not added to the output, but added to the solution
        # Unvisited- cpurse not added to the output or to the cycle

        output = []
        visited, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True

            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)

            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return output




        