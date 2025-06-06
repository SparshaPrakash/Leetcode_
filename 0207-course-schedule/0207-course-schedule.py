class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # mapping each coourse to  its prerequisites
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # getting all courses along the dfs path
        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False   # cannot be completed
            if preMap[crs] == []:
                return True # it doesnt have any prereq

            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visitSet.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):   # for courses that are not connected in the graph
            if not dfs(crs): return False

        return True

       

        